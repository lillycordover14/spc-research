# Repeat-order evidence: federal awards (as of 2026-10-23)

Thesis question 1: do defense, aerospace and industrial buyers place repeat production orders with AI-native producers?

Method: the USAspending API (`spending_by_award`, recipient text search, contracts and grants, FY2008–present), plus DoD daily contract announcements. Every matched award is filed as a source (tags `federal-award`, `repeat-orders`; 191 new records). **A** = owner-operator, **B** = software platform in others' plants. Limits: USAspending shows prime awards only. Subcontracts from primes (most of these companies' commercial and defense revenue), OTAs and loans are mostly missing.

## Production / follow-on ladder (strongest evidence first)
| Company | Approach | Awards found | Total $ | Repeat or follow-on pattern | Key sources |
|---|---|---|---|---|---|
| Firestorm Labs | A | 19 (2023–26) | $53.8M | **Clearest ladder.** SBIR Phase I (2023) → Phase II xCell (2023) → $18.8M xCell (Oct 2025) → SBIR Phase III IDIQ with 6 SOCPAC task orders, Dec 2025–May 2026 ($1.65M–$6.6M each). Also a $30M APFIT award (May 2026; about $26M obligated over 5 task orders) and an AF contract with a $100M ceiling (about $27M obligated). Repeat task orders from the same buyer. | src-20230928-f65042, src-20251022-629fc0, src-20251219-bd5788, src-20260403-8abadd, src-20260717-21bea7 |
| Hadrian | A | 1 prime | $79.4M | Army ACC-Detroit FFP contract for advanced automation manufacturing (Mar 2026): $39.2M obligated, $80M face value, Texarkana TX, one bid. First large Army prime; the rest of its revenue is subcontract work for primes and neo-primes, which this data does not show. | src-20260317-77e798, src-20260317-5585be |
| Saronic (adjacent OEM) | A | 3 | $29.3M | Navy contractor-owned, contractor-operated (COCO) Corsair USV order of $29.0M (Jul 2026), plus a SOCOM training order. | src-20260701-407277 |
| Machina Labs | A | 13 (2020–25) | $12.8M | Air Force is a **repeat buyer over 6 years**: SBIR tooling (2020–21) → $3.0M hydroform replacement (2022) → D2P2 (2024) → $3.37M incremental sheet forming (Feb 2025) → $0.51M maintenance/software install (Apr 2025), suggesting cells deployed at government sites. Also a Bureau of Reclamation part order (2024). Production-scale orders are not yet visible. | src-20220328-cc3980, src-20240627-1df50b, src-20250416-317e81, src-20250416-e1efd3 |
| Re:Build Manufacturing | A | 34 (2022–26) | $4.1M | Many small **repeat part orders**: DLA mounting plates (10+ orders, 2025–26), Navy TR-343 isolation rings (3 orders), Air Force composite training panels (5 orders), plus NSWCCD fabrication ($1.47M, 2025). This is true repeat production, but at job-shop ticket sizes. | src-20250923-08faa9, src-20260105-78ea62, src-20230324-14b99d, src-20231218-be377c |
| Vulcan Elements | A | 7 (2024–26) | $5.7M | AF SBIRs → DLA magnet qualification ($0.89M, 2025) → **Army NdFeB magnet IDIQ** (Jul 2026, $200 minimum order; ceiling not shown). The large DoD loan and Commerce funding are not in this data. | src-20260710-6361ea, src-20250501-1885f8, src-20260710-d40383 |
| Hermeus | A | 5 | $23.2M | $20.2M AF SBIR Phase II (2021) plus 2025 STRATFI/D2P2. R&D, not production. | src-20210730-d59673 |
| Divergent | A | 3 (2025) | $3.6M | Three AF sustainment awards in 2025. Most of its revenue is subcontract work for primes (LMT, RTX, GA). | src-20250924-22c5ee, src-20250924-42fb96 |
| Rangeview | A | 1 | $1.43M | AF digital investment casting (Sep 2025). | src-20250925-cef954 |
| Radical AI | B / materials | 1 | $1.2M | AF AI-driven autonomous materials experimentation (May 2025). R&D. | src-20250523-f41dd1 |
| Senra Systems | A | 1 | $39k | AF wire harness (2024). | src-20240517-21cb76 |
| Sparkz | A | 1 | $0 obligated | DOE BIL battery-grade materials award (2025). | src-20250101-f09f13 |

**No prime awards found:** Mariana Minerals, Arda, 1872, NOx, Atomic, UNION, Helicon, Critical Materials Group, Deterrence, Jeevy, CircuitHub, Heron, AMCA, VulcanForms, Foundation, Antropi, Freeform. They may hold subcontracts, OTAs via consortia, or commercial-only revenue.

## Comparators (job shop / marketplace)
- **Xometry**: 56 small federal orders (2014–26), $2.9M total, mostly NASA and Navy labs, around $5k–30k each. Many repeat buyers, small tickets.
- **Proto Labs**: 48 orders (2008–26), $1.8M total; same pattern.
- **Velo3D**: $4.5M AF Rapid Sustainment Office award (2022) and a NASA lease (2023). Its later recovery was DLA- and defense-led (see failures-and-pivots.md).

## Read for the thesis
1. Firestorm is the only producer with a visible **SBIR → Phase III IDIQ → multiple task orders** ladder. That is the pattern to underwrite.
2. Hadrian's $80M Army contract is the largest single prime award to an AI-native producer. It is new (Mar 2026), so repeat orders are unproven.
3. Machina and Vulcan show repeat government customers, but the work is still mostly R&D and qualification.
4. Repeat-order evidence for most owner-operators sits with primes (subcontracts) and commercial buyers. Expert calls with **prime supply-chain buyers** are needed to test it (see huddle-prep.md).
5. The software-first platform approach (B: Arda) has no federal prime footprint, so its repeat-revenue evidence has to come from plant-owner customers.
