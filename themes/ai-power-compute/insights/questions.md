# Open questions: power and compute, the AI buildout bottleneck

The agenda. Starting question: **what are the main bottlenecks to enterprise AI at scale?** Working answer: power and compute. The job is to go deeper on the subthemes and get smarter on the actual targets. Every source should move at least one question; tag its takeaways with the number, e.g. "(Q7)". Evidence collects in `evidence-by-question.md`. Status: open / partial / answered.

Search terms for every lane: "data center interconnection", "flexible load", "inference serving", "disaggregated inference", "KV cache", "fine-tuning open models", plus each target's name (Gimlet Labs, Sail Research, Applied Compute, Simplismart, Adaptive ML, Deep Cogito).

## A. The bottleneck map
1. **Which constraint binds, and when?** Power versus GPUs versus memory (HBM) versus networking, for AI buildout through 2028. Numbers in GW, GPUs shipped, and $ capex, with their dates. _status: open_
2. **Data center interconnection:** how long large loads wait in queues by region (PJM, ERCOT, others), what the studies cost, and what actually shortens the wait (co-location at plants, behind-the-meter power, flexibility, utility tariffs, FERC rules). _status: open_
3. **Flexible load:** will utilities and ISOs connect data centers faster in exchange for curtailment? How much headroom does flexibility unlock? Who buys it and who sells it (Emerald AI, GridCARE)? _status: open_
4. **Enterprise view:** for an enterprise (not a lab), is AI at scale limited by power and GPUs, or by cost per token, latency and serving complexity? _status: open_

## B. Inference: more useful work per GPU and per megawatt
5. **Inference demand:** inference's share of compute versus training, and how agents and long-horizon tasks change token volume. _status: open_
6. **Where inference value accrues:** NVIDIA (Dynamo and its software stack), hyperscalers, labs serving their own models, neutral inference clouds (Together, Fireworks, Baseten), or software layers (Gimlet, Simplismart, Sail)? _status: open_
7. **Disaggregated inference and KV cache:** what the shift is (prefill/decode split, KV cache offload, sharing, routing), how much it saves, and who owns it (NVIDIA Dynamo, vLLM, SGLang, LMCache, startups). Durable moat or commoditized open source? _status: open_
8. **Heterogeneous hardware:** as AMD and custom silicon grow, can software that serves models across chips (for example, Gimlet's kernel generation) capture value, or do chip vendors bundle it? _status: open_

## C. Fine-tuning and open models
9. **Is fine-tuning open models a real enterprise budget line?** Evidence of custom models in production: who, for what task, and what it saved versus frontier APIs. _status: open_
10. **Open versus closed:** open-weight models' share of enterprise usage, and where Deep Cogito sits. _status: open_
11. **What the labs and platforms absorb:** lab fine-tuning and RL APIs, Databricks, hyperscaler model platforms, Thinking Machines. What is left for a standalone post-training company? _status: open_

## D. Targets and investability
12. **Target by target:** Gimlet Labs, Sail Research, Applied Compute, Simplismart and Deep Cogito. For each: product, customers, traction, pricing, gross margin, competition, and what the founders say on the record. _status: open_
13. **Valuation versus fit:** Gimlet ($3B) and Applied Compute ($3.3B) have raised at late-stage prices. Which targets are realistic entry points for SPC, and through what (primary, secondary, a next round)? _status: open_
14. **Other investable names** per subtheme at SPC's stage: power and grid software, flexible load, inference, post-training. _status: open_
15. **Exits:** what Datadog's acquisition of Adaptive ML says (price, rationale), plus NVIDIA, hyperscaler and platform acquisitions in inference and post-training. _status: open_

## E. Calls and our perspective
16. **Who to call:** heads of energy or data center development at hyperscalers and neoclouds, utility interconnection leads, ML infrastructure leads at enterprises serving open models, and customers and former employees of the targets. _status: open_
17. **Our view:** which subtheme to push on, which targets to pursue, and what we pass on. _status: open_
