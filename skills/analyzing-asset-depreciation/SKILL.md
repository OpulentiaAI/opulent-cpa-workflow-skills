---
name: analyzing-asset-depreciation
description: Analyzes asset and vehicle depreciation. Use when the user has purchase records or mileage logs, or needs Section 179, bonus, listed-property, or Form 4562 work.
license: LicenseRef-Proprietary
---

# Analyzing asset depreciation

Turn purchase records and use logs into a transparent depreciation workpaper. Show the facts, threshold test, method, math, form map, and unresolved decisions separately.

## Scope

Produce a draft tax workpaper for CPA review. The skill ends before selecting a code in live tax software, filing a form, or advising the client. Use `writing-client-tax-memos` to turn the approved analysis into client communication.

## Workflow

1. Record the tax year, entity, return, asset owner, business activity, placed-in-service date, purchase documents, use logs, and prior depreciation. Mark missing facts as `unknown`.
2. Read `references/workflow.md`. Extract each basis item with its source location. Separate included basis, excluded amounts, trade-ins, rebates, financing, service contracts, and unresolved items.
3. For a vehicle or other listed property, calculate qualified business use from the complete usage denominator. Keep commuting, personal, investment, and business use separate.
4. Refresh the official authority for the stated tax year using `references/source-map.md`. Apply the predominant-business-use test and record the rule text in your own words with its URL and access date.
5. Determine Section 179, special depreciation allowance, regular MACRS or ADS treatment, recovery period, convention, limits, and recapture exposure. Give each conclusion a status of `supported`, `unsupported`, or `unknown`.
6. Calculate the allowed schedule only from supported parameters. Show every factor and multiplication. Build one counterfactual with its changed assumption stated plainly.
7. Map the result to the exact current form, part, and line label. Record a tax-software choice only when current vendor documentation or CPA-approved instructions support it.
8. Read `references/example.md` when the request resembles the 30 percent vehicle-use fixture.
9. Create the five files in the output contract. Run `python3 scripts/validate_analysis.py --purchase <purchase.json> --usage <usage.csv> --analysis <analysis.json> --schedule <schedule.csv>`.
10. Review the result against `references/evaluation.md`. Route every unsupported legal or software choice to CPA review.

## Output contract

- `asset_facts.json` with extracted facts, source locations, and basis decisions.
- `analysis.json` with use calculation, threshold result, eligibility, method, authority, assumptions, and counterfactual.
- `depreciation_schedule.csv` with `tax_year,basis,business_use_pct,depreciable_basis,rate_or_factor,deduction,method,source_url`.
- `form_map.csv` with `form,part,line_label,value,status,source_url`.
- `workpaper.md` with the calculation, alternatives, missing facts, recapture note, and CPA review points.

## Sources and fixtures

Read `references/source-map.md` before making a tax conclusion. The sample uses `assets/sample-input/purchase.json` and `assets/sample-input/mileage_log.csv`. It applies a synthetic CPA-approved rate only to test arithmetic. It is not a tax rate or filing recommendation.

When improving this skill from the source package, run the property-use method case at `../../environments/analyzing-asset-depreciation/suite-property-use-tax-model`. It tests rate support, use limits, separate tax treatments, source handling, and a document log against the suite answer key.

## Completion criteria

The work is complete when the validator exits zero, basis ties to source items, usage totals reconcile, the threshold result matches the calculated percentage, every legal conclusion has a current official URL, schedule math reproduces exactly, the counterfactual names its changed assumption, and all unknown legal or software choices are visible.
