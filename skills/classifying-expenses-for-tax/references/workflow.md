# Expense classification workflow

## Intake contract

Capture these facts before mapping a transaction:

- tax year and form revision
- entity and return type
- business activity and locations
- accounting method
- account owner and account purpose
- prior-year category map, if supplied
- business-purpose notes and substantiation

`unknown` is a complete value. Route the row to the exception queue when an unknown fact can change deductibility, allocation, capitalization, or form placement.

## Normalized transaction schema

Preserve `txn_id`, date, raw description, signed amount, currency, account, source file, and source row. Add normalized payee and direction in new columns. Never overwrite the source description.

## Classification record

For each row, record the tax category, destination form and line label, amount, business-use allocation, confidence, status, factual reason, and authority URL.

Use an exception when the description can support more than one treatment. Common reasons include personal versus business use, fixed asset versus current expense, inventory versus supplies, meals versus travel, loan proceeds versus income, transfers, refunds, duplicate entries, and missing business purpose.

## Reconciliation

Prove all of the following:

- normalized row count equals source row count after disclosed exclusions
- each `txn_id` appears once in the classified file
- accepted amount plus exception amount equals the normalized amount
- summary counts and totals equal accepted detail
- every exception has one direct question that could resolve it

## Source precedence

Use the user's facts and CPA-approved prior work for client method. Use the official form and instructions for the stated tax year for current form placement. Use IRS publications for explanation and recordkeeping. Treat vendor case studies and benchmark data as examples, not tax authority.
