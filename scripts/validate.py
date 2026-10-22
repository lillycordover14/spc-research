#!/usr/bin/env python3
"""Check every frontmatter against schema/*.json + taxonomy.yml enums. Exit 1 on errors. Run before committing."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
from common import ROOT, TAXONOMY, read_fm, iter_md

def enum(name):
    v = TAXONOMY[name]
    return list(v.keys()) if isinstance(v, dict) else list(v)

def check(fm: dict, schema: dict, path: Path, errs: list):
    rel = path.relative_to(ROOT)
    for k in schema["required"]:
        if k not in fm or fm[k] in (None, ""):
            errs.append(f"{rel}: missing required '{k}'")
    for k, spec in schema["properties"].items():
        if k not in fm or fm[k] is None: continue
        val = fm[k]
        if "enum_from" in spec:
            allowed = enum(spec["enum_from"])
            vals = val if isinstance(val, list) else [val]
            for v in vals:
                if v not in allowed: errs.append(f"{rel}: {k}='{v}' not in taxonomy.{spec['enum_from']} {allowed}")
        if "pattern" in spec and isinstance(val, str) and not re.fullmatch(spec["pattern"], val):
            errs.append(f"{rel}: {k}='{val}' does not match {spec['pattern']}")
        t = spec.get("type")
        if t == "array" and not isinstance(val, list): errs.append(f"{rel}: {k} should be a list")

def main():
    errs = []
    for folder, schema in (("companies", "company"), ("sources", "source"), ("people", "person")):
        sch = json.loads((ROOT / "schema" / f"{schema}.schema.json").read_text())
        for p in iter_md(ROOT / folder):
            fm, _ = read_fm(p)
            if not fm: errs.append(f"{p.relative_to(ROOT)}: no frontmatter"); continue
            check(fm, sch, p, errs)
    # cross-refs: sources[].companies must exist
    slugs = {read_fm(p)[0].get("slug") for p in iter_md(ROOT / "companies")}
    for p in iter_md(ROOT / "sources"):
        fm, _ = read_fm(p)
        for c in fm.get("companies") or []:
            if c not in slugs: errs.append(f"{p.relative_to(ROOT)}: companies -> '{c}' has no companies/{c}.md (make new-company name=...)")
    if errs:
        print("\n".join(errs)); print(f"\n{len(errs)} problem(s)"); sys.exit(1)
    print("all frontmatter valid")

if __name__ == "__main__":
    main()
