"""Shared helpers: repo paths, frontmatter read/write, taxonomy, ids."""
from __future__ import annotations
import hashlib, re, sys, datetime as dt
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = yaml.safe_load((ROOT / "taxonomy.yml").read_text())
SOURCE_TYPES = list(TAXONOMY["source_types"].keys())
# folder name under sources/ and raw/ for each source type (plural where natural)
TYPE_DIR = {"alphasense": "alphasense", "expert-call": "expert-calls", "market-research": "market-research", "article": "articles",
            "podcast": "podcasts", "website": "websites", "filing": "filings", "dataset": "datasets", "other": "other"}
def type_dir(t: str) -> str:
    return TYPE_DIR.get(t, t)

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)

def today() -> str:
    return dt.date.today().isoformat()

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
    y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    path.write_text(f"---\n{y}---\n{body if body.startswith(chr(10)) else chr(10)+body}", encoding="utf-8")

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def make_id(digest: str, date: str | None = None) -> str:
    d = (date or today()).replace("-", "")
    return f"src-{d}-{digest[:6]}"

def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "untitled"

def iter_md(folder: Path):
    for p in sorted(folder.rglob("*.md")):
        if p.name.startswith("_") or p.name == "README.md":
            continue
        yield p

def existing_hashes() -> dict:
    """hash -> source path, for dedupe."""
    out = {}
    for p in iter_md(ROOT / "sources"):
        fm, _ = read_fm(p)
        if fm.get("hash"):
            out[fm["hash"]] = p
    return out
