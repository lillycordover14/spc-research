# Affinity OBA screen, 2026-10-29

Purpose: screen SPC's Affinity sourcing lists for the best outcome-based agents under the v11 bar. The bar: the agent completes a defined unit of work end to end and owns the result. Pricing does not matter. Plain AI tools (copilots, drafting aids, chat over data, build-your-own-agent kits) fail.

Rules followed: every traction, customer and funding fact below comes from the public URL listed next to it or from the Affinity export notes, quoted as written. Company-reported figures are labelled as company claims. Nothing here was sent externally.

## Coverage

| File | Export date | Rows | Notes |
|---|---|---|---|
| LC_2026_All_organizations_export_Sep-21-2026.csv | Sep 21, 2026 | 77 | Latest LC export; primary LC source |
| LC_2026 export Sep-08-2026 (plus 3 duplicate copies) | Sep 8, 2026 | 76 | Used only for names missing from Sep 21 (Spektr, Union Technologies, Opaque) |
| LC_2026 export Sep-02-2026 (plus 2 duplicate copies) | Sep 2, 2026 | 70 | Same; Spektr appears here too |
| LS_Priority_All_organizations_export_Sep-21-2026.csv | Sep 21, 2026 | 23 | Mostly defense, infrastructure and robotics; nothing passes |
| SP_2026_All_organizations_export_Sep-21-2026.csv | Sep 21, 2026 | 56 | Tier and Financials / Key Notes columns used |
| /workspace/affinity/SP Sourcing.csv | fresh (Oct 2026) | 26 | Owners column empty; statuses mostly Initial Outreach |

All Downloads files carry an Oct 23 file time but Sep export dates in their names, so treat list status as of September. Not yet exported, so NOT screened: Sourcing (NEW) (998 rows), General Sourcing Database (830), Healthcare Sourcing (175). Healthcare Sourcing in particular could hold more E3 names.

Owner: none of the exports carries an owner field (LC and SP 2026 have a People column that lists contacts; SP Sourcing has an empty Owners column), so owner is shown as not exported.

Dedupe: 177 unique companies after normalizing names and domains (LC 77 only-LC, SP 2026 51, SP Sourcing 25, LS Priority 16, LS Priority + SP 2026 4, LC + LS Priority 3, SP 2026 + SP Sourcing 1). Scratch build: /workspace/affscreen/load.py and all.json.

## Shortlist and verdicts

Step 1 kept anything plausibly agentic from the Affinity description. Step 2 checked the website or press.

