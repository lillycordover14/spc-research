# Rebuilding America’s Industrial Middle

_Initial takeaways on AI-native, vertically integrated industries. Draft v1, 2026-10-28. Mirrors the structure of "Bottlenecks to Enterprise AI at Scale" (APC takeaways v5.1). Built from the VII primer v10.1 and the sources it cites; every claim carries a source id. Valuations marked Harmonic or PitchBook come from those tools, not press._

## 1. Key takeaways

1. **Some of the forces behind domestic production are temporary and others are lasting. The most durable opportunities for us are producers that win on the lasting constraints: skilled labor and supplier qualification.**
    - **Temporary forces:** the buildout has leaned on one policy push after another: Section 232 metals tariffs (50/25/10% since April 2026), pauses in China’s export controls (deadlines November 10 and 27, 2026), CHIPS money (FY2026 was the last appropriated year), and a FY27 munitions request of which about 82% depends on reconciliation (CNAS). Each can move with a proclamation, a deal or a budget. Producers whose economics only work behind one of these are priced at a premium while it lasts and may lose their edge when it eases. [src-20260402-1b5d6c][src-20261019-854e22][src-20261027-f82d55][src-20260701-78183b][src-20261007-c6f64e]
    - **Lasting limits:** labor and qualification are different. The US needs 3.8M more manufacturing workers by 2033 and 1.9M may go unfilled (Deloitte / Manufacturing Institute). 83% of the 17,156 US machine shops have fewer than 20 employees, and the average owner is over 65. Buyers take from nine months to several years to qualify a new supplier, and repeat first-article inspection whenever the process or site changes. China’s grip on refining (it leads 19 of 20 strategic minerals at about 70% share, IEA) is structural in direction even if the timing swings. [src-20240416-b69154][src-20250626-23f6d9][src-20260310-45bab3][src-20190801-e81d7b][src-20250521-c62d29]
    - **Implications:** we should favor producers that make more output per skilled worker and get qualified faster, and that would still win if tariffs came off. They benefit as the labor gap widens, without needing policy to stay where it is.

2. **Buyers do not pay a new producer for lower prices. They pay for speed and capacity, and only some buyers do. Cheap labor is not the edge, so the pitch is “we deliver when your shop cannot hire”, not “we are cheaper”.**
    - Hadrian’s CEO says “most of the market just doesn’t value speed”; it values flexibility, scale and total program cost. In our expert calls, three Boeing voices said they pay new suppliers parity or more, and a Northrop GM said cost is secondary to schedule. [src-20260921-876080][src-20260818-9b2d5c][src-20250712-e5e110][src-20250707-3b7a46]
    - Where speed matters it is worth real money: a Northrop engineer would pay 20–40% more to avoid a delay, though a former Hadrian customer puts the ceiling at 10–15%. SendCutSend delivers in 48 hours and Senra cut harness lead times from six months to two weeks (company claims). [src-20260802-36d46c][src-20260806-3a2ec7][src-20260227-e92d45][src-20260128-a16c79]
    - In a new automated plant, labor is less than 10% of cost of goods (Drew Baglino); China wins on a supply chain within a three-hour drive, not on wages. SendCutSend can beat China on only about 20–25% of its work, and its high machine use (lasers at 86%) comes from scheduling software, not robots. [src-20260513-bdc044][src-20260519-2d6ceb][src-20260626-541ac8]
    - The underwriting question is therefore how much revenue comes from buyers already paying for speed, not whether the company can match a job shop on price.

3. **Owning the plant is where the margin and the data sit. Software sold into other people’s plants rarely sticks, but the “data loop” that owner-operators pitch is still mostly unproven.**
    - Proto Labs earns 49% gross margin in its own factories versus 31% in its partner network. Earth AI integrated after 80 software pilots with miners did not recur, Mariana’s CEO calls selling software to miners a “death spiral”, and GrayMatter found selling autonomy software “doesn’t really work” and now rents robot cells as a service. [src-20260206-8bb619][src-20260206-2b13c7][src-20251001-cf441c][src-20250723-3f3ef8][src-20261022-3335bd]
    - The loop is evidenced only where the process runs continuously: Freeform’s cameras adjust each printed layer live, Mariana’s agents retune its refinery every 15 minutes, and Hadrian cut order-to-first-article time by 50% in about two years. Elsewhere, toolpaths come from third-party CAM software, inspection is manual, and one buyer asks whether a supplier “is actually” software-enabled. [src-20241024-7f1c2e][src-20260623-d1790b][src-20261004-9b47f5][src-20260611-7b80f0][src-20260817-8867f2][src-20250729-a0a78c]
    - No company in our research shows unit cost or quality improving with volume. That one number would separate a software-run producer from a well-run job shop.

