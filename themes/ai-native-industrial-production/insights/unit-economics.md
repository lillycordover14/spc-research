# Unit economics: AI-native producers vs job shops (as of 2026-10-23)

Thesis question 2: does AI-native have a right to win, and does the edge compound? Labels: **[R]** = reported (public filings or company statements), **[E]** = estimate or derived by grokbot; treat as directional. Company statements are self-reported and unaudited.

## Public benchmarks
| Metric | Job shop / incumbent | Digital or AI-native | Source |
|---|---|---|---|
| Gross margin, own factory | Proto Labs factory non-GAAP GM **49%** [R] (automated quick-turn, closest public analog to an owner-operator) | n/a; no private AI-native producer discloses GM | src-20260206-2b13c7 |
| Gross margin, network/marketplace | Proto Labs network **31%** [R]; Xometry marketplace **34.7%** FY25 [R] | Arda-type software would carry software margins; usage-based pricing [R], margin undisclosed | src-20260224-a7b149, src-20261020-a1e174 |
| Company-level profitability | Proto Labs adj. EBITDA 14.7%, net income $21.2M [R]; Xometry adj. EBITDA $18.5M, GAAP net loss $61.7M [R] | none public | src-20260206-8bb619 |
| Spindle utilization | Average VMC in-cut spindle use **34%** vs a 70% target (survey of 100+ US plants) [R] | Hadrian claims **75–80% uptime vs ~30%** for conventional aerospace shops [R] | src-20250120-419768, src-20251024-2e5383 |
| Labor leverage | Typical ratio of about 2 machines per operator; 10% of machinists leave the industry each year [R] | Hadrian: ~10 robots per operator, workers trained in 30 days and "10x more productive" [R] | src-20251024-2e5383, src-20250717-870195 |
| Shop rate | 3-axis $35–75/h; 5-axis $75–150/h; mid-size shops $65–85/h; Tier-1 aerospace $110–150/h [R] | Not disclosed. Owner-operators price per part and on lead time | src-20261023-58b5a8, src-20261023-6ef991 |
| Tooling / capex per part family | Stamping dies cost months and up to $1M+ per design; a full sedan die set is about $200M (LinkedIn commenter) [R] | Machina: no dies, savings of more than $1M per design, 10x lead-time cut; cycle time 30 min to hours vs seconds for stamping [R] | src-20261023-8710cc, src-20261023-c3b62f, src-20251009-1f4b2f |
| Capex per factory | n/a | Hadrian: $260M Series C plus a Morgan Stanley factory loan; 270k sq ft Mesa site, 350 jobs [R]. **[E]** At least ~$0.5–1M of capex per job created, assuming most of the raise goes into factories. | src-20250717-cc738d |
| Engineering throughput (approach B) | Manual work instructions take about 10h; complex workflows up to 30h [R] | Arda at Anduril: 15 min and ~2.5h respectively [R] | src-20261020-bbfb1c |

## Derived view [E]
- **Utilization is the main lever.** Machine-shop costs are mostly fixed: depreciation is about 32% of shop costs [R, src-20261023-6ef991]. Raising uptime from about 30–35% to 75–80% roughly halves fixed cost per spindle-hour. At the same price, that could add about 15–25 points of gross margin over a 30–40% job shop. This is the only quantifiable mechanism for a sustained edge.
- **Labor leverage compounds only if part mix repeats.** A 10:1 robot-to-operator ratio pays off on recurring part numbers. One-off prototype work behaves more like Proto Labs (49% factory GM, but slow growth).
- **Capital intensity is the main risk.** Owner-operators carry Proto Labs-style fixed assets without Proto Labs' scale. The failures in failures-and-pivots.md came from capex running ahead of utilization.

## Approach A (owner-operator) vs B (software platform)
| | A: Owner-operator (1872, NOx, Mariana, Hadrian, Machina) | B: Software platform (Arda) |
|---|---|---|
| Revenue unit | Parts or material (per part, per ton) | Usage-based software in others' plants [R] |
| Gross margin ceiling | Proto Labs factory 49% [R] is the realistic top end; likely 25–45% at scale [E] | Software margins, likely 60–80%+ [E], less forward-deployed engineering cost |
| Capex | High: factories, loans [R Hadrian] | Low. The roadmap adds robotic lines, which could pull capex back in [R] |
| Data moat | Owns process data from its own plant (closed loop) | Sees many plants' data but depends on customers' adoption |
| Repeat-order proof | Federal prime awards visible for some (repeat-orders-evidence.md) | Anchor customer (Anduril, all divisions) [R]; no federal prime footprint |
| Key risk | Utilization and capex; pricing pressure from Xometry-style networks (34.7% GM) | Becoming a feature of MES/PLM incumbents; plant owners keep the value |

Gaps: no private producer discloses GM, utilization or capex per cell. Deloitte/MI sources not filed this pass. Huddle questions in huddle-prep.md target these numbers.
