#!/usr/bin/env python3
"""
Automated sweep: pulls new items from free sources and files them as `status: unread` sources for the agent to summarize.
Runs in GitHub Actions daily (see .github/workflows/sweep.yml); can run locally too.

  python3 scripts/sweep.py [--theme anip] [--days 14] [--sites] [--dry-run]

What it does
  1. Google News RSS for every query in watchlist/searches.yml:google_news AND for every tracked company name
     (news.google.com/rss/search?q=...). Free, no key. Keeps items newer than --days.
     Company frontmatter can set `news_query:` (replaces the default "<name>" query) and `match_context:` (a list of
     words; a name match only counts if one of them also appears). Use both for names that are common words (Arda, Freeform).
  2. Trade-press RSS: every entry in watchlist/sources.yml:rss_and_trade_press that has an `rss:` URL, or whose homepage
     advertises a feed (<link type="application/rss+xml">). Keeps items that mention a tracked company or a sweep keyword.
  3. (--sites, or Mondays) snapshots each tracked company's homepage + careers page into sources/websites/.
  4. Tries to fetch full article text; falls back to the feed snippet. Dedupes on URL and text hash.
Writes a line to index/SWEEP-LOG.md. Never deletes anything.
"""
from __future__ import annotations
import argparse, datetime as dt, re, sys, time, json
from pathlib import Path
from urllib.parse import quote_plus, urlparse
import yaml, requests
from common import T, INDEX, WATCHLIST, COMPANIES, SOURCES, read_fm, iter_md, today, rel, write_fm, make_id, sha256_text
from add_source import add_record

UA = {"User-Agent": "Mozilla/5.0 (compatible; spc-research-sweep/1.0; +https://smithpointcapital.com)"}
GN = "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
FEED_GUESSES = ["/rss", "/feed", "/rss.xml", "/feed.xml", "/feeds/all.rss", "/news/rss", "/rss/news"]

def log(msg): print(msg, flush=True)

def tracked_companies():
    out = []
    for p in iter_md(COMPANIES):
        fm, _ = read_fm(p)
        if fm.get("status") in ("incumbent", "not-a-fit", "passed"): continue
        names = [fm.get("name")] + list(fm.get("aliases") or [])
        out.append({"slug": fm["slug"], "names": [n for n in names if n], "website": fm.get("website"),
                    "news_query": fm.get("news_query"), "context": [w.lower() for w in (fm.get("match_context") or [])]})
    return out

def resolve_link(url: str) -> str:
    """Google News RSS links are redirect stubs; fetching them returns Google's page, not the article. Decode to the publisher URL."""
    if not url or "news.google.com" not in url: return url
    try:
        from googlenewsdecoder import gnewsdecoder
        r = gnewsdecoder(url, interval=1)
        if (r.get("success") or r.get("status")) and r.get("decoded_url"): return r["decoded_url"]
    except Exception: pass
    return url

def fetch(url, timeout=20):
    r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
    r.raise_for_status(); return r

def page_text(url) -> tuple[str, str | None]:
    from bs4 import BeautifulSoup
    r = fetch(url)
    if "html" not in r.headers.get("content-type", ""): return "", None
    soup = BeautifulSoup(r.text, "html.parser")
    for t in soup(["script", "style", "nav", "footer", "header", "noscript", "svg", "form"]): t.decompose()
    title = soup.title.string.strip() if soup.title and soup.title.string else None
    main = soup.find("article") or soup.find("main") or soup.body or soup
    text = re.sub(r"\n{3,}", "\n\n", main.get_text("\n")).strip()
    return text, title

def discover_feed(site: str) -> str | None:
    try:
        from bs4 import BeautifulSoup
        r = fetch(site); soup = BeautifulSoup(r.text, "html.parser")
        for l in soup.find_all("link", attrs={"type": re.compile("rss|atom")}):
            if l.get("href"):
                href = l["href"]; return href if href.startswith("http") else site.rstrip("/") + "/" + href.lstrip("/")
    except Exception: pass
    for g in FEED_GUESSES:
        try:
            r = fetch(site.rstrip("/") + g, timeout=10)
            if b"<rss" in r.content[:2000] or b"<feed" in r.content[:2000]: return site.rstrip("/") + g
        except Exception: continue
    return None

def parse_feed(url):
    import feedparser
    r = fetch(url); return feedparser.parse(r.content)

def entry_date(e) -> str | None:
    for k in ("published_parsed", "updated_parsed"):
        if e.get(k):
            return time.strftime("%Y-%m-%d", e[k])
    return None

def mentions(text: str, companies, keywords) -> list[str]:
    t = text.lower(); hits = []
    for c in companies:
        if c["context"] and not any(w in t for w in c["context"]): continue
        if any(len(n) > 2 and re.search(r"\b" + re.escape(n.lower()) + r"\b", t) for n in c["names"]): hits.append(c["slug"])
    return hits if hits else (["__kw__"] if any(k.lower() in t for k in keywords) else [])

