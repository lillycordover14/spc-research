# AI-native industrial production: VC primer

_Version 5, dated 2026-10-26 (America/Chicago). Overwritten on each rerun. Built from the anip repo: sources/ (1,437 records across all types), companies/, insights/ (signals, questions, thesis, weekly/2026-W43, producers-comparison, software-first-platforms, cross-sector-map, raising-now, repeat-orders-evidence, unit-economics, failures-and-pivots, incumbents-vs-ai-native, materials-science-semis, must-read-sources, huddle-prep). Free sources only; no AlphaSense searches run by the agent (the AlphaSense-arranged expert calls Lilly filed are used)._

**New to this topic? Start with section 1 and section 1A (the macro primer), then come back to section 0.** Acronyms are spelled out on first use and collected in Appendix A.

**How to read this doc.** Three kinds of statement are kept apart:
- Plain sentence ending in `[src-…]` = sourced fact (a filing, release, dataset or reported figure).
- **Claim (who):** = something a company, founder or expert asserted. Sourced, but not verified.
- `[inference]` = my read. Not sourced; argue with it.

Confidence (`high/med/low`, per taxonomy) is marked on numbers from a deleted post, Wikipedia, Harmonic estimate or a single press article. Contradictions are shown side by side. Excluded from the category by Lilly and not covered except as failure examples: microagi, Pelico, C-Infinity, Dirac, Synera, Bright Machines (failure example only), Retrocausal, DEEP.FINE.

---

## 0. Decision summary

_In one line: the category is real and defense demand is strong, but most buyers do not pay much for speed alone, factories must be built before contracts arrive, and nobody has yet shown that the software makes each part cheaper or better over time._

**Verdict [inference].** Back capital-light owner-operators at Series B only where speed and qualification are already paid for (Senra, Freeform, Isembard, as diligence hypotheses). Use Hadrian, Divergent and SendCutSend as benchmarks. Do not pay software multiples for job-shop economics until a company shows unit cost or quality improving with volume. Nobody in the repo shows that yet.

**What the 102 podcasts changed (new in v3).** All 102 podcast files were read in full; the 5 points below changed the view. Each is a speaker's claim unless marked.
- **A. Speed is not worth much to most buyers.** Hadrian's own CEO: "one of the things that I was wrong about is speed ... most of the market just doesn't value speed. The market very much values flexibility, scale, total program cost"; only one rocket company turned speed into value [src-20260921-876080]. That weakens the "speed premium" in finding 1 below beyond urgent and prototype work.
- **B. Capex comes before contracts.** Power: "0% chance of growing revenue unless you spend a billion in CapEx"; only customer prepayment or long-term infrastructure credit has funded such companies [src-20260921-876080]. Machina, Divergent and SendCutSend describe the same debt-for-machines, equity-for-software split (section 2.5).
- **C. Cheap labor is not the edge.** Labor is "less than 10% of COGS" in a new automated plant; China wins on a co-located supply chain (Baglino) [src-20260513-bdc044]. SendCutSend says it can beat China on only about 20-25% of its work [src-20260519-2d6ceb]. Defense is the protected lane (section 2.4).
- **D. The gate is adoption and qualification, entered through repair parts.** The Navy: "we have an adoption problem", not a technology problem [src-20250319-f21bec]. Machina's main product was still "in qualification phase" in April 2026 [src-20260430-30ea09]; it and Divergent enter through sustainment (replacement parts for old weapons whose suppliers are gone) [src-20251015-e9edbf][src-20260821-1c5a08].
- **E. The edge leaks both ways.** SendCutSend customers "outgrow us" by buying their own machines [src-20251002-6a5afd]. Enablers such as GrayMatter now sell turnkey robot cells "as a service" to incumbents [src-20261022-3335bd], giving old shops the same automation. Repeat-order evidence at Divergent and GrayMatter is company claims only.

**What the expert calls and other sources showed.**

1. **Price is not the wedge.** The only "cheaper" report (Raytheon, about 50% lower) came from RFQ (request for quote) prices before any part was delivered, on a relationship brokered by RTX Ventures, a Hadrian investor [src-20250708-2aa3ad]. A Boeing customer says Xometry is cheapest and a 20-25% price gap means re-sourcing [src-20260802-ef6506]. Three Boeing voices say parity or more: "we have actually paid probably more" (Boeing Defense head of product) [src-20260818-9b2d5c]; Hadrian priced at "PCC or slightly more" (PCC = Precision Castparts, a large incumbent supplier owned by Berkshire Hathaway) (Boeing strategy/M&A lead) [src-20250712-e5e110]. A Northrop GM: "Cost is secondary. Cost is driven usually by schedule" [src-20250707-3b7a46]. The premium buyers pay is for speed.
2. **Quality at complexity is the open risk.** "None of their parts right now are flying" (Boeing Defense) [src-20260818-9b2d5c]. "We haven't received parts back that matched the specification" (PI, ex-Anduril hardware) [src-20250709-43486e].
3. **Share per customer is capped by design.** SpaceX caps a shop at about 1/3 of its revenue (ex-Hadrian head of engineering) [src-20250708-342eaf]. After a PCC factory fire, Boeing "will never" concentrate one part family on one supplier [src-20260818-9b2d5c]. Revenue per customer has a ceiling, so growth needs many primes [inference].
4. **The moat is workflow plus qualification, and AI CAM is coming from below.** Insiders say the edge is Opus, Hadrian's MES (manufacturing execution system: the software that directs work on the shop floor), plus factory design, not AI that writes toolpaths [src-20260817-8867f2][src-20261004-9b47f5]. CloudNC sells CAM Assist (AI for CAM, the software that turns a 3D model into machine instructions) to every shop and tests it in its own UK factory [src-20261009-7cafd0]. Programs last about 50 years, and suppliers for a 2035 aircraft are being chosen now [src-20260818-9b2d5c].
5. **Materials-rd budgets are not growing fast.** A former Moderna director says buyer budgets have not grown "crazily" in 5-6 years and that the gain is a "step one productivity boost" [src-20260909-af3e60] (low). An Albert Invent director says chemical majors reject royalty models ("The short answer is no") [src-20260913-3ad55e].

6. **Fast prototype contracts hide the quality gap.** OTA contracts (Other Transaction Agreements, fast prototype contracts outside normal federal rules) waive many mil-spec (military specification) quality requirements; when programs move to standard production contracts, "there's a gap" in statistical lot inspection (sampling batches of parts to prove they meet spec) that Hadrian "is still maturing" on. At thousands of parts its cost curve "asymptotes at a higher level" than traditional shops, and schedule is "near equal" once full inspection is counted (Boeing executive director, customer spending "low single millions" a year, "a fraction of a percent" of outside spend) [src-20260908-ed94f0]. He thinks "low tens of millions" could replicate Hadrian; a Northrop customer engineer thinks it is hard to copy [src-20260802-36d46c].
7. **Distributed networks win on urgency, not cost.** An Isembard customer paid $2,300-3,000 for 4-5 simple parts in 2-3 days that would cost about GBP150-200 in China, and sends larger batches to Chinese shops [src-20260621-f96bbd]. An Airbus Defence supply-chain head sees such networks limited to prototypes and non-critical parts while primes consolidate to fewer tier-1s [src-20251106-dfddcb].
8. **The only learning-over-time number.** Hadrian's first programming head: "within a couple of years, we saw a 50% cut" in order-to-first-article time; 70% 24-hour utilization is "very, very realistic"; pricing targets about 30% contribution margin; Opus "is replicable" and the moat is "financial power" plus a five-year head start [src-20261004-9b47f5].

9. **Hadrian's own numbers are claims, and they cut both ways.** **Claim (Chris Power, Hadrian CEO, on an investor-hosted panel):** "close to a billion in revenue next year", about 30% "pure software", utilization 65-80% vs about 10% at primes, "$4 of revenue on $1 of capex", labor "five to eight X more efficient ... it's not about being cheaper" [src-20260610-779f8b]. **Claim (Power):** "0% chance of growing revenue unless you spend a billion in CapEx" [src-20260921-876080]. Read together: capex comes before contracts, and the software share is a stated plan, not a reported number [inference].
10. **High utilization does not need robots.** **Claim (Jim Belosic, SendCutSend CEO):** lasers run at 86% versus the 77% Amada promised with sheet-loader automation, and top Amada shops are "really happy if they get 50 or 60"; he rejected $4M of conveyance because high-mix, low-volume work defeats rigid automation [src-20260626-541ac8]. The edge is software-driven scheduling and quoting, not robotics [inference].
11. **Roll-up economics set the floor.** **Claim (Re:Build co-founder):** "effectively it's a 30% gross margin", acquisitions at "seven times EBITDA" [src-20241001-28c2aa]. That is the incumbent benchmark an AI-native plant must beat to justify venture capital [inference].
12. **Policy now buys demand, not just capacity.** The FY26 NDAA authorizes multiyear munitions procurement (Sec. 804(b)), a purchase-commitment program with advance payments (Sec. 867) and a spares review aimed at advanced manufacturing (Sec. 1842) [src-20251218-f0d6ef]. These are the first channels that could turn prototype wins into multi-year orders [inference].

**Evidence on the four thesis claims** (claims as numbered in insights/thesis.md)

