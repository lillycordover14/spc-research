---
slug: mind-robotics
name: Mind Robotics
aliases: []
website: https://mindrobotics.com
hq: Palo Alto, CA (site); Sunnyvale per Harmonic
founded: 2025
layer: factory-ai
layers: []
model: software-first
what: Rivian spinout building full-stack factory robots (models, hardware, deployment infra) trained on video of skilled operators on live automotive lines; Rivian's Normal, IL plant is the first customer and training site; no humanoids.
fit:
- in-house-software
- data-loop
stage: series-b
total_raised_usd: 1015000000
last_round:
  date: '2026-05-13'
  amount_usd: 400000000
  lead: Kleiner Perkins
  valuation_usd: 3400000000
  source: src-20260513-83aa83 (round); src-20260515-176e26 (valuation per WSJ)
investors:
- Kleiner Perkins (Series B lead)
- Accel (Series A co-lead)
- Andreessen Horowitz (Series A co-lead)
- Eclipse (seed lead)
- Greenoaks
- Bessemer
- Salesforce Ventures
- Redpoint
- Meritech Capital
- SV Angel
- Incharge Capital (Volkswagen venture arm)
- A-Star Capital
- Garuda Ventures
- Prysm Capital
- Bain Capital Ventures
- Rivian (strategic shareholder, ~1/3)
founders:
- name: RJ Scaringe
  role: Founder & Chairman
  prior: Founder & CEO Rivian (2009-present); Mind began as Rivian internal effort 'Project Synapse'
headcount: 91
customers:
- Rivian
harmonic_urn: urn:harmonic:company:66589781
affinity_id: null
pitchbook: null
status: tracking
spc_owner: Lilly
tags:
- factory-video
- robot-density
- automotive
- software-first
sources:
- src-20251104-5c9189
- src-20260311-44ded4
- src-20260513-83aa83
- src-20260515-176e26
- src-20261014-461a42
- src-20261022-eede0b
data_quality: 'Slide 8: >$1B raised, Series A+; Harmonic: Series B 2026-05 at $3.4B. HQ conflict: website footer says Palo Alto, Harmonic says Sunnyvale. Headcount 91 is Harmonic, not press. Bessemer appears in Harmonic investor list but not in any press source. Seed reported as $115M (TechCrunch) and ~$110M (eWeek teaser). No CEO named in any source; Scaringe is chair, Doug Field is President from Oct 2026.'
updated: '2026-10-22'
---

## What they do
Mind Robotics began as Rivian's internal "Project Synapse" and was spun out in Nov 2025 with a $115M Eclipse-led seed, RJ Scaringe as chairman and Rivian as shareholder [src-20251104-5c9189] [src-20260515-176e26]. It trains foundation models on video of skilled operators doing dexterous work on Rivian's live lines in Normal, Illinois, and ships its own robot hardware and deployment infrastructure rather than a software layer on third-party robots [src-20261022-eede0b] [src-20260311-44ded4]. Listed skills are pick and place, sorting, fastening and connector insertion (flexible harnesses, tight tolerances); target tasks are assembly, material handling, inspection and precision manipulation [src-20261022-eede0b] [src-20260515-176e26]. It is explicitly not building humanoids ("Doing cartwheels does not create value in manufacturing") [src-20260311-44ded4]. It raised $1.015B in three closes within about 12 months, most recently $400M led by Kleiner Perkins at ~$3.4B in May 2026, and hired Doug Field (ex-Tesla Model 3 ramp, Apple car, Ford EV) as President in Oct 2026 [src-20260513-83aa83] [src-20260515-176e26] [src-20261014-461a42].

