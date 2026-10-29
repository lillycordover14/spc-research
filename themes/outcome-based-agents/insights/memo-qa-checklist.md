# OBA theme memo QA checklist

Run on every version of insights/OBA-theme-memo.md (source of truth) and its Word and PDF exports. The automated checks live in /workspace/oba-memo/qa.py on the box. The script was made stricter for v3 after an outside review of v2 (commit 6a9134d) found that our own v2 checklist had marked every item as passing when only 4 of 10 passed in full, 4 passed in part and 2 failed. This file records v3 results honestly, including what the script cannot catch.

## v5 (2026-10-29): example companies audit

- Every Example companies name checked against cards and sources; full keep or cut table with reasons and source ids in insights/memo-example-companies-audit.md.
- Lists cut from 131 to 81 names: A 19 to 7, B 9 to 7, C 16 to 8, D 17 to 10, E1 19 to 14, E2 25 to 16, E3 26 to 19. 16 names cut as uncertain.
- Body text unchanged; cut names still cited as evidence (Skan AI, Celonis, Rillet, Eudia, Guidewire, Epic, KPMG, Concentrix, TTEC, Clay) are used as context, not as examples.
- Category A rewritten to match its list: subhead now "Agent Platforms, Frameworks and Infrastructure"; tailwinds lead on agents reaching production, lab and cloud agent platforms (OpenAI Frontier, AWS AgentCore, Microsoft Agent 365) and frameworks (LangChain in Google's Agents CLI); tooling demand kept as one supporting tailwind (PocketOS); focus says the labs and clouds are not venture targets and independent frameworks compete with their suppliers.
- Cut names still cited in the body now read as evidence: Skan AI described as recording work for agents, Rillet as a ledger rather than an agent, Eudia as augmenting lawyers, Clay as a sales data and workflow tool. Guidewire, Epic, KPMG, Concentrix, TTEC and Celonis already read as evidence.
- Strict QA: STRICT_FLAGS 0 (three known NUM? false positives: $350,000, $400,000, $0.99). 5,127 words, 8 pages.

## v4 results, 2026-10-29

v4 applies the two blocking fixes from the outside review of v3 (commit 0ad733a) plus its nits, each checked against the filed source.

- **Blocking fix 1, B focus lead:** it now carries the don't-focus call ("Systems of record are established incumbents that most agent spending will run through, so they matter to us as the channel, the likely acquirer and the main absorber of any startup whose work they can copy"). The repeat of "three other roles" is cut.
- **Blocking fix 2, Edison wording:** now matches src-20251105-cdfbed (launch at $200 per run on 2025-11-05) and src-20260519-9cb3f1 (2026-05-19: founding subscriptions end, access by application, new pricing to be announced).
- **Nits:**
  - Truist line paraphrased as "especially favors systems of record".
  - Collibra example restated without a vague reference.
  - Magentic now carries the sourced $100M to $200M.
  - Fin named consistently, with a plain-words first mention.
  - Dermatology point cut from T2 and kept in E3.
  - "model release" no longer used twice.
  - "target discovery" and "demand package" explained.
  - Lassie dropped, because it is not in the primer.
- **Strict QA (qa.py):** 0 strict flags. Three NUM? false positives remain, all checked by hand: $350,000 and $400,000 are our estimate, and the source has $0.99 as "99 cent". There is 1 "instead of" and 0 dashes. qa.py now measures bold-lead length without the section label.
- **Primer match:** now has one documented exception, Crescendo in D.
- **Length:** 8 pages, 5,055 words. Sewon styles carry through.
- **Validate:** passed.

## v3 results, 2026-10-29

1. **Structure: two parts and five theses.** Pass. The script checks the h1 count, the five numbered theses and 3 to 5 bullets each (5, 4, 4, 4, 4). The thesis order is tailwinds and why now, then the edge for new companies, buyers, unit economics, and the main risk with where new companies win.
2. **Categories match the primer.** Pass, with two documented exceptions. There are seven categories: A Labs and Hyperscalers, B Systems of Record (incumbents only), C Horizontal Orchestration and Work Context, D SIs, BPOs and AI Services, E1 Front Office, E2 Back-Office Operations and E3 Regulated Services. The script reads primer section 8.2 (buyer function) and 8.1 (worlds) and checks every listed company against the allowed primer groups for its category. It also checks each incumbent against a fixed incumbent list. The exceptions are Lassie, which is not in the primer cuts and is placed in E3 from its a16z source, and Crescendo. The primer's 8.2 table puts Crescendo in customer service, but primer 8.4 lists it as selling finished work, and the memo's evidence on it is about AI-native outsourcing, so it sits in D.
3. **Only the four section types per category, and each company listed once.** Pass. The script counts Tailwinds (3 to 5), Headwinds (3 to 5) and one focus section per category, and runs a duplicate check across all Example companies lists (0 duplicates). The 16 names that v2 listed twice are now in one place each.
4. **Banned words, hedges, "instead of" and "large".** Pass. The script greps the banned list and runs a hedge check for could, may, might, perhaps and possibly outside quotes. It also counts "instead of" (0 uses, cap 3) and flags large, larger and largest (0). The em dash and en dash count is 0. Jargon from v2 is defined or cut: harness, graders, test eval, SoR, API key, credits and "refilling the tank", goodwill impairment, like for like, net dollar retention, general ledger, payer rules and prior authorization.
5. **Sentences.** Pass on the script, with a limit. The script reports no body sentences of 12 words or fewer, no colon labels, no citations inside bold text, no bold leads over 40 words and no repeated sentences or repeated quotes. The comma-splice check is a heuristic that skips sentences containing a later "and", so series of three are not flagged. Splices were also fixed by hand at the three places the review named.
6. **Company names only where deliberate.** Pass. The vague-reference check (one customer, a company's, one deployment, one vendor, one buyer, some buyers, one lab, an analytics agent) returns 0. Both people the review called vague are now named: Workfabric AI is the Sierra customer that audits the count, and Collibra's CEO is the source on the analytics agent. The fintech buyer is described as the buyer in a vendor selection Sierra lost, because the source does not name the company.
7. **Every figure sourced and labeled.** Pass. Each sentence's quotes and numbers are traced to the cited source files. Three NUM? flags remain and all are known false positives. $350,000 and $400,000 are labeled "by our estimate", and $0.99 appears in the source as "99 cent". Company statements are labeled "claim". These v2 sourcing errors were fixed against the filed sources:
   - NiCE is now "AI and self-service ARR".
   - Zendesk's $200M was dropped as proof of per-result pricing.
   - Decagon's roughly 45x is stated as pairing a January 2026 valuation with revenue reported later in 2026. The Newcomer publish date is not verified in the filed source.
   - Edison's $200 per run is stated as a launch price that was replaced within a year.
   - The context decay from about 90% to 60% accuracy is added as a headwind in C.
8. **Length and Sewon styles.** Pass on pages and styles: 8 pages in the PDF, with Sewon template styles for the title, subtitle, h1, numbered theses, bullets, category heads, body and example lines. Word count is 5,025 against a target of about 5,300, so it is slightly short.
9. **Validate, commit, pull --rebase, push.** See commit "OBA theme memo v3".
10. **Cold read and logic read as Brooke or Lorenzo would.** Pass. Each focus call was checked against the five theses, with no contradictions:
    - B is "do not focus", consistent with T5, which names the systems of record as absorbers.
    - E1 is "do not focus", consistent with T5 because a resolved ticket is a generic, countable task.
    - E2 is "focus", and its reasoning explains why ERP vendors find the work hard to absorb, because it runs across suppliers, banks and email outside any one record.
    - E3 is "focus", consistent with T2 and T5 on licenses and liability.
    - C and D are "do not focus", consistent with T3 (easy switching) and T4 (margins).
    - The open-model price pressure in the E3 headwinds applies to tool vendors, and the E3 focus backs license holders, so the two do not conflict.
