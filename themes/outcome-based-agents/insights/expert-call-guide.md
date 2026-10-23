# Expert-call guide

Use with `framework.md`. Each call is filed as `type: expert-call` with `expert_background` as the first line, then every point from the call as bullets in call order (Lilly's takeaways format). Tag each takeaway with the question number it answers. Hold calls until after the 2026-10-28/29 readout unless Lilly says otherwise.

## Before every call
- Read the company or person's card and their top three sources in this repo (`python3 scripts/search.py --theme oba "<name>"`).
- Pick the five questions below that our evidence is thinnest on (see `evidence-by-question.md`).

## 1. Fortune 500 head of AI / automation (agents in production)
Who to find: heads of AI, automation, intelligent operations or shared services at companies publicly known to run agents in production.
1. How many agents do you run in production today, in which functions, and what counts as "production" for you? (Q1)
2. Walk me through the last agent you moved from pilot to production. What almost stopped it? (Q3)
3. Who built the harness: you, a lab, a platform (Salesforce / ServiceNow / Microsoft / UiPath), or an SI? Would you choose the same again? (Q5)
4. Do you pay any vendor per outcome? What is the unit, how is it counted, and did it renew? (Q2)
5. Whose budget pays for agents: IT, the function, or the BPO / outsourcing line? Has headcount moved? (Q4)
6. What did OpenAI or Anthropic's enterprise launches this year change in your vendor plans? (Q6)
7. If one vendor could own orchestration across your systems, who would you trust, and what would they need to prove? (Q7, Q8)

## 2. SI agentic practice lead (Deloitte, Accenture, Cognizant, Infosys, others)
1. How many clients have agents in production versus pilots, and what separates them? (Q1, Q3)
2. Which platforms do you deploy most, and how has that mix changed in the last six months? (Q5, Q6)
3. What does a typical agentic engagement cost, and how much is software versus your people? (Q4, Q11)
4. Are clients asking for outcome-based contracts from you? How do you price them? (Q2)
5. Which startups do you see in client stacks, and which get ripped out? (Q9, Q10)
6. Where do the labs' own deployment teams compete with you, and where do they partner? (Q5)

## 3. Customer or former employee: Sycamore, Duvo, Workfabric
1. What problem did you buy it for, and what did it replace (people, BPO, RPA, another platform)? (Q4, Q15)
2. What outcome is measured, by whom, and what did it move? (Q2, Q15)
3. How much of the deployment was the vendor's product versus their engineers on site? (Q11)
4. What context does the product learn about how your work gets done, and who owns that data? (Q7)
5. Could you get the same result from your lab platform plus an SI? Why not? (Q7)
6. Renewal intent, and what would make you churn? (Q15)

## After every call
- File the call (`templates/expert-call.md` or `scripts/add_source.py`, `type: expert-call`).
- Add dated facts to the company card and `signals.md`; add claims to `evidence-by-question.md`.
- Update the "world" tally in `framework.md` section 2 with one line: `<date> <call> -> world N because ... [src-id]`.