| # | Thesis claim | For | Against | Read [inference] |
|---|---|---|---|---|
| 1 | Demand for domestic production is structural | Lockheed 7-year cell deal [src-20261014-015327]; Navy $900M [src-20260320-67ba4c]; Thales CPO: capacity is the pain after COVID-era supplier bankruptcies [src-20251110-84b67e]; Boeing has used parts taken from non-flying aircraft [src-20260818-9b2d5c] | 34% spindle utilization at existing shops [src-20250120-419768]; Taiwan 20-30% cheaper and Vietnam/Malaysia cheaper still [src-20250709-43486e]; Boeing makes about 40% of parts in-house and holds 6 months of inventory [src-20250712-e5e110] | True for defense capacity and speed. Commercial rate demand not shown |
| 2 | Owning the plant creates a data loop | Freeform and Mariana score 2 (section 6). Ex-Hadrian: about 80% of non-CAM labor automated, lead times cut about 50% [src-20250708-342eaf]; reprogramming saved 50-80% of CAM time [src-20260611-7b80f0] | Toolpaths come from third-party CAM, with Vericut (simulation software) as the check [src-20260611-7b80f0][src-20261004-9b47f5]; CMM (coordinate measuring machine) inspection is manual [src-20260817-8867f2]; a buyer asks "is it actually" software-enabled [src-20250729-a0a78c] | Workflow automation is real. Learning with volume is not evidenced |
| 3 | Moats: process data, secured capacity, qualification | Trusting a new supplier takes 5-10 years [src-20250712-e5e110]; change-of-control clauses in defense contracts (contracts that can be voided if the supplier is sold) [src-20260817-8867f2]; lock-in from 50-year programs [src-20260818-9b2d5c] | Share caps (finding 3); 90% of the first 10 Hadrian employees gone by year 5 [src-20260817-8867f2]; incumbent PCC is also automating [src-20250712-e5e110] | Qualification is a moat once paid, but it caps share. No data moat evidenced |
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
| software-first | Arda: CAD-to-work-instructions agent inside Anduril's ArsenalOS; $160M Series A at $1.5B [src-20261020-914a64] | Capital-light, fast to revenue; needs a host plant for data and competes with Siemens and Rockwell on the installed base [src-20250326-cc1810][src-20260804-0e8130] |
| hybrid | Hadrian (owns factories, now embeds cells inside Lockheed's Grand Prairie plant on a 7-year deal) [src-20261014-015327]; Isembard (owned plus franchised factories on MasonOS) [src-20260909-b547c7] | Tries to get owner data with partner capital; harder to underwrite because economics are split |

The core tradeoff in one line: owner-operators buy data ownership and pricing power with capital intensity; software-first buys speed and margin with data dependence on someone else's plant [inference].

---

## 1A. The big picture: macro primer for a newcomer

_This section assumes no background. It explains what is happening in US and allied manufacturing, why money is flowing in now, how buyers actually purchase parts, and how venture investors think about it. Every number has a source. Where a number is my reading, it says [inference]._

### 1A.1 Manufacturing in one page

- **How big it is.** US manufacturing added $2.90 trillion of value in 2025. That is 10.1% of GDP (gross domestic product, the total value of what the economy produces). It employs 12.65 million people, at average pay of $112,261 [src-20261013-a7c995].
- **How it is organized.** Think of a pyramid. At the top are a few **primes**: the big companies that sell finished systems (a missile, a jet, a submarine) to the government. The top five US defense contractors in FY2023 (fiscal year) were Lockheed Martin ($61.4B of contracts), RTX/Raytheon ($24.1B), General Dynamics ($22.9B), Boeing ($20.1B) and Northrop Grumman ($16.3B) [src-20251215-98f650]. Below them are **tier-1 suppliers** (big sub-systems), then **tier-2 and tier-3 suppliers** (individual parts, castings, forgings, wire harnesses, raw metal).
- **The bottom of the pyramid is small and old.** The US has 17,156 machine shops. 83% have fewer than 20 employees [src-20250626-23f6d9]. They are called **job shops**: small owner-run businesses that make parts to a customer's drawing. The count is shrinking: 4,874 machine shops were lost from 2002 to 2018, about 20% [src-20250909-29c826]. **Claim (Isembard):** the average owner is over 65 and 40% plan to retire within five years [src-20260310-45bab3].
- **The top has consolidated.** Aerospace and defense primes fell from 51 to 5 since the early 1990s [src-20220215-45c353]. Fewer buyers means fewer, larger programs, and more power over suppliers.

**What this means.** The supply base that makes physical parts is fragmented, aging and shrinking, while the buyers at the top are few and powerful. That gap is the opening every company in this primer is trying to fill [inference].

### 1A.2 Why this is happening now: six forces

**1. Defense needs more munitions and ships, fast.** After Russia invaded Ukraine in 2022, the US and allies used up munitions faster than factories could replace them. Congress's research service says much of the concern about the defense industrial base "has focused on munitions production due in large part to high rates of expenditure" [src-20251215-98f650]. Primes are now signing long deals with new producers. Lockheed signed a 7-year deal to put Hadrian's automated machining cells inside its missile plant [src-20261014-015327]. The Navy put $900M toward Hadrian plants for submarine parts [src-20260320-67ba4c].
- _What this means:_ demand is strongest for defense parts that are late today. It depends on budgets that Congress sets each year [inference].

**2. China controls key inputs.** China leads refining for 19 of 20 strategic energy minerals, with about 70% average share [src-20250521-c62d29]. It makes about 94% of rare-earth magnets (the strong magnets inside motors, drones and missiles) and cut magnet exports in April 2025 [src-20251103-ee9b27]. The US imports 100% of 16 mineral commodities, 67% of rare earths and 57% of refined copper [src-20260206-04fe3e]. Almost 90% of the most advanced chips are made in Taiwan [src-20230928-c47558].
- _What this means:_ "Can we make this at home?" is now a national-security question, not only a cost question. That is why governments pay for domestic capacity even when it costs more [inference].

**3. Tariffs make imported metal and parts dearer.** Tariffs are taxes on imports. Since April 2026, products made almost entirely of steel, aluminum or copper face a 50% tariff; products that contain them face 25%; and 10% if the metal was melted or smelted in the US [src-20260402-1b5d6c]. This helps US mills: Nucor's gross margin rose from 14% to 20% (part of it a one-off refund) [src-20260812-77d6f5]. It hurts US companies that buy metal: Nucor's own fabrication segment reported "margin compression resulting from higher steel input costs" [src-20260812-77d6f5].
- _What this means:_ tariffs are set by presidential proclamation and can be reversed. They are a tailwind, not a foundation [inference].

**4. There are not enough skilled workers.** Deloitte and The Manufacturing Institute project 3.8 million US manufacturing jobs to fill from 2024 to 2033, with 1.9 million possibly unfilled [src-20240416-b69154]. Manufacturing had 522,000 open jobs in August 2026, against a pre-pandemic average of 432,000 [src-20261013-a7c995]. The Defense Department says it needs at least 122,000 more shipbuilders, engineers and other critical workers by 2028 [src-20250101-af28c1].
- _What this means:_ the bottleneck is people, not machines. Software that lets a less experienced worker do skilled work is the core promise of "AI-native" production [inference].

**5. The government now lends and buys, not just regulates.** Six tools matter (each explained in 1A.4): the NDAA, CHIPS, the IRA's 45X tax credit, DPA Title III, the Office of Strategic Capital and Section 232 tariffs. Together they lower the cost of building a plant and, more recently, promise to buy output for several years.

**6. Money is available, but not cheap.** Venture investors put large sums into this category in 2026 (Hadrian raised $1.37B in one round [src-20260807-b0dc5b]). But interest rates are rising again: the Federal Reserve raised its benchmark rate to 3.75-4.00% on September 16, 2026, saying "inflation remains elevated" [src-20260916-f0c016]. Factories are mostly paid for with loans once the first one works [src-20260817-c48f28]. Higher rates make every new plant more expensive to finance [inference].

**What would reverse the trend.** A defense budget cut or delay, tariffs struck down, a peace that slows munitions buying, or a jump in rates. Also: existing shops have spare capacity. The average machine in a US shop cuts metal only 34% of the time, against a 70% target [src-20250120-419768]. Some demand can be met without new factories.

### 1A.3 How a buyer actually buys a part (the procurement path)

This is the most important mechanism to understand. A new producer does not win "the market." It wins one part number at a time, at one buyer at a time.

1. **Request for quote (RFQ).** A buyer at a prime sends a drawing and asks suppliers for a price and delivery date.
2. **Supplier qualification.** Before a new supplier can make flight or weapon parts, the buyer checks its quality system. The common standard is **AS9100**, the aerospace quality management standard. Special processes (heat treating, coatings, inspection) need **NADCAP** accreditation. Buyers told us qualification takes 9-12 months at Raytheon [src-20250708-2aa3ad] and 1-2 years at Northrop [src-20260802-36d46c].
3. **First article inspection (FAI).** The supplier makes the first part. Every dimension, material and process is checked against the drawing and written up in a standard report (AS9102). FAI is repeated whenever the design, material, process, tool or location changes, or after two years without production [src-20190801-e81d7b]. _This is why moving a part to a new supplier is slow and costly._
4. **Prototype and low-rate production (LRIP).** Small quantities, often under fast contracts such as **OTAs** (Other Transaction Agreements, which skip much of the normal federal acquisition rulebook and can roll into production without a new competition) [src-20241219-9f8fcc].
5. **Rate production.** Steady, high volume. Here price per part and consistent quality decide who wins. A Boeing executive says at around 1,000 parts a traditional shop is cheaper than Hadrian [src-20260908-ed94f0].
6. **Repeat orders and multiyear contracts.** The prize. Programs can last about 50 years, and suppliers for a 2035 aircraft are being chosen now [src-20260818-9b2d5c]. The FY26 NDAA (National Defense Authorization Act, the yearly defense policy law) now allows multiyear buying for SM-6, Tomahawk, AMRAAM, JASSM, LRASM and PAC-3 missiles [src-20251218-f0d6ef].

**Two rules that limit any one supplier.** Buyers cap how much they depend on one shop (SpaceX caps a shop at about 1/3 of its revenue) [src-20250708-342eaf]. After a factory fire at a major supplier, Boeing says it "will never" put one part family with one supplier again [src-20260818-9b2d5c].

**What this means.** Early wins are fast prototype work that buyers pay a premium for. The test of a real business is whether those wins turn into repeat rate-production orders. That is exactly Lilly's question 1, and the evidence so far is thin (section 8) [inference].

### 1A.4 The policy toolkit, in plain English

| Tool | What it is | What it does for producers | Source |
|---|---|---|---|
| NDAA | The yearly law that sets defense policy (not the money itself; money comes in separate appropriations bills) | FY26 version: multiyear munitions buying (Sec. 804(b)); an Industrial Base Fund for castings, forgings and machine tools, with purchase commitments of up to 10 years and advance payments (Sec. 867); a review of which spare parts advanced manufacturing can make (Sec. 1842) | [src-20251218-f0d6ef] |
| DPA Title III | Defense Production Act of 1950. Title III lets the government pay to expand domestic capacity: direct purchases, purchase commitments, even installing equipment in private plants | 23 awards, $820.5M since Jan 2025, mostly rare earths and rocket motors; none yet to the startups we track | [src-20251215-98f650][src-20261019-68fd3d] |
| OSC | Office of Strategic Capital, a Defense Department lender created in 2022. It makes loans and loan guarantees for 34 critical technology areas, including advanced manufacturing | $620M loan to Vulcan Elements for a magnet plant; FY2026 funding of $97.8M can back up to $4.4B of loans, and the 2025 reconciliation law adds credit subsidy for up to $100B each for critical minerals and covered technologies | [src-20251103-ee9b27][src-20260908-f6558e] |
| CHIPS Act | 2022 law: $52.7B for FY2022-2027 for US chip factories, research and workforce | Mostly helps chip fabs; it co-funded the Vulcan magnet deal with a $50M incentive | [src-20230928-c47558][src-20251103-ee9b27] |
| IRA 45X | A per-unit tax credit from the 2022 Inflation Reduction Act for US-made energy components. Critical minerals earn 10% of production costs | The 2025 tax law (P.L. 119-21) phases the minerals credit out 2031-2034 and bars Chinese-linked supply chains | [src-20251001-45a0c1] |
| Section 232 | A 1962 law letting the President set tariffs on national-security grounds | 50/25/10% metals tariffs (see 1A.2) | [src-20260402-1b5d6c] |
| Buy American / Specialty Metals | Laws requiring the Defense Department to buy US-made goods; specialty metals (titanium, nickel, some steels) must be melted in the US | Protect domestic demand for metal and parts | [src-20251215-98f650] |

**What this means.** Policy is strongest for metals and minerals (loans, credits, tariffs). For machined parts, policy works mainly through prime contracts and the new multiyear authorities [inference].

### 1A.5 How big is the market?

No free source gives a clean market size (TAM, total addressable market) for "AI-native production." What we have:
- All US manufacturing: $2.90T value added [src-20261013-a7c995].
- Metal service centers (distributors that stock, cut and ship metal): about $200B of revenue (med) [src-20251201-4b732d].
- Precision manufacturing: about $71B by 2026, machine-shop segment over $60B (med, one analyst memo) [src-20251024-2e5383].
- Global industrial robot installs: $18.6B in 2025, a proxy for automation spending [src-20260924-28b59b].

Section 3 has the full table. _What this means:_ the markets are large, but each startup sells into a narrow slice (one part type, one buyer group). Share per buyer is capped (1A.3), so growth needs many buyers [inference].

### 1A.6 How venture investors see it

- **It costs a lot to build.** A first six-machine factory cost "well north of $10 million" [src-20260817-8867f2]. Hadrian's Mesa plant was about $200M [src-20250820-cfbf02]. Software companies do not need this.
- **Margins are lower than software.** Gross margin is revenue minus the direct cost of making the product, as a share of revenue. Software companies often run far higher than manufacturers. Benchmarks here: Proto Labs 44.5% [src-20260206-8bb619]; Xometry's marketplace 34.7% [src-20260224-a7b149]; metal service centers 18-32% [src-20260729-407fd7][src-20261021-16bb64]; a manufacturing roll-up "effectively ... 30%" (claim) [src-20241001-28c2aa].
- **Who pays for what.** Venture equity pays for the team, the software and the first plant. Banks, equipment lenders and the government pay for plants two and beyond, once a plant is proven. Hadrian: "equity never funds factory construction" (claim) [src-20260807-b0dc5b]; it has a $360M bank credit line [src-20260817-c48f28].
- **The bull case.** If software lets one plant run at much higher utilization with fewer skilled workers, it can earn better margins than a job shop and win share. **Claim (Chris Power, Hadrian CEO):** utilization of 65-80% versus about 10% at primes [src-20260610-779f8b].
- **The bear case, with equal weight.** Several buyers say they pay the same or more, not less (section 0). Some see these firms as "better suited to debt than VC" [src-20250709-43486e]. Recent failures: Daedalus (an AI-run machining factory) went insolvent in August 2026 [src-20260801-4532f6]; Markforged went from a $2.1B valuation to a $42.5M sale [src-20261023-63156a]; Bright Machines' SPAC (a listing via a shell company) fell through [src-20240527-6a4884].
- **Exits are unproven.** The repo has no acquisition of an AI-native producer above $100M (Appendix B). Likely exit paths are sale to a prime or incumbent supplier, an IPO (stock listing) at scale, or continued private ownership with debt [inference].

**What this means for SPC.** The question is not "is manufacturing coming back?" It is "can a software-run plant earn better margins than a job shop, and turn fast prototype wins into multi-year orders?" Everything after this section tests that [inference].

---

## 2. Why now: the drivers in detail, ranked

Section 1A gave the short version. This section gives the evidence for each driver. They are ranked by how much each one moves revenue for the companies we track [inference on the ranking]. Each driver ends with "what this means", in plain words.

### 2.1 Defense demand (structural for 5-10 years; budget swings at the margin)
**How it works.** The US is buying more missiles, ships and drones than its factories can make. The big contractors ("primes", such as Lockheed and Raytheon) cannot add qualified suppliers fast enough. So they are signing multi-year capacity deals with new producers.
- Lockheed signed a 7-year deal to put Hadrian's automated machining cells inside its missile plant (PAC-3, THAAD, PrSM and GMLRS missiles), starting early 2027 [src-20261014-015327]. The Navy put $900M next to more than $1.5B of Hadrian money for three plants making submarine parts [src-20260320-67ba4c]. Divergent will build Tomahawk structures for RTX [src-20260601-976843] and is opening a Long Beach plant sized for 30,000 missile airframes a year [src-20261023-e02543]. The Army chose Vulcan Elements for magnets for a 1M-drones-a-year program [src-20260923-c53c99].
- **Claim (Chris Power, Hadrian CEO):** labor hours per submarine rose from about 13M to more than 70M, and the enterprise is about 50M labor hours a year short [src-20260610-779f8b].
- **Navy, on the record:** a NAVSEA (Naval Sea Systems Command) official says more than 100 ships are on contract and 55 are in construction. He also says: "I do not believe we have a technology problem, we have an adoption problem." One recent boat carries more than 100 critical parts made by 3D printing, and the Navy has spent more than $200M on it, but getting the technical authority to approve those parts took time [src-20250319-f21bec]. The nuclear supply chain shrank from more than 17,000 suppliers to about 5,000 [src-20250319-f21bec].
- **The catch: demand is lumpy.** **Claim (Power):** the government pays once a year and "may not buy missiles next year" [src-20260908-65fab6]. On an Air Force panel, Divergent's CEO said "the big thing is always demand signal", and a Boeing-owned satellite maker said "cadence and multi-year contracts develop capacity" [src-20260504-38bee3]. A Raytheon manager reports suppliers at 80-90% utilization with 9-10 months for castings [src-20250708-2aa3ad].
- **What this means [inference].** Demand is real, but qualification (getting each part approved) is the gate, and it is slow. Multi-year contracts (section 10) are what turn demand into factory loans.

### 2.2 Skilled labor (structural), and why cheap labor is not the point
**How it works.** Factories cannot hire enough machinists, welders and programmers. Software that makes tasks easier lets people with no factory background do the work.
- Headline numbers are in section 1A.2 (Deloitte: 3.8M jobs needed). A 2026 Deloitte follow-up counts 2.3M technician openings for 2025-2030 but leaves out machinists, so do not add the two [src-20260910-a2cd42].
- **Claims (owner-operators):** Hadrian trains new operators in 30-40 days instead of a decade [src-20260926-70087f]. SendCutSend hired 200 welders in a year, mostly people with no factory experience; average floor age is about 25 [src-20260525-4a12ab]. Shipyard starting pay is about $22-23 an hour and average tenure is about 4 years (Navy panel) [src-20250319-f21bec].
- **The important correction.** Drew Baglino (ex-Tesla, now Heron Power): in a new automated factory, in China or the US, "the labor differential is less than 10% of COGS" (cost of goods sold), maybe under 5%. What makes China cheaper is that its supply chain sits close together: all ~7,000 car parts within a 3-hour drive [src-20260513-bdc044]. **Claim (Belosic, SendCutSend):** a dark (fully automated) factory is not the answer; his edge is software plus well-paid people [src-20260519-2d6ceb].
- **What this means [inference].** Saving on wages alone will not beat China. The edge is having enough trained people at all, plus being close to customers and suppliers.

### 2.3 Tariffs (policy-driven; reversible)
**How it works.** Section 232 (a 1962 law letting the President set tariffs for national security) raised steel and aluminum tariffs from 25% to 50% in June 2025. Since April 6, 2026: 50% on goods made almost entirely of steel, aluminum or copper; 25% on goods that contain them; 10% if the metal was melted in the US. Grid equipment gets 15% until 2028 [src-20260402-1b5d6c].
- Who wins and loses: Nucor (a steel mill) cites the tariffs for fewer imports; its gross margin rose to 20% from 14%, though about 1.3 points came from a one-off refund. Its own fabrication unit reported "margin compression" from costlier steel [src-20260812-77d6f5]. Reliance (a metals distributor) says aluminum prices are "historically elevated largely due to" the tariff [src-20260728-ae7dea].
- **What this means [inference].** Tariffs help metal makers and hurt metal buyers, including fabrication startups. The 10% vs 25% gap rewards suppliers who can prove where their metal was melted, which favors software-native firms.

### 2.4 China and offshore competition (structural), split by market
**How it works.** China makes most of the world's magnets and refines most critical minerals (section 1A.2). On ordinary commercial parts it is usually cheaper. The split that matters is protected versus open markets.
- **Protected markets (defense).** Defense buyers are barred by DFARS (defense purchasing rules) from buying from a "foreign entity of concern", so price against China does not decide the sale [src-20250429-6f9155]. ITAR (an export-control law) keeps defense work onshore too. **Claim (Ed Mehr, Machina CEO):** "if you go head-to-head with China ... you're losing", so Machina starts in defense, which "won't source from China" [src-20260622-7846f9].
- **Open commercial markets.** **Claim (Belosic):** SendCutSend can "meet or beat China" on only about 20-25% of its work [src-20260519-2d6ceb]; customers "shop with their wallet" and will offshore "when the price is half" [src-20251002-6a5afd]. An ex-Anduril hardware lead says Taiwan is 20-30% cheaper and Vietnam and Malaysia cheaper still, even with tariffs [src-20250709-43486e]. Counter-claim: Isembard says it beat Chinese shops "on speed and cost" for a jet-engine customer (unnamed) [src-20260909-b547c7].
- Commercial buyers do pay for "insurance": the 2021 chip shortage showed a few hundred dollars of parts can stop an $80,000 car (**Claim, Vulcan CEO**) [src-20250429-6f9155].
- **What this means [inference].** Defense is the protected lane where US producers can win. In commercial work they win only where speed or supply security matters more than price.

### 2.5 Money: capex before contracts, and debt versus equity
**How it works.** A factory must be built before a buyer will sign a production contract, because the buyer wants proof the supplier can deliver. That means spending large sums ("capex", capital expenditure on buildings and machines) years ahead of revenue.
- **Claim (Power):** "0% chance of growing revenue unless you spend a billion in CapEx because no one's going to give you a production contract unless you've already started executing." Capex runs about 2 years ahead of revenue, and Hadrian was "underwater on financing costs" until late Series B. Only two capex-heavy models have worked: the customer prepays (NASA with early SpaceX; "Pentagon doesn't do this") or long-term infrastructure credit [src-20260921-876080].
- **Debt versus equity.** Equity (selling shares) is expensive money; debt (loans) is cheaper but needs assets or contracts behind it. **Claim (Mehr):** "don't fund physical hardware with equity"; Machina's machine loans cost about 2-3% over the prime rate [src-20260220-0d5345][src-20260320-1361e2], a good package about 8-9% and a risky one 12-14% [src-20260430-30ea09]. Hadrian has a $360M bank revolver (a reusable credit line) [src-20260817-c48f28].
- **What banks will not fund.** **Claim (Belosic):** lenders fund machines but not the software team or R&D [src-20260519-2d6ceb]; banks lend only on common, resaleable machines, so custom lines (anodizing, casting) are "unfinanceable" [src-20260624-3dc6f7].
- Venture and government: Hadrian's $1.37B Series D [src-20260807-b0dc5b]; OSC (the Pentagon's lender) lent Vulcan $620M [src-20251103-ee9b27]. **Claim (Dayna Grayson, Construct Capital):** later-stage industrial funding was about $3B in 2021 and has grown about 10x in 4 years [src-20260702-d79e75], which means more competition for deals [inference]. The Fed raised rates to 3.75-4.00% on Sep 16, 2026 [src-20260916-f0c016], which makes plant loans dearer [inference].
- **What this means [inference].** Equity pays for software, the team and the first plant; loans and government pay for later plants once contracts exist. A company without contracts is stuck paying equity prices for steel.

