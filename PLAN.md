# PLAN — AI-native industrial production: data store + 7-day sprint

_Status 2026-10-22: sections 0-3 are built (repo, scripts, automations, first 78 sources, thesis v0, weekly v0). What remains is the human part of section 4: AlphaSense exports, expert calls, founder conversations, and the group decision._

Goal: by the group decision next week, have every useful desktop source (AlphaSense transcripts, expert calls, market research, company sites, articles, podcasts) in one place an agent can read, and be the most knowledgeable person in the room on the five layers of slide 8.

## 0. Design decisions (made)
- **Store = git repo of Markdown + YAML frontmatter.** No database server. Reasons: diffable, every LLM/agent can read it natively, works offline, same pattern as Energy-Themes, free. `index/anip.sqlite` (FTS5) and `index/*.jsonl|csv` are generated views, rebuilt with `make index`.
- **One file per record**: `companies/<slug>.md`, `sources/<type>/<id>.md`, `people/<slug>.md`. Frontmatter = structured fields (schema in `schema/`), body = full text.
- **Controlled vocabulary** in `taxonomy.yml` (layers from slide 8, business models, fit tests, source types, statuses). Validator enforces it.
- **Originals kept** in `raw/` (PDF/DOCX/HTML); audio is transcribed and not committed.
- **Agent contract** in `AGENTS.md`: ingest, extract, source, synthesize. Works for GrokBot, Claude Code or Cowork. Paste-ready prompt in `GROKBOT-PROMPT.md`.
- **Multi-vertical**: everything theme-specific sits in `themes/<slug>/`; scripts, schemas, templates, workflows are shared. `make new-theme` starts a vertical.
- **Automation on GitHub**: `validate-and-index` on every push (so an agent that only writes files keeps the DB consistent) and a daily `sweep` (Google News RSS + trade-press RSS + Monday site snapshots) that files new items as `status: unread`.
- **GrokBot-efficient writes**: one small file per record, append-friendly logs, auto-created company stubs, generated `index/QUEUE.md` to-do list, `index/VALIDATION.md` error report; three write paths (shell, GitHub API, web editor).

## 1. Setup (15 minutes)
1. **Get it on GitHub** (private repo `spc-research`). Either link GitHub to Claude once (claude.ai → Settings → Connectors → GitHub) and tell Claude "push it", or locally: `cd spc-research && gh repo create lillycordover14/spc-research --private --source=. --push` (needs `git lfs install` first for the PDFs under raw/; if LFS is a hassle, delete `.gitattributes` and push plain).
2. **Turn on Actions**: Settings → Actions → "Allow all actions", and Settings → Actions → General → Workflow permissions → "Read and write". Then Actions tab → `sweep` → Run workflow (days=30, sites=true) for the first fill. Check `themes/anip/index/SWEEP-LOG.md` and `QUEUE.md` after.
3. **Give GrokBot the repo**: repo URL + `GROKBOT-PROMPT.md` pasted as its instructions. If GrokBot has GitHub access, it writes cards directly; if not, it returns JSON and you (or Claude) run `scripts/add_source.py`.
4. Local use: `pip install -r requirements.txt`, then `make validate && make index`.
5. Create the Affinity list "AI-native industrial production" and the Harmonic saved search "ANIP candidates" (queries in `watchlist/searches.yml`).

## 2. How data gets in (the daily loop)
```
themes/anip/inbox/alphasense/      <- AlphaSense PDF/TXT exports (transcripts, broker notes)
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
| Thu 10/23 | Setup (§1): push, enable Actions, first sweep. Drop desktop files into `inbox/`, `make ingest`. Run the 11 AlphaSense company searches + 10 theme searches, export to `inbox/alphasense/`. Book 3-4 expert calls (targets in searches.yml). Read `insights/weekly/2026-W43.md`. | Repo live on GitHub, AlphaSense material in, calls booked |
| Fri 10/24 | Agent Job 1+2 over AlphaSense material and sweep results. Pull earnings transcripts for the 9 comps (GM benchmarks). | Every source summarized; Q4 (gross margin) answered |
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
