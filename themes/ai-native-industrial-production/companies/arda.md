---
slug: arda
name: Arda
aliases:
- Arda AI
- Arda Industries
website: null
hq: San Francisco, CA
founded: 2025
layer: factory-ai
layers: []
model: software-first
what: 'AI agent for manufacturing engineers: reads CAD and design docs and produces assembly order, work instructions and station layouts for lines in plants owned by others; robot-programming agents and a factory-video model are roadmap. Co-founded by ex-OpenAI chief research officer Bob McGrew.'
fit:
- in-house-software
- data-loop
- mission-critical-output
stage: series-a
total_raised_usd: 232000000
last_round:
  date: '2026-10-20'
  amount_usd: 160000000
  lead: Altimeter, Accel, Khosla Ventures (co-leads)
  valuation_usd: 1500000000
  source: src-20261020-914a64
investors:
- Altimeter
- Accel
- Khosla Ventures
- Founders Fund
- XYZ Venture Capital
- 8VC
- SV Angel
- Felicis
founders:
- name: Bob McGrew
  role: Co-founder (leads the company; title not stated in press)
  prior: OpenAI research lead 2018-2024, chief research officer; Palantir product/engineering lead first decade; US Army Reserve Detachment 201
- name: Jakob Frick
  role: Co-founder
  prior: Palantir; SpaceX
- name: Augustus Odena
  role: Chief AI Officer
  prior: Co-founder Adept; Google Brain; Meta
- name: Alex Mark
  role: CTO
  prior: Led engineering at Palantir; IRS Direct File
headcount: null
customers:
- Anduril
harmonic_urn: null
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- factory-video
- mes
- software-first
- defense-demand
- reshoring
sources:
- src-20261020-914a64
- src-20260308-1984ea
- src-20261020-26c44d
- src-20261022-20c5aa
- src-20261022-83a6ff
- src-20261021-9e65ed
- src-20261020-672397
- src-20261020-ec038e
- src-20261020-97e733
- src-20261020-143d41
- src-20261020-7b5f99
- src-20261020-787a0a
- src-20261020-dcd2f4
- src-20261020-ab7c7d
- src-20261020-c704fe
- src-20261021-855f21
- src-20261021-ca7fa2
- src-20261020-878aa9
- src-20261020-bbfb1c
- src-20261023-a7d562
- src-20261020-a1e174
- src-20261020-5e4abd
- src-20261023-86e6bb
- src-20261020-a23633
- src-20261020-6638b9
- src-20261021-7908dd
- src-20261020-722aff
- src-20261020-282a37
- src-20261020-57bfbc
- src-20261021-ef5d1b
- src-20261020-e6a4c6
- src-20261020-894973
data_quality: 'Harmonic best match (urn:harmonic:company:54804621, arda.cards) is a DIFFERENT company (inventory cards, Seattle); no Harmonic record found by domain. Official website/domain not found in any fetched source (launch PR on BusinessWire could not be fetched). HQ ''San Francisco'' is unsourced. Mar 2026 WSJ report of ''$70M at $700M'' is superseded by the Oct 2026 launch: $72M seed + $160M Series A at $1.5B. Odena and Mark are listed as execs in press, not explicitly as co-founders.'
updated: '2026-10-22'
news_query: '"Arda" (McGrew OR manufacturing OR factory OR "production line") -Güler -Guler -Madrid'
match_context:
- mcgrew
- manufactur
- factory
- factories
- production line
- openai
- assembly
- raises
- funding
- valuation
- unicorn
- $230
- $1.5
---

## What they do
Arda emerged from stealth on 20 Oct 2026 with an agent for manufacturing engineers: it reads CAD files and design documents, works out assembly order, writes work instructions and lays out production stations, and pushes design changes to the floor without stopping the line [src-20261020-914a64]. McGrew pitches it as "what Claude or Cursor does for programmers" for manufacturing engineers [src-20261020-914a64]. Today it runs manual assembly lines; reconfigurable automated lines and agents that program robots are in prototype, and the factory-video model described in the Mar 2026 WSJ report is the longer-term direction [src-20261020-914a64] [src-20260308-1984ea]. First design partner and customer is Anduril, which runs Arda inside its ArsenalOS manufacturing software and reports basic work instructions down from 10 hours to 15 minutes and complex engineering work from up to 30 hours to about 2.5 [src-20261020-914a64]. Target markets are defence and the data-centre supply chain (transformer and electrical equipment makers) first, then consumer electronics and robotics [src-20261020-914a64].

