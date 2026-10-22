---
slug: cuspai
name: CuspAI
aliases: []
website: https://cusp.ai
hq: Cambridge, UK (offices Amsterdam, Berlin, Tokyo, US; Singapore opening)
founded: 2024
layer: materials-rd
layers: []
model: software-first
what: 'Generative AI plus molecular simulation for materials discovery, sold through the ''AI Materials Foundry'': a consortium of 45+ industry, lab and data partners where CuspAI''s MIRA platform designs candidates and partner labs synthesize and test them. Use cases: semiconductor materials, coatings, membranes/sorbents, catalysts, batteries.'
fit:
- in-house-software
- data-loop
stage: series-b
total_raised_usd: 580000000
last_round:
  date: '2026-07-20'
  amount_usd: 450000000
  lead: Kleiner Perkins, NEA (co-leads)
  valuation_usd: 2600000000
  source: src-20260720-840ae3
investors:
- Kleiner Perkins
- NEA
- Lightspeed
- Northzone
- Temasek
- Bezos Expeditions
- Glade Brook
- Lux Capital
- AMD Ventures
- UK Sovereign AI Venture Fund
- Invest-NL
- John Doerr
- Tru Arrow Partners
- StepStone
- Basis Set Ventures
- Giant Ventures
- Touring Capital
- Hoxton Ventures
- NVIDIA
- Samsung Venture
- Hyundai
founders:
- name: Chad Edwards
  role: Co-founder & CEO
  prior: Quantinuum founding commercial lead; BASF; KIT PhD
- name: Max Welling
  role: Co-founder & CTO
  prior: Microsoft VP & Distinguished Scientist; Qualcomm VP; U Amsterdam professor
headcount: 86
customers:
- 'AI Materials Foundry founding members (45+): Applied Materials, Lam Research, Tokyo Electron, Kioxia, Samsung, Hyundai, 3M, AMD, Merck, Henkel, Goodyear, Umicore, Johnson Matthey, Topsoe, Oxford PV, Mitsui Chemicals, others'
harmonic_urn: urn:harmonic:company:54896609
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- autonomous-lab
- software-first
sources:
- src-20260720-840ae3
- src-20260720-02f3fe
- src-20261022-37a0ea
- src-20261022-549759
- src-20261016-29997e
data_quality: 'Slide 8: $450M Series B. Harmonic: $980M total at $2.6B (2026-07); Dealroom profile says $580M total ($30M seed + $100M+ Series A Sep 2025 + $450M Series B), which reconciles with press, so $580M used here [src-20260720-02f3fe]. NVIDIA/Samsung/Hyundai appear in Harmonic as investors and on cusp.ai as Foundry partners; investor status unconfirmed in press. Founders'' prior roles from Harmonic, not re-sourced.'
updated: '2026-10-22'
---

## What they do
CuspAI pairs generative AI with molecular simulation to design new materials and sells access through the AI Materials Foundry, a network launched in 2026 that links compute (Nvidia), frontier models (Meta FAIR), ~30 industrial members, ~15 partner labs and data providers (CCDC, ICSD, Wiley) [src-20260720-840ae3] [src-20261022-37a0ea]. MIRA, its proprietary platform, coordinates candidate design, simulation and experimental validation end to end [src-20260720-840ae3]. Physical synthesis and testing are a partner role (imec, A*STAR, DTU, TU/e, hte, VSParticle, ATLANT 3D) rather than something CuspAI owns [src-20261022-37a0ea]. Members are the buyers of materials R&D: semiconductor equipment makers (Applied, Lam, Tokyo Electron, Kioxia), chemicals (Merck, Mitsui, Henkel, Topsoe) and autos (Hyundai) [src-20261022-37a0ea]. Founded 2024 in Cambridge UK by Chad Edwards and Max Welling; board includes LeCun and Hinton [src-20260720-840ae3].

## Why it fits the theme (or doesn't)
- owns-production: no. Labs are partners in the Foundry; the site's sign-up form has a separate 'Synthesis & Testing Partner' role [src-20261022-37a0ea]. Spend goes to compute and research headcount, not facilities [src-20260720-02f3fe].
- in-house-software: yes. MIRA is proprietary and is the product [src-20260720-840ae3].
- data-loop: partial and the key question. Experimental results come from partner labs on member problems; whether CuspAI retains that data across members is not disclosed [src-20261022-37a0ea].
- mission-critical-output: output is candidate materials for semis/energy, not parts; no qualification or production.
- Net: the software-first control case for layer 4, the way Arda is for factory AI. Contrast with Periodic (owns labs, sells agents) and Radical (owns lab, makes alloys). Not an SPC deal at $2.6B [src-20260720-840ae3].

## Traction and signals
- 2026-07-20 — $450M Series B at $2.6B, co-led by Kleiner Perkins and NEA; Bezos Expeditions, Glade Brook, Lux, AMD Ventures, UK Sovereign AI Venture Fund, Invest-NL, John Doerr new; valuation >4x the Sep 2025 round [src-20260720-840ae3]
- 2026-07-20 — Term sheets had been signed in June at a $400M target; closed at $450M; adding Singapore office to Cambridge, Amsterdam, Berlin, Tokyo, US; Dealroom total raised $580M [src-20260720-02f3fe]
- 2026-07 — AI Materials Foundry launched with 45+ founding members incl. Nvidia (compute), Meta FAIR, Samsung, Hyundai, Hitachi High-Tech, Merck [src-20260720-840ae3]
- 2026-10-22 — Site lists ~30 industry partners (3M, AMD, Applied Materials, Lam, Tokyo Electron, Kioxia, Umicore, Johnson Matthey, Topsoe, Oxford PV, UDC, Qnity), ~15 lab partners (imec, A*STAR, DTU, TU/e, Cambridge, Amsterdam) and data partners CCDC, ICSD, Wiley [src-20261022-37a0ea]
- 2025-09 — $100M+ Series A at $520M valuation [src-20260720-02f3fe]

## Economics (what we know)
- Capital: ~$580M raised; $450M Series B at $2.6B (Jul 2026); Sep 2025 valuation $520M [src-20260720-02f3fe].
- Revenue model not disclosed in any source; Foundry membership looks like a consortium/subscription plus project work, but no pricing is public [src-20261022-37a0ea].
- Use of funds: compute infrastructure, research teams, geographic expansion (US, Europe, Asia) [src-20260720-02f3fe] [src-20260720-840ae3].
- No lab capex: synthesis and testing are outsourced to partners [src-20261022-37a0ea].

## Open questions
- Who owns experimental data generated by partner labs on member projects, and does it compound across members (the data-loop test)?
- What does a Foundry membership cost and what is recurring vs project revenue?
- Any member moved a CuspAI-designed material into production? Tokyo Electron's 'could disrupt the current business model' quote is aspiration, not a result [src-20261022-37a0ea].
- Harmonic $980M total vs Dealroom $580M: which is right?

## People
- Chad Edwards, co-founder & CEO [src-20260720-840ae3]
- Max Welling, co-founder [src-20260720-840ae3]
- Board: Yann LeCun, Geoffrey Hinton [src-20260720-840ae3]
- Partner execs on record: Ian Buck (Nvidia), Rob Fergus (Meta FAIR), Yu Cao (Applied Materials), David Fried (Lam), Sumie Segawa (Tokyo Electron), Patrick Vandenameele (imec) [src-20261022-37a0ea]
