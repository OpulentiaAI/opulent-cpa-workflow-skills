# Worked synthetic example

## Scenario

A new grocery store provides six bank rows and no accounting file. The rows include an owner contribution, sales deposits, equipment, rent, inventory, and an unexplained payment.

## Result

The sample chart contains cash, inventory, equipment, suspense, owner equity, sales, and rent expense. The unexplained payment posts to suspense and appears in exceptions. The ledger cash movement is $7,350.00. The trial balance has $13,250.00 of debits and credits.

## Files

- `assets/sample-input/bank_transactions.csv`
- `assets/sample-output/chart_of_accounts.csv`
- `assets/sample-output/general_ledger.csv`
- `assets/sample-output/trial_balance.csv`
- `assets/sample-output/exceptions.csv`
- `assets/sample-output/reconciliation.md`

The fixture is intentionally small so the validator logic is easy to inspect. A production run must also reconcile statement opening and ending balances.