## Why it fits the theme (or doesn't)
- owns-production: no. Pure software; the plant, machines and workers belong to the customer [src-20261020-914a64].
- in-house-software: yes, the product is the software; team is ex-Palantir, OpenAI, Adept, Google Brain [src-20261020-914a64].
- data-loop: the agent ingests customer CAD and process docs; whether Arda retains anything across customers is unknown. The factory-video flywheel is still roadmap, not shipping [src-20260308-1984ea] [src-20261020-914a64].
- mission-critical-output: Anduril's COO says "We would be behind on our production goals without it" [src-20261020-914a64].
- Net: this is the cleanest software-first control case for the thesis, but note the product today is a manufacturing-engineering copilot (MES / work-instruction layer, adjacent to ArsenalOS, Tulip, Siemens), not AI running the plant from video. Compare with Mind Robotics, which captures the floor video but ships robots.

## Traction and signals
- 2026-10-20 — Out of stealth: $160M Series A at $1.5B co-led by Altimeter, Accel, Khosla with XYZ, 8VC, SV Angel, Felicis; $72M seed led by Accel and Founders Fund; $232M total; CNBC exclusive [src-20261020-914a64] [src-20261020-26c44d]
- 2026-10-20 — Anduril named first design partner and customer, Arda embedded in ArsenalOS; 10 hrs to 15 min on basic work instructions, up to 30 hrs to ~2.5 hrs on complex engineering work [src-20261020-914a64]
- 2026-10-20 — Team disclosed: Bob McGrew, Jakob Frick (co-founders), Augustus Odena (chief AI officer), Alex Mark (CTO) [src-20261020-914a64]
- 2026-03-08 — WSJ: raising $70M at $700M; product described as factory-video model that trains robots plus software coordinating machines and humans from DFM to finished goods [src-20260308-1984ea]
- 2025 — Founded "to speed up American manufacturing" (McGrew) [src-20261020-914a64]

## Economics (what we know)
- Pricing model: not disclosed in any source (per seat, per line, per plant, or outcome-based all unknown).
- Arda's own framing of the problem it replaces: programming conventional automation for one station takes 3-6 months and close to $1M; a new phone stays at full production about four months [src-20261020-914a64] [src-20261020-26c44d].
- Claimed customer value: 40x faster basic work instructions, ~12x on complex engineering work (Anduril) [src-20261020-914a64].
- Capital: $232M raised, no capex (software only) [src-20261020-914a64]. Altimeter's Agrawal: "the price is steep today, but the long-term opportunity is very high" [src-20261020-914a64].
- Headcount, revenue, HQ: not disclosed.

## Open questions
- Data rights: who owns CAD-derived process data, work instructions and any floor video; does Arda train cross-customer models or deploy per customer (Anduril is ITAR, so likely siloed).
- Pricing model and contract structure with Anduril.
- Design partners beyond Anduril; which transformer / electrical equipment makers in the data-centre supply chain.
- When the video model and robot-programming agents ship, and on whose robots.
- Official domain, HQ and headcount (not found; launch press release on BusinessWire could not be fetched).
- Overlap with Anduril's own ArsenalOS roadmap: partner or future competitor.

## People
- Bob McGrew, co-founder: OpenAI research lead 2018-2024 (chief research officer, left Sep 2024); Palantir product/engineering for its first decade; US Army Reserve Detachment 201 [src-20261020-914a64]
- Jakob Frick, co-founder: Palantir, SpaceX [src-20261020-914a64]
- Augustus Odena, Chief AI Officer: Adept co-founder, Google Brain, Meta [src-20261020-914a64]
- Alex Mark, CTO: led engineering at Palantir, IRS Direct File [src-20261020-914a64]
- Investor voices: Apoorv Agrawal (Altimeter); customer voice: Matt Grimm (Anduril co-founder/COO) [src-20261020-914a64]

## What arda.ai says (fetched 2026-10-23) [src-20261023-ddfbcb]
- Website: https://arda.ai/ (resolves the open domain question above). Legal name Arda Industries, Inc.
- Product: AI "single source of truth for manufacturing". Four steps: Translate (CAD, PDFs, PLM, requirements into one product model mapped to a process), Plan (full build plan: operations, tools, quality checks, fixtures, stations, visual work instructions; MEs review), Optimize (supports supply chain, schedulers, technicians; feeds production insights back), Adapt (design revisions propagate to parts, stations, instructions; reallocates resources across lines as demand shifts).
- Proof claimed: "running across multiple lines at a large US manufacturer"; key engineering tasks 5-10x faster. Customer quote: Matt Grimm (Anduril co-founder/COO), "We would be behind on our production goals without Arda."
- Next: "From AI-powered planning to robotic execution" using existing robot hardware plus new AI models.
- Positioning: software-first platform (approach B) running in plants owned by others; team from OpenAI, Palantir (forward-deployed model), Adept.
- Note: the homepage does NOT mention learning from factory video; the video angle comes from press coverage only.
