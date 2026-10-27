# Vertically Integrated Industries: VC primer

_Version 9.5, dated 2026-10-27 (America/New_York). v9 renames the theme to "Vertically Integrated Industries" (v8: "AI-Enabled Vertically Integrated Industries"; before v7.2: "AI-native industrial production") and reorganizes the whole primer by industry, each opening with its own macro case. v9.1 split Chemicals and Materials and added Lumaril. v9.4 adds "Listen & watch" episode lists to each chapter and a listening appendix (E). v9.3 renamed Parts Manufacturing to Manufacturing and expands Divergent. v9.2 merged Minerals and Metals into one Raw Materials chapter (two stages), adds Earth AI, moves Nox Metals to Manufacturing, and renames Materials to Advanced Materials: five industries. Earlier evidence, sources and verdicts carry over. v9.5 adds "Commercial traction and incumbents" sections (3.14-7.14), removes Nox from Raw Materials, and removes repeated text (Chemicals first)._

**The idea in plain English.** America has spent forty years outsourcing the "hard middle" of making things: digging and refining minerals, making metal, machining and welding parts, and producing chemicals. Now defense, industrial policy and China's export controls make that middle valuable again, and it is short of plants and people. We look for startups that **own the plant and sell the physical output** (a mineral, a metal, a part, a chemical) and use **AI, software and automation inside their own operations** to build faster and run with fewer scarce skilled workers than incumbents. Owning production is what lets them keep the margin and the data.

**The five industries (chapters 3–7).**
1. **Raw Materials (Minerals & Metals)** — Stage A, finding and mining ore; Stage B, refining and making metal (smelting, alloys, magnets, powders).
2. **Manufacturing** — metal supply / service centers, then **fabrication (sheet/structures)** and **precision (machining, 3D printing, castings, composites)**.
3. **Chemicals** — producers of chemicals, fuels, fertilizers and pharma ingredients.
4. **Advanced Materials** — producers of engineered materials (battery cathodes, cooling fluids), with a separate **Materials Discovery Labs** sub-group.
5. **Enabling Software & Robotics** — tools sold to other people's factories; tracked, **outside the core**.

