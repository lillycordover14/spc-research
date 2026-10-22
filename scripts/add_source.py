#!/usr/bin/env python3
"""
The one-call way for an agent (GrokBot / Claude) to add a source record without touching YAML by hand.

  python3 scripts/add_source.py record.json            # or:  cat record.json | python3 scripts/add_source.py -
  python3 scripts/add_source.py --theme anip record.json

record.json (only `type` and `title` are required; everything else optional):
{
  "type": "article",                 // alphasense | expert-call | market-research | article | podcast | website | filing | dataset | other
  "title": "1872 launches autonomous steel fabrication factory",
  "date": "2026-07-22",
  "url": "https://www.businesswire.com/...",
  "publisher": "BusinessWire",
  "author": null,
  "speakers": [],                     // calls/podcasts: [{"name","role","affiliation"}]
  "expert_background": null,          // expert calls: one line (first bullet of any summary)
  "companies": ["1872"],              // slugs; unknown slugs are created as status=candidate stubs
  "people": [],
  "layers": ["fabrication"],
  "tags": ["steel", "funding"],
  "summary": "3-6 lines ...",
  "key_facts": [{"fact": "$15M seed", "quote": "...", "where": "para 1"}],
  "takeaways": ["..."],
  "confidence": "high",
  "status": "summarized",             // unread | summarized | reviewed
  "added_by": "grokbot",
  "body": "full text / transcript (verbatim)"
}
Prints the path written. Dedupes on sha256(body) and on url. Exit 0 with 'dup:' prefix when already present.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from common import SOURCES, COMPANIES, SOURCE_TYPES, type_dir, read_fm, write_fm, sha256_text, make_id, today, iter_md, rel, slugify

def add_record(rec: dict, quiet: bool = False):
    """Write one source record. Returns the path written, or None if it was a duplicate."""
    say = (lambda *a: None) if quiet else print
    stype = rec.get("type")
    if stype not in SOURCE_TYPES: raise SystemExit(f"type must be one of {SOURCE_TYPES}")
    if not rec.get("title"): raise SystemExit("title required")
    body = (rec.get("body") or "").strip()
    url = rec.get("url")
    digest = sha256_text(body if body else f"{url or ''}|{rec['title']}")
    # dedupe
    for p in iter_md(SOURCES):
        fm, _ = read_fm(p)
        if fm.get("hash") == digest or (url and fm.get("url") == url):
            say(f"dup: {rel(p)}"); return None
    sid = make_id(digest, rec.get("date"))
    # company stubs for unknown slugs
    for slug in rec.get("companies") or []:
        cp = COMPANIES / f"{slug}.md"
        if not cp.exists():
            write_fm(cp, {"slug": slug, "name": rec.get("company_names", {}).get(slug, slug.replace("-", " ").title()), "aliases": [], "website": None, "hq": None,
                          "founded": None, "layer": "adjacent", "layers": [], "model": "owner-operator", "what": "", "fit": [], "stage": "unknown",
                          "total_raised_usd": None, "last_round": {}, "investors": [], "founders": [], "headcount": None, "customers": [],
                          "harmonic_urn": None, "affinity_id": None, "pitchbook": None, "status": "candidate", "spc_owner": "Lilly", "tags": [],
                          "sources": [sid], "data_quality": f"auto-created stub from {sid}; fill layer/model/what", "updated": today()},
                     "\n## What they do\n\n## Why it fits the theme (or doesn't)\n\n## Traction and signals\n\n## Economics (what we know)\n\n## Open questions\n\n## People\n")
            say(f"  + stub {rel(cp)}")
        else:
            fm, b = read_fm(cp)
            if sid not in (fm.get("sources") or []):
                fm["sources"] = (fm.get("sources") or []) + [sid]; write_fm(cp, fm, b)
    fm = {"id": sid, "type": stype, "title": rec["title"].strip(), "date": rec.get("date"), "added": today(), "url": url,
          "publisher": rec.get("publisher"), "author": rec.get("author"), "speakers": rec.get("speakers") or [],
          "expert_background": rec.get("expert_background"), "companies": rec.get("companies") or [], "people": rec.get("people") or [],
          "layers": rec.get("layers") or [], "tags": rec.get("tags") or [], "summary": rec.get("summary") or "",
          "key_facts": rec.get("key_facts") or [], "takeaways": rec.get("takeaways") or [], "confidence": rec.get("confidence") or "med",
          "raw_file": rec.get("raw_file"), "hash": digest, "word_count": len(body.split()),
          "status": rec.get("status") or ("summarized" if rec.get("summary") else "unread"), "added_by": rec.get("added_by") or "agent"}
    out = SOURCES / type_dir(stype) / f"{sid}.md"
    write_fm(out, fm, "\n" + (body or "[no body captured — see url]") + "\n")
    say(rel(out)); return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    raw = sys.stdin.read() if (not args or args[0] == "-") else Path(args[0]).read_text()
    add_record(json.loads(raw))

if __name__ == "__main__":
    main()
