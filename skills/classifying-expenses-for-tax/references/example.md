# Worked synthetic example

## Scenario

A physician starts a Schedule C consulting business. The client provides one card export with travel, office purchases, a software charge, groceries, and fuel. The tax year is 2025.

## Method

1. Preserve all six source rows and amounts.
2. Map airfare and the conference hotel to travel because the client note identifies the business event.
3. Map office supplies and the named software subscription using the 2025 Schedule C instructions.
4. Put groceries in exceptions because the record does not establish business purpose.
5. Put fuel in exceptions because the record does not establish the allowed vehicle method, business-use allocation, or substantiation.
6. Reconcile accepted and exception totals to the source total.

## Files

- `assets/sample-input/transactions.csv` is the raw synthetic export.
- `assets/sample-output/classified_transactions.csv` shows row-level decisions.
- `assets/sample-output/category_summary.csv` contains accepted totals.
- `assets/sample-output/exceptions.csv` contains direct follow-up questions.
- `assets/sample-output/workpaper.md` records scope and authority.

The example is a format and reasoning fixture. Recheck the official form for the requested tax year.
