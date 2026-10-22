#!/usr/bin/env python3
"""
Normalize everything dropped in inbox/ into sources/<type>/<id>.md (+ original kept in raw/).

Usage:
  python3 scripts/ingest.py [--theme <slug>]     # process themes/<slug>/inbox/, infer type from subfolder or filename
  python3 scripts/ingest.py --type alphasense    # force a type for everything in inbox/
  python3 scripts/ingest.py path/to/file.pdf --type expert-call --title "..." --date 2026-10-20 --companies hadrian,1872

Conventions that make inference work (any of them):
  inbox/alphasense/*.pdf            -> type alphasense
  inbox/expert-calls/*.txt          -> type expert-call
  inbox/podcasts/*.vtt|srt|txt      -> type podcast
  a filename prefix like  "article__Modern Machine Shop__2026-10-01__title.html"  -> type / publisher / date parsed from "__"

Handles: .pdf .docx .html/.htm .txt .md .vtt .srt .json(AlphaSense export) .csv (stored as dataset, no text extraction)
Dedupes on sha256 of the original file. Never deletes: originals move to raw/<type>/.
"""
from __future__ import annotations
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path
from common import ROOT, T, INBOX, RAW, SOURCES, SOURCE_TYPES, type_dir, read_fm, write_fm, sha256_file, make_id, today, slugify, existing_hashes, rel

SRC = SOURCES
TYPE_ALIASES = {"expert-calls": "expert-call", "calls": "expert-call", "transcripts": "alphasense",
                "research": "market-research", "reports": "market-research", "news": "article",
                "articles": "article", "podcasts": "podcast", "sites": "website", "websites": "website",
                "filings": "filing", "datasets": "dataset", "data": "dataset"}

def norm_type(t: str | None) -> str | None:
    if not t: return None
    t = t.strip().lower()
    t = TYPE_ALIASES.get(t, t)
    return t if t in SOURCE_TYPES else None

# ---------- text extraction ----------
def pdf_text(p: Path) -> str:
    try:
        out = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=120)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout
    except Exception:
        pass
    try:
        from pypdf import PdfReader
        return "\n\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
    except Exception as e:
        return f"[pdf text extraction failed: {e}]"

def docx_text(p: Path) -> str:
    try:
        import docx
        d = docx.Document(str(p))
        parts = [para.text for para in d.paragraphs]
        for t in d.tables:
            for row in t.rows:
                parts.append(" | ".join(c.text.strip() for c in row.cells))
        return "\n".join(parts)
    except Exception as e:
        try:
            return subprocess.run(["pandoc", str(p), "-t", "plain"], capture_output=True, text=True, timeout=120).stdout
        except Exception:
            return f"[docx extraction failed: {e}]"

def html_text(p: Path) -> tuple[str, str | None]:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(p.read_text(encoding="utf-8", errors="replace"), "html.parser")
    for t in soup(["script", "style", "nav", "footer", "header", "noscript", "svg"]):
        t.decompose()
    title = soup.title.string.strip() if soup.title and soup.title.string else None
    main = soup.find("article") or soup.find("main") or soup.body or soup
    text = re.sub(r"\n{3,}", "\n\n", main.get_text("\n"))
    return text.strip(), title

def vtt_text(p: Path) -> str:
    lines = []
    for ln in p.read_text(encoding="utf-8", errors="replace").splitlines():
        s = ln.strip()
        if not s or s == "WEBVTT" or s.isdigit() or "-->" in s or s.startswith(("NOTE", "STYLE")):
            continue
        lines.append(re.sub(r"<[^>]+>", "", s))
    # collapse exact consecutive duplicates (common in auto-captions)
    out = [l for i, l in enumerate(lines) if i == 0 or l != lines[i-1]]
    return "\n".join(out)

def json_text(p: Path) -> tuple[str, dict]:
    """AlphaSense / generic exports: pull obvious fields, dump the rest as text."""
    data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    meta = {}
    if isinstance(data, dict):
        for k in ("title", "date", "url", "publisher", "speakers", "expert_background", "summary"):
            if k in data: meta[k] = data[k]
        body = data.get("transcript") or data.get("text") or data.get("content") or data.get("body")
        if isinstance(body, list):
            body = "\n".join((f"{x.get('speaker','')}: {x.get('text','')}" if isinstance(x, dict) else str(x)) for x in body)
        if body: return str(body), meta
    return json.dumps(data, indent=1), meta

