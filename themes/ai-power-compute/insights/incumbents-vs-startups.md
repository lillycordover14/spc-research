# Incumbents vs startups: what NVIDIA, the hyperscalers and the labs ship, and what it absorbs

Answers Q6, Q7, Q8 and Q11. One row per launch, newest first, each with a source id. In scope: inference serving and scheduling software (NVIDIA Dynamo, TensorRT-LLM, NIM), hyperscaler inference and fine-tuning endpoints, lab fine-tuning and RL APIs, open-source serving milestones (vLLM, SGLang, LMCache), and acquisitions of inference or post-training startups.

| Date | Company | Launch or deal | Layer it competes with | Startup categories hit | Source |
|---|---|---|---|---|---|
| 2026-08-26 | NVIDIA | Groq LPU folded into the Vera Rubin platform for high-interactivity serving; $40B revenue opportunity per GW | Heterogeneous inference hardware and placement software | Gimlet Labs (world 5), Sail chip arbitrage | src-20260826-7aa6b5 |
| 2026-08-11 | CoreWeave | Managed inference booked ARR from $1M to over $100M, target $250M+ exiting 2026; Grammarly and You.com run fine-tuned and open models | Neutral managed inference clouds | Baseten, Together AI, Fireworks AI | src-20260811-4fafb8 |
| 2026-08-03 | NVIDIA | Dynamo described by Baseten engineers as a toolkit for KV cache movement and disaggregation, not a finished system | Disaggregated serving and KV cache software | Serving-engine startups; neutral clouds still integrate it themselves | src-20260803-db2641 |
| 2026-06-30 | Datadog | Acquired Adaptive ML into Datadog AI Research | RL post-training platforms | Applied Compute, Adaptive-style tuning shops | src-20260630-3abb4e |

## Read-across
<!-- dated bullets: which layers look absorbed, which look safe, and why [src] -->
- 2026-10-26 | NVIDIA is absorbing heterogeneity from the top: by putting Groq inside Vera Rubin it offers a mixed-hardware option without a third-party scheduler. Gimlet's opening is the long tail of non-NVIDIA silicon (d-Matrix, Cerebras, CPUs) and operators that want to avoid lock-in [src-20260826-7aa6b5] [src-20260723-741ec4]
- 2026-10-26 | Disaggregation and KV cache tooling looks absorbed as a feature: Baseten ships it in-house on top of Dynamo, and the gain is roughly 2x of a 4-6x stack. A standalone serving startup has to beat both open source and the neutral clouds [src-20260803-db2641]
- 2026-10-26 | Neoclouds moving up: CoreWeave's managed inference went from $1M to over $100M booked ARR in months, so the neutral-cloud category now includes capacity owners [src-20260811-4fafb8]
- 2026-10-26 | Looks safe for now: latency-tolerant agent inference (Sail cedes low latency, competes on cost per token) and grid flexibility software (no incumbent product; PJM resistance is the risk) [src-20260825-e500eb] [src-20260826-03722b]
