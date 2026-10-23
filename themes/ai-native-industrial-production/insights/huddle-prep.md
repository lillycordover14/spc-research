# Huddle prep: Wed/Thu Oct 28–29, 2026

Category: companies that run their own plants on in-house software and robotics. **A** = owner-operators that sell parts or material; **B** = software platforms used in plants owned by others.
Her four questions: **Q1** repeat production orders · **Q2** right to win and whether it compounds · **Q3** Series B–D producers beyond Arda · **Q4** expert calls (Mariana, Machina, Radical AI, Arda).
Supporting docs: [raising-now](raising-now.md) · [repeat-orders-evidence](repeat-orders-evidence.md) · [unit-economics](unit-economics.md) · [failures-and-pivots](failures-and-pivots.md) · [incumbents-vs-ai-native](incumbents-vs-ai-native.md) · [comments-aggregate](comments-aggregate.md)

## 60-second answers
- **Q1:** The best public evidence is Firestorm (A): 19 federal awards worth $53.8M, climbing from SBIR to a Phase III IDIQ with task orders. Next are Hadrian (A): a $79.4M Army contract plus Lockheed embedding Hadrian cells at Grand Prairie for seven years, and Machina (A): 13 AF/NASA awards since 2020. Mariana, Arda, 1872 and NOx have **no federal prime awards**; any proof has to come from commercial offtakes and subcontracts, which is what the calls are for.
- **Q2:** The quantifiable edge is utilization: Hadrian claims 75–80% vs a 34% industry average for spindle in-cut time. Proto Labs' 49% factory GM is the ceiling for an owner-operator. Past failures (Desktop Metal, Markforged, Fast Radius) sold equipment or scaled capex ahead of repeat demand. Survivors (Velo3D, Divergent) pivoted to defense repeat buyers.
- **Q3:** Form D shows these raising now: AMCA (A; SPV $125M offered, $0 sold, filed Oct 1), Firestorm (A; $40M remaining), Vulcan Elements (A; $114M remaining), Machina (A; $13.7M remaining) and Hadrian (A; WCM SPV). Mariana (A) closed its $310M round in Aug 2026.
- **Q4:** No commenter is a verified customer or ex-employee of the four. The shortlist below is ranked by role; names come from repo sources.

## A vs B: what to test on calls
| | A (Mariana, Machina, Radical AI, Hadrian, 1872, NOx) | B (Arda) |
|---|---|---|
| Proof of repeat demand | Contract structure: per part, take-or-pay, multi-year | Seat or usage expansion across plants and divisions beyond Anduril |
| Compounding | Process data from own plant feeds the next part and raises yield | Data across many plants, but who owns it? |
| Margin | 25–45% GM [E]; capex heavy | Software margins [E]; risk of competing with Siemens/NVIDIA |
| Failure analog | Fast Radius, VulcanForms | Bright Machines |

## Ranked expert shortlist
Customer and former-employee targets are roles to source through expert networks or LinkedIn; none are named in public sources. Named people are from comments-aggregate.md and incumbents-vs-ai-native.md.

| # | Expert type | Company (A/B) | Why | Qs |
|---|---|---|---|---|
| 1 | Former Machina Labs ops/manufacturing engineer | Machina (A) | Cycle time, yield and qualification; the 16-month open Form D | Q1, Q2 |
| 2 | AF Research Lab or prime (Lockheed) sheet-metal buyer, a Machina customer | Machina (A) | Repeat buyer since 2020; LM Ventures is an investor | Q1 |
| 3 | Ex-Anduril supply-chain or manufacturing-engineering lead (Arda user) | Arda (B) | Only known customer; 10h→15min claim; Arsenal-1 in-sourcing risk | Q1, Q2 |
| 4 | Former Arda employee (deployment or forward-deployed engineering) | Arda (B) | Services intensity vs software margin; pipeline beyond Anduril | Q2 |
| 5 | Former Mariana Minerals operations or MarianaOS engineer | Mariana (A) | Copper One ramp, cost per ton, software vs EPC | Q1, Q2 |
| 6 | Copper offtaker or trader, or ex-BHP/Rio autonomy lead | Mariana (A) | Offtake terms; whether a major could replicate it (BHP Ventures is an investor) | Q1, Q2 |
| 7 | Ex-RTX materials/qualification or RTX Ventures (Radical AI lead investor) | Radical AI (A) | Has any alloy entered qualification? Timeline vs runway | Q1, Q2 |
| 8 | Former Radical AI scientist or engineer | Radical AI (A) | Lab throughput, path from data to sold material | Q2 |
| 9 | Adele Ratcliff, DoD IBAS director [src-20261022-9367ca] | Buyer (DoD) | How DoD sustains awards beyond SBIR to production | Q1 |
| 10 | Jason Premo (Acclaim Aerospace); Brian Barton (Penn United) [src-20261018-c4b4cf]; Kamila Zhong (Precision CNC) [src-20261022-66fe7f] | Job shops | Incumbent view of right to win and pricing | Q2 |
| 11 | Anthony Yamson, Xometry corp dev [src-20261012-539c82] | Network comparator | Marketplace vs owner-operator economics | Q2, Q3 |
| 12 | Ex-Howmet/PCC forming engineer; Linden Schrecker (scale-up) [src-20261022-83d2a8] | Incumbent/materials | Can incremental forming displace forgings? Scale-up reality | Q2 |

