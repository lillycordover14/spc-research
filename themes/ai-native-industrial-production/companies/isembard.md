---
slug: isembard
name: Isembard
aliases: []
website: https://isembard.com
hq: London, UK (first factory Harlesden, NW London)
founded: 2024
layer: precision-parts
layers: []
model: hybrid
what: Network of software-defined precision machining facilities in the UK/Europe for aerospace, defense and energy; rebuilding sovereign precision-parts capacity.
fit:
- owns-production
- in-house-software
- mission-critical-output
- customer-qualification
stage: series-a
total_raised_usd: 59000000
last_round:
  date: '2026-03-09'
  amount_usd: 50000000
  lead: Union Square Ventures
  valuation_usd: null
  source: src-20260310-45bab3
investors:
- Union Square Ventures (Series A lead)
- Notion Capital (seed lead)
- IQ Capital
- Tamarack Global
- CIV
- 201 Ventures
- Basis Capital
- Foreword Fund
- Material Ventures
- Never Lift Ventures
- NP-Hard Ventures
- Amplifier
- Alex Bouaziz (angel)
- Matt Briers (angel)
- Andrei Danescu (angel)
- Andreas Klinger (angel)
- Charlie Delingpole (angel)
- Joshua Western (angel)
- Salar al Khafaji (angel)
founders:
- name: Alexander Fitzgerald
  role: Founder & CEO (sole founder)
  prior: Founder/CEO Cuckoo (broadband, ~100k customers, sold to Octopus Group 2022); HM Treasury tax policy 3 yrs; Hanbury Strategies; UK Army reservist
headcount: 66
customers:
- Anduril
- Tekever
- ARX Robotics
- UK Government
harmonic_urn: urn:harmonic:company:56658675
affinity_id: null
pitchbook: https://pitchbook.com/profiles/company/713168-47
status: tracking
spc_owner: Lilly
tags:
- machining
- defense-demand
- reshoring
- customer-qualification
- mes
- franchise
- job-shop
sources:
- src-20260310-45bab3
- src-20260810-f0371c
- src-20250929-857f17
- src-20250619-46e43c
data_quality: Headcount 66 per Tech.eu Aug 2026 vs 76 per Harmonic; total raised $59M = $9M seed + $50M A plus undisclosed debt for owned factories; Series A valuation not disclosed (Harmonic estimates ~$250M); seed investor 'Foreword Fund' appears as 'Forward Fund' in Resilience Media; owned vs franchised split of the 14 factories not disclosed.
updated: '2026-10-22'
---

## What they do
Isembard runs a network of small precision-machining factories (CNC milling and turning, some injection moulding) that make components for defence, aerospace, space and robotics customers such as Anduril, Tekever, ARX Robotics and the UK government [src-20260810-f0371c]. Every factory runs on MasonOS, an in-house platform Fitzgerald describes as an ERP for running factories in an integrated way: ML quoting, scheduling, supply chain and inventory, AI inspection, and robotics integration [src-20250929-857f17]. The network is a hybrid of company-owned sites and franchised sites: a franchisee brings a couple of CNC machines, power, coolant and four walls, Isembard brings the software, supply chain and demand, and a site is live in about three months [src-20260810-f0371c]. As of Aug 2026 it had 14 factories (7 UK, 5 US, 1 France, 1 Germany), 66 staff and a target of 25 factories by end of 2026, with Ukraine next [src-20260810-f0371c]. Isembard also plans to license MasonOS white-label to third-party factories [src-20250929-857f17].

