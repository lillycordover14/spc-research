---
slug: gimlet-labs
name: Gimlet Labs
aliases: []
website: https://gimletlabs.ai
hq: San Francisco, CA
founded: 2023
layer: inference-serving
layers:
- inference-serving
model: unknown
what: Serverless inference for AI agents and multi-agent systems; kforge autonomously generates optimized low-level kernels from PyTorch across hardware backends; research on dynamic scheduling and orchestration of AI workloads to hit performance and cost targets.
fit: []
stage: series-b
total_raised_usd: 404300000
last_round:
  date: '2026-09-04'
  amount_usd: null
  lead: null
  valuation_usd: 3000000000
  source: '[Harmonic, pulled 2026-10-26] valuation publicly disclosed'
investors:
- Andreessen Horowitz
- Sequoia Capital
- Menlo Ventures
- Sapphire Ventures
- Tiger Global
- Eclipse
- Factory
- M12 (Microsoft)
- Intel
- Arm
- Samsung Venture Investment
- Prosperity7 Ventures
- Wing Venture Capital
- Emergence Capital
- XTX Markets
- Hudson River Trading
- Lip-Bu Tan
- Raghu Raghuram
- Nick McKeown
- Dylan Field
founders:
- name: Zain Asgar
  role: Co-founder & CEO
  background: Co-founder & CEO of Pixie (acquired by New Relic); ex-Google
- name: Natalie Serrino
  role: Co-founder
  background: Founding engineer, Pixie
- name: Omid Azizi
  role: Co-founder
  background: Founding engineer, Pixie
- name: Michelle Nguyen
  role: Co-founder
  background: Founding engineer, Pixie
- name: James Bartlett
  role: Co-founder
  background: Founding engineer, Pixie Labs
headcount: 64
customers: []
harmonic_urn: urn:harmonic:company:64254025
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- inference-serving
- kernels
- heterogeneous-hardware
- agents-inference
- scheduling
match_context:
- inference
- kernel
- agent
- gpu
- 'ai '
- asgar
- artificial intelligence
sources:
- src-20260807-b6b235
- src-20260809-79a0d9
- src-20260819-e49885
- src-20260914-28316c
- src-20260323-a0cbfc
- src-20260904-a08d96
- src-20260723-741ec4
- src-20251202-9b5fb9
data_quality: Seed card from Harmonic, pulled 2026-10-26. Series A/B lead and amount from company posts [src-20260323-a0cbfc, src-20260904-a08d96]. Customers and pricing unverified.
updated: '2026-10-26'
---

## What they do
Founded 2023 by the Pixie team (observability company acquired by New Relic). Serverless inference built for agents, plus kforge for automatic kernel generation across hardware [Harmonic]. 64 people [Harmonic]. Strategic investors include Intel, Arm, Samsung and Microsoft's M12, which fits a hardware-agnostic thesis.

## Why it fits the theme (or doesn't)
<!-- Walk the fit tests in taxonomy.yml: eases a bottleneck (measurable)? efficiency moat? hardware-agnostic? owns a scarce asset? enterprise customers? lab-resistant? gross-margin path? investable stage? A fit test goes in frontmatter only with a source id. -->
Candidate tests: hardware-agnostic, efficiency-moat, eases-bottleneck. Valuation ($3B) is the main investable-stage question (Q13).

## Traction and signals
<!-- Dated bullets, newest first, each ending with a source id -->
- 2026-09-04 | $300M Series B led by a16z at $3B; Harmonic total $404.3M; press reports about $392M, not confirmed in company posts; billions in contracted revenue, scaling to hundreds of MW managed capacity | src-20260904-a08d96
- 2026-08-19 | d-Matrix principal engineer: Fireworks, Together, Baseten have not announced similar heterogeneous orchestration | src-20260819-e49885
- 2026-03-23 | $80M Series A led by Menlo; customer base tripled, includes a top frontier lab and a hyperscaler | src-20260323-a0cbfc
- 2026-09-04 — Series B; $404.3M raised to date at a $3B valuation [Harmonic]

## Economics (what we know)
<!-- Pricing unit, gross margin after compute pass-through, efficiency gain vs baseline (framework.md sections 3-4), ACV -->
Efficiency test: company claims 3-10x (A) and 5-10x for the same power footprint (B); no baseline hardware, model or customer verification published [src-20260323-a0cbfc, src-20260904-a08d96]. Former Groq VP sets a 50%+ savings bar to win switching [src-20260807-b6b235]. Pricing and gross margin unknown; Gimlet now operates capacity, so margins look like a cloud's.

## Open questions
- Customers and production workloads?
- Pricing and gross margin after compute?
- Efficiency claim vs baseline, customer-verified? (framework.md section 3)
- What happens when NVIDIA, a hyperscaler or open source ships the same thing?

## People
- Zain Asgar, Co-founder & CEO
- Natalie Serrino, Omid Azizi, Michelle Nguyen, James Bartlett, Co-founders
