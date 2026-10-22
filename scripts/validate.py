#!/usr/bin/env python3
"""Check every frontmatter against schema/*.json + taxonomy.yml enums. Exit 1 on errors. Run before committing."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
from common import ROOT, T, INDEX, COMPANIES, SOURCES, PEOPLE, TAXONOMY, read_fm, iter_md, rel, today

def enum(name):
    v = TAXONOMY[name]
    return list(v.keys()) if isinstance(v, dict) else list(v)

def check(fm: dict, schema: dict, path: Path, errs: list):
    rel_ = rel(path)
    for k in schema["required"]:
        if k not in fm or fm[k] in (None, ""):
            errs.append(f"{rel_}: missing required '{k}'")
    for k, spec in schema["properties"].items():
        if k not in fm or fm[k] is None: continue
        val = fm[k]
        if "enum_from" in spec:
            allowed = enum(spec["enum_from"])
            vals = val if isinstance(val, list) else [val]
            for v in vals:
                if v not in allowed: errs.append(f"{rel_}: {k}='{v}' not in taxonomy.{spec['enum_from']} {allowed}")
        if "pattern" in spec and isinstance(val, str) and not re.fullmatch(spec["pattern"], val):
            errs.append(f"{rel_}: {k}='{val}' does not match {spec['pattern']}")
        t = spec.get("type")
        if t == "array" and not isinstance(val, list): errs.append(f"{rel_}: {k} should be a list")

def main():
    errs = []
    for folder, schema in ((COMPANIES, "company"), (SOURCES, "source"), (PEOPLE, "person")):
        sch = json.loads((ROOT / "schema" / f"{schema}.schema.json").read_text())
        for p in iter_md(folder):
            fm, _ = read_fm(p)
            if not fm: errs.append(f"{rel(p)}: no frontmatter"); continue
            check(fm, sch, p, errs)
    # cross-refs: sources[].companies must exist
    slugs = {read_fm(p)[0].get("slug") for p in iter_md(COMPANIES)}
    for p in iter_md(SOURCES):
        fm, _ = read_fm(p)
        for c in fm.get("companies") or []:
            if c not in slugs: errs.append(f"{rel(p)}: companies -> '{c}' has no companies/{c}.md (make new-company name=...)")
    INDEX.mkdir(exist_ok=True)
    report = INDEX / "VALIDATION.md"
    if errs:
        report.write_text(f"# Validation — {today()} — {len(errs)} problem(s)\n\nFix these, then push again. Rules: schema/*.json + taxonomy.yml.\n\n" + "\n".join(f"- {e}" for e in errs) + "\n")
        print("\n".join(errs)); print(f"\n{len(errs)} problem(s) -> {rel(report)}"); sys.exit(1)
    report.write_text(f"# Validation — {today()}\n\nAll records valid.\n")
    print("all frontmatter valid")

if __name__ == "__main__":
    main()