4. **Capital needs split producers into three tiers. Equity should pay for software and the first plant; debt and government money should pay for the rest. Our check size fits the capital-light tier.**
    - Capital-light owner-operators win on software and speed (SendCutSend, profitable for eight years; Senra). Capital-heavy builders finance plants outside the equity stack (Hadrian’s $360M credit line and $900M of Navy money; Vulcan’s $620M OSC loan; Phoenix Tailings’ $500M conditional OSC loan). Software-first vendors need a host plant for their data (Arda inside Anduril; Mind Robotics inside Rivian). [src-20260519-38c7ed][src-20260817-c48f28][src-20260320-67ba4c][src-20251103-ee9b27][src-20260616-3580b9][src-20261020-914a64][src-20261013-cc78c0]
    - Founders say the same: “equity never funds factory construction” (Chris Power, Hadrian); “don’t fund physical hardware with equity” (Ed Mehr, Machina). Machine loans run about 8–14%, but lenders fund machines, not software teams, and custom lines are “unfinanceable” (Jim Belosic, SendCutSend). [src-20260921-876080][src-20260430-30ea09][src-20260220-0d5345][src-20260519-2d6ceb][src-20260624-3dc6f7]
    - Plants come before contracts: the Pentagon “cannot actually sign a contract until they have that physical facility built”, and capex runs about two years ahead of revenue. [src-20260325-7ba845][src-20260921-876080]

5. **Qualification is both the entry tax and the moat. Buyers cap any one supplier’s share, so the prize is turning prototype wins into multi-year repeat orders.**
    - Qualifying a new supplier takes 9–12 months at Raytheon and 1–2 years at Northrop; full aerospace trust takes 7–8 years (Power). Once paid, it locks a supplier into programs that last about 50 years. [src-20250708-2aa3ad][src-20260802-36d46c][src-20260908-65fab6][src-20260818-9b2d5c]
    - Buyers cap share: SpaceX at about a third of a shop’s revenue, others at 25–30%, and Boeing “will never” put one part family on one supplier. Probation is deliberately small: Raytheon’s spend with Hadrian is “in the tens of thousands ... on purpose”. [src-20250708-342eaf][src-20250623-5bc67c][src-20260818-9b2d5c][src-20260823-b3713f]
    - Entry is through repair, replacement and second-source parts. The FY26 NDAA adds multiyear munitions buys and purchase commitments of up to 10 years with advance payments (Secs. 804(b) and 867), the first channels that could turn prototype wins into multi-year orders. [src-20251015-e9edbf][src-20260821-1c5a08][src-20251218-f0d6ef]

6. **The key risk for any new producer is that incumbents automate with the same tools while keeping their approvals. The most defensible companies own the plant, the software and the qualification together.**
    - Incumbents are doing well and automating: Northrop claims about 20% lower recurring cost at a new plant, L3Harris credits AI for higher yields, Carpenter’s specialty-alloy margin reached 37.7%, and Reliance is taking share in metal distribution without AI. [src-20261022-1389b7][src-20261022-869770][src-20261022-679fcc][src-20261022-1e6872]
    - Enablers arm them: CloudNC sells AI machining software to 1,000+ shops, including Lockheed’s, and GrayMatter took one helmet maker from about 300 to 1,700 helmets a day on the same robots. Permanent 100% bonus depreciation makes those robots cheaper for profitable incumbents. [src-20260908-f98d21][src-20261022-3335bd][src-20260114-2075f7]
    - The top of the category is priced like AI: Hadrian at $7.87B, Divergent at $2.3B, SendCutSend at $2.1B five months after $1.01B. A company that automates one step can be copied; one that holds the qualification, the software and the plant together is harder to replace. [src-20260807-b0dc5b][src-20260222-9c80a9][src-20261020-487a39][src-20260519-38c7ed]