def file_item(e, publisher, companies, keywords, cutoff, layers_hint, args, stats, force_keep=False, require=None):
    title = (e.get("title") or "").strip(); link = e.get("link"); date = entry_date(e)
    if not title or not link: return
    if date and date < cutoff: stats["old"] += 1; return
    snippet = re.sub(r"<[^>]+>", "", e.get("summary") or e.get("description") or "")
    hits = mentions(title + " " + snippet, companies, keywords)
    if not hits and not force_keep: stats["filtered"] += 1; return
    if require and require not in hits: stats["filtered"] += 1; return   # company query: result must actually be about that company
    slugs = [h for h in hits if h != "__kw__"]
    src = e.get("source", {}).get("title") if isinstance(e.get("source"), dict) else None
    body, page_title = snippet, None
    if not args.dry_run:
        link = resolve_link(link)
        try:
            body, page_title = page_text(link); body = body or snippet
            time.sleep(0.7)
        except Exception as ex:
            stats["fetch_fail"] += 1
    rec = {"type": "article", "title": title, "date": date, "url": link, "publisher": src or publisher, "companies": slugs,
           "layers": layers_hint, "tags": ["sweep"], "summary": "", "confidence": "med", "status": "unread", "added_by": "sweep.py",
           "body": (f"[feed snippet]\n{snippet}\n\n[page text]\n{body}" if body != snippet else snippet)}
    if args.dry_run: log(f"   would add: {date} {title[:80]} -> {slugs}"); stats["new"] += 1; return
    out = add_record(rec, quiet=True)
    if out: stats["new"] += 1; log(f"   + {date} {title[:80]} -> {slugs or 'kw'}")
    else: stats["dup"] += 1

def snapshot_sites(companies, stats):
    PATHS = ["", "/careers", "/jobs", "/about", "/news", "/blog"]
    for c in companies:
        site = c.get("website")
        if not site: continue
        chunks = []
        for p in PATHS:
            try:
                t, _ = page_text(site.rstrip("/") + p)
                if len(t) > 200: chunks.append(f"\n\n===== {site.rstrip('/') + p} =====\n{t}")
                time.sleep(0.5)
            except Exception: continue
        if not chunks: stats["site_fail"] += 1; continue
        body = "".join(chunks)
        rec = {"type": "website", "title": f"{c['slug']} website + careers snapshot {today()}", "date": today(), "url": site, "publisher": c["slug"],
               "companies": [c["slug"]], "tags": ["website-snapshot", "sweep"], "confidence": "high", "status": "unread", "added_by": "sweep.py", "body": body}
        # dedupe on content hash (unchanged site = no new record); add_record handles url dedupe, so bypass url by hashing body only
        out = add_record({**rec, "url": f"{site}#snapshot-{sha256_text(body)[:8]}"}, quiet=True)
        if out: stats["sites"] += 1; log(f"   + site {c['slug']}")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--days", type=int, default=14); ap.add_argument("--sites", action="store_true")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--max-per-query", type=int, default=15)
    args = ap.parse_args()
    cutoff = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    searches = yaml.safe_load((WATCHLIST / "searches.yml").read_text()) or {}
    sources = yaml.safe_load((WATCHLIST / "sources.yml").read_text()) or {}
    companies = tracked_companies()
    keywords = searches.get("sweep_keywords") or []
    stats = dict(new=0, dup=0, old=0, filtered=0, fetch_fail=0, feeds_ok=0, feeds_fail=0, sites=0, site_fail=0)

    # 1. Google News: company names + saved queries
    queries = [(c.get("news_query") or f'"{c["names"][0]}"', c["slug"]) for c in companies] + [(q, None) for q in searches.get("google_news") or []]
    log(f"Google News: {len(queries)} queries, cutoff {cutoff}")
    for q, slug in queries:
        try:
            f = parse_feed(GN.format(q=quote_plus(q)))
            stats["feeds_ok"] += 1
            for e in f.entries[: args.max_per_query]:
                file_item(e, "Google News", companies, keywords, cutoff, [], args, stats, force_keep=True, require=slug)
            time.sleep(1.0)
        except Exception as ex:
            stats["feeds_fail"] += 1; log(f"   feed fail: {q} ({str(ex)[:60]})")

    # 2. Trade press RSS
    feeds = sources.get("rss_and_trade_press") or []
    log(f"Trade press: {len(feeds)} outlets")
    for s in feeds:
        url = s.get("rss") or (discover_feed(s["url"]) if s.get("url") else None)
        if not url: stats["feeds_fail"] += 1; log(f"   no feed found: {s.get('name')}"); continue
        try:
            f = parse_feed(url); stats["feeds_ok"] += 1
            for e in f.entries[:60]:
                file_item(e, s.get("name"), companies, keywords, cutoff, [], args, stats)
            time.sleep(1.0)
        except Exception as ex:
            stats["feeds_fail"] += 1; log(f"   feed fail: {s.get('name')} ({str(ex)[:60]})")

    # 3. Sites (weekly)
    if args.sites or dt.date.today().weekday() == 0:
        log("Site snapshots"); 
        if not args.dry_run: snapshot_sites(companies, stats)

    line = f"- {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M')}Z — new {stats['new']}, dup {stats['dup']}, filtered {stats['filtered']}, old {stats['old']}, feeds ok/fail {stats['feeds_ok']}/{stats['feeds_fail']}, sites {stats['sites']} (fail {stats['site_fail']}), page fetch fails {stats['fetch_fail']}\n"
    log(line.strip())
    if not args.dry_run:
        INDEX.mkdir(exist_ok=True); lp = INDEX / "SWEEP-LOG.md"
        head = "# Sweep log\n\nOne line per run (newest first). If `new` is 0 for a week, feeds are broken or filters too tight: check watchlist/searches.yml.\n\n"
        prev = lp.read_text().replace(head, "") if lp.exists() else ""
        lp.write_text(head + line + prev)

if __name__ == "__main__":
    main()
