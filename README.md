# AI-native industrial production — research database

Smith Point Capital theme research (owner: Lilly Cordover). Companies that build and run their own production capacity on in-house AI, software and robotics, from metals and refining to fabrication and precision parts, plus the software-first vendors that run plants owned by others. Layers follow slide 8 of the RoY 2026 investment team priorities.

**The repo is the database.** Markdown + YAML frontmatter records; `index/` is generated. Agents read `AGENTS.md`; humans read `PLAN.md`.

```
companies/      one file per company (frontmatter = structured fields, body = what/why/signals/economics/questions)
sources/        one file per document, by type: alphasense, expert-calls, market-research, articles, podcasts, websites, filings, datasets, other
people/         founders, operators, experts, investors worth tracking
insights/       thesis.md (living), questions.md (the agenda), signals.md (dated log), weekly/ (synthesis)
watchlist/      sources.yml (what to sweep), searches.yml (saved queries), experts.yml (people whose mentions we count)
inbox/          drop zone -> `make ingest`
raw/            originals (PDF/DOCX/HTML); audio is transcribed, not committed
index/          generated: companies.csv, sources.jsonl, people.jsonl, STATS.md, anip.sqlite (FTS5, gitignored)
scripts/        ingest.py, build_index.py, validate.py, new.py, search.py, fetch_site.py, transcribe.md
schema/         frontmatter schemas; taxonomy.yml is the controlled vocabulary
templates/      company.md, source.md, expert-call.md, person.md
```

## Quick start
```bash
pip install -r requirements.txt
make index && make validate            # loads the seed: 23 companies, 12 people
cp ~/Downloads/some-transcript.pdf inbox/alphasense/ && make ingest
python3 scripts/search.py "lead time"  # full-text search
make new-company name="Atomic Industries"
```

## Conventions
- Source ids: `src-YYYYMMDD-xxxxxx` (date + 6 chars of sha256). Cite them in square brackets everywhere.
- Inbox filenames can carry metadata: `article__Modern Machine Shop__2026-10-01__Title.html` → type/publisher/date parsed.
- Company `status`: candidate → tracking → pipeline → in-diligence → passed/portfolio; incumbents/competitors are benchmarks.
- `data_quality` field records known mismatches (several Harmonic best-matches were wrong companies; see nox-metals, arda, divergent, terrafirma).

## Seed (2026-10-22)
16 startups across the five layers + adjacent, 7 incumbents/comps, 12 people, watchlist, 17 open questions. Company numbers come from Harmonic (funding totals, valuations, headcount), press, and slide 8; several slide-8 valuations are already stale (Hadrian $8B Series D, Periodic $7.5B, CuspAI $2.6B, Senra $493M, Freeform $179M).
