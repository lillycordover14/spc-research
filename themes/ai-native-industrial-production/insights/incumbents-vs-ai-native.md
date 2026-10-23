# Incumbents vs AI-native: hyperscalers, conglomerates and primes facing AI-native production

Prepared by grokbot 2026-10-22 (America/Chicago). Free public sources only; every claim carries a repo source id `[src-…]` or an inline URL. AlphaSense not used. Where a fact is only in a search-result snippet and not filed as a source, it is linked inline and should be treated as med confidence. "Threat level" is grokbot's judgment, labeled as such.

## 1. Executive summary

1. **Hyperscalers are moving into the materials-discovery lab, not into production.** Google DeepMind is building its first automated materials lab in the UK in 2026, Gemini-integrated, making "hundreds of materials per day" (superconductors first) [src-20251211-cb7237]. Microsoft packages MatterGen/MatterSim into Microsoft Discovery with autonomous-lab orchestration and runs physical work through national labs (PNNL, JHU APL) [src-20260722-9cba8e]. Meta gives the simulation layer away (UMA, OMat24, OMol25) [src-20250514-664232][src-20250513-fbb4d8]. None of them sells parts, metal or qualified material.
2. **The candidate-generation layer is commoditizing.** GNoME's 2.2M predicted crystals [src-20231129-e0589a], open UMA weights, and rentable MatterGen [src-20261022-3e2a9d] mean "we generate candidates" is no longer a moat. The A-Lab novelty dispute shows synthesis and characterization are the real bottleneck [src-20240124-513fd9]. That favors startups that own the physical loop and the customer qualification work (Radical AI, Periodic, Lila) over pure-software materials plays.
3. **Hyperscaler talent is leaving to own labs.** Periodic Labs was founded by OpenAI's Liam Fedus and DeepMind's GNoME co-author Ekin Dogus Cubuk ($300M seed, a16z, NVIDIA, Bezos) [src-20250930-d8be97][src-20250930-2f9981]. That is the clearest sign that the people closest to the models think value sits in the lab plus the commercial deployment.
4. **NVIDIA and Siemens are the real threat to software-first factory AI.** Siemens closed Altair (Mar 2025) and Dotmatics (Jul 2025) [src-20250326-cc1810][src-20250701-a7fef9] and is building an "Industrial AI Operating System" with NVIDIA, with Erlangen as the blueprint [src-20260106-60b745]. Foxconn already runs Omniverse twins, a MoMClaw ops agent and humanoids, and claims 80% faster root-cause analysis and +15% labor productivity [src-20261022-89d710][src-20261022-3beb97]. Arda-style software sold into other people's plants faces that installed base. Owner-operators mostly buy this stack.
5. **Defense primes are partnering and investing, not acquiring yet.** Lockheed signed a seven-year deal to embed Hadrian automated cells inside its Grand Prairie munitions plant [src-20261014-015327], holds stakes in Machina (2023 and the 2026 Series C) [src-20230126-f00896][src-20260204-b22c24], and raised its venture fund to $1B [src-20260401-073d24]. RTX Ventures led Radical AI's $55M round [src-20250718-d46f24] and backs Fabri [src-20260630-cc821c]. Divergent builds Tomahawk structures for RTX [src-20260601-976843]. This is the best evidence so far for Q1 (repeat production): multi-year commitments are landing.
6. **The neo-prime is a hybrid threat.** Anduril's Arsenal-1 (~$1B, ~5M sq ft, ArsenalOS) is a customer for AI-native suppliers and a potential in-sourcer of their work [src-20250116-7ec83c][src-20260727-e6d2f4]. It is also Arda's first design partner [src-20261020-bbfb1c].
7. **Legacy primes and forgers are spending their own capex on AI and automation.** Examples: GE Aerospace ~$1B in 2026 including additive [src-20260309-3c255a]; Howmet's AI process control and ~$500M capex [src-20260301-357ec4]; Northrop Waynesboro targeting a 20% recurring-cost cut [src-20261022-1389b7]; L3Harris's automated GMLRS motor plant with $1B of government money [src-20261022-869770]. The startup edge is speed and greenfield software, not exclusive access to automation.
8. **For Series B–D, grokbot's read:** back owner-operators and closed-loop labs that sell qualified physical output on multi-year contracts. Discount software-only layers that compete head-on with Siemens/NVIDIA/Foxconn or with free hyperscaler models. Treat prime CVC stakes as validation and as an exit path, but also watch for customer concentration.

