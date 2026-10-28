---
slug: edison-scientific
name: Edison Scientific
aliases:
- Edison
website: https://edisonscientific.com
hq: null
founded: null
layer: vertical-outcome
layers:
- vertical-outcome
model: usage-priced
what: Commercial spinout of nonprofit FutureHouse selling Kosmos, a long-running AI scientist agent for biopharma R&D, from target discovery to regulatory document authoring.
fit:
- in-production
- lab-resistant
- investable-stage
- measurable-roi
stage: seed
total_raised_usd: 70000000
last_round:
  date: '2025-12-18'
  amount_usd: 70000000
  lead: Triatomic Capital, Spark Capital, unnamed US institutional biotech investor
  valuation_usd: null
  source: src-20251218-eefcdb
investors:
- Triatomic Capital
- Spark Capital
- Pillar VC
- Susa Ventures
- Striker Venture Partners
- Hawktail VC
- Olive VC
founders:
- Sam Rodriques (CEO)
- Andrew White
headcount: null
customers:
- Incyte (src-20260519-9cb3f1)
- Population Health Partners (src-20260629-5574a8)
harmonic_urn: null
affinity_id: null
pitchbook: null
status: candidate
spc_owner: Lilly
tags:
- ai-for-science
- life-sciences
- per-run
- forward-deployed
sources:
- src-20251105-9cd419
- src-20251105-cdfbed
- src-20251104-f897ff
- src-20251218-eefcdb
- src-20260526-6ea6d3
- src-20260519-9cb3f1
- src-20260519-f0a637
- src-20260629-5574a8
- src-20260930-ed7d9b
- src-20260924-f0c469
- src-20260829-a29596
- src-20261028-d15c5b
- src-20261028-935bd9
data_quality: Card built 2026-10-28 by grokbot from 13 sources (Lilly asked to add). Valuation (about $250M) is secondhand via Whiteford citing Bloomberg via LinkedIn [src-20261028-935bd9], so valuation_usd left null. Headcount 51 to 200 per LinkedIn via Whiteford, left null. model=usage-priced on the public per-run credit price; enterprise terms not disclosed. in-production and measurable-roi rest on company sources (Incyte deployment, PHP case study). R&D sits outside the core enterprise-ops buyers; placed as vertical-outcome because it sells completed research and regulatory work units into pharma.
updated: '2026-10-28'
news_query: '"Edison Scientific" OR ("Kosmos" "AI scientist")'
---

## What they do
Commercial spinout of the nonprofit FutureHouse, launched 2025-11-05 to develop and deploy its AI Scientist commercially [src-20251105-9cd419]. Flagship agent Kosmos reads literature, analyzes data and generates hypotheses over long runs: one run reads about 1,500 papers and runs about 42,000 lines of analysis code, with statements cited to code or literature [src-20251105-cdfbed] [src-20251104-f897ff]. Since May 2026 Kosmos is rearchitected for the biopharma R&D lifecycle, from target discovery to clinical development and regulatory authoring, trainable on partner data and reachable via Slack, Teams and email [src-20260519-9cb3f1]. Named enterprise products include Kosmos Regulatory Authoring [src-20260930-ed7d9b].

## Why it fits the theme (or doesn't)
- Fits: a vertical agent sold per unit of research work. The launch price was $200 per Kosmos run (200 credits at $1 per credit) [src-20251105-cdfbed], one of the few public per-task prices outside CX and back office.
- Fits: the lab-resistance pitch is explicit. The CEO says pharma wants models trained on its own data without lock-in to one model provider, and that frontier labs do not want to run a different model per customer (claim) [src-20260526-6ea6d3]. A Kosmos version trained on PHP's benchmark scored 81.5% against 65.5% for a frontier general model (vendor case study) [src-20260930-ed7d9b].
- Fits: forward-deployed scientists and deployment in the customer environment, SOC 2 Type II [src-20261028-d15c5b], the same delivery pattern as enterprise ops agents.
- Doesn't fit cleanly: the buyer is R&D, not an operations function, and the value case (recovered peak sales) pays off over years [inference]. The public price was withdrawn in May 2026 and enterprise terms are not disclosed [src-20260519-9cb3f1] [src-20260829-a29596].

## Traction and signals
- 2026-09-30: PHP case study: IND team time expected down about 75% (about 4 months to 1); 98% of planted errors found; Edison estimates about $99M recovered peak sales per program (vendor estimate) [src-20260930-ed7d9b]
- 2026-09-24: Springer Nature agreement brings Nature portfolio content into Kosmos [src-20260924-f0c469]
- 2026-06-29: partnership with Population Health Partners to co-build biotechs and an AI regulatory-authoring workflow [src-20260629-5574a8]
- 2026-05-26: CEO says Kosmos users have made 20,000 to 30,000 findings (estimate) [src-20260526-6ea6d3]
- 2026-05-19: Incyte collaboration to embed Kosmos across discovery and development; financial terms not disclosed [src-20260519-9cb3f1] [src-20260519-f0a637]
- 2026-05-19: founding Kosmos subscriptions end; new pricing to be announced; access by application [src-20260519-9cb3f1]
- 2025-12-18: $70M seed led by Triatomic Capital, Spark Capital and an unnamed US institutional biotech investor [src-20251218-eefcdb]
- 2025-11-05: Kosmos launched at $200 per run [src-20251105-cdfbed]; Edison launched as FutureHouse spinout with VP or C-level inbound from 6 of the top 10 pharma companies (claim) [src-20251105-9cd419]

## Economics (what we know)
- Credits at seed: Kosmos 200 credits per run; other agents 1 or 2 credits; $200 a month for 650 credits [src-20251218-eefcdb]. Launch price $1 per credit, described as "heavily discounted" [src-20251105-cdfbed].
- From May 2026: founding subscriptions retired, new pricing unpublished, enterprise terms private [src-20260519-9cb3f1] [src-20260829-a29596].
- Valuation about $250M per a secondary profile citing Bloomberg via LinkedIn; low confidence [src-20261028-935bd9].
- The case study frames value as an outcome (recovered peak sales per program), but no outcome-linked fee is disclosed [src-20260930-ed7d9b].

## Open questions
- What Incyte pays and on what unit (seat, program, run, or milestone terms).
- Whether the PHP co-build carries equity or asset economics.
- Revenue, and the enterprise pharma vs subscription split.
- Valuation from a primary source.

## People
- Sam Rodriques, co-founder and CEO [src-20251105-9cd419] [src-20260526-6ea6d3]
- Andrew White, co-founder [src-20251218-eefcdb]