### 2.6 Power, permits and build time (a hard limit)
**How it works.** A factory needs a large electricity hookup and permits. Both can take years.
- **Claim (Belosic):** "We need 100 times more power"; Reno warehouses lack electrical service; transformers and permits are delayed; "everyone wants to re-industrialize, but we don't have the power" [src-20260519-5cfe14].
- **Claim (Vulcan CEO):** "if you can't get a permit for several years ... running out of cash"; and most magnet-making equipment itself comes from China [src-20250429-6f9155]. Permits for identical equipment take "3 weeks, 3 months, or 3 years" depending on the town (Torus, Utah panel) [src-20260813-1fe8a2].
- **Claim (Mariana CEO):** after permits, a mine or refinery can take about 5 years to build and 3-5 years to ramp [src-20260513-bdc044]; Chinese refineries commission in about 6 months versus 2-4 years in the West [src-20250723-3f3ef8].
- **What this means [inference].** Speed to build and ramp is itself a competitive edge, and power is a site-selection question for every plant.

### 2.7 AI and robotics (enabling, not sufficient)
- US robot installs grew 12% to 38,428 in 2025 [src-20260924-28b59b]. LLM agents now read CAD and write work instructions (Arda: 10 hours to 15 minutes at Anduril) [src-20261020-914a64]. Freeform runs GPU clusters on site to control each printed layer [src-20260219-2125d7].
- Limits: US metalworking robot adoption is only about 3,000 units a year [src-20260618-c903cc]. Robot learning succeeds about 59-66% of the time on a new task versus 99.9%+ needed on a line [src-20260904-267293]. **Claim (Mehr):** physical AI is at "2007-2008 of LLMs" [src-20260220-0d5345]. **Claim (Nox Metals CEO):** "AI just doesn't know so much of the nuance" of a factory [src-20260325-5b68db].
- **What this means [inference].** AI makes office work around the machine (quoting, programming, instructions) faster today. It does not yet run the machines on its own.

### 2.8 More macro facts a newcomer should know
- **The munitions gap, in numbers.** **Claim (Power):** the US buys about 100 Tomahawks a year, versus about 850 fired in one day in the Iran conflict; Ukraine used three years of missile inventory in about six weeks [src-20260908-65fab6]. Lockheed has $60B+ of Pentagon deals to triple PAC-3 output from about 600 to 2,000 a year (trade press) [src-20261015-86f700].
- **Who really makes defense parts.** **Claim (Power):** 60-80% of a prime's output comes from small-business suppliers, which face payment terms of about 300 days which makes them hard to finance [src-20260908-65fab6]. The F-35 relies on "7,100 mom and pop shops" (**Claim, Nox CEO**) [src-20261022-3135b5]. The NDIA's president (ex-Pentagon) says sub-tier suppliers run batches "of 10 or 20", and their real question is "will you keep buying them from me", which is why five-year purchase guarantees matter [src-20260901-a44eee].
- **China's dependence, inside US weapons.** **Claim (Power):** of about 1,000 components in a Navy missile, "probably 150" come from China; about 70% of drone components come from China or Taiwan [src-20260610-779f8b]. China produces 56% of world castings, and the Pentagon relies on a single US foundry for large titanium parts (General Catalyst thesis) [src-20240202-8c6d3b]. China makes over 90% of rare-earth magnets; the US under 1% [src-20250429-6f9155].
- **The US lost its machine-tool industry.** US machine-tool shipments fell from $5B (1981) to $2B (1983); half of US machine-tool firms closed in 1982-87; imports rose from about 10% to about 60% by the late 1990s [src-20240118-4e5ac1]. So even AI-native US factories buy German, Japanese or Italian machines [src-20260310-f52a8d].
- **Labor numbers, freshest first.** In a Q3 2026 NAM survey of 220 manufacturers, 54.9% cite workforce as a top challenge and 4.79% of jobs sit unfilled [src-20260914-b4d55c]. The American Welding Society expects 320,500 welders needed by 2029, with 157,000+ near retirement [src-20261023-57ad95]. US factory labor costs about $46.30 an hour fully loaded, rising 3-4% a year, while a robot fell from $46,000 (2010) to $23,000 (2022) (newsletter) [src-20260826-14e4bb].
- **Precedent: the government has funded capacity before.** In the 1950s the Pentagon paid $239M (about $2.8B today) for 10 giant forging presses and leased them to industry for 4-5% of revenue [src-20240821-44ed1d]. Today's equivalents are OSC loans and Sec. 867 purchase commitments (section 10).
- **Demand from AI data centers.** An AI campus can need up to 50,000 t of copper and 200,000 t of steel; steel prices rose 25% in a year (Robeco) [src-20261007-a642ea]. A legacy fabricator building generator enclosures for Amazon, Google, Apple and Meta has "backlogs working on 2027" (**Claim**) [src-20261022-4234b3]. Bear: AI capex is estimated at 3.63% of GDP, above the railroad boom's 2.24%, and most hyperscalers have near-zero free cash flow [src-20261015-c425a9]. If AI spending slows, this demand pocket shrinks [inference].
- **What this means [inference].** The shortage is in sub-tier suppliers and skilled hands, and buyers' stop-start ordering is what keeps small shops from investing.

### What would break "why now"
- Tariffs reversed or limited by courts (they are proclamations, not laws) would hit metals and fabrication first [inference].
- A flat defense budget or delayed munitions buys would strand plants built ahead of contracts (section 2.5).
- Higher rates raise the cost of the loans that fund plants #2+ [inference].
- Spare capacity exists: the average CNC spindle at existing shops cuts metal 34% of the time versus a 70% target [src-20250120-419768] (med, survey). The US lost 4,874 machine shops (-20%) from 2002 to 2018 [src-20250909-29c826].

---
## 3. Market size by layer

**How to read this.** "TAM" (total addressable market) means the total money spent on something each year. No layer here has a clean, free TAM. Where we only have a stand-in number (a "proxy"), we say so.

**The whole sector.** US manufacturing added $2.90T of value in 2025, about 10.1% of GDP. It employs 12.65M people, paid $112,261 on average [src-20261013-a7c995] (high).

**Layer by layer.**

| Layer | Best free number | What it does not tell you |
|---|---|---|
| Metal distribution | About $200B revenue across about 9,400 sites; the top 50 firms hold about half (2025) [src-20251201-4b732d] (med) | Excludes refining |
| Metal refining | No market size found. Public money committed to minerals: $65B (2025) [src-20260716-6a06e4] (high) | US refining TAM is a gap |
| Machine shops (precision parts) | 17,156 sites, 223,313 workers, $14.23B payroll; 83% have under 20 staff; down from 17,433 in 2022 (2023) [src-20250626-23f6d9] (high). IBISWorld counts 16,619 [src-20260201-adef50] (med) | Counts, not revenue |
| Precision parts (estimate) | About $71B by 2026; machine shops over $60B [src-20251024-2e5383] (med) | One analyst memo; its sources were not traced |
| Fabrication | Structural and architectural metal: 14,533 sites, 423,013 workers, $28.26B payroll; sheet metal 4,652 sites; structural fab 3,434 (2023) [src-20250626-23f6d9] (high) | No free revenue number |
| Materials R&D | None in the repo | Gap |
| Factory software | Robots installed worldwide worth $18.6B (2025) [src-20260924-28b59b] (high) | Robot spend, not software spend |

**The market is fragmented.** Most shops are tiny: 83% of US machine shops had under 20 staff in 2023 [src-20250626-23f6d9]. At the top it is the opposite: defense primes fell from 51 to 5 since the 1990s [src-20220215-45c353].

**What this means [inference].** The pools are large but split among thousands of small shops. That makes room for a new entrant, but no one can say how big the winnable slice is.

---

## 4. The five layers

**How to read this.** We split the category into five layers, from raw metal at the bottom to factory software at the top. Each layer makes money differently. "Gross margin" is the share of revenue left after the direct cost of making the product.

### 4.1 Metals supply (mining, refining, magnets, metal distributors)
- **Who:** Mariana Minerals (copper, lithium; runs its own mines) [src-20260803-30e6d5]. Vulcan Elements (NdFeB, i.e. rare-earth, magnets) [src-20251103-ee9b27]. Nox Metals (automated metal distributor; we passed) [src-20261009-404b9b]. Candidates: Hertha (iron and steel), Cyclic, Mass Magnetics, Duranium. Established players: Reliance, Ryerson, Nucor, MP Materials.
- **How it makes money:** a "service center" buys metal in bulk, cuts it and resells it. Gross margins run about 18-32%: Ryerson 17.7% (Q2 2026) [src-20260729-407fd7]; Reliance 27.9% or 31.6% depending on inventory accounting (LIFO or FIFO) (Q3 2026) [src-20261021-16bb64]. Refining margins: no data.
- **What AI changes:** **Claim (Mariana):** its software halves project timelines that normally take 5-10 years [src-20260803-30e6d5]. Its mine is about 50% autonomous, with AI agents (reinforcement learning, "RL") adjusting the process every 15 minutes [src-20260623-d1790b]. **Claim (Nox):** a price quote in minutes, versus 3-5 days at brokers [src-20250813-5ee11b].
- **Risks:** metal prices swing; permits are slow; buyers are concentrated (Vulcan sells mostly to government) [src-20251103-ee9b27].
- **What this means [inference]:** government support is strongest here (OSC loans, tariffs, IEA finance).

### 4.2 Fabrication (cutting, bending and welding sheet metal; wire harnesses)
- **Who:** SendCutSend [src-20260519-38c7ed]; Senra (wire harnesses, the bundled cables inside machines) [src-20260701-027c1b]; Machina Labs (robots that shape sheet metal) [src-20260204-ce7053]; 1872 (robotic steel fabrication) [src-20260722-985690]. Candidates: Atomic Industries (tool and die) [src-20261023-a3bfe7], Advanced Metal Research.
- **How it makes money:** SendCutSend has been profitable for eight years [src-20260519-38c7ed]. Revenue is about $140M a year per a since-deleted post (low) [src-20260504-c3ded5], or "nine digits" per Sequoia's Reed [src-20261020-487a39] (med).
- **What AI changes:** instant online quotes, and software that packs many customers' parts onto one metal sheet ("nesting"). **Claim (Senra):** quotes in about a day and 99% first-pass yield (FPY: parts that pass inspection the first time) [src-20260701-027c1b].
- **Risks:** works for small batches, not mass production. Machina takes 30 minutes to hours per part; a stamping press takes seconds [src-20261023-c3b62f].
- **What this means [inference]:** the best layer for capital-light owner-operators, but volume is capped.

### 4.3 Precision parts (CNC machining, 3D printing, castings, composites)
CNC means computer-controlled cutting machines. "AM" (additive manufacturing) means industrial 3D printing.
- **Who:** Hadrian [src-20260807-b0dc5b]; Divergent [src-20250915-311606]; Isembard (franchise network) [src-20260909-b547c7]; Freeform (metal 3D printing) [src-20260219-2125d7]; Amca (buys and upgrades old shops) [src-20260520-af3e6c]; Fabri (castings) [src-20260617-4dfb96]; Layup (composites) [src-20260602-a7b79e]; Hybron [src-20260413-abc797]. Established players: Howmet, PCC, ATI, Carpenter, Proto Labs, Xometry.
- **How it makes money:** Proto Labs' gross margin was 44.5% in 2025 [src-20260206-8bb619]: 49% from its own factories versus 31% from its partner network [src-20260206-2b13c7]. Xometry (an online marketplace) earns 34.7% [src-20260224-a7b149]. Howmet's engine unit earns 37.7% before interest, tax and depreciation (EBITDA) [src-20260806-9a83f7]. **Claim (Rolls-Royce engineer):** small shops aim for low double-digit margins [src-20251120-0c271b]. **Claim (ex-Hadrian programming head):** a typical shop can go from 15% to 30% margin in 12-18 months with Hadrian-style operations [src-20261004-9b47f5].
- **What AI changes:** **Claim (Raytheon manager):** Hadrian quoted about 50% lower prices at about a third of the lead time [src-20250708-2aa3ad]. Other buyers disagree (section 8).
- **Risks:** buyers must approve each new supplier. That takes 9-12 months [src-20250708-2aa3ad] or 1-2 years at Northrop [src-20260802-36d46c]. (AS9100 is the aerospace quality standard; NADCAP certifies special steps like heat treating and NDT, non-destructive testing.) The leader is valued at $7.87B, out of SPC's range [inference].
- **Failures in this exact model:** Daedalus, an AI-run CNC factory in Germany with a $21M Series A, went insolvent in August 2026 [src-20260801-4532f6][src-20251203-fc28ea]. VulcanForms replaced its founder CEO [src-20240919-72efcc], then raised $220M [src-20260130-365541]. An ex-Hadrian engineer: a six-machine first factory cost "well north of $10 million", and "manufacturing is not actually a fantastically profitable business" [src-20260817-8867f2].
- **What this means [inference]:** the biggest and most contested layer; the top names are already expensive.

