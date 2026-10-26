# Framework: how we present this theme and lead expert calls

Purpose: make the readout and every expert call answer the same questions in the same structure, so evidence adds up. Agents: when a source speaks to a cell below, add a bullet with its source id to `evidence-by-question.md` under the matching question number.

## 1. The bottleneck stack (electrons to tokens)

| Layer | Bottleneck | Who is there today | Capital intensity | Where a startup can win |
|---|---|---|---|---|
| 1. Power supply | New generation, turbines, on-site power | GE Vernova, Siemens Energy, IPPs, utilities | Very high | Siting, financing and deployment software |
| 2. Grid interconnection and flexible load | Queue years, grid capacity | Utilities, ISOs; Emerald AI, GridCARE | Low (software) | Unlocking latent capacity through flexibility and better studies |
| 3. Data centers and GPU capacity | Space, GPUs, financing | Hyperscalers, CoreWeave, neoclouds | Very high | Benchmark only |
| 4. Chips, memory, networking | Supply, HBM, interconnect | NVIDIA, AMD, Broadcom, memory makers | Very high | Benchmark only |
| 5. Inference serving | Cost per token, latency, utilization | NVIDIA stack, vLLM/SGLang, Together, Fireworks, Baseten; Gimlet, Sail, Simplismart | Low to medium | Hardware-agnostic serving, agent-shaped workloads, KV-cache and scheduling |
| 6. Fine-tuning and open models | Frontier cost for narrow tasks | Lab APIs, Databricks; Applied Compute, Deep Cogito; Adaptive ML (Datadog) | Medium | Owning RL environments and evals for customer work |

Fill "who is there" and the win column with sourced evidence as it lands; the version above is the starting hypothesis.

## 2. Where inference value accrues: five possible worlds
1. **NVIDIA bundles it.** Dynamo and NVIDIA's software stack make disaggregated serving and KV cache a free feature of the hardware. Implication: avoid standalone serving software.
2. **Hyperscalers own it.** Enterprises consume tokens from Bedrock, Vertex and Azure endpoints. Implication: serving startups sell to the clouds or get squeezed.
3. **Labs own it.** Most tokens are frontier-model tokens served by the labs themselves. Implication: serving value sits inside labs; open-model serving is a niche.
4. **Neutral inference clouds.** Together, Fireworks, Baseten and peers aggregate open-model demand. Implication: scale and GPU access win; software alone doesn't.
5. **Software across hardware.** Heterogeneous chips plus agent workloads make a neutral software layer necessary (Gimlet, Simplismart, Sail). Implication: layer 5 targets win.

For every source and call, note which world the evidence points to; the readout states which world we believe and why.

### World tally
<!-- one line per source or call, newest first: `<date> <source> -> world N because ... [src-id]` -->
- 2026-10-20 ElevenLabs research engineer call -> world 4 because Fireworks and Baseten run text models in parallel behind a custom gateway, voice kept in-house [src-20261020-b4cff8]
- 2026-10-19 OpenEvidence ML engineer call -> world 4 because Baseten carries production inference and switching to Fireworks is minor code changes [src-20261019-494f8d]
- 2026-10-14 Modal Series D post -> world 4 because a serverless cloud reached $1B run rate on a 20+ cloud capacity pool [src-20261014-63cf9c]
- 2026-09-30 OpenEvidence ML engineer call -> world 4 because 70% of volume is open or fine-tuned models on a managed inference provider [src-20260930-1c36c0]
- 2026-09-14 Intel performance architect call -> world 5 (weak) because workloads are locked to single-vendor stacks today and Gimlet/Modular tools are not yet standard; adoption hinges on proven tokens per dollar [src-20260914-28316c]
- 2026-09-09 DirecTV data scientist call -> world 4 because Fireworks then Baseten were selected on price-performance; switch only at 30%+ cost increase [src-20260909-ebd6d1]
- 2026-09-04 Gimlet Series B post -> world 5 because heterogeneous disaggregation is sold to frontier labs with billions in contracted revenue (company claim) [src-20260904-a08d96]
- 2026-08-26 NVIDIA Q2 FY27 call -> world 1 because NVIDIA bundles the Groq LPU into Vera Rubin and says most data centers will be Vera Rubin plus NVLink 72 [src-20260826-7aa6b5]
- 2026-08-25 Sail CEO at AGI House -> world 5 because cost per token comes from latency relaxation plus chip choice across hundreds of data centers (company claim) [src-20260825-e500eb]
- 2026-08-19 d-Matrix principal engineer call -> world 5 because Gimlet is seen as the neutral layer for mixed accelerators [src-20260819-e49885]
- 2026-08-11 CoreWeave Q2 2026 call -> world 4 because managed inference booked ARR went from $1M to over $100M on a neutral cloud [src-20260811-4fafb8]
- 2026-08-09 Cerebras senior member call -> world 5 because value is raising utilization by placing prefill and decode on different hardware [src-20260809-79a0d9]
- 2026-08-07 Former Groq VP call -> world 1 because NVIDIA aims to control the stack (Vera Rubin) and switching off NVIDIA is extremely hard [src-20260807-b6b235]
- 2026-08-03 Latent Space with Baseten engineers -> world 4 because the neutral cloud integrates disaggregation, speculators and NVFP4 itself; Dynamo is only a toolkit [src-20260803-db2641]
- 2026-07-23 Gimlet CEO at RAISE -> world 5 because workloads are split across CPU, GPU, d-Matrix and Cerebras for 4-5x capacity per dollar (company claim) [src-20260723-741ec4]
- 2026-06-22 Baseten Series F post -> world 4 because revenue grew 20x and inference volume 40x, with post-training bundled in [src-20260622-4e261f]
- 2026-01-23 Baseten Series E post -> world 4 because NVIDIA invested in a neutral inference cloud [src-20260123-cfd280]
- 2026-01-22 a16z Inferact post -> world 5 because vLLM runs on 400k+ GPUs across hardware, open source sets the serving floor [src-20260122-e767e7]

Running count: world 1: 2, world 2: 0, world 3: 0, world 4: 9, world 5: 7. No source yet tests worlds 2 or 3.

## 3. Efficiency test (for every inference or post-training target)
Capture: the unit of improvement (tokens per dollar, tokens per watt, latency at a given throughput, GPU utilization), the benchmark and baseline, the hardware, whether customers confirm it, and what happens to the gain when open source catches up. A target passes if the gain is customer-verified and comes from something that compounds (kernels, scheduling, workload data, RL environments).

## 4. Power test (for every grid or power target)
Capture: MW unlocked or months saved, which utility or ISO accepted it, the contract form (who pays whom), and whether it repeats beyond a pilot.

## 5. Readout structure
1. **Answer first:** which bottleneck matters most for enterprise AI, and where we want to invest. One paragraph.
2. **Bottleneck map** (Q1-Q4): three numbers on power and interconnection, two on compute.
3. **Inference** (Q5-Q8): which of the five worlds, and why.
4. **Fine-tuning and open models** (Q9-Q11).
5. **Targets** (Q12-Q15): one row per target with stage, valuation, traction, the efficiency or power test result, and a recommendation (pursue, track, pass).
6. **Calls we'd make** (Q16) and the five questions we'd ask.
