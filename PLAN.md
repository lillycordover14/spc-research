# PLAN — AI-native industrial production: data store + 7-day sprint

Goal: by the group decision next week, have every useful desktop source (AlphaSense transcripts, expert calls, market research, company sites, articles, podcasts) in one place an agent can read, and be the most knowledgeable person in the room on the five layers of slide 8.

## 0. Design decisions (made)
- **Store = git repo of Markdown + YAML frontmatter.** No database server. Reasons: diffable, every LLM/agent can read it natively, works offline, same pattern as Energy-Themes, free. `index/anip.sqlite` (FTS5) and `index/*.jsonl|csv` are generated views, rebuilt with `make index`.
- **One file per record**: `companies/<slug>.md`, `sources/<type>/<id>.md`, `people/<slug>.md`. Frontmatter = structured fields (schema in `schema/`), body = full text.
- **Controlled vocabulary** in `taxonomy.yml` (layers from slide 8, business models, fit tests, source types, statuses). Validator enforces it.
- **Originals kept** in `raw/` (PDF/DOCX/HTML); audio is transcribed and not committed.
- **Agent contract** in `AGENTS.md`: ingest, extract, source, synthesize. Works for GrokBot, Claude Code or Cowork.

## 1. Setup (30 minutes, today)
1. Unzip → `ai-native-industrial-production/`. Open in VS Code / Claude Code.
2. `pip install -r requirements.txt` (pyyaml, pypdf, python-docx, bs4, requests, feedparser). `pdftotext`, `pandoc`, `ffmpeg` optional but faster.
3. `make index && make validate` — confirms the seed loads (23 companies, 12 people).
4. Push to GitHub (private): `gh repo create lillycordover14/ai-native-industrial-production --private --source=. --push` (or create empty repo in UI, then `git remote add origin ... && git push -u origin main`).
5. Give the agent access: GrokBot → point it at the repo URL + `AGENTS.md`; Claude Code → `cd` into the repo and it reads `AGENTS.md` automatically; Cowork → connect the folder.
6. Create the Affinity list "AI-native industrial production" and the Harmonic saved search "ANIP candidates" (queries in `watchlist/searches.yml`) so the weekly sweep has somewhere to pull from.

## 2. How data gets in (the daily loop)
```
inbox/alphasense/      <- AlphaSense PDF/TXT exports (transcripts, broker notes)
inbox/expert-calls/    <- Granola exports / call notes
inbox/market-research/ <- NAM, Deloitte, IEA, USGS, IFR, bank reports
inbox/articles/        <- saved HTML / text; name them  article__<publisher>__<YYYY-MM-DD>__<title>.html
inbox/podcasts/        <- .txt transcripts (yt-dlp + whisper, scripts/transcribe.md)
inbox/websites/        <- or run: python3 scripts/fetch_site.py <slug> <url>
inbox/filings/         <- SAM.gov awards, SBIR, patents, permits
inbox/datasets/        <- CSV/XLSX
make ingest            -> sources/<type>/<id>.md  (+ raw/)
<agent fills summary/tags/companies; appends signals>
make index && make validate
git add -A && git commit -m "ingest <what>" && git push
```
Anything you already have on the desktop: drag the files into the matching inbox folder in one go, run `make ingest` once. Dedupe is by file hash, so re-dropping is safe.

## 3. Brainstorm: what to collect (prioritized)
**P0 — answers the thesis questions**
- AlphaSense expert calls: ex-Hadrian / ex-Machina / ex-Divergent ops; prime procurement (Lockheed, RTX, Anduril, SpaceX) on buying machined parts and harnesses; job-shop owners; service-center GMs. Search strings in `watchlist/searches.yml`.
- Earnings transcripts (AlphaSense): Proto Labs, Xometry, Nucor, Ryerson, Reliance, Howmet, ATI, Carpenter, Rockwell — margin and lead-time benchmarks, plus every mention of "automation" and "startup".
- Company primary material: website + careers page snapshots for all 16 startups (job titles reveal the software stack), founder podcast/YouTube appearances, press releases, pitch decks SPC has received, Affinity notes.
- Hadrian financing stack: Series D + $360M debt — what lenders required. Template for every owner-operator.
- SPC's own calls: Nox Metals (Sep 2026), any founder or expert call already in Granola.

