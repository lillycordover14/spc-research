# Expert-call guide

Use with `framework.md`. File each call as `type: expert-call`, with `expert_background` as the first line, then every point from the call as bullets in call order (Lilly's takeaways format). Tag each takeaway with its question number.

## Before every call
- Read the relevant company card and its top three sources (`python3 scripts/search.py --theme apc "<name>"`).
- Pick five questions where `evidence-by-question.md` is thinnest.

## 1. Hyperscaler, neocloud or data center developer: head of energy or site development
1. What is the binding constraint on your next 1 GW: power, interconnection, turbines and transformers, GPUs, or financing? (Q1)
2. How long is your typical interconnection wait in PJM, ERCOT and other markets, and what has shortened it? (Q2)
3. Would you accept curtailable or flexible service to connect faster? On what terms? Who have you worked with? (Q3)
4. Behind-the-meter versus grid: what share of new capacity is on-site generation? (Q1, Q2)

## 2. Utility or ISO interconnection lead
1. How are large-load requests trending, and how many are speculative? (Q2)
2. What would let you connect a data center faster: flexibility commitments, co-location, new tariffs? (Q2, Q3)
3. Have you approved any flexible-load interconnection? How was it verified? (Q3)

## 3. Enterprise ML infrastructure lead (serving open models in production)
1. What share of your tokens is open models versus frontier APIs, and why? (Q4, Q10)
2. Who serves your models: a hyperscaler, an inference cloud, NVIDIA's stack, open source you run yourself, or a startup? (Q6)
3. Have you adopted disaggregated serving or KV-cache offload? What did it save? (Q7)
4. Do you fine-tune or run RL on open models? For which tasks, and what did it save versus a frontier API? (Q9)
5. Are you running non-NVIDIA hardware? What software made that possible? (Q8)

## 4. Customer or former employee of a target (Gimlet, Sail, Applied Compute, Simplismart, Deep Cogito; Adaptive ML for the Datadog comp)
1. What workload did you buy it for, and what did it replace? (Q12)
2. The measured gain: tokens per dollar, latency, accuracy. Did it hold in production? (Q12, efficiency test)
3. Pricing and contract shape; renewal intent. (Q12)
4. What would make you switch to NVIDIA's stack, a hyperscaler or a lab offering instead? (Q6, Q11)

## After every call
- File it; add dated facts to the company card and `signals.md`; add claims to `evidence-by-question.md`.
- Add one line to the world tally in `framework.md` section 2.