| Company | List (status) | Verdict | Job and evidence |
|---|---|---|---|
| BackOps | LC Sep-21 (Tier 3, "Circle back Q4'26; Raising Series B end of this year or early next") | Pass, strong | Relay agents resolve logistics exceptions, carrier claims and billing end to end; one deployment handled 500K+ carrier claims with 91% resolved without humans (company claim). $42M Series B led by Insight (Sep 16, 2026) after $26M Series A led by Theory (Mar 2026). backops.com/relay; prnewswire Series B release; businesswire Series A release |
| Greenlite, now Bretton AI | LC Sep-21 (Tier 3, "Recently raised $75M Series; good name in compliance space") | Pass, strong | Agents staff KYC/KYB, AML and sanctions investigations; 1.2M+ L1/L2 investigations completed; one client cut $5.35M of BPO spend (company claims). $75M Series B led by Sapphire (Feb 2026). Customers named: Robinhood, Mercury, Gusto, Lead Bank, Coastal Community Bank. businesswire.com/news/home/20260209387593; regtechanalyst; fintechfutures |
| Salient | LC Sep-21 (Tier 3, "a16z will get us an intro meeting ahead of raise") | Pass, strong | Voice and omnichannel agents run auto-loan servicing and collections end to end. Customers: Westlake, ACA, Exeter, CPS (CPS press release). Westlake CEO cites $12M a year saved. a16z led Series A; $60M raised Jul 2025; site says $75M total and $1B+ processed. trysalient.com; a16z.com/announcement/investing-in-salient; ir.consumerportfolio.com release |
| TJM Labs | LC Sep-21 (Tier 3, "Just raised Series B Jul'26") | Pass | Pharmacy agents do intake, data entry, refills and prior-auth support; 550+ pharmacies and 1M+ tasks a day per site (Oct 2026), 450+ and 500K a day in the Jul release. $100M total incl. $75M Series B led by Elephant; acquired EncoreRx and Pharmesol. Pharmacist still verifies. tjmlabs.com/ai-agents-for-pharmacy; pillsburylaw; updata.com |
| Mechanical Orchard | LC Sep-21 (Tier 3, "Lorenzo held meeting") | Pass | Imogen rewrites mainframe applications end to end into verified production code. Customers: SulAmerica, a North American bank, a Fortune 100 retailer. $80M+ raised (GV, Emergence, Munich Re Ventures); partners Thoughtworks and Leidos. mechanical-orchard.com |
| Tessera Labs | LC Sep-21 (listed in Affinity under a stealth placeholder name, tesseralabs.ai; no status) | Pass, early | Multi-agent system runs ERP modernization, including SAP ECC to S/4HANA migration, data mapping and code conversion. $60M Series A led by a16z (May 2026). No named customers found. businesswire.com/news/home/20260506853624; a16z.com/announcement/investing-in-tessera-labs |
| Adaptive Innovations | LC Sep-21 (Tier 3, "Interesting thesis; strong cap table and team") | Pass, strong on ownership | AI-native home health provider: it delivers the care and runs intake, scheduling, charting, billing and compliance itself, so it owns the result. $50M Series A led by Felicis and Bain Capital Ventures, $60M total (Jun 2026). adaptive.co/blog/introducing-adaptive-innovations; felicis.com blog; finsmes |
| Alaffia Health | SP 2026 Sep-21 ("Maybe Drop / Early Watch") | Pass | Agents plus clinician review run health-plan payment integrity, utilization review and appeals on full medical records. $55M Series B led by Transformation Capital (Feb 2026). businesswire.com/news/home/20260203113559; siliconangle |
| Niural | SP 2026 Sep-21 (Tier 3) | Pass | AI-native global PEO; EMMA executes payroll, onboarding, compliance and payments, and the PEO carries the employer obligation. $31M Series A (Jun 2025), extended to $52M (Jun 2026). prnewswire Series A and AI Labs releases; niural.com/ai |
| Convey | LC Sep-21 (no status) | Pass, platform caveat | Operators train "digital teammates" that run invoice processing, reconciliation and reporting; 1.1M+ hours of work done for NBCUniversal, Samsara, Unity, Faire, ChargePoint, TelevisaUnivision (company claim). $38M Series A led by a16z (Jun 2026). convey.dev; businesswire.com/news/home/20260617486214 |
| Sable | LC Sep-21 (Tier 3, "just raised large seed round. Decagon & Notion as customers") | Pass, narrow job | AI employee runs live product demos, onboarding and customer calls by driving the real product. $45M from Sequoia and 8VC (Jul 2026); customers Notion and Decagon. fortune.com 2026/07/16 Sable article; 8vc.com Sable post |
| Autonomize AI | SP 2026 Sep-21 (Tier 3) | Pass | Prior authorization and utilization management agents, live at three of the five largest US health plans (company claim). $28M Series A (Jun 2025), Cigna Group Ventures among leads. autonomize.ai Series A post |
| Novella | SP Sourcing fresh (Initial Outreach) | Pass, strong on ownership | AI-powered licensed wholesale insurance broker for E&S risks; building agents for placement, binding, endorsements and renewals. $21M raised incl. $16M Series A led by Brewer Lane (May 2026). bynovella.com blog; morningstar businesswire item |
| InstaLILY | LC Sep-21 (Tier 3, "Raised Series B Jul'26; revenue grew 5x YoY") | Pass, mixed | InstaWorkers run distribution workflows; Lily is an AI forward-deployed engineer. $60M Series B led by Energize (Jul 2026). siliconangle 2026/07/14; mdm.com |
| Tidalwave | SP Sourcing fresh (Initial Outreach) | Borderline | Mortgage ops automation (document review, verification, underwriting workflow). $22M Series A (Nov 2025); lenders NEXA, First Colony, DHI Mortgage. businesswire.com/news/home/20251121765520 |
| Spektr | LC Sep-08 and Sep-02 only (dropped from Sep-21) | Borderline | KYC/KYB agents, compliance team approves. $20M Series A led by NEA (Apr 2026). businesswire.com/news/home/20260416218452 |
| Duna | SP 2026 Sep-21 (Tier 3) | Borderline | KYB agents with human review on escalations; reads as compliance infrastructure. EUR 30M Series A led by CapitalG (Feb 2026). duna.com news |
| Assured | SP 2026 Sep-21 (Tier 3) | Borderline | P&C claims agent handles about 70% of customer interactions and supports adjusters (company claim). Funding not confirmed (search hits were a different Assured). assured.com |
| Nova Intelligence | LC Sep-21 (no status) | Borderline (tool) | Agents help SAP teams analyze and modernize custom code; Kyndryl case says 75% less manual effort. $40M seed plus A (Chemistry). novaintelligence.com/blog/series-a |
| Brain Co. | LC Sep-21 (no status) | Borderline (services) | Builds custom AI systems for governments and hospitals; Qatar permit case. $30M Series A (Sep 2025). prnewswire launch release |
| Free Market Health | SP 2026 Sep-21 (Tier 1) | Fail | Specialty pharmacy referral marketplace platform, not an agent completing work |
| Edra | SP 2026 Sep-21 (Tier 3) | Fail | Platform that turns tickets and logs into playbooks for agents; a build kit. $30M Series A led by Sequoia (Mar 2026). techcrunch 2026/03/18 |
| GovDash | SP Sourcing fresh | Fail | Proposal and capture software for contractors; a tool |
| Polimorphic | SP Sourcing fresh | Fail | Chatbots, CRM and workflow for local government; a tool |
| &AI | SP Sourcing fresh | Fail | Workspace for patent litigators; a drafting tool |
| Town | LC Sep-21 (no status) | Fail | Began as AI-native tax firm, now a general AI assistant (Series B Oct 2026) |
| Workfabric AI | SP 2026 Sep-21 (Tier 2) | Flag | Kept on the C line per instruction. No new evidence found either way; v11 verified.md already says it does not clearly pass. Needs Lilly's call |
| Magentic, Strala, Anterior, Edison Scientific | Existing examples on LC or SP 2026 | Kept | Already verified in outcome-based-agents-verified.md |

