# Working thesis — AI-native industrial production

_Seeded from slide 8 of "RoY 2026 Investment Team Priorities" (2026-10-22). This file is the living version: edit it as evidence lands. Every claim should end with a source id once we have one._

## Definition
Companies that build and run their own production capacity, using in-house AI and software to quote, schedule and control robots and machines, and that sell parts or material (or, in layer 5, software that runs plants owned by others).

Two approaches on the slide:
- **Owner-operators**: 1872, Nox Metals, Mariana Minerals, Hadrian, Machina Labs, Senra, Isembard, Freeform, SendCutSend
- **Software-first**: Arda, Mind Robotics (and CuspAI in materials)

## Why now (slide 8 numbers, to be sourced)
- Labor: US manufacturing may need 3.8M more workers by 2033; 1.9M could go unfilled (Deloitte / Manufacturing Institute) [src: TBD]
- Automation: US installed 34,200 industrial robots in 2024 vs 295,000 in China (IFR) [src: TBD]
- Inputs: top refining country holds a 72% average share of key energy minerals; China ~85% of rare-earth refining (IEA) [src: TBD]
- Demand: defense and AI buildout pull on the same $2.96T sector (NAM) with few automated plants [src: TBD]
- Size: ~$1.3T/yr US manufacturing worker earnings (12.6M x ~$107K, NAM); ~$200B US metals distribution (First Research); $6.5T of production outside China exposed to rare-earth supply cuts (IEA) [src: TBD]

## Preliminary thesis (from the slide)
1. Demand for domestic production is structural (labor gap + concentrated supply chains + defense/AI buildout).
2. Owning the plant turns production into proprietary data: data that only exists by running physical production is hard for software vendors to copy, and each part made improves quoting, scheduling and QC (1872's Factory OS).
3. Potential moats: process data from real production; secured capacity, permits, inputs; customer qualification (aerospace/defense approvals take years).
4. Hardware-inclusive producers should be in scope: more capital, lower starting margins, but what matters is the size of the system being compounded. Look for mission-critical output + a software loop.

## What would make us wrong (to test this week)
- The "data loop" is marketing: plants run on bought MES/CAM and the software is thin → these are VC-funded job shops.
- Margins never leave job-shop territory (15-25% GM) and capex per $ of revenue stays ~1:1 → growth equity / infra returns, not venture.
- Software-first vendors (Arda, Mind) get the same data by contract and scale faster without plants → the owner-operator premium disappears.
- Demand is defense-concentrated and lumpy; qualification cycles make revenue slow regardless of automation.
- Incumbents (PCC, Howmet, Nucor, Reliance) automate faster than expected or just buy the startups early.

## Where SPC can play (hypotheses)
- Seed / Series A owner-operators in **metals supply** and **fabrication** (Nox-type, 1872-type) before plant #2 — check sizes fit; the precision-parts layer is already priced (Hadrian $8B, Divergent $2.3B).
- **Layer 4 (materials)**: Radical AI is the only one in range; Periodic/CuspAI are benchmarks.
- **Layer 5 (factory AI)**: Arda at $700M is a stretch; look for the next software-first name with a real plant partner.
- Operator-led angle (SPC's edge): help portfolio companies sell into primes and metals buyers; GTM is the gap for founder-engineers from SpaceX/Tesla.

## Running conclusions
<!-- Agent/Lilly append dated bullets here as the week's evidence comes in. Newest first. -->
- 2026-10-22 — The slide's "two approaches" is really three tiers by capital intensity: (a) capital-light owner-operators that win on software + speed (SendCutSend profitable 8 years, ~$140M run rate, 48h turnaround; Senra 1,000 harnesses/month on an in-house platform with robots deliberately last), (b) capital-heavy owner-operators whose plants are financed off the equity stack (Hadrian: $360M bank revolver + $900M Navy money, "equity never funds factory construction"; Mariana: ~$400M parent plus project capital), (c) software-first vendors that need a captive plant partner for data (Arda inside Anduril's ArsenalOS; Mind Robotics inside Rivian, which owns a third). SPC's edge fits tier (a) best. [src-20260519-38c7ed] [src-20260701-027c1b] [src-20260817-c48f28] [src-20261020-914a64] [src-20261014-461a42]
- 2026-10-22 — "Data loop" is asserted everywhere and evidenced in two places: Freeform (microsecond meltpool vision, ML parameter adjustment, on-site GPU cluster; NVIDIA and Boeing invested for the data) and Mariana (release states each project's operating data improves MarianaOS for the next). 1872's weld model is Path Robotics', Nox's software is quote-to-job tracking on one saw, Senra's Amp is an ERP/MES built in-house but the build is manual. Treat the loop as unproven at seed. [src-20241024-7f1c2e] [src-20260803-30e6d5] [src-20260722-985690] [src-20251110-b1acae] [src-20260715-68183e]
- 2026-10-22 — Seed-stage reality check on the two named owner-operators: 1872 is 18 people, one 30k sq ft plant, energy/utility skids (not defense), seed led by a state-anchored fund; Nox is one aluminum cutting line but a 52-person team with 44 open roles. Both are "factory as the product" pitches ahead of the factory. Right stage for SPC's check; wrong time until plant #1 shows utilization and gross margin. [src-20261016-d61bc1] [src-20261022-2aabbe]
- 2026-10-22 — The precision-parts layer is priced out (Hadrian $7.87B, Divergent $2.3B, Freeform $179M on $126M raised). Isembard is the interesting structural variant: 14 factories in 18 months via a franchise model (franchisee brings CNCs and a building, Isembard brings MasonOS and demand), AS9100/ITAR, turning down orders at $50M Series A. Capital-light owner-operator in a qualification-gated market. [src-20260810-f0371c] [src-20260310-45bab3]
- 2026-10-22 — Factory AI (layer 5) today is work-instruction and engineering agents, not floor-video control: Arda's shipping product converts CAD/design docs into assembly order and work instructions (10 hrs to 15 min at Anduril); the video model is roadmap. Mind Robotics has no public product and ~$1B raised. The sub-$100M version of this layer is the YC crop (Allus, Faraday, Horizontal, Sidekick, Neuron) in _candidates.md. [src-20261020-914a64] [src-20260513-83aa83]
- 2026-10-22 — Policy and inputs are a real tailwind, mostly for metals supply: Section 232 at 50% on steel/aluminum/copper articles since Apr 6 2026; $1.4B OSC/Commerce package for Vulcan Elements' 10,000 t/yr magnet plant eight months after a 10 t pilot; net imports of processed metals doubled to $185B in 2025; US 100% import-reliant on 16 commodities. The financing template for refining is government loan + strategic equity, not venture alone. [src-20260402-1b5d6c] [src-20251103-ee9b27] [src-20260206-04fe3e]
- 2026-10-22 — Slide 8 numbers to refresh before the group meeting: NAM now $2.90T / 12.65M workers / $112K comp; IEA 2026 says China ~72% of refined energy minerals and >90% of REE refining (not 85%); IFR US installs 38,000 in 2025. [src-20261013-a7c995] [src-20260721-89b0cf] [src-20260618-c903cc]
