# AI-native industrial production: VC primer

_Dated 2026-10-25 (America/Chicago). Overwritten on each rerun. Built from the anip repo: sources/ (1,437 records across all types), companies/, insights/ (signals, questions, thesis, weekly/2026-W43, producers-comparison, software-first-platforms, cross-sector-map, raising-now, repeat-orders-evidence, unit-economics, failures-and-pivots, incumbents-vs-ai-native, materials-science-semis, must-read-sources, huddle-prep). Free sources only; no AlphaSense searches run by the agent (the AlphaSense-arranged expert calls Lilly filed are used)._

**How to read this doc.** Three kinds of statement are kept apart:
- Plain sentence ending in `[src-…]` = sourced fact (a filing, release, dataset or reported figure).
- **Claim (who):** = something a company, founder or expert asserted. Sourced, but not verified.
- `[inference]` = my read. Not sourced; argue with it.

Confidence (`high/med/low`, per taxonomy) is marked on numbers from a deleted post, Wikipedia, Harmonic estimate or a single press article. Contradictions are shown side by side. Excluded from the category by Lilly and not covered except as failure examples: microagi, Pelico, C-Infinity, Dirac, Synera, Bright Machines (failure example only), Retrocausal, DEEP.FINE.

---

## 0. Decision summary (read first)

**Verdict [inference].** Back capital-light owner-operators at Series B only where speed and qualification are already paid for (Senra, Freeform, Isembard, as diligence hypotheses). Use Hadrian, Divergent and SendCutSend as benchmarks. Do not pay software multiples for job-shop economics until a company shows unit cost or quality improving with volume. Nobody in the repo shows that yet.

**What the 13 expert calls (read line by line) changed.**
1. **Price is not the wedge.** The only "cheaper" report (Raytheon, about 50% lower) came from RFQ quotes before any part was delivered, on a relationship brokered by RTX Ventures, a Hadrian investor [src-20250708-2aa3ad]. A Boeing customer says Xometry is cheapest and a 20-25% price gap means re-sourcing [src-20260802-ef6506]. Three Boeing voices say parity or more: "we have actually paid probably more" (Boeing Defense head of product) [src-20260818-9b2d5c]; Hadrian priced at "PCC or slightly more" (Boeing strategy/M&A lead) [src-20250712-e5e110]. A Northrop GM: "Cost is secondary. Cost is driven usually by schedule" [src-20250707-3b7a46]. The premium buyers pay is for speed.
2. **Quality at complexity is the open risk.** "None of their parts right now are flying" (Boeing Defense) [src-20260818-9b2d5c]. "We haven't received parts back that matched the specification" (PI, ex-Anduril hardware) [src-20250709-43486e].
3. **Share per customer is capped by design.** SpaceX caps a shop at about 1/3 of its revenue (ex-Hadrian head of engineering) [src-20250708-342eaf]. After a PCC factory fire, Boeing "will never" concentrate one part family on one supplier [src-20260818-9b2d5c]. Revenue per customer has a ceiling, so growth needs many primes [inference].
4. **The moat is workflow plus qualification, and AI CAM is coming from below.** Insiders say the edge is the Opus MES plus factory design, not toolpath AI [src-20260817-8867f2][src-20261004-9b47f5]. CloudNC sells CAM Assist to every shop and tests it in its own UK factory [src-20261009-7cafd0]. Programs last about 50 years, and suppliers for a 2035 aircraft are being chosen now [src-20260818-9b2d5c].
5. **Materials-rd budgets are not growing fast.** A former Moderna director says buyer budgets have not grown "crazily" in 5-6 years and that the gain is a "step one productivity boost" [src-20260909-af3e60] (low). An Albert Invent director says chemical majors reject royalty models ("The short answer is no") [src-20260913-3ad55e].

6. **OTA work hides the quality gap.** OTA contracts waive many mil-spec quality requirements; when programs move to standard production contracts, "there's a gap" in statistical lot inspection that Hadrian "is still maturing" on. At thousands of parts its cost curve "asymptotes at a higher level" than traditional shops, and schedule is "near equal" once full inspection is counted (Boeing executive director, customer spending "low single millions" a year, "a fraction of a percent" of outside spend) [src-20260908-ed94f0]. He thinks "low tens of millions" could replicate Hadrian; a Northrop customer engineer thinks it is hard to copy [src-20260802-36d46c].
7. **Distributed networks win on urgency, not cost.** An Isembard customer paid $2,300-3,000 for 4-5 simple parts in 2-3 days that would cost about GBP150-200 in China, and sends larger batches to Chinese shops [src-20260621-f96bbd]. An Airbus Defence supply-chain head sees such networks limited to prototypes and non-critical parts while primes consolidate to fewer tier-1s [src-20251106-dfddcb].
8. **The only learning-over-time number.** Hadrian's first programming head: "within a couple of years, we saw a 50% cut" in order-to-first-article time; 70% 24-hour utilization is "very, very realistic"; pricing targets about 30% contribution margin; Opus "is replicable" and the moat is "financial power" plus a five-year head start [src-20261004-9b47f5].

**Evidence on the four thesis claims** (claims as numbered in insights/thesis.md)

| # | Thesis claim | For | Against | Read [inference] |
|---|---|---|---|---|
| 1 | Demand for domestic production is structural | Lockheed 7-year cell deal [src-20261014-015327]; Navy $900M [src-20260320-67ba4c]; Thales CPO: capacity is the pain after COVID-era supplier bankruptcies [src-20251110-84b67e]; Boeing has used parts taken from non-flying aircraft [src-20260818-9b2d5c] | 34% spindle utilization at existing shops [src-20250120-419768]; Taiwan 20-30% cheaper and Vietnam/Malaysia cheaper still [src-20250709-43486e]; Boeing makes about 40% of parts in-house and holds 6 months of inventory [src-20250712-e5e110] | True for defense capacity and speed. Commercial rate demand not shown |
| 2 | Owning the plant creates a data loop | Freeform and Mariana score 2 (section 6). Ex-Hadrian: about 80% of non-CAM labor automated, lead times cut about 50% [src-20250708-342eaf]; reprogramming saved 50-80% of CAM time [src-20260611-7b80f0] | Toolpaths come from third-party CAM, with Vericut as the check [src-20260611-7b80f0][src-20261004-9b47f5]; CMM inspection is manual [src-20260817-8867f2]; a buyer asks "is it actually" software-enabled [src-20250729-a0a78c] | Workflow automation is real. Learning with volume is not evidenced |
| 3 | Moats: process data, secured capacity, qualification | Trusting a new supplier takes 5-10 years [src-20250712-e5e110]; change-of-control clauses in defense contracts [src-20260817-8867f2]; lock-in from 50-year programs [src-20260818-9b2d5c] | Share caps (finding 3); 90% of the first 10 Hadrian employees gone by year 5 [src-20260817-8867f2]; incumbent PCC is also automating [src-20250712-e5e110] | Qualification is a moat once paid, but it caps share. No data moat evidenced |
| 4 | Hardware-inclusive producers can return venture outcomes | SendCutSend profitable 8 years [src-20260519-38c7ed]; Hadrian plants are debt-funded [src-20260817-c48f28] | "Not ... a fantastically profitable business"; a six-machine plant 1 cost "well north of $10 million" [src-20260817-8867f2]; net per-part saving after capex is 20-30% at best [src-20250712-e5e110]; Hadrian is "better suited to debt than VC" (ex-Anduril PI) [src-20250709-43486e] | Unproven. Underwrite the speed premium and the debt capacity, not cost leadership |

---

## 1. The thesis in plain English