### 4.4 Materials R&D (robot labs that use AI to discover new materials)
- **Who:** Periodic Labs [src-20261022-682e62]; CuspAI (software only) [src-20261022-37a0ea]; Radical AI (runs its own lab) [src-20260617-f9d293]; Lila Sciences (candidate). Nearby: Microsoft Discovery, Citrine.
- **How it makes money:** **Claim (CuspAI primer, AlphaSights):** custom projects earn 5-15% gross margin, a software platform 85-90%; 40-50% of pilots convert to contracts [src-20261016-29997e] (med).
- **What AI changes:** **Claim (Radical):** tests 8-20 alloys a day, aiming for 100; $60-300 per experiment; samples from grams to 500 g; no manufacturing yet [src-20260617-f9d293]. **Claim (Periodic):** at full speed, 4 months of experiments in under 2 weeks [src-20260917-1bcb81].
- **Risks:** none of the three discloses revenue; valuations of $2.6B-$7.5B come before product [inference]. The science has a mixed record. Berkeley's A-Lab claimed 41 new materials; an outside critique said "no new materials were discovered" (challenged, not retracted) [src-20240124-513fd9]. MatterGen handles only about 20 atoms per unit and needs checking by physics simulation (DFT) [src-20261022-3e2a9d]. Lila's catalysts are untested in a real electrolyzer [src-20261019-392916]. An Albert Invent director says chemical majors refuse royalty deals and their problem is "millions of SKUs" (product variants), not crystal structures [src-20260913-3ad55e].
- **Buyer views (expert calls).** A former Moderna director: buyers reach these labs through contract research firms (CROs) and pay per successful candidate. He says CuspAI won 8 of the last 10 campaigns, Radical 1 and Lila 1 (claim). He ranks long-run potential Radical > Lila > CuspAI > Periodic, and says CRO bookings were "very bad" in 2024-25 [src-20260909-af3e60] (low: hard to check). The Albert Invent director (a competitor, so biased): annual contracts run from hundreds of thousands to millions of dollars; procurement "shut[s] down" big prices; budgets open when a product launches in "one-third the number of iterations". He splits $100 as CuspAI $50, Lila $35, Periodic $15 [src-20260913-3ad55e].
- **What this means [inference]:** interesting science, but these are research shops, not producers, and buyers' budgets are small.

### 4.5 Factory software (tools sold to other companies' plants)
MES (manufacturing execution system) is the software that tracks and directs work on a shop floor. It is the established category.
- **Who:** Arda (turns CAD design files into work instructions) [src-20261020-914a64]; Mind Robotics (robot AI models; The Verge corrected "spinoff" to "a partner of Rivian, but not a spinoff") [src-20261013-cc78c0]; candidates Rapta, Allus, Faraday. Established: Siemens, which bought Altair and Dotmatics [src-20250326-cc1810][src-20250701-a7fef9], and Rockwell (gross margin 49.5%) [src-20260804-0e8130].
- **How it makes money:** **Claim (Arda):** priced by usage [src-20261020-a1e174]; no revenue disclosed.
- **What AI changes:** AI agents that write work instructions are the only shipped product (Arda at Anduril) [src-20261020-914a64] [inference].
- **Risks:** Siemens and Rockwell own the customer relationships, and the host plant owns the data [inference]. An investor says the AI is not the limit; the value needs connected plant data and new workflows [src-20261006-6265ad]. Mind has raised over $1B and shown no robot publicly [src-20261013-cc78c0]. Bright Machines, an earlier "software-defined factory", failed to go public via SPAC (a shell-company merger) and pivoted to assembling AI servers [src-20240926-fd90fb].
- **Enablers arm the incumbents.** GrayMatter Robotics tried selling autonomy software, found "that model doesn't really work", and now rents turnkey sanding and painting cells "as a service" [src-20261022-3335bd]. **Claim (GrayMatter):** Riddell went from about 300 to 1,700 helmets a day on the same robots after software updates [src-20261022-3335bd]. If old shops can rent this, automation alone stops being an edge [inference].
- **AI for machine programming and inspection.** CAM is the software that turns a 3D model into machine instructions. CloudNC's CAM Assist writes basic machining plans in minutes inside GibbsCAM, with a human checking each step; CloudNC tests it in its own factory [src-20261021-9769d1][src-20261009-7cafd0]. AI Robotics, a Korean university spinout, inspects welds on 24 production lines in 3 countries, using over 4M data points [src-20261011-a8b14d]. Both sell the same tools to incumbents [inference].
- **What this means [inference]:** this layer sells "picks and shovels". It may help old shops catch up as much as it helps new ones.

---

## 5. Company profiles

**How to read this.** Every company file not marked "not-a-fit". Each profile says what the company makes, how it is funded, who buys, what it claims and the bear case. "Owner-operator" means it runs its own factory and sells parts. "Hybrid" means it also places machines in others' plants. Order is by relevance to an SPC Series B-D check [inference].

### 5.1 Senra Systems (fabrication; owner-operator)
- **What it makes:** wire harnesses and cable assemblies for defense and space, in its own plants (about 95,000 sq ft, two sites) [src-20260701-027c1b].
- **Money:** $65M Series B, July 2026 [src-20260715-68183e].
- **Buyers:** Anduril, L3Harris, Northrop [src-20260128-a16c79]. Growth comes mostly from existing customers and referrals [src-20260701-027c1b].
- **Software:** "Amp", built in-house. It reads parts lists with AI, pulls live supplier prices, estimates labor and writes work instructions [src-20260701-027c1b].
- **Claims (Senra):** 99% FPY [src-20260701-027c1b]. 1,000 harnesses a month, aiming for 10,000 in 2027 [src-20260715-68183e]. Best at runs of 100-1,000 units, quoted in under 2 weeks; about 190 staff heading to 300 by end-2026 [src-20260701-027c1b]. Its CEO says automation is still early [src-20260715-821445]. Harnesses are about 95% outsourced even at SpaceX [src-20260715-821445].
- **Bear:** every number is company-stated. No customer or expert call covers it; only 10 sources mention it. Harness work is manual, so the edge may be paperwork software, not automation [inference].
- **What this means [inference]:** the best-sized owner-operator for SPC, but it needs real diligence.

### 5.2 SendCutSend (fabrication; owner-operator)
- **What it makes:** laser-cut sheet metal, CNC parts and finishing, ordered online with an instant quote. Owns all its plants (Reno; Paris, KY; Arlington, TX) [src-20261020-487a39].
- **Money:** $110M at a $1.01B valuation, May 2026, its first outside round [src-20260519-38c7ed]. Series B at $2.1B led by Spark, October 2026, size undisclosed [src-20261020-487a39] (med, one trade write-up).
- **Scale:** 32,000 orders a month, growing about 100% a year [src-20260525-4a12ab]. About $140M a year in revenue (deleted post) [src-20260504-c3ded5] (low). 650 staff [src-20260904-1929b3] versus 169 per Harmonic.
- **Claims (Jim Belosic, CEO):** 48-hour turnaround [src-20260227-e92d45]. Targets 80-90% machine use [src-20260626-541ac8]. A new plant costs about $50M, funded with equipment loans [src-20260519-2d6ceb]. "I love taking VC dollars and putting it directly in the payroll" [src-20261020-487a39].
- **Customer spread (claims):** the largest customer is 0.59% of revenue; he knows a defense firm with 86% from one buyer [src-20260624-3dc6f7]. Only 15-20% of each month's customers are new, so most orders come from returning, mostly small, buyers [src-20260525-4a12ab]. He says there is "enough demand to at least triple our size", but loans cannot fund it [src-20260624-3dc6f7]. Mostly commercial work, including 60% of the Fortune 500 [src-20261020-487a39].
- **Bear:** customers "outgrow us" and buy their own machines [src-20251002-6a5afd]. Belosic calls lasers and metal commodities: "I don't think it's moat-worthy" [src-20260430-9318cd]. It refuses tight-tolerance work [src-20260525-4a12ab].
- **What this means [inference]:** proof that a software-led factory can be profitable without defense money. Now priced beyond SPC.

### 5.3 Hadrian (precision parts; hybrid)
- **What it makes:** machined parts in automated CNC factories run on its "Opus" software. Now also runs cells inside Lockheed's plant [src-20261014-015327].
- **Money:** Series C $260M (equity plus debt), July 2025 [src-20250721-d99a2a]; about $1.6B valuation in January 2026, then $1.37B Series D at $7.87B in August 2026 [src-20260807-b0dc5b]; a $360M bank credit line [src-20260817-c48f28]. About $2.24B raised in total [Harmonic].
- **Plants:** four sites (California, Arizona, Alabama), about 2.85M sq ft. **Claim (Power):** 24 machines inside Lockheed's Grand Prairie plant plus 24 in Arizona for overflow, live by January 2027 [src-20261015-1a282b]. The Mesa plant cost about $200M for 270,000 sq ft and 350 jobs [src-20250820-cfbf02]. Six factories since 2022, the latest 2.2M sq ft [src-20260921-876080].
- **Share of buyers' spend:** 2-3% at Boeing [src-20260802-ef6506]; under 10% at Northrop [src-20260802-36d46c]. **Claim (Power):** aerospace-grade trust takes years [src-20260908-65fab6].
- **Claims (Power, podcasts):** more demand than capacity; "every quarter there's 2 billion more in pipeline", programs unnamed [src-20260921-876080]. He rejected buying old shops after 12 months of study [src-20260908-65fab6]. He says he was wrong about speed (section 0, point A).
- **What buyers and insiders say (expert calls; med):**
  - *Boeing Defense head of product (customer):* "None of their parts right now are flying ... all in demonstration stage." Today a gap-filler for spot buys of about 100 parts. Scores speed 8, process 9, scale 8 out of 10. "We get very excited when we get a new supplier that gives us a discount of 5%-7%" [src-20260818-9b2d5c]. Also: "we have actually paid probably more" [src-20260818-9b2d5c].
  - *Boeing strategy lead:* brackets and hinges in under a month versus 3-6; a "backup player" and "low-volume shop"; price about equal to PCC or a bit more; automation cuts labor from 100 to 30-50 hours, but machine costs offset it [src-20250712-e5e110].
  - *Northrop unit GM (buyer):* "Cost is secondary." "Machining the part is just 1/3 of the battle." Uses Hadrian for small parts and surge work; rates it 8/10 [src-20250707-3b7a46]. A Northrop director adds that incumbents still have better precision and cost, and Hadrian lags on titanium and Inconel [src-20250707-3b7a46].
  - *Ex-Anduril hardware lead (buyer):* Hadrian "struggled to consistently deliver high-quality, complex parts"; a "narrative play"; Anduril sent most CNC prototypes to Protolabs [src-20250709-43486e].
  - *Defense-startup chief of staff (buyer):* uses Atomic Industries more ("turn production in eight days"); Hadrian claims 8-9 days but is "more manual" [src-20250729-a0a78c].
  - *GE program lead:* Hadrian is "too new, too young"; broker markups are "pretty horrific" [src-20250709-0250ae] (low).
  - *Ex-Hadrian head of engineering:* would be "surprised if any one company could capture 1%" of US defense machining; "only have 10 customers"; CAM software vendors are the main threat; buyers cap a supplier at about a third of its revenue [src-20250708-342eaf].
  - *Ex-Hadrian engineer (holds equity):* the first factory's six machines cost "well north of $10 million"; in years 1-2 Anduril was the only defense buyer [src-20260817-8867f2].
  - *Ex-Xometry VP (peer):* "Hadrian needs 10 factories ... Xometry wants 10,000 customers"; revenue "surprisingly small" for the money invested; deals are slow [src-20260808-dc5cbb].
  - *Documentary narrator:* skeptics think Hadrian is "quite defense industry dependent" and overhyped [src-20260926-70087f].
- **What this means [inference]:** the benchmark for the category. At $7.87B it is a reference point, not a target.

### 5.4 Isembard (precision parts; hybrid franchise)
- **What it makes:** machined parts in owned and franchised factories, all on its "MasonOS" software; US, UK, Germany, France, Ukraine [src-20260310-45bab3].
- **Money:** $9M seed plus $50M Series A led by USV, March 2026; valuation undisclosed [src-20260310-45bab3]. Harmonic estimates about $250M (low).
- **Claims (Isembard):** 40-60% more output and 30% lower operating cost [src-20250929-857f17]. A franchisee goes live in under 90 days. 14 factories, 4 owned and 10 franchised. Now "locking in these long-term contracts ... one year, two year, three years" so machine purchases match contracts [src-20260909-b547c7]. Turning down orders [src-20260810-f0371c].
- **Buyers:** a humanoid-robot company used it for two urgent $2.3-6K orders, delivered in 2 days [src-20260621-f96bbd]. An Airbus supply-chain head sees such networks as prototype suppliers [src-20251106-dfddcb].
- **Bear:** Thales Alenia Space's procurement chief is "skeptical": he must approve and see each production site, which a franchise hides; not a customer [src-20251110-84b67e]. Output and cost claims are company-only. The CEO spends about half his time recruiting; a quality audit (AS9100D) found many issues needing a follow-up [src-20260909-b547c7]. BBC: about 100 staff at the 160,000 sq ft London site [src-20261019-202dd7].
- **What this means [inference]:** a cheaper, capital-light version of Hadrian, if primes accept franchised sites.

### 5.5 Machina Labs (fabrication; hybrid)
- **What it makes:** robots that shape sheet metal without molds ("RoboCraftsman"), plus machining and welding. Runs its own plants and places cells with customers [src-20260204-ce7053].
- **Money:** $124M Series C, February 2026 [src-20260204-ce7053].
- **Buyers:** mostly military repair depots that need old panels whose molds no longer exist [src-20261022-ca4c7a]. About 70% defense; a JASSM missile part in qualification; cleared for defense cybersecurity (CMMC Level 2) [src-20260204-ce7053]. Five Air Force awards worth $7.8M, the largest $3.37M (February 2025), plus $507K to maintain a cell at Robins Air Force Base; the Air Force buys again [src-20250416-317e81]. A Rolls-Royce-side expert says it is for prototypes, "not going to involve in our serial production" [src-20250623-5bc67c] (med).
- **Claims (Ed Mehr, CEO):** up to about 50x faster lead times [src-20261022-ca4c7a]; staff grew from 70 to 240 [src-20260320-1361e2]. A new 200,000 sq ft plant with up to 50 cells making "thousands" of assemblies a year [src-20260204-ce7053]. Gross margin "even if I do poorly ... 50%. But more likely close to 70%", because there are no molds [src-20260430-30ea09].
- **Still in qualification.** **Claim (Mehr, April 2026):** "one of our programs we are now in qualification phase ... about to go to production ... couple of years to get to volume" [src-20260430-30ea09]. With Lockheed, "qualifying and going to production for JASSM fuel tanks" [src-20260822-53d33e]. It started with repair parts that took depots "months, sometimes years" [src-20250402-161b61].
- **Bear:** 30 minutes to hours per part versus seconds for stamping [src-20261023-c3b62f]. Mehr himself: in repeat high-volume work "traditional manufacturing is pretty good", and Machina is "not a good fit" for a million identical parts [src-20260821-1c5a08][src-20251230-2c54a2].
- **What this means [inference]:** real defense demand for repair parts; production at rate is not yet proven.

### 5.6 Freeform (precision parts; owner-operator)
- **What it makes:** metal 3D-printed parts using AI-controlled multi-laser printers. It sells parts, not printers [src-20241024-7f1c2e].
- **Money:** $67M Series B, February 2026; PitchBook puts it at $179M after the round [src-20260219-2125d7] (med); about $126M raised.
- **Claim (Freeform):** a new platform, "Skyfall", "scheduled to go live in the first half of 2026", with 25x capacity and thousands of kg of parts a day [src-20260220-348ad9]. No source confirms it went live.
- **How the loop works:** cameras watch the molten metal pool every microsecond; chips process the images; models adjust the printer live [src-20241024-7f1c2e]. It runs GPU clusters on site [src-20260219-2125d7].
- **Buyers:** hundreds of mission-critical parts a week, customers undisclosed [src-20260219-2125d7]; a fast prototype contract (OTA) from DIU, the Pentagon's tech-buying unit [src-20260901-6e197d].
- **Bear:** metal 3D printing has the worst failure record in this theme (Velo3D, Markforged; section 7). Freeform's claims are company-only and Skyfall is unconfirmed.
- **What this means [inference]:** the clearest live feedback loop in precision parts, and small enough for SPC.