Screened out from descriptions without a web check (plain tools, platforms, data or non-agent businesses): Peer, Translucent AI, Cheiron, Conduct AI, Document Crunch, Elicit, Scope, dili, intuigence, Axiamatic, Conquer, Lyzr, Applied Compute, Skan.ai, Sycamore, Notch, plus all LS Priority names. These can be rechecked if wanted.

## Flagged: the 13 most interesting

1. BackOps (E2, LC Tier 3): resolves logistics claims and billing exceptions end to end at scale, two rounds in 2026, and the LC note says a Series B raise is coming.
2. Bretton AI, formerly Greenlite (E2, LC Tier 3): completes KYC and AML investigations that banks used to send to BPOs, with named fintech and bank customers and a $75M Series B.
3. Salient (E2, LC Tier 3): runs auto-loan servicing and collections for named public lenders, with a lender CEO citing $12M a year saved; a16z can broker the intro.
4. TJM Labs (E3, LC Tier 3): does pharmacy technician work across 550+ pharmacies and buys pharmacies to own the workflow.
5. Adaptive Innovations (E3, LC Tier 3): the clearest owner of the result, because it is the licensed home health provider and runs the operations with AI.
6. Mechanical Orchard (D, LC Tier 3, Lorenzo met): finishes mainframe rewrites to verified production code for a bank, an insurer and a Fortune 100 retailer.
7. Tessera Labs (D, LC): a16z-backed agents that run ERP and SAP migrations, the SI work that D displaces; early on customers.
8. Alaffia Health (E3, SP 2026): payment integrity and appeals for health plans, with clinicians in the loop and a $55M Series B; SP status says Maybe Drop, worth a second look under v11.
9. Niural (E2, SP 2026 Tier 3): a PEO that carries the employer obligation and uses its agent to run payroll and compliance.
10. Convey (C, LC): AI teammates with 1.1M+ claimed hours of finished work at named enterprises; caveat that operators train them, so it sits close to a platform.
11. Sable (E1, LC Tier 3): an AI employee that runs whole demos and onboarding calls for Notion and Decagon.
12. Novella (E3, SP Sourcing fresh): a licensed AI-native insurance broker, so it owns placement and binding.
13. Autonomize AI (E3, SP 2026 Tier 3): prior auth and UM agents at three of the five largest health plans (company claim); overlaps Anterior.

