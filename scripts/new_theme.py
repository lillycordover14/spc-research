#!/usr/bin/env python3
"""Start a new vertical:  python3 scripts/new_theme.py energy "Energy & the AI power bottleneck" [--short en]
Copies themes/_template -> themes/<slug>, fills theme.yml. Then edit taxonomy.yml (layers!) and watchlist/*.yml."""
import shutil, sys, re, datetime as dt
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    a = [x for x in sys.argv[1:]]
    short = None
    if "--short" in a:
        i = a.index("--short"); short = a[i + 1]; del a[i:i + 2]
    if len(a) < 2: raise SystemExit(__doc__)
    slug, name = re.sub(r"[^a-z0-9-]", "-", a[0].lower()), a[1]
    dst = ROOT / "themes" / slug
    if dst.exists(): raise SystemExit(f"exists: {dst}")
    shutil.copytree(ROOT / "themes" / "_template", dst)
    ty = dst / "theme.yml"
    ty.write_text(ty.read_text().replace("{{slug}}", slug).replace("{{name}}", name).replace("{{short}}", short or slug[:6]).replace("{{today}}", dt.date.today().isoformat()))
    for f in dst.rglob("*.md"):
        f.write_text(f.read_text().replace("{{name}}", name).replace("{{slug}}", slug))
    print(f"created themes/{slug}/ — next: edit themes/{slug}/taxonomy.yml layers, watchlist/*.yml, insights/thesis.md; then `make index THEME={slug}`")

if __name__ == "__main__":
    main()
