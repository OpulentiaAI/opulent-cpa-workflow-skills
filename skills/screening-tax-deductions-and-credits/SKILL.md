---
name: screening-tax-deductions-and-credits
description: Screens a client profile for tax benefits and missing proof. Use when the user asks for a deduction sweep, credit checklist, planning review, new-client scan, or document gaps.
license: LicenseRef-Proprietary
---

# Screening tax deductions and credits

Build an evidence-based opportunity register from the whole client profile. Coverage matters as much as findings, so record each topic considered even when it is not applicable.

## Scope

Produce a screening workpaper for CPA review. The skill identifies candidates and missing proof. It ends before claiming a benefit, choosing an election, calculating a final tax liability, filing, or giving advice to the client. Use a domain skill for the full analysis of a flagged vehicle, multistate, or loss issue.

## Workflow

1. Record the tax year, filing status, dependents, entity interests, income sources, business activities, assets, benefits, retirement plans, health coverage, home use, education, energy, charitable activity, losses, credits, carryovers, and prior-year returns. Use `unknown` for missing facts.
2. Read `references/workflow.md`. Build a coverage list suited to the client instead of starting from a fixed generic checklist alone.
3. Refresh official authority for the stated tax year using `references/source-map.md`. For each triggered topic, record the eligibility elements, available facts, missing evidence, interaction with other benefits, and the owning form or domain skill.
4. Give each topic a status of `supported`, `not_supported`, `review`, or `not_applicable`. Use `supported` only when every material eligibility element and calculation input is present.
5. Create one evidence request for every `review` item. Ask for the exact fact or document that can change the result.
6. Read `references/example.md` when the profile resembles the physician Schedule C fixture.
7. Create the four files in the output contract. Run `python3 scripts/validate_sweep.py --profile <profile.json> --opportunities <opportunities.csv> --coverage <coverage.csv> --evidence <evidence.csv>`.
8. Review against `references/evaluation.md`. Keep the opportunity list separate from a promise of tax savings.

## Output contract

- `opportunities.csv` with `topic,status,reason,missing_evidence,estimated_amount,source_url,owner`.
- `coverage.csv` with `topic,considered,trigger,status,notes`.
- `evidence_request.csv` with `topic,document_or_fact,why_needed,owner,status`.
- `workpaper.md` with client scope, methods, supported items, review items, interactions, excluded topics, and next CPA actions.

## Sources and fixtures

Read `references/source-map.md` before using a federal or state rule. The sample starts with `assets/sample-input/client_profile.json`. It is a synthetic screening fixture. Blank estimated amounts mean the evidence is not complete enough to estimate.

When improving this skill from the source package, run the direct HSA eligibility case at `../../environments/screening-tax-deductions-and-credits/suite-hsa-eligibility-sweep`. The suite rubric checks thresholds, monthly eligibility, contribution alternatives, employer funding, testing risk, and record support.

## Completion criteria

The work is complete when the validator exits zero, every client trigger appears in opportunities and coverage, each review item has a direct evidence request, every authority link is official and current for the tax year, no missing input is converted into savings, and the workpaper routes specialist issues to their owning analysis.