## 2. Player-by-player table

Threat = grokbot judgment for Series B–D AI-native startups. "Makes product" = does it ship physical parts/material to outside customers.

| Player | What they're building | Scale (public) | Makes product? | Relation to AI-native startups | Threat |
|---|---|---|---|---|---|
| Google DeepMind | GNoME; automated UK materials lab 2026 (Gemini-integrated) | 2.2M crystals, 380K stable; lab "hundreds of materials/day" [src-20231129-e0589a][src-20251211-cb7237] | No (R&D samples) | Competitor to AI-materials discovery; talent source (Periodic) [src-20250930-d8be97] | **High** for discovery-only; low for producers |
| Microsoft | Azure Quantum Elements → Microsoft Discovery; MatterGen/MatterSim; PNNL electrolyte | $60M Genesis Mission [src-20260722-9cba8e]; 32M candidates → 18 in <80h [src-20240109-af2802] | No | Platform vendor; partners with national labs, not startups | **Med-high** (software) |
| Meta FAIR | OC20/OMat24/OMol25 datasets, UMA models (open) | ~500M structures; UMA-m 1.4B params [src-20250514-664232] | No | Commoditizer; free inputs to startups | **Med** (erodes data moats) |
| NVIDIA | Omniverse, Isaac, Cosmos, ALCHEMI; factory blueprints | Foxconn reference [src-20261022-89d710]; ALCHEMI [src-20261022-a032ef] | No (chips) | Supplier to all; NVentures investor in Periodic [src-20250930-d8be97], Radical AI [src-20250718-d46f24], Lila [src-20251014-e9c02b] | Low (arms everyone) |
| Amazon / AWS | Industrial Innovation Fund (robotics); acquisitions Rightbot, RIVR (logistics) | ~54% of IIF portfolio robotics ([goldi.ai](https://goldi.ai/intelligence/vc/amazon-industrial-innovation-fund)) | Not in industrial parts | Investor (Standard Bots, Agility…) ([IIF](https://industrialinnovationfund.amazon/portfolio-companies)) | Low |
| Apple | $600B US commitment; American Manufacturing Program; $500M MP Materials magnets | $200M prepay [src-20250806-a0a34e] | Via suppliers | Buyer/financier template (offtake + prepay) | Low |
| OpenAI | OpenAI for Science; GPT-Rosalind (life sciences) | 30 free seats/lab [src-20261015-15af0f] | No | Talent source (Periodic founder) | Low |
| Anthropic | Claude Science; Bay Area wet lab (biology) | — [src-20260918-f473c9] | No | — | Low (bio, not materials) |
| Periodic Labs | AI scientist + autonomous lab; agents for client engineers | $300M seed; talks ~$7B (Bloomberg) [src-20250930-d8be97] | Lab output, not volume | Hyperscaler-alumni startup; peer to Radical AI | n/a (startup) |
| Siemens | Xcelerator; Altair, Dotmatics; Industrial AI OS with NVIDIA | Altair closed Mar 2025; Dotmatics Jul 2025 [src-20250326-cc1810][src-20250701-a7fef9] | Yes (own electronics plants), sells software | Competitor to software-first factory AI; acquirer of software | **High** (software-first) |
| GE Aerospace | ~$1B 2026 US manufacturing incl. metal AM; AI in FLIGHT DECK | [src-20260309-3c255a] | Yes | Customer / in-sourcer | Med |
| Honeywell | 2025 deals mostly non-AI automation (Sundyne, SparkMeter) | ([2025 AR](https://investor.honeywell.com/static-files/c7f9f713-d9e0-4a93-9b2d-a90f1ab588cb)) | Yes | Not seen in AI-native deals | Low |
| ABB | Robotics division to SoftBank ($5.375B; EU cleared Mar 2026) | [src-20251008-b6f630] | Robots | Supplier of cells | Low-med |
| Rockwell | Plex, Clearpath/OTTO; industrial-AI M&A focus ([investor day](https://stockanalysis.com/stocks/rok/transcripts/393288-investor-day-2025/)) | — | Automation hardware | Acquirer of software/robotics | Med (software) |
| Hitachi | HMAX physical-AI suite; edge AI chip; synvert | up to ¥1T M&A in Inspire 2027 [src-20260424-422a0a] | Yes | Likely acquirer | Med |
| Foxconn | FODT twins, MoMClaw agent, humanoids, Texas AI-server plant | $1.4B AI supercomputing center [src-20261022-89d710][src-20260317-a43440] | Yes (largest CM) | Competitor in electronics factory AI | **High** vs Arda-style in electronics |
| Samsung | SAIT autonomous "A-Lab"; Korea autonomous-lab consortium ([SAIT](https://semiconductor.samsung.com/sait/research/research-areas/), [SED](https://en.sedaily.com/technology/2026/08/11/korea-launches-autonomous-lab-network-as-80-institutions)) | 80+ institutions | Yes | CuspAI partner [src-20261022-37a0ea] | Med (in-house R&D) |
| BASF | Licenses Orbital CurieOS for catalysts [src-20261022-edad3e] | — | Yes | Customer | Low |
| Dow | No AI-native deal found in this pass | — | Yes | — | — |
| Merck KGaA / EMD | CuspAI partner (founding member, AI Materials Foundry) [src-20261022-37a0ea] | — | Yes | Partner/customer | Low |
| Toyota Research Institute | Accelerated Materials Design & Discovery ([TRI](https://toyotaresearchinstitute.com/amdd/)) | — | Via Toyota | Woven Capital (Toyota) in Machina Series C [src-20260204-b22c24] | Low-med |
| Mitsubishi Chemical | MI Bridge materials informatics ([MCG](https://www.mcgc.com/english/news_release/01706.html)) | — | Yes | Mitsubishi (group) in Mariana Series B [src-20260803-423f7a] | Low |
| Lockheed Martin | Hadrian embedded cells; LM Ventures $1B | 7-yr deal [src-20261014-015327]; fund $400M→$1B [src-20260401-073d24] | Yes | Customer + investor (Machina, Fabri) | Partner; possible acquirer |
| RTX | RTX Ventures; Tomahawk structures from Divergent | [src-20260630-cc821c][src-20260601-976843] | Yes | Lead investor Radical AI [src-20250718-d46f24] | Partner; possible acquirer |
| Northrop Grumman | Waynesboro digital/AI factory | 20% recurring-cost target [src-20261022-1389b7] | Yes | In-house | Med |
| General Dynamics | Not covered in free sources found | — | Yes | — | — |
| Boeing | Lockheed contract ~$14.7B to triple PAC-3 seekers ([Boeing](https://investors.boeing.com/investors/news/press-release-details/2026/Boeing-receives-seven-year-contract-to-accelerate-PAC-3-MSE-seeker-output/default.aspx)); HorizonX Digital Alloys (2018) | — | Yes | No 2026 AI-native stake found | Med |
| L3Harris | Automated GMLRS motor plant; $1B govt investment | [src-20261022-869770] | Yes | Competes for munitions demand | Med-high in munitions |
| Anduril (hybrid) | Arsenal-1, ArsenalOS | ~$1B, ~5M sq ft, >4,000 jobs planned [src-20250116-7ec83c] | Yes | Customer, Arda design partner [src-20261020-bbfb1c], in-sourcer | **High** (in-sourcing) |
| Rio Tinto | Autonomy; Founders Factory accelerator; Terra AI backer | [src-20261022-937aa1] | Yes | Investor in early-stage tools | Med (long run) |
| BHP | BHP Ventures (FieldAI, KoBold, Terra AI, GeologicAI) | [src-20261022-04e57d] | Yes | Investor in Mariana Series B [src-20260803-423f7a] | Med; investor now |
| Glencore | No AI-native deal found in this pass | — | Yes | — | — |
| Precision Castparts / PCC Forgings | Berkshire unit; see card | — | Yes | Incumbent vs Machina/Fabri | Med (qualification moat) |
| Howmet | Digital thread, AI process control; ~$500M capex | [src-20260301-357ec4] | Yes | Incumbent | Med |
| Arconic | No AI-native deal found in this pass | — | Yes | — | — |
| Jabil / Flex | Data-center power M&A: Hanley (~$725M), EPC Power ($4.4B) | [src-20261022-94abb5] | Yes | Compete for data-center hardware (an Arda target market) | Med |
| Xometry | AI marketplace; Q2'26 rev $229M, Q3 results Nov 3 ([8-K](https://www.sec.gov/Archives/edgar/data/1657573/000119312526331547/xmtr-ex99_1.htm)) | — | Network, not plants | Competitor to owner-operators on quoting/speed | Med |
| SoftBank (added) | Buying ABB Robotics for physical AI | $5.375B [src-20251008-b6f630] | Robots | Capital-rich consolidator | Med |
| Lila Sciences (added) | AI Science Factories | $550M raised, NVentures [src-20251014-e9c02b] | Lab output | Peer | n/a |

## 3. Deep dives

### Google DeepMind: GNoME to a physical lab
- GNoME (Nature, Nov 2023) predicted 2.2M crystals, 380K stable; 736 were independently realized by outside labs; a companion Berkeley A-Lab paper showed autonomous synthesis [src-20231129-e0589a].
- The A-Lab claim (41 of 58 synthesized) was challenged by Palgrave/Schoop as mostly misidentified known phases; Nature issued an author correction on the novelty claims [src-20240124-513fd9] ([correction](https://escholarship.org/uc/item/4kb4s6pg)).
- Dec 2025: DeepMind announced its first automated lab, in the UK, for 2026, "built from the ground up to be fully integrated with Gemini" and making hundreds of materials per day; superconductors first. It is part of a non-binding UK MoU [src-20251211-cb7237]. In this pass grokbot found no free source confirming the lab has opened.
- **Read:** DeepMind now owns a loop that competes for the same superconductor and battery problems as Periodic and Radical AI. But it has no stated path to qualify or sell material; Alphabet's track record is licensing and partnering. **Threat: high to discovery-only startups, low to producers.**

### Microsoft: platform plus national labs
- Jan 2024: Azure Quantum Elements screened >32M candidates down to 18 in <80h; PNNL made and tested a Na/Li/Y/Cl solid electrolyte using up to 70% less lithium [src-20240109-af2802].
- MatterGen (Nature 2025) is now an agent in Microsoft Discovery. Its own README lists the limits: ~20 atoms per cell, outputs must be DFT-validated before synthesis [src-20261022-3e2a9d].
- Jul 2026: $60M plus the SPARK office for the DOE Genesis Mission. Discovery plugs into PNNL lab automation; JHU APL runs autonomous labs with MatterGen and MatterSim [src-20260722-9cba8e].
- **Read:** Microsoft sells the operating system for labs. It is a channel or competitor for software-only AI-materials companies (CuspAI-like), not for owners of production.

### Meta FAIR: the open commoditizer
- UMA models are trained on ~500M structures (OMat24, OMol25, OC20, ODAC, OMC25), with weights and data released openly [src-20250514-664232]. OMol25 is 100M+ DFT calculations [src-20250513-fbb4d8].
- **Read:** the simulation-data moat is shrinking. Startups need proprietary experimental data (from their own lab or customer plants) to stay differentiated.

### NVIDIA: arms dealer and investor
- Stack: Omniverse/OpenUSD twins, Isaac, Cosmos, Metropolis, Factory Operations Blueprint; ALCHEMI for chemistry [src-20261022-a032ef].
- Foxconn reference: FODT twins move lines between Taiwan and Mexico [src-20261022-3beb97]. MoMClaw claims −80% root-cause time, +15% labor productivity, −10% machine failures; DeepHow vision AI adds +3% first-pass yield [src-20261022-89d710]. The Texas AI-server plant brings in humanoids [src-20260317-a43440].
- Investments: Periodic Labs [src-20250930-d8be97], Radical AI [src-20250718-d46f24], Lila [src-20251014-e9c02b].
- **Read:** NVIDIA wins either way. Its main effect is lowering the cost for incumbents to copy factory-AI software, which squeezes software-first startups.

### Siemens: the incumbent software consolidator
- Altair closed Mar 26, 2025 [src-20250326-cc1810]; Dotmatics closed Jul 1, 2025 [src-20250701-a7fef9].
- Industrial AI OS with NVIDIA (CES 2026), with Erlangen as the blueprint. Siemens' stated targets: up to 85% less engineering effort, 40% faster time-to-market, up to 20% cost savings [src-20260106-60b745].
- **Read:** the most likely acquirer of factory-software startups and the most direct competitor to Arda/Mind Robotics-type software. It does not compete with owner-operators for parts orders.

### Defense primes: partner, customer, investor
- **Lockheed:** seven-year Hadrian deal for automated machining cells inside Grand Prairie (PAC-3 MSE, THAAD, PrSM, GMLRS), commissioning early 2027 [src-20261014-015327][src-20261020-24e35c]. LM Ventures invested in Machina in 2023 and again in the Feb 2026 $124M Series C [src-20230126-f00896][src-20260204-b22c24]. Fund raised to $1B [src-20260401-073d24].
- **RTX:** RTX Ventures led Radical AI's $55M Seed+ (with NVentures, Eni Next) [src-20250718-d46f24] and invested in Fabri (automated casting) [src-20260630-cc821c]. Divergent produces Tomahawk structures [src-20260601-976843].
- **GA-ASI** partners with Divergent on UAS aerostructures [src-20261022-8629b9].
- **Northrop, L3Harris:** in-house automation. Northrop targets a 20% recurring-cost cut at Waynesboro [src-20261022-1389b7]; L3Harris has an automated GMLRS motor plant with $1B of government equity [src-20261022-869770].
- **Read:** primes are buying capacity as a service and taking minority stakes. In this pass grokbot found no prime acquisition of an AI-native producer. The "factory inside the prime" model (Hadrian at Grand Prairie) is new: strong proof of repeat orders, but a dependence risk.

### Anduril: the hybrid
- Arsenal-1: ~$1B, ~5M sq ft near Columbus, run on ArsenalOS, >4,000 jobs planned [src-20250116-7ec83c]; first Fury completed Jul 2026 [src-20260727-e6d2f4].
- Arda's first design partner [src-20261020-bbfb1c].
- **Read:** whatever Anduril can build in-house, it will. Suppliers win where the process is specialized (forming, casting, harnesses) and Anduril would rather buy.

### Mining majors (for Mariana)
- BHP Ventures invested in Mariana's $310M Series B (Khosla lead; also Mitsubishi and In-Q-Tel). Mariana targets 50,000 t/yr of refined copper at Copper One by 2030 [src-20260803-423f7a]. BHP's portfolio also includes FieldAI, KoBold, Terra AI and GeologicAI [src-20261022-04e57d].
- Rio Tinto backs early-stage tools via Founders Factory [src-20261022-937aa1]. No Glencore deal was found.
- **Read:** majors are hedging through CVC. Mariana's edge is restarting small or stranded assets on autonomy-first software that majors would not prioritize. Majors become acquirers if Copper One proves its unit costs.

### Metals and forming incumbents (for Machina)
- Howmet: digital thread, AI process control and automated inspection; ~$500M 2026 capex [src-20260301-357ec4]. GE Aerospace: ~$1B including metal AM [src-20260309-3c255a].
- **Read:** incumbents have qualification and alloy know-how and are automating in place. Machina's edge is no dedicated tooling and speed on low-volume, high-mix structures. Incumbents' moat is qualified part numbers on long-running programs.

### Contract manufacturers
- Foxconn is the most advanced AI-native incumbent factory operator (above).
- Jabil and Flex are buying data-center power hardware capability (Hanley ~$725M; EPC Power $4.4B) [src-20261022-94abb5], heading into the same end market Arda targets.
- Xometry is pitching its AI marketplace to defense and robotics buyers ([Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/11/xometry-xmtr-q2-2026-earnings-call-transcript/)).

### Others found
- **SoftBank** is buying ABB Robotics for $5.375B [src-20251008-b6f630].
- **Apple** uses offtake plus prepay ($500M MP Materials, $200M prepaid) [src-20250806-a0a34e]: a financing template for AI-native producers.
- **BASF** licenses Orbital Industries' CurieOS [src-20261022-edad3e].
- **Frontier labs:** Anthropic has a biology wet lab [src-20260918-f473c9]; OpenAI has GPT-Rosalind [src-20261015-15af0f]. Neither is in materials or manufacturing yet.
- **Lila Sciences:** $550M raised with NVentures [src-20251014-e9c02b].

## 4. Deal and relationship log (newest first)

| Date | Incumbent | Startup | Type | Source |
|---|---|---|---|---|
| 2026-10-20 | Anduril | Arda | Design partner / customer | [src-20261020-bbfb1c] |
| 2026-10-14 | Lockheed Martin | Hadrian | 7-yr embedded production cells | [src-20261014-015327] |
| 2026-08-03 | BHP Ventures, Mitsubishi, In-Q-Tel | Mariana Minerals | Series B participants ($310M) | [src-20260803-423f7a] |
| 2026-07-22 | Microsoft | DOE labs (PNNL, JHU APL) | $60M Genesis Mission | [src-20260722-9cba8e] |
| 2026-06 | RTX | Divergent | Tomahawk structures | [src-20260601-976843] |
| 2026-06-30 | RTX Ventures (+ LM Ventures) | Fabri | Investment | [src-20260630-cc821c] |
| 2026-04 | Lockheed Martin | (fund) | Venture fund to $1B | [src-20260401-073d24] |
| 2026-04 | BASF ECMS | Orbital Industries | Software licence | [src-20261022-edad3e] |
| 2026-02-04 | Lockheed Martin Ventures, Woven Capital (Toyota) | Machina Labs | Series C ($124M) | [src-20260204-b22c24] |
| 2026-01-06 | Siemens + NVIDIA | — | Industrial AI OS partnership | [src-20260106-60b745] |
| 2025-12-11 | Google DeepMind + UK govt | — | Automated materials lab MoU | [src-20251211-cb7237] |
| 2025-10-14 | NVentures | Lila Sciences | Series A extension | [src-20251014-e9c02b] |
| 2025-10-08 | SoftBank | ABB Robotics | Acquisition ($5.375B) | [src-20251008-b6f630] |
| 2025-09-30 | NVIDIA (+ a16z lead) | Periodic Labs | $300M seed | [src-20250930-d8be97] |
| 2025-08-06 | Apple | MP Materials | $500M offtake, $200M prepay | [src-20250806-a0a34e] |
| 2025-07-18 | RTX Ventures (lead), NVentures, Eni Next | Radical AI | $55M Seed+ | [src-20250718-d46f24] |
| 2025-07-01 | Siemens | Dotmatics | Acquisition (closed) | [src-20250701-a7fef9] |
| 2025-03-26 | Siemens | Altair | Acquisition (closed) | [src-20250326-cc1810] |
| 2025 | GA-ASI | Divergent | Aerostructures partnership | [src-20261022-8629b9] |
| 2023-01-26 | Lockheed Martin Ventures | Machina Labs | Investment | [src-20230126-f00896] |

**M&A of AI-native producers by incumbents:** grokbot found none in this pass. Incumbent M&A targets software (Altair, Dotmatics, Plex) and robotics (ABB→SoftBank, Clearpath→Rockwell).

## 5. Synthesis

**Where incumbents win** (grokbot judgment, grounded in the sources above)
- **Models and data.** Hyperscalers out-compute and open-source the discovery layer (GNoME, UMA, MatterGen).
- **Factory software on installed bases.** Siemens + NVIDIA + Foxconn already have the plants, the MES integration and the distribution.
- **Qualified, long-running programs.** Howmet, PCC and GE hold the qualified part numbers and are automating in place.
- **Capital for brownfield capacity.** Primes get government equity (L3Harris $1B) and fund their own expansions.

**Where AI-native startups keep a right to win**
- **Owning production and selling output, not software.** Hadrian, Machina, Divergent and Mariana sell parts or metal. Incumbents' AI tools make them better customers, not competitors.
- **Speed to new capacity on new demand.** The munitions and drone ramp is being met with multi-year deals with new entrants: Hadrian–Lockheed, Divergent–RTX.
- **Closed-loop labs that make and qualify material**, not just predict it. The A-Lab dispute shows validation is the hard part, and Periodic's founders left the hyperscalers to own it.
- **Compounding.** The edge compounds only if each program adds proprietary process data and reusable cells. Hadrian's 80% reusable capex claim is in [src-20260921-876080]. Software-only edges get competed away by Siemens/NVIDIA.

**Implications for Series B–D**
1. Prefer owner-operators and hybrids with multi-year prime commitments. Underwrite on those commitments, not on software multiples.
2. For AI-materials (Radical AI, CuspAI-like), ask whether they ship qualified matter to a paying customer. The Cronin "one or two" critique [src-20260814-b77f2d] plus hyperscaler labs means discovery-only is a weak position.
3. Prime CVC on the cap table (Lockheed, RTX, Toyota, BHP) signals a likely customer and acquirer. Diligence for concentration and right-of-first-refusal terms.
4. For software-first factory AI (Arda), the key diligence question is why Siemens/NVIDIA or Foxconn's in-house stack won't win the same customer.
5. Exit paths: in this pass, incumbents buy software and robotics, not factories. Producers may need IPO or private-equity routes, or prime M&A once margins are proven.

## 6. Open questions for expert calls

1. **Ex-Lockheed sourcing or ops lead:** How is the Hadrian Grand Prairie deal priced (per part, per cell-hour, take-or-pay)? Would Lockheed buy rather than embed? What would make Lockheed in-source the cells?
2. **Ex-RTX / RTX Ventures:** Has Radical AI delivered an alloy that entered RTX qualification? How long is alloy qualification versus the startup's runway?
3. **Ex-Google DeepMind or Microsoft Research materials scientist:** Will DeepMind's UK lab license materials, partner with producers, or stay a research facility? What share of GNoME candidates survived synthesis and characterization?
4. **Siemens or Rockwell digital-industries seller:** Where do they lose deals to startups like Arda? What's the M&A appetite for factory-AI startups after Altair?
5. **Foxconn or Jabil manufacturing engineer:** What results did digital twins and AI agents actually deliver versus the published claims (80% faster root-cause analysis)? Would they buy third-party factory AI?
6. **Ex-Anduril supply-chain lead:** Which parts does Anduril buy versus in-source at Arsenal-1? What role is Arda playing in practice?
7. **Ex-BHP or Rio Tinto autonomy lead:** Could a major replicate MarianaOS? At what Copper One unit cost would a major buy Mariana?
8. **Ex-Howmet or PCC forming/casting engineer:** On which parts can Machina-style incremental forming displace forgings or castings? How long is qualification?

## 7. Gaps and caveats
- In this pass there were no free sources on General Dynamics, Glencore, Arconic, Dow, Honeywell or Boeing AI-native deals. Treat their absence as "not found," not as "nothing exists."
- No free source confirmed the DeepMind UK lab is operating as of 2026-10-22.
- Several bodies could not be captured (paywall or blocked): Reuters, Axios, the Anduril site and LinkedIn. Those records are summary plus URL.
- Some source dates are approximate or missing where the page had no visible date; see each record.
- Valuations reported by Bloomberg (Periodic ~$7B, Lila $8.5B talks) are reported, not confirmed.
- Altair and Dotmatics deal values are not stated in the filed Siemens close releases; check before quoting.
