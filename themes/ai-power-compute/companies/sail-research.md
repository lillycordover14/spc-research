---
slug: sail-research
name: Sail Research
aliases: []
website: https://sailresearch.com
hq: San Francisco, CA
founded: null
layer: inference-serving
layers:
- inference-serving
- post-training-models
model: usage-priced
what: 'Inference platform for long-horizon AI agents: API for cost-efficient inference and deployment of open-source models, with customizable completion windows, drop-in API compatibility, and support for fine-tuning and RL rollouts.'
fit: []
stage: series-a
total_raised_usd: 80000000
last_round:
  date: '2026-06-24'
  amount_usd: null
  lead: null
  valuation_usd: 450000000
  source: '[Harmonic, pulled 2026-10-26] valuation publicly disclosed'
investors:
- Sequoia Capital
- Kleiner Perkins
- Redpoint
- CRV
- Theory Ventures
- Abstract
- Neo
- A*
- Vine Ventures
- Lip-Bu Tan
- John Hennessy
- Tri Dao
founders:
- name: Neil Movva
  role: Co-founder
  background: to fill
headcount: 29
customers: []
harmonic_urn: urn:harmonic:company:70335535
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- inference-serving
- batch-inference
- agents-inference
- open-models
- rl-post-training
match_context:
- inference
- agent
- open-source
- model
- tokens
- movva
sources:
- src-20260624-30f6ae
- src-20260825-e500eb
data_quality: Seed card from Harmonic, pulled 2026-10-26. Harmonic lists a 2014 founding date, which conflicts with the co-founder start date (2026-01); treat founding year as unverified. model=usage-priced inferred from 'cost-effective token usage' API description; verify.
updated: '2026-10-26'
---

## What they do
Inference for long-horizon agents on open-source models: flexible completion windows (trading latency for cost), drop-in API compatibility, and fine-tuning / RL rollout support [Harmonic]. 29 people [Harmonic]. Tri Dao (FlashAttention) is an angel [Harmonic].

## Why it fits the theme (or doesn't)
<!-- Walk the fit tests in taxonomy.yml: eases a bottleneck (measurable)? efficiency moat? hardware-agnostic? owns a scarce asset? enterprise customers? lab-resistant? gross-margin path? investable stage? A fit test goes in frontmatter only with a source id. -->
Candidate tests: eases-bottleneck (cheaper tokens for agent workloads), enterprise-customers, investable-stage ($450M valuation is the most accessible of the inference targets).

## Traction and signals
<!-- Dated bullets, newest first, each ending with a source id -->
- 2026-06-24 — Series A; $80M raised to date at a $450M valuation [Harmonic]

## Economics (what we know)
<!-- Pricing unit, gross margin after compute pass-through, efficiency gain vs baseline (framework.md sections 3-4), ACV -->

## Open questions
- Customers and production workloads?
- Pricing and gross margin after compute?
- Efficiency claim vs baseline, customer-verified? (framework.md section 3)
- What happens when NVIDIA, a hyperscaler or open source ships the same thing?

## People
- Neil Movva, Co-founder
