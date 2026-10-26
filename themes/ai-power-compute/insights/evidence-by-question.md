# Evidence by question

The fastest path from reading to a readout. Every time an agent summarizes a source, it adds one line per claim under the question it answers: `- YYYY-MM-DD | <claim with number> [src-id]`, newest first. The readout is written from this page. Questions are defined in `questions.md`.

## Q1. Which constraint binds, and when

- 2026-10-26 | There is a significant backlog in data center delivery due to supply chain constraints, with about 8-12 months of signed client demand waiting for fulfillment | alphasense, med | src-20261026-71d413
- 2026-10-26 | The industry is experiencing a shift toward flexibility in both delivery and operations, with clients and executives accepting partial or delayed deliveries due to external factors | alphasense, med | src-20261026-71d413
- 2026-10-26 | Speed to power and time to delivery are prioritized over cost savings or regulatory incentives, given the high returns from rapid deployment | alphasense, med | src-20261026-71d413
- 2026-10-26 | Hyperscalers generally prefer in-house workload and power optimization, but any solution that enables flexible power scheduling is considered beneficial | alphasense, med | src-20261026-71d413
- 2026-10-26 | Building strong relationships with vendors and peers, even competitors, is now critical to securing materials and meeting delivery timelines | alphasense, med | src-20261026-71d413
- 2026-10-15 | The expert's company used Crusoe for large-scale, bursty GPU workloads, primarily for custom AI model training, but migrated away due to operational risks tied to Crusoe's power generation strategy | alphasense, med | src-20261015-93d177
- 2026-10-15 | The expert expects continued growth in demand for custom model training and GPU compute, but sees Crusoe's long-term prospects as challenged by financial risks, lack of grid connectivity, and increasing competition in managed inference services | alphasense, med | src-20261015-93d177
- 2026-10-15 | Crusoe's pricing is consistently lower than competitors like CoreWeave, largely due to their unique power generation approach, but this comes with higher operational risk and less robust support | alphasense, med | src-20261015-93d177
- 2026-10-15 | Crusoe's customer base is heavily concentrated among anchor tenants (60-80%), with smaller customers mostly on flexible arrangements; the company is exposed if major tenants like Oracle reduce commitments | alphasense, med | src-20261015-93d177
- 2026-10-15 | A significant outage (likely cooling-related) led to substantial financial loss for the expert's company, with Crusoe unwilling to reimburse due to SLA limitations, highlighting gaps in service agreements for performance degradation | alphasense, med | src-20261015-93d177
- 2026-10-12 | Vendor qualification at hyperscalers involves a multi-stage process: initial sample evaluation, custom engineering, prototype validation, and limited deployment, typically spanning 6-9 months before large-scale orders are considered | alphasense, med | src-20261012-35c496
- 2026-10-12 | The market for advanced cooling solutions is currently led by a handful of specialized players (e.g., Corintis, Fabric8Labs, Mikros), with close one-on-one partnerships between vendors and hyperscalers; broader market entry is expected over the next 5-7 years | alphasense, med | src-20261012-35c496
- 2026-10-12 | The Google backstop arrangement is seen as more favorable to Google than Fluidstack, with Google positioned to take over customer relationships and assets if Fluidstack fails, further increasing Fluidstack's risk profile | alphasense, med | src-20261012-6d174a
- 2026-10-12 | Service quality at Fluidstack has declined in the past six months, with longer support times and less flexibility, coinciding with their strategic shift and new deals with Google and crypto miners | alphasense, med | src-20261012-6d174a
- 2026-10-12 | Microfluidic and micro-channel cooling technologies are rapidly evolving and are being aggressively piloted by hyperscalers due to rising TDP in GPUs and AI accelerators, with traditional direct-to-chip cold plates becoming insufficient | alphasense, med | src-20261012-35c496
- 2026-10-12 | Integrators (e.g., Delta, Supermicro) are brought in after initial validation to support broader deployment, but procurement decisions and vendor selection remain tightly controlled by the hyperscaler | alphasense, med | src-20261012-35c496
- 2026-10-12 | Fluidstack's shift to an 'America first' strategy and relationship with the U.S. government is causing concern among European customers, leading to some moving workloads to alternatives like Nebius and regional providers | alphasense, med | src-20261012-6d174a
- 2026-10-12 | Fluidstack's marketplace solution is valued for cost efficiency but is being deprioritized in favor of longer-term, contracted capacity, which is less attractive to customers who value flexibility | alphasense, med | src-20261012-6d174a
- 2026-10-12 | Fluidstack's business is highly concentrated, with over 90% of revenue tied to Anthropic, and faces significant risk if there are delays in delivering new capacity or if Anthropic exercises contract break clauses | alphasense, med | src-20261012-6d174a
- 2026-10-12 | Corintis is seen as strong in metallurgical R&D and data science, while Fabric8Labs is noted for rapid prototyping and simulation capabilities; both approaches are valued, and performance is prioritized over cost in early-stage evaluations | alphasense, med | src-20261012-35c496
- 2026-10-11 | Retrofitting existing data centers with battery storage and Heron Link is challenging and costly, so adoption is expected primarily in new builds or major upgrades | alphasense, med | src-20261011-0e1259
- 2026-10-11 | Hyperscalers are currently piloting Heron Link, but large-scale adoption is expected only after successful demonstration, likely starting in 2028-2029 | alphasense, med | src-20261011-0e1259
- 2026-10-11 | Heron's approach offers notable advantages in protection coordination, system availability, and modularity, allowing for isolation of faults and higher system uptime compared to traditional solutions | alphasense, med | src-20261011-0e1259
- 2026-10-11 | Heron Power's Heron Link integrates inverter and transformer functions into a single, compact unit, simplifying installation and potentially improving efficiency for data center battery energy storage systems | alphasense, med | src-20261011-0e1259
- 2026-10-11 | Heron Link claims round-trip efficiency improvements, with potential RTE of 98-98.5% compared to 93-94% for incumbent solutions, and 25% lower idle power consumption | alphasense, med | src-20261011-0e1259
- 2026-10-09 | FERC accepted PJM's 50 MW large-load definition and registry but rejected the rest; PJM says it is short of capacity from 2027/28 | filing, high | src-20261009-8ee3c9
- 2026-09-16 | GE Vernova selling turbine slots for 2032 delivery; added 12 GW supply for 2030-31 | filing, med | src-20260916-4be490
- 2026-09-11 | ERCOT paused energization of new large-load data centers during Batch Zero | filing, high | src-20260911-435867
- 2026-08-26 | NVIDIA prices its opportunity per GW: about $18B Hopper, $25B Blackwell, $40B Vera Rubin | filing, high | src-20260826-7aa6b5
- 2026-08-11 | CoreWeave raised prices about 25% across SKUs in July; 1.5 GW active, 4.2 GW contracted, target 8 GW+ by 2030 | filing, high | src-20260811-4fafb8
- 2026-08-07 | Microsoft added about 1 GW in the quarter on $41B capex | earnings call, high | src-20260807-235a16
- 2026-08-05 | Sivaram: one state wants 50 GW online by 2028 but only 25 GW can be built | podcast, med | src-20260805-572c12
- 2026-07-22 | GE Vernova: 116 GW gas under contract, about 20% data centers; at least 125 GW by year end | filing, high | src-20260722-3da614
- 2026-07-19 | Transformer lead times have increased dramatically post-pandemic, with large power transformers now taking over two years, and prices have surged 65%-90% compared to pre-COVID levels | alphasense, med | src-20260719-ffdc30
- 2026-07-19 | The primary bottleneck for data center buildouts is access to power generation, followed by skilled labor, with transformers being a significant but not the sole constraint | alphasense, med | src-20260719-ffdc30
- 2026-07-19 | The expert predicts a major industry shift toward 800 VDC data center architecture and solid state transformers, with Tier 1 OEMs already prepared for this transition, and expects this to become standard by 2028 | alphasense, med | src-20260719-ffdc30
- 2026-07-19 | Giga's value proposition is speed and customization, offering vertically integrated manufacturing and tailored solutions, but lacks the brand reputation of Tier 1 OEMs | alphasense, med | src-20260719-ffdc30
- 2026-07-19 | Giga is used primarily for medium voltage transformers and switchboards, chosen for faster lead times (15-30 weeks) compared to competitors, but at a premium price | alphasense, med | src-20260719-ffdc30
- 2026-06-30 | LBNL: 2,061 GW active in queues, 61-month median, only 19% of projects completed (large loads excluded) | research, high | src-20260630-eb8b9f
- 2026-05-01 | Baseten CEO: about 1,024 B200s now needs a three to five year contract with 20-30% TCV prepay | podcast, med | src-20260501-1f0aeb
- 2026-03-31 | Secondhand S&P figure: about 25 GW of 50 GW not connectable in three years | article, high | src-20260331-dc28c2
- 2026-02-12 | Solid oxide fuel cells (Bloom Energy) are valued for short lead times (as little as 60 days) and modular deployment, but have higher CapEx and fixed output limitations, making them suitable for up to 15%-20% of a data center's power mix | alphasense, med | src-20260212-faabb1
- 2026-02-12 | Midsize microturbines (from suppliers like Siemens, GE Vernova) are cost-effective and flexible but have longer lead times (16-24 months) and are often used in multiples for large facilities | alphasense, med | src-20260212-faabb1
- 2026-02-12 | Microgrid solutions combining multiple technologies (microturbines, fuel cells, renewables, battery storage) are preferred for their modularity, cost predictability, and reliability | alphasense, med | src-20260212-faabb1
- 2026-02-12 | Levelized cost of electricity (LCOE) varies: Bloom Energy SOFCs are around 9-10¢/kWh, microturbines 7-8¢/kWh, and solar (with storage and land costs) 11-13¢/kWh; utility grid power remains the cheapest but is less reliable | alphasense, med | src-20260212-faabb1
- 2026-02-12 | Energy-as-a-service models are becoming more popular, reducing operational burden and CapEx lock-in for customers, and allowing for more predictable power procurement | alphasense, med | src-20260212-faabb1
- 2026-01-14 | Emerald CEO: US wants 50 GW of AI in three years but can plug in 25 GW | podcast, med | src-20260114-9f862d

