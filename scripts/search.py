#!/usr/bin/env python3
"""Full-text search over the whole corpus (needs `make index` first).
  python3 scripts/search.py "rare earth refining"
  python3 scripts/search.py "gross margin" --kind source --limit 20
  python3 scripts/search.py --company hadrian          # every source that tags hadrian
"""
import argparse, sqlite3, json
from common import ROOT, INDEX
DB = INDEX / "db.sqlite"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("q", nargs="?"); ap.add_argument("--kind"); ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--company")
    a = ap.parse_args()
    if not DB.exists(): raise SystemExit("run `make index` first")
    con = sqlite3.connect(DB)
    if a.company:
        for r in con.execute("select s.id, s.type, s.date, s.title from mentions m join sources s on s.id=m.source_id where m.company_slug=? order by s.date desc", (a.company,)):
            print(" | ".join(str(x) for x in r))
        return
    if not a.q: raise SystemExit("give a query")
    sql = "select kind, key, title, snippet(fts, 3, '[', ']', '…', 18) from fts where fts match ?"
    params = [a.q]
    if a.kind: sql += " and kind=?"; params.append(a.kind)
    sql += " order by rank limit ?"; params.append(a.limit)
    for kind, key, title, snip in con.execute(sql, params):
        print(f"[{kind}] {key} — {title}\n    {snip.replace(chr(10),' ')}\n")

if __name__ == "__main__":
    main()
