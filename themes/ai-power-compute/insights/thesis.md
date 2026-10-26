# Working thesis: power and compute, the AI buildout bottleneck

_Seeded 2026-10-26 from Lilly's brief. Living version: every claim should end with a source id once we have one. Nothing below is sourced yet; these are hypotheses to test._

## Definition
The constraints that cap how much AI the economy can run, and the companies that relax them. Two halves:
- **Power to load:** getting megawatts to data centers faster through interconnection, flexible load and grid capacity.
- **Work per megawatt:** getting more useful tokens out of every GPU through inference serving, disaggregated inference, KV cache, kernels and scheduling, plus smaller custom models through fine-tuning and post-training on open weights.

The layers (see `taxonomy.yml`): 1. power supply, 2. grid interconnection and flexible load, 3. data centers and GPU capacity, 4. chips, memory and networking, 5. inference serving and efficiency, 6. fine-tuning, post-training and open models.

## Why now (to source)
- Interconnection queues for large loads run to years in key markets [src: TBD]
- Research suggests flexible data center load could unlock large grid headroom without new generation [src: TBD]
- Inference is overtaking training as the dominant AI workload, and agents multiply tokens per task [src: TBD]
- Open-weight models are close enough to the frontier that custom fine-tuned models can win on cost for specific tasks [src: TBD]

## Preliminary thesis (hypotheses)
1. For an enterprise, the binding constraint shows up as cost per token and capacity access, not as megawatts. Software that raises tokens per GPU is the investable expression of "power and compute" for an operator-led fund. Power-side plays are capital-heavy, except software that unlocks grid capacity (flexible load, interconnection).
2. Inference-serving value splits between NVIDIA's bundled stack and neutral, hardware-agnostic software. The neutral layer wins if hardware diversifies (AMD, custom silicon) and if agent workloads need a different serving shape (long-horizon, batch, stateful KV cache).
3. Disaggregated inference and KV-cache management are where the next large efficiency gains come from, but open source (vLLM, SGLang) commoditizes them fast. A startup needs scheduling, kernels or workload data that compounds.
4. Fine-tuning open models is real where task volume is high and latency or cost matter. Value accrues to whoever owns the RL environment and evaluation design for the customer's work, not to the training infrastructure.
5. Several targets are priced like late-stage companies ($3B+). Entry may only make sense for some, or through the next round.

## What would make us wrong
- NVIDIA's software (Dynamo and related tools) and hyperscaler endpoints absorb disaggregated serving and KV-cache management, leaving no room for neutral software.
- Enterprises don't fine-tune at scale; frontier APIs keep getting cheaper faster than custom models pay back.
- Flexible load doesn't get utility or ISO acceptance at scale, so interconnection stays a construction and permitting problem.

## Where SPC can play
- Enterprise GTM for infrastructure companies selling to Fortune 500 platform and ML teams.
- Targets for a first look: Gimlet Labs, Sail Research, Simplismart (inference); Applied Compute, Deep Cogito (post-training and open models); Emerald AI, GridCARE (grid). Adaptive ML is a comp (acquired by Datadog).

## Running conclusions
<!-- dated bullets, newest first, source ids -->
