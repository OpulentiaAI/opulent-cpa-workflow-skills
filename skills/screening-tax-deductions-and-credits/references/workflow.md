# Deduction and credit screening workflow

## Coverage families

Select the relevant families from the client facts:

- business expenses, startup costs, home office, vehicles, assets, inventory, payroll, and retirement plans
- self-employed health insurance and health savings accounts
- charitable contributions and gifts
- education, dependents, child care, and family employment
- energy, property, home sale, rental, and casualty matters
- multistate income, foreign activity, pass-through items, and credits for other taxes
- capital gains, losses, carryovers, bad debts, theft, and fraud
- estimated payments, withholding, elections, phaseouts, limitations, and prior-year carryovers

## Opportunity record

For each topic, record the trigger, eligibility elements, facts present, facts missing, interaction risks, current authority, form or schedule, owner, status, and amount only when supported.

## Status rules

- `supported`: all material facts, evidence, authority, and calculation inputs are present.
- `not_supported`: a known fact fails an eligibility element.
- `review`: a material fact, interaction, limit, authority, or calculation is unresolved.
- `not_applicable`: the profile has no trigger after the topic was considered.

## Handoff ownership

Route detailed work to the matching skill when available. Vehicle and asset issues belong to `analyzing-asset-depreciation`. State issues belong to `handling-multistate-income`. Theft and unusual losses belong to `determining-tax-loss-treatment`. Client prose belongs to `writing-client-tax-memos` after CPA approval.
