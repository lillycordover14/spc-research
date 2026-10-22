---
slug: senra-systems
name: Senra Systems
aliases: []
website: https://senrasystems.us
hq: Redondo Beach, CA (Factory 1); Cypress, CA (Factory 2)
founded: 2023
layer: fabrication
layers: []
model: owner-operator
what: Designs and manufactures aerospace wire harnesses in its own plant on proprietary software (digital-twin conversion, automated work instructions, live status) plus automation.
fit:
- owns-production
- in-house-software
- data-loop
- mission-critical-output
- speed-moat
- customer-qualification
stage: series-b
total_raised_usd: 112000000
last_round:
  date: '2026-07-15'
  amount_usd: 65000000
  lead: Lowercarbon Capital / Interlagos (co-leads)
  valuation_usd: 493000000
  source: src-20260715-fb79c2 (amount, leads, total); valuation per Harmonic, not disclosed in press
investors:
- Andreessen Horowitz
- Sequoia Capital
- Founders Fund
- 8VC
- General Catalyst
- US Air Force / Space Force (contracts)
- Lowercarbon Capital
- Interlagos
- Dylan Field
- CIV
- The Friedkin Group
- Jaws Estates Capital
- Sozo Ventures
- Alumni Ventures
founders:
- name: Jordan Black
  role: Co-founder & CEO
  prior: 'SpaceX: wire harness org, scaled Starship harnesses, led avionics manufacturing R&D; earlier Ford'
- name: Ben Shanahan
  role: Co-founder, Head of AI & Robotics (ex-CTO)
  prior: SpaceX software (wrote Starlink production application software); NeuroPace
headcount: 190
customers: []
harmonic_urn: urn:harmonic:company:12480230
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- defense-demand
- inspection-qc
- labor-gap
- lead-time
- mes
- quoting
- scheduling
- wire-harness
sources:
- src-20260715-68183e
- src-20260715-fb79c2
- src-20260701-027c1b
- src-20260715-821445
data_quality: Series B $65M (Jul 2026), total >$112M per press; Harmonic showed $107M total and $493M post (valuation not in press). Headcount ~190 per Wiring Harness News (Jul 2026) vs Harmonic 116. 'US Air Force / Space Force (contracts)' in investors is legacy from the seed file, not confirmed by 2026 sources. Wiring Harness News profile date is July 2026, exact day not shown (recorded as 2026-07-01).
updated: '2026-10-22'
---

## What they do
Senra (founded 2023, two plants in Redondo Beach and Cypress, CA) designs and builds aerospace and defense wire harnesses, a product that can be about 25% of a vehicle's cost and is still built almost entirely by hand [src-20260715-821445][src-20260715-68183e]. Its in-house platform Amp runs quoting, engineering, work instructions, supply chain, machine programming and quality in one system; technicians build from screen instructions, not drawings [src-20260701-027c1b][src-20260715-fb79c2]. Output is about 1,000 harnesses a month with a target of 10,000 a month in 2027, in runs of roughly 100 to 1,000 units for submarine, land vehicle, launch vehicle and satellite builders [src-20260715-68183e][src-20260701-027c1b]. Senra trains its own technicians in weeks and calls its approach configuration over automation; robots are deliberately last [src-20260715-68183e][src-20260701-027c1b].

## Why it fits the theme (or doesn't)
- owns-production: two factories, ~95,000 sq ft combined, ~190 staff heading to ~300 by end of 2026; Factory 3 funded by the Series B [src-20260701-027c1b][src-20260715-fb79c2].
- in-house-software: Amp is internally built and touches everything except finance: AI BOM reading, live distributor pricing via API, automatic labor estimates, per-station work instructions, one-click strip programs, QMS [src-20260701-027c1b]. Black: "Having it all in the same software is probably the most important thing" [src-20260715-68183e].
- data-loop: every part quoted or built lives in Amp's library; defects, root causes, serials and cycle times are logged and feed estimating; repeat work orders copy in two seconds [src-20260701-027c1b].
- mission-critical-output: harnesses gate vehicle production; Black left SpaceX because harness build time and quality limited the ramp [src-20260701-027c1b].
- speed-moat: quotes in about a day for simple builds; build lead time not published [src-20260701-027c1b].
- customer-qualification: not confirmed in 2026 sources (AS9100, ITAR not stated). Federally certified training program is the stated credential [src-20260715-68183e].
Caveat: the physical build is manual with standard strip/crimp equipment, so today the moat is software thread plus trained labor, not robotics [src-20260715-68183e][src-20260701-027c1b]. Shanahan's move to Head of AI & Robotics is the bet that changes.

## Traction and signals
- 2026-07-15 — $65M Series B co-led by Lowercarbon Capital and Interlagos; General Catalyst, Sequoia, a16z, Founders Fund, Dylan Field, CIV, 8VC, Friedkin Group, Jaws Estates, Sozo, Alumni Ventures; total raised >$112M; proceeds fund Factory 3 [src-20260715-fb79c2][src-20260715-68183e]
- 2026-07-15 — Ken Venner (ex-SpaceX CIO, built Warp Drive; ex-Broadcom) joins as Chief Technology and Product Officer [src-20260715-fb79c2][src-20260715-821445]
- 2026-07-15 — Output ~1,000 harnesses/month across two factories; target 10,000/month by 2027 [src-20260715-68183e][src-20260715-fb79c2]
- 2026-07 — Factory 2 in Cypress opened within months of lease signing, ~80,000 sq ft, 5x footprint expansion [src-20260715-fb79c2]
- 2026-07 — ~190 employees, ~300 expected by year-end; two sites ~95,000 sq ft; 99% first-pass yield; quote turnaround ~1 day to <2 weeks [src-20260701-027c1b]
- 2026-05 — Co-founder Shanahan moves from CTO to Head of AI & Robotics (Harmonic)

## Economics (what we know)
- Quote lead time: ~1 day for simple builds with stock parts, under 2 weeks when supply constrained [src-20260701-027c1b].
- Quality: 99% first-pass yield reported [src-20260701-027c1b].
- Volume: ~1,000 harnesses/month today; 10x target by 2027 [src-20260715-68183e].
- Capex: Factory 2 is leased (opened within months of lease); Factory 3 equity funded from the $65M round; no equipment debt disclosed [src-20260715-fb79c2].
- Pricing: not lowest-price; growth from existing customers and referrals with no BD team historically [src-20260701-027c1b].
- Revenue and GM: not disclosed. Harness shops benchmark at 20-30% GM (prior note, unsourced); Senra's software labor savings would show up here.

## Open questions
- Build lead time (order to ship) vs incumbents, and GM at 1,000/month.
- How much of the 10x volume plan is automation vs headcount (190 to 300 only gets ~1.5x)?
- Certifications held (AS9100, IPC/WHMA-A-620, ITAR) and any prime approvals.
- Customer concentration and named programs.
- Will Amp be licensed to other harness shops (software-first optionality) or stay internal?

## People
- Jordan Black, co-founder and CEO; SpaceX harness org and avionics manufacturing R&D, earlier Ford [src-20260701-027c1b][src-20260715-68183e]
- Ben Shanahan, co-founder, Head of AI & Robotics; wrote Starlink production application software at SpaceX [src-20260715-821445]
- Ken Venner, CTPO since Jul 2026; ex-SpaceX CIO (Warp Drive), ex-Broadcom [src-20260715-fb79c2][src-20260715-821445]
- Investors quoted: Caie Kelley (Lowercarbon), Achal Upadhyaya (Interlagos) [src-20260715-fb79c2]
