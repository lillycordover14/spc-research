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