## Q2. Data center interconnection

- 2026-10-19 | Solid-state transformers (SSTs) promise significant efficiency gains (from ~85% to 98-99%), with upstarts like Heron Power and Enphase seen as leading innovators, while incumbents are slower to adapt due to existing profitable business lines | alphasense, med | src-20261019-dd9f69
- 2026-10-19 | Private HVDC transmission lines face significant regulatory, easement, and business challenges, and are generally less attractive than co-location or grid-based solutions for data centers | alphasense, med | src-20261019-dd9f69
- 2026-10-19 | Grid power is generally cheaper ($70-$90/MWh) and more reliable than behind-the-meter gas ($110-$130/MWh), and is preferred by hyperscalers for reliability and carbon accounting, though behind-the-meter gas is used in specific constrained scenarios | alphasense, med | src-20261019-dd9f69
- 2026-10-19 | Co-location of data centers with generation assets is typically more efficient and cost-effective, with land and labor constraints rarely justifying long transmission builds | alphasense, med | src-20261019-dd9f69
- 2026-10-19 | Capacity pricing for private transmission solutions (e.g., $21/kW-month) is above current market rates ($15-$18/kW-month), making them less competitive compared to grid or traditional capacity markets | alphasense, med | src-20261019-dd9f69
- 2026-09-28 | VoltaGrid's main advantage is speed of deployment and existing track record, but their solution is not cost-competitive for long-term use; differentiation among providers is mainly based on experience, relationships, and proximity to sites | alphasense, med | src-20260928-37c103
- 2026-09-28 | VoltaGrid was used as a temporary bridge power solution at a large data center site due to delays in permanent power infrastructure, with modules that were quick to deploy and effective for short-term needs | alphasense, med | src-20260928-37c103
- 2026-09-28 | Turbines, while previously favored for BTM prime power, have become less attractive due to increased lead times and costs; reciprocating engines and fuel cells are now preferred for new deployments | alphasense, med | src-20260928-37c103
- 2026-09-28 | The selection of bridge power providers is opportunistic and driven by lead times, pricing, and proven ability to execute, with cost sensitivity lower than expected due to contractual structures with OEMs | alphasense, med | src-20260928-37c103
- 2026-09-28 | All BTM power solutions for data centers, including turbines, recips, and fuel cells, require on-site battery energy storage systems (BESS) to handle rapid load swings from AI workloads | alphasense, med | src-20260928-37c103
- 2026-09-24 | CAISO draft final proposal sets non-firm speed-to-power path; curtailment rules deferred | filing, med | src-20260924-fbbe33
- 2026-09-20 | GridCARE models about 5% rate reduction per GW of added flexible load (company model) | podcast, med | src-20260920-7822a2
- 2026-08-26 | PJM's independent market monitor called data center flexibility a 'regulatory fiction' (host, Volts) | podcast, high | src-20260826-03722b
- 2026-08-14 | Vistra: ERCOT queue of over 400 GW is realistically 12-15 GW by 2030 | filing, high | src-20260814-3047e8
- 2026-08-03 | U.S. utilities operate on a regulated asset base model, historically designed for slow, predictable growth, but are now facing rapid, unpredictable demand from data centers and electrification trends | alphasense, med | src-20260803-e9026c
- 2026-08-03 | There is no uniform national policy yet; states are taking varied approaches, with some welcoming data centers and others imposing moratoriums or requiring 'bring your own generation' (BYOG) solutions | alphasense, med | src-20260803-e9026c
- 2026-08-03 | The expert expects most new data center power to come from natural gas over the next 5-10 years, with short-term price spikes likely due to global events, and sees the biggest beneficiaries as integrators who can deliver turnkey power solutions (combining turbines, batteries, and controls) to data centers | alphasense, med | src-20260803-e9026c
- 2026-08-03 | Data centers are driving up grid costs, which can lead to higher utility bills for all consumers; this is influencing both federal and state policy discussions | alphasense, med | src-20260803-e9026c
- 2026-08-03 | BYOG (behind-the-meter generation) is about six times more expensive than grid power, but is being pursued for speed and reliability, especially by large tech companies; however, supply chain and technical challenges are significant | alphasense, med | src-20260803-e9026c
- 2026-06-18 | ERCOT PCLR and WLPUN pathways give large loads a formal flexible-connection route; commitment deadline June 2027 | filing, high | src-20260618-d60be4
- 2026-06-04 | There is a risk to ratepayers if utilities do not efficiently manage growth and infrastructure buildout, but this is a broader utility issue and not solely attributable to data centers or AI demand | alphasense, med | src-20260604-1f85ef
- 2026-06-04 | Power access for large data centers is not as constrained as media suggests for major hyperscalers, due to advanced planning, partnerships, and internal tools, but interconnection and permitting remain key bottlenecks | alphasense, med | src-20260604-1f85ef
- 2026-06-04 | Most hyperscalers rely on third-party developers to secure shovel-ready sites with guaranteed interconnection and power, rather than developing sites directly | alphasense, med | src-20260604-1f85ef
- 2026-06-04 | Interconnection delays and capacity constraints are distinct issues; interconnection can be improved with process modernization, while capacity buildout requires long-term infrastructure investment | alphasense, med | src-20260604-1f85ef
- 2026-06-04 | GridCARE's value proposition is strongest for vertically integrated utilities and developers lacking modern planning tools, rather than for hyperscalers with sophisticated internal capabilities | alphasense, med | src-20260604-1f85ef
- 2026-06-03 | There is a trend toward data centers potentially acting as power traders themselves, capitalizing on price spreads if they secure capacity at lower rates than prevailing market prices | alphasense, med | src-20260603-7dc891
- 2026-06-03 | The expert expects that data centers will pay for solutions like GridCARE if these tools help reduce power costs, improve operational efficiency, and provide actionable insights for negotiating power contracts | alphasense, med | src-20260603-7dc891
- 2026-06-03 | Hyperscalers are currently locking in long-term power contracts at premium prices to secure capacity, anticipating that grid constraints and rising demand will continue to drive prices higher | alphasense, med | src-20260603-7dc891
- 2026-06-03 | GridCARE is an analytics platform leveraging machine learning and AI to forecast grid capacity, enabling utilities to optimize trading, planning, and dispatch decisions, and to price capacity more effectively in spot markets | alphasense, med | src-20260603-7dc891
- 2026-06-03 | Data centers, especially hyperscalers, are experiencing increasingly volatile power consumption due to AI workloads, making traditional fixed-price power purchase agreements less optimal and driving interest in more dynamic, market-based procurement strategies | alphasense, med | src-20260603-7dc891
- 2026-05-28 | The expert's organization is piloting GridCARE, with the solution being evaluated for its ability to unlock grid capacity, reduce time to power, and manage ongoing operations as data center complexity increases | alphasense, med | src-20260528-aa6bad
- 2026-05-28 | The expert notes that the grid management challenge is primarily a software problem, but the increasing diversity of power sources and dynamic loads means hardware considerations are also important | alphasense, med | src-20260528-aa6bad
- 2026-05-28 | The decision to adopt solutions like GridCARE is made centrally to ensure scalability and consistency across global data center sites, with ongoing evaluation based on differentiation, scalability, and regional adaptability | alphasense, med | src-20260528-aa6bad
- 2026-05-28 | GridCARE is positioned at the systems level, managing the interplay between the grid and data center assets, rather than at the chip or hardware level, which is where companies like Emerald and Phaidra focus | alphasense, med | src-20260528-aa6bad
- 2026-05-28 | GridCARE and similar companies provide software platforms that optimize grid resiliency and power delivery for hyperscale data centers, managing dynamic loads and integrating multiple power sources, including behind-the-meter assets | alphasense, med | src-20260528-aa6bad
- 2026-05-14 | Power test: 80 MW with PGE in 2026 is the one utility-accepted number; 2 GW is pipeline, not energized | article, high | src-20260514-d7ee00
- 2026-03-26 | Typical data center interconnection still supplies 100% of peak power; flexible connection is the exception (Atkinson, Volts) | podcast, med | src-20260326-771e89
- 2026-01-14 | FERC accepted SPP's HILL study process for high-impact large loads | filing, high | src-20260114-d01d47
- 2025-12-18 | FERC created a Non-Firm Contract Demand service for PJM co-location | filing, high | src-20251218-ac2bd0
- 2025-10-29 | The company employs a multipronged approach to energy sourcing, including direct and indirect power purchase agreements, on-site generation, and microgrids, to ensure reliability and price stability | alphasense, med | src-20251029-76215a
- 2025-10-29 | Sustainability is a core goal, with commitments to be carbon negative and water positive by 2030, driving the adoption of renewable energy sources, water recycling, and innovative cooling methods | alphasense, med | src-20251029-76215a
- 2025-10-29 | Nuclear energy is being explored as a future power source, but regulatory and supply chain challenges remain; partnerships and investments are ongoing, but adoption is still in early stages | alphasense, med | src-20251029-76215a
- 2025-10-29 | Energy availability is the primary constraint for data center expansion, with grid connectivity often taking 8-9 months and significant investments in on-site generation (solar, wind, hydrogen, geothermal, microgrids, and battery storage) to bridge gaps | alphasense, med | src-20251029-76215a
- 2025-10-29 | Crusoe, a former crypto mining company, has successfully pivoted to AI data centers by leveraging stranded natural gas and vertical integration, making them an attractive partner for hyperscalers due to their speed and direct power access | alphasense, med | src-20251029-76215a
- 2025-05-08 | Norris: ERCOT interconnects generation faster than PJM; ERCOT's controllable load resource program is the precedent | podcast, high | src-20250508-1afa13

