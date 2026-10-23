# Cross-sector map: AI-native production (built 2026-10-23, grokbot)

**Inclusion test (Lilly):** runs its own plants on in-house software and robotics (A), or sells AI that runs production inside plants owned by others (B). Core: fabrication, precision parts/machining, forming/casting/forging, metals, minerals processing/refining. Adjacent sectors only if they pass the same test. Labs that only make R&D data, and pure software (MES/ERP), are excluded.
"In repo" = already has a card or candidate entry; see `producers-comparison.md` (other worker) for depth. This file adds sector coverage and the A/B split.

Columns: Company | URL | Produces | Own plant + in-house stack evidence | Stage / last round | Leads | Customer/order evidence | Source

## A. Owner-operators

### Fabrication, precision parts, machining, forming, forging
| Company | URL | Produces | Own plant + in-house stack | Stage | Leads | Customers | Src |
|---|---|---|---|---|---|---|---|
| Ethereal Machines (NEW) | etherealmachines.com | Multi-axis CNC parts (aero, defense, semi, medical) | Builds own CNC machines (Nimbus), own factory OS Vesper, own Bengaluru plant; 300k sq ft mega-factory planned | Series B $28.5M, Jun 2026 | Avataar (Peak XV existing) | Serves aero/defense/semi/healthcare (unnamed) | src-20260611-f67aff |
| Hadrian, Machina Labs, Freeform, Divergent, Amca, Isembard, Senra, Atomic Industries, 1872, NOx Metals, Jeevy, UNION, Foundation Industries, Forge Automation, Antropi, Radian Forge, Re:Build, SendCutSend, VulcanForms | — | — | in repo | in repo | — | — | see cards |

### Metals and alloys
| Foundation Alloy (NEW, borderline) | foundationalloy.com | Solid-state alloys / powder-derived metal parts | Own 36k sq ft MA plant + NH production cell; in-house software/robotics NOT evidenced | Series A $22M, Jun 2026 | not captured | Japanese distribution partner | src-20260616-fb5e38 |
| Hertha Metals, New Phase Metals, Advanced Metal Research | — | — | in repo | — | — | — | cards |

### Minerals, refining, critical minerals, recycling
| BatX Energies (NEW) | batxenergies.com | Recycled Li/Co/Ni/graphite, CAM next | Own 5kt shredding + 5kt hydromet plants; AI/ML claimed (Preqin profile only) | Series A ~$11M, Jul 2026 | IvyCap | Supplying recovered materials to market | src-20260702-10b647 |
| Redwood Materials (NEW, borderline) | redwoodmaterials.com | Battery materials, storage | Own Nevada plants; in-house AI stack not evidenced | Series E $425M, Jan 2026 (past D) | Google joined | n/a in source | src-20260128-7545d8 |
| Mariana Minerals, Vulcan Elements, Cyclic Materials, Westmag | — | — | in repo | — | — | — | cards |

### Chemicals
| Chemify (in repo as candidate; now sourced) | chemify.io | Molecules on demand for pharma/materials | Own fully automated Chemifarm (Glasgow, Jun 2025), in-house Chemputation AI + robotics; SV site planned | Series B >$50M, Oct 2025 | Wing, Insight (8VC in) | Pharma/biotech/materials partners (unnamed) | src-20251021-d0aa43 |
| Orbital Industries | — | Cooling fluid + modular DC infra | in repo | Series B $50M, May 2026 | Plural | — | card |

### Batteries, magnets, energy hardware
| Noveon Magnetics (NEW, borderline) | noveon.co | Rare-earth magnets | Own TX plant (>2,000 t/yr target); AI stack not evidenced | Series C $215M, 2026 | not captured | n/a | src-20260101-1badc2 |
| Tandem PV (NEW, borderline) | tandempv.com | Perovskite-silicon solar | Own 40 MW automated Fremont line (robots/conveyors); in-house software not evidenced | $50M, Mar 2025 | not captured | HVM target 2028 | src-20260401-c8b296 |
| Heron Power, TAR, Sparkz | — | — | in repo | — | — | — | cards |

### Pharma / biomanufacturing
| Multiply Labs (NEW, borderline A/B) | multiplylabs.com | Robotic GMP cell/gene therapy & biologics manufacturing | Robotic clusters with in-house software; deployed into pharma equipment (closer to B) | Series B $75M, Oct 2026 | not captured | n/a | src-20261001-74df84 |

