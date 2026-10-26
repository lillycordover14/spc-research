# Learning path: power and compute, the AI buildout bottleneck

Day 1 basics through Day 4 expert. Every item is filed in this repo. Back to [best-of](best-of.md).

## 1. State of play
- Day 1, why power binds: NVIDIA prices its market per GW ($40B per GW for Vera Rubin) and CoreWeave raised prices about 25% while adding 500 MW. Read [src-20260826-7aa6b5] and [src-20260811-4fafb8].
- Day 2, flexibility as the unlock: Duke headroom study [src-20250201-ccc248], Norris on Texas Energy & Power [src-20250508-1afa13], then the Camus and Princeton modeling on Volts [src-20260326-771e89].
- Day 3, the startups on the grid side: Emerald on Volts [src-20260826-03722b] and Crux [src-20260805-572c12]; GridCARE Series A [src-20260514-d7ee00].
- Day 4, inference and post-training: Latent Space with Baseten [src-20260803-db2641], Gimlet on TWIML and RAISE [src-20251202-9b5fb9] [src-20260723-741ec4], Sail at AGI House [src-20260825-e500eb], Applied Compute on Altimeter [src-20260929-f57402], Adaptive at Slush [src-20251201-8903ad].

## Glossary
- Curtailment rate: share of a load's maximum annual energy that is cut; Duke uses 0.25%, 0.5%, 1.0% and 5%.
- Flexible connection: a grid tie where part of the load can be cut by the utility in stressed hours, in exchange for a faster or larger connection.
- Controllable load resource (ERCOT): a load that can be dispatched down by the grid operator.
- Disaggregated inference: running prefill and decode on separate GPU pools.
- KV cache: stored attention keys and values; routing requests to where cache already sits saves prefill.
- Speculative decoding: a small model drafts tokens that the large model verifies.
- NVFP4: NVIDIA 4-bit floating point format on Blackwell.
- Completion window: a deadline the customer grants for a response (Sail), letting the provider batch and pick cheaper hardware.
- Rollout: the inference step in RL fine-tuning where the model generates attempts to be scored.