Bench: InstaLILY (5x revenue, but part platform), Spektr and Duna (compliance with human approval), Tidalwave.

## Example lines applied in the v11 build (as amended in v12)

- A: OpenAI, Anthropic, Google, Microsoft, Amazon Web Services, LangChain (unchanged)
- B: Salesforce, Zendesk, HubSpot, ServiceNow, SAP, Oracle, Workday (unchanged; SAP and Workday still lack a filed source)
- C: Ema, Duvo, Convey, Workfabric AI (Workfabric flagged)
- D: Crescendo, Otera, Mechanical Orchard, Tessera Labs, Accenture, Deloitte, Cognizant, Teleperformance (cut Distyl AI, TCS, Conduent)
- E1: Sierra, Decagon, Gradient Labs (cut Lorikeet, Vida; Sable was added in v11 and cut in v12 after AI-Native Production QA, because demos and qualification are a step in the sale rather than an owned result)
- E2: Basis, Freehand, Magentic, Didero, Salient, Bretton AI, BackOps, Niural (cut fileAI, Augment, Lio, HappyRobot). In v12 the section was retitled "E2. Back-Office Operations: Finance, Compliance and Supply Chain" so Bretton AI and BackOps sit inside its scope
- E3: EvenUp, Crosby, Lawhive, Anterior, SmarterDx, Procode, TJM Labs, Adaptive Innovations, Alaffia Health, Reserv, Harper, Pace, Strala, Edison Scientific (cut Prosper AI, Amperos Health, GenHealth.ai)

Not added to keep lines tight: Novella (Harper covers brokerage) and Autonomize AI (Anterior covers prior auth).

New names are not filed as sources in sources/ or companies/ because writes are limited to this theme folder; the URLs above are the evidence.

## Deduped Affinity companies (177)