### 5.7 Divergent (precision parts; hybrid)
- **What it makes:** 3D-printed structures plus robotic assembly ("DAPS"). Named defense work: second source for Raytheon's Tomahawk midbody and CoAspire munitions [src-20260601-976843]. A teaming agreement (not a production order) with L3Harris [src-20261013-eda149]. General Atomics work is a 2023 partnership on small drone frames, not missiles [src-20261022-8629b9].
- **Money:** Series E $290M including $40M of debt, September 2025 [src-20250915-311606].
- **Scale:** Long Beach plant, 430,000 sq ft, 1,000 jobs, online by end-2026, sized for 30,000 airframes a year; aerospace and defense about 80% of work [src-20261023-e02543].
- **Claims (Divergent):** revenue up over 5x [src-20250915-262bfd]; about 30 programs with 15 primes [src-20261014-47f64b]; old Tomahawk casting suppliers get under 20% good parts [src-20260113-c08796]. Some programs about 50% cheaper per unit [src-20260523-b05ded] (unverified). "Over 30 production contracts" in 18 months, unnamed and unvalued; repair parts redesigned in 24-48 hours where casting suppliers quit [src-20251015-e9edbf]. Production car frames for Aston Martin and other brands [src-20250309-b9a3c2].
- **Bear:** asked about a Navy 3D-printing center that "haven't been able to achieve" 20-40% savings, Czinger called it "an adoption issue" [src-20260113-c08796]. An Anduril engineer called Divergent "not really a scalable thing" (opinion, March 2025) [src-20250623-5bc67c] (low).
- **What this means [inference]:** a car-to-defense pivot that worked; a benchmark at $2.3B.

### 5.8 Amca (precision parts; buys existing shops)
- **What it does:** bought 8 certified aerospace plants and redesigns parts with its AI platform [src-20260520-af3e6c][src-20261008-149196].
- **Money:** $300M Series B at over $1B (Caffeinated, Lightspeed) [src-20260520-af3e6c].
- **Buyers:** a first Army fixed-price award, value undisclosed. **Claim:** gets redesigned parts approved in under 90 days [src-20261008-149196].
- **What this means [inference]:** the buy-old-shops path Hadrian rejected [src-20261004-9b47f5]. It buys qualification instead of earning it.

### 5.9 Vulcan Elements (metals supply; owner-operator)
- **What it makes:** rare-earth magnets; a 10-ton pilot in Durham and a 10,000-ton plant planned [src-20251103-ee9b27].
- **Money:** $65M Series A (Altimeter) [src-20261010-8e6ec0]. A $1.4B package: $620M loan from the Pentagon's OSC, $50M Commerce Department equity, $550M private [src-20251103-ee9b27]. Form D filing shows $430.7M sold [src-20260402-c8e4dc].
- **Buyers:** 7 federal awards worth $5.7M, including an Army magnet contract (IDIQ: an open-ended order vehicle) [src-20260710-6361ea][src-20250501-1885f8]; magnets for the Army drone program [src-20260923-c53c99]. **Claim (CEO Maslin):** the pilot is sold out 12 months ahead; test data feeds its recipe models [src-20250811-e7cb9a].
- **What this means [inference]:** government-backed, with government as the main buyer.

### 5.10 Mariana Minerals (metals supply; owner-operator)
- **What it does:** builds and runs mines and refineries (Copper One, Lithium One) on its own software [src-20260803-30e6d5].
- **Money:** $310M Series B (Khosla), about $400M including project money; valuation undisclosed [src-20260803-30e6d5]. A $1.5B figure appears only in Harmonic (low).
- **Operations:** about 250 staff, about 20% in software and AI [src-20260623-d1790b]. **Claim:** took over a southeast Utah copper mine and refinery at end-2025 and restarted mining in May 2026, about 50% autonomous, making 99.99% pure copper; "we do not sell software" [src-20260623-d1790b][src-20260513-bdc044]. **Claim (CEO Caldwell):** 30% lower refining cost and 40-50% lower mining cost [src-20260502-21f16a]; 10 projects in 10 years [src-20260513-dd56eb]. No buyer contracts disclosed.
- **What this means [inference]:** one of two names with a credible data loop; the check size is above SPC's.

### 5.11 1872 (fabrication; owner-operator)
- **What it makes:** steel skids, frames and enclosures for energy and utilities, using AI and robots, in Cincinnati [src-20261022-fdbf29].
- **Money:** $15M seed via Ohio's O.H.I.O. Fund [src-20260722-985690].
- **Operations:** 18 staff, about 30,000 sq ft, producing since August 2026 [src-20261016-d61bc1]; welding robots from Path Robotics [src-20260722-3bc2d8].
- **Claims (website, no baseline):** 99% FPY, welding arc on 70% of the time, 85% lower welding cost [src-20261022-fdbf29]. Full autonomy by 2027 [src-20260722-985690].
- **What this means [inference]:** the cheapest way in, but too early to judge.

### 5.12 Nox Metals (metals supply; we passed)
- An automated metal distributor outside Detroit with nesting software [src-20261009-404b9b]. $11.5M seed (Hyperion) [src-20260616-1cf7cb]. About 12 people at one site [src-20260325-5b68db]. Its founder's "controversial belief" is "raw capacity over everything else" [src-20260427-83b102].

### 5.13 Arda (factory software)
- An AI agent reads design files and writes assembly steps and work instructions [src-20261020-914a64]. $72M seed (Accel, Founders Fund), then $160M Series A at $1.5B; $232M total. **Claim (Arda/Anduril):** work instructions from 10 hours to 15 minutes; complex engineering from 30 hours to about 2.5 [src-20261020-914a64].

### 5.14 Mind Robotics (factory software)
- Trains robot AI for factory tasks (picking, fastening, plugging in connectors) and sells robots, not parts [src-20261022-eede0b]. Rivian is partner, first customer and shareholder: "a partner of Rivian, but not a spinoff" [src-20261013-cc78c0]. It depends heavily on Rivian and has raised over $1B, with no public product [src-20260515-176e26].

### 5.15-5.18 Research labs and adjacent names
- **Periodic Labs:** $300M seed, September 2025 [src-20251022-8eb7c0]; reportedly raising much more (med) [src-20260514-5796ab]. Offers custom AI agents to clients' engineers; one unnamed chip client [src-20261022-682e62]. No revenue disclosed.
- **CuspAI:** $450M Series B (Kleiner, NEA) [src-20260720-840ae3]. About 30 industry and 15 lab partners, including Samsung, AMD, Lam and Applied [src-20261022-37a0ea].
- **Radical AI:** $55M led by RTX Ventures, a prime's venture arm [src-20250718-d46f24]; a $1.2M Air Force award [src-20250523-f41dd1].
- **Terrafirma:** $100M Series A, self-driving earthmoving equipment, Austin [src-20260714-976329]; about $500M valuation per Harmonic (low). Adjacent to the thesis.

### 5.19 Other candidates (one line each)
Fabri: automated casting, $13.5M from RTX and Lockheed venture arms, shipping castings [src-20260617-4dfb96]. Layup: composite parts, $42M Series A [src-20260602-a7b79e]. Hybron: composite shells, $25M seed, contract floor over $100M [src-20260413-abc797]. Atomic Industries: AI tool and die, $25M Series A [src-20261023-a3bfe7]. Rangeview: castings from printed molds, $4.2M seed [src-20260923-3ab808]. Furientis: low-cost interceptor missiles, $25M seed (Benchmark) and a Pentagon OTA [src-20261006-410f77]. Firestorm: drones; moved from small research grants (SBIR) to a repeat-order contract, 19 awards worth $53.8M [src-20251022-629fc0][src-20251219-bd5788]. Re:Build: engineering and manufacturing roll-up, 12 sites [src-20261006-1212f9]. VulcanForms: metal 3D printing plus machining; CEO change, then re-raise [src-20240919-72efcc]. Incumbents are in section 7.

**What this means [inference].** Most profiles rest on company claims. Buyer calls exist mainly for Hadrian, and they are mixed.

---

### 5.20 More company specifics from all sources
- **Hadrian.** Revenue was $3M in 2023 with a $30M+ target for 2024 (Forbes) [src-20240815-500933]. **Claim (Power, 2025):** "basically 10xed revenue in four quarters"; target about $1B by 2027; "manufacturers in the US are horrifically low margin" [src-20250718-ac643a]. **Claim (Power):** close to 100% of workers "never set foot inside a factory", trained in 30 days; "a 25-year-old kid ... running 14 robots" [src-20260610-779f8b]. At Lockheed's plant, "Lockheed Martin employees will operate Hadrian's production cells" (Axios) [src-20261020-09eec1]. The Army's Red River Depot contract runs to March 2027 [src-20260318-472c29]. Hadrian says it does not discuss customers due to "very strict NDAs" [src-20250718-ac643a], which limits checking. All of Hadrian's debt is still corporate; a dedicated plant with a creditworthy buyer would be the first project-finance case [src-20261012-b7af6d].
- **SendCutSend.** More than 300,000 customers and 30M parts shipped, with 1-3 day delivery [src-20261020-9deafa]. Belosic added 450 people in 2026 and is finalizing a first acquisition [src-20261020-1d0bbb]. Named customers include Zipline, Waymo, Anduril, Castelion and Relativity [src-20261020-c541ad]. Ad spend fell from $120-170K a month to about $4K, as word of mouth took over [src-20260525-4a12ab]. Bear: "the software is the easy part ... the hard part is everything outside the software".
- **Senra.** **Claims (CEO Jordan Black):** a harness "can be 25% of the cost of your vehicle"; "800 plus mom-and-pop shops" are going away; the only Department of Labor-certified harness training, 4 weeks versus 2 years; technicians average 48-55 years old; the factory is "only 25% built up"; it "didn't have a sales team until 4 months ago" [src-20260715-821445]. He admits "the dexterity and the models might not be at the caliber we need today" [src-20260715-821445]. A BMW expert agrees harness routing is "beyond the edge" for robots today [src-20261014-ce5195]. Lockheed consolidated cable harnesses from five factories to one, a sign of the bottleneck [src-20261014-47f64b].
- **Divergent.** **Claim (Czinger):** the first factory exits "about three airframes per day"; it "haven't cracked it yet" on exquisite munitions [src-20261014-47f64b]. Printer output rose from 50 grams to 1-2 kg an hour; structures priced "at or below casting"; 500+ products on the same machines [src-20260325-7ba845]. "We never compete as a prime" [src-20261002-b0cee5].
- **Machina.** Its largest client in 2023 was the Air Force; Mehr was "not sure how to compare our pricing" to sheet-metal shops [src-20261023-af2e72]. It won't start a project "unless the customer is actually committed with some dollars" [src-20260622-7846f9]. Its Form D shows $38.94M sold of $52.61M [src-20260225-5e3f18] (a filing, possibly one tranche).
- **Mariana.** The prior operator shut the Utah mine in 2024 partly for lack of haul-truck drivers; autonomy is bought in from Sandvik and Pronto [src-20260502-21f16a]. Target: 50,000 t of copper a year by 2030 versus about 2,500 t under the prior operator [src-20261011-e2426c]. Headcount rises from the prior peak of ~130 to ~300 despite autonomy, due to more output (**Claim**) [src-20260813-1fe8a2].
- **Vulcan.** Its Benson, NC plant (1.1M sq ft, 10,000 t a year, ~1,000 jobs) is under construction [src-20261020-ca1a28]. Rare-earth oxide feed from Ucore is planned from 2027, so upstream supply is also pre-commercial [src-20260324-61ffc3]. The US set a $110/kg rare-earth price floor for MP and Lynas, a policy demand guarantee [src-20261022-161490].
- **Isembard and Amca.** Isembard hired a commercial chief from McDonald's/KFC to run its "manufacturing franchise network" [src-20261006-5a64c1]; it has more software engineers than machinists and says 95% of CNC machines are owned by small businesses whose owners are retiring [src-20250619-46e43c]. Amca bought Electrocube, a top-20 Boeing supplier [src-20260212-c61f30], and won an Army Materiel Command contract for engineering, qualification and production (**Claim**) [src-20261008-9941fd].
- **Arda, Mind and Nox.** **Claim (Arda):** a 2,000-part missile avionics box was planned in two days; Arda is "now used across all of [Anduril's] product divisions"; its investor says "the price is steep today" [src-20261020-878aa9]. Mind uses Rivian as "a live, high-volume manufacturing environment for model training"; Rivian owns 32.1% [src-20261013-58de15]. Nox: 46 people, 250-300 customers, 75,000 sq ft (**Claim**) [src-20261009-404b9b]; instant quoting is easy with a 50% buffer, the hard part is beating a human estimator [src-20261022-3135b5].
- **New entrants worth knowing.** Helicon (composite drone frames, $16.5M): cycles of 5-15 minutes versus hours; "less than ten customers" (**Claim**) [src-20261020-c4b077]. Westmag (drone motors, a16z seed): China makes "over 30 million more drone motors and robot actuators per year than the U.S." [src-20260602-66bb0d]. Firestorm's containerized printers made "1,000 parts on the USS Essex" during RIMPAC (**Claim**) [src-20261019-34ca73]. CircuitHub (circuit boards) says it is profitable and that "90% of high-mix US EMS Assembly COGS is labor" (**Claim**) [src-20260520-09ca24]. Jeevy sends about 90% of volume to partner shops and keeps 10% in-house; SpaceX is a top customer [src-20261014-40926d]. Anduril is building a $3.7B shipyard in Maryland [src-20261017-5be775], so it is both a buyer and a competitor.
- **Failures and warnings, again.** NGP said Daedalus was doubling or tripling revenue months before its insolvency [src-20251203-fc28ea]. A drone founder: "3D printing is most definitely way high on the hype curve and very low on the efficacy curve" [src-20261022-f423ef]. Castelion: dependence on government revenue "is extremely damaging" [src-20251010-d50ea5]. Bright Machines' Lior Susan: contract manufacturing has "extremely low gross margin" [src-20240508-097e37].

## 6. Data loop scorecard

**The idea.** A "data loop" means every part a factory makes teaches its software to make the next part cheaper or better. If true, the leader pulls further ahead over time. This is the core of the "AI-native" pitch.

**Scale:** 0 = asserted only; 1 = mechanism described; 2 = partial evidence; 3 = measured improvement over time. **Nobody scores 3.**

