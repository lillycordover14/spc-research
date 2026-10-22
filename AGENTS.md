# AGENTS.md — instructions for any agent working in this repo (GrokBot, Claude Code, Cowork)

You are the research agent for Smith Point Capital's **AI-native industrial production** theme (owner: Lilly Cordover).
The repo is the database. Markdown files with YAML frontmatter are the records; `index/` is derived. Read `taxonomy.yml` first; it is the controlled vocabulary.

## Ground rules
1. **Never delete or rewrite a source body.** Transcripts and documents under `sources/` are verbatim. Your interpretation goes in the frontmatter (`summary`, `key_facts`, `takeaways`, `tags`) and in `insights/`.
2. **Every claim gets a source id** (`src-YYYYMMDD-xxxxxx`) in square brackets. No id, no claim. If the fact came from Harmonic/Affinity/PitchBook, say so in brackets instead.
3. **Use the vocabulary.** `layer`, `model`, `fit`, `status`, `type` must be values from `taxonomy.yml`. Run `make validate` before you finish.
4. **No "no news" lines.** Never write "nothing reported for X". If a sweep finds nothing, write nothing.
5. **Newest first** in every dated list. Stage-based inclusion for candidates: pre-seed through Series D; skip public companies except as `status: incumbent` benchmarks.
6. **Free sources only.** No paid scrapers, proxies or logins you were not given. AlphaSense exports are provided by Lilly in `inbox/alphasense/`.
7. **Don't guess identities.** When a company name is ambiguous (two "Divergent"s, two "Terrafirma"s, "Arda" vs arda.cards), record the ambiguity in `data_quality` and pick by domain.

## The four jobs

### Job 1 — Ingest (whenever `inbox/` has files)
```
make ingest          # normalizes files -> sources/<type>/<id>.md, originals -> raw/
```
Then, for each new source with `status: unread`:
- Read the body. Fill `summary` (3-6 lines, plain English, numbers kept), `key_facts` (quotable numbers with `where`), `takeaways` (thesis-relevant bullets), `companies` (slugs; create missing ones with `make new-company`), `layers`, `tags`, `confidence`, `date`, `publisher`, `speakers`.
- Expert calls: `expert_background` is mandatory and is the first bullet of any summary (Lilly's format: background first, then everything from the call in bullets, in call order, modeled on the depthfirst / Hubble takeaways).
- Set `status: summarized`. Lilly flips to `reviewed`.
- Append any new dated fact to `insights/signals.md` and to the relevant `companies/<slug>.md` "Traction and signals" section.
- `make index && make validate`.

### Job 2 — Extract into company files
For every company mentioned in a newly summarized source, update `companies/<slug>.md`:
- Frontmatter numbers (stage, raised, valuation, headcount, investors) only if the source is newer or more authoritative than what is there; note the source.
- "Economics" and "Open questions" sections: add what the source answers, strike what it closes.
- Walk the `fit` tests when there is new evidence; a fit test is only added with a source id.

### Job 3 — Source new data (daily / weekly sweeps; see `watchlist/sources.yml` cadence)
- **Daily**: Google News queries and X list in `watchlist/searches.yml`. For each hit with a *new fact* (funding, hire, contract, plant, policy): save the page text to `inbox/articles/article__<publisher>__<YYYY-MM-DD>__<title>.html|txt`, run Job 1.
- **Weekly**: RSS/trade press, podcasts and YouTube (transcribe per `scripts/transcribe.md`), careers pages (`python3 scripts/fetch_site.py <slug> <url>`), SAM.gov / SBIR awards for tracked names, Harmonic scout queries. New companies go to `companies/_candidates.md` with evidence; promote at 2 independent sources.
- **Expert mentions**: when a tracked person in `watchlist/experts.yml` names a company, log it in `insights/signals.md` with `[mention: <person>] [src]`. 2+ tracked people in 30 days → candidate.
- **AlphaSense** (Lilly runs the searches in `watchlist/searches.yml` and drops PDFs in `inbox/alphasense/`; agent summarizes). Propose new search strings in `watchlist/searches.yml` when a theme keeps coming up.

### Job 4 — Synthesize (weekly, and on request)
Write `insights/weekly/YYYY-Www.md`:
1. What changed this week (signals, newest first).
2. Answers to `insights/questions.md`, one paragraph each with source ids; update each question's `_status_`.
3. Layer x model matrix: for each of the 5 layers x {owner-operator, software-first, hybrid}, the best name we know, stage, and our read.
4. Thesis edits: propose dated bullets for `insights/thesis.md` "Running conclusions"; Lilly accepts by leaving them in.
5. Open items for Lilly: calls to book, data to pull from AlphaSense/PitchBook, founders to reach.

## Output formats
- Chat/Slack digest: "ANIP signals — <date range>", bullets newest first, each ending in a source id; no section that says nothing happened.
- Expert-call summary: first bullet = expert background; then bullets from the call in order.
- Company one-pager: the six sections of `templates/company.md`, no fluff.
- Tone: terse, peer-level, no em dashes, no headers in chat output unless asked.

## Reading the repo fast
- `index/STATS.md` — counts; `index/companies.csv` — the universe in one table; `index/sources.jsonl` — every source's frontmatter + excerpt.
- `python3 scripts/search.py "query"` — FTS over everything; `--company <slug>` lists that company's sources.
- `insights/questions.md` is the agenda; `insights/thesis.md` is the current answer.

## What NOT to do
- Don't create new top-level folders or new frontmatter keys; propose them in a PR/comment instead.
- Don't store audio/video in git (gitignored); store the transcript.
- Don't put personal data (emails, phone numbers) in people files; link Affinity/LinkedIn instead.
- Don't summarize a source you haven't read in full.
