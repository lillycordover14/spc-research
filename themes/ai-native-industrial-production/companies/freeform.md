---
slug: freeform
name: Freeform
aliases:
- Freeform Future
website: https://freeform.co
hq: Hawthorne / Los Angeles, CA
founded: 2018
layer: precision-parts
layers: []
model: owner-operator
what: Builds its own multi-laser metal AM machines (GoldenEye, 18 lasers; Skyfall, hundreds of lasers) with in-house sensors, FPGA/GPU controls and ML that monitor and correct the melt in real time, and runs them as a parts service for aerospace, defense, space and energy customers; does not sell printers.
fit:
- owns-production
- in-house-software
- data-loop
- mission-critical-output
stage: series-b
total_raised_usd: 126000000
last_round:
  date: '2026-02-19'
  amount_usd: 67000000
  lead: null
  valuation_usd: 179000000
  source: src-20260219-2125d7 (valuation per PitchBook via TechCrunch; Harmonic agrees)
investors:
- Founders Fund
- NVIDIA / NVentures
- Two Sigma Ventures
- Boeing
- AE Industrial Partners / AE Ventures
- Threshold Ventures
- Linse Capital
- Apandion
founders:
- name: Erik Palitsch
  role: Founder & CEO
  prior: SpaceX propulsion, ~10 yrs; ran Merlin and Raptor programs
- name: T.J. Ronacher
  role: Co-founder, President (departed by Feb 2026)
  prior: Hyperloop One VP hardware; SpaceX propulsion
headcount: 66
customers:
- Defense Innovation Unit (OTA, Jul 2026)
- undisclosed aerospace/defense/F1/rocket-engine customers
harmonic_urn: urn:harmonic:company:793668
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- additive
- process-control
- inspection-qc
- defense-demand
- capex-financing
sources:
- src-20260219-2125d7
- src-20241024-7f1c2e
- src-20261022-81b3ed
- src-20260901-6e197d
- src-20261022-230f15
- src-20241029-1d136e
- src-20250424-da4c3f
- src-20261020-bac9ca
- src-20261021-da5fb5
- src-20260107-c03729
data_quality: Slide 8 shows $67M Series A; TechCrunch (Feb 2026) calls the $67M a Series B and Harmonic shows Series B at $179M valuation. Legal name Freeform Future Corp. Headcount 66 from Harmonic; TechCrunch says up to 100 hires planned. DIU award value undisclosed.
updated: '2026-10-23'
news_query: '"Freeform" ("metal 3D printing" OR "additive manufacturing" OR Palitsch OR "metal parts" OR laser) -TV -series -episode'
match_context:
- additive
- 3d print
- metal
- palitsch
- laser
- manufactur
- spacex
---

## What they do
Freeform designs and builds its own laser powder-bed metal printers and operates them as a service, delivering finished metal parts rather than selling machines [src-20241024-7f1c2e][src-20260219-2125d7]. The differentiator is the control loop: microsecond-scale computer-vision meltpool monitoring, in-house telemetry on FPGAs and GPUs, and ML models that adjust print parameters live, backed by on-site NVIDIA H200 clusters running physics simulations [src-20241024-7f1c2e][src-20260219-2125d7]. The current GoldenEye system has 18 lasers; the next platform, Skyfall, targets hundreds of lasers and thousands of kilograms of parts per day [src-20260219-2125d7]. It ships hundreds of mission-critical parts a week to undisclosed aerospace, defense, rocket-engine and F1 customers and holds a July 2026 DIU award to scale propulsion and structural hardware [src-20260219-2125d7][src-20261022-81b3ed][src-20260901-6e197d].

