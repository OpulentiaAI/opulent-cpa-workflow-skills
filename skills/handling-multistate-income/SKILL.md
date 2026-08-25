---
name: handling-multistate-income
description: Sources income and tests state filing requirements. Use when W-2 or 1099 income crosses states, or for nonresident returns, remote work, nexus, apportionment, or state credits.
license: LicenseRef-Proprietary
---

# Handling multistate income

Build a state-by-state workpaper that separates source facts, allocation math, filing conclusions, and unresolved legal questions.

## Scope

Produce draft sourcing and filing workpapers for CPA review. The skill ends before filing a state return, making an election, registering an entity, or giving a legal conclusion to the client.

## Workflow

1. Record the tax year, taxpayer and entity types, domicile, residency periods, work locations, travel days, payers, forms, withholding, business activities, property, payroll, and prior state filings. Use `unknown` when a fact is missing.
2. Read `references/workflow.md`. Build one income record per payer and source type. Preserve federal amounts, state boxes, source documents, and withholding.
3. Build a state activity matrix. Separate individual residency, income sourcing, business nexus, apportionment, filing threshold, reciprocity, composite or pass-through rules, and credits for tax paid to another state.
4. Refresh each state's official authority for the stated tax year using `references/source-map.md`. Record the exact form or instruction revision and access date. Treat Multistate Tax Commission material as a model reference, not a state's enacted rule.
5. Allocate each income item with a stated method and supported denominator. Do not allocate from payer address alone when service location, market, property, payroll, sales, or another state rule controls.
6. Create a filing determination for every relevant state. Use `required`, `not_required`, or `review`. A current official source and complete facts are required for the first two values.
7. Read `references/example.md` when the case resembles the Illinois resident with Illinois and Arizona service income.
8. Create the four files in the output contract. Run `python3 scripts/validate_multistate.py --income <income.csv> --sourcing <sourcing.csv> --summary <summary.csv> --determinations <determinations.csv>`.
9. Review against `references/evaluation.md`. List each missing fact that could change source, filing, tax, credit, or registration treatment.

## Output contract

- `income_sourcing.csv` with `income_id,state,source_type,gross_amount,allocated_amount,allocation_basis,status,source_url`.
- `state_summary.csv` with `state,source_income,withholding,resident_return_income,notes`.
- `filing_determinations.csv` with `state,return_type,status,reason,form_or_instruction,source_url,accessed`.
- `workpaper.md` with residency timeline, activity matrix, allocation math, credit interaction, assumptions, and CPA review points.

## Sources and fixtures

Read `references/source-map.md` before applying a state rule. The sample uses `assets/sample-input/income.csv` and `assets/sample-input/allocation_facts.csv`. It is a synthetic 2025 fixture and does not establish that service-day allocation is correct for another client, state, or income type.

When improving this skill from the source package, run the jurisdiction-mapping case at `../../environments/handling-multistate-income/suite-cross-border-jurisdiction-map`. It is a process calibration for entity, jurisdiction, rate, risk, and action tracking. The live skill still requires current state-specific authority.

## Completion criteria

The work is complete when the validator exits zero, every income item allocates back to its federal gross amount, state summaries equal detail, each filing conclusion has a current official state source, residence and source income are reported separately, and all unresolved thresholds, reciprocity, credits, or nexus facts are visible.