## 2. Where we would invest

The areas below follow the chain from the factory floor back to raw materials, then chemicals and materials, and end with the one software exception. Each one opens by explaining which takeaway it acts on.

### A. Fabrication and assembly

**How it ties to takeaways 2 and 4:** takeaway 2 says buyers pay for speed, not price, and takeaway 4 says capital-light producers fit our check. The companies here take many small, high-mix orders, run them on in-house software, and finance machines with debt.

Job shops lack capital, software and successors, and online marketplaces never own the margin. SendCutSend (Series B at $2.1B, profitable for eight years) shows the model works; it is our benchmark rather than a target. [src-20261020-487a39][src-20260519-38c7ed]

#### Senra Systems _($65M Series B, July 2026, co-led by Lowercarbon and Interlagos; ~$493M post per Harmonic; ~190 employees)_

- **Overview and use cases:** Senra builds wire harnesses and cable assemblies for aerospace, defense and space in two of its own California plants (about 95,000 sq ft). Harnesses can be about 25% of a vehicle’s cost and are still built almost entirely by hand. Its in-house platform, Amp, runs quoting, engineering, work instructions, supply chain, machine programming and quality in one system. The CEO ran SpaceX’s harness organization. [src-20260715-fb79c2][src-20260701-027c1b][src-20260715-821445][src-20260715-68183e]
- **Thesis:** Senra acts on takeaway 2: it sells speed (lead times from six months to two weeks, a company claim) on a part that gates vehicle production. Growth comes from existing customers, and every part it quotes or builds feeds Amp’s library, the start of a data loop (takeaway 3). The Series B funds a third factory, and the stage fits us. [src-20260128-a16c79][src-20260701-027c1b]
- **Areas to diligence:** The physical build is still manual on standard equipment, so today’s edge is software plus trained labor, not robots; we would test whether the new AI and robotics push lowers cost per harness. 2026 sources do not confirm AS9100 or ITAR status. We would ask for first-pass yield (99% claimed), repeat-order data, gross margin and customer concentration. [src-20260715-68183e][src-20260701-027c1b]

#### 1872 _($15M seed via Ohio’s O.H.I.O. Fund; ~18 employees)_

- **Overview and use cases:** 1872 makes welded steel skids, frames and enclosures for energy and utility customers in one 30,000 sq ft plant in Cincinnati, using robots and its own software. [src-20260722-985690][src-20261022-fdbf29][src-20261016-d61bc1]
- **Thesis:** Data-center and grid buildout is pulling on fabricated enclosures (one legacy fabricator has backlogs into 2027), and 1872 is a “factory as the product” bet at a seed price. At this stage it is a relationship to build ahead of a second plant. [src-20261022-4234b3]
- **Areas to diligence:** Its welding AI belongs to Path Robotics, not 1872, so the software edge is unproven, and we found no customer evidence yet. We would wait for plant-one utilization, gross margin and a first repeat order. [src-20260722-3bc2d8]

### B. Precision and defense hardware

**How it ties to takeaways 5 and 6:** takeaway 5 says qualification is a moat once paid, and takeaway 6 says the safest producers own the plant, software and approvals together. The companies here make tight-tolerance parts for long defense and aerospace programs.

The top of this layer is priced out (Hadrian $7.87B, Divergent $2.3B, Amca over $1B), so we use those as benchmarks. Our entry is Series B, or a capital-light structure such as a franchise. [src-20260807-b0dc5b][src-20260222-9c80a9][src-20260520-af3e6c]

#### Freeform _($67M Series B, February 2026; ~$179M post per PitchBook; Founders Fund, NVIDIA, Boeing)_