**P1 — market and policy**
- Deloitte/MI labor gap report; IFR World Robotics 2025; USGS MCS 2026; IEA Critical Minerals 2026; NAM facts; First Research metals distribution; Kearney Reshoring Index; DoD Industrial Base reports; Section 232 and DPA Title III actions; NDAA FY27 reshoring provisions.
- SAM.gov / SBIR / DIU awards for every tracked company (defense traction at seed).
- Patents by assignee (Hadrian, Machina, Divergent, Freeform, Senra): what IP is software vs process.

**P2 — landscape expansion**
- Harmonic scout queries (weekly) → `_candidates.md`; Reindustrialize speaker lists; a16z AD, Founders Fund, Lux, Construct, Countdown portfolio pages; YC batch lists (S24-S26) filtered to manufacturing.
- Investor memos: Contrary (Hadrian), Not Boring, Sacra revenue estimates.
- Incumbent automation moves: PCC, Howmet, Nucor, Reliance 10-Ks and investor days on automation capex.

**P3 — nice to have**
- Import/export records (Panjiva) for Isembard/Mariana; state incentive filings; Glassdoor for plant culture; LinkedIn headcount series (Harmonic has it).

## 4. The week
| Day | Do | Output |
|---|---|---|
| Thu 10/23 | Setup (§1). Drop everything already on the desktop into `inbox/`, `make ingest`. Run the 11 AlphaSense company searches + 10 theme searches, export to `inbox/alphasense/`. Book 3-4 expert calls (targets in searches.yml). | Repo live, first 30-60 sources in, calls booked |
| Fri 10/24 | Agent Job 1+2 over everything ingested. Snapshot all 16 websites/careers (`fetch_site.py`). Pull earnings transcripts for the 9 comps. | Every source summarized; company files updated; `signals.md` populated |
| Sat/Sun | Agent weekly sweep (Job 3): podcasts/YouTube transcribed, Harmonic scout, SAM.gov. Lilly reads `index/STATS.md` + top sources only. | `_candidates.md` with 10-20 names; first `insights/weekly/2026-W43.md` draft |
| Mon 10/27 | Expert calls 1-2. Ingest Granola notes same day. Answer questions A1-A3 and B4-B5 in writing. | Questions A/B partial → answered |
| Tue 10/28 | Expert calls 3-4. Answer C and D. Build the layer x model matrix with SPC's pick per cell. | Matrix v1 |
| Wed 10/29 | Synthesis: rewrite `insights/thesis.md` with sources; one-page group view (matrix + 5 conclusions + 3 names to go after). Memo-review pass. | Group doc ready |
| Thu 10/30 | Group decision. Log decisions in `insights/thesis.md`; set the standing weekly cadence for the agent. | Decision + cadence |

## 5. Definition of done for the week
- ≥ 80 sources ingested and summarized, ≥ 40 of them AlphaSense/expert material.
- All 17 questions in `insights/questions.md` have a written answer or a named blocker.
- Layer x model matrix with a view per cell and 3 named targets for outreach.
- Weekly agent sweep running on a schedule (GrokBot or scheduled Cowork task) producing "ANIP signals" digests.

## 6. Later (not this week)
- Embeddings over `sources/` for semantic search (sqlite-vec or a small Chroma store) once > 300 sources.
- Sync `index/companies.csv` ↔ Affinity list fields; Harmonic list upsert.
- Second theme (energy, inference) can reuse the same scaffold: copy repo, replace `taxonomy.yml` layers.