## Why it fits the theme (or doesn't)
- owns-production: yes; its own factory and its own machines; 'network of autonomous factories' positioning [src-20261022-81b3ed].
- in-house-software: yes; the whole stack (sensors, controls, telemetry, ML, compute) is built in-house [src-20241024-7f1c2e].
- data-loop: the clearest example in the set; proprietary print-physics data is why NVIDIA invested and is used to raise quality and throughput [src-20241024-7f1c2e][src-20260219-2125d7].
- mission-critical-output: propulsion and structural hardware for space/defense; Boeing came inbound as investor [src-20260901-6e197d][src-20241024-7f1c2e].
- speed-moat: prototype-to-production under one roof; no lead-time numbers published [src-20261022-81b3ed].
- customer-qualification: no AS9100/NADCAP/ITAR visible on the site; open question [src-20261022-81b3ed].
- Model: owner-operator, service only; Palitsch's 2024 position is that they do not sell printers [src-20241024-7f1c2e]. $179M post on ~$126M raised says the market is pricing it as a capex-heavy service bureau, not a software company; the Skyfall throughput step and the DIU demand signal are what would change that.

## Traction and signals
- 2026-10-20: Palitsch joint conversation with Ed Mehr (Machina) on new-process factories [src-20261020-bac9ca]
- 2026-09-01 — DIU other transaction agreement (awarded Jul 2026) under Adaptive Space Manufacturing and Integration at Scale to scale production of propulsion and structural hardware; value undisclosed; Skyfall unveiled earlier in 2026 [src-20260901-6e197d]
- 2026-07-30 — DIU contract announced on company site [src-20261022-81b3ed]
- 2026-03-24 — Fast Company 2026 Most Innovative Companies [src-20261022-81b3ed]
- 2026-02-19 — $67M Series B (Apandion, AE Ventures, Founders Fund, Linse, NVentures, Threshold, Two Sigma); valuation undisclosed, PitchBook $179M; hundreds of parts/week; up to 100 hires and facility expansion for backlog; co-founder T.J. Ronacher departed [src-20260219-2125d7]
- 2024-10-24 — $14M raise with Boeing and NVIDIA; service-only model; NVIDIA supplying H100s; hiring up to 55 [src-20241024-7f1c2e]

## Economics (what we know)
- Throughput: GoldenEye 18 lasers today; Skyfall target thousands of kg/day, i.e. a step-change in revenue per machine if achieved [src-20260219-2125d7].
- Volume: hundreds of mission-critical parts per week on a ~66-person team (Harmonic headcount) [src-20260219-2125d7].
- Capital: ~$126M raised (Harmonic) for a $179M post; $67M Series B funds platform scale-up, hiring and facility expansion; no debt or equipment financing disclosed [src-20260219-2125d7].
- Compute: on-site H200 cluster (an unusual capex line for a parts maker) [src-20260219-2125d7].
- Unknown: revenue, GM, cost per part vs EOS/Velo3D-based bureaus, lead times, pricing, machine count.

## Open questions
- Why was the Series B valuation step-up so small on $67M: dilution-heavy round, slow revenue, or priced as a service bureau? Ask for the revenue run-rate and backlog.
- Will Skyfall be sold or licensed to primes (hybrid) or stay captive? Palitsch said no machine sales in 2024.
- Who are the customers (Boeing? SpaceX-adjacent rocket programs? F1 teams?) and what qualifications (AS9100, NADCAP, ITAR) are held.
- Dollar value and scope of the DIU OTA.
- What changed with Ronacher's departure.

## People
- Erik Palitsch (Founder & CEO; SpaceX propulsion, ran Merlin and Raptor programs) [src-20261022-81b3ed][src-20260219-2125d7]
- T.J. (Thomas) Ronacher (Co-founder, President; departed by Feb 2026) [src-20260219-2125d7]
- Cameron Kay (Head of Talent) [src-20260219-2125d7]

## Deep dive (grokbot, 2026-10-23)

- $67M (Feb 2026), $126M total; DIU OTA Jul 2026. Owns its multi-laser AM machines with real-time ML melt control.
- **Right to win:** machine + process data loop vendor printers lack. Risk: AM qualification time; customers mostly unnamed.
- **Experts:** DIU program office; rocket-engine propulsion buyers.
