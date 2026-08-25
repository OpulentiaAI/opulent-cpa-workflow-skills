---
name: classifying-expenses-for-tax
description: Classifies bank and card transactions into tax categories and exceptions. Use when the user has transaction CSVs, mixed personal and business activity, or needs return-line mapping.
license: LicenseRef-Proprietary
---

# Classifying expenses for tax

Turn raw transaction exports into a traceable first-pass tax workpaper. Finish with every source row accounted for once, every accepted mapping tied to a current authority, and every uncertain item in the exception queue.

## Scope

Produce a CPA review package. The skill ends before filing, posting entries, changing tax software, or sending a client message. Use `building-books-from-bank-data` when the request requires a chart of accounts, journal entries, a general ledger, or a trial balance.

## Workflow

1. Record the tax year, entity type, business activity, accounting method, source files, and any prior-year taxonomy. Mark a missing fact as `unknown`.
2. Normalize the input without changing source values. Assign a stable `txn_id`, preserve the original description and amount, and record the source file and source row.
3. Read `references/workflow.md`. Build the category and form map for the stated tax year from official instructions. Treat line numbers in examples as illustrations until the current form is checked.
4. Classify each row with a category, form, line label, confidence, reason, evidence, and status. Use `accepted` only when the source facts support the mapping. Use `exception` when business purpose, payee, allocation, substantiation, or tax treatment is unresolved.
5. Read `references/example.md` when the input resembles the physician Schedule C fixture or when an output example would resolve format ambiguity.
6. Reconcile row counts and signed amounts to the source. Create the four files in the output contract.
7. Run `python3 scripts/validate_output.py --input <normalized.csv> --classified <classified.csv> --summary <summary.csv> --exceptions <exceptions.csv>`. Resolve every failure before handoff.
8. Review the package against `references/evaluation.md`. State the form revision and access date used for each mapping.

## Output contract

- `classified_transactions.csv` with `txn_id,date,description,amount,category,form,line_label,confidence,status,reason,source_url`.
- `category_summary.csv` with `category,form,line_label,transaction_count,total_amount` for accepted rows.
- `exceptions.csv` with `txn_id,issue,question,amount` for every exception row.
- `workpaper.md` with scope, source reconciliation, methods, assumptions, unresolved items, authority list, and CPA review points.

`confidence` is a decimal from 0 to 1. Confidence records uncertainty. It does not replace evidence.

## Sources and fixtures

Read `references/source-map.md` before using benchmark patterns, synthetic data, or tax authorities. The bundled files under `assets/sample-input/` and `assets/sample-output/` are synthetic and use a 2025 Schedule C example. Copy their structure, then replace their facts and authorities.

When improving this skill from the source package, run the direct APEX client-cost case at `../../environments/classifying-expenses-for-tax/apex-client-cost-classification`. Harbor gives the agent the instruction and source workspace, then loads the rubric and reference answer during verification.

## Completion criteria

The work is complete when the validator exits zero, accepted totals plus exception totals equal the normalized source total, all source rows appear once, every accepted form mapping has a source URL, and the workpaper identifies each `unknown` and CPA decision.