## Q3. Flexible load

- 2026-10-26 | There is a strong advantage for third-party vendors like Emerald to serve as intermediaries between utilities and data centers, providing standardized solutions that utilities can more easily integrate than bespoke hyperscaler solutions | alphasense, med | src-20261026-7c85c9
- 2026-10-26 | The market for grid and energy optimization in data centers is extremely large (hundreds of billions of dollars in inefficiencies), but Emerald's current niche is much smaller; long-term growth depends on expanding their solution set and adapting to evolving industry needs | alphasense, med | src-20261026-7c85c9
- 2026-10-26 | Speed to power (time to grid connection) is currently the most valuable factor for data centers, often outweighing cost considerations | alphasense, med | src-20261026-7c85c9
- 2026-10-26 | Partnerships with major hardware vendors (e.g., NVIDIA's Vera Rubin DSX reference design) could provide Emerald with a distribution advantage, but widespread deployment is constrained by engineering and retrofitting challenges | alphasense, med | src-20261026-7c85c9
- 2026-10-26 | Emerald's value proposition lies in enabling flexible power loads and faster grid connections, which is especially relevant in markets with long interconnection queues (e.g., Northern Virginia, ERCOT, Ireland) | alphasense, med | src-20261026-7c85c9
- 2026-10-21 | Emerald AI ran a DSX Flex pilot at Nscale's AI factory in Iceland on utility demand signals | X post, med | src-20261021-92e29b
- 2026-10-20 | GridCARE says it qualified 5 GW with six utilities in 12 months; index claims up to 120 GW unlockable (company claim) | article, med | src-20261020-4957d3
- 2026-10-15 | The market for load flexibility solutions is expected to grow rapidly as grid bottlenecks worsen, but this will also drive more operators to develop their own software rather than rely on third parties | alphasense, med | src-20261015-1b72b8
- 2026-10-15 | Spatial flexibility (moving workloads between regions) is technically feasible but complex and costly; most AI labs will likely accept some curtailment rather than rely on this approach | alphasense, med | src-20261015-1b72b8
- 2026-10-15 | Partnerships with chip providers (e.g., NVIDIA) could provide a distribution advantage for third-party solutions if embedded at the hardware level, but the long-term customer base may shift to smaller operators and AI labs if hyperscalers build in-house | alphasense, med | src-20261015-1b72b8
- 2026-10-15 | Inference workloads have less flexibility for curtailment than training, but some flexibility is still possible, especially for AI labs willing to accept lower availability in exchange for lower costs | alphasense, med | src-20261015-1b72b8
- 2026-10-15 | Data sensitivity and the need for access to GPU and workload data are major barriers to adopting third-party solutions like Emerald, making in-house solutions more attractive for large operators | alphasense, med | src-20261015-1b72b8
- 2026-10-14 | Two main use cases are being tested: curtailing data center power usage during grid events (e.g., lightning) and shifting AI training workloads to optimize grid capacity | alphasense, med | src-20261014-9f536d
- 2026-10-14 | The vendor selection process took eight months, with Emerald AI chosen over larger incumbents (e.g., Schneider Electric, Siemens, ABB) due to its unique focus on bridging utilities and data centers, though concerns remain about cybersecurity, latency, and integration with legacy systems | alphasense, med | src-20261014-9f536d
- 2026-10-14 | The utility is piloting Emerald AI's Conductor software to optimize electricity distribution between the grid and data centers, focusing on demand response during grid stress events and off-peak utilization | alphasense, med | src-20261014-9f536d
- 2026-10-14 | The utility is considering phased expansion from 100,000 to potentially 8 million customers, but full deployment depends on resolving latency, scalability, and data ownership issues; partnerships like NVIDIA are seen as potentially beneficial for performance, reliability, and sustainability goals | alphasense, med | src-20261014-9f536d
- 2026-10-14 | The primary value for data center operators, especially hyperscalers and neoclouds, is earlier energization and GPU revenue, not just energy cost savings | alphasense, med | src-20261014-d1112c
- 2026-10-14 | The NVIDIA partnership (integration with DSX Flex and Vera Rubin AI Factory) gives Emerald a strong go-to-market advantage, but the open architecture means this may not be a permanent moat; long-term defensibility depends on deep, recurring integration and becoming critical infrastructure | alphasense, med | src-20261014-d1112c
- 2026-10-14 | Strict SLAs currently limit the adoption of flexible compute, but the expert expects a bifurcation in the market, with more flexible SLAs emerging for training workloads over the next 3-5 years | alphasense, med | src-20261014-d1112c
- 2026-10-14 | Latency, especially in spatial flexibility (moving workloads between data centers), remains a key challenge, with even millisecond delays impacting critical utility applications and field operations | alphasense, med | src-20261014-9f536d
- 2026-10-14 | Emerald's spatial flexibility, moving workloads between regions, adds value for operators with geographically distributed AI clusters, but is limited by data locality, GPU availability, and integration complexity | alphasense, med | src-20261014-d1112c
- 2026-10-14 | Emerald differentiates itself by orchestrating AI workloads as flexible grid resources, enabling data centers to offer demand flexibility and potentially accelerate grid interconnection timelines | alphasense, med | src-20261014-d1112c
- 2026-10-02 | SCE study with GridCARE found potential 20 MW of flexible capacity on a constrained circuit | article, med | src-20261002-e720dd
- 2026-09-20 | GridCARE: PGE 400 MW for five data centers on flexible interconnection agreements; peak risk 40 to 70 hours a year | podcast, med | src-20260920-7822a2
- 2026-09-16 | The pilot with Emerald involved controlling a data center's compute load in response to real-time grid events, successfully demonstrating rapid and reliable response to grid operator instructions over several days | alphasense, med | src-20260916-064af8
- 2026-09-16 | The expert emphasized that utilities are primarily driven by regulatory incentives and are less likely to pay for solutions like Emerald unless incentivized by regulation; data centers are the clearer initial customers | alphasense, med | src-20260916-064af8
- 2026-09-16 | The competitive landscape is nascent, with potential for consolidation and a need for solutions that manage both compute load and behind-the-meter power, especially as backup power requirements evolve | alphasense, med | src-20260916-064af8
- 2026-09-16 | Success metrics focused on speed and accuracy of response to grid events, with Emerald's technology meeting requirements across multiple scenarios, including unique U.K.-specific demand spikes | alphasense, med | src-20260916-064af8
- 2026-09-16 | Future plans include scaling up to a megawatt-level pilot, with ongoing discussions about commercial deployment and the need to develop new contract structures between data centers and grid operators | alphasense, med | src-20260916-064af8
- 2026-09-09 | Willingness to pay for SaaS solutions that offer a unified view of electrical, cooling, and front-of-meter assets, especially if they can scale enterprise-wide | alphasense, med | src-20260909-19a68e
- 2026-09-09 | There is active internal development of grid signal and instrumentation solutions, but the expert sees value in third-party platforms that can provide enterprise-level visibility and alerting | alphasense, med | src-20260909-19a68e
- 2026-09-09 | The expert is highly skeptical of claims that software solutions can accelerate utility interconnect timelines, citing the physical and regulatory constraints of power infrastructure | alphasense, med | src-20260909-19a68e
- 2026-09-09 | Industry-wide, there is a shift toward microgrids and behind-the-meter power generation due to grid unreliability, with increasing adoption of battery energy storage and anticipation of 800 VDC architectures | alphasense, med | src-20260909-19a68e
- 2026-09-09 | Current industry focus is on optimizing power usage and maintaining stable operations in degraded power environments, with a strong need for real-time telemetry and digital twin capabilities to monitor grid conditions | alphasense, med | src-20260909-19a68e
- 2026-08-31 | Utilities prefer capitalizable agreements over subscription models due to regulatory incentives, but cloud-based solutions make capitalizability more complex | alphasense, med | src-20260831-5ca620
- 2026-08-31 | Sales cycles for utilities are long, often taking several years for enterprise agreements and still lengthy for pilots, with internal champions and seniority being critical for success | alphasense, med | src-20260831-5ca620
- 2026-08-31 | References from other utilities and relationships are more influential than price in competitive RFP processes, and large utility families (e.g., Exelon, AEP) can serve as effective sales channels | alphasense, med | src-20260831-5ca620
- 2026-08-31 | Pilot contracts with utilities are typically small (hundreds of thousands of dollars), milestone-based, and have a low conversion rate (10-20%) to larger enterprise deals | alphasense, med | src-20260831-5ca620
- 2026-08-31 | For data center-related grid software, data centers often pay for the software while utilities act as users, with ongoing operational modules providing the most lucrative revenue opportunities | alphasense, med | src-20260831-5ca620
- 2026-08-26 | Emerald pitches 75 MW instead of 50 MW from the same grid tap; deployed at multi-megawatt scale at a whole data center; 96 MW Vera Rubin site with NVIDIA and Digital Realty later this year | podcast, high | src-20260826-03722b
- 2026-08-26 | Sivaram: optimizing power cost is not top of mind for data centers; speed to connect is the value | podcast, high | src-20260826-03722b
- 2026-08-25 | Up to 100 GW headroom is a company claim, not yet tied to a study in our sources | article, high | src-20260825-62437e
- 2026-08-25 | First utility tariff-style program trading grid access for flexibility (Silicon Valley Power) answers part of the flexible-load question | article, high | src-20260825-62437e
- 2026-05-14 | Grid utilization ~30% (Stanford, cited) frames latent capacity thesis | article, high | src-20260514-d7ee00
- 2026-03-26 | Camus, Princeton ZERO Lab and encoord modeling: flexibility needed at most about 4% of hours, unlock on the order of 30% | podcast, med | src-20260326-771e89
- 2026-03-19 | Emerald says a grid test cut an AI cluster 35% in 30 seconds; working with National Grid in the UK | podcast, med | src-20260319-960dc9
- 2026-03-02 | EPRI DCFlex: up to 40% reduction with sub-minute response; about 100 MW Aurora project | research, high | src-20260302-a34f1a
- 2026-01-14 | Emerald CEO: grid hits peak congestion under 1% of the time; Oracle Phoenix GPUs cut 25% | podcast, med | src-20260114-9f862d
- 2025-02-01 | Duke: 76 GW headroom at 0.25% curtailment, 98 GW at 0.5%, 126 GW at 1.0%; average event 1.7 to 2.5 hours; 88% of curtailment hours retain at least half of load | market-research, high | src-20250201-ccc248

## Q4. Enterprise view of the bottleneck

- 2026-09-09 | Snowflake AI Data Cloud supports over 41% of the Global 2000 (enterprise AI where data sits) | filing, med | src-20260909-61633d

## Q5. Inference demand

- 2026-10-26 | Fireworks site: 10,000+ companies; distributed via Azure Foundry (UiPath) | website, med | src-20261026-505f9f
- 2026-10-26 | Baseten site: Speechify cut costs 44% (customer claim on vendor site) | website, med | src-20261026-4d6360
- 2026-10-16 | Sail CEO predicts async could be 95% or more of inference demand (founder view) | podcast, med | src-20261016-e74533
- 2026-08-13 | Datadog: inference is becoming the bigger part of AI workloads | earnings call, med | src-20260813-44037d
- 2026-07-22 | Alphabet: model APIs at about 22B tokens per minute, up from 16B a quarter earlier; still supply constrained | filing, high | src-20260722-d9fefd
- 2026-05-01 | Host: Baseten expects more than $1B revenue this year after 30x scale; CEO cites about 400% NDR and no top-30 churn | podcast, med | src-20260501-1f0aeb
- 2026-04-29 | Alphabet processes 16B tokens per minute; TPU 8i 80% better performance per dollar | earnings call, high | src-20260429-ed9e1e

## Q6. Where inference value accrues

- 2026-10-21 | Meta wants to serve as much high margin inference demand as possible (world 3) | earnings call, med | src-20261021-99ff3b
- 2026-10-20 | Switching between providers is technically straightforward, and the company is open to adding more providers if they meet requirements and improve performance | alphasense, med | src-20261020-b4cff8
- 2026-10-20 | Providers are used in parallel, with a custom gateway routing requests based on real-time performance metrics to optimize latency and throughput | alphasense, med | src-20261020-b4cff8
- 2026-10-20 | Inference providers are used primarily for text model use cases such as user input preprocessing and content moderation, while voice models are run in-house | alphasense, med | src-20261020-b4cff8
- 2026-10-20 | Fireworks AI and Baseten were chosen as primary providers due to their feature completeness, model availability, and reliability; DeepInfra and Together AI were considered but lacked some features and had higher latency | alphasense, med | src-20261020-b4cff8
- 2026-10-20 | Evaluation of inference providers is based on a comprehensive checklist, with security/compliance, uptime, and latency as the most critical factors | alphasense, med | src-20261020-b4cff8
- 2026-10-19 | The expert sees inference as a more general and widely needed capability for enterprises compared to advanced post-training or reinforcement learning, which are niche and require significant data and expertise | alphasense, med | src-20261019-494f8d
- 2026-10-19 | The expert believes that while inference platforms can add features like post-training and sandboxing, their core value remains in optimized inference, and broader platform expansion depends on customer demand and implementation quality | alphasense, med | src-20261019-494f8d
- 2026-10-19 | Migrating from one inference provider to another (e.g., Baseten to Fireworks) would be relatively straightforward, mostly requiring minor code changes if interfaces are similar | alphasense, med | src-20261019-494f8d
- 2026-10-19 | Integration with providers like Baseten is primarily through API endpoints, with additional engineering for handling bursty traffic, retries, and resilience | alphasense, med | src-20261019-494f8d
- 2026-10-19 | Baseten is mainly used for production inference workloads, with internal post-training and experimentation typically handled at smaller scale and with less optimization | alphasense, med | src-20261019-494f8d
- 2026-09-11 | Oracle reports a 20% renewal premium on compute | earnings call, med | src-20260911-a92c4e
- 2026-09-09 | The evaluation process prioritized inference latency, throughput, reliability, model availability, ease of use, and overall price-performance, with Together AI ranking second due to its broad model coverage and competitive performance | alphasense, med | src-20260909-ebd6d1
- 2026-09-09 | The company would only consider switching vendors if inference costs increased by 30% or more, and would first seek to optimize workloads or models before making such a move; AI is now embedded in business processes and unlikely to be abandoned even with significant cost increases | alphasense, med | src-20260909-ebd6d1
- 2026-09-09 | The company began evaluating AI inference platforms in late 2024, selecting Fireworks AI for production workloads in mid-2025 due to strong performance and price-performance ratio, and later adopted Baseten for more flexible, custom deployment needs | alphasense, med | src-20260909-ebd6d1
- 2026-09-09 | ROI is measured through business outcomes such as increased customer engagement, higher self-service resolution rates, reduced support costs, and improved employee productivity, rather than just token-level costs | alphasense, med | src-20260909-ebd6d1
- 2026-09-09 | Fireworks AI is used for both customer-facing (70%) and internal (30%) applications, including enterprise AI assistants, RAG applications, knowledge search, content generation, and agentic AI workloads, primarily serving millions of consumer subscribers | alphasense, med | src-20260909-ebd6d1
- 2026-09-04 | Evidence for world 5, software across heterogeneous hardware | article, med | src-20260904-a08d96
- 2026-08-26 | NVIDIA folds Groq LPU into Vera Rubin but says most data centers will be Vera Rubin plus NVLink 72 only (world 1) | filing, high | src-20260826-7aa6b5
- 2026-08-19 | Nebius Token Factory sells open-model inference (world 4) | earnings call, med | src-20260819-1d8a42
- 2026-08-11 | CoreWeave managed inference booked ARR grew from $1M to over $100M; target $250M+ exiting 2026 (neoclouds move up the stack) | filing, high | src-20260811-4fafb8
- 2026-08-07 | Microsoft MAI models pitched on cost-efficient inference: hyperscaler capturing serving (world 2) | earnings call, med | src-20260807-235a16
- 2026-08-07 | Amazon positions Bedrock as the inference service; capex about $220B (world 2) | earnings call, med | src-20260807-cce06a
- 2026-08-03 | Baseten engineers: NVIDIA Dynamo is a toolkit, not an out-of-box speedup; integration still differentiates (world 4) | podcast, high | src-20260803-db2641
- 2026-06-22 | Strongest evidence for world 4 so far | article, high | src-20260622-4e261f
- 2026-01-23 | NVIDIA invests in the neutral inference cloud, supporting world 4 | article, high | src-20260123-cfd280

## Q7. Disaggregated inference and KV cache

- 2026-10-20 | Google llm-d 1.0: prefix-aware routing cut median TTFT over 85% and lifted throughput 2.4x; Gemini prefix hit rate 35% to 70% | article, high | src-20261020-7e4d10
- 2026-08-19 | Their core innovation is in orchestrating different portions of LLM workloads (e.g., parent and draft models, prefill and decode stages) on the most suitable hardware, improving throughput and reducing latency and cost | alphasense, med | src-20260819-e49885
- 2026-08-19 | The industry is rapidly evolving, with new algorithmic advances (e.g., Mixture of Experts, speculative decoding) driving changes in hardware architectures and deployment strategies | alphasense, med | src-20260819-e49885
- 2026-08-19 | Gimlet Labs' approach is seen as ahead of the curve, addressing current industry challenges in AI inference efficiency and scalability | alphasense, med | src-20260819-e49885
- 2026-08-19 | Gimlet Labs is positioning itself as a differentiated AI inference provider by enabling disaggregated deployment of large language models (LLMs) across heterogeneous hardware, such as GPUs and specialized AI accelerators | alphasense, med | src-20260819-e49885
- 2026-08-19 | Competitors like Fireworks, Together, and Baseten primarily focus on simplifying GPU-based deployments and have not publicly announced similar heterogeneous orchestration capabilities | alphasense, med | src-20260819-e49885
- 2026-08-03 | Baseten: disaggregation adds roughly 2x on top of NVFP4 and speculators (each roughly 2x); 4-6x over baseline is typical, 10x aggressive | podcast, high | src-20260803-db2641
- 2026-01-22 | Nearly all inference services use vLLM under the hood per a16z; open source sets the floor for serving software | article, med | src-20260122-e767e7

## Q8. Heterogeneous hardware

- 2026-10-16 | Sail prices workloads across NVIDIA, AMD, Intel, TPU and Trainium: no bad chips, only bad prices | podcast, med | src-20261016-e74533
- 2026-10-13 | Gimlet adds Cerebras to Gimlet Cloud, plans 100 MW of Cerebras capacity, targets 3,000 tok/s | article, med | src-20261013-6f3a28
- 2026-09-14 | Open-source tools such as Triton (compiler), vLLM, and SGLang (schedulers) are commonly used for benchmarking and are preferred due to their flexibility and community support | alphasense, med | src-20260914-28316c
- 2026-09-14 | Kernel compilation for heterogeneous hardware is less optimized than vendor-specific compilers, resulting in performance trade-offs, but can offer significant cost savings | alphasense, med | src-20260914-28316c
- 2026-09-14 | Current AI workloads are typically locked into single-vendor hardware/software stacks, making heterogeneous hardware orchestration difficult and costly | alphasense, med | src-20260914-28316c
- 2026-09-14 | Companies like Gimlet Labs and Modular are developing solutions to enable distributed AI workloads across mixed hardware, but their tools are not yet standard or widely used | alphasense, med | src-20260914-28316c
- 2026-09-14 | Adoption of commercial orchestration/compilation tools will depend on their ability to demonstrate superior cost-performance (e.g., tokens per dollar) and gain traction among large AI model users | alphasense, med | src-20260914-28316c
- 2026-09-09 | Broadcom: Anthropic 5 GW of TPU 8i in 2027; OpenAI over 5 GW of XPU in 2028 | earnings call, high | src-20260909-fd7170
- 2026-09-04 | Speedup claim lacks named baseline, hardware and model, so efficiency test stays unverified | article, med | src-20260904-a08d96
- 2026-08-25 | Sail: completion windows alone give 2-3x cost per token; chip choice adds the rest toward 10x (company claim) | podcast, med | src-20260825-e500eb
- 2026-08-11 | AMD claims 30% more tokens per dollar; Anthropic up to 2 GW of MI450 | earnings call, med | src-20260811-1061b1
- 2026-08-09 | There is a trend toward using specialized hardware for different phases of model inference (e.g., prefill on high-compute GPUs, decode on memory-rich or older GPUs), and Gimlet's orchestration aims to automate this process | alphasense, med | src-20260809-79a0d9
- 2026-08-09 | The approach involves splitting workloads into smaller chunks and dynamically assigning them to idle hardware, potentially using AI to predict and optimize resource allocation | alphasense, med | src-20260809-79a0d9
- 2026-08-09 | Maximizing utilization and performance in heterogeneous environments requires sophisticated software capable of understanding both the workload and the hardware capabilities, especially when supporting custom models | alphasense, med | src-20260809-79a0d9
- 2026-08-09 | Gimlet's core value proposition is increasing hardware utilization in data centers by orchestrating workloads to reduce idle hardware, which can lead to substantial efficiency gains | alphasense, med | src-20260809-79a0d9
- 2026-08-07 | The value of disaggregating inference workloads (e.g., splitting prefill and decode across different chips) is significant for customers if it leads to substantial cost savings, but the differentiation must be meaningful (e.g., 50%+ savings) to drive adoption | alphasense, med | src-20260807-b6b235
- 2026-08-07 | The expert expects only four to five major chip companies to become credible players in the market, with many others likely to be acquired for IP or fail to scale, making the orchestration opportunity dependent on the success and proliferation of these new entrants | alphasense, med | src-20260807-b6b235
- 2026-08-07 | NVIDIA's strategy is to control as much of the AI stack as possible, acquiring or partnering with companies to fill gaps, which could make it difficult for independent orchestration platforms to differentiate unless they partner with emerging hardware players | alphasense, med | src-20260807-b6b235
- 2026-08-07 | Gimlet's approach as a software orchestration layer for heterogeneous AI hardware is interesting, but faces tough competition from established players, especially as companies like NVIDIA expand their stack with initiatives like Vera Rubin | alphasense, med | src-20260807-b6b235
- 2026-08-07 | Convincing customers to switch from incumbents like NVIDIA is extremely difficult, even with superior technology, due to entrenched relationships and risk aversion | alphasense, med | src-20260807-b6b235
- 2026-07-23 | Gimlet CEO: about 4-5x capacity for the same cost, goal of 10x (company claim) | podcast, med | src-20260723-741ec4
- 2026-07-22 | Alphabet delivered first TPU system sales into customer data centers; vLLM and SGLang supported on TPUs | filing, high | src-20260722-d9fefd
- 2026-03-23 | 3-10x claim is on >1T param models, same power envelope; baseline unstated | article, med | src-20260323-a0cbfc
- 2025-12-02 | Gimlet CEO: kernel gains vs best-in-class are single digits to 20-30%; most gain must come from placement | podcast, med | src-20251202-9b5fb9

## Q9. Fine-tuning as a real budget line

- 2026-10-25 | Baseten Loops SDK post-trains Muse Spark Open and deploys checkpoints straight to inference | X post, med | src-20261025-548e28
- 2026-10-23 | Baseten Environment Network: RL environment partners plus Baseten training and deployment | X post, med | src-20261023-8cc4a2
- 2026-10-21 | The RL stack involves iterative tweaking of model weights to align outputs with expected results, requiring fast, continuous feedback loops and specialized APIs from providers like Fireworks | alphasense, med | src-20261021-5156de
- 2026-10-21 | Maintaining control over models allows companies to avoid costly migrations and maintain consistent performance as upstream models are deprecated or updated | alphasense, med | src-20261021-5156de
- 2026-10-21 | Enterprises and application companies use post-training and RL to optimize models for reliability, lower latency, and reduced hallucination, rather than solely for intelligence improvements | alphasense, med | src-20261021-5156de
- 2026-10-21 | Cost optimization and differentiation are key drivers for companies to invest in post-training, with priorities varying by company stage (e.g., cost for mature companies, differentiation for startups) | alphasense, med | src-20261021-5156de
- 2026-10-21 | Applied Compute is used to validate data value and accelerate RL processes, providing expertise and infrastructure for efficient model tuning and evaluation | alphasense, med | src-20261021-5156de
- 2026-10-21 | Applied Compute Shift-1 router claims up to 55% lower coding-agent cost (company claim) | X post, med | src-20261021-14f61d
- 2026-10-20 | The team initially used commercial LLM providers (OpenAI, Google) but faced challenges with cost, orchestration, and scalability, prompting a shift toward open-source models and in-house fine-tuning | alphasense, med | src-20261020-9ee336
- 2026-10-20 | The team has achieved significant cost savings (5-6x cheaper) compared to previous commercial LLM solutions, with the potential for further improvements in performance and latency | alphasense, med | src-20261020-9ee336
- 2026-10-20 | The collaboration with Applied Compute involves both direct engineering support and onboarding internal machine learning engineers to their platform, with a focus on reinforcement learning and evaluation automation | alphasense, med | src-20261020-9ee336
- 2026-10-20 | Applied Compute is used primarily for fine-tuning LLMs and evaluation, with a recent contract incentivizing the team to explore using Applied Compute for inference as well | alphasense, med | src-20261020-9ee336
- 2026-10-20 | A unified platform for both training and inference is highly desirable for operational efficiency, faster updates, and scalability, but Applied Compute's inference offering is currently less mature than its training and evaluation capabilities | alphasense, med | src-20261020-9ee336
- 2026-10-06 | Applied Compute trained a Harvey custom model from expert rubrics plus synthetic data; training choices set up the customer's inference deployment | podcast, med | src-20261006-ba3eb2
- 2026-09-29 | Applied Compute AC2 in private beta; best customers have well-defined evals and spend tens of millions on inference | podcast, med | src-20260929-f57402
- 2026-08-25 | Sail CEO: about 80% of RL fine-tuning cost is rollouts; Applied Compute cited as a fine-tuning partner | podcast, med | src-20260825-e500eb
- 2026-06-30 | Rationale is data plus RL talent, supporting the view that post-training value sits with data owners | article, high | src-20260630-3abb4e
- 2026-05-01 | Baseten CEO: almost all customers modify open models with their own data | podcast, med | src-20260501-1f0aeb
- 2026-04-08 | Model is services-heavy agent training in customer environments | website, high | src-20260408-405ee6
- 2025-12-01 | Adaptive ML: 50-90% cost savings vs frontier models; 4B RL-tuned model on par with GPT-4 at 7x lower latency | podcast, med | src-20251201-8903ad

## Q10. Open versus closed models

- 2026-09-30 | The majority of spend on open-source and fine-tuned models is with a managed inference provider, primarily for inference rather than post-training, with inference accounting for over 95% of usage | alphasense, med | src-20260930-1c36c0
- 2026-09-30 | The expert values managed inference providers for their engineering focus on optimizing inference, which is seen as a key differentiator over neo cloud providers focused on training workloads | alphasense, med | src-20260930-1c36c0
- 2026-09-30 | The company has shifted to a 70/30 split in volume between open-source/fine-tuned models and frontier models, with cost still weighted towards frontier models due to higher per-token expenses | alphasense, med | src-20260930-1c36c0
- 2026-09-30 | Open-source and fine-tuned models are preferred for tasks requiring high speed, parallelism, and deterministic outputs, especially in healthcare where accuracy and reliability are critical | alphasense, med | src-20260930-1c36c0
- 2026-09-30 | Fine-tuning and post-training are largely handled internally by the expert's team, with the inference provider offering infrastructure and convenience rather than deep ML strategy | alphasense, med | src-20260930-1c36c0
- 2026-08-26 | Monetization moves from open models to enterprise specialized models | article, high | src-20260826-50c34c
- 2026-06-22 | Open-weight models as serious alternatives to closed APIs per Baseten | article, high | src-20260622-4e261f

## Q11. What labs and platforms absorb

- 2026-10-23 | Baseten bundling RL post-training overlaps Applied Compute | X post, med | src-20261023-8cc4a2
- 2026-10-20 | Open-source KV-aware routing from Google commoditizes a core startup serving feature | article, med | src-20261020-7e4d10
- 2026-10-14 | Serverless clouds also moving into post-training | article, high | src-20261014-63cf9c
- 2026-06-22 | Neutral inference cloud bundling post-training squeezes standalone post-training vendors | article, high | src-20260622-4e261f
- 2026-03-31 | Strategic cap table (NVIDIA, GE Vernova, Siemens, Eaton) signals incumbents want flexibility to exist but could absorb it | article, high | src-20260331-dc28c2

## Q12. Targets

- 2026-10-14 | Modal Sandboxes at $300M run rate is the direct comp for Sail Research's Sailboxes | article, high | src-20261014-63cf9c
- 2026-09-04 | Gimlet is now an inference cloud operator with physical capacity, not only software; capital intensity rises | article, med | src-20260904-a08d96
- 2026-08-25 | Sail founded December 2025, serving trillions of tokens a week from hundreds of data centers; cedes low-latency inference | podcast, med | src-20260825-e500eb
- 2026-08-04 | Named Indian customers but no efficiency benchmark with baseline | article, med | src-20260804-e772d5
- 2026-06-24 | Sail raised $80M (seed Sequoia, A Kleiner); customers Parallel, Detail.dev, Jack and Jill, Quadrillion | website, high | src-20260624-30f6ae
- 2026-03-23 | Named customer types (frontier lab, hyperscaler) but no named customers | article, med | src-20260323-a0cbfc
- 2025-12-02 | Gimlet at about eight figures of revenue in Dec 2025, mostly via data center partners; cloud not yet launched | podcast, med | src-20251202-9b5fb9
- 2025-09-05 | Simplismart CEO: 25% cost saved for one customer via rapid autoscaling; deployment on about 60 H100s | podcast, med | src-20250905-9d3aa9

## Q13. Valuation versus fit

- 2026-09-04 | Contracted revenue in the billions at $3B post makes Gimlet a late entry point for SPC | article, med | src-20260904-a08d96
- 2026-08-26 | Smallest-valuation post-training target with public open-weight track record; investable stage | article, high | src-20260826-50c34c
- 2026-08-25 | At $1.05B, Emerald is a growth-stage entry point | article, high | src-20260825-62437e
- 2026-08-04 | Revenue under $200K in FY25; traction is early, entry price is the cheapest of the six | article, med | src-20260804-e772d5
- 2026-04-08 | Valuation went from $1.3B (Apr 2026) to about $3.3B (Sep 2026, Harmonic) in five months | website, high | src-20260408-405ee6

## Q14. Other investable names

- 2026-09-01 | Series A Gimlet and Simplismart comp in automated inference optimization | article, med | src-20260901-21f9eb
- 2026-04-02 | Seed-stage Emerald and GridCARE comp | article, med | src-20260402-51ffad
- 2026-01-22 | Candidate comp for Simplismart and Baseten software layer | article, med | src-20260122-e767e7

## Q15. Exits

- 2026-06-30 | Exit comp for post-training is an acqui-hire into a data-rich platform, price undisclosed; a press estimate of $100-200M is speculation only | article, high | src-20260630-3abb4e

## Q16. Who to call

- 2026-04-21 | GridCARE CEO: customers are hyperscalers, neoclouds, powered land providers, PE-backed colos; found 400 MW in one market | podcast, med | src-20260421-e5221e

## Q17. Our view

- 2026-04-21 | GridCARE CEO: no utility studied was over 50% utilized (company claim) | podcast, med | src-20260421-e5221e