## Questions by expert type (Q-tag)

**Customers of A (Machina, Mariana, Hadrian-type buyers)**
1. Is this a production contract or a development effort? How many part numbers or tons, and on what term? (Q1)
2. Pricing basis: per part, per hour or take-or-pay? Premium or discount to your incumbent supplier? (Q1, Q2)
3. Qualification: how long did first-article and AS9100/NADCAP approval take, and does it carry over to the next part? (Q1, Q2)
4. Has lead time or quality improved order over order? Give numbers. (Q2)
5. What would make you dual-source, in-source, or switch back to a job shop or overseas supplier? (Q2)
6. Which other vertically integrated producers are you buying from or evaluating? (Q3)

**Former employees of A (Machina, Mariana, Radical AI)**
1. Real utilization, yield and scrap now vs a year ago? (Q2)
2. What software is actually in-house vs bought (CAM, scheduling, inspection)? (Q2)
3. What share of revenue is repeat production vs R&D or NRE? Who are the top three customers? (Q1)
4. Capex per cell or plant and payback; how is the plant financed? (Q2)
5. Where did the pilot-to-volume transition break? (the VulcanForms and Bright Machines pattern) (Q2)
6. Is the company raising, and on what milestone? (Q3)
7. Which competitors or peers would you back? (Q3)

**Arda customers and ex-Arda staff (B)**
1. What do you pay (usage-based), and how has the spend grown since rollout? (Q1)
2. Does Arda own or reuse data across customers? Would you let it? (Q2)
3. How much forward-deployed engineering is needed per site? (Q2)
4. Arda vs Siemens/NVIDIA/Rockwell digital tools: why did you choose Arda? (Q2)
5. Is the robotics-line roadmap real? Would Arda start operating plants (move toward A)? (Q2, Q3)
6. Deployments beyond Anduril: how many and how deep? (Q1)

**Job shops and network comparators (Premo, Barton, Zhong, Yamson)**
1. Your shop rate, utilization and gross margin; where do AI-native shops undercut you? (Q2)
2. Lost deals to Hadrian/Machina/SendCutSend: which parts and why? (Q2)
3. Could you buy the same automation (cells, CAM AI) and close the gap? (Q2)
4. Which AI-native producers are winning repeat defense work? (Q1, Q3)
5. Is labor or capital the binding constraint? (Q2)

**Government and prime buyers (Ratcliff, ex-Lockheed/RTX/Anduril)**
1. How do SBIR or OTA awards become production IDIQs? Which companies are at that stage? (Q1)
2. Would you embed (Hadrian–Lockheed), buy parts, or acquire? (Q1, Q2)
3. Which qualification steps are a moat and which are only a tax? (Q2)
4. Which B–D producers are on your shortlist now? (Q3)
5. How does the munitions and Golden Dome ramp change order duration? (Q1)

## Gaps to close before the huddle
- No verified customer or ex-employee names for the four targets; source them through an expert network.
- Federal data misses subcontracts and OTAs (Divergent, Arda, Mariana).
- No private GM, utilization or capex disclosures. Uncollected comment threads: Arda launch, Mariana, Radical AI.