- **Overview and use cases:** Freeform 3D-prints metal parts (heat exchangers, manifolds, rocket-engine injectors and nozzles) on its own multi-laser printers and sells parts, not printers. Cameras watch the molten metal at microsecond scale and machine-learning models adjust each layer live on an on-site GPU cluster. The founder ran SpaceX’s Merlin and Raptor engine programs, and it won a DIU contract in July 2026. [src-20260219-2125d7][src-20241029-1d136e][src-20241024-7f1c2e][src-20260901-6e197d]
- **Thesis:** Freeform has the clearest data loop in the category (takeaway 3): its process runs continuously and produces print data no vendor sees, which is why NVIDIA and Boeing invested. Selling parts rather than machines keeps the margin, and a valuation under $200M leaves an entry point. [src-20241024-7f1c2e][src-20260219-2125d7]
- **Areas to diligence:** Customers are undisclosed, so we would ask for named references and whether any parts fly on a production program. We would ask for yield and cost-per-part trends over time, the evidence no one in the category has shown. We would also check capital needs for its larger printer and the co-founder’s departure; its Form D shows about $8M of the round unsold. [src-20260107-a36a83]

#### Isembard _($50M Series A, March 2026, led by USV; ~$250M per Harmonic estimate; 14 factories)_

- **Overview and use cases:** Isembard runs a network of precision machining factories (CNC milling and turning in aluminium, steel, titanium and Inconel) for customers such as Anduril, Babcock and Tekever. Every site runs its MasonOS software; franchisees bring the machines and building, and Isembard brings the software and the demand. [src-20260310-45bab3][src-20261027-ee8c62][src-20250929-857f17]
- **Thesis:** Isembard is a capital-light owner-operator in a qualification-gated market (takeaways 4 and 5). It reached 14 factories (4 owned, 10 franchised) in about 18 months, says revenue grew 10x year on year, and cut one customer’s lead time from about 10 weeks to under 14 days at a matched price. [src-20260909-b547c7][src-20260914-37bb6a][src-20260310-cdfd82]
- **Areas to diligence:** We would test economics per franchise and how primes audit franchised sites, since a Thales buyer is skeptical. We would confirm AS9100 and ITAR coverage across the network and the plan and structure for US expansion from a UK base. [src-20251110-84b67e]

### C. Refining and magnets

**How it ties to takeaways 1 and 4:** takeaway 1 says China’s refining grip is a lasting constraint, and takeaway 4 says government debt can replace most of the equity in a plant. The companies here own a permitted, working plant outside China, which is the scarce asset and the only thing OSC and DOE lenders will finance.

Policy money lands here first: $65B of public money was committed to minerals in 2025, and DoD set a price floor with MP Materials. Mariana Minerals is the benchmark, with one of the two credible data loops, but its check size is above ours. [src-20260716-6a06e4][src-20250710-e21373][src-20260803-30e6d5]

#### Vulcan Elements _($65M Series A, Altimeter; $620M OSC loan and $50M Commerce equity in a $1.4B package)_

- **Overview and use cases:** Vulcan makes sintered rare-earth magnets for drone and robot motors, chip-fab tools and cars from non-Chinese material in North Carolina. A 10-ton pilot runs in Durham, and a 10,000-ton plant is being built in Benson. [src-20261010-8e6ec0][src-20251103-ee9b27]
- **Thesis:** China makes over 90% of rare-earth magnets and the US under 1%, so a domestic producer has the government as buyer of last resort (takeaway 1). The Army chose Vulcan for its million-drones-a-year program, and the company says pilot output is sold out 12 months ahead. Government debt funds the plant (takeaway 4). [src-20250429-6f9155][src-20260923-c53c99][src-20250811-e7cb9a]
- **Areas to diligence:** The key question is whether unit cost gets close enough to China that commercial buyers sign without subsidy; no commercial buyer is named. Oxide supply from ReElement and Ucore arrives in 2027, and the CEO says the equipment is Chinese too. Its Form D shows about $114M of a $545M offering unsold, so we would check round timing and allocation. [src-20260324-61ffc3][src-20250429-6f9155][src-20260402-c8e4dc]

#### Phoenix Tailings _($116.6M Series B; $500M conditional OSC loan; selected for a $66M DOE grant)_