| Company | Score | How the loop works | Best evidence / what is missing |
|---|---|---|---|
| Freeform | 2 | Cameras on the molten metal adjust each printed layer live | [src-20241024-7f1c2e][src-20260219-2125d7]. Missing: yield or cost trend |
| Mariana | 2 | AI agents retune the refinery every 15 minutes | [src-20260623-d1790b]. Missing: recovery or cost per ton |
| Hadrian | 2 | Opus software for workflow, programming and quality checks | 30-40 day training [src-20260926-70087f]; 25-75% shorter cycle times at a studied shop and a 50% cut in order-to-first-part time in about two years [src-20261004-9b47f5]. Missing: it relies on outside CAM software [src-20261004-9b47f5] |
| Radical AI | 2 | Robot lab tests and learns in a closed loop | 8-20 alloys a day [src-20260617-f9d293]. Missing: hit-rate trend |
| Divergent | 2 | Design software feeds printer, then assembly | 600+ part numbers [src-20250915-311606]. Missing: cost-per-part trend |
| Senra | 1 | Amp standardizes inputs, guides technicians, tracks materials and design changes [src-20260715-68183e] | 99% FPY claim [src-20260701-027c1b]. Missing: before and after |
| SendCutSend | 1 | Instant quoting at volume | 32,000 orders a month [src-20260525-4a12ab]. Missing: any learning metric |
| Isembard | 1 | MasonOS quoting across franchises | Claim: 40-60% more output [src-20250929-857f17]. Missing: outside proof |
| Machina | 1 | Robot forming learns each new shape | Claim: 50x lead time [src-20261022-ca4c7a]. Missing: cycle-time trend |
| Vulcan | 1 | Test data feeds recipe models | [src-20250811-e7cb9a]. Missing: any number |
| Nox | 1 | Auto-nesting and quote-time estimates | [src-20260325-5b68db]. Missing: scrap rate |
| Arda | 1 | Agent improves with host's design data | [src-20261020-914a64]. Missing: who owns the data |
| Periodic, CuspAI, Mind | 1 | Lab or factory as a training ground for AI | [src-20260917-1bcb81][src-20261022-37a0ea][src-20260513-83aa83]. Missing: production evidence |
| 1872 | 0 | The welding AI belongs to Path, not 1872 | [src-20260722-3bc2d8]. Missing: everything |

**What this means [inference].** The loop is real where the process is continuous and physical (molten metal, ore, alloys). It is weakest where a shop makes separate parts to a customer's drawing.

---

### 6.1 More on data loops: what the sources say for and against
- **For: the data does not exist unless you make it.** Periodic's founder: published values for one material property "spanned many orders of magnitude", and negative results are unpublished, so own-lab data is needed [src-20260403-ba156a][src-20260106-62dba1]. Meta's open release of 100M+ physics simulations shows simulation data is becoming free, but the same paper says errors remain and "more than just model scaling will be required", which favors real experimental data [src-20250513-fbb4d8]. **Claim (Power):** manufacturing data is "never on the internet"; a blueprint is not enough without machining and inspection data [src-20260908-65fab6].
- **For: concrete loop mechanisms.** **Claim (SendCutSend):** "after millions and millions of parts ... we feed it back into our app ... the more jobs that we take in, the smarter we get", for example warning designers about bends; nearly half a million drawings are uploaded a month [src-20260626-541ac8][src-20260624-3dc6f7]. **Claim (Machina):** 150+ sensor channels are recorded every 4 milliseconds [src-20250402-161b61]; a SpaceX part took 25 trials early and now 4-5 on average [src-20260926-70087f]. **Claim (GrayMatter):** 3.6M hours of production runtime recorded [src-20261022-3335bd].
- **Against: the data is siloed and the loop is slow.** Plant data sits in separate layers (machine controllers, MES, ERP), which limits AI (Construct) [src-20250409-8f07e3]. An IMTS observer: "models are largely good enough"; the bottleneck is plant data and adoption [src-20260922-94fcb0]. Physical AI data is "expensive, slow, hard to scale" [src-20260909-524e7c]. Some of Periodic's workflows are "still like 90% human" [src-20261008-83dc1b]. Argonne's academic robot lab publishes its data openly, which weakens the "proprietary data" argument [src-20250217-059784] [inference].
- **Against: trust breaks easily.** AI Robotics' CEO says a pilot fails if "one false detection" makes operators switch the inspector off [src-20261011-5db652]. A VC newsletter warns autonomous plants "keep producing confidently" when wrong, while aerospace change-control rules assume a fixed process [src-20261015-0e1593].
- **Incumbents are using AI too.** **Claim (Foxconn, NVIDIA event):** 80% faster root-cause analysis, +15% labor productivity, -10% machine failures, +3% first-pass yield [src-20261022-89d710]. **Claim (PepsiCo):** AI digital twins raised a Gatorade plant's throughput 20% in 3 months [src-20261015-0e1593].
- **What this means [inference].** Running the plant does create data others lack, but nobody yet shows cost falling with volume, and incumbents can buy similar tools.

## 7. Competition and incumbents

**How to read this.** "Incumbents" are the established, mostly public, companies. Their margins are the bar a startup must beat.

**What incumbents earn** (gross margin unless noted):
- Proto Labs (fast-turn parts): $533.1M revenue in 2025, 44.5% margin [src-20260206-8bb619]; uses AI for pricing [src-20260731-ef3d40].
- Xometry (online marketplace): 34.7% on the marketplace, 39.1% overall, with a $61.7M net loss [src-20260224-a7b149]; partnered with Siemens [src-20260804-7625ed].
- Metal distributors: Reliance 27.9% or 31.6% (Q3 2026) [src-20261021-16bb64]; Ryerson 17.7% (Q2 2026) [src-20260729-407fd7].
- Nucor (steel): 20% versus 14% a year earlier, including a one-off $130M refund worth about 1.3 points [src-20260812-77d6f5].
- Howmet (engine and aerospace parts): $2.55B quarterly revenue; engine unit EBITDA margin 37.7% [src-20260806-9a83f7]; uses AI process control [src-20260301-357ec4].
- Carpenter (specialty alloys): 32.1%, or 40.4% excluding metal surcharges [src-20261022-d47483]. Rockwell (automation): 49.5% [src-20260804-0e8130].

**What expert calls add (claims, med).**
- PCC (Precision Castparts, a Berkshire-owned supplier) wants accounts of $50M+. Its share of Boeing machining fell from 50% to 30% in 10 years; its parts cost 5-7% more; it is also automating [src-20250712-e5e110]. After a PCC factory fire hit every order from that plant, Boeing will not concentrate supply again [src-20260818-9b2d5c].
- How much Boeing makes itself is disputed: about 40% of parts, with flight-critical work kept in-house [src-20250712-e5e110], versus only 20-30% of the 1.2M parts per airplane [src-20260818-9b2d5c]. One may count spend and the other part count.
- Boeing uses more than 10 machining shops and wants 2-3; old suppliers have "extremely high inertia" [src-20260818-9b2d5c].
- Xometry grew after shedding its own machines; Protolabs was held back by its factories; the market stays fragmented for 5 years [src-20260808-dc5cbb].

**Incumbents partner rather than build.** Lockheed hosts Hadrian [src-20261014-015327], and its venture arm runs a $1B fund [src-20260401-073d24]. RTX Ventures led Radical [src-20250718-d46f24] and backs Fabri [src-20260617-4dfb96]. Siemens bought Altair and Dotmatics [src-20250326-cc1810][src-20250701-a7fef9]. Lindsay Goldberg is buying up Alro (metal distribution) [src-20260811-27702f].

**Failures to learn from.**
- Markforged (3D printers): valued at $2.1B in 2021, sold to Stratasys for $42.5M in 2026. Velo3D's shareholders were wiped out but the business recovered (Q1 2026 revenue $13.8M, up 48%). Survivors used several processes, not 3D printing alone [src-20261023-63156a].
- Velo3D refocused on defense after a lender standstill and rescue [src-20261023-9f720f]; its Q1 2026 gross margin was 17.2% versus -73.6% [src-20261023-63156a].
- Bright Machines (failure example only): its $1.6B SPAC deal fell through; it closed Israeli R&D with about 60 layoffs in 2024; it sold only $71.5M of a $145.5M 2022 round [src-20240527-6a4884].
- Daedalus: AI-run CNC factory in Germany, $21M Series A in February 2024, insolvent August 2026 [src-20260801-4532f6]. The closest failed copy of the owner-operator thesis.
- VulcanForms: founder CEO replaced, then raised $220M in January 2026 [src-20240919-72efcc][src-20260130-365541]. A pivot, not a failure.

**What this means [inference].** The real threat is not Xometry's software. It is approved suppliers like PCC automating while keeping their approvals, and primes keeping critical work in-house. Survivors found a repeat defense buyer before spending heavily; sellers of equipment did not compound.

---

