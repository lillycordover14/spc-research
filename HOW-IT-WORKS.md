# How this system works (for Lilly and for GrokBot)

## The one-paragraph version
This repo is a filing cabinet that an AI can read and write. Every company, every document and every person is one small text file with a fixed header. You (or an agent, or a scheduled job) drop new files in; GitHub automatically checks them and rebuilds the indexes; the agent reads the to-do list the index produces, summarizes what is new, updates the company files, and writes the weekly synthesis. Add a second vertical by copying one folder. Nothing runs on a server you have to maintain.

## The three kinds of cards
| Card | Lives in | Header (frontmatter) holds | Body holds |
|---|---|---|---|
| **Company** | `themes/<theme>/companies/<slug>.md` | slug, layer, model, stage, raised, investors, founders, status, fit tests | What they do / why it fits / dated signals / economics / open questions / people |
| **Source** | `themes/<theme>/sources/<type>/<id>.md` | id, type, title, date, url, publisher, companies, layers, tags, summary, key facts, takeaways, status | The full text or transcript (verbatim when we have it; extracted notes when we don't) |
| **Person** | `themes/<theme>/people/<slug>.md` | name, role, affiliation, prior roles, why we track them | notes |

Header = YAML between two `---` lines. Allowed values (layers, models, types, statuses) are in `themes/<theme>/taxonomy.yml`. A validator rejects anything else, so the data stays clean no matter who writes it.

Source ids look like `src-20260817-c48f28` (date + 6 characters of a hash). Every claim anywhere in the repo ends with one in square brackets. That is the whole citation system.

## The map
```
spc-research/
  HOW-IT-WORKS.md  AGENTS.md  GROKBOT-PROMPT.md  PLAN.md  README.md
  scripts/      shared tools (ingest, add_source, sweep, build_index, validate, search, new, new_theme, fetch_site)
  schema/       what a valid header looks like            templates/  blank cards
  .github/workflows/   the two automations (validate-and-index on push; daily sweep)
  themes/
    _template/                         copy this to start a new vertical
    ai-native-industrial-production/   the first vertical
      theme.yml  taxonomy.yml
      companies/  sources/  people/    the cards
      insights/   thesis.md (living), questions.md (agenda), signals.md (dated log), weekly/ (synthesis)
      watchlist/  sources.yml (what we sweep), searches.yml (saved queries), experts.yml (people whose mentions we count)
      inbox/      drop zone            raw/   originals (PDF etc.)
      index/      GENERATED: STATS.md, QUEUE.md, VALIDATION.md, SWEEP-LOG.md, companies.csv, sources.jsonl, people.jsonl, db.sqlite
```

## Four doors for data (pick whichever is easiest)
1. **Drop a file.** Put a PDF / DOCX / HTML / TXT / VTT / AlphaSense export in `inbox/<type>/`, run `make ingest`. The script extracts the text, keeps the original in `raw/`, writes a source card with `status: unread`, and dedupes by file hash. Name files `type__publisher__YYYY-MM-DD__title.ext` and the header fills itself.
2. **Agent JSON.** An agent with a shell runs `python3 scripts/add_source.py record.json` (fields documented at the top of that script). It creates company stubs for unknown slugs and dedupes on URL and text.
3. **Write the card directly on GitHub.** Any agent or human that can create a file (web editor, GitHub API `PUT /repos/{owner}/{repo}/contents/{path}`) copies `templates/source.md`, fills the header, pastes the text, commits. GitHub then validates and indexes it automatically. This is the GrokBot path if GrokBot cannot run Python.
4. **The daily sweep does it for you.** `.github/workflows/sweep.yml` runs `scripts/sweep.py` every morning: Google News RSS for every tracked company and every saved query, trade-press RSS filtered by company names and keywords, and on Mondays a snapshot of each company's website and careers page. New items land as `status: unread`.

## What GitHub does by itself
- **On every push** (`validate-and-index`): checks every header against the schema and taxonomy, writes `index/VALIDATION.md` (problems listed, or "all valid"), rebuilds `index/` and commits it. If validation fails the run shows red and the problems are in that file.
- **Every day at 6:17am Central** (`sweep`): the sweep above, then validate + index + commit. `index/SWEEP-LOG.md` has one line per run; if `new` is 0 for a week, feeds are broken or filters too tight.
- You can trigger either by hand from the Actions tab ("Run workflow").

## What the agent does (GrokBot, Claude, whoever)
Read `AGENTS.md` once. Then each run:
1. Open `themes/<theme>/index/QUEUE.md`. It lists unread sources (oldest first), summarized-but-untagged sources, and company stubs to fill.
2. For each unread source: read the body, fill `summary`, `key_facts`, `takeaways`, `companies`, `layers`, `tags`, set `status: summarized`. For expert calls, `expert_background` is mandatory and is the first bullet of any summary.
3. Push each new fact into the company card (dated bullet, newest first, source id) and into `insights/signals.md`.
4. Weekly: write `insights/weekly/YYYY-Www.md` answering `insights/questions.md`, propose dated bullets for `insights/thesis.md` "Running conclusions".
5. Rules that never change: never edit a source body; every claim has a source id; no "no news" lines; only taxonomy values; free sources only; when two companies share a name, say so in `data_quality`.

## Finding things
- `index/STATS.md` counts; `index/companies.csv` the whole universe in one table (opens in Excel); `index/sources.jsonl` every source header plus a 600-char excerpt.
- `python3 scripts/search.py "lead time"` full-text search over everything; `--company hadrian` lists that company's sources.
- `insights/questions.md` is the agenda, `insights/thesis.md` the current answer, `insights/weekly/` the trail.

## Adding another vertical
```
make new-theme slug=energy name="Energy & the AI power bottleneck" short=en
```
Edit `themes/energy/taxonomy.yml` (the layers from that slide), `watchlist/*.yml`, `insights/thesis.md`. Done. Scripts, schemas, workflows and the agent instructions are shared; the sweep and the index pick the new theme up automatically. Every `make` target takes `THEME=energy`.

## Storage and limits
- A source card is 5-200 KB of text. 10,000 sources is roughly 0.5-1 GB, fine for a git repo. Beyond that, split themes into separate repos (same scaffold).
- Originals under `raw/` are plain git files for now (fine up to a few hundred MB). When they get large, turn on Git LFS for PDFs (two lines in `.gitattributes`, already written there) or point `raw_file` at a bucket (Cloudflare R2 or SharePoint) and keep only the text in git. Audio/video is never committed; transcribe it (`scripts/transcribe.md`).
- Nothing in the repo is a server. Backups are the git history; every change is a commit by a named author or bot.

## Statuses, in plain words
- Source: `unread` (nobody has read it) → `summarized` (agent filled the header) → `reviewed` (Lilly looked).
- Company: `candidate` (one mention) → `tracking` (we watch) → `pipeline` → `in-diligence` → `passed` / `portfolio`; `incumbent` and `competitor` are benchmarks, not targets; `not-a-fit` keeps the record so nobody re-researches it.
- Confidence: `high` (primary source, numbers quoted), `med` (press), `low` (secondary, deleted posts, unverified).