- **Overview and use cases:** Phoenix turns rare-earth concentrate and recycled magnet scrap into the metals and alloys that magnet makers melt (NdPr, dysprosium, terbium), using a lower-energy route first funded by ARPA-E. It runs a 200 t/yr metal plant in New Hampshire, is building a $375M separation plant in Rochester, NY to ramp from 2027, and bought an AI and automation team in April 2026. [src-20260219-bd22b6][src-20210621-c887f1][src-20251023-4f8da0][src-20261020-f2cfc3][src-20260508-cf2550]
- **Thesis:** Phoenix is the most advanced US rare-earth metal maker, with a $100M contract from an undisclosed automaker and backing from BMW i Ventures, Yamaha and Sumitomo. It sits between oxide and magnet, the step where China’s lead is greatest (takeaway 1). [src-20250130-1a7b77][src-20241230-a7f987][src-20260219-bd22b6]
- **Areas to diligence:** We would test a roughly 15x ramp, from 200 t to about 3,000 t of metal by 2028; the OSC loan and the DOE grant are both still conditional. Long-term feedstock is not locked in, customers are unnamed, and China sets NdPr prices with no public price floor like MP’s. The check size is large. [src-20260616-3580b9][src-20260602-0b0139]

### D. Specialty chemicals and advanced materials

**How it ties to takeaways 1 and 3:** takeaway 1 says China dependence is lasting, which gives US makers a policy-backed buyer, and takeaway 3 says owning the product keeps the margin. The companies here make and sell the product rather than license a discovery.

Specialty players earn far more than commodity ones (Lonza 31.6% EBITDA margin versus a $2.4B net loss at Dow), and about 46% of US generic doses depend on Chinese source materials (USCC). Discovery labs (Periodic, CuspAI, Lila) invent materials but do not sell them, so we track them separately. [src-20260128-af3b8f][src-20260129-338338][src-20250605-bde73f]

#### Phlow _(BARDA-funded since 2020; $15.9M 2026 award for a Virginia API alliance)_

- **Overview and use cases:** Phlow makes active ingredients for essential generic medicines in its own Virginia plants, using batch and continuous-flow chemistry at up to 50–100 t a year. It makes epinephrine API for Fresenius; validation is done and the Drug Master File is filed. [src-20260209-16223c][src-20260721-fa5081]
- **Thesis:** Phlow is the most direct answer to China dependence and the BIOSECURE Act (takeaway 1). Government buyers plus a generic maker are the kind of offtake that can repeat. [src-20260721-fa5081][src-20250605-bde73f]
- **Areas to diligence:** Commercial supply waits on FDA approval in 2027, generics are excluded from the Section 232 tariff, and margins are thin. Revenue grew from a COVID-era contract, and the CEO calls US support so far “a drop in the bucket”. The edge is automation, not AI, and we would clarify stage and round timing. [src-20260209-16223c][src-20260402-ecae19][src-20240613-4b9301]

#### Orbital Industries _($50M Series B, May 2026, led by Plural; ~50 employees)_

- **Overview and use cases:** Orbital sells an AI-designed, PFAS-free fluid for cooling data-center servers, made by a contract manufacturer, plus modular data centers. AWS is a strategic partner, and BASF licenses its design software. [src-20260528-93befb][src-20260528-375aec][src-20261022-edad3e]
- **Thesis:** Orbital owns the product margin and has an urgent buyer. Liquid cooling is expected to reach 53% of AI chips in 2026, and the EU’s PFAS restriction pushes demand for replacements. If the fluid ships in 2027, it could be among the first AI-designed materials sold at scale. [src-20260817-13658d][src-20260326-379e42]
- **Areas to diligence:** The fluid is in qualification for 2027 GPUs and none has been sold. We would ask who the contract maker is, gross margin per liter, and how much revenue today is software licensing rather than fluid. [src-20260528-375aec]

#### Osmo _($70M Series B, February 2026, led by Two Sigma Ventures; $130M raised)_

