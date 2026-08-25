# Books from bank data workflow

## Required facts

Capture the legal entity, reporting period, tax year, accounting method, business activity, bank accounts, opening balances, loan accounts, owner accounts, payroll providers, sales channels, inventory method, and materiality threshold. Ask for prior books when they exist.

## Chart design

Start with accounts required by the known activity. Give each account a stable code, type, and normal balance. Keep assumptions visible in the `source` column. A suspense account is allowed as a temporary control. It must have an exception for each balance.

## Posting rules

- Preserve one `txn_id` across all lines of a journal entry.
- Use a unique `entry_id` for each line.
- Make debits equal credits for each `txn_id`.
- Keep the bank account side consistent with the signed bank amount.
- Record transfers on both accounts when both sides are present and test for duplicates.
- Keep owner contributions, draws, loan proceeds, debt payments, fixed assets, inventory, and refunds separate from operating income and expense.

## Reconciliation order

1. Prove source row coverage.
2. Prove each journal entry balances.
3. Prove bank-account movement equals normalized bank activity.
4. Derive account balances from ledger debits and credits.
5. Prove the trial balance equals those derived balances.
6. Prove total trial-balance debits equal credits.
7. Explain every suspense balance and missing opening balance.

## Source precedence

Use client facts, bank records, contracts, and CPA-approved prior work for the books. Use accounting and tax authorities selected by the CPA for treatment. Vendor examples and benchmark golden outputs show task shape only.
