---
name: determining-tax-loss-treatment
description: Analyzes unusual tax losses and builds an evidence workpaper. Use when a client reports theft, fraud, a hacked account, casualty, scam, or unrecovered property.
license: LicenseRef-Proprietary
---

# Determining tax loss treatment

Turn an unusual loss event into a fact record, treatment matrix, evidence request, and review-ready tax workpaper.

## Scope

Produce a draft analysis for CPA and legal review. The skill ends before claiming a deduction, filing Form 4684 or another return, telling the client the loss is deductible, or deciding whether conduct is theft under state law. Use `screening-tax-deductions-and-credits` for a broad client benefit sweep instead of a single loss event.

## Workflow

1. Record the tax year, discovery date, loss date, property or funds, adjusted basis, value before and after, reimbursements, recovery efforts, account use, profit motive, insurance, police or platform reports, litigation, and state-law classification. Use `unknown` for missing facts.
2. Read `references/workflow.md`. Separate fact extraction, net-loss arithmetic, legal classification, federal tax treatment, timing, limitation, and form placement.
3. Refresh current official authority for the tax year using `references/source-map.md`. Identify each plausible treatment and the facts required to support or reject it.
4. Calculate gross loss, reimbursements received or expected, reasonable recovery prospects, and provisional net loss. Keep value questions and legal limits separate from arithmetic.
5. Build a treatment matrix. Give each candidate a status of `supported`, `rejected`, or `review`, with reason, missing fact, and official URL.
6. Build the evidence request from the gaps that could change classification, timing, amount, or form.
7. Read `references/example.md` when the event resembles the hacked business-account fixture.
8. Create the five files in the output contract. Run `python3 scripts/validate_loss.py --event <event.json> --facts <facts.json> --treatments <treatments.csv> --forms <forms.csv> --evidence <evidence.csv>`.
9. Review the result against `references/evaluation.md`. State the tax-year authority revision and every point reserved for CPA or counsel.

## Output contract

- `event_facts.json` with sourced facts, amounts, dates, business or personal use, recovery status, and unknowns.
- `treatment_matrix.csv` with `candidate,status,reason,missing_fact,source_url`.
- `form_map.csv` with `candidate,form,section,line_label,status,source_url`.
- `evidence_request.csv` with `gap,document_or_fact,why_needed,owner,status`.
- `workpaper.md` with timeline, arithmetic, treatment comparison, timing, authorities, and review points.

## Sources and fixtures

Read `references/source-map.md` before making a conclusion. The sample remains in `review` because the state-law theft classification is unknown. This is the intended result when a legal element lacks proof.

When improving this skill from the source package, run the APEX settlement-holdback case at `../../environments/determining-tax-loss-treatment/apex-settlement-holdback`. It tests recovery documents, one supported treatment, exact account direction, and a bounded conclusion.

## Completion criteria

The work is complete when the validator exits zero, gross loss less recoveries equals provisional net loss, every treatment has a current official source, every unresolved legal or recovery fact appears in the evidence request, form mapping is tied to a treatment rather than assumed, and the workpaper avoids a final deduction claim while review items remain.
