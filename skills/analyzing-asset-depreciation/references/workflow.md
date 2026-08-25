# Asset depreciation workflow

## Fact record

Capture the asset description, serial or VIN when needed, owner, acquisition date, placed-in-service date, purchase price, taxes, fees, rebates, trade-in, financing, service contracts, improvements, disposition history, prior depreciation, and source page or row for each fact.

## Vehicle use

Calculate:

`qualified business use percentage = qualified business miles / total miles`

Keep commuting outside qualified business miles. Record gaps, duplicate trips, missing dates, and whether the log was contemporaneous. Use the exact authority for investment use and employer use when they apply.

## Decision record

Store these decisions separately:

- basis and business-use basis
- listed-property status
- predominant-business-use threshold
- Section 179 eligibility and limit
- special depreciation allowance eligibility and limit
- GDS or ADS method
- recovery period and convention
- passenger-auto limits or other caps
- recapture risk in later years
- form and software mapping

Each decision needs facts, conclusion, status, authority URL, authority revision, and access date. `unknown` is complete when a required fact or current authority is missing.

## Calculation record

Show basis, business-use percentage, depreciable business basis, rate or table factor, limitation, deduction before limit, deduction after limit, and carryforward. Keep legal eligibility separate from arithmetic.

## Counterfactual

Change one stated assumption, e.g. qualified business use from 30 percent to 100 percent. Hold every other assumption constant unless the rule itself requires a different method. Explain which factors changed and which stayed fixed.
