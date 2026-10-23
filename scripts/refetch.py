#!/usr/bin/env python3
"""Upgrade headline-only sweep sources to full article text.

  python3 scripts/refetch.py --theme oba [--max 150] [--dry-run]

Targets sources added by sweep.py that are still `status: unread` and have no page text (word_count < 150).
Resolves Google News redirect links to the publisher URL, fetches the article, and rewrites the body as
"[feed snippet] ... [page text] ...". Keeps id and frontmatter; updates url, hash and word_count. Skips pages it can't read.
"""
import argparse, time
from common import SOURCES, read_fm, write_fm, iter_md, sha256_text, rel
from sweep import resolve_link, page_text

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--max", type=int, default=150); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(); done = tried = 0
    for p in iter_md(SOURCES):
        if tried >= a.max: break
        fm, body = read_fm(p)
        if fm.get("added_by") != "sweep.py" or fm.get("status") != "unread" or (fm.get("word_count") or 0) >= 150 or "[page text]" in body: continue
        if fm.get("type") == "website": continue
        tried += 1
        url = resolve_link(fm.get("url") or "")
        if "news.google.com" in url: print(f"   unresolved: {rel(p)}"); continue
        try:
            text, _ = page_text(url); time.sleep(0.7)
        except Exception as ex:
            print(f"   fetch fail: {url[:80]} ({str(ex)[:50]})"); fm["url"] = url
            if not a.dry_run: write_fm(p, fm, body)
            continue
        if len(text.split()) < 150: print(f"   too short: {url[:80]}"); fm["url"] = url; (None if a.dry_run else write_fm(p, fm, body)); continue
        new = f"[feed snippet]\n{body.strip()}\n\n[page text]\n{text}"
        fm.update(url=url, hash=sha256_text(new), word_count=len(new.split()))
        if not a.dry_run: write_fm(p, fm, "\n" + new + "\n")
        done += 1; print(f"   + {fm['id']} {len(text.split())} words  {url[:70]}")
    print(f"refetch: upgraded {done} of {tried} headline-only sources")

if __name__ == "__main__":
    main()
