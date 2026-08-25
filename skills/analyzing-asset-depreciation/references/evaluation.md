# Evaluation contract

## Blind task prompt

Analyze the supplied vehicle purchase documents and mileage log for the stated tax year. Produce the facts, eligibility analysis, schedule, form map, and workpaper. Show the math and surface unsupported decisions.

## World design

Include a purchase agreement, add-on contract, mileage log, client note claiming 100 percent business use, entity profile, and current official tax sources. Seed a mismatch between the client claim and mileage log, one unresolved basis item, and one commuting trap.

## Binary criteria

1. Extracted included basis ties to supported purchase items.
2. Total mileage equals business, commuting, and personal mileage.
3. Qualified business use excludes commuting and equals the source log.
4. The predominant-use conclusion matches the official threshold.
5. Section 179 and special allowance conclusions cite current authority.
6. Depreciation schedule math reproduces from stated factors.
7. The counterfactual changes only the disclosed assumption.
8. Form mapping names the form, part, line label, and source.
9. Unresolved basis, method, limit, or software choices are marked `unknown` or routed to CPA review.

Use a fresh agent, immutable inputs, hidden grader files, a separate output path, and three repeated runs. Grade one outcome per criterion.
