"""Shared helpers: repo + theme paths, frontmatter read/write, taxonomy, ids.

Every script works on ONE theme (vertical) at a time. The theme is resolved from, in order:
  --theme <slug>  (argv)   >   THEME env var   >   the only theme under themes/   >   error.
Shared things (schema/, templates/, scripts/) live at the repo root; everything else lives in themes/<slug>/.
"""
from __future__ import annotations
import hashlib, re, sys, os, datetime as dt
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "themes"

def _resolve_theme() -> Path:
    slug = None
    argv = sys.argv
    if "--theme" in argv:
        i = argv.index("--theme")
        if i + 1 < len(argv):
            slug = argv[i + 1]; del argv[i:i + 2]      # consume so argparse never sees it
    slug = slug or os.environ.get("THEME")
    if not slug:
        cands = [p for p in THEMES.iterdir() if p.is_dir() and not p.name.startswith("_") and (p / "theme.yml").exists()]
        if len(cands) == 1: return cands[0]
        raise SystemExit(f"which theme? pass --theme <slug> or set THEME. available: {[c.name for c in cands]}")
    # accept the short code too (theme.yml: short)
    for p in THEMES.iterdir():
        if not p.is_dir() or p.name.startswith("_") or not (p / "theme.yml").exists(): continue
        meta = yaml.safe_load((p / "theme.yml").read_text()) or {}
        if p.name == slug or meta.get("short") == slug: return p
    raise SystemExit(f"theme '{slug}' not found under themes/")

T = _resolve_theme()                                    # theme root
THEME_META = yaml.safe_load((T / "theme.yml").read_text()) or {}
TAXONOMY = yaml.safe_load((T / "taxonomy.yml").read_text())
SOURCE_TYPES = list(TAXONOMY["source_types"].keys())
TYPE_DIR = {"alphasense": "alphasense", "expert-call": "expert-calls", "market-research": "market-research", "article": "articles",
            "podcast": "podcasts", "website": "websites", "filing": "filings", "dataset": "datasets", "other": "other"}
def type_dir(t: str) -> str:
    return TYPE_DIR.get(t, t)

COMPANIES, SOURCES, PEOPLE = T / "companies", T / "sources", T / "people"
INBOX, RAW, INDEX, INSIGHTS, WATCHLIST = T / "inbox", T / "raw", T / "index", T / "insights", T / "watchlist"
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)

def today() -> str:
    return dt.date.today().isoformat()

def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))

def read_fm(path: Path):
    """Return (frontmatter dict, body str). Empty dict if no frontmatter."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        raise SystemExit(f"[yaml error] {path}: {e}")
    return fm, text[m.end():]

def write_fm(path: Path, fm: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    body = body if body.startswith("\n") else "\n" + body
    path.write_text(f"---\n{y}---\n{body}", encoding="utf-8")

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def make_id(digest: str, date: str | None = None) -> str:
    d = (date or today()).replace("-", "")[:8]
    if not re.fullmatch(r"\d{8}", d): d = today().replace("-", "")
    return f"src-{d}-{digest[:6]}"

def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "untitled"

def iter_md(folder: Path):
    if not folder.exists(): return
    for p in sorted(folder.rglob("*.md")):
        if p.name.startswith("_") or p.name == "README.md":
            continue
        yield p

def existing_hashes() -> dict:
    """hash -> source path, for dedupe."""
    out = {}
    for p in iter_md(SOURCES):
        fm, _ = read_fm(p)
        if fm.get("hash"):
            out[fm["hash"]] = p
    return out

def company_slugs() -> set:
    return {read_fm(p)[0].get("slug") for p in iter_md(COMPANIES)}