**Three labels, used for every company.**
- **Fully integrated** — owns production and sells the product itself. _Core fit._ (Example: SendCutSend owns its lasers and ships parts.)
- **Hybrid** — owns some production or a lab, but also sells services, licenses its process, franchises, or relies on partners to make the product. _Partial fit._ (Example: Hadrian runs its own plants and also puts cells inside Lockheed's plant.)
- **Enabler** — sells software, design, robots or tools to other companies' plants. _Outside the core;_ tracked as competitor, supplier or comparable. (Example: Arda.)

**How to read this doc.** Every industry chapter has the same order: (1) the problem today, (2) macro and tailwinds ranked and marked structural or reversible, (3) headwinds at equal weight, (4) why an AI-enabled vertically integrated company is the answer and where that breaks, (5) what would have to be true and signals — then deeper macro detail, how the industry works, unit economics and data loop, company profiles grouped by label, bear case and key sources. The macro is deliberately the heaviest part. Statements are kept apart:
- Plain sentence ending in `[src-…]` = sourced fact.
- **Claim (who):** = a company, founder or expert assertion. Sourced, not verified.
- `[inference]` = my read. Not sourced; argue with it.

Confidence (high/med/low) is marked on weak numbers. Acronyms are collected in Appendix A. Excluded by Lilly (failure examples only): 

**Contents** (PDF page numbers)

TOC_PLACEHOLDER

---

## 0. Decision summary

_In one line: the category is real and defense demand is strong, but most buyers do not pay much for speed alone, factories must be built before contracts arrive, and nobody has yet shown that the software makes each part cheaper or better over time._

**Verdict [inference].** Back capital-light owner-operators at Series B only where speed and qualification are already paid for (Senra, Freeform, Isembard, as diligence hypotheses). Use Hadrian, Divergent and SendCutSend as benchmarks. Do not pay software multiples for job-shop economics until a company shows unit cost or quality improving with volume. Nobody in the repo shows that yet.

**What the 102 podcasts changed (new in v3).** All 102 podcast files were read in full; the 5 points below changed the view. Each is a speaker's claim unless marked.
- **A. Speed is not worth much to most buyers.** Hadrian's own CEO: "one of the things that I was wrong about is speed ... most of the market just doesn't value speed. The market very much values flexibility, scale, total program cost"; only one rocket company turned speed into value [src-20260921-876080]. That weakens the "speed premium" in finding 1 below beyond urgent and prototype work.
- **B. Capex comes before contracts.** Power: "0% chance of growing revenue unless you spend a billion in CapEx"; only customer prepayment or long-term infrastructure credit has funded such companies [src-20260921-876080]. Machina, Divergent and SendCutSend describe the same debt-for-machines, equity-for-software split (section 2.5).
- **C. Cheap labor is not the edge.** Labor is "less than 10% of COGS" in a new automated plant; China wins on a co-located supply chain (Baglino) [src-20260513-bdc044]. SendCutSend says it can beat China on only about 20-25% of its work [src-20260519-2d6ceb]. Defense is the protected lane (section 3.6).
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
| 2 | Owning the plant creates a data loop | Freeform and Mariana score 2 (section each chapter's data-loop section). Ex-Hadrian: about 80% of non-CAM labor automated, lead times cut about 50% [src-20250708-342eaf]; reprogramming saved 50-80% of CAM time [src-20260611-7b80f0] | Toolpaths come from third-party CAM, with Vericut (simulation software) as the check [src-20260611-7b80f0][src-20261004-9b47f5]; CMM (coordinate measuring machine) inspection is manual [src-20260817-8867f2]; a buyer asks "is it actually" software-enabled [src-20250729-a0a78c] | Workflow automation is real. Learning with volume is not evidenced |
| 3 | Moats: process data, secured capacity, qualification | Trusting a new supplier takes 5-10 years [src-20250712-e5e110]; change-of-control clauses in defense contracts (contracts that can be voided if the supplier is sold) [src-20260817-8867f2]; lock-in from 50-year programs [src-20260818-9b2d5c] | Share caps (finding 3); 90% of the first 10 Hadrian employees gone by year 5 [src-20260817-8867f2]; incumbent PCC is also automating [src-20250712-e5e110] | Qualification is a moat once paid, but it caps share. No data moat evidenced |
| 4 | Hardware-inclusive producers can return venture outcomes | SendCutSend profitable 8 years [src-20260519-38c7ed]; Hadrian plants are debt-funded [src-20260817-c48f28] | "Not ... a fantastically profitable business"; a six-machine plant 1 cost "well north of $10 million" [src-20260817-8867f2]; net per-part saving after capex is 20-30% at best [src-20250712-e5e110]; Hadrian is "better suited to debt than VC" (ex-Anduril PI) [src-20250709-43486e] | Unproven. Underwrite the speed premium and the debt capacity, not cost leadership |

## 1. The theme in plain English

**What it is.** AI-enabled vertically integrated industries means companies that build and run their own factories (or, in one variant, the software that runs other people's factories) and sell the output: parts, metal, material. The product is the physical thing; the software is how they make it faster and with fewer skilled people than incumbents. SPC's slide 8 frames it as producers "that build and run their own production capacity, using in-house AI and software to quote, schedule, and control robots and machines" [src-20261022-80fd75].

**Legacy vs AI-native.**

| | Legacy | AI-native |
|---|---|---|
| Who | Job shops (small owner-run machine or fab shops that build to a customer's drawing), service centers (metal distributors that stock, cut and ship metal), brokers and marketplaces | Hadrian, SendCutSend, Senra, 1872, Nox, Mariana |
| Software | ERP and CAM bought off the shelf (CAM = software that turns a 3D model into machine toolpaths; ERP = the back-office system of record) | Built in-house around quoting, nesting (packing parts onto a sheet or block to minimize scrap), CAM automation, scheduling, robot control and inspection |
| Speed | Average aerospace part 8-12 weeks, 40% late or with quality issues [src-20251024-2e5383] (med, single memo) | **Claim (SendCutSend):** 48 hours design to delivery [src-20260227-e92d45]; **Claim (Senra):** harness lead time six months to two weeks [src-20260128-a16c79] |
| Learning | Knowledge sits in the heads of machinists averaging early-60s in age (**Claim, Chris Power**) [src-20260908-65fab6] | Thesis: every part made improves the next quote, schedule and QC. Evidenced at 2 of ~15 names (section each chapter's data-loop section) |

**Three business models** (taxonomy `model`):

| Model | Best example | Tradeoff |
|---|---|---|
| owner-operator | SendCutSend: owns all its lasers and plants, bootstrapped to a $1.01B round in May 2026 [src-20260519-38c7ed], then a Series B at $2.1B five months later [src-20261020-487a39] (med, single trade write-up) | Owns the data and the margin; carries the capex and utilization risk |
| software-first | Arda: CAD-to-work-instructions agent inside Anduril's ArsenalOS; $160M Series A at $1.5B [src-20261020-914a64] | Capital-light, fast to revenue; needs a host plant for data and competes with Siemens and Rockwell on the installed base [src-20250326-cc1810][src-20260804-0e8130] |
| hybrid | Hadrian (owns factories, now embeds cells inside Lockheed's Grand Prairie plant on a 7-year deal) [src-20261014-015327]; Isembard (owned plus franchised factories on MasonOS) [src-20260909-b547c7] | Tries to get owner data with partner capital; harder to underwrite because economics are split |

The core tradeoff in one line: owner-operators buy data ownership and pricing power with capital intensity; software-first buys speed and margin with data dependence on someone else's plant [inference].

**Why the rename [inference].** The original name implied only factories for machined and fabricated parts. Lilly's broader frame is any sector where a company uses AI to make and sell its own product. That pulls in chemicals (section 5) and materials producers such as Orbital and Mitra (section 4.10), and it makes the integration label in section the industry chapters the first screen: a company that owns production and sells the output fits; a company that sells software to someone else's plant is an enabler.

## 2. Cross-cutting macro (applies to all five industries)

_This merges the old sections 2 (macro primer), 2 (macro in depth), 2 (why-now drivers) and the Oct 26 sourcing notes (old 0A). It assumes no background. Every number has a source; anything marked [inference] is my read._

**The short version [inference].** Four things are true at once:
1. Washington is spending, lending and even taking equity at a scale not seen since the Cold War. That money goes to anyone who can produce metals, magnets, munitions and chips in the US.
2. Building a factory has got more expensive and more uncertain. Rates went back up, metal tariffs raise input costs, and construction spending on manufacturing plants is falling.
3. China has shown it will cut off critical minerals, and the current pause on those controls expires in weeks.
4. Labor is the binding constraint, not demand.

AI-native producers sell into the first and third points and are hurt by the second. Their pitch on labor (fewer, more productive people) only works if the software is real.

### 2.1 Manufacturing in one page

- **How big it is.** US manufacturing added $2.90 trillion of value in 2025. That is 10.1% of GDP (gross domestic product, the total value of what the economy produces). It employs 12.65 million people, at average pay of $112,261 [src-20261013-a7c995].
- **How it is organized.** Think of a pyramid. At the top are a few **primes**: the big companies that sell finished systems (a missile, a jet, a submarine) to the government. The top five US defense contractors in FY2023 (fiscal year) were Lockheed Martin ($61.4B of contracts), RTX/Raytheon ($24.1B), General Dynamics ($22.9B), Boeing ($20.1B) and Northrop Grumman ($16.3B) [src-20251215-98f650]. Below them are **tier-1 suppliers** (big sub-systems), then **tier-2 and tier-3 suppliers** (individual parts, castings, forgings, wire harnesses, raw metal).
- **The bottom of the pyramid is small and old.** The US has 17,156 machine shops. 83% have fewer than 20 employees [src-20250626-23f6d9]. They are called **job shops**: small owner-run businesses that make parts to a customer's drawing. The count is shrinking: 4,874 machine shops were lost from 2002 to 2018, about 20% [src-20250909-29c826]. **Claim (Isembard):** the average owner is over 65 and 40% plan to retire within five years [src-20260310-45bab3].
- **The top has consolidated.** Aerospace and defense primes fell from 51 to 5 since the early 1990s [src-20220215-45c353]. Fewer buyers means fewer, larger programs, and more power over suppliers.

**What this means.** The supply base that makes physical parts is fragmented, aging and shrinking, while the buyers at the top are few and powerful. That gap is the opening every company in this primer is trying to fill [inference].

### 2.2 Six forces behind "why now" (overview)

**1. Defense needs more munitions and ships, fast.** After Russia invaded Ukraine in 2022, the US and allies used up munitions faster than factories could replace them. Congress's research service says much of the concern about the defense industrial base "has focused on munitions production due in large part to high rates of expenditure" [src-20251215-98f650]. Primes are now signing long deals with new producers. Lockheed signed a 7-year deal to put Hadrian's automated machining cells inside its missile plant [src-20261014-015327]. The Navy put $900M toward Hadrian plants for submarine parts [src-20260320-67ba4c].
- _What this means:_ demand is strongest for defense parts that are late today. It depends on budgets that Congress sets each year [inference].

**2. China controls key inputs.** China leads refining for 19 of 20 strategic energy minerals, with about 70% average share [src-20250521-c62d29]. It makes about 94% of rare-earth magnets (the strong magnets inside motors, drones and missiles) and cut magnet exports in April 2025 [src-20251103-ee9b27]. The US imports 100% of 16 mineral commodities, 67% of rare earths and 57% of refined copper [src-20260206-04fe3e]. Almost 90% of the most advanced chips are made in Taiwan [src-20230928-c47558].
- _What this means:_ "Can we make this at home?" is now a national-security question, not only a cost question. That is why governments pay for domestic capacity even when it costs more [inference].

**3. Tariffs make imported metal and parts dearer.** Tariffs are taxes on imports. Since April 2026, products made almost entirely of steel, aluminum or copper face a 50% tariff; products that contain them face 25%; and 10% if the metal was melted or smelted in the US [src-20260402-1b5d6c]. This helps US mills: Nucor's gross margin rose from 14% to 20% (part of it a one-off refund) [src-20260812-77d6f5]. It hurts US companies that buy metal: Nucor's own fabrication segment reported "margin compression resulting from higher steel input costs" [src-20260812-77d6f5].
- _What this means:_ tariffs are set by presidential proclamation and can be reversed. They are a tailwind, not a foundation [inference].

**4. There are not enough skilled workers.** Deloitte and The Manufacturing Institute project 3.8 million US manufacturing jobs to fill from 2024 to 2033, with 1.9 million possibly unfilled [src-20240416-b69154]. Manufacturing had 522,000 open jobs in August 2026, against a pre-pandemic average of 432,000 [src-20261013-a7c995]. The Defense Department says it needs at least 122,000 more shipbuilders, engineers and other critical workers by 2028 [src-20250101-af28c1].
- _What this means:_ the bottleneck is people, not machines. Software that lets a less experienced worker do skilled work is the core promise of "AI-native" production [inference].

**5. The government now lends and buys, not just regulates.** Six tools matter (each explained in 2.4): the NDAA, CHIPS, the IRA's 45X tax credit, DPA Title III, the Office of Strategic Capital and Section 232 tariffs. Together they lower the cost of building a plant and, more recently, promise to buy output for several years.

**6. Money is available, but not cheap.** Venture investors put large sums into this category in 2026 (Hadrian raised $1.37B in one round [src-20260807-b0dc5b]). But interest rates are rising again: the Federal Reserve raised its benchmark rate to 3.75-4.00% on September 16, 2026, saying "inflation remains elevated" [src-20260916-f0c016]. Factories are mostly paid for with loans once the first one works [src-20260817-c48f28]. Higher rates make every new plant more expensive to finance [inference].

**What would reverse the trend.** A defense budget cut or delay, tariffs struck down, a peace that slows munitions buying, or a jump in rates. Also: existing shops have spare capacity. The average machine in a US shop cuts metal only 34% of the time, against a 70% target [src-20250120-419768]. Some demand can be met without new factories.

### 2.3 Industrial policy and the policy toolkit

**From grants to stakes.** The CHIPS Act of 2022 gave about $39B of manufacturing incentives and $11B of R&D money, run by NIST at Commerce [src-20220511-6efadf]. Under the current administration the tools have changed more than the money has. The government now takes equity. Commerce turned Intel's CHIPS grants into a 9.9% stake: $8.9B for 433.3M shares at $20.47 a share [src-20260726-39275b]. Fortune counts about $26.7B of US government equity across roughly 30 deals, including $400M in MP Materials, and notes how hard the stakes are to track [src-20260726-39275b].
- **Why it matters [inference]:** a startup that becomes a "national champion" for one material can now get the government as a shareholder and an anchor buyer. The flip side is that the state also picks winners, and a competitor it picks can crowd you out.

**CHIPS is ending.** According to the Congressional Research Service, FY2026 was the last year of appropriated CHIPS manufacturing money. The 35% advanced-manufacturing investment tax credit (48D) covers only projects that start construction by December 31, 2026 [src-20260701-78183b]. The CRS report tracks fab-by-fab status: several big fabs have slipped or been rescoped, and the window for new projects to qualify closes in about nine weeks [src-20260701-78183b].
- **For our companies [inference]:** semiconductor-adjacent materials startups (Periodic, CuspAI, Orbital) are selling into an industry whose subsidy flow peaks now. After 2026 the growth has to come from AI demand, not from subsidies.

**IRA to OBBBA.** The One Big Beautiful Bill Act (OBBBA, July 2025) cut back much of the Inflation Reduction Act (IRA), but kept the 45X production credit for components (battery cells, modules, critical minerals and others) [src-20250608-08074e]. Here is what changed, per Miller & Chevalier [src-20250608-08074e]:
- Most 45X phase-downs now begin in 2030. Wind components lose the credit after 2027.
- A product gets no credit if it receives "material assistance" from a prohibited foreign entity (in practice, Chinese-linked inputs or ownership above set thresholds).
- Metallurgical coal was added as a critical mineral that qualifies.
- Critical minerals keep the credit longer than most components.

**Bonus depreciation is now permanent.** OBBBA made 100% first-year ("bonus") depreciation permanent for qualifying property acquired after January 19, 2025. IRS Notice 2026-11 sets out the guidance [src-20260114-2075f7][src-20260101-08d847].
- **Plain English:** a manufacturer that buys a $2M machine can deduct all $2M from taxable income in year one, not over 7–10 years. That makes machines cheaper after tax for any profitable buyer.
- **For our companies [inference]:** this is quietly one of the most helpful policies for owner-operators like Hadrian, SendCutSend and Senra once they pay tax. It helps profitable incumbent job shops even more, since they can use the deduction now. It also makes it cheaper for an incumbent to buy robots, which narrows the startups' edge.

| Tool | What it is | What it does for producers | Source |
|---|---|---|---|
| NDAA | The yearly law that sets defense policy (not the money itself; money comes in separate appropriations bills) | FY26 version: multiyear munitions buying (Sec. 804(b)); an Industrial Base Fund for castings, forgings and machine tools, with purchase commitments of up to 10 years and advance payments (Sec. 867); a review of which spare parts advanced manufacturing can make (Sec. 1842) | [src-20251218-f0d6ef] |
| DPA Title III | Defense Production Act of 1950. Title III lets the government pay to expand domestic capacity: direct purchases, purchase commitments, even installing equipment in private plants | 23 awards, $820.5M since Jan 2025, mostly rare earths and rocket motors; none yet to the startups we track | [src-20251215-98f650][src-20261019-68fd3d] |
| OSC | Office of Strategic Capital, a Defense Department lender created in 2022. It makes loans and loan guarantees for 34 critical technology areas, including advanced manufacturing | $620M loan to Vulcan Elements for a magnet plant; FY2026 funding of $97.8M can back up to $4.4B of loans, and the 2025 reconciliation law adds credit subsidy for up to $100B each for critical minerals and covered technologies | [src-20251103-ee9b27][src-20260908-f6558e] |
| CHIPS Act | 2022 law: $52.7B for FY2022-2027 for US chip factories, research and workforce | Mostly helps chip fabs; it co-funded the Vulcan magnet deal with a $50M incentive | [src-20230928-c47558][src-20251103-ee9b27] |
| IRA 45X | A per-unit tax credit from the 2022 Inflation Reduction Act for US-made energy components. Critical minerals earn 10% of production costs | The 2025 tax law (P.L. 119-21) phases the minerals credit out 2031-2034 and bars Chinese-linked supply chains | [src-20251001-45a0c1] |
| Section 232 | A 1962 law letting the President set tariffs on national-security grounds | 50/25/10% metals tariffs (see 2.3) | [src-20260402-1b5d6c] |
| Buy American / Specialty Metals | Laws requiring the Defense Department to buy US-made goods; specialty metals (titanium, nickel, some steels) must be melted in the US | Protect domestic demand for metal and parts | [src-20251215-98f650] |

**What this means.** Policy is strongest for metals and minerals (loans, credits, tariffs). For machined parts, policy works mainly through prime contracts and the new multiyear authorities [inference].

### 2.4 The government as lender and investor: OSC, EDF and DPA Title III

There are three federal "banks" for industry. Founders mix them up; investors shouldn't.

**1. Office of Strategic Capital (OSC), Department of Defense.**
- **What it is:** a DoD lender created in 2022 to make loans and loan guarantees for "critical technologies" in the defense supply chain.
- **Recent deals:** in June 2026 OSC issued conditional loans of $725M to Energy Fuels and $500M to Phoenix Tailings (rare-earth metal and magnet feedstock; facility due 2028), about $1.2B in total [src-20260618-184e0c]. It made an earlier $150M loan to MP Materials [src-20260807-110c13].
- **New fund-finance program:** OSC opened a program to lend $500M–$1B per fund to private investment funds that back critical-technology companies. Applications are due November 1, 2026, and commitments are expected by March 10, 2027 (Mintz) [src-20260831-4dd3b7].
- **The FY27 budget request** includes about $20B of mandatory money for OSC [src-20260831-4dd3b7].
- **Quote (Breaking Defense):** an OSC official said that without germanium, gallium and rare earths, the defense-production buildout "is a pipe dream" [src-20260618-184e0c].
- **What it means [inference]:** for a capital-heavy producer (Vulcan, Mariana, a casting or forging startup), OSC debt can replace 30–60% of the equity it would otherwise need. That is a real reason VC returns in this space can beat their history. For SPC specifically, the fund-finance window is worth a look on its own: it is leverage for funds, not just for companies.

**2. Office of Energy Dominance Financing (EDF), formerly the DOE Loan Programs Office (LPO).**
- **What it is:** DOE renamed LPO as EDF. Its leadership says it has more than $289B of loan authority and is restructuring about $83B of Biden-era loans and conditional commitments [src-20260116-27c00a][src-20251217-51eb2f].
- **Where the money is going:** toward nuclear, grid, fossil and critical minerals. Mayer Brown lists $17.5B conditional for Westinghouse AP1000 long-lead components and $26.5B to Southern Company, among others [src-20260804-05a6a5].
- **For mineral developers:** EDF wants offtake contracts, a proven technology and US content. Mayer Brown lays out what developers need to bring [src-20260804-05a6a5].
- **What it means [inference]:** EDF debt fits late-stage plants, not Series A companies. But a reactor buildout means years of demand for forgings, castings, valves and precision parts, which is exactly what Hadrian-, Freeform- and Divergent-style producers sell.

**3. Defense Production Act (DPA) Title III and the Industrial Base Fund.**
- **What it is:** DoD grants and purchase commitments to create or expand domestic capacity.
- **Examples:** the critical-minerals factbook lists DPA, DLA (Defense Logistics Agency) stockpile orders for magnets, and CHIPS awards, including USA Rare Earth's $277M grant plus a $1.3B loan [src-20260807-110c13]. The FY2026 NDAA added munitions-automation and Industrial Base Fund sections [src-20251218-f0d6ef].

**Executive orders on critical minerals.** The March 2025 order ("Immediate Measures to Increase American Mineral Production") speeds up permits and directs DPA and DFC financing toward minerals [src-20250320-91988a]. The April 2025 order opens offshore and seabed minerals [src-20250424-a310b3].
- **What it means [inference]:** permitting speed is the policy most likely to matter for a mine or refinery startup. A permit that takes 3 years instead of 10 changes the net present value more than any grant.

### 2.5 Capex, construction, rates and how plants get financed

- **Factory construction is cooling:** US manufacturing construction spending was $202.4B (annualized) in December 2025, almost 16% below its August 2024 peak, and down 21.9% year on year by May 2026 [src-20260302-477c5f][src-20260708-da5010].
- **Data centers are crowding it out:** data centers make up about 35% of contractor backlogs [src-20260708-da5010]. They compete with factories for electricians, switchgear and power.
- **Rates went back up:** on September 16, 2026 the Fed raised its target by 25bp to 3.75–4.00%, by a 12–0 vote, citing inflation that is still elevated [src-20260916-f0c016].
- **Activity is still strong:** the ISM manufacturing PMI was 54.5 in September 2026, the ninth straight month above 50 (expansion). New orders were 55.3, backlog 56.4, and prices paid 77.9 [src-20261008-89df84]. Deloitte's 2026 outlook notes the PMI was below 50 for most of 2025 [src-20251112-669746].
- **What it means [inference]:**
  1. Demand for parts is good: orders and backlogs are both above 50.
  2. Building new plants is harder. It is costlier to finance and costlier to build.
  3. The CHIPS and IRA-era plant boom is past its peak.
  4. This favors capital-light models: robotized brownfield shops and roll-ups of existing shops (Amca) over greenfield megafactories. It also explains why customers keep pushing suppliers to hold inventory.

**How it works.** A factory must be built before a buyer will sign a production contract, because the buyer wants proof the supplier can deliver. That means spending large sums ("capex", capital expenditure on buildings and machines) years ahead of revenue.
- **Claim (Power):** "0% chance of growing revenue unless you spend a billion in CapEx because no one's going to give you a production contract unless you've already started executing." Capex runs about 2 years ahead of revenue, and Hadrian was "underwater on financing costs" until late Series B. Only two capex-heavy models have worked: the customer prepays (NASA with early SpaceX; "Pentagon doesn't do this") or long-term infrastructure credit [src-20260921-876080].
- **Debt versus equity.** Equity (selling shares) is expensive money; debt (loans) is cheaper but needs assets or contracts behind it. **Claim (Mehr):** "don't fund physical hardware with equity"; Machina's machine loans cost about 2-3% over the prime rate [src-20260220-0d5345][src-20260320-1361e2], a good package about 8-9% and a risky one 12-14% [src-20260430-30ea09]. Hadrian has a $360M bank revolver (a reusable credit line) [src-20260817-c48f28].
- **What banks will not fund.** **Claim (Belosic):** lenders fund machines but not the software team or R&D [src-20260519-2d6ceb]; banks lend only on common, resaleable machines, so custom lines (anodizing, casting) are "unfinanceable" [src-20260624-3dc6f7].
- Venture and government: Hadrian's $1.37B Series D [src-20260807-b0dc5b]; OSC (the Pentagon's lender) lent Vulcan $620M [src-20251103-ee9b27]. **Claim (Dayna Grayson, Construct Capital):** later-stage industrial funding was about $3B in 2021 and has grown about 10x in 4 years [src-20260702-d79e75], which means more competition for deals [inference]. The Fed raised rates to 3.75-4.00% on Sep 16, 2026 [src-20260916-f0c016], which makes plant loans dearer [inference].
- **What this means [inference].** Equity pays for software, the team and the first plant; loans and government pay for later plants once contracts exist. A company without contracts is stuck paying equity prices for steel.

### 2.6 Defense and munitions budgets

- **The FY27 request:** CNAS counts $49.5B of procurement for 10 key munitions in FY27, about 8.5 times the FY16–26 average of $5.8B [src-20261007-c6f64e].
- **The catches** [src-20261007-c6f64e]:
  - About 82% of the money depends on a reconciliation bill passing.
  - Lead times have not improved for 6 of the 10 munitions.
  - Production capacity is the hardest constraint to move.
  - The war with Iran used up more than half of the US stock of high-end interceptors.
  - CNAS calls the budget "necessary but insufficient."
- **Contracts:** framework agreements with the primes (multi-year deals) are mostly not yet converted into contracts while the FY27 bill is pending [src-20261007-c6f64e].
- **What it means [inference]:** this is the single biggest demand driver for AI-native precision parts, energetics, castings and forgings. But the money is back-loaded and political. A startup should show signed sub-tier purchase orders from the primes, not just "the budget is huge." Watch the reconciliation vote.

**How it works.** The US is buying more missiles, ships and drones than its factories can make. The big contractors ("primes", such as Lockheed and Raytheon) cannot add qualified suppliers fast enough. So they are signing multi-year capacity deals with new producers.
- Lockheed signed a 7-year deal to put Hadrian's automated machining cells inside its missile plant (PAC-3, THAAD, PrSM and GMLRS missiles), starting early 2027 [src-20261014-015327]. The Navy put $900M next to more than $1.5B of Hadrian money for three plants making submarine parts [src-20260320-67ba4c]. Divergent will build Tomahawk structures for RTX [src-20260601-976843] and is opening a Long Beach plant sized for 30,000 missile airframes a year [src-20261023-e02543]. The Army chose Vulcan Elements for magnets for a 1M-drones-a-year program [src-20260923-c53c99].
- **Claim (Chris Power, Hadrian CEO):** labor hours per submarine rose from about 13M to more than 70M, and the enterprise is about 50M labor hours a year short [src-20260610-779f8b].
- **Navy, on the record:** a NAVSEA (Naval Sea Systems Command) official says more than 100 ships are on contract and 55 are in construction. He also says: "I do not believe we have a technology problem, we have an adoption problem." One recent boat carries more than 100 critical parts made by 3D printing, and the Navy has spent more than $200M on it, but getting the technical authority to approve those parts took time [src-20250319-f21bec]. The nuclear supply chain shrank from more than 17,000 suppliers to about 5,000 [src-20250319-f21bec].
- **The catch: demand is lumpy.** **Claim (Power):** the government pays once a year and "may not buy missiles next year" [src-20260908-65fab6]. On an Air Force panel, Divergent's CEO said "the big thing is always demand signal", and a Boeing-owned satellite maker said "cadence and multi-year contracts develop capacity" [src-20260504-38bee3]. A Raytheon manager reports suppliers at 80-90% utilization with 9-10 months for castings [src-20250708-2aa3ad].
- **What this means [inference].** Demand is real, but qualification (getting each part approved) is the gate, and it is slow. Multi-year contracts (section 11) are what turn demand into factory loans.

**Oct 26 sourcing update (formerly 0A).** - **Defense money is approved in principle but hasn't been paid out.** CNAS puts the FY27 munitions request at $49.5B, 8.5x the FY16-26 average, but 82% of it depends on reconciliation. Lead times are unchanged for 6 of 10 munitions, and production capacity is the hardest constraint to move. Framework deals with primes (Lockheed up to $9B, Northrop over $2B) are mostly unconverted [src-20261007-c6f64e]. CRS/CBO estimate a $21.7B replacement bill and say some interceptors will take at least five years to replace [src-20261005-b7e08b].
- **Bear: orders lag the budget.** Carpenter's defense bookings fell from the prior quarter and the prior year because customers "are not receiving funds"; the CEO expects a rush once the budget clears [src-20261022-de5e6c]. Aero bookings rose 49% y/y on higher-price long-term agreements. **Claim (Carpenter):** AI productivity gains are ahead of plan (no number given).
- **What this means [inference]:** repeat orders in defense are likely gated by the budget until after the midterms. Ask candidates how much of their backlog is funded versus framework-only.

### 2.7 Labor: the binding constraint, and why cheap labor is not the point

- **The gap:** Deloitte and the Manufacturing Institute estimate that US manufacturing will need 3.8M workers by 2033, and that 1.9M of those jobs could go unfilled [src-20240403-f5594a].
- **Talent is the top problem:** in 2024, 65% of NAM survey respondents named attracting and keeping workers as their top business challenge [src-20240402-b9644b].
- **Technicians:** a 2026 Deloitte/MI study projects 2.3M technician openings by 2030, with about 500k open today. Technician roles are growing about 6 times faster than other manufacturing jobs. It also argues that AI can speed up skills training [src-20260910-b300bf].
- **Spending plans:** 80% of manufacturers plan to put at least 20% of their improvement budgets into smart manufacturing [src-20251112-669746].
- **What it means [inference]:** the pitch to buyers is not "cheaper labor." It is "we can deliver when your job shop can't hire." A producer whose software lets one machinist run 4–6 machines, or a fabricator whose quoting runs itself, sells capacity in a capacity-short market. That is why "owner-operator" beats "software to the plant": the incumbent plant often can't staff enough people to use the software.

**How it works.** Factories cannot hire enough machinists, welders and programmers. Software that makes tasks easier lets people with no factory background do the work.
- Headline numbers are in section 2.2 (Deloitte: 3.8M jobs needed). A 2026 Deloitte follow-up counts 2.3M technician openings for 2025-2030 but leaves out machinists, so do not add the two [src-20260910-a2cd42].
- **Claims (owner-operators):** Hadrian trains new operators in 30-40 days instead of a decade [src-20260926-70087f]. SendCutSend hired 200 welders in a year, mostly people with no factory experience; average floor age is about 25 [src-20260525-4a12ab]. Shipyard starting pay is about $22-23 an hour and average tenure is about 4 years (Navy panel) [src-20250319-f21bec].
- **The important correction.** Drew Baglino (ex-Tesla, now Heron Power): in a new automated factory, in China or the US, "the labor differential is less than 10% of COGS" (cost of goods sold), maybe under 5%. What makes China cheaper is that its supply chain sits close together: all ~7,000 car parts within a 3-hour drive [src-20260513-bdc044]. **Claim (Belosic, SendCutSend):** a dark (fully automated) factory is not the answer; his edge is software plus well-paid people [src-20260519-2d6ceb].
- **What this means [inference].** Saving on wages alone will not beat China. The edge is having enough trained people at all, plus being close to customers and suppliers.

### 2.8 Power, permits and build time

**How it works.** A factory needs a large electricity hookup and permits. Both can take years.
- **Claim (Belosic):** "We need 100 times more power"; Reno warehouses lack electrical service; transformers and permits are delayed; "everyone wants to re-industrialize, but we don't have the power" [src-20260519-5cfe14].
- **Claim (Vulcan CEO):** "if you can't get a permit for several years ... running out of cash"; and most magnet-making equipment itself comes from China [src-20250429-6f9155]. Permits for identical equipment take "3 weeks, 3 months, or 3 years" depending on the town (Torus, Utah panel) [src-20260813-1fe8a2].
- **Claim (Mariana CEO):** after permits, a mine or refinery can take about 5 years to build and 3-5 years to ramp [src-20260513-bdc044]; Chinese refineries commission in about 6 months versus 2-4 years in the West [src-20250723-3f3ef8].
- **What this means [inference].** Speed to build and ramp is itself a competitive edge, and power is a site-selection question for every plant.

### 2.9 Venture climate and how investors see it

- **AI dominates:** US VC deal value hit $515.8B through Q3 2026, with AI taking 82.7% of it. Exits are still stalled (PitchBook-NVCA) [src-20261008-8f7d66].
- **Defense tech:** a record $2.5B in Q3 for defense-specific startups, led by Castelion ($1.1B) and Mach ($900M). Seed deals fell to 41, the fewest since 2016 [src-20261006-0f220a].
- **Concentration:** one tracker counts $14.6B of defense-tech funding year to date, against $9.6B for all of 2025, with deal count flat. The money is going to fewer winners [src-20260908-abd0c7].
- **What it means [inference]:** the dollars are concentrating in late-stage "AI" and "defense" labels, and seed is getting thinner. That creates two opportunities: (a) better seed and Series A prices for producers that don't fit the hype labels; (b) a risk that the best AI-native producers are priced as AI companies. Lila, CuspAI and Periodic valuations are an example (section 6).

- **It costs a lot to build.** A first six-machine factory cost "well north of $10 million" [src-20260817-8867f2]. Hadrian's Mesa plant was about $200M [src-20250820-cfbf02]. Software companies do not need this.
- **Margins are lower than software.** Gross margin is revenue minus the direct cost of making the product, as a share of revenue. Software companies often run far higher than manufacturers. Benchmarks here: Proto Labs 44.5% [src-20260206-8bb619]; Xometry's marketplace 34.7% [src-20260224-a7b149]; metal service centers 18-32% [src-20260729-407fd7][src-20261021-16bb64]; a manufacturing roll-up "effectively ... 30%" (claim) [src-20241001-28c2aa].
- **Who pays for what.** Venture equity pays for the team, the software and the first plant. Banks, equipment lenders and the government pay for plants two and beyond, once a plant is proven. Hadrian: "equity never funds factory construction" (claim) [src-20260807-b0dc5b]; it has a $360M bank credit line [src-20260817-c48f28].
- **The bull case.** If software lets one plant run at much higher utilization with fewer skilled workers, it can earn better margins than a job shop and win share. **Claim (Chris Power, Hadrian CEO):** utilization of 65-80% versus about 10% at primes [src-20260610-779f8b].
- **The bear case, with equal weight.** Several buyers say they pay the same or more, not less (section 0). Some see these firms as "better suited to debt than VC" [src-20250709-43486e]. Recent failures: Daedalus (an AI-run machining factory) went insolvent in August 2026 [src-20260801-4532f6]; Markforged went from a $2.1B valuation to a $42.5M sale [src-20261023-63156a]; Bright Machines' SPAC (a listing via a shell company) fell through [src-20240527-6a4884].
- **Exits are unproven.** The repo has no acquisition of an AI-native producer above $100M (Appendix B). Likely exit paths are sale to a prime or incumbent supplier, an IPO (stock listing) at scale, or continued private ownership with debt [inference].

**What this means for SPC.** The question is not "is manufacturing coming back?" It is "can a software-run plant earn better margins than a job shop, and turn fast prototype wins into multi-year orders?" Everything after this section tests that [inference].

### 2.10 Science policy: the Genesis Mission, DOE, NSF and the national labs

- **What it is:** the Genesis Mission (EO 14363, November 24, 2025) tells DOE to build an integrated AI platform for science. It links national-lab supercomputers, datasets and robotic labs. Named priorities include advanced manufacturing, critical materials, semiconductors and energy [src-20251124-b97a20].
- **Platform demo (July 2026):** a Model Access Gateway to frontier models, simulation agents, national-lab datasets and DOE-built Model Context Protocol (MCP) tools, with open protocols for outside tools [src-20260722-edf40f].
- **Awards (October 8, 2026):** 12 new Phase II awards worth $159M, for 14 Phase II projects in total. The first-year cohort has 297 projects. Materials examples include rare-earth separations at UIUC and quantum magnets at ORNL [src-20261008-452806].
- **Hackathon (October 21, 2026):** 450+ participants and 185 projects, backed by $1M of compute and 55k DOE compute hours [src-20261021-4b8e0f].
- **NSF:** spends more than $700M a year on AI research [src-20261019-5257f3].
- **Existing ties:** national-lab self-driving labs such as Argonne's Polybot [src-20250217-059784] and Sandia's partnership with Radical AI on hydrogen-purification alloys [src-20260929-dfb65a] show that labs are already working with startups.
- **What it means [inference]:** Genesis is both a funder and a competitor for discovery startups. It gives free compute, data and test beds, and partnerships like Radical–Sandia. It also builds free public models, tools and data that weaken the "proprietary model" moat. Startups win on what they make and qualify, not on the model.

### 2.11 More macro facts a newcomer should know

- **Labor numbers, freshest first.** In a Q3 2026 NAM survey of 220 manufacturers, 54.9% cite workforce as a top challenge and 4.79% of jobs sit unfilled [src-20260914-b4d55c]. The American Welding Society expects 320,500 welders needed by 2029, with 157,000+ near retirement [src-20261023-57ad95]. US factory labor costs about $46.30 an hour fully loaded, rising 3-4% a year, while a robot fell from $46,000 (2010) to $23,000 (2022) (newsletter) [src-20260826-14e4bb].
- **Precedent: the government has funded capacity before.** In the 1950s the Pentagon paid $239M (about $2.8B today) for 10 giant forging presses and leased them to industry for 4-5% of revenue [src-20240821-44ed1d]. Today's equivalents are OSC loans and Sec. 867 purchase commitments (section 11).
- **What this means [inference].** The shortage is in sub-tier suppliers and skilled hands, and buyers' stop-start ordering is what keeps small shops from investing.

### 2.12 Market size: overview

No free source gives a clean market size (TAM, total addressable market) for "AI-native production." What we have:
- All US manufacturing: $2.90T value added [src-20261013-a7c995].
- Metal service centers (distributors that stock, cut and ship metal): about $200B of revenue (med) [src-20251201-4b732d].
- Precision manufacturing: about $71B by 2026, machine-shop segment over $60B (med, one analyst memo) [src-20251024-2e5383].
- Global industrial robot installs: $18.6B in 2025, a proxy for automation spending [src-20260924-28b59b].

The full table follows. _What this means:_ the markets are large, but each startup sells into a narrow slice (one part type, one buyer group). Share per buyer is capped (2.2), so growth needs many buyers [inference].

**How to read this.** "TAM" (total addressable market) means the total money spent on something each year. No layer here has a clean, free TAM. Where we only have a stand-in number (a "proxy"), we say so.

**All of US manufacturing.** US manufacturing added $2.90T of value in 2025, about 10.1% of GDP. It employs 12.65M people, paid $112,261 on average [src-20261013-a7c995] (high).

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

_Each industry chapter repeats its own market-size numbers in section x.7._

### 2.13 Data loops: what the sources say for and against

- **For: the data does not exist unless you make it.** Periodic's founder: published values for one material property "spanned many orders of magnitude", and negative results are unpublished, so own-lab data is needed [src-20260403-ba156a][src-20260106-62dba1]. Meta's open release of 100M+ physics simulations shows simulation data is becoming free, but the same paper says errors remain and "more than just model scaling will be required", which favors real experimental data [src-20250513-fbb4d8]. **Claim (Power):** manufacturing data is "never on the internet"; a blueprint is not enough without machining and inspection data [src-20260908-65fab6].
- **For: concrete loop mechanisms.** **Claim (SendCutSend):** "after millions and millions of parts ... we feed it back into our app ... the more jobs that we take in, the smarter we get", for example warning designers about bends; nearly half a million drawings are uploaded a month [src-20260626-541ac8][src-20260624-3dc6f7]. **Claim (Machina):** 150+ sensor channels are recorded every 4 milliseconds [src-20250402-161b61]; a SpaceX part took 25 trials early and now 4-5 on average [src-20260926-70087f]. **Claim (GrayMatter):** 3.6M hours of production runtime recorded [src-20261022-3335bd].
- **Against: the data is siloed and the loop is slow.** Plant data sits in separate layers (machine controllers, MES, ERP), which limits AI (Construct) [src-20250409-8f07e3]. An IMTS observer: "models are largely good enough"; the bottleneck is plant data and adoption [src-20260922-94fcb0]. Physical AI data is "expensive, slow, hard to scale" [src-20260909-524e7c]. Some of Periodic's workflows are "still like 90% human" [src-20261008-83dc1b]. Argonne's academic robot lab publishes its data openly, which weakens the "proprietary data" argument [src-20250217-059784] [inference].
- **Against: trust breaks easily.** AI Robotics' CEO says a pilot fails if "one false detection" makes operators switch the inspector off [src-20261011-5db652]. A VC newsletter warns autonomous plants "keep producing confidently" when wrong, while aerospace change-control rules assume a fixed process [src-20261015-0e1593].
- **Incumbents are using AI too.** **Claim (Foxconn, NVIDIA event):** 80% faster root-cause analysis, +15% labor productivity, -10% machine failures, +3% first-pass yield [src-20261022-89d710]. **Claim (PepsiCo):** AI digital twins raised a Gatorade plant's throughput 20% in 3 months [src-20261015-0e1593].
- **What this means [inference].** Running the plant does create data others lack, but nobody yet shows cost falling with volume, and incumbents can buy similar tools.

### 2.14 Macro scorecard by industry [inference]

| Force | Raw Materials (A: mining / B: refining & metal) | Manufacturing | Chemicals | Advanced Materials | Software & Robotics |
|---|---|---|---|---|---|
| OSC/EDF/DPA money | Strong + (both stages; most to B) | + (via defense) | Mild + (DOE loans, grants) | + (DOE battery awards) | 0 |
| China export controls | Strong + (B most) | Input-cost − | + (pharma reshoring, BIOSECURE) | + (battery materials) | 0 |
| Section 232 tariffs | A: Mild +; B: Strong + (makers), − (buyers) | Mixed | + (pharma; generics excluded) | 0 | 0 |
| Rates 3.75–4.00% | − (most capex-heavy) | Mild − | − | − | Mild − |
| Construction slowdown | − | − | Mild − | 0 | − |
| Munitions budget | + (B strong: magnets, alloys) | Strong + | Mild + (energetics, fuels) | 0 | Mild + |
| Labor shortage | Mild − | Strong + (automation edge) | Mild + | Mild + | Strong + |
| 100% bonus depreciation | + | + | + | + | + (buyers' capex) |
| VC concentration | − | Hype pricing | Mild − | Hype pricing (discovery labs) | − |

**What would change the picture [inference]:** a lasting US–China minerals deal (bad for domestic premiums); the reconciliation bill failing (munitions money slips); rate cuts in 2027 (good for every plant financing).

### 2.15 What would break "why now"

- Tariffs reversed or limited by courts (they are proclamations, not laws) would hit metals and fabrication first [inference].
- A flat defense budget or delayed munitions buys would strand plants built ahead of contracts (section 2.5).
- Higher rates raise the cost of the loans that fund plants #2+ [inference].
- Spare capacity exists: the average CNC spindle at existing shops cuts metal 34% of the time versus a 70% target [src-20250120-419768] (med, survey). The US lost 4,874 machine shops (-20%) from 2002 to 2018 [src-20250909-29c826].


### 2.16 Listen & watch

_Free episodes and videos for this chapter (from listening list v2; links checked Oct 27, 2026). ★ = top pick. Full list: Appendix E._

1. ★ **"China Has Mass. Can America Catch Up?"**, a16z Podcast, Sep 29, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/china-has-mass-can-america-catch-up/) — *Why:* Anduril's and Hadrian's CEOs explain the munitions gap: war games run out in about a week, restocking takes 2–3 years. Repo: src-20250929-452dcb.
2. **"How LA Is Becoming America's New Industrial Tech Hub"**, Bloomberg *Odd Lots*, Sep 21, 2026, 34 min. [▶ Open link](https://www.youtube.com/watch?v=mgCQ0Pl754c) — *Why:* the best mainstream framing; the bottleneck is factory software and feedback, not robots. Repo: src-20260921-a51ab2.
3. **"Can the U.S. Still Build Things?" (#34)**, *The Drone Ultimatum*, with Miles Arnone (Re:Build), about 95 min. [▶ Open link](https://www.thedroneultimatum.com/can-the-us-still-build-things-fixing-the-industrial-base-miles-arnone-podcast-34/) — *Why:* the case for buying and upgrading old shops instead of building megafactories. Repo: src-20261022-f423ef.

## 3. Raw Materials (Minerals & Metals)

_What this industry is._ Raw Materials covers everything from finding ore to delivering a finished metal product: **Stage A, finding and mining** (exploration, mining and concentrating ore) and **Stage B, refining and making metal** (refining to pure oxides, carbonates or cathode, then smelting, alloys, magnets and powders). It sits at the bottom of every supply chain in this primer. Metal distribution (service centers that buy mill metal and cut it to size) now sits in Manufacturing (chapter 4) as a supplier to parts makers.

### 3.1 Shared macro: China's refining grip, the critical-minerals orders and government lending

**China owns the middle of the chain.**
- **China owns the middle of the chain.** China leads refining for 19 of 20 strategic energy minerals, with about 70% average share [src-20250521-c62d29]. It did about 99% of heavy rare-earth processing until 2023 [src-20250414-50f023] and makes about 60% of refined germanium [src-20261027-f82d55].
- **China has shown it will use that leverage.** Export licensing on 7 heavy rare earths and magnets since April 2025; broader controls in October 2025 that were then suspended to **November 10, 2026**; an outright ban on gallium, germanium and antimony exports to the US suspended only to **November 27, 2026** [src-20261019-854e22][src-20261027-f82d55]. China's rare-earth exports fell 9.6% year on year in January–September 2026 [src-20261019-854e22].
- **Prices are already showing stress.** Germanium hit a record ¥28,500/kg on October 26, 2026, up about 110% year to date, with US-warehouse material at a 78.6% premium [src-20261027-f82d55]. In 2025 antimony rose 144% and germanium 106%, while lithium fell 24% and nickel 11% [src-20260130-ebdd5a].
- **Not enough capacity is coming.** The IEA estimates about $6.5 trillion a year of downstream output depends on minerals with concentrated supply chains, and planned magnet capacity outside China covers only about a third of 2035 demand [src-20261014-b9d647].
- **Magnets are almost all Chinese.** China makes about 94% of rare-earth magnets [src-20251103-ee9b27]; another source puts China above 90% and the US under 1% [src-20250429-6f9155]. Magnets go into every motor, drone and guided weapon.

**The critical-minerals executive orders.** March 2025 "Immediate Measures to Increase American Mineral Production" and the April 2025 seabed-minerals order direct agencies to speed permits and finance projects [src-20250320-91988a][src-20250424-a310b3]. A new president can reverse them, but permits already granted stay granted [inference].

**OSC, DOE and DPA lending.** OSC: $620M to Vulcan (2025), $725M Energy Fuels and $500M Phoenix Tailings (June 2026) [src-20251103-ee9b27][src-20260618-184e0c]; EDF (ex-LPO) claims $289B+ of authority and is steering to minerals [src-20260116-27c00a][src-20260804-05a6a5]; ~$26.7B of US government equity across ~30 deals incl. $400M in MP Materials [src-20260726-39275b]; $65B of public money committed to minerals in 2025 [src-20260716-6a06e4]. The FY26 NDAA adds an Industrial Base Fund for castings, forgings and machine tools with purchase commitments of up to 10 years [src-20251218-f0d6ef]. _Meaning [inference]:_ the state is now the anchor lender and often the anchor buyer for both stages; that lowers the cost of capital but lets the state pick champions.

### 3.2 Stage A — Finding and mining: problem, tailwinds and headwinds

**The problem.**
- **The US mines too little and refines almost nothing.** US nonfuel mines produced $112B of output in 2025, but metals were only $38.1B of that; the rest is mostly sand, gravel and stone [src-20260130-ebdd5a]. The US is 100% import-reliant for 16 mineral commodities and more than 50% for 54, including 67% of rare earths and 57% of refined copper [src-20260206-04fe3e].
- **Exploration rarely finds anything.** **Claim (Earth AI):** the industry discovery success rate is about 0.5% per project; Earth AI claims 75% for its own targets [src-20250127-c28430].
- **Building takes a decade.** **Claim (Mariana CEO):** after permits, a mine or refinery takes about 5 years to build and 3–5 years to ramp [src-20260513-bdc044]; Chinese refineries commission in about 6 months versus 2–4 years in the West [src-20250723-3f3ef8].

**Tailwinds, ranked [ranking is inference].**

| Rank | Tailwind | Date / size | Structural or reversible? |
|---|---|---|---|
| 1 | **Executive orders on permitting** | March 2025 "Immediate Measures to Increase American Mineral Production"; April 2025 seabed minerals order [src-20250320-91988a][src-20250424-a310b3] | Reversible by a new president; permits granted under them stay granted |
| 2 | **Demand from defense, grid and data centers** | Rare earths in F-35, submarines, Tomahawk and JDAM [src-20250414-50f023]; an AI campus can need up to 50,000 t of copper [src-20261007-a642ea] | Defense structural; AI capex could slow [src-20261015-c425a9] |
| 3 | **Federal lending and equity at scale** | OSC: $620M to Vulcan (2025), $725M Energy Fuels and $500M Phoenix Tailings (June 2026) [src-20251103-ee9b27][src-20260618-184e0c]; EDF (ex-LPO) claims $289B+ of authority and is steering to minerals [src-20260116-27c00a][src-20260804-05a6a5]; ~$26.7B of US government equity across ~30 deals incl. $400M in MP Materials [src-20260726-39275b]; $65B of public money committed to minerals in 2025 [src-20260716-6a06e4] | Durable for this administration; agencies and authorities can be rescoped |
| 4 | **Tax credits** | 45X credit of 10% of production cost for critical minerals, kept by the 2025 tax law but phased out 2031–34 and barred for Chinese-linked supply chains [src-20251001-45a0c1][src-20250608-08074e] | Legislated, with a sunset |
| 5 | **Stockpiling** | Net imports of processed mineral materials rose to $185B in 2025 from $77B, partly stockpiling [src-20260130-ebdd5a] | Temporary; stockpiles end |

**Headwinds, at equal weight.**

1. **Commodity prices swing.** Lithium fell 24% and nickel 11% in 2025 [src-20260130-ebdd5a]. A mine underwritten at peak prices can be uneconomic in a year.
2. **Permits and time.** Permitting plus 5 years to build and 3–5 to ramp (**Claim, Mariana CEO**) [src-20260513-bdc044].
3. **Geology decides.** Ore grade, not software, sets most of the cost [inference]; most exploration projects never become mines [inference].
4. **Rates.** The Fed raised to 3.75–4.00% on September 16, 2026 [src-20260916-f0c016]; mines are the most rate-sensitive assets in this primer [inference].
5. **A US–China deal takes the urgency out.** Strature puts a 63% probability on a short roll-over of the suspensions [src-20261016-83adeb] (med).

### 3.3 Stage B — Refining and making metal: problem, tailwinds and headwinds

**The problem.**
- **The US refines almost nothing.** The US is 100% import-reliant for 16 mineral commodities and more than 50% for 54, including 67% of rare earths and 57% of refined copper [src-20260206-04fe3e]. Chinese refineries commission in about 6 months versus 2–4 years in the West [src-20250723-3f3ef8].
- **Castings and forgings are thin.** China produces 56% of world castings, and the Pentagon relies on a single US foundry for large titanium parts (General Catalyst thesis) [src-20240202-8c6d3b].
- **Prices of metal have jumped.** ENR reports steel mill products up about 86% and copper wire about 91.4% since February 2020 [src-20260302-477c5f]; steel rose 25% in a year (Robeco) [src-20261007-a642ea]. Reliance says aluminum is "historically elevated largely due to" tariffs [src-20260728-ae7dea].
- **The precedent shows how far capacity fell.** In the 1950s the Pentagon paid $239M (about $2.8B today) for 10 giant forging presses and leased them to industry [src-20240821-44ed1d]. Nothing comparable has been built since [inference].

**Tailwinds, ranked [ranking is inference].**

| Rank | Tailwind | Date / size | Structural or reversible? |
|---|---|---|---|
| 1 | **China's export controls** make non-Chinese supply a security good, not a cost good | Apr 2025 licensing; Oct 2025 controls suspended to Nov 10, 2026; Ga/Ge/Sb ban suspended to Nov 27, 2026 [src-20261019-854e22][src-20261027-f82d55] | Structural in direction; the timing can swing with any US–China deal |
| 2 | **Defense and aerospace demand** | FY27 request: $49.5B for 10 key munitions, 8.5x the FY16–26 average [src-20261007-c6f64e]; Army chose Vulcan magnets for a 1M-drones-a-year program [src-20260923-c53c99]; Carpenter's aerospace bookings rose 49% y/y on long-term agreements [src-20261022-de5e6c] | Structural for 5–10 years; yearly budgets swing |
| 3 | **Section 232 metals tariffs** | 25% to 50% on steel and aluminum in June 2025; since April 6, 2026, 50% on goods almost entirely of steel, aluminum or copper, 25% on derivatives, 10% if melted in the US [src-20260402-1b5d6c][src-20260602-b995e2] | Presidential proclamation; can reverse overnight or be struck down |
| 4 | **Government money for magnets and specialty metals** | $1.4B Vulcan/ReElement package: $620M OSC loan, $50M CHIPS, $50M Commerce equity, DoD warrants [src-20251103-ee9b27]; FY26 NDAA Industrial Base Fund for castings, forgings and machine tools with purchase commitments up to 10 years (Sec. 867) [src-20251218-f0d6ef] | Durable in law; funding is annual |
| 5 | **Buy American / specialty metals rules** | Titanium, nickel and some steels for DoD must be melted in the US [src-20251215-98f650] | Structural (statute) |
| 6 | **Data-center and grid build-out** | An AI campus can need up to 200,000 t of steel and 50,000 t of copper [src-20261007-a642ea]; grid equipment gets a 15% tariff rate until 2028 [src-20260402-1b5d6c] | Reversible if AI capex slows [src-20261015-c425a9] |

**Who gains today.** Nucor's gross margin rose to 20% from 14% (about 1.3 points a one-off refund) [src-20260812-77d6f5]. The incumbents are winning this cycle [inference].

**Headwinds, at equal weight.**

1. **China can crash prices on purpose.** If China floods the market after a deal, prices collapse; producers need floor-price offtake contracts (the MP Materials–DoD template) [inference, based on src-20260726-39275b].
2. **Tariffs cut both ways.** They help metal makers and hurt metal buyers; Nucor's own fabrication unit reported "margin compression" [src-20260812-77d6f5].
3. **The equipment is Chinese too.** **Claim (Vulcan CEO):** most magnet-making equipment comes from China [src-20250429-6f9155].
4. **Orders lag the budget.** Carpenter's defense bookings fell because customers "are not receiving funds" [src-20261022-de5e6c].
5. **Plants are capital-heavy.** Vulcan's 10,000-ton plant rests on a $1.4B package [src-20251103-ee9b27]; custom lines are "unfinanceable" (**Claim, Belosic**) [src-20260624-3dc6f7].
6. **The state picks winners.** Government equity can crowd out a startup that is not the chosen champion [inference].

### 3.4 Why an AI-enabled, vertically integrated company is the answer here
- **Stage A, finding and mining:** AI narrows where to drill; owning the claims and the drill rigs keeps the upside of a discovery. **Claim (Earth AI):** drilling at about $100 a meter and up to 80% lower exploration cost [src-20250127-c28430]. **Where it breaks [inference]:** a discovery is worth little until it is drilled out, and most projects are sold to miners rather than run.
- **Stage B, refining: why own the refinery?** The scarce thing is a working, permitted, financed plant outside China. A software vendor cannot sell "non-Chinese supply"; only the owner of output can sign the offtake contract that lenders (OSC, EDF) want [src-20260804-05a6a5].
- **Why AI?** The two biggest costs are time to build and time to ramp. **Claim (Mariana):** its software halves 5–10-year project timelines, and its first plant runs about 50% autonomously with AI agents retuning the process every 15 minutes [src-20260803-30e6d5][src-20260623-d1790b]. If true, that attacks exactly the 6-month (China) versus 2–4-year (West) commissioning gap [src-20250723-3f3ef8].
- **Magnets and specialty metals:** the buyer (DoD, drone makers) needs a non-Chinese, qualified source. Only an owner of the plant can be that source and sign the long-term offtake or loan. Speed of qualification is the edge: **Claim (Vulcan):** its pilot plant opened March 31, 2025 and was shipping and qualifying magnets within months [src-20250811-e7cb9a]; software and data on each batch are how a new plant learns faster [inference].
- **Where the logic breaks [inference].** Ore grade and price cycles decide most of the economics, not software; a refinery is a single giant bet, so venture equity is the wrong money for most of it.

### 3.5 What would have to be true, and signals to watch

- A non-Chinese price floor holds (offtake contracts with floors, or tariffs) even after a US–China deal. **Watch:** November 10 and November 27, 2026 deadlines; any DoD price-floor deals.
- AI actually shortens build and ramp. **Watch:** Mariana's first plant hitting nameplate on schedule; recovery and cost per ton (not yet disclosed).
- Government debt replaces most equity. **Watch:** OSC fund-finance commitments (expected by March 10, 2027) [src-20260831-4dd3b7]; EDF mineral loans closing.
- Permitting really gets faster. **Watch:** time from application to permit on new projects under the 2025 orders.
- An AI explorer turns a prospect into a defined resource. **Watch:** a formal resource estimate at Earth AI's Fontenoy or Willow Glen projects [src-20241121-ac9f37].
- A US magnet maker reaches cost close enough to China that offtakes renew without subsidy. **Watch:** Vulcan's first production; Army drone-magnet orders.
- Section 232 stays in place long enough for plants to be built. **Watch:** court challenges and any tariff deals.
- Defense money actually flows. **Watch:** the FY27 reconciliation vote and Carpenter's next defense bookings.

### 3.6 Macro in more depth

**Stage A and B, minerals detail.**

**Where things stand (late October 2026):**
- **April 2025:** China put export licensing on 7 heavy rare earths and the magnets made from them (MOFCOM Announcement No. 18). That rule is still in force [src-20261019-854e22][src-20250414-50f023].
- **October 2025:** China added broader controls, including rules that reach foreign products containing Chinese rare earths (Nos. 55–58, 61, 62). Under the US–China truce, Announcement No. 70 suspended them until **November 10, 2026**. No extension text has been published as of October 19. The US side says the truce runs to January 10, 2027 [src-20261019-854e22].
- **Gallium, germanium and antimony:** China's outright ban on exports of these to the US is suspended until **November 27, 2026** [src-20261027-f82d55].
- **Exports are already down:** China's rare-earth exports fell 9.6% year on year in January–September 2026 [src-20261019-854e22].
- **Germanium price:** a record ¥28,500/kg on October 26, up about 110% year to date. Material held in US warehouses trades at a 78.6% premium. China makes about 60% of refined germanium [src-20261027-f82d55].
- **Forecast:** Strature puts a 63% probability on a short roll-over of the suspensions and spells out what happens if they lapse [src-20261016-83adeb] (med; one forecaster).

**Why defense cares.** CSIS points out that China did about 99% of heavy rare-earth processing until 2023, and that rare earths go into the F-35, Virginia- and Columbia-class submarines, Tomahawk missiles and JDAM bombs [src-20250414-50f023].

**How big the risk is.** The IEA's critical-minerals outlook estimates that about $6.5 trillion a year of downstream economic output depends on minerals with concentrated supply chains. It also finds that planned magnet capacity outside China would meet only about a third of 2035 demand [src-20261014-b9d647].

**What it means [inference]:**
1. Any startup producing rare-earth metals, magnets, gallium or germanium in the US has a buyer of last resort in the US government and a very strong story.
2. The risk goes both ways. If China floods the market after a deal, prices collapse, as they have before. Producers need floor-price offtake contracts (the MP Materials–DoD template) or they get crushed.
3. Discovery labs also have a real pitch here: "design out" the scarce element. Examples are magnets without heavy rare earths, catalysts without platinum-group metals, and Orbital's PFAS-free fluids. This is the strongest commercial reason for materials AI right now (see section 6).

**Watch:** November 10 and November 27, 2026.

**How it works.** China makes most of the world's magnets and refines most critical minerals (section 2.2). On ordinary commercial parts it is usually cheaper. The split that matters is protected versus open markets.
- **Protected markets (defense).** Defense buyers are barred by DFARS (defense purchasing rules) from buying from a "foreign entity of concern", so price against China does not decide the sale [src-20250429-6f9155]. ITAR (an export-control law) keeps defense work onshore too. **Claim (Ed Mehr, Machina CEO):** "if you go head-to-head with China ... you're losing", so Machina starts in defense, which "won't source from China" [src-20260622-7846f9].
- **Open commercial markets.** **Claim (Belosic):** SendCutSend can "meet or beat China" on only about 20-25% of its work [src-20260519-2d6ceb]; customers "shop with their wallet" and will offshore "when the price is half" [src-20251002-6a5afd]. An ex-Anduril hardware lead says Taiwan is 20-30% cheaper and Vietnam and Malaysia cheaper still, even with tariffs [src-20250709-43486e]. Counter-claim: Isembard says it beat Chinese shops "on speed and cost" for a jet-engine customer (unnamed) [src-20260909-b547c7].
- Commercial buyers do pay for "insurance": the 2021 chip shortage showed a few hundred dollars of parts can stop an $80,000 car (**Claim, Vulcan CEO**) [src-20250429-6f9155].
- **What this means [inference].** Defense is the protected lane where US producers can win. In commercial work they win only where speed or supply security matters more than price.

**Stage B, metals detail.**

- **Section 232 metals tariffs:** Proclamation 11021 (April 2026) set 50% on steel, aluminum and copper, 25% on derivative products and 15% on some industrial machinery. A June 2026 proclamation adjusted them further [src-20260602-b995e2].
- **Input-cost inflation:** ENR reports construction material prices up 55.5% since February 2020. Steel mill products are up about 86% and copper wire about 91.4%. Tariff-exposed materials pushed input prices higher in early 2026 [src-20260302-477c5f][src-20260708-da5010].
- **Energy:** ENR also notes an energy-price spike tied to the Iran conflict [src-20260708-da5010].
- **What it means [inference]:** tariffs help a US producer by making imported parts dearer. They hurt by raising the cost of the steel and aluminum it buys and the machines it installs. The net effect is positive for finished parts (fabrication, machining) and mixed for anyone who buys a lot of metal and sells into price-sensitive markets. Tariffs can also be reversed overnight, so a model should never assume they last.

**How it works.** Section 232 (a 1962 law letting the President set tariffs for national security) raised steel and aluminum tariffs from 25% to 50% in June 2025. Since April 6, 2026: 50% on goods made almost entirely of steel, aluminum or copper; 25% on goods that contain them; 10% if the metal was melted in the US. Grid equipment gets 15% until 2028 [src-20260402-1b5d6c].
- Who wins and loses: Nucor (a steel mill) cites the tariffs for fewer imports; its gross margin rose to 20% from 14%, though about 1.3 points came from a one-off refund. Its own fabrication unit reported "margin compression" from costlier steel [src-20260812-77d6f5]. Reliance (a metals distributor) says aluminum prices are "historically elevated largely due to" the tariff [src-20260728-ae7dea].
- **What this means [inference].** Tariffs help metal makers and hurt metal buyers, including fabrication startups. The 10% vs 25% gap rewards suppliers who can prove where their metal was melted, which favors software-native firms.

**Inputs inside weapons and data centers.**

- **China's dependence, inside US weapons.** **Claim (Power):** of about 1,000 components in a Navy missile, "probably 150" come from China; about 70% of drone components come from China or Taiwan [src-20260610-779f8b]. China produces 56% of world castings, and the Pentagon relies on a single US foundry for large titanium parts (General Catalyst thesis) [src-20240202-8c6d3b]. China makes over 90% of rare-earth magnets; the US under 1% [src-20250429-6f9155].
- **Demand from AI data centers.** An AI campus can need up to 50,000 t of copper and 200,000 t of steel; steel prices rose 25% in a year (Robeco) [src-20261007-a642ea]. A legacy fabricator building generator enclosures for Amazon, Google, Apple and Meta has "backlogs working on 2027" (**Claim**) [src-20261022-4234b3]. Bear: AI capex is estimated at 3.63% of GDP, above the railroad boom's 2.24%, and most hyperscalers have near-zero free cash flow [src-20261015-c425a9]. If AI spending slows, this demand pocket shrinks [inference].

**Government lending and minerals orders (detail in 2.4):** the OSC, EDF and DPA Title III loans listed in 2.4 are mostly minerals deals (Energy Fuels, Phoenix Tailings, MP Materials) [src-20260618-184e0c][src-20260807-110c13].

### 3.7 How the industry and its supply chain work

- **Stage A, finding and mining:** explorers find a deposit and drill it out; the project is usually sold to a miner, which mines and concentrates the ore (crushing and separating the useful mineral).
- **Stage B, refining and making metal:** concentrate is refined to a pure oxide, carbonate or cathode, then smelted or melted into alloys, magnets, powders and mill products, which go to service centers and parts makers (chapter 4) or battery, chemical and materials plants (chapters 5 and 6).
- **Buyers:** miners (for deposits), metal makers, magnet makers, battery makers, primes, the DoD stockpile and traders. Prices are set on global exchanges or in China, so a US producer is a price-taker unless it has a floor-price offtake [inference]. Incumbents: Nucor (mills), Carpenter (specialty alloys), MP Materials (magnets).
- **Policy detail:** see 3.1 and the tracker in section 11.

- **Who:** Mariana Minerals (copper, lithium; runs its own mines) [src-20260803-30e6d5]. Vulcan Elements (NdFeB, i.e. rare-earth, magnets) [src-20251103-ee9b27]. Candidates: Hertha (iron and steel), Cyclic, Mass Magnetics, Duranium. Established players: Reliance, Ryerson, Nucor, MP Materials.
- **How it makes money:** a "service center" buys metal in bulk, cuts it and resells it. Gross margins run about 18-32%: Ryerson 17.7% (Q2 2026) [src-20260729-407fd7]; Reliance 27.9% or 31.6% depending on inventory accounting (LIFO or FIFO) (Q3 2026) [src-20261021-16bb64]. Refining margins: no data.
- **What AI changes:** **Claim (Mariana):** its software halves project timelines that normally take 5-10 years [src-20260803-30e6d5]. Its mine is about 50% autonomous, with AI agents (reinforcement learning, "RL") adjusting the process every 15 minutes [src-20260623-d1790b].
- **Risks:** metal prices swing; permits are slow; buyers are concentrated (Vulcan sells mostly to government) [src-20251103-ee9b27].
- **What this means [inference]:** government support is strongest here (OSC loans, tariffs, IEA finance).

**Market size (this industry).** No free source sizes US refining or exploration. Public money committed to minerals: $65B in 2025 [src-20260716-6a06e4] (high). US refining TAM is a gap.

### 3.8 Where AI and automation help

**Stage A:** AI targeting of where to drill (Earth AI) and ore-body modeling. **Stage B:** process control of refineries (AI agents tuning a plant), recipe and process tuning for magnets and alloys, faster engineering and permitting documents. **Claim (Mariana):** MarianaOS combines capital-project, mine and refinery software; its first plant runs about 50% autonomously [src-20260803-30e6d5][src-20260623-d1790b].

### 3.9 Right to win, unit economics and data loop

**Right to win:** Stage A, owning claims and drills so a discovery's value stays in-house; Stage B, a permitted, financed plant outside China plus software that shortens build and ramp. **Unit economics:** cost per ton, recovery and exploration cost per discovery are undisclosed for every startup [gap].

**Data loop (score 0–3; scale in 2.13):**

| Company | Score | How the loop works | Best evidence / what is missing |
|---|---|---|---|
| Mariana | 2 | AI agents retune the refinery every 15 minutes | [src-20260623-d1790b]. Missing: recovery or cost per ton |
| Vulcan | 1 | Test data feeds recipe models | [src-20250811-e7cb9a]. Missing: any number |

### 3.10 Companies, grouped by label

#### Stage A — Finding and mining

#### Earth AI (mineral exploration; hybrid; owns claims, drills, sells deposits)

**What it does.** Earth AI uses its own AI targeting software to pick where minerals are likely to be in poorly explored ground, then drills those targets with its own low-cost drill rigs. **Claim (Earth AI):** drilling at about $100 a meter, a 75% discovery success rate against an industry estimate of about 0.5%, and exploration costs up to 80% lower [src-20250127-c28430]. It is now building its own assay labs because outside labs left it about 7,000 meters of samples behind; the goal is results in five days instead of five months. It will still use third parties to validate a discovery before any sale [src-20260429-1bdb70]. Founded in 2017; projects are in New South Wales and the Northern Territory, Australia [src-20250127-c28430][src-20250326-5929b8].

**Business model.** It owns most of its ground: the Kooranjie (NSW) and Elkedra (NT) tenements are 100% Earth AI-owned [src-20250326-5929b8], and Willow Glen is its own molybdenum-gold project [src-20241220-f860e9]. At Fontenoy it started in an alliance with ASX-listed Legacy Minerals, earning up to a 3% royalty for a discovery while Legacy kept the licences [src-20221213-5d9521]; in October 2024 it agreed to take 80% of the project in exchange for A$4.5M of development work [src-20241121-ac9f37]. The plan is to prove a deposit and then sell the mining rights to a larger miner, keeping a small stake or royalty [src-20241121-ac9f37]. **Claim (CEO Roman Teslyuk):** a "mega mine" it would keep and pay a contractor to mine; it may also sell offtake early and direct material to the US, or sell projects to new critical-mineral funds; it expects projects to sell for about 5% of the metal in the ground and runs a portfolio of about 30 projects like a venture fund [src-20251001-cf441c].

**Funding.** $20M Series B in January 2025, led by Tamarack Global and Cantos Ventures, with Overmatch, Alpaca, Sparkwave, Y Combinator and Scrum Ventures [src-20250127-c28430].

**Discoveries reported (all company releases unless noted).**
- **Fontenoy (palladium–platinum–nickel), 2024:** announced with its listed partner Legacy Minerals as "one of the largest palladium mineral systems in Australia," with mineralization across about 2 km² (claim) [src-20241121-ac9f37].
- **Willow Glen (gold), Dec 2024:** 650 m drilled, seven gold intercepts at about 1.14 g/t; size not yet known [src-20241220-f860e9].
- **Kooranjie and Elkedra, Mar 2025:** six surface prospects, up to 0.26% tungsten (Kooranjie) and 0.39% cobalt and 1.39% copper (Elkedra) from rock-chip samples, before drilling [src-20250326-5929b8].
- **Kooranjie (indium), 2025:** rock chips up to 117 ppm indium on a 250 m outcrop (low) [src-20250601-b499c3].

**How vertically integrated: hybrid.** It owns the targeting software, the drill rigs, soon the lab, and most of the claims, so it controls the whole exploration loop and its data. It does not mine, refine or sell metal; it plans to sell deposits. It fits Stage A as an owner of exploration assets, not as a producer [inference].

**Why it matters for the thesis [inference].** Owning the claims means a discovery's value stays with Earth AI, unlike an exploration-software vendor that is paid per study. Owning drills and labs makes the data loop faster (target → drill → assay → retrain).

**Bear case.**
- **No defined resource yet.** In the free sources found, no formal resource estimate (such as a JORC report) is published for any project; rock chips and a few drill intercepts are not a mine [inference; gap].
- **The 75% success rate is the company's own metric** and is not defined or independently checked [src-20250127-c28430].
- **The assets are in Australia,** so they add to US supply only through offtake or ownership choices [inference].
- **The exit is a project sale,** at about 5% of the metal's value by the CEO's own estimate; most of the value of a mine accrues to whoever builds it [src-20251001-cf441c].
- **Exploration is a long, cash-hungry lottery;** timelines from discovery to mine run a decade or more (3.2).
- **Competition** from far better-funded AI explorers, notably KoBold Metals [inference; not sourced this run].

**Next step [inference].** Ask for drill results at Fontenoy, a timeline to a formal resource estimate, how "success rate" is defined, and which buyers or funds it has spoken to.

#### Mariana Minerals (mining and refining; fully integrated; fits)

- **What it does:** builds and runs mines and refineries (Copper One, Lithium One) on its own software [src-20260803-30e6d5].
- **Money:** $310M Series B (Khosla), about $400M including project money; valuation undisclosed [src-20260803-30e6d5]. A $1.5B figure appears only in Harmonic (low).
- **Operations:** about 250 staff, about 20% in software and AI [src-20260623-d1790b]. **Claim:** took over a southeast Utah copper mine and refinery at end-2025 and restarted mining in May 2026, about 50% autonomous, making 99.99% pure copper; "we do not sell software" [src-20260623-d1790b][src-20260513-bdc044]. **Claim (CEO Caldwell):** 30% lower refining cost and 40-50% lower mining cost [src-20260502-21f16a]; 10 projects in 10 years [src-20260513-dd56eb]. No buyer contracts disclosed. **Claim (co-founder Lozano, Oct 24):** most mine capex comes from project investors separate from VC; East Texas lithium goes to an unnamed battery maker, ramping next year; two projects today; autonomy partly through partner firms [src-20261024-c53370].
- **What this means [inference]:** one of two names with a credible data loop; the check size is above SPC's.
- **More specifics (from all sources):** The prior operator shut the Utah mine in 2024 partly for lack of haul-truck drivers; autonomy is bought in from Sandvik and Pronto [src-20260502-21f16a]. Target: 50,000 t of copper a year by 2030 versus about 2,500 t under the prior operator [src-20261011-e2426c]. Headcount rises from the prior peak of ~130 to ~300 despite autonomy, due to more output (**Claim**) [src-20260813-1fe8a2].
- **Oct 26 podcast (formerly 0A; all company claims, agent transcription):** Mariana has four software suites and retrofits autonomy onto equipment partly through partner firms. VC funds R&D while most mine capex comes from separate project investors. East Texas lithium goes to an unnamed battery company and ramps next year. It has two projects today against a goal of 10 [src-20261024-c53370].

#### Stage B — Refining and making metal

#### Vulcan Elements (magnets; fully integrated; fits)

- **What it makes:** rare-earth magnets; a 10-ton pilot in Durham and a 10,000-ton plant planned [src-20251103-ee9b27].
- **Money:** $65M Series A (Altimeter) [src-20261010-8e6ec0]. A $1.4B package: $620M loan from the Pentagon's OSC, $50M Commerce Department equity, $550M private [src-20251103-ee9b27]. Form D filing shows $430.7M sold [src-20260402-c8e4dc].
- _More detail: Appendix D (Vulcan Elements)._

**Mariana's refinery (cross-reference).** Mariana also refines what it mines; its refinery and MarianaOS are covered in its profile under Stage A above [src-20260803-30e6d5].

**Context names (not profiled):** Phoenix Tailings (rare-earth metal and magnet feedstock; $500M conditional OSC loan, facility due 2028) [src-20260618-184e0c]; MP Materials (incumbent; $400M DoD equity) [src-20260726-39275b]; Energy Fuels ($725M conditional OSC loan) [src-20260618-184e0c]; ReElement (Vulcan's refining partner; $80M OSC loan) [src-20251103-ee9b27]; Hertha, Mass Magnetics, Duranium (candidates). Cyclic (candidate, not sourced this run).

_Placement check:_ Earth AI explores and drills its own claims (Stage A); Mariana mines and refines copper and lithium (profiled in Stage A, refinery cross-referenced in Stage B); Vulcan makes sintered NdFeB magnets (Stage B) [src-20250326-5929b8][src-20260803-30e6d5][src-20251103-ee9b27].

### 3.11 Bear case, at equal weight

- **Both stages:** a US–China deal and Chinese price-dumping can make every Western project uneconomic overnight (3.1); the state picks champions with equity (MP Materials) [src-20260726-39275b].
- **Stage A:** commodity cycles (lithium −24%, nickel −11% in 2025) [src-20260130-ebdd5a]; ore grade, not software, sets most of the cost [inference]; Earth AI has no published resource estimate (3.10).
- **Stage B:** incumbents are winning this cycle (Nucor margins) [src-20260812-77d6f5]; tariffs can be reversed and squeeze metal buyers; magnet economics depend on subsidy and offtake, and equipment comes from China (**Claim, Vulcan CEO**) [src-20250429-6f9155]; defense orders lag budgets (Carpenter) [src-20261022-de5e6c]; Mariana has disclosed no recovery or cost-per-ton number [src-20260623-d1790b].

### 3.12 Key sources

- USGS Mineral Commodity Summaries 2026 [src-20260206-04fe3e]; USGS 2026 release [src-20260130-ebdd5a]
- IEA on refining concentration and outlook [src-20250521-c62d29][src-20261014-b9d647]
- MOFCOM controls and truce dates [src-20261019-854e22]; Ga/Ge/Sb ban and prices [src-20261027-f82d55]; CSIS on heavy rare earths [src-20250414-50f023]
- OSC loans [src-20260618-184e0c]; OSC fund finance [src-20260831-4dd3b7]; EDF [src-20260116-27c00a][src-20260804-05a6a5]; executive orders [src-20250320-91988a][src-20250424-a310b3]; 45X [src-20251001-45a0c1]
- Government equity stakes [src-20260726-39275b]; Strature roll-over odds [src-20261016-83adeb]; refinery build times [src-20250723-3f3ef8]
- Section 232 proclamations [src-20260402-1b5d6c][src-20260602-b995e2]; Nucor [src-20260812-77d6f5]; Carpenter [src-20261022-de5e6c]; Vulcan/OSC package [src-20251103-ee9b27]; Army drone magnets [src-20260923-c53c99]
- Earth AI [src-20250127-c28430][src-20241121-ac9f37][src-20221213-5d9521][src-20241220-f860e9][src-20250326-5929b8][src-20250601-b499c3][src-20260429-1bdb70][src-20251001-cf441c]


### 3.13 Listen & watch

Full list: Appendix E._

**Stage A — Finding and mining**

1. ★ **"Critical Minerals: Mining for the Industrial Future"**, a16z Podcast, Jul 23, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/critical-minerals-mining-for-the-industrial-future/) — *Why:* Mariana's Turner Caldwell on owning mines and refineries and using software to cut build time and cost. Repo: src-20250723-3f3ef8.
2. **"Inside Earth AI: Cutting the Cost of Critical Mineral Discovery" (S2 E57)**, Rare Earth Exchanges, Feb 26, 2026, 33 min. [▶ Open link](https://www.youtube.com/watch?v=-dQONUziAxY) — *Why:* founder Roman Teslyuk on training on 50 years of Australian drilling archives, and why few new deposits are found each year (his figures). Repo: src-20251001-cf441c.
3. **"From Y Combinator to mining, ft Earth AI's Roman Teslyuk"**, YouTube, Apr 28, 2026, 66 min. [▶ Open link](https://www.youtube.com/watch?v=KXbUJ2CjWbI) — *Why:* the longer Earth AI founder story; pair with the primer's bear case (no resource estimate yet). **Not in the repo (new).**
4. **"Critical Minerals: What Makes Mining Tech VC-Backable"**, *Deep Tech Catalyst*, with Jun Ku (Main Sequence), length not listed. [▶ Open link](https://www.thescenarionist.com/p/critical-minerals-at-venture-scale-deeptech) — *Why:* an investor on how non-dilutive government money makes heavy-capex mining fundable. Repo: src-20261022-cd6c5c.

**Stage B — Refining and making metal**

1. ★ **"How The Rarest Company On Earth Raised $75M"**, *Sourcery*, Aug 11, 2025, length not listed. [▶ Open link](https://podcasts.apple.com/us/podcast/how-the-rarest-company-on-earth-raised-%2475m/id1738124704?i=1000721503376) — *Why:* Vulcan's early demand: pilot plant opened Mar 2025 and was qualifying magnets with customers within four months (company claim). Repo: src-20250811-e7cb9a.
2. **"'Supply Chains Win Wars': Rare Earth Magnets with John Maslin"**, *Building the Base*, Apr 29, 2025, length not listed. [▶ Open link](https://buildingthebase.org/episode/supply-chains-win-wars-rare-earth-magnets-with-john-maslin-ceo-vulcan-elements) — *Why:* the magnet macro in one sitting; the gap is processing and metal-making, not ore. Repo: src-20250429-6f9155.
3. **"Energy, Minerals, and the Physical Stack Behind AI"**, a16z Podcast, May 13, 2026, length not listed. [▶ Open link](https://a16z.com/podcast/energy-minerals-and-the-physical-stack-behind-ai/) — *Why:* Mariana's refinery and plant software (the data loop inside owned assets). Repo: src-20260513-bdc044.
4. **"Advancing US critical minerals with software and autonomy"**, Benchmark Mineral Intelligence, Jun 23, 2026, 23 min. [▶ Open link](https://www.youtube.com/watch?v=OvJX0j5OPXs) — *Why:* how industry analysts see AI-run refineries. Repo: src-20260623-6dc76b.
5. *(Quick watch)* **"The Future is Metal – Mariana Minerals"**, a16z, Aug 5, 2026, 9 min. [▶ Open link](https://www.youtube.com/watch?v=uFt-tkagUUI) — *Why:* nine minutes on China's 90%+ share of refining. Repo: src-20260805-b7e3c7.

### 3.14 Commercial traction and incumbents

_Status labels: **Revenue** = paying customers or product sales; **Pilot** = pilots, LOIs, government awards or samples; **Lab** = pre-revenue. Company statements are marked **Claim**._

**Who's actually commercializing**

| Company | Sub-section | Status | Evidence |
|---|---|---|---|
| Mariana Minerals | Stage A/B (mines and refines) | Revenue-stage producer; buyers not disclosed | Restarted its Utah copper mine in May 2026, about 50% autonomous; **Claim:** 99.99% copper [src-20260623-d1790b][src-20260513-bdc044]. **Claim:** East Texas lithium goes to an unnamed battery maker, ramping next year [src-20261024-c53370]. No buyer contracts public. |
| Vulcan Elements | Stage B (magnets) | Pilot, with government buyers | Seven federal awards worth $5.7M, including an Army magnet IDIQ [src-20260710-6361ea][src-20250501-1885f8]. **Claim:** pilot output sold out 12 months ahead [src-20250811-e7cb9a]. |
| Earth AI | Stage A (exploration) | Lab / pre-revenue | No published resource estimate [src-20250127-c28430][src-20241121-ac9f37]. |
| Phoenix Tailings (context) | Stage B (rare-earth metal) | Pilot | $500M conditional loan; commercial facility due 2028 [src-20260618-184e0c]. |

**Revenue vs lab.** Real revenue today sits with incumbents in refining and magnets (MP Materials: $224.4M revenue in 2025, still a $85.9M net loss [src-20260201-0b4d7a]). Startup revenue is thin: Mariana is producing, Vulcan sells pilot volumes and federal work. AI exploration (Stage A) is pre-revenue by nature: a find earns nothing until a mine is built.

**Incumbents.** BHP, Rio Tinto and MP Materials. _What they do better:_ balance sheets, permits in hand, offtake relationships and operating know-how; MP also has $400M of DoD equity [src-20260726-39275b]. They buy AI rather than build it: BHP Ventures backs AI exploration startups [src-20261022-04e57d]; Fleet Space lists Rio Tinto among the miners using its surveys [src-20261014-84a296]. _Where startups win [inference]:_ small deposits and tailings the majors ignore, and refining or magnet steps where policy pays for a non-Chinese source.

**Regulation and qualification.** Permitting is the clock. A federal environmental impact statement (NEPA) took 4.5 years on average, 3.5 median, and a quarter took over 6 [src-20200612-38edca]. US mine permitting commonly takes 7–10 years versus about 2 in Australia and Canada; mines average 15.7 years from discovery to production [src-20240101-a81fa2], rising to 17.8 years for mines opened 2020–24 (US: 19.1) [src-20250101-3e6713]. Refinery build times: see 3.6 [src-20250723-3f3ef8]. Magnet buyers (defense, autos) then qualify the material, see 6.14.

**5-year outlook (to 2031).** _Stage B refining and magnets:_ **possible**. Vulcan and Mariana have product and government pull. _Stage A AI exploration:_ **unlikely**. Discovery-to-mine timelines run well past 2031. **Bear case, equal weight:** the subsidy-backed buyers (DoD, OSC loans) may not renew, loans are still conditional, and Chinese price cuts can strand US plants; MP is the largest US name and still loses money [src-20260201-0b4d7a].

## 4. Manufacturing

_What this industry is._ Manufacturing turns metal (and some plastics and composites) into finished parts made to a customer's drawing. We use three sub-types, in chain order, and tag every company with one:

- **Metal Supply:** buying standard metal from mills and cutting it to size for parts makers (Nox Metals). These are suppliers to the parts makers below, not raw-materials producers.
- **Fabrication (sheet/structures):** cutting, bending and welding sheet metal and plate into brackets, enclosures, frames and structures. Lower tolerance, high volume of simple jobs, fast turnaround; margin depends on machine use and material cost.
- **Precision & Defense Hardware (machining, 3D printing, castings, composites):** tight-tolerance parts for aerospace, defense and medical, made by CNC machining, additive manufacturing (3D printing), casting or composites layup. Slower, needs certifications (AS9100, NADCAP) and a first-article inspection; higher margin.

Between fabrication and precision, the difference matters because fabrication competes on speed and price for many small orders, while precision competes on qualification and trust for long-lived programs. The macro below covers both; where it differs, we say which.

### 4.1 The problem today

- **The supplier base is small, old and shrinking.** The US has 17,156 machine shops; 83% have fewer than 20 employees [src-20250626-23f6d9]. 4,874 machine shops (about 20%) were lost from 2002 to 2018 [src-20250909-29c826].
- **Buyers have consolidated.** Aerospace and defense primes fell from 51 to 5 since the early 1990s [src-20220215-45c353].
- **Parts are late.** An average aerospace part takes 8–12 weeks, and about 40% arrive late or with quality issues (med, single memo) [src-20251024-2e5383]. Castings take 9–10 months at a Raytheon supplier [src-20250708-2aa3ad].
- **Yet existing shops are underused.** The average US machine cuts metal only 34% of the time against a 70% target [src-20250120-419768]. The shortage is people, programming and process, not machines [inference].
- **Labor.** Machinists: 344,900 jobs, $59,620 median pay, a 1% decline projected to 2035 but 30,400 openings a year from retirements [src-20260901-d504f9]. Welders: 437,700 jobs, $53,750 median, 40,300 openings a year [src-20260901-3b0073]. Deloitte and The Manufacturing Institute project 3.8M manufacturing jobs to fill by 2033 with 1.9M possibly unfilled [src-20240403-f5594a].
- **Moving a part is slow by design.** A first-article inspection (AS9102) is repeated whenever the design, material, process, tool or location changes [src-20190801-e81d7b].

### 4.2 Macro and tailwinds, ranked [ranking is inference]

| Rank | Tailwind | Date / size | Structural or reversible? |
|---|---|---|---|
| 1 | **Munitions and shipbuilding demand** | FY27 request $49.5B for 10 key munitions, 8.5x the FY16–26 average [src-20261007-c6f64e]; Lockheed's 7-year deal for Hadrian cells in its missile plant from early 2027 [src-20261014-015327]; Navy $900M toward Hadrian submarine-part plants [src-20260320-67ba4c] | Structural for years; annual budget timing reversible |
| 2 | **Multi-year buying in law** | FY26 NDAA: multiyear munitions buys, Industrial Base Fund purchase commitments up to 10 years (Sec. 867), additive manufacturing (Sec. 1842) [src-20251218-f0d6ef] | Statute, but needs appropriations |
| 3 | **Tariffs on imported parts** | 25% on goods containing steel, aluminum or copper since April 6, 2026 [src-20260402-1b5d6c] | Reversible by proclamation or court |
| 4 | **Reshoring and data-center demand** | Fabricated-metal shipments ~$490B in 2025, up from ~$472B in 2023 (sums of monthly Census data) [src-20261002-dedd62]; a fabricator for hyperscaler generator enclosures has "backlogs working on 2027" (**Claim**) [src-20261022-4234b3] | Partly cyclical |
| 5 | **Cheaper robots and better software** | Industrial robot installs worth $18.6B globally; 38,428 US installs [src-20260924-28b59b]; 100% bonus depreciation restored [src-20260114-2075f7] | Structural (tech); tax treatment reversible |
| 6 | **Additive gets real** | 3D-printing market $21.9B in 2025, +9.1% [src-20250325-4c256c]; one Navy boat has 100+ printed critical parts and $200M+ Navy spend [src-20250319-f21bec] | Structural; growth is Asia-led |

**The defense supplier base, in numbers.** DoD relies on more than 200,000 suppliers and has little view below the first tier: its supply-chain tool holds country-of-origin data for fewer than 10% of F-35 sub-tier suppliers. F-35 production stopped for about six months in both 2023 and 2024 because of Chinese magnet content. For more than half of 99 materials in shortfall (FY23) there was no domestic maker. DoD put about $6.5B into 828 industrial-base projects (DPA Title III, IBAS, ManTech) in FY20–24; castings and forgings are one of eight priority areas; 155mm shell output is planned to rise from 168,000 to 1.2M a year [src-20250724-1c09ad]. At the top, primes fell from 51 to 5 [src-20220215-45c353]. _Meaning [inference]:_ the bottleneck is thousands of small sub-tier shops nobody tracks, which is where a new owner-operator can enter.

**Reshoring, in numbers.** Companies announced about 247,000 US manufacturing jobs from reshoring and foreign direct investment in 2025, near 2024's level; 2.3M since 2010; about 309,000 projected for 2026, possibly 400,000. Only 14 of 64 conditional (tariff-linked) announcements had converted by mid-2026. 90% of jobs are high- or medium-high-tech; contract manufacturers quoting reshored work rose from 16% to 33%; 57% cite policy uncertainty as the top concern (med) [src-20261023-986299]. _Meaning [inference]:_ demand for domestic parts is real but announcements run ahead of orders; startups should count purchase orders, not pledges.

**Shipments and welders.** US fabricated-metal shipments rose from $471.5B (2023) to $479.8B (2024) and $490.4B (2025) [src-20261002-dedd62]. Welding has 437,700 jobs, median pay $53,750, and about 40,300 openings a year, mostly to replace retirees [src-20260901-3b0073]. _Meaning [inference]:_ demand grows slowly but steadily, while replacing retiring workers is the binding constraint, which is where automation pays.

### 4.3 Headwinds, at equal weight

1. **Spare capacity already exists** (34% utilization) [src-20250120-419768], so primes can push work to existing shops.
2. **Imports are cheaper.** Taiwan is 20–30% cheaper and Vietnam/Malaysia cheaper still [src-20250709-43486e].
3. **Qualification is slow** (9–12 months at Raytheon) [src-20250708-2aa3ad], and the Navy calls it "an adoption problem" [src-20250319-f21bec].
4. **Tariffs raise input costs**; Nucor's own fabrication unit saw margin compression [src-20260812-77d6f5].
5. **Rates and construction.** Fed 3.75–4.00% [src-20260916-f0c016]; manufacturing construction down 21.9% y/y [src-20260708-da5010].
6. **Automation saves less than it sounds.** **Claim:** labor falls from 100 to 30–50 hours a part, but net saving after machine costs is 20–30% at best [src-20250712-e5e110]. Robot-learning success rates in real tasks are 59–66% [src-20260904-267293].
7. **Payment terms.** Small suppliers face about 300-day payment terms (**Claim, Power**) [src-20260908-65fab6].

### 4.4 Why an AI-enabled, vertically integrated company is the answer here

- **Versus job shops:** they lack capital, software and successors (**Claim, Isembard:** the average owner is over 65 and 40% plan to retire within five years [src-20260310-45bab3]). A new owner-operator that automates quoting, CAM programming and inspection can run machines more hours with fewer machinists [inference].
- **Versus marketplaces (Xometry-style):** a network cannot guarantee quality or capacity; owned factories earn more (Proto Labs 49% gross margin in own factories versus 31% for its network) [src-20260206-8bb619][src-20260206-2b13c7].
- **Versus software sold to shops:** shops buy slowly and the vendor never owns the margin [inference].
- **Versus imports:** defense rules and tariffs favor US supply.
- **Fabrication vs precision:** in fabrication the edge is speed and price on many small orders (**Claim, SendCutSend:** 48-hour delivery); in precision it is qualification, data on every part and long contracts [inference].
- **Where it breaks [inference].** If primes keep using existing shops, or qualification stays slow, a capital-heavy new factory sits idle; automation savings may not cover machine and financing costs.

### 4.5 What would have to be true, and signals to watch

- Primes sign multi-year contracts with new suppliers. **Watch:** more Lockheed-style deals; Sec. 867 purchase commitments.
- Plants run well above 34% utilization. **Watch:** any disclosed utilization or gross margin from Hadrian, Isembard, Senra.
- Qualification gets faster. **Watch:** first articles passed per quarter; Navy approvals of printed parts.
- Debt, not equity, funds plants. **Watch:** equipment loans and OSC loans to parts makers.

### 4.6 Macro in more depth

**Defense demand and the sub-tier.**

- **The munitions gap, in numbers.** **Claim (Power):** the US buys about 100 Tomahawks a year, versus about 850 fired in one day in the Iran conflict; Ukraine used three years of missile inventory in about six weeks [src-20260908-65fab6]. Lockheed has $60B+ of Pentagon deals to triple PAC-3 output from about 600 to 2,000 a year (trade press) [src-20261015-86f700].
- **Who really makes defense parts.** **Claim (Power):** 60-80% of a prime's output comes from small-business suppliers, which face payment terms of about 300 days which makes them hard to finance [src-20260908-65fab6]. The F-35 relies on "7,100 mom and pop shops" (**Claim, Nox CEO**) [src-20261022-3135b5]. The NDIA's president (ex-Pentagon) says sub-tier suppliers run batches "of 10 or 20", and their real question is "will you keep buying them from me", which is why five-year purchase guarantees matter [src-20260901-a44eee].
- **The US lost its machine-tool industry.** US machine-tool shipments fell from $5B (1981) to $2B (1983); half of US machine-tool firms closed in 1982-87; imports rose from about 10% to about 60% by the late 1990s [src-20240118-4e5ac1]. So even AI-native US factories buy German, Japanese or Italian machines [src-20260310-f52a8d].

**How a buyer actually buys a part (procurement path).**

This is the most important mechanism to understand. A new producer does not win "the market." It wins one part number at a time, at one buyer at a time.

1. **Request for quote (RFQ).** A buyer at a prime sends a drawing and asks suppliers for a price and delivery date.
2. **Supplier qualification.** Before a new supplier can make flight or weapon parts, the buyer checks its quality system. The common standard is **AS9100**, the aerospace quality management standard. Special processes (heat treating, coatings, inspection) need **NADCAP** accreditation. Buyers told us qualification takes 9-12 months at Raytheon [src-20250708-2aa3ad] and 1-2 years at Northrop [src-20260802-36d46c].
3. **First article inspection (FAI).** The supplier makes the first part. Every dimension, material and process is checked against the drawing and written up in a standard report (AS9102). FAI is repeated whenever the design, material, process, tool or location changes, or after two years without production [src-20190801-e81d7b]. _This is why moving a part to a new supplier is slow and costly._
4. **Prototype and low-rate production (LRIP).** Small quantities, often under fast contracts such as **OTAs** (Other Transaction Agreements, which skip much of the normal federal acquisition rulebook and can roll into production without a new competition) [src-20241219-9f8fcc].
5. **Rate production.** Steady, high volume. Here price per part and consistent quality decide who wins. A Boeing executive says at around 1,000 parts a traditional shop is cheaper than Hadrian [src-20260908-ed94f0].
6. **Repeat orders and multiyear contracts.** The prize. Programs can last about 50 years, and suppliers for a 2035 aircraft are being chosen now [src-20260818-9b2d5c]. The FY26 NDAA (National Defense Authorization Act, the yearly defense policy law) now allows multiyear buying for SM-6, Tomahawk, AMRAAM, JASSM, LRASM and PAC-3 missiles [src-20251218-f0d6ef].

**Two rules that limit any one supplier.** Buyers cap how much they depend on one shop (SpaceX caps a shop at about 1/3 of its revenue) [src-20250708-342eaf]. After a factory fire at a major supplier, Boeing says it "will never" put one part family with one supplier again [src-20260818-9b2d5c].

**What this means.** Early wins are fast prototype work that buyers pay a premium for. The test of a real business is whether those wins turn into repeat rate-production orders. That is exactly Lilly's question 1, and the evidence so far is thin (section 9) [inference].

### 4.7 How the industry and its supply chain work

- **Who:** SendCutSend [src-20260519-38c7ed]; Senra (wire harnesses, the bundled cables inside machines) [src-20260701-027c1b]; Machina Labs (robots that shape sheet metal) [src-20260204-ce7053]; 1872 (robotic steel fabrication) [src-20260722-985690]. Atomic Industries (AI-designed injection molds plus its own molding presses; section 4.10) [src-20261027-b51989]. Candidate: Advanced Metal Research.
- **How it makes money:** SendCutSend has been profitable for eight years [src-20260519-38c7ed]. Revenue is about $140M a year per a since-deleted post (low) [src-20260504-c3ded5], or "nine digits" per Sequoia's Reed [src-20261020-487a39] (med).
- **What AI changes:** instant online quotes, and software that packs many customers' parts onto one metal sheet ("nesting"). **Claim (Senra):** quotes in about a day and 99% first-pass yield (FPY: parts that pass inspection the first time) [src-20260701-027c1b].
- **Risks:** works for small batches, not mass production. Machina takes 30 minutes to hours per part; a stamping press takes seconds [src-20261023-c3b62f].
- **What this means [inference]:** the best layer for capital-light owner-operators, but volume is capped.

CNC means computer-controlled cutting machines. "AM" (additive manufacturing) means industrial 3D printing.
- **Who:** Hadrian [src-20260807-b0dc5b]; Divergent [src-20250915-311606]; Isembard (franchise network) [src-20260909-b547c7]; Freeform (metal 3D printing) [src-20260219-2125d7]; Amca (buys and upgrades old shops) [src-20260520-af3e6c]; Fabri (castings) [src-20260617-4dfb96]; Layup (composites) [src-20260602-a7b79e]; Hybron [src-20260413-abc797]. Established players: Howmet, PCC, ATI, Carpenter, Proto Labs, Xometry.
- **How it makes money:** Proto Labs' gross margin was 44.5% in 2025 [src-20260206-8bb619]: 49% from its own factories versus 31% from its partner network [src-20260206-2b13c7]. Xometry (an online marketplace) earns 34.7% [src-20260224-a7b149]. Howmet's engine unit earns 37.7% before interest, tax and depreciation (EBITDA) [src-20260806-9a83f7]. **Claim (Rolls-Royce engineer):** small shops aim for low double-digit margins [src-20251120-0c271b]. **Claim (ex-Hadrian programming head):** a typical shop can go from 15% to 30% margin in 12-18 months with Hadrian-style operations [src-20261004-9b47f5].
- **What AI changes:** **Claim (Raytheon manager):** Hadrian quoted about 50% lower prices at about a third of the lead time [src-20250708-2aa3ad]. Other buyers disagree (section 9).
- **Risks:** buyers must approve each new supplier. That takes 9-12 months [src-20250708-2aa3ad] or 1-2 years at Northrop [src-20260802-36d46c]. (AS9100 is the aerospace quality standard; NADCAP certifies special steps like heat treating and NDT, non-destructive testing.) The leader is valued at $7.87B, out of SPC's range [inference].
- **Failures in this exact model:** Daedalus, an AI-run CNC factory in Germany with a $21M Series A, went insolvent in August 2026 [src-20260801-4532f6][src-20251203-fc28ea]. VulcanForms replaced its founder CEO [src-20240919-72efcc], then raised $220M [src-20260130-365541]. An ex-Hadrian engineer: a six-machine first factory cost "well north of $10 million", and "manufacturing is not actually a fantastically profitable business" [src-20260817-8867f2].
- **What this means [inference]:** the biggest and most contested layer; the top names are already expensive.

**Market size (this industry).** Machine shops: 17,156 sites, 223,313 workers, $14.23B payroll; 83% have under 20 staff (2023) [src-20250626-23f6d9] (high). Precision parts: about $71B by 2026, machine shops over $60B (one analyst memo) [src-20251024-2e5383] (med). Structural and architectural metal: 14,533 sites, 423,013 workers, $28.26B payroll [src-20250626-23f6d9] (high). Fabricated-metal shipments about $490B in 2025 [src-20261002-dedd62]. No free revenue number for fabrication alone. Metal service centers (Nox's market): about $200B of revenue across about 9,400 sites; the top 50 firms hold about half (2025) [src-20251201-4b732d] (med).

### 4.8 Where AI and automation help

Instant quoting, automated CAM programming, scheduling, in-process inspection and robot welding/forming. See the company data-loop rows below; the general case is in 7.6 and 2.13.

### 4.9 Right to win, unit economics and data loop

_More unit-economics inputs: Appendix D._

**Data loop (score 0–3; scale in 2.13):**

| Company | Score | How the loop works | Best evidence / what is missing |
|---|---|---|---|
| Freeform | 2 | Cameras on the molten metal adjust each printed layer live | [src-20241024-7f1c2e][src-20260219-2125d7]. Missing: yield or cost trend |
| Hadrian | 2 | Opus software for workflow, programming and quality checks | 30-40 day training [src-20260926-70087f]; 25-75% shorter cycle times at a studied shop and a 50% cut in order-to-first-part time in about two years [src-20261004-9b47f5]. Missing: it relies on outside CAM software [src-20261004-9b47f5] |
| Divergent | 2 | Design software feeds printer, then assembly | 600+ part numbers [src-20250915-311606]. Missing: cost-per-part trend |
| Senra | 1 | Amp standardizes inputs, guides technicians, tracks materials and design changes [src-20260715-68183e] | 99% FPY claim [src-20260701-027c1b]. Missing: before and after |
| SendCutSend | 1 | Instant quoting at volume | 32,000 orders a month [src-20260525-4a12ab]. Missing: any learning metric |
| Isembard | 1 | MasonOS quoting across franchises | Claim: 40-60% more output [src-20250929-857f17]. Missing: outside proof |
| Machina | 1 | Robot forming learns each new shape | Claim: 50x lead time [src-20261022-ca4c7a]. Missing: cycle-time trend |
| Nox | 1 | Auto-nesting and quote-time estimates | [src-20260325-5b68db]. Missing: scrap rate |
| 1872 | 0 | The welding AI belongs to Path, not 1872 | [src-20260722-3bc2d8]. Missing: everything |

### 4.10 Companies, grouped by label

#### Metal Supply

#### Nox Metals (metal distribution; fully integrated; we passed)

- An automated metal distributor outside Detroit with nesting software [src-20261009-404b9b]. $11.5M seed (Hyperion) [src-20260616-1cf7cb]. About 12 people at one site [src-20260325-5b68db]. Its founder's "controversial belief" is "raw capacity over everything else" [src-20260427-83b102].
- **More specifics:** Nox: 46 people, 250-300 customers, 75,000 sq ft (**Claim**) [src-20261009-404b9b]; instant quoting is easy with a 50% buffer, the hard part is beating a human estimator [src-20261022-3135b5].

_Sub-type: metal supply / service center._

#### Fabrication

#### SendCutSend (fabrication; fully integrated; fits, benchmark)

_Sub-type: fabrication._

- **What it makes:** laser-cut sheet metal, CNC parts and finishing, ordered online with an instant quote. Owns all its plants (Reno; Paris, KY; Arlington, TX) [src-20261020-487a39].
- **Money:** $110M at a $1.01B valuation, May 2026, its first outside round [src-20260519-38c7ed]. Series B at $2.1B led by Spark, October 2026, size undisclosed [src-20261020-487a39] (med, one trade write-up).
- _More detail: Appendix D (SendCutSend)._

#### 1872 (fabrication; fully integrated; fits)

_Sub-type: fabrication._

- **What it makes:** steel skids, frames and enclosures for energy and utilities, using AI and robots, in Cincinnati [src-20261022-fdbf29].
- **Money:** $15M seed via Ohio's O.H.I.O. Fund [src-20260722-985690].
- _More detail: Appendix D (1872)._

#### Senra Systems (wire harnesses; fully integrated; fits)

_Sub-type: fabrication (electrical assembly; not metal, closest fit)._

- **What it makes:** wire harnesses and cable assemblies for defense and space, in its own plants (about 95,000 sq ft, two sites) [src-20260701-027c1b].
- **Money:** $65M Series B, July 2026 [src-20260715-68183e].
- _More detail: Appendix D (Senra Systems)._

#### Machina Labs (robotic sheet forming; hybrid; partial fit)

_Sub-type: fabrication._

- **What it makes:** robots that shape sheet metal without molds ("RoboCraftsman"), plus machining and welding. Runs its own plants and places cells with customers [src-20260204-ce7053].
- **Money:** $124M Series C, February 2026 [src-20260204-ce7053].
- _More detail: Appendix D (Machina Labs)._

#### Precision & Defense Hardware

#### Hadrian (precision parts; hybrid; fits mostly, benchmark)

_Sub-type: precision._

- **What it makes:** machined parts in automated CNC factories run on its "Opus" software. Now also runs cells inside Lockheed's plant [src-20261014-015327].
- **Money:** Series C $260M (equity plus debt), July 2025 [src-20250721-d99a2a]; about $1.6B valuation in January 2026, then $1.37B Series D at $7.87B in August 2026 [src-20260807-b0dc5b]; a $360M bank credit line [src-20260817-c48f28]. About $2.24B raised in total [Harmonic].
- _More detail: Appendix D (Hadrian)._

#### Isembard (precision parts; hybrid franchise; partial fit)

_Sub-type: precision._

- **What it makes:** machined parts in owned and franchised factories, all on its "MasonOS" software; US, UK, Germany, France, Ukraine [src-20260310-45bab3].
- **Money:** $9M seed plus $50M Series A led by USV, March 2026; valuation undisclosed [src-20260310-45bab3]. Harmonic estimates about $250M (low).
- _More detail: Appendix D (Isembard)._

#### Freeform (metal 3D printing; fully integrated; fits)

_Sub-type: precision._

- **What it makes:** metal 3D-printed parts using AI-controlled multi-laser printers. It sells parts, not printers [src-20241024-7f1c2e].
- **Money:** $67M Series B, February 2026; PitchBook puts it at $179M after the round [src-20260219-2125d7] (med); about $126M raised.
- _More detail: Appendix D (Freeform)._

#### Divergent (printed structures and munition airframes; fully integrated; fits, benchmark)

_Sub-type: precision & defense hardware._ Website: divergent.us (the old divergent3d.com no longer works).

**What it does.** Divergent makes metal structures for missiles, aircraft and cars with its own system, DAPS: software-defined design, its own metal 3D printers, and robotic assembly without fixed tooling [src-20260617-9683d4]. Its new printer, Monolith One (24 kW, 12 lasers), is built in-house and is not sold or licensed to anyone [src-20260617-9683d4]. It sells parts per unit with a low start fee ("factory-as-a-service") and does not license its technology [src-20260222-9c80a9]. **Label: fully integrated:** it owns the design software, the printers, the alloys, the factory and the assembly.

**Defense traction.**
- **Tomahawk:** contracted by Raytheon as a second source for the Tomahawk midbody; first prototypes are done and production is aimed for the first half of 2027. The Raytheon–Pentagon contract still waits on the FY2027 budget [src-20260601-976843].
- **L3Harris:** teaming agreement (Oct 13, 2026) to use Divergent's printing for the Red Wolf and Green Wolf munitions [src-20261013-eda149].
- **Customers named:** Lockheed Martin, RTX, General Atomics, CoAspire, Saab, Triumph, Bugatti, McLaren [src-20260617-9683d4]; CoAspire work is for the Air Force's affordable-mass-missile programs [src-20260601-976843]. **Claim, CEO:** contracts with 15+ primes [src-20260222-9c80a9].

**Factory 2 (Long Beach).** 430,000 sq ft; 64 Monolith One printers over 24 months, on top of 6 in Torrance [src-20260617-9683d4]. **Claims, company:** up to 30,000 missile airframes or 60,000 warhead casings a year, 8x more output, about 2x the throughput of other printers [src-20260617-9683d4][src-20260601-976843]. About 80% of the factory is driven by defense volume (CEO) [src-20260601-976843].

**Money and growth.** $290M Series E (Sep 2025) at a $2.3B valuation; over $1B raised [src-20260222-9c80a9]. **Claims, CEO:** 2025 revenue more than 5x 2024; planned mix about 70% aerospace and defense, 30% auto over three years; unit cost at parity with high-rate casting [src-20260222-9c80a9]. About 500 staff [src-20260222-9c80a9].

**Bear case.**
- **Qualification:** aerospace parts need certification that takes years. An independent view (USC's Prof. S.K. Gupta): "Certification is a long, complicated process. That's why technology adoption has been slow"; the article adds that printing is sensitive to conditions, which could make copying the factory harder [src-20260222-9c80a9].
- **Defense budget dependence:** Tomahawk volume waits on the FY2027 budget, and Factory 2 is mostly sized for munitions [src-20260601-976843].
- **Capital intensity:** in-house printers plus a 430,000 sq ft plant are expensive to build and fill [inference].
- **Cost vs casting at scale:** parity with casting is only the CEO's claim; no independent cost data found [gap].

**Next step:** confirm the Tomahawk production start and Factory 2 printer installs in 2027.

#### Amca (buys existing shops; fully integrated; fits)

_Sub-type: precision._

- **What it does:** bought 8 certified aerospace plants and redesigns parts with its AI platform [src-20260520-af3e6c][src-20261008-149196].
- **Money:** $300M Series B at over $1B (Caffeinated, Lightspeed) [src-20260520-af3e6c].
- _More detail: Appendix D (Amca)._

#### Atomic Industries (tooling and molded parts; fully integrated; fits)

_Sub-type: precision (tooling and molding)._

- **What it does, in plain English.** Almost every plastic part (a car bumper clip, a drone shell, a subway seat bracket) is made by squirting molten plastic into a steel mold. The mold is the expensive, slow part: a skilled toolmaker designs where the cooling channels, ejector pins and plastic entry points go, then machines the steel, then runs trial shots and tweaks it, often over many weeks. Atomic uses physics simulation plus machine learning to design that mold, builds it in its own Michigan shop, and then runs the mold in its own presses to sell finished parts [src-20260130-9500f0][src-20261027-b51989].
- **Where it sits.** Detroit area (Warren and Shelby Township, Macomb County, Michigan). Founded 2019 by Aaron Slodov (software, ex-Google per TBPN), Austin Bishop and Lou Young Jr. (a veteran toolmaker, head of manufacturing); Y Combinator W21 [src-20231204-652d42][src-20260128-2b7e8b][src-20250919-2805c7].
- _More detail: Appendix D (Atomic Industries)._

**Nox vs SendCutSend, in one line.** Nox sells standard metal (plate and bar) cut to size; SendCutSend takes the customer's own design and returns a finished custom part [src-20261027-93d80b][src-20261027-82f772].

**Where the sub-sections blur.** The three boxes are a guide, not walls. Checked against each company's own website on Oct 27, 2026:
- **SendCutSend** started with laser-cut sheet (fabrication) but now also offers CNC machining, bending, welding, plating and powder coat, which overlaps Precision & Defense Hardware [src-20261027-82f772]. Kept in Fabrication because sheet cutting is its core.
- **Senra** makes wire harnesses and electrical assemblies, not metal parts [src-20261027-6834f5]. Placed in Fabrication as the closest fit (assembly to a drawing).
- **Atomic Industries** makes plastic injection-molded parts and its own molds; it says "today our focus is plastics" (**Claim, company**) [src-20261027-de288e]. Placed in Precision & Defense Hardware (tooling and molding), not metal.
- **Machina Labs** forms sheet metal with robots (fabrication) but to aerospace tolerances (precision).
- **Divergent** prints and robot-assembles whole missile, aircraft and car structures, which spans both; it sits in Precision & Defense Hardware because most new volume is munitions [src-20260601-976843].
- **Amca** buys existing component makers (sensors, bearings, hydraulics) rather than running one process; its site describes single-source critical defense components (**Claim, company**) [src-20261027-77bb69]. Placed in Precision & Defense Hardware.
- **Nox** sells cut metal only; its site lists no machining or finishing [src-20261027-93d80b], so it is a supplier to the other two boxes, not a parts maker.

**Other candidates, new entrants and failures**

Fabri: automated casting, $13.5M from RTX and Lockheed venture arms, shipping castings [src-20260617-4dfb96]. Layup: composite parts, $42M Series A [src-20260602-a7b79e]. Hybron: composite shells, $25M seed, contract floor over $100M [src-20260413-abc797]. Rangeview: castings from printed molds, $4.2M seed [src-20260923-3ab808]. Furientis: low-cost interceptor missiles, $25M seed (Benchmark) and a Pentagon OTA [src-20261006-410f77]. Firestorm: drones; moved from small research grants (SBIR) to a repeat-order contract, 19 awards worth $53.8M [src-20251022-629fc0][src-20251219-bd5788]. Re:Build: engineering and manufacturing roll-up, 12 sites [src-20261006-1212f9]. VulcanForms: metal 3D printing plus machining; CEO change, then re-raise [src-20240919-72efcc]. Incumbents are in section 7.

**What this means [inference].** Most profiles rest on company claims. Buyer calls exist mainly for Hadrian, and they are mixed.

- **New entrants worth knowing.** Helicon (composite drone frames, $16.5M): cycles of 5-15 minutes versus hours; "less than ten customers" (**Claim**) [src-20261020-c4b077]. Westmag (drone motors, a16z seed): China makes "over 30 million more drone motors and robot actuators per year than the U.S." [src-20260602-66bb0d]. Firestorm's containerized printers made "1,000 parts on the USS Essex" during RIMPAC (**Claim**) [src-20261019-34ca73]. CircuitHub (circuit boards) says it is profitable and that "90% of high-mix US EMS Assembly COGS is labor" (**Claim**) [src-20260520-09ca24]. Jeevy sends about 90% of volume to partner shops and keeps 10% in-house; SpaceX is a top customer [src-20261014-40926d]. Anduril is building a $3.7B shipyard in Maryland [src-20261017-5be775], so it is both a buyer and a competitor.

- **Failures and warnings, again.** NGP said Daedalus was doubling or tripling revenue months before its insolvency [src-20251203-fc28ea]. A drone founder: "3D printing is most definitely way high on the hype curve and very low on the efficacy curve" [src-20261022-f423ef]. Castelion: dependence on government revenue "is extremely damaging" [src-20251010-d50ea5]. Bright Machines' Lior Susan: contract manufacturing has "extremely low gross margin" [src-20240508-097e37].

### 4.11 Bear case, at equal weight

- 34% utilization at existing shops means spare capacity [src-20250120-419768].
- Imports 20–30% cheaper [src-20250709-43486e].
- Automation net savings 20–30% at best (**Claim**) [src-20250712-e5e110].
- Qualification 9–12 months [src-20250708-2aa3ad].
- Hype pricing: SendCutSend at $2.1B five months after $1.01B [src-20261020-487a39] (med).
- Failures: Daedalus insolvency (section 4.10).
- **Metal supply:** incumbents are winning (Reliance share gains) [src-20261022-1e6872]; a distributor's moat is inventory, credit and relationships; we passed on Nox (4.10).

### 4.12 Key sources

- Census machine-shop counts [src-20250626-23f6d9]; shops lost [src-20250909-29c826]; utilization [src-20250120-419768]
- Fabricated-metal shipments (Census/FRED) [src-20261002-dedd62]
- BLS machinists and welders [src-20260901-d504f9][src-20260901-3b0073]; Deloitte/MI [src-20240403-f5594a][src-20260910-b300bf]
- Wohlers 3D printing [src-20250325-4c256c]
- CRS on primes [src-20251215-98f650]; primes 51 to 5 [src-20220215-45c353]
- Lockheed–Hadrian [src-20261014-015327]; Navy $900M [src-20260320-67ba4c]; NDAA [src-20251218-f0d6ef]; NAVSEA [src-20250319-f21bec]
- Service centers [src-20251201-4b732d]; Reliance [src-20260728-ae7dea][src-20261021-16bb64][src-20261022-1e6872]; Ryerson [src-20260729-407fd7]
- Website checks (Oct 27, 2026): Nox [src-20261027-93d80b], SendCutSend [src-20261027-82f772], 1872 [src-20261027-ff001d], Senra [src-20261027-6834f5], Atomic [src-20261027-de288e], Amca [src-20261027-77bb69]
- FAI standard [src-20190801-e81d7b]; IFR robots [src-20260924-28b59b]


### 4.13 Listen & watch

Full list: Appendix E._

**Metal Supply**

1. ★ **"Just Gonna Send It Podcast: Zane Hengsperger (Nox Metals) – Ep. 13"**, SendCutSend, Mar 25, 2026, 54 min. [▶ Open link](https://www.youtube.com/watch?v=qhRV1cBG2lw) — *Why:* Nox's founder in conversation with a big customer type; why software beats old-line distributors on quoting and cutting. Repo: src-20260325-5b68db.
2. **"Reindustrializing America: Zane Hengsperger on building Nox"**, *First Builders*, Apr 27, 2026, length not listed. [▶ Open link](https://podcasts.apple.com/us/podcast/reindustrializing-america-zane-hengsperger-on-building/id1818466924?i=1000763907900) — *Why:* the detailed founder story and lean-capital bet. Repo: src-20260427-83b102.
3. **"Building NOX Metals & The Future of Manufacturing" (#430)**, *Powers Pod*, length not listed. [▶ Open link](https://www.powerspod.com/reindustrializing-america-building-nox-metals-the-future-of-manufacturing-with-zane-hengsperger/) — *Why:* Nox as the AI-run metal service center. Repo: src-20261022-3135b5.

**Fabrication**

1. ★ **"How to Build a Manufacturing Company in America | Jim Belosic, SendCutSend"**, *The Peel*, Apr 30, 2026, 1 h 32 min. [▶ Open link](https://www.youtube.com/watch?v=Zajo84R1ckI) — *Why:* a bootstrapped fabricator at about $140M run rate in eight years (company figure); the best repeat-order case study. Repo: src-20260430-9318cd.
2. **"What Everyone is Missing About Reindustrialization"**, Machina Labs, Oct 20, 2026, 55 min. [▶ Open link](https://www.youtube.com/watch?v=EiMhaHThSXk) — *Why:* Machina's and Freeform's founders on why the money is in the finished part ($57 of steel becomes a $2,000 part). Repo: src-20261020-bac9ca.
3. **"The Crisis Facing American Manufacturing"**, *Core Memory* (Ashlee Vance), Sep 26, 2026, 25 min. [▶ Open link](https://www.youtube.com/watch?v=NpvYyx2OUTc) — *Why:* a short documentary inside Hadrian and Machina Labs. Repo: src-20260926-70087f.

**Precision & Defense Hardware**

1. ★ **"How to Dominate Manufacturing in the US | Chris Power, Hadrian"**, *Relentless*, Sep 21, 2026, 1 h 19 min. [▶ Open link](https://www.youtube.com/watch?v=hmOLr_h7zTk) — *Why:* the clearest unit-economics case for owning factories; about 80% of capex is shared across programs. Repo: src-20260921-876080.
2. **"From hypercars to cruise missiles: Lukas Czinger on the future of US defense" (E2292)**, *This Week in Startups*, May 23, 2026, 1 h 46 min. [▶ Open link](https://www.youtube.com/watch?v=U5kZI86lIjk) — *Why:* Divergent's CEO on moving from cars to missile airframes and why it builds its own printers. Repo: src-20260523-b05ded.
3. **"Building the Arsenal: Speed, Scale, and Affordability"**, Air & Space Forces Association, Oct 14, 2026, 40 min. [▶ Open link](https://www.youtube.com/watch?v=r7BNP3R_TWk) — *Why:* the buyer side; Divergent's CEO on a panel about producing munitions at scale. Repo: src-20261014-47f64b.
4. *(Read or listen)* **TBPN transcript: Atomic Industries raises $25M Series A**, Sep 19, 2025. [▶ Open link](https://www.tbpndigest.com/story/2025-09-19/aaron-slodovs-atomic-industries-raises-25m-series-a-to-automate-injection-mold-manufacturing-in-detroit/transcript) — *Why:* Atomic's move from software to molds to parts; "mid eight figure" contracts (company claim). Repo: src-20250919-2805c7.

### 4.14 Commercial traction and incumbents

_Labels as in 3.14._

**Who's actually commercializing**

| Company | Sub-section | Status | Evidence |
|---|---|---|---|
| Nox Metals | Metal Supply | Revenue | **Claim:** 46 people, 250–300 customers, 75,000 sq ft [src-20261009-404b9b]; a price quote in minutes versus 3–5 days at brokers [src-20250813-5ee11b]. |
| SendCutSend | Fabrication | Revenue | About $140M a year (low confidence) [src-20260504-c3ded5]; 32,000 orders a month, growing ~100% a year [src-20260525-4a12ab]; 300,000+ customers [src-20261020-9deafa]; named customers include Zipline, Waymo, Anduril [src-20261020-c541ad]. |
| Senra | Fabrication | Revenue | Growth comes from existing customers [src-20260701-027c1b]. |
| Machina Labs | Fabrication | Revenue (paid projects) | Won't start a project unless the customer commits dollars [src-20260622-7846f9]. |
| 1872 | Fabrication | Lab / pre-revenue (no evidence) | $15M seed [src-20260722-985690]; no customer evidence found [gap]. |
| Hadrian | Precision & Defense | Revenue | $3M revenue in 2023 [src-20240815-500933]; **Claim:** "10xed revenue" [src-20250718-ac643a]; Army Red River Depot contract to Mar 2027 [src-20260318-472c29]; cells inside Lockheed's plant [src-20261014-015327]. |
| Divergent | Precision & Defense | Revenue; defense ramp is pilot | Sells parts per unit [src-20260222-9c80a9]; Tomahawk midbody second source, production aimed for H1 2027 [src-20260601-976843]; L3Harris teaming (Oct 2026) [src-20261013-eda149]. |
| Isembard | Precision & Defense | Revenue | **Claim:** 14 factories (4 owned, 10 franchised) on long-term contracts [src-20260909-b547c7]. |
| Amca | Precision & Defense | Revenue | Eight plants; bought Electrocube [src-20260212-c61f30]; **Claim:** Army Materiel Command contract [src-20261008-9941fd]. |
| Atomic Industries | Precision & Defense | Revenue (claimed) | **Claim:** "mid eight figure" part contracts [src-20250919-2805c7]. |
| Freeform | Precision & Defense | Pilot | Hundreds of parts a week, customers undisclosed [src-20260219-2125d7]; DIU OTA [src-20260901-6e197d]. |

**Revenue vs lab.** This is the most commercial industry in the primer: Metal Supply and Fabrication are revenue businesses today. Precision & Defense has revenue, but most defense volume is still prototypes and second-source qualification. Failures show the risk: Markforged and Velo3D (section 8), Daedalus insolvency [src-20251203-fc28ea].

**Incumbents.** Precision Castparts and Howmet (castings and forgings) [src-20260923-3ab808]; Protolabs ($533.1M revenue, 44.5% gross margin) [src-20260206-8bb619]; Reliance and Ryerson (metal service centers) [src-20261022-1e6872][src-20260729-407fd7]. _What they do better:_ qualified parts at volume. A buyer says for "a standard part on a 737" a Howmet or tier-two shop is more reliable [src-20260908-ed94f0]; Reliance is gaining share in metal supply [src-20261022-1e6872]. _Where startups win:_ fast quoting and low-volume, high-mix work, and new defense programs where primes need second sources (primes earn 7–12% cost-plus, so they outsource) [src-20260501-4e5b9a].

**Regulation and qualification.** AS9100 certification typically takes 6–12 months from kickoff to certificate for small and mid-size shops (low; consultant source) [src-20260101-f25186]. ITAR registration and AS9100 are table stakes for defense work [src-20250929-857f17][src-20260819-dadd06][src-20261023-58b5a8]. Part qualification at a prime then adds its own cycle; Divergent's Tomahawk work runs from prototype in 2026 to aimed production in 2027 [src-20260601-976843].

**5-year outlook (to 2031).** **Likely.** SendCutSend, Hadrian and Divergent already sell, and defense demand is pulling. **Bear case, equal weight:** defense demand is lumpy and budget-dependent (2.6); customers "outgrow" online fabricators by buying machines [src-20251002-6a5afd]; and incumbents can buy the same robots (GrayMatter rents cells to them [src-20261022-3335bd]), so the margin edge may shrink.

## 5. Chemicals

_What this industry is._ Chemicals covers companies that make and sell molecules: commodity and specialty chemicals, fuels, fertilizers and pharmaceutical ingredients (APIs and their intermediates). Engineered materials (battery cathodes, cooling fluids, alloys) and the AI discovery labs are now a separate chapter (6, Advanced Materials).

### 5.1 The problem today

- **Europe is closing plants.** About 9% of European capacity (37 Mt) is closing; plants need 80–85% utilization to pay (detail 5.6).
- **US growth is flat.** US chemical volumes are expected up only 0.5% in 2026 (detail 5.6).
- **Pharma ingredients depend on China and India.** About 46% of US generic doses depend on Chinese source materials (detail 5.6).
- **The 'valley of death' killed the last wave.** Zymergen admitted it had no commercial-scale manufacturing and its contract makers missed goals [src-20220101-9c58e3]; LanzaTech's FY2025 10-K flags substantial doubt about going concern [src-20260331-20d171]. Twelve's first plant opened years late [src-20260610-bf26af].

### 5.2 Macro and tailwinds, ranked [ranking is inference]

| Rank | Tailwind | Date / size | Structural or reversible? |
|---|---|---|---|
| 1 | **Pharma onshoring policy** | Section 232 pharma tariff (April 2026): 100% on patented drugs and ingredients, 20% with approved onshoring plans [src-20260402-ecae19]; BIOSECURE enacted Dec 18, 2025, first list due Dec 2026 [src-20260110-4db409]; WuXi AppTec on the 1260H list (June 2026) [src-20260818-489fdf] | BIOSECURE structural (statute); tariff reversible |
| 2 | **Europe's capacity exit** | 37 Mt closed, about 9% of capacity [src-20260115-ec35af] | Structural (energy costs) |
| 3 | **US feedstock and energy edge** | Cheap shale ethane; Middle East disruption raising demand for US output [src-20260615-0c9b7e] | Durable, gas-price dependent |
| 4 | **Government loans and grants** | Solugen conditional $213.6M DOE loan guarantee [src-20240613-2df5d6]; Phlow $15.9M award [src-20260721-fa5081]; On Demand Pharmaceuticals ~$35.6M federal awards [src-20250813-79a0cf]; AIRCO ~$70M DoD-related awards [src-20260526-9ebac5] | Annual budgets; reversible |
| 5 | **Defense chemicals (energetics, fuels)** | Munitions 8.5x request [src-20261007-c6f64e]; AIRCO MAD fuel systems [src-20260526-9ebac5] | Structural for the munitions cycle |
| 6 | **Cheap US gas and ammonia** | Henry Hub averaged about $3.44/MMBtu in 2025; US ammonia plants ran at about 80% and net import reliance fell to 5% [src-20260206-c8fbbc] | Durable while shale lasts |

**Pharma onshoring money, in numbers.** Since Eli Lilly's $27B API and sterile-injectables pledge in 2025, 14 big drugmakers have pledged more than $480B of US production over 4–10 years, pointing to 22 new sites and about 44,000 jobs [src-20260601-17c2d4]. CBRE counts about $600B of 2025 manufacturing-plus-R&D pledges but only about $60B tied to specific amounts and locations [src-20260210-883e2f]. In 2026 nine mid-sized firms (including Teva and Sun) pledged another $19.6B for tariff exemptions; MFN pricing deals now cover 26 companies and 89% of the branded market [src-20260701-818dbe]. The 232 regime gives 0% until 2029 to firms with pricing deals, and generics are exempt but under review [src-20260601-17c2d4].

**The state is now a buyer of APIs.** An August 2025 executive order directs HHS (ASPR) to secure a six-month API supply for about 26 critical drugs in the Strategic API Reserve, prioritizing domestic sources; the order says only about 10% of APIs by volume are US-made [src-20260701-818dbe]. Companies are donating tons of antibiotics and other APIs to it [src-20260701-818dbe].

**FDA is clearing the path for new plants.** FDA PreCheck opened February 1, 2026, drew 80+ requests in a month and picked seven facilities on June 29, 2026, including Lilly's API plant in Lebanon, Indiana and Amneal's sterile plant [src-20260629-8074e1]. It reviews a new plant before any product application, which shortens the slowest step for a new API maker [inference].

**Why it matters for startups [inference].** The big pledges mostly fund big pharma's own patented-drug plants. The gap left open is generic APIs and key starting materials (KSMs) — the 46% China-dependence number — where margins are thin and only policy (SAPIR purchases, a generics tariff, BIOSECURE) creates a buyer. That is exactly where Phlow and On Demand Pharmaceuticals sit. Watch whether equipment orders follow the pledges: CFR notes that even 15% of pledged capital going to equipment would be more than $75B of orders, which had not appeared [src-20260601-17c2d4].

**Feedstock and energy: the US–Europe gap, in numbers.** Gas is both fuel and raw material for chemicals: in Europe 62% of the industry's gas is burned for heat and 38% is feedstock, and the industry is Europe's largest industrial gas user (324 TWh in 2023) [src-20251001-7ec954]. From January to July 2026 European gas averaged €45.1/MWh (up 15.7%) against €12.5/MWh in the US (down 9%); the ratio widened from 2.8 to 3.6, and in July 2026 European gas cost more than five times US gas [src-20260915-e74614]. European gas is still about 2.5 times its 2014–19 average while US gas is only about 6% above; EU chemical capacity utilization sits at 75% and EU chemical imports fell 5.9% in the first half of 2026 [src-20260915-e74614]. _Meaning [inference]:_ this is a structural cost edge for any molecule made from gas in the US, and the reason Europe's 37 Mt of closures [src-20260115-ec35af] are not coming back.

**Ammonia and fertilizer.** The US made 14.0 Mt of ammonia (as nitrogen) in 2025 at 38 plants of 18 companies, 57% of capacity in Louisiana, Oklahoma and Texas, running at about 80%; 88% goes to fertilizer and the rest to explosives, plastics and fibers. Net import reliance fell from 13% (2021) to 5% (2025), with imports mainly from Canada (49%) and Trinidad (47%). Gulf ammonia averaged about $450 per short ton in 2025 against $1,070 in 2022 [src-20260206-c8fbbc]. _Meaning [inference]:_ the US is close to self-sufficient in commodity nitrogen, so a newcomer like Nitricity wins only on a niche (organic, local, low-carbon) rather than on supply security; prices swing more than twofold with gas, which sets the bar for any alternative.

**Oil-based feedstocks.** Brent averaged about €74.6 a barrel over the 2026 period Cefic tracks [src-20260915-e74614]; oil-based (naphtha) crackers dominate Europe while US crackers run mostly on ethane from shale gas, which is why the gas gap above flows straight into petrochemical costs [inference]. Demand growth: see 5.6. _Meaning [inference]:_ US demand is flat, so US makers grow mainly by taking export share from Europe and imports, not from a growing home market.

**Process-plant software is a related bet.** Process plants (chemicals, polymers, biologics) are the main market for Lumaril, an AI closed-loop control startup profiled as an enabler in section 7.10. If plants can raise yield through software alone, that lowers the bar for existing US plants and competes with new-build startups [inference].

### 5.3 Headwinds, at equal weight

1. **Commodities are an incumbent's game.** See 5.11 (3).
2. **Scale-up kills companies.** See 5.11 (1); Geno was sold in 2026 [src-20260812-dc968f].
3. **Green premiums are fragile.** Alaska postponed its Twelve-fuel flight over carbon intensity [src-20260901-c5f851]; e-fuels need mandates or buyers paying more.
4. **Regulators can stop a product.** California says Nitricity's fertilizer contains prohibited synthetic nitrogen; litigation ongoing [src-20260320-7b8d7b]. Phlow's epinephrine awaits FDA (2027) [src-20260209-16223c].
5. **Generics are excluded from the 232 tariff.** See 5.11 (4).
6. **Pledges are not plants.** Only about $60B of about $600B of pharma pledges has specific amounts and locations [src-20260210-883e2f], and equipment orders have not followed [src-20260601-17c2d4]. Pricing deals give 0% tariffs until 2029, blunting the stick [src-20260601-17c2d4].
7. **Rates.** Plants are capital-heavy and long-dated; Fed 3.75–4.00% [src-20260916-f0c016].
8. **AI discovery is not the bottleneck.** Discovery without scale-up does not create supply [inference].

### 5.4 Why an AI-enabled, vertically integrated company is the answer here

- **Owning the plant captures the value.** Whoever sells the molecule keeps the margin; pure AI software for chemistry is a tool, so we label it **enabler** only.
- **AI and automation shorten scale-up,** the step that killed the last wave: continuous-flow and modular plants (Phlow, On Demand Pharmaceuticals), AI-tuned bioprocesses (Solugen), robotic labs (Chemify, Radical) — mostly **claims** at this stage.
- **Versus imports:** BIOSECURE and the 232 tariff reward provable US supply for APIs and intermediates.
- **Where it breaks [inference].** In commodities, cost per ton wins and incumbents own it; in pharma, FDA approval, not AI, sets the timeline.

### 5.5 What would have to be true, and signals to watch

- Onshoring rules bite on generics, not just patented drugs. **Watch:** any 232 extension to generics; BIOSECURE's first OMB list (due Dec 2026).
- Repeat orders from paying buyers. **Watch:** Phlow's FDA decision on epinephrine (2027); Nitricity's sold-out-through-2028 contracts holding after the CDFA case; Twelve's fuel deliveries.
- Plants hit nameplate on time. **Watch:** Solugen's Bioforge Marshall; Twelve AirPlant One output versus 50k gal/yr.
- The US–Europe gas gap stays wide. **Watch:** Cefic's quarterly gas ratio (3.6 in Jan–Jul 2026) [src-20260915-e74614].

### 5.6 Macro in more depth

**Europe is shrinking.** Announced European chemical closures rose sixfold a year, to 37 Mt over 2022–25, about 9% of capacity. Almost half is upstream petrochemicals; nine steam crackers (16% of Europe's cracking capacity) are closing. In 49% of cases the stated reason is energy cost. Confirmed new investment collapsed to 0.3 Mt in 2025, and confirmed capex fell from EUR7.6bn to 1.5bn [src-20260115-ec35af]. Roland Berger calls it a "structural reset," not a downturn, with about 20,000 direct and 89,000 indirect jobs at risk [src-20260201-63910c]. FTI says chemical plants need 80–85% utilization to pay; Europe's average is about 74% and Germany's was 70% in Q3 2025, some segments are below 65%, more than 30 German chemical companies a year have gone insolvent since 2024, and Europe's share of global chemical sales is set to stay below 15% [src-20260401-e2adb0]. Roland Berger puts the net capacity loss above 30 Mt [src-20260201-63910c]. _Meaning [inference]:_ buyers of European intermediates need new suppliers; US plants with cheap gas are the natural replacement.

**The US has a feedstock edge, but growth is slow.** Shale gas makes US ethane cheap. ACC expects US chemical volumes up only 0.5% in 2026, led by basic chemicals, with specialty and consumer chemicals declining. Middle East disruption is raising demand for gas-advantaged US output; tariff uncertainty is the main risk [src-20260615-0c9b7e]. [inference] Commodity chemistry in the US is an incumbent's game (Dow, ExxonMobil, LyondellBasell); the openings for startups are further up the ladder.

**China and India own the pharma building blocks.** About 90% of US prescriptions are generics. India supplies 47.2% of US generic doses and China 13.0%; only 10.5% are US-made. Indian firms get 65–70% of their KSMs, intermediates and APIs from China, so after adjusting, about 46% of US generic doses depend on Chinese source materials [src-20250605-bde73f]. Estimates vary: direct Chinese API is about 8% of volume, and Brookings' own review puts Chinese API in "perhaps a quarter" of US drug volume [src-20250501-c298cb]. CFR finds about 41% of KSMs in US-approved APIs come only from China, including the starting materials for 94% of amoxicillin, 74% of heparin and 70% of acetaminophen sold in the US; US amoxicillin production went from 100% domestic to zero in twelve years. It estimates shortages would peak 4.5–9 months after a Chinese restriction [src-20260501-7f527d]. _Meaning [inference]:_ the case is strongest for a short list of old, cheap molecules, which need a price floor or a government buyer.

**Policy is pushing reshoring, mainly in pharma.**
- **Section 232 pharma tariff (April 2026):** 100% on patented drugs and their ingredients; 20% for companies with approved onshoring plans (rising to 100% in 2030); zero for companies with pricing-and-onshoring deals; 15% for the EU, Japan, Korea and Switzerland. Generics are excluded for now. FDA data cited in the proclamation: only 15% of patented API volume is made in the US [src-20260402-ecae19]. Deadlines run to July 31 and September 29, 2026; pricing-deal firms get 0% until 2029 [src-20260601-17c2d4].
- **BIOSECURE Act:** enacted in the FY2026 defense bill (signed Dec 18, 2025). It bars federal contracts, grants and loans involving "biotechnology companies of concern"; the first OMB list is due by Dec 2026 [src-20260110-4db409]. The Pentagon added WuXi AppTec to its 1260H list in June 2026 [src-20260818-489fdf].
- **Executive Order 14293 (May 2025)** and FDA's PreCheck pilot speed approval of new US drug and API plants (see the policy tracker, section 11).
- **Government lending** (section 2.4) can fund plants: Solugen holds a conditional $213.6M DOE loan guarantee [src-20240613-2df5d6].

[inference] The policy pull is strongest for pharma intermediates and APIs and for defense chemicals (energetics). It is weakest for commodities, where the US is already a net exporter.

### 5.7 How the industry and its supply chain work

Think of chemistry as a five-step ladder. Each step takes the output of the step below and makes it more specific, smaller in volume and higher in price per kilogram.

1. **Feedstocks.** The raw inputs: natural gas and natural-gas liquids (ethane, propane), crude-oil fractions (naphtha), salt, sulfur, phosphate rock and, increasingly, biomass such as corn sugar.
2. **Commodity (basic) chemicals.** Made in giant, continuous plants measured in millions of tons a year. A **steam cracker** heats ethane or naphtha to "crack" it into ethylene and propylene, the building blocks of most plastics. Others: ammonia, chlorine, sulfuric acid, methanol. Price is set by feedstock and energy cost; margins are thin and cyclical.
3. **Intermediates.** Molecules one or several reaction steps further on (for example acetic acid, adipic acid, solvents and monomers). In pharma, the key ones are **key starting materials (KSMs)**, the purchased building blocks an approved drug process starts from.
4. **Specialty and fine chemicals.** Smaller volumes sold for what they do, not what they are: coatings, catalysts, water-treatment chemicals, electronic chemicals, flavors, crop chemicals, energetics. Higher margins; buyers qualify a supplier and then rarely switch.
5. **Active pharmaceutical ingredients (APIs).** The molecule in a drug that does the work. A **finished dose form (FDF)** is the pill or injection. A **CRO** (contract research organization) makes molecules for research; a **CDMO** (contract development and manufacturing organization) makes them at commercial scale under FDA rules.

Two engineering terms matter for startups. **Batch** chemistry runs one tank at a time; **continuous flow** pumps reactants through pipes or small reactors nonstop, which is safer for hazardous steps and easier to automate (FDA guidance Q13 covers continuous manufacturing). **Biomanufacturing** uses enzymes or engineered microbes (fermentation) instead of heat and pressure to make molecules.

Who buys: ACC says more than 80% of basic and specialty chemicals are bought by other industries, not consumers [src-20260615-0c9b7e]. So chemical demand follows manufacturing, housing, autos, data centers and pharma.

**Market size (this industry).** No clean free revenue number for US chemicals in the repo [gap]. Physical proxies: US ammonia output 14.0 Mt of nitrogen in 2025, 88% to fertilizer, Gulf price about $450 per short ton [src-20260206-c8fbbc]; Europe announced 37 Mt of closures in 2022–25 [src-20260115-ec35af]; only about 10% of APIs by volume are made in the US [src-20260701-818dbe].

### 5.8 Where AI and automation help

| Stage | What AI does | Maturity | Molecule-to-revenue time |
|---|---|---|---|
| **Discovery** (what molecule?) | Generative design, property prediction, screening billions of candidates | Real but crowded; models are commoditizing (4A) | Drugs: 10+ years to market; specialty chemicals: 2–5 years to qualify |
| **Synthesis planning** (how to make it?) | Retrosynthesis software suggests reaction routes (Synthia, IBM RXN, PostEra) | Decision support only; chemists still filter routes [inference from literature review] | Months saved per route |
| **Lab execution** (actually make it) | Robots plus AI run reactions and learn from results ("self-driving labs") | Early; claims of autonomous discovery have been disputed (the 2023 A-Lab row) | Faster make-test loops for research compounds |
| **Process and plant** (make it cheaply at scale) | New catalysts and enzymes, continuous-flow control, yield optimization | Where the money is, and where startups own plants | 3–7 years for a new plant [inference] |

The key point for SPC: **discovering a molecule is not the bottleneck; making it reliably at scale and getting buyers to qualify it is.** This matches the materials finding in 4A.4.

### 5.9 Right to win, unit economics and data loop

**Right to win [inference].** Own the plant and the offtake; use automation to shorten scale-up; target molecules where policy forces US supply (APIs, intermediates, defense chemicals), not commodities where Dow and ExxonMobil win on cost.

_Chemicals business models, unit economics and data loop (v8 sections 4B.4, 4B.5): Appendix D._

**Data loop (score 0–3; scale in 2.13):**

No chemicals company in the repo has a scored data loop yet [gap].

### 5.10 Companies, grouped by label

#### Producers — fully integrated

**Solugen (Houston; specialty and commodity chemicals; Full).**
- **Process:** "chemoenzymatic" production pairs an enzyme with a metal catalyst to turn corn syrup into chemicals, starting with hydrogen peroxide and organic acids. **Claim (Solugen founders):** 96% yield at scale versus about 60% for the traditional route [src-20260320-f90e80].
- **Origin:** started with a reactor costing about $10,000 and sold to hot-tub owners in Dallas before raising large rounds. Its Bioforge plant runs 24/7 on railcars of corn syrup. **Claim:** smaller plants near customers undercut incumbents on shipping [src-20260320-f90e80].
- **What it means [inference]:** the clearest AI-adjacent chemical producer. It owns plants, sells product and has repeat industrial buyers. But the edge is enzyme engineering and plant design more than AI, and the products are lower-value chemicals exposed to commodity pricing.
- _More detail: Appendix D (Solugen)._

**Twelve (Moses Lake, WA; e-fuels and e-chemicals from CO2, water and power; Full).** _Strong fit; fuller profile._
- **What it makes:** AirPlant One opened June 10, 2026 and makes e-jet fuel and E-Naphtha from captured CO2, water and renewable power; the fuel meets ASTM spec and is being sold. Nameplate is about 50,000 gallons a year [src-20260610-bf26af][src-20260901-c5f851].
- **Who buys / repeat orders:** Alaska Airlines and Microsoft committed in 2022 to buy output; IAG and the US Air Force are named customers [src-20260610-bf26af][src-20260901-c5f851]. No repeat-order data yet.
- **AI / automation angle:** the edge is electrochemistry and plant design, not AI; offtakers are mostly strategic investors (Alaska, Microsoft, Amazon Climate Pledge Fund) [src-20260901-c5f851] [inference on the AI point].
- **Money:** $645M raised (round reported in the source) [src-20260610-bf26af].
- **Bear (one line):** the plant ran years late, and Alaska postponed its first flight over carbon intensity [src-20260901-c5f851] — the premium depends on mandates.

**Phlow (Richmond/Petersburg, VA; US-made essential-medicine APIs; Full).** _Strong fit; fuller profile._
- **What it makes:** active pharmaceutical ingredients (APIs) for essential generic medicines, in its own plants using batch plus continuous-flow chemistry: a kilo facility (~250 kg a year) and a metric-ton facility (50–100 t a year) [src-20260209-16223c][src-20260721-fa5081].
- **Who buys / repeat orders:** a deal under which Phlow makes epinephrine API and Fresenius makes finished doses; validation campaign done; Drug Master File filed; commercial supply pending FDA in 2027 [src-20260209-16223c]. A $15.9M award to an end-to-end Virginia alliance: Occam makes building blocks, Phlow the APIs, Civica finishes ketamine, midazolam and others [src-20260721-fa5081]. Government buyers plus a generic maker = the kind of offtake that can repeat.
- **AI / automation angle:** continuous-flow manufacturing (smaller footprint, more automation, fewer batch steps) — automation rather than AI.
- **Why it fits:** the most direct answer to the 46% China-dependence number [src-20250605-bde73f] and to BIOSECURE.
- **Bear (one line):** generics are excluded from the 232 tariff and margins are thin; one FDA delay pushes revenue a year.

**On Demand Pharmaceuticals (Rockville, MD; on-demand API and drug manufacturing; Full).**
- **What it makes:** APIs at its Rockville plant, plus a modular "Pharmacy on Demand" unit using AI/ML process control, deployed at North Mississippi Medical Center [src-20250813-79a0cf].
- **Who buys:** hospitals and government (DoD/HHS funded since 2020, about $35M in federal awards); the unit makes shortage drugs [src-20250813-79a0cf]. No commercial repeat-order data.
- **AI / automation angle:** **Claim:** AI/ML-controlled modular continuous manufacturing.
- **Bear (one line):** still grant-funded; hospital-scale units may not reach meaningful volume.

**Nitricity (Fremont and Delhi, CA; organic nitrogen fertilizer from air, power and almond shells; Full).**
- **What it makes:** nitrogen fertilizer for organic growers; its Delhi plant is about 100x pilot scale and ramping [src-20260320-7b8d7b].
- **Who buys / repeat orders:** Delhi output **sold out through 2028** to organic growers [src-20260320-7b8d7b] — the best repeat-demand signal among the new names. $50M Series B (Khosla, World Fund).
- **AI / automation angle:** electrified, automated plasma process; little explicit AI [inference].
- **Bear (one line):** California's agriculture department (CDFA) says the product contains prohibited synthetic nitrogen; if that stands, the organic market closes (litigation ongoing) [src-20260320-7b8d7b].

#### Producers — hybrid

**Warp Sciences (San Francisco; US drug-discovery chemistry CRO; Hybrid).**
- **What it is:** a US-based chemistry CRO that combines expert chemists, AI and robotics in labs "designed for automation from day one" to make the molecules biotech and pharma teams test. It does not develop its own drugs [src-20261027-c11426][src-20261022-b542e2].
- **Team:** CEO Kevin Weil (ex-OpenAI Chief Product Officer and head of OpenAI for Science), COO DJ Patil (first US Chief Data Scientist), CSO Sol Reisberg (about 20 years in medicinal chemistry, ex-Gilead and Schrödinger, a long-time buyer from offshore CROs) and Mano Paluri (ex-Meta FAIR) [src-20261022-b542e2].
- **What it means [inference]:** a direct BIOSECURE and reshoring play with a top-tier team, but it is services-first and launched five days ago. No customers, prices or throughput are public. US chemist labor costs several times Chinese CRO rates, so the thesis depends on automation actually lowering unit cost. It is research-scale, not manufacturing-scale.
- _More detail: Appendix D (Warp Sciences)._

**Chemify (Glasgow; robotic chemistry, "chemputation"; Hybrid).**
- **What it is:** founded in 2022 from Lee Cronin's University of Glasgow lab. Its "Chemifarm" turns code written in a chemical programming language into molecules made by robots. The first £12M Chemifarm opened in June 2025 [src-20251021-d0aa43].
- **Money:** a Series B of more than $50M (Wing, Insight) [src-20251021-d0aa43]. In Sept 2026, £22M in Scottish and UK government grants went toward an £89.9M expansion, with staff growing from 152 to about 450 in three years [src-20260917-2991e2].
- **What it means [inference]:** the most ambitious "AI makes molecules" platform. Today it is a research-scale CRO and co-discovery shop, not a bulk producer, so it sits beside the discovery labs in 6.10.
- _More detail: Appendix D (Chemify)._

**AIRCO (formerly Air Company; New York and Pennsylvania; CO2-to-fuels and alcohols; Hybrid, close to Enabler).**
- **What it makes:** fuels and alcohols from CO2; now licenses its process and builds containerized "MAD" fuel systems for the military rather than running large plants [src-20260526-9ebac5].
- **Who buys:** DoD — about $70M of DoD-related awards, including a $15M STRATFI; Pennsylvania manufacturing hub [src-20260526-9ebac5].
- **AI / automation angle:** modular, automated units deployable in the field.
- **Bear (one line):** licensing plus defense prototypes means it may never sell product at volume itself.

#### Watch list and AI-chemistry enablers

**Watch list (short notes, not core):**
- **Debut (beauty ingredients by biomanufacturing; Hybrid).** $20M for AI ingredient discovery; pilot plant; $2M to plan a facility [src-20250801-a4ae9d]. Bear: no commercial plant yet.
- **Cemvita (microbes turning CO2 into chemicals and oil; Hybrid).** Brazil plant at the agreement stage [src-20250804-e1bddd]. Bear: no operating commercial plant.
- **Geno (Genomatica; bio-based chemicals; acquired).** Acquired by Again in 2026 [src-20260812-dc968f]. Kept as a scale-up cautionary tale.
- **Lygos (bio-based organic acids).** Sold its Soltellus business to Dober (low confidence) [src-20260101-5ca758].
- **Visolis:** not added; only a LinkedIn source was found.

**AI-chemistry enablers (software or drug developers; not producers):**
- **Iambic (Enabler / drug developer).** Enchant v3 model (41B parameters) and an automated lab that makes hundreds of compounds a week; its own drug pipeline (IAM-C1, IAM217) and partners; S-1 filed October 2026 [src-20260921-cb3d77]. Sells drugs, not chemicals. Bear: drug-development risk dominates.
- **PostEra and SYNTHIA (Merck KGaA's retrosynthesis software; Enablers).** Software for planning how to make molecules [src-20261027-13f9b3]. Tools, not producers. Bear: commoditizing as general AI models improve [inference].

**Process-plant software (cross-reference).** Lumaril, AI closed-loop control sold to chemical, polymer and biologics plants and paid on the production it adds (company claim), is profiled in full in section 7.10 as an enabler [src-20261027-d5ba3f].

_Short v8 notes on LanzaTech, Zymergen, Zapata and others: Appendix D._

### 5.11 Bear case, at equal weight

1. **Biomanufacturing has a terrible record.** Ginkgo, Zymergen and Amyris all collapsed in 2021–23. For simple molecules, making them with organisms usually costs more than conventional chemical synthesis, so bio works mainly for complex, high-value compounds [src-20240101-499ec8]. Zymergen had no in-house commercial-scale manufacturing, its contract manufacturers missed production goals, and customers could not get its Hyaline film to work in their own production lines [src-20220101-9c58e3]. LanzaTech is fighting going-concern doubt [src-20260331-20d171].
2. **AI-for-chemistry software alone fails.** Zapata is the example [src-20241011-721c93]. Retrosynthesis tools are still decision support for chemists [inference].
3. **Commodity economics punish newcomers.** Europe's plants are closing because of energy cost and Chinese overcapacity [src-20260115-ec35af]. A US startup selling a commodity competes with shale-fed incumbents and Chinese surplus, so it needs a real cost edge, not a green premium.
4. **Pharma policy can reverse or be diluted.** Section 232 exempts generics (where China dependence is deepest) and gives 0–20% rates to companies that do deals [src-20260402-ecae19]. A federal court enjoined WuXi's 1260H designation (search summary; low). The cheaper Indian and Chinese supply still exists.
5. **Capex before contracts again.** Chemical plants take years and hundreds of millions. Solugen's DOE loan is still conditional [src-20240613-2df5d6].
6. **Labor cost of US CROs.** Warp and Chemify must automate faster than offshore labs cut prices [inference].

**What fits SPC [inference].**

| Company | Integration | Fit with "AI-enabled, vertically integrated, makes and sells product" |
|---|---|---|
| Solugen | Full | **Best fit.** Own plants, product revenue, government loan; AI is secondary to enzyme and process IP. Late stage. |
| Orbital (6.10) | Full (specialty fluids) | Good fit; see 6.10. |
| Warp Sciences | Hybrid (CRO) | Fits the reshoring and data-loop thesis; services, not product; too early to judge. |
| Chemify | Hybrid (CRO plus IP) | Interesting option on "code to molecule"; research scale. |
| CuspAI, Periodic, Lila | Enabler or discovery lab | Not producers; track via 6.10. |
| LanzaTech, Zymergen, Zapata | — | Cautionary tales. |

**Diligence questions:** What is the yield and cost per kilogram at the current plant versus incumbents? How many customers have reordered after qualification? Who keeps the data rights? How much capex is committed before offtake contracts?

### 5.12 Key sources

- Cefic gas and trends [src-20260915-e74614][src-20251001-7ec954]; USGS ammonia [src-20260206-c8fbbc]
- Cefic closures [src-20260115-ec35af]; Roland Berger [src-20260201-63910c]; FTI [src-20260401-e2adb0]
- ACC 2026 outlook [src-20260615-0c9b7e]
- USCC on generics [src-20250605-bde73f]; Brookings [src-20250501-c298cb]; CFR [src-20260501-7f527d]
- Section 232 pharma [src-20260402-ecae19]; BIOSECURE [src-20260110-4db409]; WuXi 1260H [src-20260818-489fdf]
- Solugen DOE loan [src-20240613-2df5d6]; Zymergen [src-20220101-9c58e3]; LanzaTech [src-20260331-20d171]; pledges and deadlines [src-20260601-17c2d4][src-20260701-818dbe]
- New company sources: Twelve, Phlow, ODP, Nitricity, AIRCO, Debut, Cemvita, Geno, Lygos, Iambic, PostEra/SYNTHIA (cited in 6.10)

_Brooke's reading and listening list (v7.2 section 4B.10): Appendix D._


### 5.13 Listen & watch

Full list: Appendix E._

1. ★ **"Inside The Startup Reinventing The $6 Trillion Chemical Manufacturing Industry"**, YC, Mar 2026, about 13 min. [▶ Open link](https://www.ycombinator.com/library/NO-inside-the-startup-reinventing-america-s-trillion-dollar-chemical-industry) — *Why:* the best short intro to a fully integrated chemical maker (Solugen; ~96% yield claim). Repo: src-20260320-f90e80.
2. **"EP 312 Lee Cronin on Automating Chemistry"**, *The Jim Rutt Show*, Jul 2025, length not listed. [▶ Open link](https://jimrutt.substack.com/p/ep-312-lee-cronin-on-automating-chemistry-f9f) — *Why:* Chemify's "code to molecule" and how it charges (company claims). Repo: src-20250724-0f42f3.
3. **"Why Twelve believes power-to-liquids will revolutionise SAF"**, *Sustainability in the Air*, Jul 24, 2025, 34 min. [▶ Open link](https://podcasts.apple.com/bm/podcast/why-twelve-believes-power-to-liquids-will-revolutionise/id1620281360?i=1000718768981) — *Why:* an owned e-fuels plant and its long-term buyers; policy is the swing factor. Not in the repo.
4. **"Mission-driven doctor, inventor & entrepreneur" (Ep. 175)**, *Molecule to Market*, Phlow CEO Eric Edwards, 55 min. [▶ Open link](https://moleculetomarketpod.com/episodes/mission-driven-doctor-inventor-entrepreneur/) — *Why:* drug-ingredient onshoring with the government as anchor buyer. Not in the repo.

### 5.14 Commercial traction and incumbents

_Labels as in 3.14. This is the deepest traction section because chemicals is where lab-to-revenue gaps have killed the most startups._

**Who's actually commercializing (selling product today first)**

| Company | Segment | Status | Evidence |
|---|---|---|---|
| Solugen | Specialty/commodity | **Revenue** | Bioforge plant runs 24/7; repeat industrial buyers; conditional $213.6M DOE loan [src-20240613-2df5d6][src-20260320-f90e80]. |
| Nitricity | Fertilizer | **Revenue** | Delhi output sold out through 2028 [src-20260320-7b8d7b]; California regulator dispute pending. |
| Twelve | E-fuels | **Revenue (early)** | Fuel meets ASTM spec and is being sold; offtakers Alaska, Microsoft, IAG, US Air Force [src-20260610-bf26af][src-20260901-c5f851]. Plant ran years late. |
| AIRCO | CO2 fuels (defense) | **Revenue (government)** | About $70M of DoD-related awards; licensing plus field units [src-20260526-9ebac5]. |
| On Demand Pharmaceuticals | APIs | **Pilot** | About $35M of federal awards; one hospital-deployed unit [src-20250813-79a0cf]. |
| Phlow | APIs | **Pilot** | Epinephrine API with Fresenius; validation done; commercial supply pending FDA in 2027 [src-20260209-16223c]; $15.9M award [src-20260721-fa5081]. |
| Chemify | Robotic chemistry (CRO) | **Pilot** | **Claim:** 12 customers [src-20250724-0f42f3]. Research scale. |
| Debut | Bio-ingredients | **Pilot** | Pilot plant [src-20250801-a4ae9d]. |
| Warp Sciences | Chemistry CRO | **Lab / pre-revenue** | Launched October 2026; no customers public [src-20261022-b542e2]. |

Exits and failures: Zymergen [src-20220101-9c58e3]; LanzaTech going-concern doubt [src-20260331-20d171]; Geno sold [src-20260812-dc968f].

**Revenue vs lab.** _Real revenue:_ specialty chemicals made in owned plants (Solugen), fertilizer (Nitricity), and government-funded fuels (Twelve, AIRCO). _Pilot:_ US-made APIs; revenue waits on FDA. _Mostly lab:_ AI chemistry platforms and new CROs (Chemify, Warp) and AI-discovered molecules.

**Startup vs incumbent: cost and scale.**

| | BASF | Dow | LyondellBasell | Startups |
|---|---|---|---|---|
| 2025 revenue | €59.7B | $40.0B | $30.2B | Twelve nameplate ~50,000 gal/yr [src-20260610-bf26af]; Phlow 50–100 t/yr API [src-20260721-fa5081] |
| 2025 profit | EBITDA €6.6B before special items (11.0%) | Net loss $2.4B | Net loss $738M | Mostly not public |
| Yearly capex / R&D | Capex €4.8B; R&D €2.0B | — | Capex $1.9B | Solugen's conditional DOE loan: $213.6M |
| Sources | [src-20260227-9fe9e6] | [src-20260129-338338] | [src-20260130-12a9f3] | as cited |

_Meaning [inference]:_ a single incumbent spends more on R&D in a year than most chemical startups have raised in total, so startups cannot win on cost per ton in commodities. Two openings remain. The incumbents are themselves losing money and closing plants (5.6), and startups can win where a smaller plant has a real process edge (**Claim (Solugen):** 96% yield versus about 60% for the traditional route [src-20260320-f90e80]) or where policy pays for US supply (APIs, defense). Incumbents also buy AI rather than build it: LyondellBasell signed a multi-year deal with Citrine [src-20260902-224ead]. Lonza (contract pharma manufacturing) is the incumbent for APIs; no free source in the repo yet [gap].

**TSCA timeline: new molecules vs drop-ins.**
- **New molecule (premanufacture notice, PMN):** the law gives EPA 90 days, extendable by 90. In practice the median final decision took **520 days in 2025** and 469 in Q1 2026; about 92% of pending cases are past the deadline and 307 have waited over a year [src-20261027-f4abbf]. GAO found EPA met the 90 days less than 10% of the time [src-20250101-74b3e0]. EPA had 427 active cases on Oct 1, 2026 [src-20261001-d40423].
- **Low volume (LVE, up to 10,000 kg a year):** 30-day review, the fastest path for pilot volumes [src-20261027-f4abbf].
- **Drop-in chemical** (a molecule already in commerce, such as hydrogen peroxide or jet fuel): no new-chemical review; the PMN process applies to new chemicals and new uses [src-20261027-f4abbf][src-20261001-d40423]. _Meaning [inference]:_ a startup that makes an existing molecule by a better process (Solugen, Twelve) skips one to two years of EPA review; an AI-discovered new molecule should budget around 1.5 years before US sale at full volume.
- **Pharma (FDA):** a standard generic application (ANDA) has a 10-month review goal, 8 months if prioritized [src-20261027-711e48]; plants also need cGMP inspection (Phlow's 2027 timing [src-20260209-16223c]).
- **EU REACH:** registration applies before selling into Europe [src-20251110-84b67e][src-20251218-f0d6ef].

**5-year outlook (to 2031).** _Specialty and pharma intermediates:_ **possible**. Solugen and Nitricity sell today; Phlow could be supplying by 2027 if FDA approves. _Commodity chemicals:_ **unlikely**. _AI-discovered new molecules at volume:_ **unlikely**, given TSCA and scale-up times. **Bear case, equal weight:** see 5.11. Biomanufacturing's record is poor, generics are outside the tariff, green premiums depend on mandates, and Nitricity's regulator fight could close its market.

## 6. Advanced Materials

_What this industry is._ Advanced Materials covers companies that make and sell engineered materials rather than commodity molecules: battery cathodes, cooling fluids and hardware for data centers, sorbents, alloys and catalysts. Two producers sit here (Mitra Chem, Orbital Industries). AI discovery labs (Radical AI, CuspAI, Periodic Labs, Lila Sciences) are kept in a clearly labeled sub-group, **Materials Discovery Labs**: they invent materials with AI and robotic labs but mostly do not yet sell product at scale.

### 6.1 The problem today

- **China makes almost all battery materials.** In 2025 China made 70% of the world's electric vehicles, more than 80% of battery cells, about 85% of cathode active material and more than 90% of anode material [src-20260501-79ef76]. For the cheaper LFP (lithium iron phosphate) chemistry, more than 98% of cathode material and cells are made in China [src-20250521-9be25a].
- **The US is switching to the chemistry it makes least.** LFP was more than 55% of EV batteries worldwide in 2025. In the US, more than 50 GWh of cell capacity (LG Energy Solution, Ford) has been reassigned to LFP, much of it for grid storage, which was a third of US battery deployment; LFP cathode and its precursors are almost entirely made in China [src-20260501-600ef9].
- **Data centers need new cooling materials.** Data centers used 415 TWh of electricity in 2024 (1.5% of the world total), heading to about 945 TWh in 2030, growing about 15% a year; cooling takes from 7% (hyperscale) to over 30% (enterprise) of a data center's power [src-20250410-22e27a]. Liquid cooling is expected to reach 53% of AI chips in 2026 (med) [src-20260817-13658d].
- **The old fluorine chemistry is being regulated out.** Many cooling fluids, seals and coatings use PFAS ("forever chemicals"). EU scientific committees backed a broad PFAS restriction in March 2026, with targeted exemptions; fluoropolymers and fluorinated gases are in scope [src-20260326-379e42].
- **Discovery is cheap, scale-up is not.** AI shortens the first two steps of making a new material (weeks to months), but scale-up and customer qualification take one to five years each (6.6).

_What this means [inference]:_ there is real, policy-backed demand for a non-Chinese cathode and for new cooling materials, but the winner is whoever can make tons at a qualified spec, not whoever finds the molecule first.

### 6.2 Macro and tailwinds, ranked [ranking is inference]

| Rank | Tailwind | Evidence | Durable? |
|---|---|---|---|
| 1 | **Battery supply-chain localization** | China ~85% of cathode, >98% of LFP cathode [src-20260501-79ef76][src-20250521-9be25a]; Mitra has a $100M DOE award for a Michigan plant [src-20261023-6e0642] | Structural (security), but subsidy-dependent |
| 2 | **Grid-storage pivot to LFP** | >50 GWh of US capacity moved to LFP; storage a third of US deployment [src-20260501-600ef9] | Structural while data centers add load |
| 3 | **Data-center power and cooling** | 415 → ~945 TWh by 2030; cooling 7–30%+ of power [src-20250410-22e27a]; liquid cooling 53% of AI chips in 2026 [src-20260817-13658d] | Structural; tied to AI capex |
| 4 | **PFAS rules** | EU restriction backed March 2026 [src-20260326-379e42]; US keeps 4 ppt PFOA/PFOS limits, deadline 2031 [src-20260520-caa33e] | EU structural; US partly reversed |
| 5 | **AI and lab automation getting cheaper** | Discovery labs funded (Periodic, Lila, CuspAI; 6.10); open datasets like OMol25 (100M+ calculations) [src-20250513-fbb4d8] | Structural (tech), hype-sensitive |

**Battery chain, in more depth.** The IEA expects China still to hold about three-quarters of cathode and about 90% of anode production in 2035; the EU and US together reach only about 10% of cathode [src-20260501-79ef76]. China's edge in LFP comes from cheap inputs, equipment and patents [src-20250521-9be25a]. _Meaning [inference]:_ a US cathode maker sells mostly security of supply, so its customers are those who must or will pay for it (automakers with tax-credit rules, defense, utilities buying storage).

**Cooling, in more depth.** Accelerated (AI) servers are the fastest-growing slice of data-center load, and the US alone accounts for almost half of its electricity demand growth to 2030 from data centers [src-20250410-22e27a]. Each point of cooling efficiency is power that can go to chips instead [inference]. Orbital targets exactly this with fluids and hardware, with qualification aimed at 2027 [src-20260528-375aec].

**PFAS, in more depth.** The EU's restriction would cover manufacture, sale and use with time-limited exemptions [src-20260326-379e42]. In the US, the EPA kept the 4 parts-per-trillion limits for PFOA and PFOS in drinking water but proposed moving compliance from 2029 to 2031 and rescinding limits for four other PFAS (May 2026) [src-20260520-caa33e]. _Meaning [inference]:_ PFAS-free replacements have a firm market in Europe and a softer one in the US.

### 6.3 Headwinds, at equal weight

1. **Chinese price.** China's scale sets cathode prices; a US plant is a price-taker without offtake or subsidy [src-20250521-9be25a] [inference].
2. **EV slowdown in the US.** US LFP share in EVs almost halved; capacity is being re-pointed to storage [src-20260501-600ef9].
3. **Scale-up and qualification take years** (6.6) and are where most money is spent.
4. **Rules can soften.** The US PFAS rollback shows regulation-driven demand can shrink [src-20260520-caa33e].
5. **Discovery-lab hype.** Large rounds before revenue (6.10); Plural, an Orbital investor, says there is "no AlphaFold moment" in materials [src-20260528-2c20ee].

### 6.4 Why an AI-enabled, vertically integrated company is the answer here

Owning the plant is the only way to capture the margin in step 5 (supply) of the materials chain; a lab that licenses an invention captures little [inference]. AI helps most where a producer can run many experiments on its own line: Mitra uses AI from lab scale (1 kg/day) to production (1,000 kg/day) [src-20261023-6e0642]. **Where it breaks:** discovery speed does not shorten customer qualification, and Chinese cost still sets price.

### 6.5 What would have to be true, and signals to watch

- A US cathode plant reaches steady output at a price buyers accept. **Watch:** Mitra's Muskegon plant start-up and offtakes [src-20261023-6e0642].
- Liquid cooling stays standard as AI chips grow. **Watch:** liquid-cooling share (53% expected in 2026) [src-20260817-13658d].
- The EU PFAS restriction is adopted. **Watch:** the final SEAC opinion and Commission proposal [src-20260326-379e42].
- A discovery lab sells product, not just papers. **Watch:** Periodic, Lila, CuspAI revenue from materials.

### 6.6 Macro in more depth

The steps, with typical time in brackets [inference, built from sources cited]:
1. **Compute screen** (weeks): the model narrows millions of candidates to hundreds. Now cheap.
2. **Synthesis and first tests** (months): grams to 500 g in an SDL. This is the step labs speed up 6–17 times. An RSC benchmark finds a median speedup of about 6 times over random sampling (search; low), and Lila claims 17 times [src-20260925-679418].
3. **Scale-up** (1–3 years): kilograms to tons. It needs process chemistry or metallurgy, and a pilot line. Radical's RAI-939 is at this step now [src-20260807-52b690].
4. **Qualification** (1–5 years): the customer tests the material in its own product against specs. Aerospace alloys need allowables databases. Chip fluids need qualification by the fab or GPU maker (Orbital, 2027 target [src-20260528-375aec]). Water sorbents need regulatory approval (Kemira).
5. **Supply** (ongoing): someone has to make it reliably at cost. This is where the margin is, and where owner-producers sit.

**Where AI helps:** step 1 a lot, step 2 a lot, steps 3–5 little. Steps 3–5 are most of the time and money. That is why Plural says there is "no AlphaFold moment" [src-20260528-2c20ee], and why the Lila CTO says only about 5% of science is cheap to verify [src-20260917-29aa29].

**Materials discovery, step by step.**

A new material (an alloy, a battery cathode, a catalyst, a coolant, a magnet) normally takes 10–20 years and tens of millions of dollars to go from idea to qualified product. Discovery labs try to compress that with three tools:
1. **Generative and predictive models.** Software proposes candidate structures and predicts their properties, so you test hundreds instead of millions. Examples:
   - Microsoft's MatterGen is a diffusion model trained on about 608k stable materials. It generates crystal structures to a target property [src-20250116-63e766][src-20261022-3e2a9d].
   - Google DeepMind's GNoME predicted 2.2M crystals, about 380k of them stable. Outside labs have since made 736 of them [src-20231129-1dc706].
   - Meta's open OMat24 dataset holds more than 110M quantum-mechanics (DFT) calculations [src-20130101-5e5543].
2. **Self-driving labs (SDLs).** Robots mix, synthesize and test the candidates, and the results feed back into the model. Examples are Berkeley's A-Lab, Argonne's Polybot [src-20250217-059784] and Radical AI's alloy lab.
3. **The closed loop.** Model proposes, robot makes and measures, model updates. The claim is that each turn makes the next guess better, so the lab gets faster over time. This is the materials version of the "data loop" in section 6.

**The key point [inference]:** models are becoming free. GNoME, MatterGen, OMat24 and the Genesis Mission platform are all public or close to it. The scarce assets are (a) physical throughput, meaning how many real samples you can make and test, (b) data that is proprietary and tied to real-world performance, and (c) the ability to scale up and qualify a material with a customer. That is where the right to win sits.

### 6.7 How the industry and its supply chain work

| Model | What they sell | Examples | Producer test? |
|---|---|---|---|
| 1. Software / SaaS | Data platform and AI tools to the R&D teams of chemical and materials companies | Citrine, Uncountable, Kebotix (status unclear), Albert Invent, Microsoft Discovery | No |
| 2. Discovery-as-a-service / IP | Custom discovery projects, licensing and royalties, with partners making the material | CuspAI, Periodic, Lila (materials arm), Aionics, Dunia | No |
| 3. Lab plus government / partner contracts | Its own SDL; paid by defense and labs, then licensing or making specialty material | Radical AI | Partly (makes alloys at small scale) |
| 4. Owner-producer | Designs the material **and** makes and sells the product | Orbital Industries, Mitra Chem | Yes, closest to the thesis |

**Market size (this industry).** No free market size for materials R&D in the repo [gap]. Physical proxies: China holds about 85% of cathode active material and more than 90% of anode material [src-20260501-79ef76]; data centers used 415 TWh in 2024, heading to about 945 TWh by 2030, with cooling 7% to over 30% of that power [src-20250410-22e27a].

### 6.8 Where AI and automation help

AI screens candidates and runs robotic labs (steps 1–2 in 6.6); producers use it to tune their own lines, as Mitra does from 1 kg/day to 1,000 kg/day [src-20261023-6e0642].

### 6.9 Right to win, unit economics and data loop

**Right to win [inference].** Make the material at a qualified spec in the US, with an offtake; discovery alone captures little margin.

_Materials unit economics, data loop and right to win (v8 sections 4A.5–4A.7): Appendix D._

**Data loop (score 0–3; scale in 2.13):**

| Company | Score | How the loop works | Best evidence / what is missing |
|---|---|---|---|
| Radical AI | 2 | Robot lab tests and learns in a closed loop | 8-20 alloys a day [src-20260617-f9d293]. Missing: hit-rate trend |
| Periodic, CuspAI, Mind | 1 | Lab or factory as a training ground for AI | [src-20260917-1bcb81][src-20261022-37a0ea][src-20260513-83aa83]. Missing: production evidence |

### 6.10 Companies, grouped by label

#### Producers — fully integrated

**Orbital Industries (formerly Orbital Materials; London and Princeton, NJ; model 4).**
- **Funding:** $50M Series B led by Plural, May 28, 2026; about 50 staff [src-20260528-93befb][src-20260528-375aec].
- **Model:** it is vertically integrated and sells products, not software. The two products are a PFAS-free dielectric cooling fluid for data centers and "Nova Array," a modular data center it says can be deployed in 180 days [src-20260528-93befb].
- **What it means [inference]:** **the most thesis-aligned name in the section.** It found a buyer with an urgent need (data-center cooling), chose a product it can make through a contract manufacturer, and owns the margin. If the fluid ships in 2027 it could be among the first AI-designed materials sold at scale. Diligence: who the CMO is, qualification status, gross margin per liter.
- _More detail: Appendix D (Orbital Industries)._

**Mitra Chem (Mountain View, CA; LMFP and LFP battery cathodes; model 4).**
- **History:** began shipping LMFP cathode samples to global customers in 2023 [src-20240611-24c650]. Series B led by GM.
- **Production:** **Per BusinessPost (Korean):** a $100M DOE production grant, $50M from Michigan's MSF fund, and a planned 30k-ton-a-year, $370M LFP plant in Michigan. Korea's L&F invested $10M for about 3.3%, and the two are considering a joint-venture plant [src-20260831-db47e6] (med; single foreign-language article).
- **What it means [inference]:** an AI-designed chemistry turning into a chemical plant, so it does pass the producer test. But it competes on cost per kWh against Chinese LFP, which is the hardest market in industry. Its value depends on 45X and the foreign-entity rules (section 2.3).
- _More detail: Appendix D (Mitra Chem)._

#### Materials Discovery Labs (sub-group, kept separate from producers)

_Radical AI, CuspAI, Periodic Labs, Lila Sciences and smaller names. They invent materials; they do not yet sell product at scale._

_Pure discovery labs and design partners. Most do not run a production floor, so they are tracked, not targeted (section 6). Labels: Radical AI hybrid; CuspAI, Periodic and Lila enablers._

**Radical AI (New York; alloys and metals; model 3; Hybrid; partial fit).**
- **Funding:** $55M led by RTX Ventures [src-20250718-d46f24]. An Air Force AFWERX Direct-to-Phase II contract worth $1,197,902 [src-20250825-300a14].
- **Technology:** its AI engine, "Antimatter," drives a self-driving alloy lab. TIME named it one of the Best Inventions of 2026 [src-20261020-055082].
- **What it means [inference]:** the clearest defense-led path. Hypersonic and propulsion alloys have a buyer (RTX and the Air Force) and a clear test (the torch test). The risk is the jump from a 500 g button to qualified mill product, which needs a melter and forger partner.
- _More detail: Appendix D (Radical AI)._

**CuspAI (Cambridge, UK; sorbents, membranes, chemicals; model 2; Enabler; track).**
- **Funding:** $450M Series B (Kleiner, NEA) [src-20260720-840ae3].
- **Partners:** about 30 industry and 15 lab partners, including Samsung, AMD, Lam and Applied [src-20261022-37a0ea]. Its "AI Materials Foundry" consortium has 45+ members.
- **What it means [inference]:** the best commercial traction in the group, with a named buyer (Kemira) and a regulatory driver (PFAS rules). But CuspAI is a design shop: Kemira makes and sells the product, and CuspAI's take is a royalty or fee.
- _More detail: Appendix D (CuspAI)._

**Periodic Labs (San Francisco; semiconductors, superconductors, magnets; model 2; Enabler; track).**
- **Funding:** $300M seed, September 2025 [src-20251022-8eb7c0]; reportedly raising more (med) [src-20260514-5796ab].
- **Go-to-market:** **Claim (Periodic, via Heard In):** acts as its own "customer zero." It sends forward-deployed engineers, runs models on the client's site and fine-tunes on the client's data. Its first focus is semiconductor heat dissipation [src-20261008-38b3d6]. Its website lists magnets, semiconductors and superconductors, plus a Montreal ML office [src-20261001-e0573e][src-20261007-13c943].
- **What it means [inference]:** the most "frontier lab" of the group (OpenAI and DeepMind alumni). It is priced on talent; commercial proof is the least public.
- _More detail: Appendix D (Periodic Labs)._

**Lila Sciences (Cambridge, MA; "scientific superintelligence," life sciences and materials; model 2; Enabler; track).**
- **Funding and site:** $550M raised and a new 250k sq ft site in Cambridge [src-20260610-21e4df]. Reportedly in talks at about $8.5B (Bloomberg, via repo notes).
- **Catalysts (company claim):** 2,942 catalysts screened in 3 months, across six palladium-based families. The best matched ruthenium after more than 1,000 hours of testing. 17 times faster, with over 90% less hands-on time [src-20260925-679418]. Still untested in a real electrolyzer [src-20261019-392916].
- **What it means [inference]:** most of the value is in biology. Materials is a second line. Not an industrial producer.
- _More detail: Appendix D (Lila Sciences)._

### 6.11 Bear case, at equal weight

1. **No AI-designed material is clearly in volume commercial sale yet** [inference, from sources]. Orbital targets 2027 [src-20260528-375aec]. Kemira's PFAS sorbent and RAI-939 are at pilot or test-article stage [src-20260521-f4b51b][src-20260807-52b690].
2. **The science record is mixed.**
   - A-Lab's claim of 41 new materials was challenged ("no new materials were discovered") [src-20240124-513fd9].
   - For GNoME, the 736 independent syntheses are under 0.2% of the 380k predicted-stable crystals [src-20231129-1dc706].
   - MatterGen is limited to about 20 atoms per unit cell [src-20261022-3e2a9d].
3. **Synthesis and qualification, not discovery, are the bottleneck.** AI speeds up the cheap part.
4. **Buyers have small budgets and refuse to share IP.** R&D software sells in the hundreds of thousands; majors refuse royalties [src-20260913-3ad55e][src-20261016-29997e].
5. **The models are commodities:** open models and Genesis.
6. **Valuations far ahead of revenue:** CuspAI ($450M raised), Periodic ($300M seed), Lila (talks at about $8.5B, reported), none with disclosed material revenue [inference].
7. **Legal and safety issues:** the Royal Society review notes that patent law recognizes only human inventors, and flags safety and cyber risks of autonomous labs [src-20250716-e94853].
8. **Market size:** the lab-automation market is about $8–9B today, perhaps $20–24B later [src-20260709-1159ab] (low). That is small next to manufacturing.

_Materials bull case and SPC actions: Appendix D._

### 6.12 Key sources

- IEA Global EV Outlook 2026 [src-20260501-79ef76][src-20260501-600ef9]; IEA LFP supply chain [src-20250521-9be25a]
- IEA Energy and AI [src-20250410-22e27a]; TrendForce liquid cooling [src-20260817-13658d]
- ECHA PFAS [src-20260326-379e42]; EPA PFAS [src-20260520-caa33e]
- Mitra [src-20261023-6e0642]; Orbital [src-20260528-375aec][src-20260528-93befb][src-20260528-2c20ee]
- Discovery labs [src-20260807-52b690][src-20260925-679418][src-20260917-29aa29]; OMol25 [src-20250513-fbb4d8]


### 6.13 Listen & watch

Full list: Appendix E._

**Producers**

1. ★ **"Jonathan Godwin, CEO at Orbital: Orbital raised $50m Series B"**, *Scaling Europe*, Jun 29, 2026, 21 min. [▶ Open link](https://open.spotify.com/episode/2iSBDNWM2Sc5czUAIW0ugX) — *Why:* Orbital's founder on why it builds and sells hardware (a GPU-cooling material) instead of only models (company claims). Not in the repo (new).
2. **"Developing a supply chain for American-made batteries"**, *Volts*, Sep 6, 2024, length not listed (free transcript on page). [▶ Open link](https://www.volts.wtf/p/developing-a-supply-chain-for-american) — *Why:* Mitra Chem's CEO on China's grip on LFP cathodes and its iron-rich roadmap. Not in the repo (new).

**Materials Discovery Labs**

1. ★ **"The Self-Driving Lab — Joseph Krause, Radical AI"**, *Latent Space*, Jun 17, 2026, length not listed. [▶ Open link](https://www.latent.space/p/radical-ai) — *Why:* the moat is experiments, not models; customers asking for 300 lb pushed Radical toward making alloys. Repo: src-20260617-f9d293.
2. **"AI for Atoms: Periodic Labs with Liam Fedus"**, *No Priors*, Apr 3, 2026, 29 min. [▶ Open link](https://www.youtube.com/watch?v=Oru2Jxr1xHU) — *Why:* economics of an AI lab running its own experiments. Repo: src-20260403-40fa0e.
3. **"Meet the Ex-OpenAI & DeepMind Leads Creating an AI Scientist"**, *The Generalist*, Sep 29, 2026, 60 min. [▶ Open link](https://www.youtube.com/watch?v=vJVZgeXKlVo) — *Why:* Periodic's superconductor focus and the impurity problem. Repo: src-20260929-ca6d19.
4. **"Max Welling, CuspAI — Nebius Conversations"**, May 4, 2026, 19 min. [▶ Open link](https://www.youtube.com/watch?v=40CU4rbO7E4) — *Why:* the software-only model for contrast; it designs but does not make. Repo: src-20260504-36655f.

### 6.14 Commercial traction and incumbents

_Labels as in 3.14._

**Who's actually commercializing**

| Company | Sub-section | Status | Evidence |
|---|---|---|---|
| Orbital Industries | Producers | **Pilot**, with some licensing revenue | AWS partnership; cooling fluid in qualification, aiming to ship with 2027 GPUs [src-20260528-375aec]; BASF licenses its CurieOS software [src-20261022-edad3e]. |
| Mitra Chem | Producers | **Pilot** (samples) | Cathode samples shipped to customers since 2023 [src-20240611-24c650]; Muskegon plant [src-20261023-6e0642]. |
| Citrine Informatics | Discovery (software) | **Revenue** | Customers Huntsman and Perstorp [src-20261022-267188]; multi-year LyondellBasell deal [src-20260902-224ead]. |
| Radical AI | Discovery Labs | **Pilot** (government) | AFWERX contract worth $1,197,902 [src-20250825-300a14]. |
| CuspAI | Discovery Labs | **Pilot** (partners) | About 30 industry and 15 lab partners [src-20261022-37a0ea]. |
| Periodic Labs | Discovery Labs | **Lab** | No customers named [src-20261011-bf3574]. |

**Revenue vs lab.** Producers are at pilot or sample stage; the only clear revenue is software and licensing (Citrine, Orbital's CurieOS). Discovery labs are lab-stage: investors say there has been "no AlphaFold moment" for materials yet [src-20260528-2c20ee].

**Incumbents.** Albemarle ($5.14B net sales in 2025, $2.71B from energy storage) [src-20260201-955851]; Umicore (€3.6B revenue; its battery-materials unit had €436M revenue and still lost money) [src-20260220-f497c9]; Corning (a qualified supplier on defense and electronics lists) [src-20261022-1389b7]. _What they do better:_ qualified products, long customer trust and plants already built. Umicore spent decades mastering cathodes [src-20250529-3a588b]. _Where startups win [inference]:_ new needs where no incumbent is qualified (PFAS-free cooling fluids, hypersonic alloys). Even Umicore's losses show that battery materials are hard for everyone; China sets cathode prices [src-20250521-9be25a].

**Regulation and qualification.** Customer qualification takes 1–5 years (6.6). Battery products also need safety certification; full UL compliance typically takes 12–20+ weeks (low; vendor source) [src-20250101-040756]. New chemistries also face TSCA review (5.14).

**5-year outlook (to 2031).** _Producers:_ **possible** for one or two names (Orbital if its fluid qualifies in 2027; Mitra if its plant is funded). _Discovery labs:_ **unlikely** to be selling material at scale. **Bear case, equal weight:** see 6.11. Qualification can outlast a startup's runway, Chinese cathode pricing caps margins, and discovery labs may end up as royalty businesses, not producers.

## 7. Enabling Software & Robotics (tracked, outside the core)

_What this industry is._ Enabling Software & Robotics covers companies that sell tools to factories rather than making the product themselves: factory operating systems, inventory and ordering software, inspection AI, CAM automation and robots. We track it because it sets the pace for the producers in chapters 3–6, but it sits **outside the core thesis** (it is an enabler, not an owner of output).

### 7.1 The problem today

- **Factory workflows are slow and manual.** **Claim (Accel, on Arda):** assembly instructions drop from hours to minutes and complex engineering workflows run >10x faster; Anduril uses Arda inside ArsenalOS [src-20261020-8d7abc].
- **Robots are not spread evenly.** Industrial robot installs reached $18.6B worldwide; the US installed 38,428 units [src-20260924-28b59b]. US installs rose 11% in 2025, with metal and machinery only about 3,000 units [src-20260618-c903cc].
- **Robots still fail often in real tasks.** Robot-learning success rates are 59–66% [src-20260904-267293].
- **Labor is the reason to automate.** 522,000 open manufacturing jobs in August 2026 versus a pre-pandemic 432,000 [src-20261013-a7c995]; NAM: 54.9% cite workforce as a top challenge [src-20260914-b4d55c].

### 7.2 Macro and tailwinds, ranked [ranking is inference]

| Rank | Tailwind | Date / size | Structural or reversible? |
|---|---|---|---|
| 1 | **Labor shortage** | 3.8M jobs to fill by 2033, 1.9M unfilled [src-20240403-f5594a]; technician openings 2.3M by 2030 [src-20260910-b300bf] | Structural (demographics) |
| 2 | **Cheap AI models and cheaper robots** | Robot about $46K in 2010 versus labor at $46.30/hr fully loaded, rising 3–4% a year (newsletter) [src-20260826-14e4bb] | Structural |
| 3 | **Manufacturing expanding** | ISM manufacturing 54.5 (Sept 2026) [src-20261008-89df84] | Cyclical |
| 4 | **Tax: 100% bonus depreciation** | Restored [src-20260114-2075f7] | Legislated; reversible |
| 5 | **Incumbents prove margins** | Rockwell gross margin 49.5% [src-20260804-0e8130]; Siemens digital push [src-20250326-cc1810] | Structural |

**Factory automation spending.** After two weak years, Roland Berger calls 2026 the first year of renewed growth in industrial automation: up to about 9% a year to 2030, with 6–7% more realistic. Value is shifting from hardware to software, which lets automation reach smaller batches. Pharma and consumer goods are strong; automotive is weak; defense is not yet moving the market [src-20260116-0c4980] (med).

**Robot installs.** The robot numbers in 7.1 show the same pattern: US installs rose 11% in 2025, but only about 3,000 went to metal and machinery [src-20260618-c903cc]. _Meaning [inference]:_ the total market for factory tools is growing again, but most spend still goes to incumbents' hardware; a software startup must sell measurable output, which is why outcome-priced tools like Lumaril (7.10) stand out.

**Robots: where they go, in more depth.** A record 603,307 industrial robots were installed worldwide in 2025 (up 11%), with 5.08M in operation; IFR forecasts 655,000 installs in 2026 and 806,000 in 2029. China installed 354,226 (up 20%), and Chinese brands now supply more than half of China's own installs; the US (38,428, up 12%) passed Japan for second place; Europe fell 14% [src-20260924-28b59b]. US robot density is 307 per 10,000 manufacturing workers (8th in the world), against 1,220 in South Korea and 449 in Germany [src-20260618-c903cc]. _Meaning [inference]:_ the US is under-automated relative to peers, and the robot hardware itself is increasingly Chinese, so US value capture is more likely in software and in owning the production than in making robots.

**Incumbents are growing on the same demand.** Rockwell's fiscal Q3 2026 sales rose 8% (10% organic) with a 49.5% gross margin and software recurring revenue up high single digits, led by semiconductors, data centers and warehouse automation [src-20260804-0e8130]. Siemens bought Altair (simulation and AI) in March 2025 to deepen its software stack [src-20250326-cc1810]. _Meaning [inference]:_ incumbents capture most of the near-term automation spend; startups need a wedge incumbents do not price (for example, outcome-based pricing).

**What buyers say they will spend.** In NAM's Q3 2026 survey, 78.9% of manufacturers were positive, the highest since 2022, but they expect capex growth of only 2.6% over the next year and 80.8% name raw-material costs as their top problem; 63.0% plan to import industrial machinery [src-20260914-b4d55c]. Manufacturing job openings were 522,000 in August 2026 against 432,000 before the pandemic, and average total pay was $112,261 in 2025 [src-20261013-a7c995]. _Meaning [inference]:_ labor is scarce and dear while capex budgets are tight, which favors tools that pay for themselves out of output rather than up-front licenses.

**How much the technology can move costs.** BCG models factory-of-the-future technology (automation and physical AI) raising productivity by up to 60% and cutting labor 30–60% in some plants, with the US leading on readiness; but it finds greenfield aerospace and defense still favors China, and tariffs can blunt the push to invest [src-20260528-a1c5d1]. Robot learning is far from production reliability: about 59–66% success on short tasks versus the 99.9%+ factories need [src-20260904-267293]. _Meaning [inference]:_ the near-term gains come from control and scheduling software on existing equipment, not general-purpose robots.

**Why process plants pay for throughput.** In process industries the plant is the cost: chemical assets need about 80–85% utilization to earn their cost of capital, and Europe's average is about 74% [src-20260401-e2adb0]. US ammonia plants ran at about 80% in 2025 [src-20260206-c8fbbc], and EU chemical capacity utilization was 75% in mid-2026 [src-20260915-e74614]. When a plant is already sold out (US gas-advantaged plants with Middle East disruption lifting demand for their output [src-20260615-0c9b7e]), each extra percent of throughput or yield is near-pure margin, because feedstock, labor and capital are already paid for [inference]. Where plants run below breakeven (much of Europe), better yield lowers cost per ton on the output they do sell [inference]. This is the economic opening for closed-loop control software in chemicals, polymers and biologics.

**Software is where automation value is moving.** Roland Berger expects automation value to shift from hardware to software over 2026–30, with pharma among the strongest end markets [src-20260116-0c4980] (med). Rockwell's growth leaders include life sciences and data centers [src-20260804-0e8130]. _Meaning [inference]:_ the buyers most willing to pay for software control are regulated, high-value process plants (pharma, biologics, specialty chemicals), which is also where a single bad batch is most costly, so trust and validation become the gating factor.

### 7.3 Headwinds, at equal weight

1. **Small factories buy slowly** and churn; budgets are thin [inference].
2. **Incumbents bundle software** with hardware (Siemens, Rockwell) [src-20250326-cc1810][src-20260804-0e8130].
3. **Reliability gap** in robot learning (59–66%) [src-20260904-267293].
4. **Rates and capex caution** reduce equipment budgets (Fed 3.75–4.00%) [src-20260916-f0c016].
5. **Value capture:** a vendor never owns the output margin; the owner-operators in chapters 3–6 may build their own software [inference].

### 7.4 Why vertical integration matters here, and where the logic breaks

- Software and robots are the **means** by which the producers in chapters 3–6 win; selling them separately is a smaller, more competitive business [inference].
- An enabler can still win if it becomes the standard for thousands of small factories (Arda's bet), where owning factories would be too slow.
- **Where it breaks:** if owner-operators build in-house, the enabler market shrinks to job shops that buy slowly.

### 7.5 What would have to be true, and signals to watch

- Usage-based pricing sticks with small factories. **Watch:** Arda's customer counts and retention (claims only so far).
- Robot success rates rise above ~90% in real work. **Watch:** benchmark updates.
- Producers license out their software (Isembard's MasonOS, Mariana's MarianaOS) — a sign enabler value is real.

### 7.6 Macro in more depth

**AI and robotics: enabling, not sufficient.**

- US robot installs grew 12% to 38,428 in 2025 [src-20260924-28b59b]. LLM agents now read CAD and write work instructions (Arda: 10 hours to 15 minutes at Anduril) [src-20261020-914a64]. Freeform runs GPU clusters on site to control each printed layer [src-20260219-2125d7].
- Limits: US metalworking robot adoption is only about 3,000 units a year [src-20260618-c903cc]. Robot learning succeeds about 59-66% of the time on a new task versus 99.9%+ needed on a line [src-20260904-267293]. **Claim (Mehr):** physical AI is at "2007-2008 of LLMs" [src-20260220-0d5345]. **Claim (Nox Metals CEO):** "AI just doesn't know so much of the nuance" of a factory [src-20260325-5b68db].
- **What this means [inference].** AI makes office work around the machine (quoting, programming, instructions) faster today. It does not yet run the machines on its own.

**Oct 26 sourcing update (formerly 0A).**
- **Macro (BCG).** Factory-of-the-future tech can raise productivity up to 60%, and physical AI cut robot training time about 70%. But greenfield aerospace and defense plants still favor China on cost, and tariffs can reduce the pressure to invest [src-20260528-a1c5d1].

**Data loops in general:** see 2.13.

### 7.7 How the industry and its supply chain work

MES (manufacturing execution system) is the software that tracks and directs work on a shop floor. It is the established category.
- **Who:** Arda (turns CAD design files into work instructions) [src-20261020-914a64]; Mind Robotics (robot AI models; The Verge corrected "spinoff" to "a partner of Rivian, but not a spinoff") [src-20261013-cc78c0]; candidates Rapta, Allus, Faraday. Established: Siemens, which bought Altair and Dotmatics [src-20250326-cc1810][src-20250701-a7fef9], and Rockwell (gross margin 49.5%) [src-20260804-0e8130].
- **How it makes money:** **Claim (Arda):** priced by usage [src-20261020-a1e174]; no revenue disclosed.
- **What AI changes:** AI agents that write work instructions are the only shipped product (Arda at Anduril) [src-20261020-914a64] [inference].
- **Risks:** Siemens and Rockwell own the customer relationships, and the host plant owns the data [inference]. An investor says the AI is not the limit; the value needs connected plant data and new workflows [src-20261006-6265ad]. Mind has raised over $1B and shown no robot publicly [src-20261013-cc78c0]. Bright Machines, an earlier "software-defined factory", failed to go public via SPAC (a shell-company merger) and pivoted to assembling AI servers [src-20240926-fd90fb].
- **Enablers arm the incumbents.** GrayMatter Robotics tried selling autonomy software, found "that model doesn't really work", and now rents turnkey sanding and painting cells "as a service" [src-20261022-3335bd]. **Claim (GrayMatter):** Riddell went from about 300 to 1,700 helmets a day on the same robots after software updates [src-20261022-3335bd]. If old shops can rent this, automation alone stops being an edge [inference].
- **AI for machine programming and inspection.** CAM is the software that turns a 3D model into machine instructions. CloudNC's CAM Assist writes basic machining plans in minutes inside GibbsCAM, with a human checking each step; CloudNC tests it in its own factory [src-20261021-9769d1][src-20261009-7cafd0]. AI Robotics, a Korean university spinout, inspects welds on 24 production lines in 3 countries, using over 4M data points [src-20261011-a8b14d]. Both sell the same tools to incumbents [inference].
- **What this means [inference]:** this layer sells "picks and shovels". It may help old shops catch up as much as it helps new ones.

**Market size (this industry).** Global industrial robot installs worth $18.6B in 2025 [src-20260924-28b59b] (a proxy: robot spend, not software). Automation market growth of 6–7% a year expected to 2030, up to about 9% [src-20260116-0c4980] (med). Closed-loop process-control software (Lumaril's market) has no free market size [gap].

### 7.8 Where AI and automation help

Work instructions from CAD, inventory and kanban automation, vision inspection, robot programming and CAM automation.

### 7.9 Right to win, unit economics and data loop

**Data loop (score 0–3; scale in 2.13):**

| Company | Score | How the loop works | Best evidence / what is missing |
|---|---|---|---|
| Arda | 1 | Agent improves with host's design data | [src-20261020-914a64]. Missing: who owns the data |

### 7.10 Companies, grouped by label

**Enabler**

#### Lumaril (enabler; AI closed-loop control for process plants; fuller profile)

**What it does (company claims, Lumaril site) [src-20261027-d5ba3f].** Lumaril describes four steps: **Connect** to a plant's existing control systems, adding cheap off-the-shelf audio and video sensors with "no rip-and-replace"; **Understand** the plant by building a real-time model of it; **Decide** using classical control plus AI and machine learning; **Act** by changing setpoints (the target temperatures, pressures, speeds and flows operators normally set) and control logic itself, through a safety layer, to raise throughput and yield. Target markets: manufacturing, chemicals, biologics, oil and gas, agriculture and polymers. **Claim (Lumaril):** "We're paid on the production we add." Lux Capital, its investor, describes the product as codifying operator expertise and running deep learning on event-driven plant data for near-real-time decisions [src-20261027-311fa6]. A funding database says it adjusts PLC setpoints, updates control logic and coordinates labor (low) [src-20261003-496a99].

**Team [src-20261027-d5ba3f].** Co-founders Mark Elliot (creator of Palantir Foundry, Palantir's commercial CTO, later CTO at Theorem, earlier a Lockheed engineer) and Ben Duffield (co-creator of Foundry and Foundry group lead). Kim Lear runs operations (ex-Palantir, Zipline); Steve Frost runs business development (ex-Anduril, US Marine Corps). Offices in New York and El Segundo.

**Funding.** Founded 2025; $12M seed led by Lux (low) [src-20261003-496a99][src-20261027-311fa6]. A WSJ Pro headline (Oct 27, 2026; article paywalled, only the free headline and summary read) reports $66M raised at a $400M valuation [src-20261027-79ddd6]. Customers, revenue and measured yield gains are not public [gap].

**Why it is the closest software play to the core thesis [inference].** Our thesis backs companies that own production and sell output, because they keep the margin and the data. Lumaril does not own a plant, but it copies the two things that matter:
1. **It is paid like a producer.** Normal factory software is sold per seat or per site, whether or not output rises. Lumaril says it earns a share of the extra production it creates. Its revenue rises and falls with the plant's output, like an owner's, and the plant pays nothing if nothing improves. That removes the main reason plants say no to new software.
2. **It runs the plant, not a dashboard.** Most AI tools advise a human, who may ignore the advice. Closed-loop control means the software itself moves the setpoints, within safety limits, many times a day. So Lumaril is the one learning from every change it makes, which is the data loop our producers get from owning plants (2.9), without buying the plant.
Together this is "owner economics without owner capital": a capital-light route to the same margin and data. It also lets SPC back the thesis in process industries (chemicals, polymers, biologics) where building a new plant costs hundreds of millions.

**Label: enabler.** It sells to other companies' plants; it does not own production. Tracked outside the core, but the strongest enabler in the primer.

**Bear case.**
- **No plant, no moat on the asset.** The plant owner can end the contract, and owns the physical capacity and the customer [inference].
- **Strong incumbents.** Honeywell, AspenTech (Emerson) and Emerson already sell advanced process control (APC) and optimization into the same chemical and refining plants, with decades of installed base [inference].
- **Trust is the gate.** Plants rarely let outside software change setpoints in closed loop; one safety incident or off-spec batch can end a deployment. Winning that trust takes years per site [inference].
- **Attribution fights.** Outcome pricing needs agreement on what output would have been without Lumaril; feedstock, weather and demand changes make that disputable [inference].
- **Early.** Founded 2025; no public customer results [src-20261003-496a99].

**Next step [inference].** Ask for one plant's before/after throughput and yield, how the baseline is set for pricing, how closed-loop control was approved by the plant's safety team, and the share of revenue that is outcome-based today.

#### Arda (factory software for manufacturing engineers; enabler / software; does not fit, competitor and comparable)

- **What it does:** Arda is an IDE (a work environment) for manufacturing engineers with an AI agent inside. The agent reads a product's CAD and design files, works out the assembly sequence (using robotic motion planning under the hood), lays out stations and writes the work instructions for an engineer to review. When the design changes, it updates the line [src-20261020-a1e174]. **Claim (Bob McGrew, CEO):** "a user interface and an agent that does for manufacturing engineers what Claude or Cursor does for programmers"; "when a design changes, you can retrain a human in a day — but it takes three to six months in order to change the automation" [src-20261020-9be48d].
- **Customers:** Anduril is design partner, anchor customer and the only named user. Arda runs inside Anduril's ArsenalOS manufacturing software and, per its lead investor, in every Anduril division [src-20261020-a1e174]. **Claim (Arda/Anduril):** work instructions from about 10 hours to 15 minutes, and complex engineering from up to 30 hours to about 2.5. Anduril's COO: "We would be behind on our production goals without it" [src-20261020-a1e174]. **Claim (Arda):** a 2,000-part missile avionics box was planned in two days [src-20261020-878aa9]. **Claim (Altimeter):** Arda already works with makers of transformers and electrical gear for data centers, where large power transformers averaged about 128 weeks of lead time [src-20261020-a1e174].
- **What it means [inference]:** not a target under the new theme, since Arda does not make or sell product. It matters as (a) a tool that could give incumbents and primes the same speed edge that integrated producers claim, and (b) a valuation comparable for factory software.
- _More detail: Appendix D (Arda)._

#### Mind Robotics (factory robotics AI; enabler; does not fit)

- Trains robot AI for factory tasks (picking, fastening, plugging in connectors) and sells robots, not parts [src-20261022-eede0b]. Rivian is partner, first customer and shareholder: "a partner of Rivian, but not a spinoff" [src-20261013-cc78c0]. It depends heavily on Rivian and has raised over $1B, with no public product [src-20260515-176e26].
- **More specifics:** Mind uses Rivian as "a live, high-volume manufacturing environment for model training"; Rivian owns 32.1% [src-20261013-58de15].
- **What it means [inference]:** sells robots and models to plants (first Rivian); a comparable for the 'physical AI' enablers, not a producer.

**Mentions:** CloudNC (CAM automation) and GrayMatter (robot programming) — not profiled this run.

### 7.11 Bear case, at equal weight

- Siemens and Rockwell bundle and own the installed base [src-20250326-cc1810][src-20260804-0e8130].
- Producers may build in-house (Hadrian Opus, Isembard MasonOS, Mariana MarianaOS).
- Robot-learning reliability 59–66% [src-20260904-267293].
- Lumaril-style closed-loop control must beat Honeywell, AspenTech and Emerson APC and win plant trust (7.10).

### 7.12 Key sources

- IFR World Robotics [src-20260924-28b59b][src-20260618-c903cc]; robot-learning benchmark [src-20260904-267293]
- Rockwell [src-20260804-0e8130]; Siemens [src-20250326-cc1810]; Deloitte outlook [src-20251112-669746]; BCG [src-20260528-a1c5d1]
- BEA/JOLTS openings [src-20261013-a7c995]; ISM [src-20261008-89df84]; NAM [src-20260914-b4d55c]
- Roland Berger automation 2026 [src-20260116-0c4980]
- Lumaril [src-20261027-d5ba3f][src-20261027-311fa6][src-20261003-496a99][src-20261027-79ddd6]
- Arda [src-20261020-a1e174][src-20261020-914a64][src-20261020-8d7abc]


### 7.13 Listen & watch

Full list: Appendix E._

1. ★ **"Building Factory SuperIntelligence with Ariyan Kabir"**, *Machine Minds*, length not listed. [▶ Open link](https://machineminds.buzzsprout.com/2212148/episodes/19077384-building-factory-superintelligence-with-ariyan-kabir) — *Why:* GrayMatter moved from licensing software to selling robot cells as a service, which tests the thesis. Repo: src-20261022-3335bd.
2. **"Former top OpenAI employees raise capital for defense startup valued at $1.5B"**, CNBC, Oct 16, 2026, short clip. [▶ Open link](https://www.cnbc.com/video/2026/10/16/former-top-openai-employees-raises-capital-for-defense-startup-valued-at-1point5b.html) — *Why:* Arda on the 3–6 months it takes to retool factory automation. Repo: src-20261020-878aa9.
3. **"Mind Robotics: Building the AI-Native Robotics Platform"**, Kleiner Perkins, May 13, 2026, 4 min. [▶ Open link](https://www.youtube.com/watch?v=fc9GB9Yz75Y) — *Why:* Rivian's line as Mind's live data loop. Repo: src-20260513-abe9cf.
4. **"Big Ideas 2026: Physical AI and the Industrial Stack"**, a16z Podcast, Dec 25, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/big-ideas-2026-physical-ai-and-the-industrial-stack/) — *Why:* how investors frame the software layer going into 2026. Repo: src-20251225-725014.
- *Gap:* no free Lumaril podcast or founder interview found (searched Oct 27, 2026). Use the primer profile (section 7.10).

### 7.14 Commercial traction and incumbents

_Labels as in 3.14._

| Company | Status | Evidence |
|---|---|---|
| Arda | **Revenue (one customer)** | Anduril is the only named customer [src-20261020-a1e174]. |
| Mind | **Revenue (first customer)** | Rivian is its first customer [src-20261013-cc78c0]. |
| GrayMatter Robotics | **Revenue** | Rents turnkey robot cells "as a service" after software-only sales did not work [src-20261022-3335bd]. |
| Lumaril | **Lab / pre-revenue** | No public customers [src-20261003-496a99]. |

**Revenue vs lab.** Robot cells sold as a service have revenue; AI control software is mostly first-customer stage.

**Incumbents.** Rockwell and other controls vendors own the installed base [src-20250326-cc1810][src-20260804-0e8130]. _What they do better:_ certified hardware and plant trust. _Where startups win [inference]:_ new factories (often the producers in chapters 3–6) with no legacy system.

**Regulation and qualification.** Little formal regulation; the hurdle is customer qualification and, for defense customers, ITAR and cybersecurity rules (4.14).

**5-year outlook (to 2031).** **Possible**, as tools inside producers rather than standalone winners. **Bear case, equal weight:** see 7.11. Software-only models have struggled (GrayMatter's pivot) and incumbents can bundle similar features.

## 8. Competition and incumbents

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

### 8.1 The right to win: versus job shops, contract manufacturers and overseas

**The question.** Why would a buyer use a new AI-native producer instead of a local job shop, a contract manufacturer (CM, a firm that builds to someone else's design), or a cheaper overseas supplier?

**Arguments for the new producers.**
- **Old shops are slow to quote and run like consultancies.** **Claim (Power):** legacy shops "operate like consulting businesses", reselling $60-an-hour labor at $120 [src-20250509-22b78a]. **Claim (SendCutSend):** job shops need months-long runs to "make their margin back" [src-20260624-3dc6f7]. **Claim (Nox):** a competitor's quote took about 8 hours per email round versus 10 seconds [src-20261022-3135b5].
- **Buyers like one roof and good paperwork.** The ex-customer FlyX CEO came back to Hadrian for "everything under one roof" and because it is "one of the few that give you the proper documentation"; Xometry's marketplace was a "big headache" [src-20260806-3a2ec7]. A Raytheon engineer values that Hadrian is 30-45 minutes away, takes 3D model files directly rather than drawings, and showed lower part-to-part variation "than compared to our traditional suppliers" [src-20260823-b3713f].
- **Responsiveness.** An Anduril engineer praises a dedicated project manager and 24-hour responses versus mom-and-pop "radio silence"; in-machine probing cut one lead time by about 40% (7 days to 2-3) [src-20250623-5bc67c].
- **Greenfield beats retrofit.** **Claim (Power):** after 12 months studying legacy certified shops, they were maybe 30% more efficient after upgrades, so Hadrian built new [src-20260908-65fab6]. "You can't automate unless you standardize the hardware": 40 different machines explode the software work [src-20240622-b8cd8b]. A BMW strategy manager says a new robot-first plant could need 20-40% fewer people, while old plants with spare labor "none of them is really thinking about greenfield" [src-20261014-ce5195][src-20261021-25a598].
- **Overseas loses on protected and urgent work.** Defense rules and ITAR keep work onshore (section 3.6). **Claim (Isembard):** a new local factory cut lead time from about 10 weeks to under 14 days and "can match on price" for one warehouse customer [src-20260310-cdfd82]. **Claim (VulcanForms CEO):** "we're winning business back from overseas" [src-20261005-f3f30a].

**Arguments against (equal weight).**
- **Machining is crowded and easy to enter.** A Rolls-Royce engineer: there is "no shortage" of machine shops; it is the easiest entry path [src-20251120-0c271b]. Legacy shops still win big defense work: Bender CCP holds a $40M part of a $944M Navy repair program, paying machinists $35-45 an hour [src-20261018-2b4a22].
- **Incumbents automate too.** Northrop's new Virginia plant claims about 20% lower recurring cost [src-20261022-1389b7]; L3Harris says AI improves yields at its rocket-motor plant, with deliveries up 60% [src-20261022-869770]; GE invested $600M in three years once demand was certain [src-20261014-47f64b]. FlyX's CEO thinks an incumbent could build this automation "organically" [src-20260806-3a2ec7].
- **Buyers design for many vendors.** The Anduril engineer wants "a dumb way of making parts" so "four or five different vendors can make the parts", because "I don't know how long you will be in business"; he will not switch for "5%-10% cash back" and avoids vendors near 100% capacity [src-20250623-5bc67c].
- **Speed alone is "AI-washing" risk.** Freeform's CEO: legacy processes "haven't really fundamentally changed ... We can slap iPads on things and epoxy floors"; "ask them exactly how" they use AI [src-20261020-bac9ca]. Interested party, but a sharp test.
- **China still wins on cost in open markets.** **Claim (Power):** US aerospace parts cost "two to three times" China's, and prototypes "eight to 10 times" [src-20250509-22b78a]. A DoD study: China can deliver a finished forging "for the same cost that a U.S. forge will pay for the raw materials" [src-20220801-c32e19].

**What this means [inference].** New producers win on responsiveness, documentation and greenfield design, in markets protected from China. They do not win on price alone, and incumbents are closing the automation gap.

## 9. Customers and repeat orders

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

### 9.1 How buyers qualify suppliers and reorder, step by step

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

## 10. Capital and financing

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

## 11. Policy tracker (newest first)

**How to read this.** Section 2.3 explains each tool. This is the dated list, in plain words.

| Date | Policy | What it does | Source |
|---|---|---|---|
| 2026-11-27 (deadline) | China Ga/Ge/Sb US-export ban suspension ends | Ban returns unless extended; germanium already at a record | [src-20261027-f82d55] |
| 2026-11-10 (deadline) | China Oct-2025 rare-earth controls suspension (No. 70) ends | Broad controls return unless extended | [src-20261019-854e22] |
| 2026-11-01 (deadline) | OSC fund-finance applications due | $500M-$1B of loans per fund | [src-20260831-4dd3b7] |
| 2026-10-08 | Genesis Mission Phase II awards | 12 awards worth $159M; 297 first-year projects | [src-20261008-452806] |
| 2026-09-16 | FOMC hike | 3.75-4.00% | [src-20260916-f0c016] |
| 2026-06-18 | OSC rare-earth loans | $725M Energy Fuels, $500M Phoenix Tailings (conditional) | [src-20260618-184e0c] |
| 2026-06 | Section 232 adjustment | Further changes to the steel, aluminum and copper tariffs | [src-20260602-b995e2] |
| 2026-01 | IRS Notice 2026-11 | 100% bonus depreciation made permanent | [src-20260114-2075f7] |
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

## 12. Companies worth attention

**How to read this.** "Target" means worth a diligence call now. "Candidate" means worth watching. "Benchmark" means too expensive for SPC but useful for comparison. "White space" means a gap with no strong company yet.

**Targets.**
- **Senra** (Manufacturing; fabrication, electrical assemblies): Series B size, real customers, its own software. Next: founder call; ask for first-pass yield and repeat-order data.
- **Freeform** (Manufacturing; precision): the best-evidenced loop; $179M valuation. Next: customer reference calls (Boeing, DIU).
- **Isembard** (Manufacturing; precision, franchise): a capital-light Hadrian variant; valuation undisclosed; Thales' procurement chief is skeptical [src-20251110-84b67e]. Next: economics per franchise, and how primes would audit franchised sites.

**Enabler worth attention.**
- **Lumaril** (enabler; AI closed-loop control for process plants): built by the creators of Palantir Foundry; a WSJ headline reports $66M raised at a $400M valuation [src-20261027-79ddd6]. It is the closest software play to our thesis because it is **paid on the production it adds** (company claim) and **runs the plant's controls itself** in closed loop, so it earns like an owner and learns from every change it makes, without owning the plant [src-20261027-d5ba3f] [inference]. Bear: no plant; Honeywell, AspenTech and Emerson APC incumbents; plants must trust it to move setpoints. Next: one plant's before/after yield and how the pricing baseline is set. Full profile: 7.10.

**Candidates.**
- **Earth AI** (Raw Materials, Stage A; hybrid explorer): owns most of its claims, drills them itself and plans to sell proven deposits; $20M Series B (Jan 2025) [src-20250127-c28430]. Next: drill results at Fontenoy and a timeline to a formal resource estimate. Profile: 3.10.
- **Fabri** (Manufacturing; castings): castings are about 40% of munitions (claim, Power) [src-20260921-876080]; backed by RTX and Lockheed. Next: a second source.
- **1872** (Manufacturing; fabrication): cheap entry, energy skids. Next: track to its first repeat order.
- **Atomic Industries** (Manufacturing; precision, plastic molding): AI-designed molds plus its own presses; claims multi-year part contracts (section 4.10). Next: a buyer call to confirm repeat programs.
- **Machina** (Manufacturing; precision): depot demand. Next: verify valuation.

**Benchmarks.** Hadrian, Divergent, SendCutSend, Mariana and Amca are priced at $1B-$7.9B. (Oct 26 run: no new candidates added; Mariana's project-level financing [claim, src-20261024-c53370] lowers its equity need but doesn't change its tier.) Periodic, CuspAI, Mind and Arda are priced before product; watch for revenue.

**White space.**
- Manufacturing (metal supply): software for mid-size metal distributors: about 9,400 sites, with the top 50 holding half [src-20251201-4b732d]. We passed on Nox.
- Manufacturing, forgings: the Pentagon flags castings and forgings as hard to enter [src-20220215-45c353]; no AI-native forger is in the repo.
- Manufacturing, inspection as a service: inspection takes as long at Hadrian as at legacy shops [src-20260908-ed94f0].

**What this means [inference].** SPC's entry is a Series B in Manufacturing (fabrication or a franchise-style variant), with Lumaril as the one enabler worth a call, not the expensive leaders.

## 13. Bottom line

**Five conclusions.**
1. The category is real, but proven demand is narrow. Most buyers value flexibility, scale and total program cost over speed [src-20260921-876080]. Paid demand is speed on prototypes and low-rate work. These startups hold 2-10% of spend at the primes we spoke to [src-20260802-ef6506][src-20260802-36d46c].
2. The data loop has partial evidence (score 2) only where the process is continuous: Freeform, Mariana, Radical, plus Hadrian's faster training. Nobody shows improvement over time (section each chapter's data-loop section).
3. Capital falls into three tiers: capital-light owner-operators (SendCutSend, Senra); capital-heavy owner-operators funded by debt and government (Hadrian, Vulcan, Mariana); and software vendors that need someone else's plant (Arda, Mind) [inference].
4. Precision & Defense Hardware is priced out at the top: Hadrian $7.87B [src-20260807-b0dc5b], Amca over $1B [src-20260520-af3e6c]. SPC's entry is Series B in fabrication or a hybrid or franchise model [inference].
5. Policy money lands mostly on metals supply: OSC, tariffs including copper, IEA finance, and DPA awards to rare earths and rocket motors [src-20251103-ee9b27][src-20260402-1b5d6c][src-20250805-80f2f4][src-20261019-68fd3d]. The FY26 defense law adds robotic munitions automation and a fund for castings, forgings and machine tools, but no money has reached tracked startups yet [src-20251218-f0d6ef]. Precision parts gets its pull through prime contracts instead [inference].

**Our pick per layer and model [inference].**
- Metals supply: Vulcan and Mariana as benchmarks; distributor software as white space.
- Fabrication: **Senra** (pick); SendCutSend (benchmark); 1872; Machina (hybrid); Path Robotics (enabler).
- Manufacturing, Precision & Defense Hardware: **Freeform** (pick); Fabri; **Isembard** (hybrid pick); Hadrian and Divergent (benchmarks).
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

### 13.1 The bear case in one list

- **Repeat orders are still tiny.** Hadrian's Raytheon spend is "in the tens of thousands" during probation [src-20260823-b3713f]; Divergent's FY25 Air Force awards were about $3.64M [src-20250924-22c5ee]; Mach's federal awards are R&D-scale [src-20260630-fdc552].
- **Customers churn when work gets cheaper.** FlyX left Hadrian over cost as drone work became "less stringent" [src-20260806-3a2ec7].
- **Primes keep sourcing broad.** Buyers want "four or five different vendors" and cap each at 25-30% of their spend [src-20250623-5bc67c].
- **Robots don't pay yet.** BMW's strategy manager: humanoid ROI "would still be probably negative" [src-20261021-25a598]; BMW has no Figure robots running now [src-20261014-ce5195].
- **Defense demand is lumpy.** One defense company got "90% of revenue from congressional marks" (low confidence) [src-20261022-f423ef]; stop-start budgets are "brake and then the accelerator" [src-20260901-a44eee].
- **Incumbents are booming and investing.** Carpenter's specialty-alloy margin hit 37.7% [src-20261022-679fcc]; Howmet absorbed about 720 extra staff in six months [src-20260630-bd78e7]; Nucor credits "supportive federal trade policies" for record shipments [src-20260727-787ce9].
- **AI tools are for sale to everyone.** CloudNC's AI CAM tool is in 1,000+ shops, including Lockheed's [src-20260908-f98d21].
- **Budget gating (Oct 26).** Carpenter's defense bookings are down because funds haven't reached customers [src-20261022-de5e6c]; 82% of the FY27 munitions request rests on reconciliation [src-20261007-c6f64e]; Reliance is taking share with no AI [src-20261022-1e6872].
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
- Raw Materials (Stage B): refining TAM and economics: no free source found.
- Manufacturing: fabrication TAM: none; Census CBP gives counts and payroll only [src-20250626-23f6d9]. Next: 2022 Economic Census receipts by NAICS 3323/3327.
- AI/robotics cost decline over 24 months: no source.
- Golden Dome amounts: the NDAA funding tables reference Golden Dome funds; size and recipients unconfirmed [src-20251218-f0d6ef]. Freeform Skyfall go-live: unconfirmed.
- ABL use by startups: none evidenced.
- Exits (Q14): no comparable acquisition above $100M in repo.
- Chemicals: no clean free US revenue TAM; ammonia volumes only [src-20260206-c8fbbc].
- Raw Materials (Stage A): Earth AI has no published resource estimate; its 75% success rate is self-reported and undefined [src-20250127-c28430].
- Advanced Materials: no market size for materials R&D or US cathode demand in dollars.
- Enabling Software: Lumaril customers, revenue and measured yield gains are not public; WSJ article body is paywalled (headline only) [src-20261027-79ddd6].

## Appendix C. Source coverage (ledger, 2026-10-25)

Per-source ledger: `insights/exports/primer-ledger.csv`; reading notes kept outside the PDF.

| Bucket | Read status |
|---|---|
| Expert calls (all 28 on-thesis) | Read in full, line by line |
| Podcasts | All 102 read in full (40 earlier, 62 in v3). v5 re-reviewed every reading note (expert calls, podcasts, cited and uncited sources) and added sections 2.5, 5.20, 2.13, 8.1, 9.1, 9A.1 and 12.1 (v5 numbering; now 2.15, 5.x profiles/5.7, 6.1, 7.1, 8.1, 10.1, 13.1). Not citable: 3 files with no transcript (e5f014, da4c3f, 725014). Not cited: one unverified secondary summary (a51ab2) and two duplicates (aafb71 = 8f85ca; dad375 = 876080). Excluded R&D labs (Periodic, CuspAI, Radical) used only for data-loop context |
| Sources the primer cites (~200) | Read in full, except: the FY26 NDAA (about 517K words) checked against every primer claim plus the manufacturing, munitions, reshoring and tariff sections; the DIU guidebook and the boilerplate parts of 10-Q/10-K filings (e.g. ATI) skimmed |
| On-thesis sources not cited (~390) | Read in full; 99 turned out to be a title or placeholder only. One 589K-character academic review of self-driving labs not read (general background) |
| No real text captured | Fast Radius (SEC block page), VulcanForms layoffs, Siemens (menu JSON) and other stubs: claims citing them were removed |
| Form D / award stubs, noise, duplicates | Data rows checked; category confirmed by keyword scan, not read line by line |

Honest limits: the long filings above were not read line by line. Podcast claims are speakers' words on friendly shows, several sponsored or investor-hosted; they are labeled as claims. Funding and valuation discrepancies were dropped by design.

## Appendix D. Profile and deep-dive detail (moved from the chapters)

**Chemicals: other notes carried from v8** (verified where cited):**
- **CuspAI, Orbital, Periodic, Lila:** see 5.4. CuspAI is an enabler (Kemira makes the PFAS sorbent). Orbital is the closest to a producer, since it makes and sells its own fluid.
- **LanzaTech (gas fermentation to chemicals and fuels; bear case):** its FY2025 10-K flags substantial doubt about continuing as a going concern, with $13.2M cash and a $1.0bn accumulated deficit [src-20260331-20d171].
- **Zymergen (synthetic biology; failed):** see 4B.7 [src-20220101-9c58e3].
- **Zapata (quantum and generative-AI software, including chemistry; failed):** wound down in Oct 2024 because its assets did not cover its obligations [src-20241011-721c93].
- **Geno (Genomatica), Debut, Iambic, Isomorphic, IBM RXN, Synthia, PostEra:** not separately sourced this run. Geno and Debut are biomanufacturing comparables; Iambic and Isomorphic are pharma molecule-design comparables (enablers, not producers); IBM RXN, Synthia and PostEra are synthesis-planning tools. Treat them as names to verify, not evidence.

**Chemicals: business models and unit economics**

1. **Own the plant and sell the chemical (fully vertically integrated).** Solugen is the archetype. Revenue is per kilogram; margin depends on yield, feedstock and logistics. Highest capex; best fit for SPC's producer thesis.
2. **Robotic CRO (make molecules for others, fee for service).** Chemify and Warp Sciences. Revenue per compound or per project, plus possible IP upside. Cash comes earlier, but it is a services business until automation lowers unit cost.
3. **Design partner or licensor.** CuspAI, Iambic and Isomorphic (pharma comparables). Paid in fees, milestones or royalties; someone else makes and sells the product (see 4A.5).
4. **Software.** Retrosynthesis and lab-informatics tools (Synthia, IBM RXN, PostEra's tools). Low capex but weak pricing power; Zapata shows the downside (4B.7).
5. **Biomanufacturing platform.** Engineered microbes or enzymes licensed or used in-house (Geno, LanzaTech, Debut). History is poor (4B.7).

**Claim (Cronin, Chemify):** customers pay for molecules, for software access, and for co-discovered assets with shared upside; Chemify had 12 customers and expected 20 big ones the next year, and aims to be cash-flow positive within a venture cycle [src-20250724-0f42f3].

**Chemicals: data loop**

Chemistry's public data (patents, papers) mostly records successes and leaves out failed reactions. A company that runs its own robots captures every run, including failures, in a form a model can learn from. Lightspeed's Warp memo makes exactly this argument: each run yields both chemistry results and robotics and process data, used to run the lab better and to choose what to make next [src-20261022-b542e2]. Cronin says Chemify has converted a few hundred thousand published reactions into its chemical programming code and versions every run [src-20250724-0f42f3]. [inference] The loop is real only if volume is high and the data stays with the operator. Pharma customers often keep the data rights, the same problem CuspAI faces (4A.6).

**Best things for Brooke to read and listen to (chemicals)**

1. **Y Combinator podcast, "Inside the startup reinventing America's trillion-dollar chemical industry" (Solugen, Mar 2026)** — https://www.ycombinator.com/library/NO-inside-the-startup-reinventing-america-s-trillion-dollar-chemical-industry — The best 13-minute intro to a vertically integrated AI- and bio-enabled chemical producer.
2. **Jim Rutt Show EP 312, Lee Cronin on Automating Chemistry (Jul 2025)** — https://jimrutt.substack.com/p/ep-312-lee-cronin-on-automating-chemistry-f9f — Chemify's "code to molecule" vision and business model, in the founder's words, with a free transcript.
3. **CFR, "The Pharma Choke Point" (2026)** — https://www.cfr.org/reports/the-pharma-choke-point — The clearest account of China's hold on drug starting materials, with shortage scenarios.
4. **Cefic/Roland Berger, European chemical closures radar 2022–2025** — https://cefic.org/app/uploads/2026/01/European-Chemical-Closures-and-Investments-Radar-2022-2025.pdf — Hard numbers on Europe's chemical shrinkage.
5. **Sarah Constantin, "What's Behind the SynBio Bust?"** — https://sarahconstantin.substack.com/p/whats-behind-the-synbio-bust — The best bear case on biomanufacturing economics.
6. **Lightspeed, "Why We're Backing Warp" (Oct 2026)** — https://lsvp.com/stories/why-were-backing-warp/ — A concise investor case for robotic US chemistry CROs and the lab data loop.
7. **Section 232 pharma proclamation (Apr 2026)** — https://www.whitehouse.gov/presidential-actions/2026/04/adjusting-imports-of-pharmaceuticals-and-pharmaceutical-ingredients-into-the-united-states/ — The actual tariff rules driving pharma onshoring.
8. **Schondelmeyer USCC testimony (Jun 2025)** — https://www.uscc.gov/sites/default/files/2025-06/Stephen_Schondelmeyer_Testimony.pdf — The data on how US generics depend on China through India.
9. **Manufacturing Chemist, "Where Zymergen went wrong"** — https://manufacturingchemist.com/where-zymergen-went-wrong-a-biomanufacturing-perspective-for-synthetic-biology-204177 — A short lesson: scale-up and customer qualification kill companies, not discovery.
10. **Industrial AI Podcast, "Max Welling's CuspAI" (Feb 2025)** — https://podwise.ai/episodes/2974143 — The materials-design view from CuspAI's co-founder (listed, not yet transcribed into the repo).

**Chemicals: bull case**

- **Real, dated policy pull** for US-made APIs and KSMs, through tariffs, BIOSECURE and the onshoring EO [src-20260402-ecae19][src-20260110-4db409].
- **Europe's retreat leaves supply gaps** in specialty and intermediate chemicals that customers must re-source [src-20260115-ec35af].
- **Process innovation is a real cost lever:** a 96% versus 60% yield claim, if true at scale, is a structural advantage (Solugen's claim) [src-20260320-f90e80].
- **Owner-operated robotic labs** may produce the proprietary failure data that public chemistry lacks [src-20261022-b542e2].

**Materials: unit economics and who pays**

- **Software (Citrine, Uncountable, Albert):** annual contracts in the hundreds of thousands to low millions of dollars per enterprise. Procurement pushes back on high prices [src-20260913-3ad55e]. Gross margins are software-like, but the market is capped by R&D budgets.
- **Discovery projects (CuspAI, Periodic):** 5–15% gross margin on custom work, 85–90% on the platform. Conversion of 40–50% of pilots. Royalties of about 1% (bulk) to 3–5% (specialty), often refused [src-20261016-29997e] (med). Chemical majors refuse royalty deals [src-20260913-3ad55e].
- **Per-candidate (pharma-style):** buyers come through CROs and pay per successful candidate [src-20260909-af3e60] (low).
- **Government:** AFWERX awards of about $1.2M [src-20250825-300a14]; Genesis Phase II awards averaging about $13M ($159M across 12) [src-20261008-452806]; ARPA-E and DARPA.
- **Owner-producer:** product gross margin. A specialty fluid or alloy might earn 30–60% if it is differentiated; commodity cathode much less [inference].

**The math [inference].** Take a specialty material with $200M a year of sales and a 3% royalty. That is $6M a year to the designer, years after the project, and only if it ships. A lab valued at $3–8B would need dozens of such hits. The same material made by the designer at a 40% gross margin earns $80M. This is why the money is moving toward owner-producers (Orbital) and why CuspAI-type firms are pushing for royalties.

**Materials: data loop**

- **For:** SDLs create negative results and process data that no public set has. Radical says its 300 alloys in 16 weeks compares with 3,493 studied in 20 years [src-20260807-52b690]. Citrine aggregates 70k experiments a month across customers [src-20261022-267188].
- **Against:**
  - Customers often keep the data rights [src-20261016-29997e].
  - Public datasets (OMat24's 110M+ calculations) close the computed-data gap for everyone [src-20130101-5e5543].
  - Each material class needs its own loop: an alloy loop does not help with sorbents.
  - A 2026 hype-versus-reality review of SDLs says that A-Lab's results needed correction [src-20260709-1159ab][src-20240124-513fd9].
- **Verdict [inference]:** the loop is real within one material class and one lab. It is weaker across customers and classes than in factory machining, where every part feeds one quoting model.

**Materials: right to win**

- **Incumbents:** BASF, Dow, Johnson Matthey, Kemira and Albemarle have process know-how, plants and qualification relationships, and they partner rather than build (BASF–Orbital [src-20261022-edad3e]; Kemira–CuspAI [src-20260521-f4b51b]; JM–Kebotix [src-20210803-6788dd]).
- **Big tech:** gives models and data away, so the model alone is no moat.
- **National labs:** Genesis and partners like Sandia are both funder and competitor [src-20260929-dfb65a][src-20261008-452806].
- **Startups win where [inference]:**
  1. They own the physical throughput (Radical, Lila).
  2. They pick a product where the buyer is in a hurry and the incumbent has nothing (PFAS-free coolants, PFAS sorbents, hypersonic alloys, rare-earth-free magnets).
  3. They make it themselves, or lock in a royalty and a supply role.
- **Ranking by fit to SPC's producer thesis [inference]:** Orbital > Radical > Mitra Chem > CuspAI > Periodic > Lila.

**Materials: bull case**

1. **Policy pull:** mineral controls (2.6) and PFAS bans create buyers who must replace a material, not just optimize one.
2. **Defense pull:** hypersonic, propulsion and munitions materials have funded test paths (Radical with AFWERX and RTX) [src-20250825-300a14][src-20250718-d46f24].
3. **Throughput really is up an order of magnitude** (Radical, Lila, CuspAI claims) [src-20260807-52b690][src-20260925-679418][src-20260521-f4b51b].
4. **Data-center demand** gives a fast, rich buyer (Orbital with AWS) [src-20260528-375aec].
5. **Public infrastructure** (Genesis, national labs) lowers the cost of compute and testing for startups [src-20261008-452806].

**Materials: what SPC should do**

- **Treat discovery-only labs as out of scope for producer investments.** Track them as a source of materials for the companies we do back.
- **Pursue owner-producers like Orbital,** and labs moving into production (Radical with a melt and forge partner; Mitra).
- **Diligence questions:**
  1. Which material is in customer qualification, with whom, and what is the spec?
  2. Who makes it at scale, and who owns that margin?
  3. What data rights do you keep?
  4. What do you get in revenue per hit, and how many hits a year?
  5. What happens when GNoME, MatterGen or Genesis make your model free?
- **Watch list:** Orbital's 2027 GPU qualification; RAI-939 spec-sheet data; Kemira scale-up; Periodic's first named customer; Mitra's Michigan plant FID (final investment decision).

**Parts: more unit-economics inputs**

- **How a job shop prices.** A vendor guide (low confidence) puts 3-axis CNC time at $35-75 an hour and 5-axis at $75-150; shops aim for 75-85% machine use; markups run 25-40% on prototypes and 15-25% on production; one case shop netted 4-5% [src-20261023-58b5a8]. Inspection adds $50-150 a part and material markups run 18-35% [src-20261023-6ef991] (low).
- **Margins along the chain.** **Claim (Mehr):** supply-chain shops run 10-15% margins [src-20250427-5bd04d]. Primes earn about 7-12% on cost-plus contracts [src-20260501-4e5b9a]. A Rolls-Royce engineer: simple parts go "as low as 7%, 8%", complex low-volume parts need double digits; his former $50-60M-a-year Tier-1 had 450-500 staff [src-20251120-0c271b]. Anduril's gross margin is 36-38% with a $1.2B operating loss (Contrary, an investor) [src-20260501-4e5b9a]. Protolabs earned 46.4% gross and 12.0% operating margin (non-GAAP) in Q2 2026 [src-20260731-4f4aac]. Howmet's capex is about 5% of sales [src-20260630-bd78e7].
- **What drives a qualified shop's cost.** The FlyX CEO: AS9100 costs "hundred thousand, millions of dollars to maintain"; aerospace shops inspect 100% of parts versus sampling (say 5 of 100) at job shops; "the main cost is in the machinery, certification, highly skilled worker" [src-20260806-3a2ec7].
- **Why volume pricing matters.** SendCutSend's own price list: an aluminum part costs $9.41 at quantity 1 and $3.20 at 100 (-65%) [src-20261022-935cf7]. Belosic: "If I was to run one of those customers at a time, we'd be bankrupt", which is why nesting many orders on one sheet matters [src-20260219-15615f].
- **Machine and plant costs.** **Claim (Belosic):** a 12 kW fiber laser costs $1.2-1.3M, "every 3 kW is like 200 grand"; he rejected $4M of conveyors [src-20260626-541ac8]. SendCutSend's Pennsylvania plant: $63.2M, about 170,500 sq ft, 309 jobs, with a $3M state grant [src-20261020-be0cab]. Anduril's rocket-motor plant: $75M for up to 6,000 motors a year with 100 staff [src-20260501-4e5b9a]. **Claim (Machina):** a cell pays back "in less than a year", about 70% of parts are off the shelf, and the DoD estimates one system saves $85M over 25 years by avoiding tooling [src-20250402-161b61]. A stamping die set can cost about $200M but makes thousands of parts a day, so Machina wins only at low volume (LinkedIn commenter) [src-20251009-1f4b2f]. **Claim (Mehr):** a stamping press is used only about 5% of its life [src-20261020-bac9ca].
- **Utilization is the profit lever.** **Claim (Power):** primes' machines run about 10% of the time versus 65-80% at Hadrian, giving "$4 of revenue on $1 of capex" [src-20260610-779f8b]. SendCutSend's CNCs run 90-98%, with 92 standard tools covering 5,000+ unique parts and under 20 programmers handling 100-150 new parts a day (**Claim**) [src-20260525-4a12ab].
- **Robots versus people.** A BMW strategy manager: a humanoid robot's parts could cost $20-30K, a worker about $60,000 a year, yet "the ROI would still be probably negative" today once charging, IT and supervision are counted; one human may supervise 10 robots after validation [src-20261021-25a598]. Foxconn: a robot pick-and-place "may take ... 10 to 15 seconds. But by human, maybe only 2 seconds" [src-20260317-a43440].
- **What this means [inference].** The money is made on machine use and certification, not on robots. A new producer must keep machines busy across many customers to beat 10-15% shop margins.

**Vulcan Elements**

- **Buyers:** 7 federal awards worth $5.7M, including an Army magnet contract (IDIQ: an open-ended order vehicle) [src-20260710-6361ea][src-20250501-1885f8]; magnets for the Army drone program [src-20260923-c53c99]. **Claim (CEO Maslin):** the pilot is sold out 12 months ahead; test data feeds its recipe models [src-20250811-e7cb9a].
- **What this means [inference]:** government-backed, with government as the main buyer.
- **More specifics (from all sources):** Its Benson, NC plant (1.1M sq ft, 10,000 t a year, ~1,000 jobs) is under construction [src-20261020-ca1a28]. Rare-earth oxide feed from Ucore is planned from 2027, so upstream supply is also pre-commercial [src-20260324-61ffc3]. The US set a $110/kg rare-earth price floor for MP and Lynas, a policy demand guarantee [src-20261022-161490].

**SendCutSend**

- **Scale:** 32,000 orders a month, growing about 100% a year [src-20260525-4a12ab]. About $140M a year in revenue (deleted post) [src-20260504-c3ded5] (low). 650 staff [src-20260904-1929b3] versus 169 per Harmonic.
- **Claims (Jim Belosic, CEO):** 48-hour turnaround [src-20260227-e92d45]. Targets 80-90% machine use [src-20260626-541ac8]. A new plant costs about $50M, funded with equipment loans [src-20260519-2d6ceb]. "I love taking VC dollars and putting it directly in the payroll" [src-20261020-487a39].
- **Customer spread (claims):** the largest customer is 0.59% of revenue; he knows a defense firm with 86% from one buyer [src-20260624-3dc6f7]. Only 15-20% of each month's customers are new, so most orders come from returning, mostly small, buyers [src-20260525-4a12ab]. He says there is "enough demand to at least triple our size", but loans cannot fund it [src-20260624-3dc6f7]. Mostly commercial work, including 60% of the Fortune 500 [src-20261020-487a39].
- **Bear:** customers "outgrow us" and buy their own machines [src-20251002-6a5afd]. Belosic calls lasers and metal commodities: "I don't think it's moat-worthy" [src-20260430-9318cd]. It refuses tight-tolerance work [src-20260525-4a12ab].
- **What this means [inference]:** proof that a software-led factory can be profitable without defense money. Now priced beyond SPC.
- **More specifics (from all sources):** More than 300,000 customers and 30M parts shipped, with 1-3 day delivery [src-20261020-9deafa]. Belosic added 450 people in 2026 and is finalizing a first acquisition [src-20261020-1d0bbb]. Named customers include Zipline, Waymo, Anduril, Castelion and Relativity [src-20261020-c541ad]. Ad spend fell from $120-170K a month to about $4K, as word of mouth took over [src-20260525-4a12ab]. Bear: "the software is the easy part ... the hard part is everything outside the software".

**1872**

- **Operations:** 18 staff, about 30,000 sq ft, producing since August 2026 [src-20261016-d61bc1]; welding robots from Path Robotics [src-20260722-3bc2d8].
- **Claims (website, no baseline):** 99% FPY, welding arc on 70% of the time, 85% lower welding cost [src-20261022-fdbf29]. Full autonomy by 2027 [src-20260722-985690].
- **What this means [inference]:** the cheapest way in, but too early to judge.

**Senra Systems**

- **Buyers:** Anduril, L3Harris, Northrop [src-20260128-a16c79]. Growth comes mostly from existing customers and referrals [src-20260701-027c1b].
- **Software:** "Amp", built in-house. It reads parts lists with AI, pulls live supplier prices, estimates labor and writes work instructions [src-20260701-027c1b].
- **Claims (Senra):** 99% FPY [src-20260701-027c1b]. 1,000 harnesses a month, aiming for 10,000 in 2027 [src-20260715-68183e]. Best at runs of 100-1,000 units, quoted in under 2 weeks; about 190 staff heading to 300 by end-2026 [src-20260701-027c1b]. Its CEO says automation is still early [src-20260715-821445]. Harnesses are about 95% outsourced even at SpaceX [src-20260715-821445].
- **Bear:** every number is company-stated. No customer or expert call covers it; only 10 sources mention it. Harness work is manual, so the edge may be paperwork software, not automation [inference].
- **What this means [inference]:** the best-sized owner-operator for SPC, but it needs real diligence.
- **More specifics (from all sources):** **Claims (CEO Jordan Black):** a harness "can be 25% of the cost of your vehicle"; "800 plus mom-and-pop shops" are going away; the only Department of Labor-certified harness training, 4 weeks versus 2 years; technicians average 48-55 years old; the factory is "only 25% built up"; it "didn't have a sales team until 4 months ago" [src-20260715-821445]. He admits "the dexterity and the models might not be at the caliber we need today" [src-20260715-821445]. A BMW expert agrees harness routing is "beyond the edge" for robots today [src-20261014-ce5195]. Lockheed consolidated cable harnesses from five factories to one, a sign of the bottleneck [src-20261014-47f64b].

**Machina Labs**

- **Buyers:** mostly military repair depots that need old panels whose molds no longer exist [src-20261022-ca4c7a]. About 70% defense; a JASSM missile part in qualification; cleared for defense cybersecurity (CMMC Level 2) [src-20260204-ce7053]. Five Air Force awards worth $7.8M, the largest $3.37M (February 2025), plus $507K to maintain a cell at Robins Air Force Base; the Air Force buys again [src-20250416-317e81]. A Rolls-Royce-side expert says it is for prototypes, "not going to involve in our serial production" [src-20250623-5bc67c] (med).
- **Claims (Ed Mehr, CEO):** up to about 50x faster lead times [src-20261022-ca4c7a]; staff grew from 70 to 240 [src-20260320-1361e2]. A new 200,000 sq ft plant with up to 50 cells making "thousands" of assemblies a year [src-20260204-ce7053]. Gross margin "even if I do poorly ... 50%. But more likely close to 70%", because there are no molds [src-20260430-30ea09].
- **Still in qualification.** **Claim (Mehr, April 2026):** "one of our programs we are now in qualification phase ... about to go to production ... couple of years to get to volume" [src-20260430-30ea09]. With Lockheed, "qualifying and going to production for JASSM fuel tanks" [src-20260822-53d33e]. It started with repair parts that took depots "months, sometimes years" [src-20250402-161b61].
- **Bear:** 30 minutes to hours per part versus seconds for stamping [src-20261023-c3b62f]. Mehr himself: in repeat high-volume work "traditional manufacturing is pretty good", and Machina is "not a good fit" for a million identical parts [src-20260821-1c5a08][src-20251230-2c54a2].
- **What this means [inference]:** real defense demand for repair parts; production at rate is not yet proven.
- **More specifics (from all sources):** Its largest client in 2023 was the Air Force; Mehr was "not sure how to compare our pricing" to sheet-metal shops [src-20261023-af2e72]. It won't start a project "unless the customer is actually committed with some dollars" [src-20260622-7846f9]. Its Form D shows $38.94M sold of $52.61M [src-20260225-5e3f18] (a filing, possibly one tranche).

**Hadrian**

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
- **More specifics (from all sources):** Revenue was $3M in 2023 with a $30M+ target for 2024 (Forbes) [src-20240815-500933]. **Claim (Power, 2025):** "basically 10xed revenue in four quarters"; target about $1B by 2027; "manufacturers in the US are horrifically low margin" [src-20250718-ac643a]. **Claim (Power):** close to 100% of workers "never set foot inside a factory", trained in 30 days; "a 25-year-old kid ... running 14 robots" [src-20260610-779f8b]. At Lockheed's plant, "Lockheed Martin employees will operate Hadrian's production cells" (Axios) [src-20261020-09eec1]. The Army's Red River Depot contract runs to March 2027 [src-20260318-472c29]. Hadrian says it does not discuss customers due to "very strict NDAs" [src-20250718-ac643a], which limits checking. All of Hadrian's debt is still corporate; a dedicated plant with a creditworthy buyer would be the first project-finance case [src-20261012-b7af6d].

**Isembard**

- **Claims (Isembard):** 40-60% more output and 30% lower operating cost [src-20250929-857f17]. A franchisee goes live in under 90 days. 14 factories, 4 owned and 10 franchised. Now "locking in these long-term contracts ... one year, two year, three years" so machine purchases match contracts [src-20260909-b547c7]. Turning down orders [src-20260810-f0371c].
- **Buyers:** a humanoid-robot company used it for two urgent $2.3-6K orders, delivered in 2 days [src-20260621-f96bbd]. An Airbus supply-chain head sees such networks as prototype suppliers [src-20251106-dfddcb].
- **Bear:** Thales Alenia Space's procurement chief is "skeptical": he must approve and see each production site, which a franchise hides; not a customer [src-20251110-84b67e]. Output and cost claims are company-only. The CEO spends about half his time recruiting; a quality audit (AS9100D) found many issues needing a follow-up [src-20260909-b547c7]. BBC: about 100 staff at the 160,000 sq ft London site [src-20261019-202dd7].
- **What this means [inference]:** a cheaper, capital-light version of Hadrian, if primes accept franchised sites.
- **More specifics (from all sources):** Isembard hired a commercial chief from McDonald's/KFC to run its "manufacturing franchise network" [src-20261006-5a64c1]; it has more software engineers than machinists and says 95% of CNC machines are owned by small businesses whose owners are retiring [src-20250619-46e43c]. Amca bought Electrocube, a top-20 Boeing supplier [src-20260212-c61f30], and won an Army Materiel Command contract for engineering, qualification and production (**Claim**) [src-20261008-9941fd].

**Freeform**

- **Claim (Freeform):** a new platform, "Skyfall", "scheduled to go live in the first half of 2026", with 25x capacity and thousands of kg of parts a day [src-20260220-348ad9]. No source confirms it went live.
- **How the loop works:** cameras watch the molten metal pool every microsecond; chips process the images; models adjust the printer live [src-20241024-7f1c2e]. It runs GPU clusters on site [src-20260219-2125d7].
- **Buyers:** hundreds of mission-critical parts a week, customers undisclosed [src-20260219-2125d7]; a fast prototype contract (OTA) from DIU, the Pentagon's tech-buying unit [src-20260901-6e197d].
- **Bear:** metal 3D printing has the worst failure record in this theme (Velo3D, Markforged; section 8). Freeform's claims are company-only and Skyfall is unconfirmed.
- **What this means [inference]:** the clearest live feedback loop in precision parts, and small enough for SPC.

**Amca**

- **Buyers:** a first Army fixed-price award, value undisclosed. **Claim:** gets redesigned parts approved in under 90 days [src-20261008-149196].
- **What this means [inference]:** the buy-old-shops path Hadrian rejected [src-20261004-9b47f5]. It buys qualification instead of earning it.

**Atomic Industries**

- **Plants (company site, updated July 18, 2026).** Warren: 50,000 sq ft, mold building, 8 machine systems (machining, EDM spark-erosion, gun drilling, conformal cooling). Shelby: 100,000 sq ft, 16 injection presses from 55 to 2,000 tons. Markets listed: automotive, rail, industrial, consumer, defense; customers are OEMs and their Tier 1 suppliers [src-20261027-b51989]. It also owns a Velo3D metal printer for 3D-printed tool-steel mold inserts with built-in cooling channels (2023) [src-20231128-ff966f]. Macomb County gave a 50% property-tax cut for 10 years; Atomic plans over $10M of equipment and 30-60 jobs at Shelby [src-20260616-57c7d5].
**Business model and where it fits Lilly's two approaches.**
- It is an **owner-operator**, not a software vendor. Young: "Rather than selling software or molds ... vertically integrate that tool building capability into producing parts. Every tool that we can put into production grows our business" [src-20260130-9500f0]. It started as software, then made molds, and now makes parts [src-20250919-2805c7].
- **The pricing idea (company claim):** because its molds are cheap to design and build, it wants to quote a piece price with no separate mold charge. Young's example: "I could quote someone 250 for a piece price, and Company B quotes 250 piece price plus a $300,000 mold" [src-20260130-9500f0]. That turns a one-off tooling sale into multi-year part revenue.
- In the theme's layers it is **fabrication / tooling**: a "new producer" in Approach 1 terms, whose edge is AI in the engineering step (mold design and process setup) rather than robots on the floor.
**Customers and repeat orders.**
- **Claim (Slodov, Sept 2025):** "we picked up like our first couple big ... part production contracts ... it's just like, you know, I need a widget for five years ... we're kind of in the mid eight figure range for that right now"; target "nine figures" next; about 50 staff [src-20250919-2805c7]. Whether "mid eight figures" is annual revenue or total contract value is not clear from the transcript.
- **Named work (company, March 2025):** molds for a drone program and production work for the New York City subway (transit authority) [src-20250327-008034]. Fortune bio: supplies "major OEMs to high growth hardware startups" [src-20260629-d8e640]. No customer is named by a customer.
- **Buyer voice (expert call, med):** a defense-startup chief of staff sourcing drone components: "we use a company called Atomic more than we do Hadrian ... they have the software design integration mastered ... I just cannot believe how fast it moves"; "we can get them designs for a component and they can turn production in eight days" [src-20250729-a0a78c]. This is the only independent buyer on record, and it is about speed, not repeat volume.
- **What this means [inference]:** multi-year part programs are exactly the "repeat production order" signal Lilly is testing for, but today they are company-reported, unnamed and unvalued.
**Right to win against job shops, toolmakers and China.**
- **The market it attacks.** US mold builders are small, aging and squeezed. The trade group says Chinese shops sell molds "up to 40% below" US cost, get 90% of the price paid up front (versus 55% of US builders), and a 2018 tariff on Chinese molds was lifted within six months [src-20250101-110ec0]. US shops call themselves "almost a dying industry" short of trained toolmakers [src-20250701-0ecf2d]. Tariffs since 2025 have helped: 54% of 79 surveyed US shops saw or expect reshoring, and one shop's quote requests rose 25% in a month [src-20250501-39c489].
- **Atomic's angle (company claims):** design speed is where China wins. Young: "Chinese tool shops can deploy 200 designers simultaneously ... the largest tool shop in North America has fewer than 30 mold designers" [src-20260130-9500f0]. Software places cooling lines and ejectors "in seconds instead of days" [src-20260128-2b7e8b]; molds "50% more efficient, built 50% faster and cost 50% less"; cycle times down 20-40% [src-20260130-9500f0]. Slodov: US shops lose bids by slow, margin-gated quoting while China quotes instantly [src-20250327-008034].
- **Against US job shops:** one company owns design, mold build, trials and production, so there is no hand-off between a mold shop and a separate molder [src-20261027-b51989]. Folding the mold into the part price is hard for a capital-thin shop to copy.
**Unit economics (what we know).**
- About $8M spent on the test bed, "more about R&D than direct revenue" [src-20260130-9500f0]; over $10M planned at Shelby [src-20260616-57c7d5]. Roughly 45-50 staff, about 16 of them software engineers [src-20260130-9500f0][src-20250919-2805c7].
- No margin, price or payback data. **[inference]** Bundling the mold into the piece price means Atomic carries the mold cost up front and earns it back only if the program runs its full volume, so its returns depend on long programs and its ability to build molds cheaply.
**Data loop.** Molds in the test bed carry sensors for plastic flow, ejection force and internal temperature, feeding back into design [src-20260130-9500f0]. Models for cooling-line design are trained on physics-solver output, not on past human designs [src-20260130-9500f0]. Slodov: "we're the only ones with a labeled dataset because we're creating it daily in the factory" (claim) [src-20250327-008034]. The site says production results feed back into cycle time and future mold decisions [src-20261027-b51989]. On the scorecard in section each chapter's data-loop section this is a medium-strong loop: owned production data, but limited to its own presses.
**Team and money (brief).** $3.2M pre-seed (2022), $17M seed (Dec 2023, led by Narya with 8090 Industries and Acequia; Toyota, Porsche and Yamaha venture arms), $25M Series A (Sept 2025, led by MaC Venture Capital and DTX Ventures) [src-20220405-b7aac2][src-20231204-652d42][src-20261023-a3bfe7]. Several small SPV filings [src-20250905-f62778]. No SBIR, AFWERX or other government award was found in free sources this run.
**Bear case (equal weight).**
- **Proof is thin.** Every performance number (50/50/50, 20-40% faster cycles, first-shot good parts) is the company's own. The trade editor wrote that success "will be measured not by software capabilities but by results" and listed these as open questions [src-20260130-9500f0].
- **Humans still do the hard part.** Parting lines and die draw (how the mold splits and opens) are not yet automated [src-20260130-9500f0][src-20260128-2b7e8b]. Those are the judgment calls that make complex molds hard.
- **Automotive is a slow, protective buyer.** Young himself: automotive is "deeply protective and resistant to change" [src-20260130-9500f0]. Being both moldmaker and molder means competing with customers' existing Tier 1 molders.
- **Commodity end-market.** Injection-molded parts are a low-margin, price-shopped business, and Chinese mold prices are up to 40% lower [src-20250101-110ec0]. The tariff tailwind can disappear, as it did in 2018. Tariffs also raise steel and imported press costs [src-20250701-0ecf2d].
- **Capital intensity.** Rolling mold cost into part price ties up cash in steel. With a $25M Series A, a mid-eight-figure book (by its own account) and two plants, Atomic will need more capital or debt to scale.
- **Small and early.** About 50 people, one independent buyer quote, no named OEM program. The same speed edge is claimed by Protolabs-style quick-turn molders and by any large molder that buys mold-design software.
- **The edge can leak.** Mold-simulation tools (Moldflow-type software) are sold to every shop; if they add AI, Atomic's design advantage narrows to its own data [inference].
**Open questions / expert-call questions.**
1. To a buyer (Tier 1 or drone OEM): what did you order, how many repeat programs, and did Atomic really skip the separate mold charge? Price versus your normal molder and versus China?
2. To a former Atomic engineer or toolmaker: what share of a mold's design is truly automated today; how many trial loops (T1, T2, T3) does a typical mold still need?
3. Is "mid eight figures" annual revenue or contract value, and how much is parts versus molds?
4. Press utilization at Shelby, and how many molds a month Warren builds.
5. To a US mold-shop owner: does instant AI design change who wins bids, or is price versus China still decisive?
- **What this means [inference]:** the cleanest "AI in the engineering step, owner-operator in production" story in plastics, aimed at a real bottleneck (dying US moldmaker base). Worth a call, but the repeat-order and economics evidence is all company-reported so far.

**Solugen**

- **Money and policy:** a $213.6M DOE loan guarantee for Bioforge Marshall in Minnesota (three modular trains of organic acids, 56 permanent jobs). It is **conditional**: it funds only once legal, technical and financial conditions are met. Production was scheduled for fall 2025 [src-20240613-2df5d6]. A web summary says Solugen broke ground in Marshall in April 2026 and partnered with American Rheinmetall Munitions on energetics inputs (low; not verified in a primary source this run).

**Warp Sciences**

- **Money:** emerged Oct 22, 2026 with a $215M Series A led by Lightspeed, at an $865M valuation according to Weil [src-20261022-40bbe0].
- **First service:** lead-optimization "analog" synthesis, meaning variants of a candidate molecule. Chemists do the work first; robots progressively take repetitive steps such as reaction set-up and purification [src-20261022-b542e2].
- **Claims (Warp):** it aims to "reshore" discovery chemistry that biotechs outsource to Chinese CROs such as WuXi AppTec, and to make discovery "compound" because lab data trains better models [src-20261027-c11426][src-20261022-40bbe0].

**Chemify**

- **Claims (Cronin):** "AWS for chemistry"; makes complex molecules for drug discovery first, then fragrances, paints, catalysts and monomers; plans Chemifarms near customers for supply-chain security [src-20250724-0f42f3].

**Orbital Industries**

- **Commercial status:** a multi-year AWS partnership. The fluid is in qualification with chip makers, a contract manufacturer is lined up, and the target is to ship alongside 2027 GPUs [src-20260528-375aec].
- **Claims:** **Claim (CEO Godwin):** the traditional way would take "10 years and $100M" [src-20260528-375aec]. **Investor view (Plural):** there is "no AlphaFold moment for materials," so value comes from owning the product [src-20260528-2c20ee].
- **Licensing:** it licensed its CurieOS platform to BASF [src-20261022-edad3e].

**Mitra Chem**

- **Earlier reporting:** TechCrunch on generative AI in battery development [src-20231014-d1a13f].

**Radical AI**

- **Lead material, RAI-939:** a high-temperature refractory alloy. A Purdue Applied Research Institute torch test found about 125 times the survivability of C103, the incumbent niobium alloy (company release reporting Purdue's test) [src-20260807-52b690]. **Claim (Radical):** about 300 alloys made in 16 weeks, in a space where only 3,493 alloys had been studied in 20 years. It is now scaling up to bigger test articles and building spec-sheet data [src-20260807-52b690].
- **Partnerships:** Sandia National Laboratories, on alloys for hydrogen purification [src-20260929-dfb65a]. A Makino partnership on machining [src-20261022-e2876c].
- **Throughput:** **Claim (Krause):** 8–20 alloys a day, aiming for 100; $60–300 per experiment; samples from grams to 500 g; no manufacturing yet [src-20260617-f9d293][src-20260710-366df7].

**CuspAI**

- **Kemira PFAS project:** a sorbent to remove "forever chemicals" from drinking water. About 300 trillion structures searched, 5,000+ designs generated, about 20 candidates made and tested, all in 6 months. Kemira calls it an "industry first" commercial partnership and says further projects are being scoped [src-20260521-f4b51b].
- **Singapore:** a five-year, multi-program partnership with A*STAR and a new office there [src-20260723-f1e4f1].
- **Economics (expert call, AlphaSights):** custom projects earn 5–15% gross margin and the platform 85–90%; 40–50% of pilots convert. Royalties are talked about at about 1% (bulk) and 3–5% (specialty), but customers often refuse to give up data rights [src-20261016-29997e] (med).

**Periodic Labs**

- **Critique:** the VC newsletter VCA notes "nothing published yet" and no customers named [src-20261011-bf3574].
- **Speed claim:** 4 months of experiments in under 2 weeks at full speed [src-20260917-1bcb81].

**Lila Sciences**

- **mRNA (company claim):** 950k+ sequences tested, and an in vivo CAR-T program done in 6 months for about a tenth of the usual cost [src-20260828-66bafe].
- **Quote (CTO, Ray Summit):** only about 5% of science is "cheap to verify," which limits how far AI alone can go [src-20260917-29aa29].
**Other names.**
- **Citrine Informatics:** materials-informatics software (model 1). **Claim:** 380 projects, 550 models and 70k experiments a month. Customers include Huntsman and Perstorp, with DARPA INTACT and ARPA-E work [src-20261022-267188][src-20260902-224ead]. Last raise was a $16M Series C in 2023 (search; low).
- **Uncountable:** R&D data platform for formulations (model 1) [src-20260101-850ff7]. $27M Series A in 2025 (search; low).
- **Kebotix:** AI plus robotic chemistry. Johnson Matthey project on catalytic-converter coatings in 2021 [src-20210803-6788dd]. Current status unclear.
- **Aionics:** AI for battery electrolytes. **Claim:** screens about 3,000 formulations a second. Partners include Porsche's Cellforce, earlier with Form, Resonac and Cuberg. It sends samples to the customer and scales through manufacturing partners [src-20231014-d1a13f][src-20261016-29997e].
- **Dunia:** an autonomous electrocatalyst lab (IRIS). **Claim:** "20 years to 2" [src-20261023-b4535c]. Raised €11.5M in 2024 (search; low).
- **Big tech:** Microsoft (MatterGen, Discovery), Google DeepMind (GNoME, plus an automated materials lab in the UK [src-20251211-cb7237]) and Meta (OMat24, OMol25 [src-20250513-fbb4d8]). They give away the model layer.
- **Terrafirma (adjacent, not materials):** $100M Series A, self-driving earthmoving equipment, Austin [src-20260714-976329]; about $500M valuation per Harmonic (low). Adjacent to the theme.

**Arda**

- **Business model:** usage-based software pricing. For customers with ITAR (export-controlled) data, Arda deploys inside the customer's own systems with forward-deployed engineers, the Palantir playbook [src-20261020-a1e174].
- **Plan:** "Act 1" is software for manual assembly lines. "Act 2" is robotic lines that reconfigure as fast as human workers when the design changes [src-20261020-a1e174].
- **Team and money:** founded 2025 by Bob McGrew (Palantir's second engineer, later OpenAI Chief Research Officer). $72M seed (Accel, Founders Fund), then a $160M Series A at $1.5B co-led by Altimeter, Accel and Khosla; $232M total [src-20261020-914a64][src-20261020-9be48d]. Accel says complex engineering workflows run "more than 10x faster" (claim) [src-20261020-8d7abc]. Its investor admits "the price is steep today" [src-20261020-878aa9].
- **Bear case (equal weight):** one customer (Anduril), and every number is from Arda, Anduril or Arda's investors; there is no independent buyer call yet. It sells into the installed base of Siemens, Rockwell and other MES vendors (section 8). As software it does not own production data unless the host lets it, the same weakness as other enablers (section 1). "Act 2" robotic lines are unbuilt.

## Appendix E. Listening list (all links)

*Compiled Oct 27, 2026, to match primer v9.3 (five industries). Every link was opened on Oct 27, 2026, loaded, and is free (YouTube, open podcast pages or free web pages). Lengths come from YouTube or the podcast host; "length not listed" means the page did not give one. ★ = top pick for the section. "Repo" gives the source ID. Company numbers are the companies' own claims unless marked otherwise.*

**Start here, if you only have 3 hours:** a16z *China Has Mass* (macro) → a16z *Critical Minerals* (Raw Materials) → Relentless with Chris Power (Manufacturing) → YC on Solugen (Chemicals) → Latent Space with Radical AI (Advanced Materials).

### E.0 Cross-cutting macro

1. ★ **"China Has Mass. Can America Catch Up?"**, a16z Podcast, Sep 29, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/china-has-mass-can-america-catch-up/) — *Why:* Anduril's and Hadrian's CEOs explain the munitions gap: war games run out in about a week, restocking takes 2–3 years. Repo: src-20250929-452dcb.
2. **"How LA Is Becoming America's New Industrial Tech Hub"**, Bloomberg *Odd Lots*, Sep 21, 2026, 34 min. [▶ Open link](https://www.youtube.com/watch?v=mgCQ0Pl754c) — *Why:* the best mainstream framing; the bottleneck is factory software and feedback, not robots. Repo: src-20260921-a51ab2.
3. **"Can the U.S. Still Build Things?" (#34)**, *The Drone Ultimatum*, with Miles Arnone (Re:Build), about 95 min. [▶ Open link](https://www.thedroneultimatum.com/can-the-us-still-build-things-fixing-the-industrial-base-miles-arnone-podcast-34/) — *Why:* the case for buying and upgrading old shops instead of building megafactories. Repo: src-20261022-f423ef.

### E.1 Raw Materials (Minerals & Metals)

### Stage A — Finding and mining

1. ★ **"Critical Minerals: Mining for the Industrial Future"**, a16z Podcast, Jul 23, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/critical-minerals-mining-for-the-industrial-future/) — *Why:* Mariana's Turner Caldwell on owning mines and refineries and using software to cut build time and cost. Repo: src-20250723-3f3ef8.
2. **"Inside Earth AI: Cutting the Cost of Critical Mineral Discovery" (S2 E57)**, Rare Earth Exchanges, Feb 26, 2026, 33 min. [▶ Open link](https://www.youtube.com/watch?v=-dQONUziAxY) — *Why:* founder Roman Teslyuk on training on 50 years of Australian drilling archives, and why few new deposits are found each year (his figures). Repo: src-20251001-cf441c.
3. **"From Y Combinator to mining, ft Earth AI's Roman Teslyuk"**, YouTube, Apr 28, 2026, 66 min. [▶ Open link](https://www.youtube.com/watch?v=KXbUJ2CjWbI) — *Why:* the longer Earth AI founder story; pair with the primer's bear case (no resource estimate yet). **Not in the repo (new).**
4. **"Critical Minerals: What Makes Mining Tech VC-Backable"**, *Deep Tech Catalyst*, with Jun Ku (Main Sequence), length not listed. [▶ Open link](https://www.thescenarionist.com/p/critical-minerals-at-venture-scale-deeptech) — *Why:* an investor on how non-dilutive government money makes heavy-capex mining fundable. Repo: src-20261022-cd6c5c.

#### Stage B — Refining and making metal

1. ★ **"How The Rarest Company On Earth Raised $75M"**, *Sourcery*, Aug 11, 2025, length not listed. [▶ Open link](https://podcasts.apple.com/us/podcast/how-the-rarest-company-on-earth-raised-%2475m/id1738124704?i=1000721503376) — *Why:* Vulcan's early demand: pilot plant opened Mar 2025 and was qualifying magnets with customers within four months (company claim). Repo: src-20250811-e7cb9a.
2. **"'Supply Chains Win Wars': Rare Earth Magnets with John Maslin"**, *Building the Base*, Apr 29, 2025, length not listed. [▶ Open link](https://buildingthebase.org/episode/supply-chains-win-wars-rare-earth-magnets-with-john-maslin-ceo-vulcan-elements) — *Why:* the magnet macro in one sitting; the gap is processing and metal-making, not ore. Repo: src-20250429-6f9155.
3. **"Energy, Minerals, and the Physical Stack Behind AI"**, a16z Podcast, May 13, 2026, length not listed. [▶ Open link](https://a16z.com/podcast/energy-minerals-and-the-physical-stack-behind-ai/) — *Why:* Mariana's refinery and plant software (the data loop inside owned assets). Repo: src-20260513-bdc044.
4. **"Advancing US critical minerals with software and autonomy"**, Benchmark Mineral Intelligence, Jun 23, 2026, 23 min. [▶ Open link](https://www.youtube.com/watch?v=OvJX0j5OPXs) — *Why:* how industry analysts see AI-run refineries. Repo: src-20260623-6dc76b.
5. *(Quick watch)* **"The Future is Metal – Mariana Minerals"**, a16z, Aug 5, 2026, 9 min. [▶ Open link](https://www.youtube.com/watch?v=uFt-tkagUUI) — *Why:* nine minutes on China's 90%+ share of refining. Repo: src-20260805-b7e3c7.

### E.2 Manufacturing

### Metal Supply

1. ★ **"Just Gonna Send It Podcast: Zane Hengsperger (Nox Metals) – Ep. 13"**, SendCutSend, Mar 25, 2026, 54 min. [▶ Open link](https://www.youtube.com/watch?v=qhRV1cBG2lw) — *Why:* Nox's founder in conversation with a big customer type; why software beats old-line distributors on quoting and cutting. Repo: src-20260325-5b68db.
2. **"Reindustrializing America: Zane Hengsperger on building Nox"**, *First Builders*, Apr 27, 2026, length not listed. [▶ Open link](https://podcasts.apple.com/us/podcast/reindustrializing-america-zane-hengsperger-on-building/id1818466924?i=1000763907900) — *Why:* the detailed founder story and lean-capital bet. Repo: src-20260427-83b102.
3. **"Building NOX Metals & The Future of Manufacturing" (#430)**, *Powers Pod*, length not listed. [▶ Open link](https://www.powerspod.com/reindustrializing-america-building-nox-metals-the-future-of-manufacturing-with-zane-hengsperger/) — *Why:* Nox as the AI-run metal service center. Repo: src-20261022-3135b5.

#### Fabrication

1. ★ **"How to Build a Manufacturing Company in America | Jim Belosic, SendCutSend"**, *The Peel*, Apr 30, 2026, 1 h 32 min. [▶ Open link](https://www.youtube.com/watch?v=Zajo84R1ckI) — *Why:* a bootstrapped fabricator at about $140M run rate in eight years (company figure); the best repeat-order case study. Repo: src-20260430-9318cd.
2. **"What Everyone is Missing About Reindustrialization"**, Machina Labs, Oct 20, 2026, 55 min. [▶ Open link](https://www.youtube.com/watch?v=EiMhaHThSXk) — *Why:* Machina's and Freeform's founders on why the money is in the finished part ($57 of steel becomes a $2,000 part). Repo: src-20261020-bac9ca.
3. **"The Crisis Facing American Manufacturing"**, *Core Memory* (Ashlee Vance), Sep 26, 2026, 25 min. [▶ Open link](https://www.youtube.com/watch?v=NpvYyx2OUTc) — *Why:* a short documentary inside Hadrian and Machina Labs. Repo: src-20260926-70087f.

#### Precision & Defense Hardware

1. ★ **"How to Dominate Manufacturing in the US | Chris Power, Hadrian"**, *Relentless*, Sep 21, 2026, 1 h 19 min. [▶ Open link](https://www.youtube.com/watch?v=hmOLr_h7zTk) — *Why:* the clearest unit-economics case for owning factories; about 80% of capex is shared across programs. Repo: src-20260921-876080.
2. **"From hypercars to cruise missiles: Lukas Czinger on the future of US defense" (E2292)**, *This Week in Startups*, May 23, 2026, 1 h 46 min. [▶ Open link](https://www.youtube.com/watch?v=U5kZI86lIjk) — *Why:* Divergent's CEO on moving from cars to missile airframes and why it builds its own printers. Repo: src-20260523-b05ded.
3. **"Building the Arsenal: Speed, Scale, and Affordability"**, Air & Space Forces Association, Oct 14, 2026, 40 min. [▶ Open link](https://www.youtube.com/watch?v=r7BNP3R_TWk) — *Why:* the buyer side; Divergent's CEO on a panel about producing munitions at scale. Repo: src-20261014-47f64b.
4. *(Read or listen)* **TBPN transcript: Atomic Industries raises $25M Series A**, Sep 19, 2025. [▶ Open link](https://www.tbpndigest.com/story/2025-09-19/aaron-slodovs-atomic-industries-raises-25m-series-a-to-automate-injection-mold-manufacturing-in-detroit/transcript) — *Why:* Atomic's move from software to molds to parts; "mid eight figure" contracts (company claim). Repo: src-20250919-2805c7.

### E.3 Chemicals

1. ★ **"Inside The Startup Reinventing The $6 Trillion Chemical Manufacturing Industry"**, YC, Mar 2026, about 13 min. [▶ Open link](https://www.ycombinator.com/library/NO-inside-the-startup-reinventing-america-s-trillion-dollar-chemical-industry) — *Why:* the best short intro to a fully integrated chemical maker (Solugen; ~96% yield claim). Repo: src-20260320-f90e80.
2. **"EP 312 Lee Cronin on Automating Chemistry"**, *The Jim Rutt Show*, Jul 2025, length not listed. [▶ Open link](https://jimrutt.substack.com/p/ep-312-lee-cronin-on-automating-chemistry-f9f) — *Why:* Chemify's "code to molecule" and how it charges (company claims). Repo: src-20250724-0f42f3.
3. **"Why Twelve believes power-to-liquids will revolutionise SAF"**, *Sustainability in the Air*, Jul 24, 2025, 34 min. [▶ Open link](https://podcasts.apple.com/bm/podcast/why-twelve-believes-power-to-liquids-will-revolutionise/id1620281360?i=1000718768981) — *Why:* an owned e-fuels plant and its long-term buyers; policy is the swing factor. Not in the repo.
4. **"Mission-driven doctor, inventor & entrepreneur" (Ep. 175)**, *Molecule to Market*, Phlow CEO Eric Edwards, 55 min. [▶ Open link](https://moleculetomarketpod.com/episodes/mission-driven-doctor-inventor-entrepreneur/) — *Why:* drug-ingredient onshoring with the government as anchor buyer. Not in the repo.

### E.4 Advanced Materials

### Producers

1. ★ **"Jonathan Godwin, CEO at Orbital: Orbital raised $50m Series B"**, *Scaling Europe*, Jun 29, 2026, 21 min. [▶ Open link](https://open.spotify.com/episode/2iSBDNWM2Sc5czUAIW0ugX) — *Why:* Orbital's founder on why it builds and sells hardware (a GPU-cooling material) instead of only models (company claims). Not in the repo (new).
2. **"Developing a supply chain for American-made batteries"**, *Volts*, Sep 6, 2024, length not listed (free transcript on page). [▶ Open link](https://www.volts.wtf/p/developing-a-supply-chain-for-american) — *Why:* Mitra Chem's CEO on China's grip on LFP cathodes and its iron-rich roadmap. Not in the repo (new).

#### Materials Discovery Labs

1. ★ **"The Self-Driving Lab — Joseph Krause, Radical AI"**, *Latent Space*, Jun 17, 2026, length not listed. [▶ Open link](https://www.latent.space/p/radical-ai) — *Why:* the moat is experiments, not models; customers asking for 300 lb pushed Radical toward making alloys. Repo: src-20260617-f9d293.
2. **"AI for Atoms: Periodic Labs with Liam Fedus"**, *No Priors*, Apr 3, 2026, 29 min. [▶ Open link](https://www.youtube.com/watch?v=Oru2Jxr1xHU) — *Why:* economics of an AI lab running its own experiments. Repo: src-20260403-40fa0e.
3. **"Meet the Ex-OpenAI & DeepMind Leads Creating an AI Scientist"**, *The Generalist*, Sep 29, 2026, 60 min. [▶ Open link](https://www.youtube.com/watch?v=vJVZgeXKlVo) — *Why:* Periodic's superconductor focus and the impurity problem. Repo: src-20260929-ca6d19.
4. **"Max Welling, CuspAI — Nebius Conversations"**, May 4, 2026, 19 min. [▶ Open link](https://www.youtube.com/watch?v=40CU4rbO7E4) — *Why:* the software-only model for contrast; it designs but does not make. Repo: src-20260504-36655f.

### E.5 Enabling Software & Robotics (tracked, outside the core)

1. ★ **"Building Factory SuperIntelligence with Ariyan Kabir"**, *Machine Minds*, length not listed. [▶ Open link](https://machineminds.buzzsprout.com/2212148/episodes/19077384-building-factory-superintelligence-with-ariyan-kabir) — *Why:* GrayMatter moved from licensing software to selling robot cells as a service, which tests the thesis. Repo: src-20261022-3335bd.
2. **"Former top OpenAI employees raise capital for defense startup valued at $1.5B"**, CNBC, Oct 16, 2026, short clip. [▶ Open link](https://www.cnbc.com/video/2026/10/16/former-top-openai-employees-raises-capital-for-defense-startup-valued-at-1point5b.html) — *Why:* Arda on the 3–6 months it takes to retool factory automation. Repo: src-20261020-878aa9.
3. **"Mind Robotics: Building the AI-Native Robotics Platform"**, Kleiner Perkins, May 13, 2026, 4 min. [▶ Open link](https://www.youtube.com/watch?v=fc9GB9Yz75Y) — *Why:* Rivian's line as Mind's live data loop. Repo: src-20260513-abe9cf.
4. **"Big Ideas 2026: Physical AI and the Industrial Stack"**, a16z Podcast, Dec 25, 2025, length not listed. [▶ Open link](https://a16z.com/podcast/big-ideas-2026-physical-ai-and-the-industrial-stack/) — *Why:* how investors frame the software layer going into 2026. Repo: src-20251225-725014.
- *Gap:* no free Lumaril podcast or founder interview found (searched Oct 27, 2026). Use the primer profile (section 7.10).
