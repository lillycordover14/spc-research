#!/usr/bin/env python3
"""Snapshot a company's website (home + a few key pages) into sources/websites/ as one source per run.
  python3 scripts/fetch_site.py machina-labs https://machinalabs.ai
Pages tried: /, /about, /careers, /jobs, /products, /technology, /blog, /news, /press (whatever answers 200).
Careers pages are gold: job titles reveal the software/robotics stack and what the plant actually does.
"""
import sys, re, time, requests
from pathlib import Path
from bs4 import BeautifulSoup
from common import ROOT, write_fm, make_id, sha256_text, today

PATHS = ["", "/about", "/company", "/careers", "/jobs", "/products", "/product", "/technology", "/platform", "/blog", "/news", "/press", "/customers"]
UA = {"User-Agent": "Mozilla/5.0 (research snapshot; smithpointcapital.com)"}

def grab(url):
    try:
        r = requests.get(url, headers=UA, timeout=20)
        if r.status_code != 200 or "text/html" not in r.headers.get("content-type", ""): return None
        soup = BeautifulSoup(r.text, "html.parser")
        for t in soup(["script", "style", "nav", "footer", "noscript", "svg"]): t.decompose()
        text = re.sub(r"\n{3,}", "\n\n", soup.get_text("\n")).strip()
        return text if len(text) > 200 else None
    except Exception:
        return None

def main():
    slug, base = sys.argv[1], sys.argv[2].rstrip("/")
    chunks = []
    for p in PATHS:
        t = grab(base + p)
        if t: chunks.append(f"\n\n===== {base + p} =====\n{t}"); time.sleep(0.5)
    if not chunks: raise SystemExit("nothing fetched (JS-only site? use the browser and paste text into inbox/websites/)")
    body = "".join(chunks)
    sid = make_id(sha256_text(body))
    fm = {"id": sid, "type": "website", "title": f"{slug} website snapshot {today()}", "date": today(), "added": today(),
          "url": base, "publisher": slug, "companies": [slug], "layers": [], "tags": ["website-snapshot"],
          "summary": "", "key_facts": [], "takeaways": [], "confidence": "high", "raw_file": None,
          "hash": sha256_text(body), "word_count": len(body.split()), "status": "unread", "added_by": "fetch_site.py"}
    out = ROOT / "sources" / "websites" / f"{sid}.md"
    write_fm(out, fm, body); print(out.relative_to(ROOT))

if __name__ == "__main__":
    main()
