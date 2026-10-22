#!/usr/bin/env python3
"""
Walk companies/, sources/, people/ -> write
  index/sources.jsonl      one line per source (frontmatter + first 600 chars of body)
  index/companies.csv      flat table for Excel / Harmonic / Affinity sync
  index/companies.jsonl
  index/people.jsonl
  index/anip.sqlite        tables + FTS5 full-text over every body (gitignored; rebuild anytime)
  index/STATS.md           counts by type / layer / status (committed so agents can read it)
"""
from __future__ import annotations
import csv, json, sqlite3, sys, collections
from pathlib import Path
from common import ROOT, read_fm, iter_md, today

IDX = ROOT / "index"; IDX.mkdir(exist_ok=True)

def load(folder: str, key: str):
    rows = []
    for p in iter_md(ROOT / folder):
        fm, body = read_fm(p)
        if not fm: continue
        fm["_path"] = str(p.relative_to(ROOT))
        fm["_body"] = body
        rows.append(fm)
    return rows

def main():
    sources, companies, people = load("sources", "id"), load("companies", "slug"), load("people", "slug")
    # sources.jsonl
    with (IDX / "sources.jsonl").open("w") as f:
        for s in sources:
            row = {k: v for k, v in s.items() if k != "_body"}
            row["excerpt"] = s["_body"].strip()[:600]
            f.write(json.dumps(row, default=str, ensure_ascii=False) + "\n")
    # companies
    cols = ["slug","name","layer","model","stage","status","hq","founded","headcount","total_raised_usd","website",
            "harmonic_urn","fit","tags","what","updated","_path"]
    with (IDX / "companies.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(cols)
        for c in sorted(companies, key=lambda x: (x.get("layer",""), x.get("name",""))):
            w.writerow([",".join(c[k]) if isinstance(c.get(k), list) else c.get(k, "") for k in cols])
    with (IDX / "companies.jsonl").open("w") as f:
        for c in companies:
            f.write(json.dumps({k: v for k, v in c.items() if k != "_body"}, default=str, ensure_ascii=False) + "\n")
    with (IDX / "people.jsonl").open("w") as f:
        for p in people:
            f.write(json.dumps({k: v for k, v in p.items() if k != "_body"}, default=str, ensure_ascii=False) + "\n")
    # sqlite + fts
    db = IDX / "anip.sqlite"
    if db.exists(): db.unlink()
    con = sqlite3.connect(db)
    con.executescript("""
      create table sources(id text primary key, type, title, date, added, publisher, url, companies, layers, tags, status, confidence, word_count, path, summary, body);
      create table companies(slug text primary key, name, layer, model, stage, status, hq, founded, headcount, total_raised_usd, website, harmonic_urn, fit, tags, what, updated, path, body);
      create table people(slug text primary key, name, role, affiliation, companies, why_track, path, body);
      create table mentions(source_id, company_slug);
      create virtual table fts using fts5(kind, key, title, body, tokenize='porter');
    """)
    for s in sources:
        j = lambda k: json.dumps(s.get(k, []), default=str)
        con.execute("insert or replace into sources values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (s.get("id"), s.get("type"), s.get("title"), str(s.get("date") or ""), str(s.get("added") or ""), s.get("publisher"), s.get("url"),
             j("companies"), j("layers"), j("tags"), s.get("status"), s.get("confidence"), s.get("word_count"), s["_path"],
             s.get("summary") or "", s["_body"]))
        for slug in s.get("companies") or []:
            con.execute("insert into mentions values (?,?)", (s.get("id"), slug))
        con.execute("insert into fts values (?,?,?,?)", ("source", s.get("id"), s.get("title"), (s.get("summary") or "") + "\n" + s["_body"]))
    for c in companies:
        con.execute("insert or replace into companies values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (c.get("slug"), c.get("name"), c.get("layer"), c.get("model"), c.get("stage"), c.get("status"), c.get("hq"),
             str(c.get("founded") or ""), c.get("headcount"), c.get("total_raised_usd"), c.get("website"), c.get("harmonic_urn"),
             json.dumps(c.get("fit", [])), json.dumps(c.get("tags", [])), c.get("what"), str(c.get("updated")), c["_path"], c["_body"]))
        con.execute("insert into fts values (?,?,?,?)", ("company", c.get("slug"), c.get("name"), (c.get("what") or "") + "\n" + c["_body"]))
    for p in people:
        con.execute("insert or replace into people values (?,?,?,?,?,?,?,?)",
            (p.get("slug"), p.get("name"), p.get("role"), p.get("affiliation"), json.dumps(p.get("companies", [])), p.get("why_track"), p["_path"], p["_body"]))
        con.execute("insert into fts values (?,?,?,?)", ("person", p.get("slug"), p.get("name"), p["_body"]))
    con.commit(); con.close()
    # stats
    by = lambda rows, k: collections.Counter(str(r.get(k)) for r in rows)
    by_layer = collections.Counter(l for s in sources for l in (s.get("layers") or []))
    mentions = collections.Counter(c for s in sources for c in (s.get("companies") or []))
    lines = [f"# Index stats — {today()}", "",
             f"- sources: {len(sources)}  | companies: {len(companies)} | people: {len(people)}", "",
             "## Sources by type", *[f"- {k}: {v}" for k, v in sorted(by(sources,'type').items())], "",
             "## Sources by status", *[f"- {k}: {v}" for k, v in sorted(by(sources,'status').items())], "",
             "## Sources by layer", *[f"- {k}: {v}" for k, v in by_layer.most_common()], "",
             "## Companies by layer / status", *[f"- {k}: {v}" for k, v in sorted(by(companies,'layer').items())], "",
             *[f"- status={k}: {v}" for k, v in sorted(by(companies,'status').items())], "",
             "## Most-mentioned companies", *[f"- {k}: {v}" for k, v in mentions.most_common(15)], ""]
    (IDX / "STATS.md").write_text("\n".join(lines))
    if "--stats" in sys.argv: print("\n".join(lines))
    else: print(f"index built: {len(sources)} sources, {len(companies)} companies, {len(people)} people -> index/")

if __name__ == "__main__":
    main()