**What it is.** AI-native industrial production means companies that build and run their own factories (or, in one variant, the software that runs other people's factories) and sell the output: parts, metal, material. The product is the physical thing; the software is how they make it faster and with fewer skilled people than incumbents. SPC's slide 8 frames it as producers "that build and run their own production capacity, using in-house AI and software to quote, schedule, and control robots and machines" [src-20261022-80fd75].

**Legacy vs AI-native.**

| | Legacy | AI-native |
|---|---|---|
| Who | Job shops (small owner-run machine or fab shops that build to a customer's drawing), service centers (metal distributors that stock, cut and ship metal), brokers and marketplaces | Hadrian, SendCutSend, Senra, 1872, Nox, Mariana |
| Software | ERP and CAM bought off the shelf (CAM = software that turns a 3D model into machine toolpaths; ERP = the back-office system of record) | Built in-house around quoting, nesting (packing parts onto a sheet or block to minimize scrap), CAM automation, scheduling, robot control and inspection |
| Speed | Average aerospace part 8-12 weeks, 40% late or with quality issues [src-20251024-2e5383] (med, single memo) | **Claim (SendCutSend):** 48 hours design to delivery [src-20260227-e92d45]; **Claim (Senra):** harness lead time six months to two weeks [src-20260128-a16c79] |
| Learning | Knowledge sits in the heads of machinists averaging early-60s in age (**Claim, Chris Power**) [src-20260908-65fab6] | Thesis: every part made improves the next quote, schedule and QC. Evidenced at 2 of ~15 names (section 6) |

**Three business models** (taxonomy `model`):

| Model | Best example | Tradeoff |
|---|---|---|
| owner-operator | SendCutSend: owns all its lasers and plants, bootstrapped to a $1.01B round in May 2026 [src-20260519-38c7ed], then a Series B at $2.1B five months later [src-20261020-487a39] (med, single trade write-up) | Owns the data and the margin; carries the capex and utilization risk |
| software-first | Arda: CAD-to-work-instructions agent inside Anduril's ArsenalOS; $160M Series A at $1.5B [src-20261020-914a64] | Capital-light, fast to revenue; needs a host plant for data and competes with Siemens/NVIDIA/Rockwell on the installed base [src-20260106-60b745] |
| hybrid | Hadrian (owns factories, now embeds cells inside Lockheed's Grand Prairie plant on a 7-year deal) [src-20261014-015327]; Isembard (owned plus franchised factories on MasonOS) [src-20260909-b547c7] | Tries to get owner data with partner capital; harder to underwrite because economics are split |

The core tradeoff in one line: owner-operators buy data ownership and pricing power with capital intensity; software-first buys speed and margin with data dependence on someone else's plant [inference].

---

## 2. Why now: the drivers, ranked

Ranked by how much each driver actually moves revenue for the companies we track [inference on the ranking].

### 2.1 Defense demand and munitions/shipbuilding ramps (structural for 5-10 years; budget-cyclical at the margin)
- Mechanism: primes cannot add qualified capacity fast enough; they are now signing multi-year capacity deals with new producers.
- Evidence: Lockheed signed a 7-year agreement to put Hadrian automated cells inside its Missiles and Fire Control plant for PAC-3 MSE, THAAD, PrSM and GMLRS, commissioning early 2027 [src-20261014-015327]. Navy put $900M alongside >$1.5B of Hadrian capital for three maritime plants (Virginia/Columbia submarine parts) [src-20260320-67ba4c]. Divergent will build Tomahawk structures for RTX [src-20260601-976843] and is opening a Long Beach factory sized for 30,000 missile airframes or 60,000 warhead casings a year [src-20261023-e02543]. Army selected Vulcan Elements for magnets for SkyFoundry, a 1M-drones-a-year target [src-20260923-c53c99].
- **Claim (Chris Power):** submarine labor hours per boat rose from ~13M to 70M+; Virginia/Columbia built at ~0.6/yr vs ~2 bought; the enterprise is ~50M labor hours a year short [src-20260610-779f8b].
- Expert view: DoD supply base is "a limited pool of qualified suppliers operating at high utilization"; one Raytheon program manager reports 80-90% utilization at suppliers and 9-10 months for castings [src-20250708-2aa3ad].
- Layers: precision-parts, fabrication, metals-supply (magnets). Durability: high while munitions stockpiles are rebuilt [inference].

### 2.2 Skilled labor gap (structural)
- Mechanism: the binding constraint is machinists, welders and programmers, not machines. Software that deskills tasks expands who can run a plant.
- Evidence: Deloitte/MI (Apr 2024) project 3.8M manufacturing jobs needed 2024-2033, 1.9M possibly unfilled [src-20240416-b69154]. The 2026 follow-up counts 2.3M technician openings 2025-2030 [src-20260910-a2cd42] (different scope; do not add to the 3.8M). Manufacturing openings were 522,000 in Aug 2026 vs 432,000 pre-pandemic average [src-20261013-a7c995]. DoD METAL program says the industrial base needs at least 122,000 more shipbuilders, engineers and critical roles by 2028 [src-20250101-af28c1] (page undated).
- **Claim (Hadrian):** Opus trains new operators in 30-40 days instead of a decade [src-20260926-70087f]; 40-hour tasks to 2 hours [src-20261022-002ed8].
- Layers: all producing layers; strongest in precision-parts and fabrication.

### 2.3 Reshoring and tariffs (policy-driven; reversible)
- Section 232 (a 1962 statute letting the President set tariffs on national-security grounds): steel and aluminum went from 25% to 50% in June 2025; the April 2, 2026 proclamation (effective April 6, 2026) sets 50% on articles made entirely or almost entirely of steel, aluminum or copper, 25% on derivatives, and 10% on derivatives made with US-melted or US-smelted metal; grid and industrial equipment gets a temporary 15% (10% with US inputs) until Jan 1, 2028 [src-20260402-1b5d6c].
- Effect visible in incumbents: Reliance cites aluminum prices "historically elevated largely due to" the 50% tariff [src-20260728-ae7dea]; Nucor cites Section 232 plus AD/CVD reducing imports, gross margin 20% vs 14% a year earlier [src-20260812-77d6f5].
- Mechanism: a 10% vs 25% gap rewards anyone who can document US melt provenance, which favors software-native suppliers over brokers [inference, also argued in src-20260402-1b5d6c takeaways].
- Layers: metals-supply first, fabrication second.

### 2.4 Supply-chain trust and offshore concentration (structural)
- China leads refining for 19 of 20 strategic energy minerals with ~70% average share [src-20250521-c62d29]; produces ~94% of rare earth magnets and cut magnet exports in April 2025 [src-20251103-ee9b27]. IEA estimates ~$6.5T of downstream production outside China at risk if magnet export controls are fully enacted [src-20260721-89b0cf].
- US 2025 net import reliance: 100% for 16 commodities, rare earths 67%, refined copper 57%, lithium >50% [src-20260206-04fe3e].
- Offshore lead time: **Claim (SendCutSend):** China lead times two to three weeks vs its 48 hours, and US steel costs ~2x China [src-20260227-e92d45]; **Claim (Belosic):** can meet or beat China on only ~20-25% of work [src-20260519-2d6ceb].
- Layers: metals-supply (refining, magnets) most; precision-parts via ITAR (US-persons-only export control on defense articles) which keeps work onshore regardless.

- Bear: an ex-Anduril hardware lead says Taiwan is only 20-30% cheaper but more reliable, and Vietnam/Malaysia stay "significantly cheaper" even with tariffs [src-20250709-43486e]. Offshore cost gaps have not closed for volume work.

### 2.5 Capital availability (cyclical; currently abundant)
- Venture: Hadrian $1.37B Series D at $7.87B [src-20260807-b0dc5b]; Mariana $310M B [src-20260803-30e6d5]; Arda $232M total [src-20261020-914a64]; Mind Robotics >$1B in ~12 months [src-20260513-83aa83].
- Bank debt: Hadrian $360M revolver, Morgan Stanley lead plus 7 banks [src-20260817-c48f28]. **Claim (Mehr):** Machina equipment debt ~2-3% over prime [src-20260320-1361e2].
- Government: Office of Strategic Capital (OSC, DoD's lender for critical-tech companies) [src-20260908-f6558e]: $620M direct loan to Vulcan in a $1.4B package [src-20251103-ee9b27]. IEA: public minerals finance commitments quadrupled 2023-2025 to $65B [src-20260716-6a06e4].
- OTAs (Other Transaction Agreements, fast non-FAR prototype contracts that can roll into production without re-competition; $500M prototype cap) [src-20241219-9f8fcc]: DIU OTA to Freeform [src-20260901-6e197d].
- Read: equity funds plant #1; banks and government fund plants #2+ once a plant is proven [inference, consistent with src-20260807-b0dc5b].

### 2.6 Cost and capability of AI, vision and robotics (enabling, not sufficient)
- What changed in 24 months (from the repo): US robot installs back to growth, 38,428 in 2025 (+12%), US passed Japan for #2 [src-20260924-28b59b]; global installed stock 5.08M [src-20260924-28b59b]. Path Robotics' Obsidian weld model is now a supplier to 1872 [src-20260722-3bc2d8]; Freeform runs H200 clusters on site for real-time meltpool control [src-20260219-2125d7]; LLM agents now read CAD and write work instructions (Arda: 10 hours to 15 minutes at Anduril) [src-20261020-914a64].
- Counterpoint: US metalworking robot adoption is small, ~3,000 units a year [src-20260618-c903cc]. Hadrian's former head of programming says Opus relies on mature third-party CAM for toolpathing and its edge is workflow, not unique technology [src-20261004-9b47f5].
- Gap: the repo has no source quantifying the cost decline of vision sensors, GPUs or robot cells over 24 months.
- Layers: factory-ai and materials-rd depend on this most.

### What would break "why now"
Tariff reversal or court limits would hit metals-supply and fabrication margins first (the 10%/25%/50% structure is a proclamation, not a statute) [inference]. A flat defense budget or delayed munitions buys would stall precision-parts plants built ahead of contracts; Power himself says ~$1B of capex must be deployed ahead of contracts [src-20260921-876080]. Higher rates matter because plants #2+ are debt-funded [inference]. AI over-claiming is already visible: the data loop is evidenced at only 2 of ~15 names (section 6), and Mehr publicly criticizes "SpaceX cosplay and an AI bump" [src-20261021-da5fb5]. Robot learning is far from production reliability: one-shot task success ~59-66% vs 99.9%+ needed [src-20260904-267293]; an investor notes even 99% accuracy is too low on a line [src-20261013-c6e3c0]. Demand is not the only constraint: average VMC in-cut spindle utilization is 34% vs a 70% target, so existing shops have slack before anyone needs new plants [src-20250120-419768] (med, survey). The domestic base has shrunk for 20 years (4,874 machine shops lost 2002-2018, -20%) and defense rides on commercial tier 2-3 volume, which VC-built defense plants do not replace [src-20250909-29c826].

---
## 3. Market size by layer

No layer has a clean, free TAM. Where only a proxy exists, it says so.

| Layer | Figure | Year | Source | Conf. | Note |
|---|---|---|---|---|---|
| All manufacturing | $2.90T value added; 12.65M employees; $112,261 avg comp | 2025 | NAM facts [src-20261013-a7c995] | high | 10.1% of GDP |
| metals-supply (distribution) | ~$200B revenue, ~9,400 establishments, top 50 ~50% | 2025 | First Research [src-20251201-4b732d] | med | Service centers only, not refining |
| metals-supply (refining) | Market size not found; public finance commitments $65B | 2025 | IEA [src-20260716-6a06e4] | high | Gap: US refining TAM |
| precision-parts (shop base) | Machine shops (NAICS 332710): 17,156 establishments, 223,313 employees, $14.23B payroll; 83% under 20 staff; down from 17,433 in 2022 | 2023 | Census CBP [src-20250626-23f6d9] | high | Counts, not revenue. IBISWorld says 16,619 businesses [src-20260201-adef50] (med) |
| fabrication (shop base) | Architectural and structural metals (3323): 14,533 est, 423,013 employees, $28.26B payroll; sheet metal work 4,652 est; structural fab 3,434 est | 2023 | Census CBP [src-20250626-23f6d9] | high | No free revenue TAM |
| metals-supply (service centers, Census) | Metal service centers (423510): 8,608 est, 145,207 employees, $12.40B payroll | 2023 | Census CBP [src-20250626-23f6d9] | high | vs ~9,400 per First Research |
| precision-parts | ~$71B precision manufacturing by 2026; machine-shop segment >$60B | 2026 | Contrary memo [src-20251024-2e5383] | med | Single analyst memo, citations not traced |
| precision-parts (global framing) | "~$1.8T a year" component manufacturing | 2026 | **Claim (Isembard)** [src-20260310-45bab3] | low | Company PR; no method |
| materials-rd | No TAM in repo | n/a | n/a | n/a | Gap |
| factory-ai | Global robot installs value $18.6B | 2025 | IFR [src-20260924-28b59b] | high | Proxy for automation spend, not software |

Fragmentation (supports a consolidation or software-native entrant story):
- 83% of the 17,156 US machine-shop establishments had under 20 employees in 2023 [src-20250626-23f6d9] (high). Contrary says ~90% have <20 employees and <$7M revenue [src-20251024-2e5383] (med).
- **Claim (Belosic):** ~93% of manufacturers have ≤100 employees, ~75% of those ≤20 [src-20260519-2d6ceb].
- **Claim (Isembard):** ~95% of production by small businesses, average owner over 65, 40% plan to retire within 5 years [src-20260310-45bab3].
- DoD: aerospace/defense primes fell from 51 to 5 since the 1990s; castings and forgings face high barriers to entry [src-20220215-45c353].

---

## 4. The five layers

### 4.1 metals-supply (mining, refining, magnets, service centers)
- **Players:** Mariana Minerals (copper, lithium; owner-operator) [src-20260803-30e6d5]; Vulcan Elements (NdFeB magnets) [src-20251103-ee9b27]; Nox Metals (automated service center, `passed`) [src-20261009-404b9b]; candidates Hertha (iron/steel), Cyclic, Mass Magnetics, Duranium (`_candidates.md`). Incumbents: Reliance, Ryerson, Nucor, MP Materials.
- **Economics:** service centers earn 18-32% gross margin (Ryerson 17.7% Q2'26 [src-20260729-407fd7]; Reliance 27.9% LIFO, 31.6% FIFO Q3'26 [src-20261021-16bb64]). Refining economics: gap.
- **AI-native change:** **Claim (Mariana):** MarianaOS halves 5-10 year project timelines [src-20260803-30e6d5]; mine ~50% autonomous with RL agents adjusting process control every 15 minutes [src-20260623-d1790b]. **Claim (Nox):** quote in minutes vs 3-5 days at brokers [src-20250813-5ee11b].
- **Risks:** commodity price; permitting; offtake concentration (Vulcan's offtakes are mostly government) [src-20251103-ee9b27].
- **Why it matters:** policy pull is strongest here (OSC, Section 232, IEA) [inference].

### 4.2 fabrication (sheet metal, welding, forming, harnesses)
- **Players:** SendCutSend (owner-operator) [src-20260519-38c7ed]; Senra (wire harnesses) [src-20260701-027c1b]; Machina Labs (robotic sheet forming, hybrid) [src-20260204-ce7053]; 1872 (robotic steel fabrication) [src-20260722-985690]; candidates Atomic Industries (tool and die) [src-20261023-a3bfe7], Advanced Metal Research.
- **Economics:** SendCutSend profitable for eight years [src-20260519-38c7ed]; ~$140M run rate per a deleted post (low) [src-20260504-c3ded5]; "nine digits" of revenue per Sequoia's Reed [src-20261020-487a39] (med).
- **AI-native change:** instant quoting plus auto-nesting; Senra quotes in ~1 day and claims 99% first-pass yield (FPY: share of parts passing inspection first time, no rework) [src-20260701-027c1b].
- **Risks:** low-mix volume ceiling; Machina cycle times are 30 minutes to hours per part vs seconds for stamping [src-20261023-c3b62f].

### 4.3 precision-parts (CNC machining, additive, castings, composites)
- **Players:** Hadrian (hybrid) [src-20260807-b0dc5b]; Divergent (hybrid) [src-20250915-311606]; Isembard (hybrid franchise) [src-20260909-b547c7]; Freeform (owner-operator AM) [src-20260219-2125d7]; Amca (acquire-and-upgrade) [src-20260520-af3e6c]; Fabri (casting) [src-20260617-4dfb96]; Layup (composites) [src-20260602-a7b79e]; Hybron [src-20260413-abc797]. Incumbents: Howmet, PCC, ATI, Carpenter, Proto Labs, Xometry.
- **Economics:** Proto Labs FY25 GAAP gross margin 44.5% [src-20260206-8bb619], factory 49% vs network 31% [src-20260206-2b13c7]; Xometry marketplace 34.7% [src-20260224-a7b149]; Howmet engine products EBITDA margin 37.7% [src-20260806-9a83f7]. **Claim (Rolls-Royce engineer):** small shops want low double-digit margins [src-20251120-0c271b]. **Claim (ex-Hadrian programming head):** a typical shop can go from 15% to 30% margin in 12-18 months with Hadrian-style ops [src-20261004-9b47f5].
- **AI-native change:** **Claim (Raytheon manager):** Hadrian ~50% lower price at ~1/3 lead time [src-20250708-2aa3ad]. Contradicted below (section 8).
- **Risks:** customer qualification (AS9100 = aerospace quality management standard; NADCAP = industry accreditation for special processes like heat treat and NDT) takes 9-12 months for suppliers [src-20250708-2aa3ad] and 1-2 years per Northrop [src-20260802-36d46c]; layer is now priced at $7.87B for the leader [inference: priced out for SPC]. **Failures in this exact model:** Daedalus (ex-OpenAI founder, AI-run CNC factory, Karlsruhe, $21M A led by NGP) entered insolvency Aug 2026 [src-20260801-4532f6][src-20251203-fc28ea]; VulcanForms laid off >20% in 2023-24 and lost large customers (anecdotal) [src-20240910-5d51ed], replaced its founder CEO [src-20240919-72efcc], then raised $220M [src-20260130-365541]. Ex-Hadrian engineer: a six-machine first factory cost "well north of $10 million" and "manufacturing is not actually a fantastically profitable business" [src-20260817-8867f2].

### 4.4 materials-rd (self-driving labs, AI materials discovery)
- **Players:** Periodic Labs [src-20261022-682e62]; CuspAI (software-first) [src-20261022-37a0ea]; Radical AI (owner-operator lab) [src-20260617-f9d293]; Lila Sciences (candidate). Incumbent-adjacent: Microsoft Discovery, Citrine.
- **Economics:** **Claim (CuspAI primer, AlphaSights):** custom programs 5-15% gross margin, platform 85-90%; pilot conversion 40-50% [src-20261016-29997e] (med).
- **AI-native change:** **Claim (Radical):** 8-20 alloys a day, target 100/day; $60-300 per experiment; samples grams to 500 g, no manufacturing yet [src-20260617-f9d293]. **Claim (Fedus, Periodic):** at full throughput, 4 months of experiments in under 2 weeks [src-20260917-1bcb81].
- **Risks:** no revenue disclosed at any of the three; valuations ($2.6B to $7.5B) precede product [inference]. Track record of the underlying science is mixed: Berkeley A-Lab's claimed 41 new materials were challenged as mostly misidentified known phases, with a Nature correction [src-20240124-513fd9]; MatterGen is limited to ~20 atoms per cell and needs DFT validation [src-20261022-3e2a9d]; Lila's catalysts are unproven in a real electrolyzer [src-20261019-392916]. Business model is unproven: an Albert Invent director says chemical majors have not bought royalty models and the problem is "millions of SKUs", not crystal structures [src-20260913-3ad55e].
- **Buyer view (expert calls, read line by line).** Former Moderna director: buyers reach these platforms through CROs and pay per successful candidate; of the last 10 campaigns CuspAI won 8, Radical 1 and Lila 1 (claim); long-run potential ranked Radical > Lila > CuspAI > Periodic; CRO book-to-bill was "very bad" in 2024-25 [src-20260909-af3e60] (low: several claims cannot be checked). Albert Invent director (a competitor, so biased): ACVs run from hundreds of thousands to millions; procurement "shut[s] down" big sticker prices; the proof that opens budgets is a product launched in "one-third the number of iterations"; his $100 split is CuspAI $50, Lila $35, Periodic $15 [src-20260913-3ad55e].

### 4.5 factory-ai (software for other people's plants)
- **Players:** Arda (CAD to work instructions) [src-20261020-914a64]; Mind Robotics (Rivian spinout, robot foundation models) [src-20260513-83aa83]; candidates Rapta, Allus, Faraday. Incumbents: Siemens (with NVIDIA, Altair, Dotmatics) [src-20260106-60b745][src-20250326-cc1810][src-20250701-a7fef9], Rockwell (GM 49.5%) [src-20260804-0e8130]. MES (manufacturing execution system: software that tracks and directs work on the shop floor) is the incumbent category.
- **Economics:** **Claim (Arda):** usage-based pricing [src-20261020-a1e174]; no revenue disclosed.
- **AI-native change:** work-instruction agents are the only shipped wedge (Arda at Anduril) [src-20261020-914a64] [inference].
- **Risks:** distribution vs Siemens/Rockwell; data rights sit with the host plant [inference]. Investor view: model capability is not the constraint; value needs unified plant data and workflow change [src-20261006-6265ad]. Mind Robotics has raised >$1B and still shown no robot publicly [src-20261013-cc78c0]. Bright Machines, the earlier software-defined-factory bet, failed its SPAC and pivoted to AI-server assembly [src-20240926-fd90fb].
- **AI CAM and inspection (promoted from the skipped pile in this audit).** CloudNC's CAM Assist generates 3-axis and 3+2-axis machining strategies in minutes inside GibbsCAM, with the programmer reviewing each step; CloudNC runs its own Chelmsford factory as a test bed [src-20261021-9769d1][src-20261009-7cafd0]. AI Robotics (DGIST spinout) runs weld-bead inspection on 24 lines in 3 countries on more than 4M field data points [src-20261011-a8b14d]. Both are software-first wedges that give incumbents the same tools [inference].

---

## 5. Company profiles

Every file in `companies/` whose status is not `not-a-fit`. Full profiles for tracking, passed and `candidate` files with a deep dive; one-line table for the remaining candidates and incumbents. Ordered by relevance to an SPC Series B-D check [inference on ordering].

### 5.1 Senra Systems | fabrication | owner-operator | tracking
- **What:** wire harnesses and cable assemblies for defense and space, own plants (~95,000 sq ft over two sites) [src-20260701-027c1b].
- **Capital:** $65M Series B Jul 2026, total >$112M [src-20260715-68183e]; valuation not in press; Harmonic $493M post [Harmonic] (low).
- **Customers:** Anduril, L3Harris, Northrop [src-20260128-a16c79]; growth mostly from existing customers and referrals [src-20260701-027c1b].
- **Software:** Amp, in-house platform touching everything but finance: AI BOM read, live distributor pricing, auto labor estimates, work instructions [src-20260701-027c1b].
- **Claims (Senra):** 99% FPY; 1,000 harnesses/month going to 10K/month in 2027 [src-20260715-68183e]; ~190 staff to ~300 by YE2026 [src-20260701-027c1b].
- **Conflict:** headcount ~190 (Wiring Harness News) vs 116 [Harmonic].
- **Valuation (conflict):** $65M Series B at $11.47/share, $492.96M post, $105.41M total (Forge) [src-20260715-8161a3] (low) | $422.8M (PrivateMarketView, not filed) (low). Company disclosed no valuation.
- **Fit:** owns-production, in-house-software, mission-critical-output, customer-qualification. Data-loop partial. [inference]
- **Why it matters:** best-fit Series B-sized owner-operator in the repo; harnesses are ~95% outsourced even at SpaceX (**Claim, Senra**) [src-20260715-821445].
- **Bear:** every operating metric (99% FPY, 10K/month, growth) is company-stated; no customer or expert call in the repo; only 10 sources mention Senra. Harnesses are labor-heavy, so the software edge may be workflow rather than automation [inference].

### 5.2 SendCutSend | fabrication | owner-operator | tracking
- **What:** instant-quote sheet metal, CNC and finishing; owns all plants (Reno; Paris, KY; Arlington, TX) [src-20261020-487a39].
- **Capital:** $110M at $1.01B, first institutional round, May 2026 [src-20260519-38c7ed]; Series B at $2.1B led by Spark, Oct 2026, size undisclosed [src-20261020-487a39] (med, single trade write-up). Prior valuation shown side by side: $1.01B [src-20260519-38c7ed] vs "roughly $1.1 billion" [src-20261020-487a39].
- **Scale:** 32K orders/month, ~100% y/y [src-20260525-4a12ab]; ~$140M run rate (deleted post) [src-20260504-c3ded5] (low); 650 staff [src-20260904-1929b3] vs 169 [Harmonic].
- **Claims (Belosic):** 48-hour turnaround [src-20260227-e92d45]; 80-90% utilization target [src-20260626-541ac8]; new facility ~$50M funded with equipment loans [src-20260519-2d6ceb]; "I love taking VC dollars and putting it directly in the payroll" [src-20261020-487a39].
- **Fit:** owns-production, in-house-software, speed-moat. Mission-critical-output weak (60% of Fortune 500 but commercial mix) [src-20261020-487a39].
- **Why it matters:** proof that a software-native owner-operator can be profitable without defense budgets [inference]; now likely priced beyond SPC.

### 5.3 Hadrian | precision-parts | hybrid | tracking
- **What:** automated CNC factories run on Opus software; now also embedded cells at Lockheed [src-20261014-015327].
- **Capital:** Series C $260M equity+debt Jul 2025 [src-20250721-d99a2a]; ~$1.6B valuation Jan 2026 [src-20260807-b0dc5b]; $1.37B Series D at $7.87B, Aug 6 2026 [src-20260807-b0dc5b]; $360M revolver [src-20260817-c48f28]. Total ~$2.24B [Harmonic].
- **Footprint:** four facilities (CA, AZ, AL), about 2.85M sq ft; 24 machines inside Lockheed Grand Prairie plus 24 in Arizona for overflow, line live by January 2027 (**Claim, Power**) [src-20261015-1a282b].
- **Capex:** ~$200M Mesa factory, 270K sq ft, 350 jobs [src-20250820-cfbf02]; six factories since 2022, latest 2.2M sq ft [src-20260921-876080].
- **Revenue (conflict):** ~$3M 2024 (Wikipedia) [src-20261022-de170d] (low) | $35M+ ARR 2024 (teardown) [src-20260819-dadd06] (low). Neither is primary.
- **Experts:** see section 8; share of wallet 2-3% at Boeing [src-20260802-ef6506], <10% at Northrop [src-20260802-36d46c].
- **Fit:** all seven tests partly met; customer-qualification still building (**Claim, Power:** AS9100-grade trust takes years) [src-20260908-65fab6].
- **Bear (expert calls, med):** ex-Anduril hardware lead: Hadrian "struggled to consistently deliver high-quality, complex parts" and got no production volume there [src-20250709-43486e]; Boeing CTO-org manager: "we have actually paid probably more", and no certified flying aircraft uses its parts [src-20260818-9b2d5c]; Northrop director: incumbents still have higher precision and a cost edge, and Ti/Inconel capability lags [src-20250707-3b7a46]; defense-startup chief of staff chose Atomic and questions how automated Hadrian really is [src-20250729-a0a78c]; ex-Xometry VP: deals are slow to win [src-20260808-dc5cbb]; ex-Hadrian engineer: CAM vendors are the main threat, and buyers cap a supplier at ~1/3 of its revenue [src-20250708-342eaf].
- **Buyer and insider voices (expert calls read line by line; speaker role as given by the call network; med):**

| Speaker (relation) | What they said | Source |
|---|---|---|
| Boeing Defense head of product, CTO org (current customer) | "None of their parts right now are flying ... all in demonstration stage." Near term a gap filler for spot buys of about 100 parts; long term "about 50%-60% automation". Scores: speed 8, process 9, scalability 8 out of 10. "We get very excited when we get a new supplier that gives us a discount of 5%-7%" | [src-20260818-9b2d5c] |
| Boeing strategy and M&A lead (buyer view) | Brackets, hinges and bulkheads in under 1 month vs 3-6 months; a "backup player" and "low-volume shop"; price about PCC or slightly more; automation cuts labor from 100 to 30-50 hours but capex offsets it | [src-20250712-e5e110] |
| Northrop operating-unit GM (buyer) | "Cost is secondary." "Machining the part is just 1/3 of the battle." Hadrian handles fasteners, shims and surge work; needed 8 parts, charged for 10-15; rates it 8/10 | [src-20250707-3b7a46] |
| PI, ex-Anduril hardware (buyer) | Not "able to deliver reliably high quality parts"; a "narrative play"; Anduril's CNC prototypes went mostly to Protolabs | [src-20250709-43486e] |
| Chief of staff, 40-person defense startup (buyer) | Uses Atomic Industries more ("turn production in eight days"). Hadrian also claims 8-9 days but is "more manual" and heavy on program managers | [src-20250729-a0a78c] |
| GE program lead (indirect exposure) | Hadrian is "too new, too young"; broker markups are "pretty horrific"; UK MOD DE&S has a new direct-sourcing cell | [src-20250709-0250ae] (low) |
| Ex-Hadrian head of engineering | Would be "surprised if any one company could capture 1%" of ITAR machining; machines are German and cost about $1M each; "only have 10 customers"; "all but one of the first 12 or 15 employees are gone" | [src-20250708-342eaf] |
| Ex-Hadrian (second call) | Power rejected a roll-up as "unredeemable" and went greenfield; started with aluminum milling only; "automate 80% of the tasks about 80% of the way"; keeps 10% of capacity idle for surge | [src-20260611-7b80f0] |
| Ex-Hadrian (third call; holds equity, a bias) | Factory 1: six machines, "well north of $10 million"; in years 1-2 Anduril was the only defense payer; CAM pay $130-150K vs $80-110K market; "dangerously good salesman" | [src-20260817-8867f2] |
| Ex-Xometry VP (peer) | "Hadrian needs 10 factories ... Xometry wants 10,000 customers"; revenue "surprisingly small" vs investment; rates Hadrian 6/10 | [src-20260808-dc5cbb] |

- **Contradictions, side by side.** Lead time: Northrop says Hadrian is fast [src-20250707-3b7a46] | a defense startup finds Atomic as fast and less manual [src-20250729-a0a78c]. Quality: Boeing scores process 9/10 [src-20260818-9b2d5c] | ex-Anduril PI says parts missed spec [src-20250709-43486e]. Competitor Formlogic: named as a live competitor by an ex-Hadrian engineer [src-20250708-342eaf] | "went under" per the client on another call [src-20250709-43486e] (unverified).
- **Why it matters:** the category benchmark; at $7.87B a reference not a target [inference].

### 5.4 Isembard | precision-parts | hybrid | tracking
- **What:** owned plus franchised machining factories on MasonOS; US, UK, DE, FR, UA [src-20260310-45bab3].
- **Capital:** $9M seed plus $50M Series A (USV lead), Mar 2026; valuation undisclosed [src-20260310-45bab3]; Harmonic estimate ~$250M [Harmonic] (low).
- **Scale (conflict):** 6 factories, target 25 by YE2026 [src-20260310-45bab3] | 14 factories Aug 2026 [src-20260810-f0371c] | 4 owned + 10 franchised [src-20260909-b547c7]. Consistent if growth is real; owned vs franchised split only in the podcast.
- **Claims (Isembard):** 40-60% throughput gains, 30% lower opex [src-20250929-857f17]; franchisee live in under 90 days [src-20260909-b547c7]; turning down orders [src-20260810-f0371c].
- **Customer view:** a humanoid company used Isembard for two urgent $2.3-6K orders, 2-day turnaround [src-20260621-f96bbd]; Airbus supply-chain head sees networks as prototype suppliers [src-20251106-dfddcb].
- **Bear:** Thales Alenia Space CPO is "skeptical" for aerospace, defense and space: he must qualify and see each production site, which a franchise network obscures; not a customer [src-20251110-84b67e]. Throughput and opex claims are company-only. BBC: ~100 staff at the 160,000 sq ft Southwark site [src-20261019-202dd7].
- **Fit:** franchise variant of Hadrian at a fraction of the price; capital-light [inference].

### 5.5 Machina Labs | fabrication | hybrid | tracking
- **What:** RoboCraftsman robotic sheet forming plus machining/welding; owns plants and places cells [src-20260204-ce7053].
- **Capital:** $124M Series C Feb 2026, lead and valuation undisclosed [src-20260204-ce7053]; Form D $38.9M sold of $52.6M [src-20260225-ccbe26]; $50M C-1 tranche at $5.47/share, $333.07M post (Forge) [src-20260204-7a0c74] (low) matches Harmonic $333M [Harmonic]; PrivateMarketView $374M (not filed) (low).
- **Customers:** biggest is military depots (legacy panels whose dies no longer exist) [src-20261022-ca4c7a]; ~70% defense; JASSM qualification; CMMC L2 [src-20260204-ce7053]; 13 federal awards 2020-25, $12.8M, Air Force a repeat buyer [src-20250416-317e81][src-20220328-cc3980].
- **Claims (Mehr):** up to ~50x faster lead times [src-20261022-ca4c7a]; staff 70 to 240 [src-20260320-1361e2].
- **Conflict:** new plant "200,000 sq ft" [src-20260204-ce7053] vs "250K sq ft" [src-20260320-1361e2].
- **Risk:** cycle time per part 30 minutes to hours vs seconds for stamping [src-20261023-c3b62f].

### 5.6 Freeform | precision-parts | owner-operator | tracking
- **What:** AI-controlled multi-laser metal AM service bureau; does not sell printers [src-20241024-7f1c2e].
- **Capital:** $67M Series B Feb 2026; PitchBook $179M post [src-20260219-2125d7] (med); ~$126M raised.
- **Skyfall:** **Claim (Freeform):** laser platform "scheduled to go live in the first half of 2026", 25x capacity, thousands of kg of parts a day [src-20260220-348ad9]. No source confirms it went live.
- **Loop:** microsecond meltpool vision, FPGA/GPU processing, models adjust print parameters live [src-20241024-7f1c2e]; on-site H200 clusters [src-20260219-2125d7].
- **Demand:** hundreds of mission-critical parts weekly, customers undisclosed [src-20260219-2125d7]; DIU OTA [src-20260901-6e197d].
- **Bear:** metal AM has the worst failure record in the theme (Velo3D, Markforged, Desktop Metal-era SPACs; section 7); Freeform's loop and capacity claims are company-only, customers undisclosed, Skyfall unconfirmed.
- **Why it matters:** clearest closed-loop process control in precision-parts; small enough for SPC [inference].

### 5.7 Divergent | precision-parts | hybrid | tracking
- **What:** AM plus robotic assembly (DAPS); missile airframes for RTX, L3Harris, GA-ASI [src-20260601-976843][src-20261013-eda149][src-20261022-8629b9].
- **Capital:** Series E $290M ($250M equity + $40M debt) at $2.3B, Sep 2025 [src-20250915-311606].
- **Scale (conflict):** Long Beach 400,000 sq ft [src-20261002-b0cee5] | 430,000 sq ft, 1,000 jobs, online by YE2026 [src-20261023-e02543]. Same capacity in both: 30,000 airframes a year.
- **Claims:** revenue up >5x [src-20250915-262bfd]; ~30 programs with 15 primes [src-20261014-47f64b]; A&D ~80% [src-20261023-e02543]; Tomahawk casting yields under 20% at legacy suppliers (claim) [src-20260113-c08796].
- **Why it matters:** the auto-to-defense pivot that worked; benchmark at $2.3B [inference].

### 5.8 Amca | precision-parts | owner-operator | candidate
- **What:** buys AS9100 plants (8) and re-engineers components with the RAPID AI platform [src-20260520-af3e6c][src-20261008-149196].
- **Capital:** $300M Series B at $1B+, Caffeinated and Lightspeed [src-20260520-af3e6c].
- **Demand:** first Army Advanced Manufacturing CSO Active Capability Gap FFP award, value undisclosed [src-20261008-149196]. **Claim:** qualifies re-engineered parts in under 90 days [src-20261008-149196].
- **Why it matters:** the roll-up path Hadrian rejected [src-20261004-9b47f5]; buys qualification instead of earning it [inference].

### 5.9 Vulcan Elements | metals-supply | owner-operator | candidate
- **What:** sintered NdFeB magnets; 10 t pilot in Durham, 10,000 t plant planned [src-20251103-ee9b27].
- **Capital:** $65M Series A (Altimeter) [src-20261010-8e6ec0]; $1.4B package: $620M OSC loan, $50M Commerce equity, $550M private [src-20251103-ee9b27]; Form D $430.7M sold [src-20260402-c8e4dc].
- **Demand:** 7 federal awards, $5.7M incl. an Army magnet IDIQ [src-20260710-6361ea][src-20250501-1885f8]; SkyFoundry magnets [src-20260923-c53c99]. **Claim (Maslin):** pilot sold out 12 months ahead; in-house characterization data feeds ML recipe models [src-20250811-e7cb9a].

### 5.10 Mariana Minerals | metals-supply | owner-operator | tracking
- **What:** builds and runs mines and refineries (Copper One, Lithium One) on MarianaOS [src-20260803-30e6d5].
- **Capital:** $310M Series B (Khosla), ~$400M parent plus project capital; valuation undisclosed in release [src-20260803-30e6d5]. $1.5B appears only in Harmonic and secondary coverage [Harmonic] (low).
- **Ops:** ~250 staff, ~20% software/ML; Utah mine ~50% autonomous [src-20260623-d1790b]. **Claim (Caldwell):** 30% lower refining cost, 40-50% lower mining cost [src-20260502-21f16a]; 10 projects in 10 years [src-20260513-dd56eb].
- **Why it matters:** one of two names with a credible data loop; Series B check size above SPC [inference].

### 5.11 1872 | fabrication | owner-operator | tracking
- **What:** AI-native steel fabrication (skids, frames, enclosures) for energy and utility, Cincinnati [src-20261022-fdbf29].
- **Capital:** $15M seed via O.H.I.O. Fund [src-20260722-985690].
- **Ops:** 18 staff, ~30,000 sq ft, producing since Aug 2026 [src-20261016-d61bc1]; Path Robotics weld cells [src-20260722-3bc2d8].
- **Claims (website, no baseline):** 99% FPY, 70% arc-on time, 85% weld cost reduction [src-20261022-fdbf29]. Full autonomy targeted 2027 [src-20260722-985690].
- **Why it matters:** cheapest entry into owner-operator fab; pre-revenue proof [inference].

### 5.12 Nox Metals | metals-supply | owner-operator | passed
- **What:** automated metals service center outside Detroit; Factos nesting [src-20261009-404b9b].
- **Capital (conflict):** $11.5M seed (Hyperion) [src-20260616-1cf7cb] + $4.6M pre-seed [src-20251110-b1acae] = ~$16.1M | a podcast says ~$4.6M raised [src-20260427-83b102] (low; predates the seed).
- **Ops (conflict):** 52 staff (YC) [src-20261022-2aabbe] vs 11 (Built In LA, Oct 2026) per company file; 75K sq ft, 250-300 customers [src-20261009-404b9b].
- **Status:** passed; kept as a seed-stage reference for a software-led service center.

### 5.13 Arda | factory-ai | software-first | tracking
- **What:** agent reads CAD and design docs, writes assembly order and work instructions [src-20261020-914a64].
- **Capital:** $72M seed (Accel, Founders Fund); $160M Series A at $1.5B (Altimeter, Accel, Khosla); $232M total [src-20261020-914a64]. Earlier WSJ report: $70M at $700M [src-20260308-1984ea].
- **Claim (Arda/Anduril):** work instructions 10 hours to 15 minutes; complex engineering 30 hours to ~2.5 [src-20261020-914a64].

### 5.14 Mind Robotics | factory-ai | software-first | tracking
- **What:** Rivian spinout training robot models on factory work [src-20261022-eede0b].
- **Capital:** $115M seed, $500M A (~$2B) [src-20260311-44ded4], $400M B (~$3.4B, WSJ) [src-20260515-176e26]; >$1B total [src-20260513-83aa83]. No public product.

### 5.15 Periodic Labs | materials-rd | owner-operator | tracking
- **Capital (conflict):** $300M seed at ~$1.3B [src-20251022-8eb7c0] | talks ~$7B [src-20260326-79447c] (med) | "advanced talks" $500M+ at $7.5B led by AMP [src-20260514-5796ab] (med) | closed at $7.5B, ~$1.1B raised [Harmonic] (low) | Series A closed, $605M total, 62 staff (AI-compiled page citing StartupHub) [src-20260612-5506d2] (low). No primary confirmation.
- **Offer:** custom AI agents for clients' engineers; one unnamed semiconductor client [src-20261022-682e62].

### 5.16 CuspAI | materials-rd | software-first | tracking
- **Capital (conflict):** $450M Series B at $2.6B, Kleiner and NEA [src-20260720-840ae3]; ~$580M total [src-20260720-02f3fe] | £300-350M at ~£2bn [src-20261016-29997e] (med, AlphaSights primer). Guardian: $450M = £330M, $2.6B headline "£2bn" [src-20260720-3cfc67], so these are the same round | $980M total [Harmonic] (low).
- **Network:** ~30 industry, ~15 lab partners incl. Samsung, AMD, Lam, Applied [src-20261022-37a0ea].

### 5.17 Radical AI | materials-rd | owner-operator | tracking
- **Capital (conflict):** $55M Seed+ led by RTX Ventures [src-20250718-d46f24] | ">$60M" [src-20260710-366df7] | $10M pre-seed + $55M = $65M [src-20250722-6b94a0].
- **Ops:** see 4.4; AF award $1.2M [src-20250523-f41dd1].

### 5.18 Terrafirma | adjacent | owner-operator | tracking
- $100M Series A, autonomous earthworks, Austin [src-20260714-976329]; ~$500M estimated post [Harmonic] (low). Adjacent to thesis.

### 5.19 Remaining candidate and incumbent files (one line each)

| Company | Layer | Status | One line |
|---|---|---|---|
| Fabri | precision-parts | candidate | Automated investment casting, $13.5M, RTX and LMT Ventures; shipping castings [src-20260617-4dfb96] |
| Layup Parts | precision-parts | candidate | Custom composite parts, $42M A [src-20260602-a7b79e] |
| Hybron | precision-parts | candidate | Composite shells, $25M seed; contract floor >$100M [src-20260413-abc797] |
| Atomic Industries | fabrication | candidate | AI tool and die, $25M A [src-20261023-a3bfe7] |
| Rangeview | precision-parts | candidate | Printed-mold castings, $4.2M seed [src-20260923-3ab808] |
| Furientis | adjacent | candidate | Low-cost interceptors, $25M seed (Benchmark), DoW OTA [src-20261006-410f77] |
| Firestorm Labs | adjacent | candidate | SBIR to Phase III IDIQ with repeat SOCPAC task orders, 19 awards, $53.8M [src-20251022-629fc0][src-20251219-bd5788] |
| Re:Build | precision-parts | candidate | Engineering plus manufacturing roll-up, 12 sites [src-20261006-1212f9] |
| VulcanForms | precision-parts | candidate | LPBF AM plus machining; layoffs Apr 2023 and Jun 2024 (failure reference) [src-20261023-63156a] |
| Proto Labs, Xometry, Howmet, PCC, ATI, Carpenter, Reliance, Ryerson, Nucor, Rockwell, Siemens | various | incumbent | Benchmarks in section 7 |

---

## 6. Data loop scorecard

Scale: 0 asserted only; 1 mechanism described; 2 partial evidence; 3 quantified improvement over time. Nobody scores 3.

| Company | Score | Mechanism | Best evidence | Missing |
|---|---|---|---|---|
| Freeform | 2 | Meltpool vision adjusts each layer live | [src-20241024-7f1c2e][src-20260219-2125d7] | Yield or cost trend over time |
| Mariana | 2 | RL agents adjust process every 15 min | [src-20260623-d1790b] | Recovery or cost data per tonne |
| Hadrian | 2 | Opus workflow, programming and QC | 30-40 day training [src-20260926-70087f]; 25-75% cycle-time cuts at a studied shop; 50% cut in order-to-first-article within about two years [src-20261004-9b47f5] | Relies on third-party CAM [src-20261004-9b47f5] |
| Radical AI | 2 | Self-driving lab closed loop | 8-20 alloys/day [src-20260617-f9d293] | Hit rate trend |
| Divergent | 2 | Generative design to print to assembly | 600+ part numbers [src-20250915-311606] | Cost per part trend |
| Senra | 1 | Amp reuses BOM and labor data | 99% FPY claim [src-20260715-68183e] | Before/after |
| SendCutSend | 1 | Instant quoting at volume | 32K orders/month [src-20260525-4a12ab] | Any learning metric |
| Isembard | 1 | MasonOS ML quoting across franchise | Claim 40-60% throughput [src-20250929-857f17] | Third-party proof |
| Machina | 1 | Robot forming learns per geometry | Claim 50x lead time [src-20261022-ca4c7a] | Cycle-time trend |
| Vulcan | 1 | Characterization data into recipe ML | [src-20250811-e7cb9a] | Any number |
| Nox | 1 | Auto-nesting, quote-time estimates | [src-20260325-5b68db] | Scrap rate |
| Arda | 1 | Agent improves with host design data | [src-20261020-914a64] | Data rights |
| Periodic, CuspAI, Mind | 1 | Lab or factory as RL environment | [src-20260917-1bcb81][src-20261022-37a0ea][src-20260513-83aa83] | Production evidence |
| 1872 | 0 | Weld model is Path's, not 1872's | [src-20260722-3bc2d8] | Everything |

Read: the loop is real where the process is physical and continuous (melt pools, ore, alloys), and weakest where the product is discrete parts sold on drawings [inference].

---

## 7. Competition and incumbents

| Incumbent | Metric | Value | Source | AI move |
|---|---|---|---|---|
| Proto Labs | FY25 revenue / GAAP GM | $533.1M / 44.5% | [src-20260206-8bb619] | AI pricing [src-20260731-ef3d40] |
| Proto Labs | Factory vs network GM | 49% vs 31% | [src-20260206-2b13c7] | |
| Xometry | FY25 marketplace / total GM | 34.7% / 39.1%; net loss $61.7M | [src-20260224-a7b149] | Siemens partnership [src-20260804-7625ed] |
| Xometry | Q2'26 revenue | $229M (+41%) | [src-20260804-33fe9f] | |
| Reliance | Q3'26 GM | 27.9% LIFO / 31.6% FIFO | [src-20261021-16bb64] | |
| Ryerson | Q2'26 GM | 17.7% | [src-20260729-407fd7] | |
| Nucor | Q2'26 GM | 20% vs 14% | [src-20260812-77d6f5] | |
| Howmet | Q2 revenue / Engine EBITDA margin | $2.55B / 37.7% | [src-20260806-9a83f7] | AI process control [src-20260301-357ec4] |
| ATI | Adj. EBITDA margin / backlog | 22.6% / $4.4B | [src-20260806-70254e][src-20260628-27be55] | |
| Carpenter | GM | 32.1% (40.4% ex-surcharge) | [src-20261022-d47483] | |
| Nucor | FY25 GM / utilization | 12%; steel mills 83%, steel products 62%; backlog mills $3.35B vs $2.13B | [src-20260225-3ea941] | "highly automated" |
| Ryerson | Footprint FY25 | ~4,300 staff, 103 NA sites (pre-Olympic) | [src-20260223-0f0be4] | analytics for pricing |
| ATI | FY25 backlog | $3.7B vs $3.9B | [src-20260220-d8abeb] | |
| Proto Labs | 10-K AI uses | pricing, molding inspection, CNC toolpath checks, AI routing in minutes | [src-20260220-fe6c5e] | yes |
| Xometry | 10-K self-description | "AI-native" marketplace | [src-20260224-0bf807] | yes |
| Howmet | FY25 staff | 25,430; names AI-enabled competitors as a risk | [src-20260212-91b1e0] | risk factor |
| Rockwell | GM | 49.5% | [src-20260804-0e8130] | |

Note the two ATI backlog figures measure different dates: $3.7B at Dec 28 2025 [src-20260220-d8abeb] vs $4.4B in Q2 2026 [src-20260628-27be55].

**What the expert calls add on incumbents (claims, med).**

| Incumbent | Data point | Source |
|---|---|---|
| PCC | Minimum account size about $50M+, majors >$25M; share of Boeing machining fell from 50% to 30% over 10 years; parts cost 5-7% more; also automating | [src-20250712-e5e110] |
| PCC | A factory fire hit all allocations from that plant, so Boeing will not concentrate supply again | [src-20260818-9b2d5c] |
| Boeing in-house (conflict) | About 40% of parts made in-house; flight-critical work stays in-house [src-20250712-e5e110] \| only 20-30% of the 1.2M parts per airplane made in-house [src-20260818-9b2d5c]. Different scopes (spend vs part count) are possible | both |
| Boeing supply base | More than 10 machining shops, wants 2-3; legacy suppliers have "extremely high inertia" | [src-20260818-9b2d5c] |
| Xometry, Protolabs | Target $5M+ accounts; Boeing spend with each is under $1M and over $1M | [src-20250712-e5e110] |
| Xometry | Grew after shedding its own machines; Protolabs was held back by its own factories; market stays fragmented for 5 years | [src-20260808-dc5cbb] |
| Protolabs | 8-inch cube limit on fast CNC; Xometry supplier rates "abysmal" | [src-20260611-7b80f0] |
| Federal prime awards (USAspending, ledger totals) | Xometry 56 awards, $2.9M, 2014-26; Proto Labs 48 awards, $1.8M, 2008-26; Hadrian 1 award, $79.4M (2026). Incumbent marketplaces win many small federal orders; Hadrian wins few large ones | [src-20260130-7d74e3][src-20080929-77494f][src-20260317-77e798] |

Read: the incumbent threat is not Xometry's software but PCC-type primes' suppliers automating while holding qualification, and primes keeping critical work in-house [inference].

Incumbents are partnering, not building: Lockheed embeds Hadrian [src-20261014-015327] and LM Ventures runs a $1B fund [src-20260401-073d24]; RTX Ventures led Radical [src-20250718-d46f24] and backs Fabri [src-20260617-4dfb96]; Siemens bought Altair and Dotmatics [src-20250326-cc1810][src-20250701-a7fef9]; Lindsay Goldberg is rolling up Alro [src-20260811-27702f].

Failures to learn from:
- Fast Radius: SPAC Feb 2022, Chapter 11 Nov 2022, sold for ~$15.9M [src-20221108-bb31a1][src-20261023-63156a].
- Markforged: $2.1B valuation 2021, sold to Stratasys for $42.5M in 2026 [src-20261023-63156a].
- Velo3D: defense refocus; Q1 2026 GM 17.2% vs -73.6% [src-20261023-9f720f].
- Bright Machines (failure example only): $1.6B SPAC fell through; Israel R&D closed with ~60 layoffs in 2024; sold $71.5M of a $145.5M 2022 Form D [src-20240527-6a4884][src-20261023-63156a].
- Daedalus: AI-run precision CNC factory (Karlsruhe), $21M Series A Feb 2024, insolvency Aug 2026 [src-20260801-4532f6]. The closest failed analog to the owner-operator thesis.
- VulcanForms: layoffs Apr 2023 and Jun 2024 (>20%, anecdotal), founder CEO replaced, then $220M in Jan 2026 [src-20240910-5d51ed][src-20240919-72efcc][src-20260130-365541]. Pivot, not failure.
- Velo3D debt cut 60% to ~$10M via debt-to-equity, Mar 2026 [src-20260311-79b04d].
- Lesson: survivors found a repeat defense buyer before scaling capex; equipment sellers did not compound [inference].

---
## 8. Customers and demand

**Who buys:** primes (Lockheed, RTX, Northrop, Boeing, L3Harris, GA-ASI), new primes (Anduril), depots and government programs (Army, Navy, DIU), commercial hard-tech (SendCutSend's 60% of Fortune 500) [src-20261020-487a39].

**What they value, side by side (all AlphaSense-arranged expert calls, med):**

| Buyer | Price vs incumbents | Speed | Share of wallet / switching |
|---|---|---|---|
| Raytheon senior manager [src-20250708-2aa3ad] | Hadrian ~50% lower on RFQ quotes; no parts received yet; introduced via RTX Ventures | ~1/3 the lead time | Sweet spot $300-700 parts, no castings; suppliers at 80-90% utilization |
| Boeing head of product [src-20260802-ef6506] | 20-25% gap would trigger re-sourcing | Hadrian 2-3x faster | Hadrian 2-3% of precision spend, prototypes and non-critical parts |
| Boeing executive director [src-20260908-ed94f0] | At 1,000 parts a traditional shop is cheaper | Full inspection time equal | Losing Hadrian = minimal impact |
| Northrop process engineer [src-20260802-36d46c] | Would pay 20-40% more to avoid program delay | n/a | Hadrian <10% of outsourced work, maybe 10-20%; CNC only; replacing it takes months to a year |
| FlyX CEO [src-20260806-3a2ec7] | Would choose Hadrian at 5% premium, not at 30-40% | n/a | n/a |
| ICT USA [src-20260805-59d4fe] | 10-12% gap triggers switch | n/a | 85% Hadrian / 15% Machina |
| Boeing CTO-org manager [src-20260818-9b2d5c] | Paid more so far; 5-7% discount is exciting, 30-50% would move volume | n/a | No certified flying aircraft uses Hadrian parts |
| Boeing strategy head [src-20250712-e5e110] | 20-30% per-part saving "optimistic"; expensive at low volume | 24/7 faster | Xometry better for low volume |
| Northrop director [src-20250707-3b7a46] | Incumbents keep a cost edge, will price-war | Lead time is the pain | Rates Hadrian 8/10 |
| Ex-Anduril hardware lead [src-20250709-43486e] | Defense buyers are price-insensitive | n/a | No production volume given |
| Thales Alenia CPO [src-20251110-84b67e] | n/a | Capacity is the pain; Chrome VI banned from end-2024 | Prime does not qualify Tier-2 network sites; would only use suppliers with $30-40M revenue; fits smaller defense, auto and energy first |
| Anduril senior engineer [src-20250623-5bc67c] | Wants conforming parts at competitive price | Lower lead times | Skeptical of "AI bells and whistles" |
| Ex-Xometry VP [src-20260808-dc5cbb] | n/a | n/a | 50-60% of parts arrive with no 3D model; CEO in every deal, so feast or famine |
| Defense startup chief of staff [src-20250729-a0a78c] | n/a | Atomic 8 days, Hadrian 8-9 days | Big buyers will move in-house after a "honeymoon period" |
| GE program lead [src-20250709-0250ae] (low) | Broker markup "pretty horrific" | n/a | Hadrian "too new, too young" |

The contradiction to put on the slide: Raytheon reports Hadrian *cheaper*; Boeing reports it *dearer at volume*. Both can be true if Hadrian prices aggressively on low-volume, urgent work [inference]. The demand that is proven is speed on prototypes and LRIP; demand at rate production is not yet proven [inference].

**Qualification as moat or tax.** Supplier qualification 9-12 months (Raytheon) [src-20250708-2aa3ad]; onboarding 1-2 years (Northrop) [src-20260802-36d46c]; Power says AS9100-level trust takes 7-8 years [src-20260908-65fab6] (claim). Airbus: supply base consolidating to fewer suppliers; networks suit prototypes [src-20251106-dfddcb]. A Raytheon engineer says quality from new suppliers now surpasses legacy [src-20260823-b3713f]. Read: a tax at entry, a moat once paid; Amca buys it via acquisitions [src-20260520-af3e6c] [inference].

**Repeat orders (federal data).** Firestorm is the only producer with a SBIR (Small Business Innovation Research, staged federal R&D grants) to Phase III IDIQ to repeat task orders ladder: 19 awards, $53.8M [src-20251022-629fc0][src-20251219-bd5788]. Hadrian's Army award was $39.2M obligated, $80M total, one bid received [src-20260317-5585be]. Mariana, Arda, 1872, Nox: no prime awards found (insights/repeat-orders-evidence.md).

---

## 9. Capital and financing

| Company | Equity raised | Last round / valuation | Debt or gov | Capex datapoint | Who funds plant | Source |
|---|---|---|---|---|---|---|
| Hadrian | ~$2.24B [Harmonic] | $1.37B D at $7.87B, Aug 2026 | $360M revolver; Navy $900M | ~$200M per 270K sq ft plant; ~$1B ahead of contracts (claim) | Debt, per Power: "equity never funds factory construction" | [src-20260807-b0dc5b][src-20260817-c48f28][src-20260320-67ba4c][src-20250820-cfbf02][src-20260921-876080] |
| Divergent | n/d; Series D $230M (Hexagon) | $290M E at $2.3B, Sep 2025 | $40M debt in E | Long Beach 400-430K sq ft, cost n/d | Equity + debt | [src-20250915-311606][src-20231115-5d0589][src-20261023-e02543] |
| Isembard | $59M | $50M A, val. n/d | Undisclosed debt for owned plants | n/d | Franchisees fund their own plants | [src-20260310-45bab3][src-20250929-857f17] |
| SendCutSend | $116M + Oct round | $2.1B B (size n/d) | Equipment loans | ~$50M new facility; first $750K laser financed | Equipment debt | [src-20261020-487a39][src-20260519-2d6ceb][src-20260227-e92d45] |
| Vulcan Elements | $65M A + $50M Commerce equity | n/d | $620M OSC loan; $550M private | 10,000 t plant | Government-led | [src-20251103-ee9b27][src-20261010-8e6ec0] |
| Mariana | ~$400M incl. project capital | $310M B, val. n/d ($1.5B Harmonic, low) | Project capital | n/d | Project finance | [src-20260803-30e6d5] |

Pattern: equity for software, team and plant #1; banks, OSC and project finance for plants #2+ [inference]. Bear: Lowercarbon says modular-hardware companies at Series B often have ~$10M revenue at break-even gross margin [src-20251211-87dc10]; a six-machine first plant cost >$10M [src-20260817-8867f2]. ABL (asset-based lending against receivables and inventory) is not evidenced for any tracked startup (gap).

---

## 9A. Unit economics by layer

Startup margins are not disclosed anywhere in the repo. The table puts incumbent benchmarks next to the cost drivers the expert calls quantify. Cells marked (claim) come from a single speaker.

| Layer | Gross margin benchmark | Capex and fixed cost | Variable cost and pricing | What moves the margin [inference] |
|---|---|---|---|---|
| metals-supply | Service centers 17.7% (Ryerson) to 31.6% FIFO (Reliance) [src-20260729-407fd7][src-20261021-16bb64]; Nucor 12% FY25 [src-20260225-3ea941] | Vulcan 10,000 t magnet plant on a $1.4B package [src-20251103-ee9b27] | Metal price passes through; tariffs lift inventory gains [src-20260728-ae7dea] | Quote speed and remnant use; price cycle dominates |
| fabrication | SendCutSend profitable 8 years, margin n/d [src-20260519-38c7ed] | ~$50M per new facility; first laser $750K, debt-financed [src-20260519-2d6ceb][src-20260227-e92d45] | Xometry material can be 85% of a part's price (claim) [src-20260611-7b80f0] | Utilization (80-90% target) [src-20260626-541ac8] |
| precision-parts | Proto Labs 44.5%; own factories 49% vs network 31% [src-20260206-8bb619][src-20260206-2b13c7]; job shops 15-25% (thesis.md) | Plant 1: six machines, >$10M; Grob/Hermle 5-axis about $1M each vs Doosan $200K; target 20-25% low-cost machines (claim) [src-20260817-8867f2]; Mesa ~$200M [src-20250820-cfbf02] | Labor hours 100 to 30-50 per part, net saving 20-30% at best after capex (claim) [src-20250712-e5e110]; NRE $1-5K, casting tooling tens to hundreds of $K [src-20260611-7b80f0]; CAM staff $130-150K [src-20260817-8867f2] | Machining is 1/3 of the work; inspection, paperwork and certs are the rest [src-20250707-3b7a46][src-20260611-7b80f0] |
| materials-rd | Custom programs 5-15%, platform 85-90% (claim) [src-20261016-29997e] | Self-driving lab about $20M to build, low running cost (claim) [src-20260909-af3e60] | Buyer pays about $150K per software benchmark, $500K per pilot, $2M per validated candidate, $10-15M a year per lab line (claim) [src-20260909-af3e60]; ACVs "hundreds of thousands to millions" [src-20260913-3ad55e] | Hit rate and repeat campaigns; royalties rejected |
| factory-ai | Rockwell 49.5% [src-20260804-0e8130] | Software; needs a host plant | Arda usage-based [src-20261020-a1e174]; AI Robotics welding inspection on 24 lines, revenue up about 18x, profitable without outside capital [src-20261011-a8b14d] | False-detection rate on live lines [src-20261011-a8b14d] |

Power and compute are minor costs: 1,200A service with 500-600A used for 6-8 machines; about 30 CNCs run on 2,000A (claim) [src-20260817-8867f2].

---

## 10. Policy tracker (newest first)

| Date | Policy | What it does | Layer | Source |
|---|---|---|---|---|
| 2026-10-20 | Army 1M drones plan (reported) | Volume demand for magnets, airframes | metals-supply, fabrication | [src-20261020-878aa9] |
| 2026-10-20 | 45X | Advanced manufacturing production credit | metals-supply | [src-20261020-7d90fa] |
| 2026-09-23 | SkyFoundry / Vulcan award | Army drone magnet supply | metals-supply | [src-20260923-c53c99] |
| 2026-09-08 | OSC | DoD lender for critical-tech capex | all producers | [src-20260908-f6558e] |
| 2026-08-18 | Section 232 pharma | 100% on patented pharma, APIs | adjacent | [src-20260818-489fdf] |
| 2026-10-19 | DPA Title III tally | 23 awards, $820.5M since Jan 2025; rare earths $405.1M, solid rocket motors $196.4M; none to tracked startups | metals-supply | [src-20261019-68fd3d] (med, third-party) |
| 2026-07-16 | IEA public finance | Minerals commitments $65B | metals-supply | [src-20260716-6a06e4] |
| 2026-04-06 | Section 232 metals | 50/25/10% structure; grid 15% to 2028 | metals-supply, fabrication | [src-20260402-1b5d6c] |
| 2026-01-01 | DIU CSO | Commercial Solutions Opening, fast awards | precision-parts | [src-20260101-0b051b] |
| 2025-12-18 | FY26 NDAA (PL 119-60) | Sec. 225 robotic munitions automation; Sec. 867 Industrial Base Fund (castings, forgings, machine tools); Sec. 1652 Golden Dome cost reports; Sec. 1841 Civil Reserve Manufacturing Network; Sec. 1847 surge report | precision-parts, metals-supply | [src-20251218-f0d6ef][src-20251218-6c4228] |
| 2025-12-15 | DIB strategy / DPA | DPA Title III (Defense Production Act authority to fund domestic capacity) | metals-supply | [src-20251215-98f650] |
| 2025-11-03 | OSC loan to Vulcan | $620M | metals-supply | [src-20251103-ee9b27] |
| 2025-08-06 | Apple-MP prepay | Offtake as financing | metals-supply | [src-20250806-a0a34e] |
| 2025-08-01 | Section 232 copper | 50% on semi-finished copper content; refined copper 15% (2027) / 30% (2028) under review | metals-supply | [src-20250805-80f2f4] |
| 2024-12-19 | OTA authority | Prototype to production without recompete | precision-parts | [src-20241219-9f8fcc] |
| 2024-12-06 | PPBE reform | Budget process speed | all | [src-20241206-6e78bd] |

Gaps: Golden Dome dollar flows (the NDAA requires reports, not money) [src-20251218-f0d6ef]; no DPA Title III award to a tracked startup in the third-party tally [src-20261019-68fd3d]; OSC loan to Vulcan is the only federal loan to a tracked name [src-20251103-ee9b27].

---

## 11. Companies worth attention

| Bucket | Company | Layer | Model | Why | Next step |
|---|---|---|---|---|---|
| Target | Senra | fabrication | owner-operator | Series B size, real customers, in-house software | Founder call; FPY and repeat-order data |
| Target | Freeform | precision-parts | owner-operator | Best evidenced loop; $179M post | Customer reference calls (Boeing, DIU) |
| Target | Isembard | precision-parts | hybrid | Capital-light Hadrian variant; val. undisclosed; Thales CPO skeptical [src-20251110-84b67e] | Unit economics per franchise; site-audit answer for primes |
| Candidate | Fabri | precision-parts | owner-operator | Castings are ~40% of munitions (claim, Power) [src-20260921-876080]; RTX/LMT backed | Promote file; 2nd source |
| Candidate | 1872 | fabrication | owner-operator | Cheap entry, energy skids | Track to first repeat order |
| Candidate | Atomic Industries | fabrication | owner-operator | Tool and die bottleneck | Second source |
| Candidate | Machina | fabrication | hybrid | Depot demand; long Form D | Verify valuation |
| Benchmark | Hadrian, Divergent, SendCutSend, Mariana, Amca | various | various | Priced $1B-$7.9B | Use for comps |
| Benchmark | Periodic, CuspAI, Mind, Arda | materials-rd, factory-ai | various | Priced pre-product | Watch for revenue |
| White space | Service-center software for mid-size distributors | metals-supply | software-first | ~9,400 establishments, top 50 hold ~50% [src-20251201-4b732d]; Nox passed | Sweep |
| White space | Forgings | precision-parts | owner-operator | DoD flags castings and forgings barriers [src-20220215-45c353]; no AI-native forger in repo | Sweep |
| White space | Inspection/NDT as a service | precision-parts | enabler | Inspection time equal for Hadrian vs legacy [src-20260908-ed94f0] | Sweep |

---

## 12. Bottom line

**Five conclusions**
1. The category is real, but proven demand is speed on prototype and low-rate work; rate production share is 2-10% at the primes we spoke to [src-20260802-ef6506][src-20260802-36d46c].
2. The data loop is evidenced (score 2) only where the process is continuous: Freeform, Mariana, Radical, plus Hadrian's training compression. Nobody shows improvement over time (section 6).
3. Capital splits into three tiers: capital-light owner-operators (SendCutSend, Senra), capital-heavy owner-operators financed by debt and government (Hadrian, Vulcan, Mariana), and software-first vendors that need a host plant (Arda, Mind) [inference].
4. Precision-parts is priced out at the top (Hadrian $7.87B [src-20260807-b0dc5b], Amca $1B+ [src-20260520-af3e6c]); SPC entry is Series B in fabrication or a hybrid/franchise variant [inference].
5. Policy pull lands mostly on metals-supply (OSC, Section 232 incl. copper, IEA finance, DPA Title III to rare earths and rocket motors) [src-20251103-ee9b27][src-20260402-1b5d6c][src-20250805-80f2f4][src-20261019-68fd3d]; the FY26 NDAA adds robotic munitions automation and an Industrial Base Fund for castings, forgings and machine tools, but no money to tracked startups yet [src-20251218-f0d6ef]; precision-parts gets pull through prime contracts instead [inference].

**Layer x model matrix (our pick per cell, [inference])**

| | owner-operator | hybrid | software-first | enabler |
|---|---|---|---|---|
| metals-supply | Vulcan, Mariana (benchmarks) | n/a | White space (service-center software) | n/a |
| fabrication | **Senra** (pick); SendCutSend (benchmark); 1872 | Machina | n/a | Path Robotics |
| precision-parts | **Freeform** (pick); Fabri | **Isembard** (pick); Hadrian, Divergent (benchmarks) | n/a | n/a |
| materials-rd | Radical, Periodic | n/a | CuspAI | n/a |
| factory-ai | n/a | n/a | Arda, Mind (benchmarks) | Siemens, Rockwell (incumbents) |

**Three targets:** Senra, Freeform, Isembard (reasons in section 11).

**Three risks**
1. Rate-production economics: at 1,000 parts a traditional shop is cheaper (Boeing) [src-20260908-ed94f0].
2. Capex ahead of contracts: ~$1B needed per Power [src-20260921-876080]; a munitions slowdown strands plants [inference].
3. Valuation outrunning revenue: SendCutSend's multiple is unknown ("nine digits" revenue at $2.1B) [src-20261020-487a39]; Periodic and Mind priced before product.

**Strongest bear case**
- Rate economics: Boeing buyers report paying more, not less, and cost only matters after quality and delivery are proven [src-20260818-9b2d5c][src-20260908-ed94f0]; 2-10% share of wallet is prototype work [src-20260802-ef6506][src-20260802-36d46c].
- The model has failed recently: Daedalus insolvent [src-20260801-4532f6]; Bright Machines' SPAC collapsed [src-20261023-63156a]; Fast Radius, Markforged, Velo3D wiped out; VulcanForms cut staff before re-raising [src-20240910-5d51ed].
- Quality at complexity is unproven: ex-Anduril lead says Hadrian struggled on complex parts [src-20250709-43486e]; Thales will not qualify a franchise network [src-20251110-84b67e].
- The AI is thinner than the pitch: Opus rides third-party CAM [src-20261004-9b47f5]; robot learning at ~60% vs 99.9% [src-20260904-267293]; A-Lab novelty claims retracted in part [src-20240124-513fd9].
- Valuation: Hadrian $7.87B, Mind $3.4B, Periodic ~$7.5B (reported) with no audited revenue; a defense-budget or tariff reversal hits capex built ahead of contracts [src-20260921-876080].
- Slack exists: 34% spindle utilization in incumbent shops [src-20250120-419768] means demand can be met without new plants.
- Share per customer is capped by policy: a 1/3-of-revenue cap at SpaceX [src-20250708-342eaf], no single-sourcing after the PCC fire [src-20260818-9b2d5c], and 5-10 years to trust a new supplier [src-20250712-e5e110].
- Regulators get stricter after Boeing's quality lapses: "Innovation ... is the first thing that gets sacrificed, and Hadrian falls in that innovation category" [src-20260818-9b2d5c].
- Team durability: 90% of Hadrian's first 10 employees gone by year 5; a 40-person software team churns [src-20260817-8867f2].
- AI CAM vendors sell the same automation to every incumbent shop: CloudNC CAM Assist is in GibbsCAM [src-20261021-9769d1][src-20261009-7cafd0]. Ex-Hadrian staff call CAM vendors the main threat [src-20250708-342eaf].
- Some buyers see financing, not venture: "better suited to debt than VC" [src-20250709-43486e]; "propped up by VC money" (peer view) [src-20260808-dc5cbb].
- Materials-rd: model leadership turns over on a "three-month cadence", so stickiness is falling [src-20260909-af3e60] (low); chemical customers have "25 data points", not big data [src-20260913-3ad55e].

**Bias check on targets.** Senra (10 sources), Freeform (14) and Isembard (13) are among the least-covered names, not the most (Hadrian 76, Machina 42, Arda 33, SendCutSend 31). That avoids picking for press volume but means each target rests mostly on company claims; Isembard also has the one negative buyer call. Treat all three as hypotheses for diligence, not conclusions.

**What would change our mind**
- A prime shows Hadrian or peers at >20% of rate-production spend with lower unit price (bull).
- A company publishes scrap, cycle time or quote accuracy improving with volume (moves loop to 3).
- Section 232 struck down or rolled back (bear for metals-supply and fabrication).
- A tracked owner-operator raises a down round or stalls a plant (bear).

**Status of questions.md** (status as written in the file | primer view)

| Q | Topic | File status | Primer view |
|---|---|---|---|
| 1 | Data loop real? | partial | partial: section 6 |
| 2 | Each part improves the next? | partial | partial: no quantified trend anywhere |
| 3 | Software-first data rights | partial | partial: Arda/Mind rights undisclosed |
| 4 | Gross margin at scale | open | partial: incumbent benchmarks in section 7; startup margins still unknown |
| 5 | Capex and financing | partial | partial: section 9 |
| 6 | Utilization and lead time | partial | partial: 48h SendCutSend, 80-90% utilization targets |
| 7 | Pricing | open | partial: expert table in section 8 |
| 8 | Buyer mix | partial | partial |
| 9 | Qualification | partial | partial: 9-12 months to 1-2 years |
| 10 | Policy pull | partial | partial: section 10 |
| 11 | Service-center margins | open | partial: Reliance/Ryerson GM; software effect unknown |
| 12 | Domestic refining | partial | partial |
| 13 | Landscape | partial | partial: 138 long-tail candidates |
| 14 | Exits | open | open: only Alro roll-up and failure sale prices |
| 15 | SPC operator edge | open | open |
| 16 | Fit to SPC size | partial | partial: section 11 |
| 17 | One-page matrix | partial | partial: matrix above |

---

## Fix before IC (slide 8 figures)

Slide 8 mixes round sizes and valuations [src-20261022-80fd75]. Corrected values:

| Item | Slide 8 says | Correct per sources | Conf. |
|---|---|---|---|
| Hadrian | ~$1.6B (C) | Footprint ~2.85M sq ft, four sites [src-20261015-1a282b]. ~$1.6B was the Jan 2026 valuation, not Series C (C was $260M, Jul 2025). Now $1.37B Series D at $7.87B, Aug 2026; ~$2.24B raised [src-20260807-b0dc5b][src-20250721-d99a2a][Harmonic] | high |
| Periodic | $300M seed | $300M seed at ~$1.3B [src-20251022-8eb7c0] | Then $500M+ at $7.5B in "advanced talks" [src-20260514-5796ab] vs closed at $7.5B, ~$1.1B raised [Harmonic] vs closed, $605M total [src-20260612-5506d2] (low): say "reported $7.5B", no total | med |
| CuspAI | $450M (B) | $450M Series B at $2.6B, ~$580M total [src-20260720-840ae3][src-20260720-02f3fe] ; the £ figures are the same round converted (£330M, "£2bn") [src-20260720-3cfc67] | high |
| Senra | $65M (B) | $65M is the round; total >$112M [src-20260715-68183e]; $492.96M post (Forge, share-price derived) [src-20260715-8161a3] vs $422.8M (PrivateMarketView): label "secondary-data estimate" | low |
| Freeform | $67M (B) | $67M Series B at $179M post (PitchBook), ~$126M raised [src-20260219-2125d7]; Skyfall H1 2026 launch unconfirmed [src-20260220-348ad9] | med |
| Machina | $124M (C) | $124M is the round; valuation undisclosed [src-20260204-ce7053]; $333.07M post on a $50M C-1 tranche (Forge) [src-20260204-7a0c74] vs $374M (PrivateMarketView): label estimate | low |
| NAM | $2.96T; 12.6M x ~$107K | $2.90T value added 2025; 12.65M employees; $112,261 avg comp [src-20261013-a7c995] | high |
| IFR | 34,200 US vs 295,000 China (2024) | Correct for 2024 [src-20250925-5d6799]; 2025 is 38,428 US (+12%) vs 354,226 China [src-20260924-28b59b] (prelim 38,000 / +11% in [src-20260618-c903cc]) | high |
| IEA refining | Top refiner 72%; China ~85% of REE refining | ~72% of refined energy minerals and >90% of REE refining [src-20260721-89b0cf] (med, via Skillings) vs top-supplier REE share fell from >90% to 85% [src-20260716-6a06e4] (high) vs ~70% avg refining share [src-20250521-c62d29]. Use 85% with the 2026 IEA cite | high |
| Deloitte | 3.8M needed, 1.9M unfilled | Correct (2024-2033) [src-20240416-b69154]; 2026 update: 2.3M technician openings 2025-2030 [src-20260910-a2cd42]; do not combine | high |
| Also stale | SendCutSend $1B (B); Arda ~$700M; Mariana $1.5B | SendCutSend $2.1B Series B, Oct 2026 [src-20261020-487a39] (med); Arda $1.5B [src-20261020-914a64]; Mariana valuation not disclosed [src-20260803-30e6d5] | |

---

## Appendix A. Glossary

| Term | Definition |
|---|---|
| ABL | Asset-based lending: credit secured by receivables and inventory |
| AS9100 | Aerospace quality management standard; table stakes for flight parts |
| AD/CVD | Antidumping and countervailing duties on unfairly priced imports |
| BOM | Bill of materials |
| CAM | Software turning a 3D model into machine toolpaths |
| CMMC | DoD cybersecurity certification for contractors |
| CSO | Commercial Solutions Opening, a fast DoD solicitation |
| DFARS | DoD procurement rules, incl. specialty-metal sourcing |
| DPA Title III | Defense Production Act authority to fund domestic capacity |
| FFP | Firm fixed price contract |
| FPY | First-pass yield: share passing inspection first time |
| IDIQ | Indefinite-delivery, indefinite-quantity contract vehicle |
| ITAR | US export control limiting defense work to US persons |
| Job shop | Small owner-run shop building to a customer's drawing |
| LIFO/FIFO | Inventory accounting methods; LIFO lowers margins when prices rise |
| LPBF | Laser powder bed fusion, a metal 3D printing process |
| LRIP | Low-rate initial production |
| MES | Software that tracks and directs shop-floor work |
| NADCAP | Accreditation for special processes (heat treat, NDT, coatings) |
| NDT | Non-destructive testing |
| Nesting | Packing parts on sheet or stock to minimize scrap |
| NRE | Non-recurring engineering: one-time setup cost before production |
| OSC | DoD Office of Strategic Capital, a lender |
| OTA | Other Transaction Agreement, fast non-FAR prototype contract |
| PPBE | DoD planning, programming, budgeting and execution process |
| SBIR | Staged federal R&D grants to small businesses |
| Section 232 | National-security tariff authority (1962 statute) |
| Service center | Metal distributor that stocks, cuts and ships |
| Utilization | Share of available machine hours actually producing |

## Appendix B. Source map (5 per layer)

| Layer | Sources |
|---|---|
| metals-supply | [src-20260803-30e6d5] [src-20260623-d1790b] [src-20251103-ee9b27] [src-20260716-6a06e4] [src-20261021-16bb64] |
| fabrication | [src-20260519-38c7ed] [src-20261020-487a39] [src-20260701-027c1b] [src-20260204-ce7053] [src-20261016-d61bc1] |
| precision-parts | [src-20260807-b0dc5b] [src-20261014-015327] [src-20250708-2aa3ad] [src-20260802-ef6506] [src-20260219-2125d7] |
| materials-rd | [src-20260617-f9d293] [src-20260917-1bcb81] [src-20261022-37a0ea] [src-20261016-29997e] [src-20260720-840ae3] |
| factory-ai | [src-20261020-914a64] [src-20260513-83aa83] [src-20260106-60b745] [src-20260804-0e8130] [src-20261004-9b47f5] |

## Appendix C. Gaps and next actions
- Hadrian revenue: two low-confidence figures conflict; get a primary number.
- Startup gross margins: none disclosed; ask Senra, SendCutSend.
- Refining TAM and economics: no free source found.
- Fabrication TAM: none; Census CBP gives counts and payroll only [src-20250626-23f6d9]. Next: 2022 Economic Census receipts by NAICS 3323/3327.
- AI/robotics cost decline over 24 months: no source.
- Valuations for Senra, Machina: secondary-data estimates only (Forge, PrivateMarketView), low; Mariana undisclosed.
- Periodic $7.5B round: talks in Bloomberg/Forbes; "closed" only on an AI-compiled page [src-20260612-5506d2].
- Golden Dome money flows: none in law text yet [src-20251218-f0d6ef]. Freeform Skyfall go-live: unconfirmed.
- ABL use by startups: none evidenced.
- Exits (Q14): no comparable acquisition above $100M in repo.

## Appendix D. Ten sources for one hour
1. [src-20261022-80fd75] SPC slide 8 deck.
2. [src-20260807-b0dc5b] Hadrian Series D and the capex-by-debt rule.
3. [src-20260921-876080] Power on capex ahead of contracts.
4. [src-20261004-9b47f5] Ex-Hadrian programming head on what Opus is.
5. [src-20260802-ef6506] Boeing on Hadrian share and price.
6. [src-20250708-2aa3ad] Raytheon on price, lead time, utilization.
7. [src-20260519-2d6ceb] Belosic on SendCutSend economics vs China.
8. [src-20260701-027c1b] Senra operating profile.
9. [src-20260623-d1790b] Mariana's autonomous mine and RL control.
10. [src-20260402-1b5d6c] Section 232 April 2026 proclamation.

## Appendix E. Source coverage (ledger, 2026-10-25)

Full per-source ledger (1,437 rows: id, type, category, read status, key facts, primer section): `insights/exports/primer-ledger.csv`. Summary:

| Bucket | Count | Read status |
|---|---|---|
| Expert calls read line by line | 20 | yes: every line read (about 118K words); notes in the ledger |
| Promoted from dup/noise after full read (CloudNC x2, AI Robotics) | 3 | yes; now cited |
| Other cited sources | 202 | partial: cited passages read in the body; long podcast transcripts read via summary plus keyword pass |
| On-thesis, not cited | 419 | no: machine-read (keyword and number extraction on full body, plus summary). About 1.5M words, not read line by line |
| Form D and federal-award stubs | 256 | data row checked: 237 match a company in raising-now or repeat-orders; 19 are history rows for excluded or non-target companies |
| Noise / off-thesis / duplicates | 343 / 115 / 71 | no: full body keyword-scanned to confirm the category; 66 high-keyword items hand-checked, 4 promoted (1 to adjacent) |
| Of the rows above, no body text captured (LinkedIn, TBPN stubs, empty pages) | 14 | no: nothing to read beyond the stub |

Honest limits: about 2.2M on-thesis words exist; about 120K (5%) were read line by line: 20 expert calls plus the 3 promoted items. Not read line by line: 8 other on-thesis expert calls (5 cited, 3 uncited; passages and summaries used) and all 99 on-thesis podcasts (27 cited). 20 off-thesis or noise expert calls were checked for category only.
