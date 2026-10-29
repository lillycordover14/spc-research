# OBA theme memo QA checklist

Run on every version of insights/OBA-theme-memo.md (source of truth) and its Word and PDF exports. Results below are for v2, 2026-10-29.

1. Two parts only, with five numbered theses in the set order: tailwinds and why now, where new companies have an edge, buyer demand, unit economics, main risk and where new companies win. Each thesis is a bold full sentence with 3 to 5 bullets. Result: pass (bullets 5, 4, 4, 4, 4).
2. Part 2 categories follow the primer's five groups (A to D, then E vertical applications split by buyer function). Result: pass, 12 categories (four groups plus eight buyer functions). HR and recruiting, IT operations, real estate, government and software engineering are left out for length.
3. Each category has only Tailwinds (3 to 5), Headwinds (3 to 5), Why we should (not) focus here, and "Example companies:" with names only. There are no tables, no "where we would not invest", no "biggest questions", no "what has to be true", no "what would change our mind". Result: pass.
4. Banned words grep: investability, investable now, watch, moat, flywheel, unlock, landscape, leverage, robust, crucial, delve, navigate, paradigm, In summary, this memo, below we, takeaway #, see section, venture-fit phrasing, em dashes, "It's not X, it's Y", hype words for numbers. Result: pass. "Large" appears only to describe company size.
5. No body sentence of 12 words or fewer (parentheticals excluded), no colon labels mid-sentence, no label-style leads. Result: pass (qa.py reports 0 SHORT, 0 COLON).
6. Company names are used only where deliberate, with no vague "one vendor". Result: pass.
7. Every figure and quote traces to a filed source id cited inline in short form. Company statements are labeled "claim" and our own figures "by our estimate" or "our count". Result: pass. qa.py has 3 NUM? flags, all known false positives: $350,000 to $400,000 is our estimate, $0.99 is matched in the source, and "45" belongs to the 45x estimate. UBS is not used. Truist is used once, in B.
8. Length and styles: 5,583 words, 9 pages in the PDF against a target of about 8 pages. Sewon template styles carry into the docx (title, subtitle, h1, numbered theses, bullets, h2/h3 category heads, body). Result: pass on styles. Length is one page over target because there are 12 categories against 9 in the VII memo.
9. Validate, commit, pull --rebase, push. Result: see commit "OBA theme memo v2".
10. Cold read as Brooke or Lorenzo, who are new to the theme. Terms are defined on first use (BPO, ARR, FDE, ERP). Each focus call reads as a decision with its economics. Result: pass.