- **Overview and use cases:** Osmo designs its own fragrance molecules with AI and sells formulas and ingredients to nearly 100 brands. A 60,000 sq ft plant with robotics opened in Elizabeth, NJ in May 2026. [src-20260204-1ec8c6][src-20260512-3ad5dc]
- **Thesis:** Osmo is the clearest case of AI-designed molecules sold as product by the company that designed them, made in its own US plant (takeaway 3). [src-20260204-1ec8c6]
- **Areas to diligence:** Customers so far are small brands, while the large fragrance houses own the big accounts. Revenue is not disclosed, and a molecule’s value depends on perfumers adopting it.

### E. Selective software: closed-loop plant control paid on output

**How it ties to takeaway 3:** takeaway 3 says we should mostly avoid software sold into other companies’ plants. This is the one exception we would consider, because it is paid like a producer and runs the plant itself rather than advising an operator.

This is our lowest-priority area and would be at most one investment.

#### Lumaril _($12M seed led by Lux; WSJ Pro reports $66M at a $400M valuation)_

- **Overview and use cases:** Lumaril connects to a plant’s existing controls, adds cheap audio and video sensors, builds a real-time model and changes setpoints itself through a safety layer to raise throughput and yield in chemicals, biologics and polymers. Its founders created Palantir Foundry, and it says “we’re paid on the production we add.” [src-20261027-d5ba3f][src-20261003-496a99][src-20261027-79ddd6]
- **Thesis:** Lumaril earns a producer’s margin and data loop without owning the plant, which lets us back the thesis in process industries where a new plant costs hundreds of millions. Chemical plants need 80–85% utilization to earn their cost of capital and Europe averages about 74%, so each extra point of yield in a sold-out plant is close to pure margin. [src-20261027-d5ba3f][src-20260401-e2adb0]
- **Areas to diligence:** No customers or results are public, so we would ask for one plant’s before-and-after yield, how the pricing baseline is set, and how the plant’s safety team approved closed-loop control. We would also assess competition from Honeywell, AspenTech and Emerson, and the owner’s ability to end the contract.

## 3. Where we would not invest

**We would avoid layers where returns depend on commodity prices, government programs or being priced as an AI company, rather than on the go-to-market and customer support we provide.**

- **Precision parts at the top (Hadrian, Divergent, Amca):** $1B–$7.9B valuations ahead of audited revenue; useful as benchmarks. [src-20260807-b0dc5b][src-20260222-9c80a9][src-20260520-af3e6c]
- **Equity-funded mines and greenfield megaplants (Mariana-scale):** one large bet better suited to debt, with commodity prices that swing (lithium fell 24% in 2025; Ganfeng lost over 75% of its value). [src-20260130-ebdd5a][src-20250529-3a588b]
- **AI mineral exploration (Earth AI, KoBold):** a discovery earns nothing until a mine is built, and mines average 15.7 years from discovery to production (19.1 in the US). [src-20240101-a81fa2][src-20250101-3e6713]
- **Materials discovery labs (Periodic, Lila, CuspAI):** priced on talent and none sells material yet; faster discovery does not shorten customer qualification. [src-20261010-7b9ecf][src-20260528-2c20ee]
- **Factory software and robots sold to others (Arda, Mind Robotics):** first-customer stage, Siemens and Rockwell own the installed base, and Mind has raised over $1B with no public product. [src-20261020-a1e174][src-20260515-176e26][src-20260804-0e8130]
- **Agrochemical actives (Enko):** new actives take 10–15 years and about $300M to register. [src-20250601-f7467b]

## 4. What we would underwrite

**We would look for companies that own the plant and its software, are already paid for speed or qualification, finance machines with debt, and can show each unit getting better or cheaper over time.**

- **Owns production and the software that runs it,** so the margin and the data stay in-house.
- **Already paid for speed or qualification:** a named buyer, a repeat purchase order or a qualified part.
- **Debt or government money funds the machines;** equity pays for software and the first plant.
- **Improves with use:** scrap, cycle time, yield or quote accuracy improving with volume, or a plan to measure it.
- **Wins without policy:** would still sell if tariffs came off or a US–China deal lowered prices.
- **Better than job-shop margins,** above the roughly 30% gross margin of incumbent roll-ups and toward Proto Labs’ 44.5%. [src-20241001-28c2aa][src-20260206-8bb619]