## Why it fits the theme (or doesn't)
- owns-production: no. Rivian owns the plant; Mind deploys into it [src-20260311-44ded4] [src-20261014-461a42].
- in-house-software: yes, models plus hardware plus deployment infrastructure are all built in-house; Rivian's custom silicon may become its robotics processor [src-20260311-44ded4].
- data-loop: this is the whole bet. "Mind is collecting video data at industrial scale" from a live high-volume line [src-20261022-eede0b]. But the data source is also the first customer and ~one-third shareholder [src-20261014-461a42], so the loop is captive to Rivian until a second plant appears.
- mission-critical-output: not yet; no product shown publicly as of Oct 2026 [src-20261014-461a42].
- Net: taxonomy calls this software-first, but it is really a full-stack robot vendor with a captive OEM. For the thesis it is the test of whether a software/robotics vendor can get proprietary process data without owning the plant; the answer so far is yes, by having the plant owner own a third of you.

## Traction and signals
- 2026-10-13 — Doug Field (ex-Tesla SVP Engineering, ex-Apple car lead, ex-Ford Chief EV/Digital/Design Officer) joins as President over product, engineering, operations; Rivian disclosed as first customer owning ~one-third of Mind; no public product yet [src-20261014-461a42]
- 2026-05-15 — Valuation ~$3.4B (WSJ); Salesforce Ventures and VW-tied Incharge Capital in the round; origin as Rivian "Project Synapse" [src-20260515-176e26]
- 2026-05-13 — $400M Series B led by Kleiner Perkins; new Meritech, Redpoint, SV Angel, Incharge, A-Star, Garuda; returning Accel, a16z, Eclipse, Prysm, Bain Capital Ventures, Greenoaks; >$1B cumulative [src-20260513-83aa83]
- 2026-03-11 — $500M Series A co-led by Accel and a16z at ~$2B (WSJ); $615M total; Scaringe says large number of robots deployed by YE2026; traditional robot forms, not humanoids [src-20260311-44ded4]
- 2025-11-04 — Spinout announced in Rivian Q3 letter; $115M seed led by Eclipse (Jiten Behl, ex-Rivian); Scaringe chairman per SEC filing; no website, broad trademark only [src-20251104-5c9189]
- 2026-10-22 — Website lists HQ Palo Alto, Rivian as first manufacturing partner, careers incl. Application Engineer roles [src-20261022-eede0b]

## Economics (what we know)
- Pricing model: not disclosed in any source (per cell, per task, RaaS or sale all unknown).
- Capital: $1.015B raised ($115M + $500M + $400M) in ~12 months before a public product; valuation ~$3.4B [src-20260513-83aa83] [src-20260515-176e26].
- Deployments: one plant (Rivian Normal, IL); robot count not disclosed; Scaringe promised a "large number" deployed by end of 2026 [src-20260311-44ded4] [src-20260513-83aa83].
- Ownership: Rivian ~one-third [src-20261014-461a42]; Rivian may also supply the robotics chip [src-20260311-44ded4].
- Revenue, headcount (Harmonic: 91), unit cost per robot: not disclosed.

## Open questions
- Data rights: does Rivian own the operator video and the trained policies, or does Mind, and can Mind reuse Rivian-derived models at VW or another OEM.
- Who is CEO; Field is President and Scaringe is chair while running Rivian.
- First non-Rivian deployment; whether VW (via Incharge) is a design partner or only an investor.
- Pricing model and whether Mind sells robots, cells or outcomes.
- Robot count live at Normal and which of the four listed skills are in production vs training.
- HQ: Palo Alto (site) vs Sunnyvale (Harmonic).

## People
- RJ Scaringe, Founder & Chairman; Rivian founder and CEO [src-20251104-5c9189] [src-20261014-461a42]
- Doug Field, President (Oct 2026): Tesla SVP Engineering (Model 3 ramp), Apple car project lead, Ford Chief EV/Digital/Design Officer to Apr 2026 [src-20261014-461a42]
- Jiten Behl, Eclipse partner (seed lead), formerly at Rivian [src-20251104-5c9189]
- Ilya Fushman, Kleiner Perkins (Series B lead) [src-20260515-176e26]