### Construction, textiles, food
| Reframe Systems (NEW) | reframe.systems | Net-zero homes | Own local robotic microfactories | Series B $40M, Aug 2026 | not captured | n/a | src-20260801-e54188 |
| Unspun (NEW) | unspun.io | Woven apparel | Own 3D-weaving robots; plans 10 US factories | Raising $40M (reported Apr 2026) | n/a | n/a | src-20260406-67dc95 |
| Hippo Harvest (NEW) | hippoharvest.com | Greenhouse greens | Own robotic greenhouses | Series C $30M, 2026 | n/a | n/a | src-20260101-1566af |

### Aerospace, defense, ships, munitions
| Saronic, Firestorm Labs, Firehawk, Castelion, Mach Industries, Hermeus, Critical Materials Group, Helicon, Deterrence | — | — | in repo (Saronic Series D $1.75B Mar 2026) | — | — | — | cards |

### Electronics / PCBs
| CircuitHub, Axal, Tenet Industries, ProvenMetal | — | — | in repo | — | — | — | cards |

## B. Software-first platforms (AI running production in plants owned by others)
Reference: Arda (arda.ai): turns CAD/PLM into a build plan, work instructions and station layout, keeps the line current on design changes, moving toward robot execution [src-20261023-ddfbcb].
| Company | URL | What it does on the floor | Evidence | Stage | Leads | Customers | Src |
|---|---|---|---|---|---|---|---|
| Arda | arda.ai | Design-to-line planning, line reconfiguration, next robotics | Multiple lines at a large US manufacturer; ArsenalOS | Series A $160M @ $1.5B, Oct 2026 | Altimeter, Accel, Khosla | Anduril | src-20261023-ddfbcb, src-20261020-bbfb1c |
| Almetra (ex-Deltia) (NEW) | almetra.ai | Cameras over lines turn video into cycle-time/output data; moving to control layer + robotics | Bosch eBike +19% output, ABB +15% | Series A EUR16.3M, Jun 2026 | blisce/ | Bosch, Siemens Energy, ABB, Aumovio | src-20260625-940831 |
| microagi (NEW, enabler) | microagi.ai | Films workers (cameras, gloves) to train robots for a specific customer factory | 5 companies collecting; 1 deploying on a line | Seed $55M, Jul 2026 | Hummingbird | auto, logistics, food (unnamed) | src-20260716-017398 |
| Bright Machines, Path Robotics, GrayMatter Robotics, Instrumental, Code Metal, Mind Robotics, Standard Bots, Formic, RobCo, Flexciton, Fero Labs, Phaidra, Sight Machine-type peers | — | in repo | — | — | — | — | cards / candidates |

## Adjacent / excluded (fail the test)
| Company | Reason | Src |
|---|---|---|
| KoBold Metals | Exploration AI; Mingomba not yet producing (Series D $280M per Form D, first sale Oct 2025) | src-20260102-562cdf |
| Standard Nuclear | Own HALEU fuel production but no in-house AI/robotics evidence | src-20260128-577ea2 |
| Scimplify | Orchestrates 500+ partner factories (asset-light) | src-20261014-b218c5 |
| Medra ($52M A), Warp Sciences ($215M) | Autonomous wet labs produce data/compounds for R&D, not production plants | src-20260223-adeec6, src-20261022-40bbe0 |
| Isomorphic, Xaira, Generate (IPO Feb 2026), Enveda, Cradle, Galux, Aureka, ChemLex | AI drug discovery; no production plant | src-20260101-b4955c |
| Periodic Labs, Lila, Radical AI, CuspAI, Deep Material, Matter Machine, Apoha | Autonomous materials labs: R&D, not plants (in repo where present) | cards |
| Apollo Atomics, Zeno Power | Factory-built nuclear, pre-production | — |
| Diden Robotics, Maxinsights | Sell robots / training data, not production | — |
| Salience, iPronics, Polaris (photonics) | Fabless | — |

## Gaps
- No-AI-evidence borderline A rows (Redwood, Noveon, Tandem, Foundation Alloy) need a check of in-house software/robotics.
- Lead investors not captured for several rows; medical devices, semiconductor fabs and casting turned up no company that passes the test.
