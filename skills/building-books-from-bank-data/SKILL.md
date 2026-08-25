---
name: building-books-from-bank-data
description: Builds a chart of accounts, ledger, trial balance, and exceptions. Use when a business has no books, bank CSVs must become accounting records, or an imbalance needs tracing.
license: LicenseRef-Proprietary
---

# Building books from bank data

Build review-ready books from raw bank activity. Finish with every source transaction posted once, each journal entry balanced, cash reconciled, and the trial balance tied.

## Scope

Produce draft books and a reconciliation workpaper for CPA review. The skill ends before posting to a live accounting system, issuing financial statements, or filing a return. Use `classifying-expenses-for-tax` when the request only needs tax categories and form mapping.

## Workflow

1. Record the entity, accounting period, accounting method, business activity, bank accounts, opening balances, and source files. Use `unknown` for missing facts.
2. Normalize the bank data. Preserve source descriptions, signed amounts, account names, file names, and row numbers. Assign one stable `txn_id` to each bank row.
3. Read `references/workflow.md`. Draft the smallest chart of accounts that represents the known business and reporting needs. Mark accounts added from assumptions.
4. Post each transaction as a balanced journal entry. Route unresolved treatment to a suspense account and the exception report. Do not hide an unknown inside a confident account name.
5. Reconcile the cash movement in the ledger to the signed bank activity and any supplied opening and ending balances.
6. Derive the trial balance from the ledger. Trace any difference to the exact journal entry or source row before handoff.
7. Read `references/example.md` when the request resembles the grocery fixture or when the ledger format is unclear.
8. Create the five files in the output contract. Run `python3 scripts/validate_books.py --bank <bank.csv> --coa <coa.csv> --ledger <ledger.csv> --trial-balance <tb.csv> --exceptions <exceptions.csv>`.
9. Review the result against `references/evaluation.md` and state every unresolved opening balance, transfer, owner transaction, loan, fixed asset, inventory, payroll, tax, or revenue-recognition issue.

## Output contract

- `chart_of_accounts.csv` with `account_code,account_name,account_type,normal_balance,source`.
- `general_ledger.csv` with `entry_id,txn_id,date,account_code,account_name,debit,credit,memo,source_row,status`.
- `trial_balance.csv` with `account_code,account_name,debit_balance,credit_balance`.
- `exceptions.csv` with `txn_id,account_code,issue,question,amount`.
- `reconciliation.md` with source coverage, cash tie-out, trial-balance tie-out, assumptions, and CPA review points.

## Sources and fixtures

Read `references/source-map.md` before using benchmark or product patterns. The files under `assets/` are a synthetic cash-basis grocery example. They show structure, not a universal chart of accounts.

When improving this skill from the source package, run the direct APEX reconciliation case at `../../environments/building-books-from-bank-data/apex-ar-reconciliation`. The hidden checks require the correct QBO and Clio balances, matter corrections, write-down, write-off, and final tie-out.

## Completion criteria

The work is complete when the validator exits zero, every bank row maps to ledger entries, every entry balances to the cent, every ledger account exists in the chart, cash movement equals signed bank activity, trial-balance balances equal ledger balances, total debits equal total credits, and every suspense posting appears in exceptions.