| Company | Domain | List(s) and export | Status (first list) |
|---|---|---|---|
| &AI | tryandai.com | SP Sourcing (fresh) | Initial Outreach |
| 101domain GRS Limited | knoxsystems.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| \N | gridcare.ai | LS Priority (Sep-21), SP 2026 (Sep-21) | Identified / 2H:Yes / Grid / Power for AI |
| Aaru | aaru.com | SP 2026 (Sep-21) | Tier 3 |
| Acryl Data | datahub.com | SP Sourcing (fresh) | Initial Outreach |
| Adaptive | adaptive.co | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Interesting thesis; strong cap table and team |
| Agon.com |  | LS Priority (Sep-21) | Initial Outreach / 2H:TBD / Defense & Sovereign Autonomy |
| AirGarage | airgara.ge | SP Sourcing (fresh) | Initial Outreach |
| Airspace Intelligence | airspace-intelligence.com | SP 2026 (Sep-21) | Tier 2 |
| Alaffia Health | alaffia.ai | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Altara | altara.co | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Launched out of stealth May'26. To track |
| Ambrook | ambrook.com | SP Sourcing (fresh) | Initial Outreach |
| Amca | amca.co | SP 2026 (Sep-21) | Tier 3 |
| Analogical Engines | analogicalengines.com | SP 2026 (Sep-21) | Tier 3 |
| AndrenaM | andrenam.com | LC (Sep-21), LC (Sep-08) |  |
| Anterior | anterior.com | SP 2026 (Sep-21) | Tier 2 |
| Apoha | apoha.ai | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Applied Compute | appliedcompute.com | SP 2026 (Sep-21) |  |
| Aranya | aranya.tech | LS Priority (Sep-21) | Identified / 2H:TBD / Inference Economics |
| Archetype AI | archetypeai.io | SP 2026 (Sep-21) | On Hold |
| Archimetis | archimetis.ai | LC (Sep-21), LC (Sep-08) |  |
| Architect | architectlabs.com | LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Silicon Design |
| ARDA | arda.ai | LS Priority (Sep-21) | Meeting / 2H:Yes / Autonomous Factories I Engineering |
| Arondite | arondite.com | LC (Sep-21), LC (Sep-08) |  |
| Aslan | aslanprotects.com | SP 2026 (Sep-21) |  |
| Assured Insurance Technologies | assured.claims | SP 2026 (Sep-21) | Tier 3 |
| Atomic Canyon | atomic-canyon.com | SP Sourcing (fresh) | Initial Outreach |
| Autonomize | autonomize.ai | SP 2026 (Sep-21) | Tier 3 |
| Axiamatic | axiamatic.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Axiomatic_AI | axiomatic-ai.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Part of verification thesis; to see how verification pla |
| axle energy | axle.energy | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| BackOps | backops.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Circle back Q4'26; Raising Series B end of this year or early |
| bedrock robotics | bedrockrobotics.com | SP 2026 (Sep-21) | Tier 2 |
| BIORCE | biorce.com | SP 2026 (Sep-21) | On Hold |
| Brain Co. | brain.co | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Callosum | callosum.com | LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Inference Economics |
| Camus Energy | camus.energy | SP 2026 (Sep-21) | Tier 3 |
| CarOnSale | caronsale.de | SP Sourcing (fresh) | Initial Outreach |
| Cheiron | cheiron.bio | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Ciridae | ciridae.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Reach out post Labor Day. Reached out Jul'26; to reach out in |
| CivilGrid | civilgrid.com | SP 2026 (Sep-21) | On Hold |
| Clarium Health | clariumhealth.com | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| cognichip | cognichip.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Check back quarterly. Part of chip thesis; I think most  |
| Collate | collate.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Raised $95M funding from Redpoint Jun'26 |
| Compass Regulatory | compassregulatory.com | SP Sourcing (fresh) | Initial Outreach |
| Conduct AI Ltd. | conduct.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / DHL is customer; built on SAP who is also an investor |
| Conquer Technology Ltd | conquer.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Convey | convey.dev | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Convoke | convoke.bio | SP 2026 (Sep-21) | Tier 3 |
| Corma.ai |  | LS Priority (Sep-21) | Initial Outreach / 2H:TBD / Defense & Sovereign Autonomy |
| CVector Energy Corp | cvector.energy | SP 2026 (Sep-21) | Tier 3 |
| dili | dili.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Diode Computers | diode.computer | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Rethinking the PCB workflow by embedding AI and real-wor |
| Dirac | diracinc.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Siemens just invested $10M 8 months ago. Customers like mitsu |
| discoveryloop | discoveryloop.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| DOCUMENT CRUNCH | documentcrunch.com | SP Sourcing (fresh) | Initial Outreach |
| dominion Dynamics | dominion-dynamics.com | LS Priority (Sep-21) | Identified / 2H:TBD / Defense & Sovereign Autonomy |
| Duna Trading s.a.u. | duna.com | SP 2026 (Sep-21) | Tier 3 |
| Duranta | getduranta.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Follow up 1st or 2nd week of November |
| E- Licit | elicit.com | SP Sourcing (fresh) | Initial Outreach |
| Edison Scientific Inc. | edisonscientific.com | SP 2026 (Sep-21) | Tier 2 |
| Edra.ai | edra.ai | SP 2026 (Sep-21) | Tier 3 |
| Ellipsis Health | ellipsishealth.com | SP 2026 (Sep-21) | On Hold |
| Endra | endra.ai | LS Priority (Sep-21) | Initial Outreach / 2H:TBD / Autonomous Factories I Engineering |
| Enzo Health | enzo.health | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| etalytics | etalytics.de | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| EthonAI | ethon.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Customers like Siemens, Roche, Lindt |
| Faro Health | farohealth.com | SP 2026 (Sep-21) | Tier 3 |
| Field AI | fieldai.com | LS Priority (Sep-21) | Live Deal / 2H:Yes / Physical AI I Robotics |
| Flourish | flourishlabs.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Foxglove | foxglove.dev | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Potentially wait until OEM traction; check back every quarter |
| Free Market Health | freemarkethealth.com | SP 2026 (Sep-21) | Tier 1 |
| Friday Harbor | fridayharbor.ai | SP Sourcing (fresh) | Early Track |
| Genieai | genieai.tech | SP Sourcing (fresh) | Initial Outreach |
| gimlet labs, inc. | gimletlabs.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| goodfire | goodfire.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02), LS Priority (Sep-21) | Identified / 2H:TBD / Frontier Intelligence |
| Govdash (YC W22) | govdash.com | SP Sourcing (fresh) | Initial Outreach |
| Greenlite | greenlite.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Recently raised $75M Series; good name in compliance space |
| Gridsight | gridsight.ai | SP 2026 (Sep-21) | Tier 3 |
| HavocAI | havocai.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| hellosmartsuite | smartsuite.com | SP Sourcing (fresh) | Initial Outreach |
| Hilbert's Program | hilberts.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Just raised Series A Apr'26 by a16z. Walmart, Levain, Blank S |
| HockeyStack | hockeystack.com | SP Sourcing (fresh) | Initial Outreach |
| Hyper | callhyper.com | SP Sourcing (fresh) | Initial Outreach |
| incident_io | incident.io | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Instalily.ai | instalily.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Raised Series B Jul'26; revenue grew 5x YoY |
| Integral | useintegral.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Early track |
| intuigence.ai | intuigenceai.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| isembard | isembard.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Check back in during Q3; reached out to CEO a couple months a |
| Itera Inc. | itera.co | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Decide if interesting; selling electronics prototyping a |
| Katalyze AI | katalyzeai.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Brooke had a relationship last year. Is it interesting?  |
| Keenable.ai | keenable.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Kharon | kharon.com | SP 2026 (Sep-21), SP Sourcing (fresh) | Tier 1 |
| Lovelace.AI | lovelace.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Lyzr | lyzr.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Raised Series B Jul'26 |
| Machina Labs | machinalabs.ai | SP 2026 (Sep-21) | Tier 3 |
| Magentic | magentic.com | LC (Sep-21) |  |
| Mangomint | mangomint.com | SP Sourcing (fresh) | Initial Outreach |
| Mariana Minerals | marianaminerals.com | LS Priority (Sep-21), SP 2026 (Sep-21) | Initial Outreach / 2H:Yes / Autonomous Factories I Engineering |
| Marlow | gomarlow.com | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Meadow | meadowfi.com | SP Sourcing (fresh) | Initial Outreach |
| Mechanical Orchard | mechanical-orchard.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Lorenzo held meeting; seems interesting to track and tackling |
| Mine Vision Systems | minevisionsystems.com | SP 2026 (Sep-21) | Tier 3 |
| Mithrl | mithrl.com | SP 2026 (Sep-21) |  |
| MoeGo Gallery | moego.pet | SP Sourcing (fresh) | Initial Outreach |
| NetBox Labs | netboxlabs.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 2 / Lorenzo to reach out to Headline when in SF |
| Netris | netris.io | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / a16z invested in Series A Q2'26 |
| niural | niural.com | SP 2026 (Sep-21) | Tier 3 |
| NODA AI | nodaintelligence.ai | LS Priority (Sep-21) | Meeting / 2H:Yes / Defense & Sovereign Autonomy |
| Noetive | noetive.ai | LS Priority (Sep-21) | Identified / 2H:TBD / Physical AI I Robotics |
| Notch | notch.cx | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Nova Intelligence | novaintelligence.com | LC (Sep-21) |  |
| Novella | bynovella.com | SP Sourcing (fresh) | Initial Outreach |
| Novellia | novellia.com | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Nox Metals | noxmetals.co | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / AI-first vertically-integrated shop; interesting thesis  |
| Onos | onoshealth.com | SP 2026 (Sep-21) | Tier 3 |
| Opaque Systems | opaque.co | LC (Sep-08) |  |
| OpturaAI | optura.ai | SP 2026 (Sep-21) | On Hold |
| outset.ai | outset.ai | SP 2026 (Sep-21) | Tier 3 |
| p-1 ai | p-1.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Held first intro call |
| Parspec | parspec.io | SP Sourcing (fresh) | Initial Outreach |
| Peer | getpeer.ai | SP 2026 (Sep-21) | Tier 3 |
| Perceptic | perceptic.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / CEO is ex-Palantir partner of Life Sciences & Healthcare |
| Physical Superintelligence PBC | psi.inc | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Polimorphic | polimorphic.com | SP Sourcing (fresh) | Initial Outreach |
| Popai Health | popai.health | SP 2026 (Sep-21) | Tier 3 |
| Pramaana Labs | pramaanalabs.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Verification thesis; to track |
| Provision | getprovision.co | SP Sourcing (fresh) | Initial Outreach |
| Qualified Health | qualifiedhealthai.com | SP 2026 (Sep-21) | Tier 2 |
| Quilter | quilter.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Seems interesting; Reached out to CEO Q1'26 who said heads do |
| Radify | radifymetals.com | SP 2026 (Sep-21) |  |
| Rally (YC W22) | rallyuxr.com | SP Sourcing (fresh) | To Email |
| Recursive Superintelligence | recursive.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Revel | revel.io | LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Autonomous Factories I Engineering |
| Sable AI, Inc. | withsable.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / just raised large seed round. Decagon & Notion as customers.  |
| Sail Research | sailresearch.com | LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Inference Economics |
| Salient | trysalient.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / a16z will get us an intro meeting ahead of raise; not taking  |
| Scope | getscope.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Mostly European customers; Pacific Gas & Electric in USA pilo |
| Seekr.com | seekr.com | LC (Sep-21) |  |
| Semaphor | semaphorsurgical.com | SP 2026 (Sep-21) | Maybe Drop / Early Watch |
| Sift | sift.com | SP 2026 (Sep-21) | Tier 2 |
| Simile | simile.ai | SP 2026 (Sep-21) | Tier 3 |
| skan.ai | skan.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| SkyPilot | skypilot.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| smack technologies inc. | smacktechnologies.com | LS Priority (Sep-21) | Initial Outreach / 2H:TBD / Defense & Sovereign Autonomy |
| Spektr | spektr.com | LC (Sep-08), LC (Sep-02) |  |
| Tessera Labs (Affinity stealth placeholder name) | tesseralabs.ai | LC (Sep-21) |  |
| Steelhead Technologies | gosteelhead.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| StirlingX | stirlingx.io | LC (Sep-21), LC (Sep-08) |  |
| Strala.ai | strala.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Strong team; case studies are coming soon; attempted out |
| Striveworks | striveworks.us | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Sycamore | sycamore.so | SP 2026 (Sep-21) | On Hold |
| Taktile | taktile.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Just raised Series C; have tried reaching out 5x+ times; pote |
| tem. | tem.energy | SP 2026 (Sep-21) | Tier 3 |
| TerraAI | terraai.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Mining thesis - think this is an interesting area; all softwa |
| TerraFirma, Inc | terrafirma.inc | LS Priority (Sep-21) | Initial Outreach / 2H:TBD / Autonomous Factories I Engineering |
| Texture | texture.energy | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Early Track / Strong CEO; interesting energy angle; have tried reachin |
| The Engineering Company | flowengineering.com | LS Priority (Sep-21) | Meeting / 2H:TBD / Autonomous Factories I Engineering |
| TheCRM | thecrm.com | SP Sourcing (fresh) | Initial Outreach |
| ThinkLabs AI, Inc. | thinklabs.ai | LS Priority (Sep-21), SP 2026 (Sep-21) | Live Deal / 2H:Yes / Grid / Power for AI |
| Tidalwave.ai | tidalwave.ai | SP Sourcing (fresh) | Initial Outreach |
| TJM Labs | tjmlabs.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Just raised Series B Jul'26; reach out in a year when closer  |
| Town | town.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Trajectory | trajectory.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02), LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Agentic Enterprise |
| Translucent AI | translucent.ai | SP 2026 (Sep-21) | Tier 2 |
| TurbineOne | turbineone.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Turing Engram Systems | engram.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Msft, Harvey, and Notion are customers. Emerged from stealth  |
| Twin1 | twin1.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Unconventional AI | unconv.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Union Technologies | union.tech | LC (Sep-08) |  |
| Upscale trading | upscale.com | LC (Sep-21), LC (Sep-08), LC (Sep-02) | Tier 3 / Networking thesis |
| Valarian Technologies | valarian.com | LC (Sep-21), LC (Sep-08), LC (Sep-02), LS Priority (Sep-21) | Initial Outreach / 2H:Yes / Defense & Sovereign Autonomy |
| Veeda AI | veeda.ai | LC (Sep-21), LC (Sep-08), LC (Sep-02) |  |
| Verse | verse.inc | SP 2026 (Sep-21) | Tier 3 |
| wafer.ai | wafer.ai | LS Priority (Sep-21), SP 2026 (Sep-21) | Identified / 2H:Yes / Inference Economics |
| Workfabric AI | workfabric.com | SP 2026 (Sep-21) | Tier 2 |
| xdof.ai | xdof.ai | SP 2026 (Sep-21) | Tier 3 |