### 7.1 The right to win: versus job shops, contract manufacturers and overseas
**The question.** Why would a buyer use a new AI-native producer instead of a local job shop, a contract manufacturer (CM, a firm that builds to someone else's design), or a cheaper overseas supplier?

**Arguments for the new producers.**
- **Old shops are slow to quote and run like consultancies.** **Claim (Power):** legacy shops "operate like consulting businesses", reselling $60-an-hour labor at $120 [src-20250509-22b78a]. **Claim (SendCutSend):** job shops need months-long runs to "make their margin back" [src-20260624-3dc6f7]. **Claim (Nox):** a competitor's quote took about 8 hours per email round versus 10 seconds [src-20261022-3135b5].
- **Buyers like one roof and good paperwork.** The ex-customer FlyX CEO came back to Hadrian for "everything under one roof" and because it is "one of the few that give you the proper documentation"; Xometry's marketplace was a "big headache" [src-20260806-3a2ec7]. A Raytheon engineer values that Hadrian is 30-45 minutes away, takes 3D model files directly rather than drawings, and showed lower part-to-part variation "than compared to our traditional suppliers" [src-20260823-b3713f].
- **Responsiveness.** An Anduril engineer praises a dedicated project manager and 24-hour responses versus mom-and-pop "radio silence"; in-machine probing cut one lead time by about 40% (7 days to 2-3) [src-20250623-5bc67c].
- **Greenfield beats retrofit.** **Claim (Power):** after 12 months studying legacy certified shops, they were maybe 30% more efficient after upgrades, so Hadrian built new [src-20260908-65fab6]. "You can't automate unless you standardize the hardware": 40 different machines explode the software work [src-20240622-b8cd8b]. A BMW strategy manager says a new robot-first plant could need 20-40% fewer people, while old plants with spare labor "none of them is really thinking about greenfield" [src-20261014-ce5195][src-20261021-25a598].
- **Overseas loses on protected and urgent work.** Defense rules and ITAR keep work onshore (section 2.4). **Claim (Isembard):** a new local factory cut lead time from about 10 weeks to under 14 days and "can match on price" for one warehouse customer [src-20260310-cdfd82]. **Claim (VulcanForms CEO):** "we're winning business back from overseas" [src-20261005-f3f30a].

**Arguments against (equal weight).**
- **Machining is crowded and easy to enter.** A Rolls-Royce engineer: there is "no shortage" of machine shops; it is the easiest entry path [src-20251120-0c271b]. Legacy shops still win big defense work: Bender CCP holds a $40M part of a $944M Navy repair program, paying machinists $35-45 an hour [src-20261018-2b4a22].
- **Incumbents automate too.** Northrop's new Virginia plant claims about 20% lower recurring cost [src-20261022-1389b7]; L3Harris says AI improves yields at its rocket-motor plant, with deliveries up 60% [src-20261022-869770]; GE invested $600M in three years once demand was certain [src-20261014-47f64b]. FlyX's CEO thinks an incumbent could build this automation "organically" [src-20260806-3a2ec7].
- **Buyers design for many vendors.** The Anduril engineer wants "a dumb way of making parts" so "four or five different vendors can make the parts", because "I don't know how long you will be in business"; he will not switch for "5%-10% cash back" and avoids vendors near 100% capacity [src-20250623-5bc67c].
- **Speed alone is "AI-washing" risk.** Freeform's CEO: legacy processes "haven't really fundamentally changed ... We can slap iPads on things and epoxy floors"; "ask them exactly how" they use AI [src-20261020-bac9ca]. Interested party, but a sharp test.
- **China still wins on cost in open markets.** **Claim (Power):** US aerospace parts cost "two to three times" China's, and prototypes "eight to 10 times" [src-20250509-22b78a]. A DoD study: China can deliver a finished forging "for the same cost that a U.S. forge will pay for the raw materials" [src-20220801-c32e19].

**What this means [inference].** New producers win on responsiveness, documentation and greenfield design, in markets protected from China. They do not win on price alone, and incumbents are closing the automation gap.

## 8. Customers and demand

**The short version.** Buyers pay extra for speed on urgent and prototype parts. Proof of repeat, high-volume orders is thin.

**Who buys.** Primes (Lockheed, RTX, Northrop, Boeing, L3Harris, General Atomics); new primes (Anduril); military depots and programs (Army, Navy, DIU); and commercial hardware firms (SendCutSend serves 60% of the Fortune 500) [src-20261020-487a39].

**What buyers told expert calls (AlphaSense-arranged; med).** Grouped by theme.

*On price.*
- Raytheon senior manager: Hadrian quoted about 50% lower, at about a third of the lead time, but no parts had been delivered, and the introduction came via RTX Ventures. Best fit is $300-700 parts, not castings. Suppliers run at 80-90% capacity [src-20250708-2aa3ad].
- Boeing head of product: a 20-25% price gap would make Boeing switch; Hadrian is 2-3x faster and holds 2-3% of precision spend, on prototypes and non-critical parts [src-20260802-ef6506].
- Boeing executive director: at 1,000 parts a traditional shop is cheaper; with full inspection, time is equal; losing Hadrian would barely matter [src-20260908-ed94f0].
- Boeing CTO-org manager: Boeing has paid more so far; a 5-7% discount is exciting; 30-50% would move volume; no certified flying aircraft uses Hadrian parts [src-20260818-9b2d5c].
- Northrop director: incumbents keep a cost edge and will start a price war; lead time is the pain; rates Hadrian 8/10 [src-20250707-3b7a46].
- Ex-Anduril hardware lead: defense buyers do not care much about price; no production volume given [src-20250709-43486e].

*On paying for speed.*
- Northrop process engineer: would pay 20-40% more to avoid a program delay. Hadrian has under 10% of outsourced work, maybe 10-20%, CNC only; replacing it would take months to a year [src-20260802-36d46c].
- FlyX CEO, a former customer: left over cost. A premium of "10%-15% is tops"; 30-40% is "not justifiable". Hadrian is "two times" faster with rework "one in thousands", but aerospace-grade quality is "overkill" for drones. Once qualified, aerospace customers "cannot afford to switch" [src-20260806-3a2ec7].
- Defense-startup chief of staff: Atomic takes 8 days, Hadrian 8-9; big buyers move work in-house after a "honeymoon period" [src-20250729-a0a78c].

*On scale and switching.*
- Raytheon senior mechanical engineer: buys weekly, but spend is "currently in the tens of thousands" during a trial period; "multiple millions" possible later [src-20260823-b3713f].
- Thales Alenia procurement chief: capacity is the pain, and chrome-VI coatings are banned from end-2024. He does not approve second-tier network sites and uses only suppliers with $30-40M revenue; networks fit smaller defense, auto and energy work first [src-20251110-84b67e].
- Ex-Xometry VP: 50-60% of parts arrive with no 3D model; the CEO is in every deal, so sales are feast or famine [src-20260808-dc5cbb].

**The contradiction.** Raytheon says Hadrian is *cheaper*; Boeing says it is *dearer at volume*. Both can be true if Hadrian prices low on small, urgent jobs [inference].

**Qualification: a tax at entry, a moat once paid.** Getting approved takes 9-12 months at Raytheon [src-20250708-2aa3ad] and 1-2 years at Northrop [src-20260802-36d46c]. **Claim (Power):** full aerospace trust takes 7-8 years [src-20260908-65fab6]. Airbus is cutting to fewer suppliers and sees networks as prototype shops [src-20251106-dfddcb]. A Raytheon engineer says new suppliers' quality now beats legacy [src-20260823-b3713f]. Amca buys qualification by acquiring shops [src-20260520-af3e6c] [inference].

**Repeat orders in federal data.** Firestorm is the only producer that climbed the full ladder: small research grants (SBIR), then a Phase III open-ended contract (IDIQ), then repeat task orders: 19 awards, $53.8M [src-20251022-629fc0][src-20251219-bd5788]. Hadrian's Army award was $39.2M obligated of $80M, with one bid [src-20260317-5585be]. The federal record ($79.4M) calls it "DATA RIGHTS AND INTELLECTUAL PROPERTY" [src-20260317-77e798], so it is not plainly a repeat parts order. Raytheon spend is "tens of thousands" so far [src-20260823-b3713f]. Shipbuilder HII pays Path Robotics and GrayMatter per unit of output [src-20260101-164f12]; they are vendors, not producers. Mariana, Arda, 1872 and Nox: no prime awards found.

**What this means [inference].** Paid demand today is speed on prototypes and early low-rate production (LRIP). Rate production at scale is not yet proven.

---

### 8.1 How buyers qualify suppliers and reorder, step by step
- **The ladder.** An Anduril engineer describes it: first "a PO for six months ... If they can do it well, giving another PO for two years" [src-20250623-5bc67c]. Prototypes are bought on lead time, "not price at all"; production is bought on price [src-20250623-5bc67c]. Each change of design, material, source, process or location, or a 2-year gap, means repeating the first-article inspection (FAI) [src-20190801-e81d7b].
- **Repeat orders are real but small so far.** A Raytheon engineer: Hadrian is approved "for all of our different products" and delivers weekly, "meeting our quota", but spend is "in the tens of thousands ... on purpose" during a probation; "tens of millions" are possible if classified testing is solved. Testing, not machining, is his biggest bottleneck; mechanical parts get output only "1/3 of the way there" [src-20260823-b3713f].
- **Buyers cap each supplier.** The Anduril engineer keeps a vendor at about 25-30% of its business and wants about 25% spare capacity; SpaceX went from 17 flights in 2020 to 140 in 2024, so vendors had to scale 20x [src-20250623-5bc67c].
- **Churn happens when the work changes.** FlyX left Hadrian because "the cost was going up and also the nature of the projects changed": most drone work is "less stringent", so aerospace-grade suppliers are "like you have a Porsche and you are going 20 mi an hour" [src-20260806-3a2ec7]. At 5% cheaper he would pick Hadrian [src-20260806-3a2ec7].
- **What primes say in public.** On an Air Force panel, a prime voice called funding "the elephant in the room"; Lockheed said the government does not "want to buy factories. We want to buy weapons"; one-year max-rate runs lose workers, multiyear deals keep them. Primes want authority to qualify second and third sources [src-20261014-47f64b]. Divergent's CEO said spare parts work has high part counts and small contracts, and certification cost "will actually ruin the business case" [src-20261014-47f64b].
- **The "field of dreams" problem.** A merchant banker on a defense panel: the Pentagon "cannot actually sign a contract until they have that physical facility built", but with a contract "financing that facility is a no-brainer" [src-20260325-7ba845]. A Pentagon memo gave contractors 21 days to submit faster munitions plans with "skin in the game" capex (**Claim, Critical Materials Group**) [src-20260902-841664].
- **New primes pull work down the chain.** Anduril says "Hadrian had been involved in design from day one" on a boat program (Contrary, an Anduril investor) [src-20260501-4e5b9a]. Anduril's COO says of Arda, "We would be behind on our production goals without it" [src-20261020-722aff].
- **Base rates for research-to-production.** Only about 5% of companies graduate from SBIR Phase II to Phase III (production) [src-20240129-b46554]; a CRS study found 49% of 269 Phase II awards generated product revenue [src-20200505-dd1158]. Castelion calls the roughly 3-year gap from research money to a program of record the "valley of death" [src-20251010-d50ea5].
- **Other buyer data points.** Ursa Major won $137M in two Navy contracts, but to develop and qualify, not full-rate production [src-20261014-08000a]. Divergent's three FY25 Air Force awards totaled about $3.64M, all development-scale [src-20250924-22c5ee]. GM Defense delivered PAC-3 parts 22 days after contract [src-20261019-409403].
- **What this means [inference].** Reorders come in a ladder: probation, small repeat POs, then multi-year deals. Most new producers are still on the lower rungs.

## 9. Capital and financing

**How it works.** Venture equity is the most expensive money because investors want large returns. Loans are cheaper but need assets or contracts behind them. So equity usually pays for the first plant, and loans and government money pay for the rest.

**Who funded what.**
- **Hadrian:** about $2.24B of equity [Harmonic]; $1.37B Series D at $7.87B, August 2026 [src-20260807-b0dc5b]; a $360M bank credit line [src-20260817-c48f28]; $900M from the Navy [src-20260320-67ba4c]. A plant costs about $200M for 270,000 sq ft [src-20250820-cfbf02]. **Claim (Power):** about $1B must be spent ahead of contracts, and "equity never funds factory construction" [src-20260921-876080].
- **Divergent:** $230M Series D (Hexagon) [src-20231115-5d0589]; $290M Series E at $2.3B including $40M of debt [src-20250915-311606]; Long Beach plant 400-430,000 sq ft, cost undisclosed [src-20261023-e02543].
- **Isembard:** $59M; undisclosed debt for owned plants; franchisees pay for their own [src-20260310-45bab3][src-20250929-857f17].
- **SendCutSend:** $116M plus the October round at $2.1B [src-20261020-487a39]. Funded by equipment loans: about $50M per new plant [src-20260519-2d6ceb], and its first $750K laser was financed [src-20260227-e92d45].
- **Vulcan:** $65M Series A plus $50M of Commerce equity; a $620M OSC loan and $550M private; a 10,000-ton plant [src-20251103-ee9b27][src-20261010-8e6ec0].
- **Mariana:** about $400M including project money; project finance funds the sites [src-20260803-30e6d5].

**Bear.** Lowercarbon says hardware companies at Series B often have about $10M revenue and only break-even gross margins [src-20251211-87dc10]. A six-machine first plant cost over $10M [src-20260817-8867f2]. ABL (asset-based lending, loans against receivables and inventory) is not evidenced for any tracked startup (gap).

**What this means [inference].** Equity pays for software, team and plant #1; banks, OSC and project finance pay for plants #2 and on. A company without contracts is stuck funding plants with expensive equity.

---

## 9A. Unit economics by layer

**The idea.** Unit economics means how much a company earns or loses on each part or ton, after direct costs. No startup discloses margins in the repo, so below are incumbent benchmarks and the cost drivers experts named. "(claim)" means one speaker.

- **Metals supply.** Distributors earn 17.7% (Ryerson) to 31.6% (Reliance) [src-20260729-407fd7][src-20261021-16bb64]; Nucor earned 12% in 2025 [src-20260225-3ea941]. Vulcan's 10,000-ton plant rests on a $1.4B package [src-20251103-ee9b27]. Metal costs pass through to buyers, and tariffs raise the value of stock on hand [src-20260728-ae7dea]. Margin moves with quote speed, reuse of offcuts and, above all, the price cycle [inference].
- **Fabrication.** SendCutSend is profitable, margin undisclosed [src-20260519-38c7ed]. About $50M per plant, debt-funded [src-20260519-2d6ceb][src-20260227-e92d45]. Material can be 85% of a part's price (claim) [src-20260611-7b80f0]. Margin moves with machine use, target 80-90% [src-20260626-541ac8].
- **Precision parts.** Proto Labs 44.5%: 49% own factories versus 31% network [src-20260206-8bb619][src-20260206-2b13c7]; job shops 15-25% (thesis.md). A six-machine first plant cost over $10M; top German 5-axis machines cost about $1M each versus $200K for a Doosan (claim) [src-20260817-8867f2]; Mesa about $200M [src-20250820-cfbf02]. Automation cuts labor from 100 to 30-50 hours per part, but after machine costs the net saving is 20-30% at best (claim) [src-20250712-e5e110]. One-time engineering per part (NRE) is $1-5K; casting tooling tens to hundreds of thousands [src-20260611-7b80f0]. CAM programmers earn $130-150K [src-20260817-8867f2]. Machining is only a third of the job; inspection, paperwork and certificates are the rest [src-20250707-3b7a46][src-20260611-7b80f0].
- **Materials R&D.** Custom projects 5-15% margin, platforms 85-90% (claim) [src-20261016-29997e]. A robot lab costs about $20M to build. Buyers pay about $150K per software test, $500K per pilot, $2M per proven candidate and $10-15M a year per lab line (claim) [src-20260909-af3e60]. Contracts run "hundreds of thousands to millions" [src-20260913-3ad55e]. Hit rate and repeat work drive margin; royalties are rejected [inference].
- **Factory software.** Rockwell earns 49.5% [src-20260804-0e8130]. Arda prices by usage [src-20261020-a1e174]. AI Robotics grew revenue about 18x and is profitable without outside money; its key metric is false alarms on live lines [src-20261011-a8b14d].

Power is a minor cost: one plant used 500-600 amps of a 1,200-amp service for 6-8 machines; about 30 CNCs run on 2,000 amps (claim) [src-20260817-8867f2].

**What this means [inference].** Owning the factory gives better margins than brokering (49% versus 31% at Proto Labs). But machines are costly, and machining is only a third of the work.

---

### 9A.1 More unit-economics inputs, in plain words
- **How a job shop prices.** A vendor guide (low confidence) puts 3-axis CNC time at $35-75 an hour and 5-axis at $75-150; shops aim for 75-85% machine use; markups run 25-40% on prototypes and 15-25% on production; one case shop netted 4-5% [src-20261023-58b5a8]. Inspection adds $50-150 a part and material markups run 18-35% [src-20261023-6ef991] (low).
- **Margins along the chain.** **Claim (Mehr):** supply-chain shops run 10-15% margins [src-20250427-5bd04d]. Primes earn about 7-12% on cost-plus contracts [src-20260501-4e5b9a]. A Rolls-Royce engineer: simple parts go "as low as 7%, 8%", complex low-volume parts need double digits; his former $50-60M-a-year Tier-1 had 450-500 staff [src-20251120-0c271b]. Anduril's gross margin is 36-38% with a $1.2B operating loss (Contrary, an investor) [src-20260501-4e5b9a]. Protolabs earned 46.4% gross and 12.0% operating margin (non-GAAP) in Q2 2026 [src-20260731-4f4aac]. Howmet's capex is about 5% of sales [src-20260630-bd78e7].
- **What drives a qualified shop's cost.** The FlyX CEO: AS9100 costs "hundred thousand, millions of dollars to maintain"; aerospace shops inspect 100% of parts versus sampling (say 5 of 100) at job shops; "the main cost is in the machinery, certification, highly skilled worker" [src-20260806-3a2ec7].
- **Why volume pricing matters.** SendCutSend's own price list: an aluminum part costs $9.41 at quantity 1 and $3.20 at 100 (-65%) [src-20261022-935cf7]. Belosic: "If I was to run one of those customers at a time, we'd be bankrupt", which is why nesting many orders on one sheet matters [src-20260219-15615f].
- **Machine and plant costs.** **Claim (Belosic):** a 12 kW fiber laser costs $1.2-1.3M, "every 3 kW is like 200 grand"; he rejected $4M of conveyors [src-20260626-541ac8]. SendCutSend's Pennsylvania plant: $63.2M, about 170,500 sq ft, 309 jobs, with a $3M state grant [src-20261020-be0cab]. Anduril's rocket-motor plant: $75M for up to 6,000 motors a year with 100 staff [src-20260501-4e5b9a]. **Claim (Machina):** a cell pays back "in less than a year", about 70% of parts are off the shelf, and the DoD estimates one system saves $85M over 25 years by avoiding tooling [src-20250402-161b61]. A stamping die set can cost about $200M but makes thousands of parts a day, so Machina wins only at low volume (LinkedIn commenter) [src-20251009-1f4b2f]. **Claim (Mehr):** a stamping press is used only about 5% of its life [src-20261020-bac9ca].
- **Utilization is the profit lever.** **Claim (Power):** primes' machines run about 10% of the time versus 65-80% at Hadrian, giving "$4 of revenue on $1 of capex" [src-20260610-779f8b]. SendCutSend's CNCs run 90-98%, with 92 standard tools covering 5,000+ unique parts and under 20 programmers handling 100-150 new parts a day (**Claim**) [src-20260525-4a12ab].
- **Robots versus people.** A BMW strategy manager: a humanoid robot's parts could cost $20-30K, a worker about $60,000 a year, yet "the ROI would still be probably negative" today once charging, IT and supervision are counted; one human may supervise 10 robots after validation [src-20261021-25a598]. Foxconn: a robot pick-and-place "may take ... 10 to 15 seconds. But by human, maybe only 2 seconds" [src-20260317-a43440].
- **What this means [inference].** The money is made on machine use and certification, not on robots. A new producer must keep machines busy across many customers to beat 10-15% shop margins.

## 10. Policy tracker (newest first)

**How to read this.** Section 1A.4 explains each tool. This is the dated list, in plain words.

| Date | Policy | What it does | Source |
|---|---|---|---|
| 2026-10-20 | Army plan for 1M drones (reported) | Big volume demand for magnets and airframes | [src-20261020-878aa9] |
| 2026-10-20 | 45X tax credit | Advanced manufacturing production credit: a tax credit per unit made in the US | [src-20261020-7d90fa] |
| 2026-10-19 | DPA Title III tally | 23 awards, $820.5M since January 2025, mostly rare earths ($405.1M) and rocket motors ($196.4M); none to tracked startups | [src-20261019-68fd3d] (med) |
| 2026-09-23 | Army drone magnets | Vulcan chosen to supply | [src-20260923-c53c99] |
| 2026-09-08 | OSC | Pentagon office that lends to critical-tech companies | [src-20260908-f6558e] |
| 2026-07-16 | IEA tally | $65B of public money committed to minerals | [src-20260716-6a06e4] |
| 2026-04-06 | Section 232 metals tariffs | 50% / 25% / 10% tiers; grid equipment 15% to 2028 | [src-20260402-1b5d6c] |
| 2026-01-01 | DIU CSO | Fast Pentagon buying process for commercial tech | [src-20260101-0b051b] |
| 2025-12-18 | FY26 defense law (NDAA) | See below | [src-20251218-f0d6ef][src-20251218-6c4228] |
| 2025-12-15 | Defense industrial strategy | Uses the Defense Production Act (DPA) to fund US capacity | [src-20251215-98f650] |
| 2025-11-03 | OSC loan to Vulcan | $620M | [src-20251103-ee9b27] |
| 2025-08-06 | Apple and MP Materials | Apple commits to buy US-made magnets (no dollar figure here) | [src-20250806-a0a34e] |
| 2025-08-01 | Section 232 copper | 50% on semi-finished copper; refined copper 15% (2027) and 30% (2028) under review | [src-20250805-80f2f4] |
| 2024-12-19 | OTA authority | Prototype contracts can roll into production without a new competition | [src-20241219-9f8fcc] |

**The FY26 defense law in plain words** [src-20251218-f0d6ef][src-20251218-6c4228]:
- Sec. 804(b) lets the Pentagon sign multi-year orders from FY2026 for SM-6, Tomahawk, AMRAAM, JASSM, LRASM, PAC-3 and cheap mass-produced munitions.
- Sec. 867 expands the Industrial Base Fund for castings, forgings and machine tools. It adds grants, OTAs and purchase commitments of up to 10 years, including advance payments.
- Sec. 1842 makes each program check within 120 days which critical spare parts advanced manufacturing could make within 24 months, and who pays the setup cost.
- Also: Sec. 225 (robotic munitions automation), Sec. 1652 (Golden Dome cost reports), Sec. 1841 (a civil reserve manufacturing network), Sec. 1847 (a surge report).

**Gaps.** Golden Dome money to tracked names is unknown. Sec. 1652 only requires reports, though the act's funding tables mention funds "supporting the Golden Dome missile defense system"; the amount is unconfirmed [src-20251218-f0d6ef]. No DPA award went to a tracked startup [src-20261019-68fd3d]. The Vulcan OSC loan is the only federal loan to a tracked name [src-20251103-ee9b27].

**What this means [inference].** Policy now pays for demand (multi-year orders, purchase commitments), not just factories. These are the first tools that could turn prototype wins into multi-year orders.

---

## 11. Companies worth attention

**How to read this.** "Target" means worth a diligence call now. "Candidate" means worth watching. "Benchmark" means too expensive for SPC but useful for comparison. "White space" means a gap with no strong company yet.

**Targets.**
- **Senra** (fabrication): Series B size, real customers, its own software. Next: founder call; ask for first-pass yield and repeat-order data.
- **Freeform** (precision parts): the best-evidenced loop; $179M valuation. Next: customer reference calls (Boeing, DIU).
- **Isembard** (precision parts, franchise): a capital-light Hadrian variant; valuation undisclosed; Thales' procurement chief is skeptical [src-20251110-84b67e]. Next: economics per franchise, and how primes would audit franchised sites.

**Candidates.**
- **Fabri:** castings are about 40% of munitions (claim, Power) [src-20260921-876080]; backed by RTX and Lockheed. Next: a second source.
- **1872:** cheap entry, energy skids. Next: track to its first repeat order.
- **Atomic Industries:** tool and die is a bottleneck. Next: a second source.
- **Machina:** depot demand. Next: verify valuation.

**Benchmarks.** Hadrian, Divergent, SendCutSend, Mariana and Amca are priced at $1B-$7.9B. Periodic, CuspAI, Mind and Arda are priced before product; watch for revenue.

**White space.**
- Software for mid-size metal distributors: about 9,400 sites, with the top 50 holding half [src-20251201-4b732d]. We passed on Nox.
- Forgings: the Pentagon flags castings and forgings as hard to enter [src-20220215-45c353]; no AI-native forger is in the repo.
- Inspection as a service: inspection takes as long at Hadrian as at legacy shops [src-20260908-ed94f0].

**What this means [inference].** SPC's entry is a Series B in fabrication or a franchise-style variant, not the expensive leaders.

---

## 12. Bottom line

**Five conclusions.**
1. The category is real, but proven demand is narrow. Most buyers value flexibility, scale and total program cost over speed [src-20260921-876080]. Paid demand is speed on prototypes and low-rate work. These startups hold 2-10% of spend at the primes we spoke to [src-20260802-ef6506][src-20260802-36d46c].
2. The data loop has partial evidence (score 2) only where the process is continuous: Freeform, Mariana, Radical, plus Hadrian's faster training. Nobody shows improvement over time (section 6).
3. Capital falls into three tiers: capital-light owner-operators (SendCutSend, Senra); capital-heavy owner-operators funded by debt and government (Hadrian, Vulcan, Mariana); and software vendors that need someone else's plant (Arda, Mind) [inference].
4. Precision parts is priced out at the top: Hadrian $7.87B [src-20260807-b0dc5b], Amca over $1B [src-20260520-af3e6c]. SPC's entry is Series B in fabrication or a hybrid or franchise model [inference].
5. Policy money lands mostly on metals supply: OSC, tariffs including copper, IEA finance, and DPA awards to rare earths and rocket motors [src-20251103-ee9b27][src-20260402-1b5d6c][src-20250805-80f2f4][src-20261019-68fd3d]. The FY26 defense law adds robotic munitions automation and a fund for castings, forgings and machine tools, but no money has reached tracked startups yet [src-20251218-f0d6ef]. Precision parts gets its pull through prime contracts instead [inference].

**Our pick per layer and model [inference].**
- Metals supply: Vulcan and Mariana as benchmarks; distributor software as white space.
- Fabrication: **Senra** (pick); SendCutSend (benchmark); 1872; Machina (hybrid); Path Robotics (enabler).
- Precision parts: **Freeform** (pick); Fabri; **Isembard** (hybrid pick); Hadrian and Divergent (benchmarks).
- Materials R&D: Radical and Periodic (own labs); CuspAI (software).
- Factory software: Arda and Mind (benchmarks); Siemens and Rockwell (incumbents).

**Three risks.**
1. At volume, old shops win: at 1,000 parts a traditional shop is cheaper (Boeing) [src-20260908-ed94f0].
2. Factories before contracts: about $1B needed, per Power [src-20260921-876080]. A munitions slowdown would leave plants idle [inference].
3. Prices ahead of revenue: SendCutSend's multiple is unknown ("nine digits" of revenue at $2.1B) [src-20261020-487a39]; Periodic and Mind are priced before product.

**The strongest bear case.**
- Boeing buyers report paying more, not less; cost matters only after quality and delivery are proven [src-20260818-9b2d5c][src-20260908-ed94f0]. The 2-10% share is prototype work [src-20260802-ef6506][src-20260802-36d46c].
- The model has failed recently: Daedalus went insolvent [src-20260801-4532f6]; Bright Machines' SPAC fell through [src-20240527-6a4884]; Markforged sold for $42.5M after a $2.1B valuation, and Velo3D's shareholders were wiped out though the business survived [src-20261023-63156a].
- Quality on complex parts is unproven: the ex-Anduril lead says Hadrian struggled [src-20250709-43486e]; Thales will not approve a franchise network [src-20251110-84b67e].
- The AI is thinner than the pitch: Opus relies on outside CAM [src-20261004-9b47f5]; robot learning succeeds about 60% of the time versus 99.9% needed [src-20260904-267293]; A-Lab's 41 new compounds were challenged (not retracted) [src-20240124-513fd9].
- Valuations run ahead: Hadrian $7.87B, Mind $3.4B, Periodic about $7.5B (reported), with no audited revenue. A defense or tariff reversal hits plants built ahead of contracts [src-20260921-876080].
- Most buyers do not value speed, per Hadrian's own CEO [src-20260921-876080]. Labor is under 10% of a new plant's cost, so wage savings do not beat China [src-20260513-bdc044].
- Spare capacity exists: existing shops' spindles cut metal only 34% of the time [src-20250120-419768], so demand can be met without new plants.
- Share per customer is capped: SpaceX limits a shop to about a third of its revenue [src-20250708-342eaf]; Boeing will not single-source after the PCC fire [src-20260818-9b2d5c]; trusting a new supplier takes 5-10 years [src-20250712-e5e110].
- Regulators tighten after Boeing's quality failures: "Innovation ... is the first thing that gets sacrificed, and Hadrian falls in that innovation category" [src-20260818-9b2d5c].
- Teams churn: 90% of Hadrian's first 10 employees left by year 5 [src-20260817-8867f2].
- AI CAM vendors sell the same automation to every old shop: CloudNC is inside GibbsCAM [src-20261021-9769d1][src-20261009-7cafd0]; ex-Hadrian staff call CAM vendors the main threat [src-20250708-342eaf].
- Some see a debt business, not a venture one: "better suited to debt than VC" [src-20250709-43486e]; "propped up by VC money" (peer view) [src-20260808-dc5cbb].

**Bias check on our picks.** Senra (10 sources), Freeform (14) and Isembard (13) are among the least-covered names (Hadrian has 76, Machina 42, Arda 33, SendCutSend 31). That avoids picking for press volume, but it means each pick rests mostly on company claims, and Isembard has the one negative buyer call. Treat all three as diligence hypotheses, not conclusions.

**What would change our mind.**
- A prime shows Hadrian or a peer at over 20% of rate-production spend at a lower unit price (bull).
- A company publishes scrap, cycle time or quote accuracy improving with volume (the loop reaches 3).
- Section 232 tariffs are struck down or rolled back (bear for metals and fabrication).
- A tracked owner-operator raises at a lower valuation or stalls a plant (bear).

**What this means [inference].** Back capital-light owner-operators where buyers already pay for speed and qualification. Do not pay software prices for job-shop economics until someone shows the loop.

---


### 12.1 The bear case in one list (new evidence from all sources)
- **Repeat orders are still tiny.** Hadrian's Raytheon spend is "in the tens of thousands" during probation [src-20260823-b3713f]; Divergent's FY25 Air Force awards were about $3.64M [src-20250924-22c5ee]; Mach's federal awards are R&D-scale [src-20260630-fdc552].
- **Customers churn when work gets cheaper.** FlyX left Hadrian over cost as drone work became "less stringent" [src-20260806-3a2ec7].
- **Primes keep sourcing broad.** Buyers want "four or five different vendors" and cap each at 25-30% of their spend [src-20250623-5bc67c].
- **Robots don't pay yet.** BMW's strategy manager: humanoid ROI "would still be probably negative" [src-20261021-25a598]; BMW has no Figure robots running now [src-20261014-ce5195].
- **Defense demand is lumpy.** One defense company got "90% of revenue from congressional marks" (low confidence) [src-20261022-f423ef]; stop-start budgets are "brake and then the accelerator" [src-20260901-a44eee].
- **Incumbents are booming and investing.** Carpenter's specialty-alloy margin hit 37.7% [src-20261022-679fcc]; Howmet absorbed about 720 extra staff in six months [src-20260630-bd78e7]; Nucor credits "supportive federal trade policies" for record shipments [src-20260727-787ce9].
- **AI tools are for sale to everyone.** CloudNC's AI CAM tool is in 1,000+ shops, including Lockheed's [src-20260908-f98d21].
- **Commodity risk.** Ganfeng's market value fell more than 75% with lithium prices [src-20250529-3a588b], a warning for Mariana and Vulcan.

## Appendix A. Glossary

| Term | Definition |
|---|---|
| A&D | Aerospace and defense |
| ABL | Asset-based lending: credit secured by receivables and inventory |
| ACV | Annual contract value |
| AD/CVD | Antidumping and countervailing duties on unfairly priced imports |
| AM | Additive manufacturing: 3D printing |
| AS9100 | Aerospace quality management standard; table stakes for flight parts |
| AS9102 | Standard form for a first article inspection report |
| B2B / B2G | Selling to businesses / to government |
| BOM | Bill of materials |
| CAM | Software turning a 3D model into machine toolpaths |
| Capex | Capital expenditure: money spent on plants and machines |
| CHIPS Act | 2022 law funding US chip factories ($52.7B) |
| CMMC | DoD cybersecurity certification for contractors |
| CNC | Computer numerical control: a computer-driven cutting machine |
| CRO | Contract research organization: an outside lab hired for experiments |
| CSO | Commercial Solutions Opening, a fast DoD solicitation |
| DFARS | DoD procurement rules, incl. specialty-metal sourcing |
| DIB | Defense industrial base: every company that supplies the Defense Department |
| DIU | Defense Innovation Unit, which buys commercial tech fast |
| DoD / DoW | Department of Defense, also called Department of War since 2025 |
| DPA Title III | Defense Production Act authority to fund domestic capacity |
| EBITDA | Earnings before interest, tax, depreciation and amortization; a rough cash-profit measure |
| FAI | First article inspection: full check of the first part made |
| FFP | Firm fixed price contract |
| Form D | SEC filing a company makes when it sells private shares |
| FPY | First-pass yield: share passing inspection first time |
| GM | Gross margin: revenue minus direct cost, as a share of revenue |
| IDIQ | Indefinite-delivery, indefinite-quantity contract vehicle |
| IEA | International Energy Agency |
| IRA / 45X | Inflation Reduction Act (2022); 45X is its per-unit manufacturing tax credit |
| ITAR | US export control limiting defense work to US persons |
| Job shop | Small owner-run shop building to a customer's drawing |
| LIFO/FIFO | Inventory accounting methods; LIFO lowers margins when prices rise |
| LPBF | Laser powder bed fusion, a metal 3D printing process |
| LRIP | Low-rate initial production |
| MES | Software that tracks and directs shop-floor work |
| NADCAP | Accreditation for special processes (heat treat, NDT, coatings) |
| NDAA | National Defense Authorization Act, the yearly defense policy law |
| NDT | Non-destructive testing |
| Nesting | Packing parts on sheet or stock to minimize scrap |
| NRE | Non-recurring engineering: one-time setup cost before production |
| ODM | Original design manufacturer: builds products others sell under their brand |
| OSC | DoD Office of Strategic Capital, a lender |
| OTA | Other Transaction Agreement, fast non-FAR prototype contract |
| PPBE | DoD planning, programming, budgeting and execution process |
| Prime | Top contractor selling whole systems to the government (Lockheed, RTX, Boeing) |
| RFQ | Request for quote |
| RL | Reinforcement learning: AI that learns by trial and reward |
| SBIR | Staged federal R&D grants to small businesses |
| Section 232 | National-security tariff authority (1962 statute) |
| Service center | Metal distributor that stocks, cuts and ships |
| SPAC | A shell company that lists a private company on the stock market |
| TAM | Total addressable market |
| Tier-1/2/3 | Supplier levels below a prime: sub-systems, then parts, then raw inputs |
| USAspending | Public federal database of contract awards |
| Utilization | Share of available machine hours actually producing |

## Appendix B. Gaps and next actions
- Hadrian revenue: two low-confidence figures conflict; get a primary number.
- Startup gross margins: none disclosed; ask Senra, SendCutSend.
- Refining TAM and economics: no free source found.
- Fabrication TAM: none; Census CBP gives counts and payroll only [src-20250626-23f6d9]. Next: 2022 Economic Census receipts by NAICS 3323/3327.
- AI/robotics cost decline over 24 months: no source.
- Golden Dome amounts: the NDAA funding tables reference Golden Dome funds; size and recipients unconfirmed [src-20251218-f0d6ef]. Freeform Skyfall go-live: unconfirmed.
- ABL use by startups: none evidenced.
- Exits (Q14): no comparable acquisition above $100M in repo.

## Appendix C. Source coverage (ledger, 2026-10-25)

Per-source ledger: `insights/exports/primer-ledger.csv`; reading notes kept outside the PDF.

| Bucket | Read status |
|---|---|
| Expert calls (all 28 on-thesis) | Read in full, line by line |
| Podcasts | All 102 read in full (40 earlier, 62 in v3). v5 re-reviewed every reading note (expert calls, podcasts, cited and uncited sources) and added sections 2.8, 5.20, 6.1, 7.1, 8.1, 9A.1 and 12.1. Not citable: 3 files with no transcript (e5f014, da4c3f, 725014). Not cited: one unverified secondary summary (a51ab2) and two duplicates (aafb71 = 8f85ca; dad375 = 876080). Excluded R&D labs (Periodic, CuspAI, Radical) used only for data-loop context |
| Sources the primer cites (~200) | Read in full, except: the FY26 NDAA (about 517K words) checked against every primer claim plus the manufacturing, munitions, reshoring and tariff sections; the DIU guidebook and the boilerplate parts of 10-Q/10-K filings (e.g. ATI) skimmed |
| On-thesis sources not cited (~390) | Read in full; 99 turned out to be a title or placeholder only. One 589K-character academic review of self-driving labs not read (general background) |
| No real text captured | Fast Radius (SEC block page), VulcanForms layoffs, Siemens (menu JSON) and other stubs: claims citing them were removed |
| Form D / award stubs, noise, duplicates | Data rows checked; category confirmed by keyword scan, not read line by line |

Honest limits: the long filings above were not read line by line. Podcast claims are speakers' words on friendly shows, several sponsored or investor-hosted; they are labeled as claims. Funding and valuation discrepancies were dropped by design.