def extract(p: Path) -> tuple[str, dict]:
    ext = p.suffix.lower()
    meta: dict = {}
    if ext == ".pdf": return pdf_text(p), meta
    if ext == ".docx": return docx_text(p), meta
    if ext in (".html", ".htm"):
        t, title = html_text(p); meta["title"] = title; return t, meta
    if ext in (".vtt", ".srt"): return vtt_text(p), meta
    if ext == ".json": return json_text(p)
    if ext in (".txt", ".md", ".text"):
        return p.read_text(encoding="utf-8", errors="replace"), meta
    if ext in (".csv", ".xlsx", ".xls", ".parquet"):
        return f"[structured data, {p.stat().st_size} bytes — see raw_file]", {"type": "dataset"}
    if ext in (".mp3", ".m4a", ".wav", ".mp4"):
        return "[audio/video — transcribe with scripts/transcribe.md (whisper), then re-ingest the .txt]", {"type": "podcast"}
    return p.read_text(encoding="utf-8", errors="replace"), meta

# ---------- filename conventions ----------
def parse_name(p: Path) -> dict:
    """ 'type__publisher__YYYY-MM-DD__title.ext' -> dict; tolerant of missing pieces."""
    stem = p.stem
    out: dict = {"title": stem}
    parts = stem.split("__")
    if len(parts) >= 2:
        t = norm_type(parts[0])
        if t: out["type"] = t; parts = parts[1:]
        for seg in parts[:-1]:
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", seg): out["date"] = seg
            else: out["publisher"] = seg
        out["title"] = parts[-1]
    m = re.search(r"(\d{4}-\d{2}-\d{2})", stem)
    if m and "date" not in out: out["date"] = m.group(1)
    return out

def guess_type(p: Path, forced: str | None, meta: dict) -> str:
    if forced: return forced
    if p.parent != INBOX:
        t = norm_type(p.parent.name)
        if t: return t
    if meta.get("type"): return meta["type"]
    n = parse_name(p)
    if n.get("type"): return n["type"]
    s = p.name.lower()
    if "alphasense" in s or "tegus" in s or "transcript" in s: return "alphasense"
    if "call" in s or "granola" in s: return "expert-call"
    if p.suffix.lower() in (".vtt", ".srt"): return "podcast"
    if p.suffix.lower() in (".html", ".htm"): return "article"
    if p.suffix.lower() in (".csv", ".xlsx"): return "dataset"
    return "other"

def ingest_file(p: Path, forced_type: str | None, args) -> Path | None:
    if p.name.startswith(".") or p.name == ".gitkeep": return None
    digest = sha256_file(p)
    seen = existing_hashes()
    if digest in seen:
        print(f"  skip (dup of {rel(seen[digest])}): {p.name}"); return None
    text, meta = extract(p)
    stype = guess_type(p, forced_type, meta)
    named = parse_name(p)
    date = args.date or meta.get("date") or named.get("date")
    sid = make_id(digest, date)
    title = args.title or meta.get("title") or named.get("title") or p.stem
    # keep original
    raw_dir = RAW / type_dir(stype); raw_dir.mkdir(parents=True, exist_ok=True)
    raw_dest = raw_dir / f"{sid}__{p.name}"
    shutil.move(str(p), raw_dest)
    fm = {
        "id": sid, "type": stype, "title": str(title).strip(), "date": date, "added": today(),
        "url": args.url or meta.get("url"), "publisher": args.publisher or meta.get("publisher") or named.get("publisher"),
        "author": None, "speakers": meta.get("speakers", []), "expert_background": meta.get("expert_background"),
        "companies": [c for c in (args.companies or "").split(",") if c], "people": [],
        "layers": [l for l in (args.layers or "").split(",") if l], "tags": [],
        "summary": meta.get("summary") or "", "key_facts": [], "takeaways": [], "confidence": "med",
        "raw_file": rel(raw_dest), "hash": digest, "word_count": len(text.split()),
        "status": "unread", "added_by": "ingest.py",
    }
    out_dir = SRC / type_dir(stype); out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{sid}.md"
    write_fm(out, fm, "\n" + text.strip() + "\n")
    print(f"  + {rel(out)}  ({stype}, {fm['word_count']} words)")
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="files to ingest (default: everything in inbox/)")
    ap.add_argument("--type", dest="stype"); ap.add_argument("--title"); ap.add_argument("--date")
    ap.add_argument("--url"); ap.add_argument("--publisher"); ap.add_argument("--companies", help="comma-separated slugs")
    ap.add_argument("--layers", help="comma-separated layers")
    a = ap.parse_args()
    forced = norm_type(a.stype)
    if a.stype and not forced: raise SystemExit(f"unknown --type {a.stype}; use one of {SOURCE_TYPES}")
    files = [Path(x) for x in a.paths] if a.paths else [p for p in INBOX.rglob("*") if p.is_file() and not p.name.startswith(".")]
    if not files: print(f"{rel(INBOX)}/ is empty"); return
    print(f"ingesting {len(files)} file(s)")
    n = 0
    for p in files:
        if ingest_file(p, forced, a): n += 1
    print(f"done: {n} new source(s). Next: fill summary/companies/layers in the frontmatter (or let the agent), then `make index`.")

if __name__ == "__main__":
    main()
