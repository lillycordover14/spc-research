#!/usr/bin/env python3
"""Scaffold a record from templates/.
  python3 scripts/new.py company "Nox Metals"
  python3 scripts/new.py source "Call with ex-Hadrian ops lead" --type expert-call
  python3 scripts/new.py person "Chris Power"
"""
import argparse, sys
from pathlib import Path
from common import ROOT, T, COMPANIES, PEOPLE, SOURCES, slugify, today, make_id, sha256_text, SOURCE_TYPES, type_dir, rel

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["company", "source", "person"])
    ap.add_argument("name")
    ap.add_argument("--type", default="other")
    a = ap.parse_args()
    if a.kind == "company":
        slug = slugify(a.name); out = COMPANIES / f"{slug}.md"; tpl = "company.md"
    elif a.kind == "person":
        slug = slugify(a.name); out = PEOPLE / f"{slug}.md"; tpl = "person.md"
    else:
        if a.type not in SOURCE_TYPES: raise SystemExit(f"--type must be one of {SOURCE_TYPES}")
        sid = make_id(sha256_text(a.name + today()))
        out = SOURCES / type_dir(a.type) / f"{sid}.md"
        tpl = "expert-call.md" if a.type == "expert-call" else "source.md"
        slug = sid
    if out.exists(): raise SystemExit(f"exists: {rel(out)}")
    text = (ROOT / "templates" / tpl).read_text()
    text = text.replace("{{slug}}", slug).replace("{{name}}", a.name).replace("{{title}}", a.name) \
               .replace("{{today}}", today()).replace("{{id}}", slug).replace("{{type}}", a.type)
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text)
    print(rel(out))

if __name__ == "__main__":
    main()
