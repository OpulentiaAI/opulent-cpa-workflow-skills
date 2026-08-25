# Evaluation contract

## Blind task prompt

Build draft books from the supplied bank exports and business profile. Produce the chart of accounts, general ledger, trial balance, exception report, and reconciliation workpaper. Trace differences to source rows.

## World design

Use a synthetic company at a fixed period end. Include multiple bank exports, opening balances, invoices, loan documents, a payroll export, and seeded traps such as a duplicate transfer, missing opening balance, fixed asset, owner contribution, and ambiguous payment. Keep the expected ledger and grader outside the agent workspace.

## Binary criteria

1. Every normalized bank row is represented in the ledger.
2. Every journal entry balances to the cent.
3. All ledger accounts exist in the chart of accounts.
4. Bank-account movement ties to source activity and disclosed opening balances.
5. Trial-balance amounts equal balances derived from the ledger.
6. Total trial-balance debits equal total credits.
7. Seeded ambiguous items post to suspense and appear in exceptions.
8. The workpaper traces each remaining difference to an entry or source row.

## Run method

Use a fresh agent, an immutable source directory, and a separate output directory. Run the deterministic validator before qualitative grading. Inspect the trajectory for hidden hard-coded answers, skipped sources, and changes to source files. Repeat three times to test process consistency.
