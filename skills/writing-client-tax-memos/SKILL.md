---
name: writing-client-tax-memos
description: Writes plain memos from CPA-approved tax workpapers. Use when a client needs a result, rule, calculation, open item, planning note, or follow-up explained.
license: LicenseRef-Proprietary
---

# Writing client tax memos

Explain an approved result so the client can understand what happened, why it happened, what remains open, and what they can do next.

## Scope

Produce a draft client memo from an approved workpaper. The skill does not perform the underlying tax analysis, change approved numbers, give an unsupported recommendation, or send the memo. Route unresolved analysis back to its domain owner and obtain CPA approval before delivery.

## Workflow

1. Record the audience, purpose, tax year, approved workpaper, approved numbers, current authority, open items, requested action, and CPA voice examples.
2. Read `references/workflow.md`. Build a fact sheet that separates approved facts, approved conclusions, open items, and planning assumptions.
3. Stop and return the workpaper for review when a material number, rule, or conclusion lacks CPA approval or a current source.
4. Draft in this order: result, client facts, rule, calculation, open items, planning note, requested action, and sources. Adapt the section names to the case.
5. Use simple sentences and the same noun for the same thing. Explain technical terms once. Keep client names, amounts, and dates exact.
6. Read `references/example.md` when the memo concerns the 30 percent vehicle-use fixture.
7. Create `client_memo.md` and `fact_check.csv`. Run `python3 scripts/validate_memo.py --facts <facts.json> --memo <memo.md> --fact-check <fact_check.csv>`.
8. Review against `references/evaluation.md`. Mark the draft as pending CPA approval and leave delivery outside this skill.

## Output contract

- `client_memo.md` with a subject, result, facts, rule, calculation, open items, planning note, client action, and short source list.
- `fact_check.csv` with `fact_id,claim,status,source_url,workpaper_ref` for every material number and rule.

## Sources and fixtures

Read `references/source-map.md` when source or voice questions arise. The bundled vehicle memo starts with `assets/sample-input/approved_facts.json`. It is synthetic and uses a fixture calculation approved only inside the sample.

When improving this skill from the source package, run the direct solo 401(k) memo case at `../../environments/writing-client-tax-memos/suite-solo-401k-client-memo`. The answer contract fixes every modeled amount, the execution calendar, Form 5500-EZ monitoring, and the sources and assumptions section.

## Completion criteria

The work is complete when the validator exits zero, every material claim appears in the fact check, all claim statuses are approved, rule claims have current sources, numbers match the workpaper, open items are visible, the planning note is conditional, internal agent or evaluation mechanics are absent, and the memo remains an unsent draft pending CPA approval.