## Why it fits the theme (or doesn't)
- owns-production: yes for the company-owned sites; the first factory opened Jan 2025 in Harlesden and owned factories are funded with equity plus undisclosed debt [src-20260810-f0371c] [src-20250929-857f17]. The franchised sites are capacity Isembard directs but does not own, so the model is hybrid rather than pure owner-operator [src-20260310-45bab3] [src-20250929-857f17].
- in-house-software: yes. "We actually build our own software and that's what our factories are running on" (Fitzgerald); MasonOS covers quoting, scheduling, supply chain, manufacturing, QC and delivery [src-20250929-857f17] [src-20260310-45bab3]. CAM / toolpath generation is never claimed, so machine programming may still be off-the-shelf [src-20250929-857f17].
- mission-critical-output: defence and aerospace parts; Anduril and the UK government are customers; demand exceeds supply and orders are being turned down [src-20260810-f0371c].
- customer-qualification: AS9100, ISO 9001, ITAR, Cyber Essentials, JOSCAR listed at MasonOS launch [src-20250929-857f17].
- data-loop: plausible (one platform across 14 sites quoting and scheduling the same part families) but no evidence yet; company claims 40-60% throughput and 30% cost gains without data [src-20250929-857f17].
- speed-moat: no lead-time data in any source; removed until evidenced.
- Net: the European read on Hadrian with a franchise twist. The franchise model scales factory count fast and capital-light, at the cost of control over quality and process data; it is also what makes Isembard a software licensor (hybrid) rather than a pure owner-operator.

## Traction and signals
- 2026-08-10 — 14 factories (7 UK, 5 US, 1 FR, 1 DE), 66 staff, target 25 by YE2026, Ukraine next; customers Anduril, Tekever, ARX Robotics, UK gov; demand exceeds supply, turning down orders [src-20260810-f0371c]
- 2026-08-10 — First franchisee Shawn Rowcliffe (22, ex-Babcock machinist); other franchisees include a restaurant owner, a cardiac nurse, a veteran and an investor [src-20260810-f0371c]
- 2026-03-09 — $50M Series A led by USV; new Tamarack Global, IQ Capital; existing Notion, CIV; angels Bouaziz, Danescu, Briers; 6 factories at announcement; US, UK, DE, FR, UA footprint; hiring engineers in Europe and US [src-20260310-45bab3]
- 2025-09-29 — MasonOS launched at Resilience Conference London; three user groups planned: owned, franchised, white-label licensees; certs AS9100, ISO 9001, ITAR, Cyber Essentials, JOSCAR [src-20250929-857f17]
- 2025-04 — $9M seed led by Notion Capital with 201 Ventures, Basis, Foreword, Material, Never Lift, NP-Hard; undisclosed debt for owned factories [src-20250929-857f17]
- 2025-01 — First factory opened in Harlesden, NW London [src-20260810-f0371c]

## Economics (what we know)
- Franchise unit: ~3 months to set up; franchisee supplies a couple of CNC machines, power, coolant and the building; Isembard supplies MasonOS, supply chain and work [src-20260810-f0371c]. Franchise fee / revenue share not disclosed.
- Plant financing: equity plus undisclosed debt for company-owned factories [src-20250929-857f17]; franchisees fund their own machines [src-20260810-f0371c].
- Company claims for MasonOS: throughput +40-60%, operating cost -30% (unverified) [src-20250929-857f17].
- Scale: 14 factories and 66 staff in Aug 2026 implies under 5 people per site [src-20260810-f0371c].
- Revenue, gross margin, lead times, pricing, machine utilization, capex per site: not disclosed in any source.
- Market framing used by the company: ~$1.8T component manufacturing, ~95% by small shops, average owner over 65, 40% retiring within five years [src-20260310-45bab3].

## Open questions
- Owned vs franchised split of the 14 sites, and whether owned sites are greenfield or acquired job shops.
- How much of MasonOS is in-house: quoting, scheduling and inspection are claimed; CAM, CNC control and MES core may be bought.
- Franchise economics: fee, revenue share, who owns the part data and process data generated at a franchisee.
- Lead times vs incumbents (speed-moat unproven).
- Revenue run-rate and GM; how much of demand is Anduril.
- US plan: 5 US sites exist [src-20260810-f0371c]; where, owned or franchised, and whether the US gets its own entity and ITAR-compliant data boundary.
- Harmonic headcount (76) vs press (66).

## People
- Alexander Fitzgerald, Founder & CEO: age 33, sole founder; Cuckoo broadband founder (sold to Octopus 2022), HM Treasury, Hanbury Strategies, Army reservist [src-20260810-f0371c]
- Shawn Rowcliffe, first franchisee, ex-Babcock machine operator [src-20260810-f0371c]
- Investors on record: Rebecca Kaden (USV), Stephen Millard (Notion Capital) [src-20260310-45bab3] [src-20260810-f0371c]
