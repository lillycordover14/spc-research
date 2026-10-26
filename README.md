# spc-research — thematic research database

Smith Point Capital's research database for investment themes. **The repo is the database**: one Markdown file with a YAML header per company, source and person; GitHub Actions validate and index on every push and run a daily sweep of free sources. Agents (GrokBot, Claude) read `AGENTS.md`; humans read `HOW-IT-WORKS.md` and `PLAN.md`.

Themes (verticals) live under `themes/<slug>/`. First theme: **ai-native-industrial-production** (`anip`), owner Lilly Cordover. Add another with `make new-theme`.

```
HOW-IT-WORKS.md   plain-English explainer        AGENTS.md   rules for agents       GROKBOT-PROMPT.md   paste-ready prompt
PLAN.md           setup + 7-day sprint           scripts/    shared tools           schema/ templates/  shared formats
.github/workflows/ validate-and-index (push), sweep (daily)
themes/<slug>/    theme.yml taxonomy.yml companies/ sources/ people/ insights/ watchlist/ inbox/ raw/ index/
```

## Quick start
```bash
pip install -r requirements.txt
make validate && make index            # single theme resolves automatically; otherwise THEME=anip
cp ~/Downloads/transcript.pdf themes/ai-native-industrial-production/inbox/alphasense/ && make ingest
python3 scripts/search.py "lead time"
make new-company name="Atomic Industries"
make sweep ARGS="--dry-run --days 30"  # see what the daily job would file
```

## State on 2026-10-22
78 sources (54 articles, 9 market/policy reports, 2 filings, 8 website snapshots, 3 podcasts, 2 other), 23 companies (16 startups + 7 incumbents), 16 people, 39 candidates, thesis with 7 sourced conclusions, 17 open questions with a first-pass answer in `insights/weekly/2026-W43.md`.

**Start here:** [Best of: AI-native industrial production](themes/ai-native-industrial-production/insights/best-of.md) lists the top podcasts, investor theses, market maps, an incumbent scoreboard and every startup with its best sources. All of these sources carry the `must-read` tag.

## Themes
- **AI-native industrial production** (`anip`): [best-of](themes/ai-native-industrial-production/insights/best-of.md), prompts `GROKBOT-PROMPT.md` and `GROKBOT-SOURCING-PROMPT.md`.
- **Outcome-based agents and agentic orchestration** (`oba`, started 2026-10-23, readout 2026-10-28/29): [questions](themes/outcome-based-agents/insights/questions.md), [framework](themes/outcome-based-agents/insights/framework.md), prompt `GROKBOT-OBA-PROMPT.md`.
- **Power and compute: the AI buildout bottleneck** (`apc`, started 2026-10-26): [questions](themes/ai-power-compute/insights/questions.md), [framework](themes/ai-power-compute/insights/framework.md), prompt `GROKBOT-APC-PROMPT.md`. Targets: Gimlet Labs, Sail Research, Applied Compute, Simplismart, Deep Cogito; Adaptive ML (acquired by Datadog) as a comp.
