# Solo 401(k) Contribution Plan — 2026 Analysis

Client: Jordan, owner of Northstar Design (Schedule C sole proprietorship, no
employees). Tax year 2026. This analysis calculates the maximum modeled 2026
one-participant 401(k) contribution, separates the employee, catch-up, and
employer components, and prepares an execution calendar covering plan
documents, deposits, records, and Form 5500-EZ monitoring.

The figures below are a **planning estimate**, not a filed tax result. They
become a filed result only when reflected on the 2026 Form 1040 and supporting
schedules after adviser confirmation.

## Deliverables produced

- `solo_401k_execution_memo.md` — client-facing execution memo with the result,
  rule, calculation, open items, planning note, execution calendar, and Form
  5500-EZ monitoring.
- `solo_401k_contribution_workbook.xlsx` — four-sheet workbook (Inputs,
  Contribution Model, Deadlines, Sources & Assumptions) with live formulas in
  every calculation cell.

## Authority and inputs used

Source documents in `source_docs/` are treated as authoritative:

- `client_facts.md` — synthetic client facts for Northstar Design.
- `calculation_inputs.csv` — deterministic calculation inputs.
- `official_guidance.md` — governing 2026 federal rules and IRS links.

Governing public sources:

- IRS one-participant 401(k) plans guidance:
  https://www.irs.gov/retirement-plans/one-participant-401k-plans
- IRS 2026 COLA dollar limitations:
  https://www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions
- IRS Notice 2025-67 (2026 limits):
  https://www.irs.gov/pub/irs-drop/n-25-67.pdf
- IRS Publication 560 (retirement plans for small business):
  https://www.irs.gov/publications/p560

## Inputs

| Input | Value | Source |
|---|---|---|
| Schedule C net profit (before 1/2 SE tax and plan contribution) | $180,000 | client_facts.md |
| Net earnings factor | 92.35% | calculation_inputs.csv |
| Modeled SE tax rate (combined) | 15.3% | calculation_inputs.csv |
| Outside-plan elective deferral (unrelated employer, 2026) | $10,000 | client_facts.md |
| 2026 regular elective-deferral limit (IRC 402(g)) | $24,500 | official_guidance.md |
| 2026 age-50 catch-up limit (IRC 414(v)) | $8,000 | official_guidance.md |
| Employer (profit-sharing) contribution rate | 20% | client_facts.md |
| 2026 defined-contribution annual addition limit (IRC 415(c)) | $72,000 | official_guidance.md |
| Owner age at year-end 2026 | 54 | client_facts.md |
| Form 5500-EZ asset filing threshold | $250,000 | IRS one-participant 401(k) guidance |

## Calculation

### Step 1 — Net earnings subject to self-employment tax

$180,000 × 92.35% = **$166,230.00**

The 92.35% factor is the net-earnings-from-self-employment factor used in the
evaluation model. It is used only to compute the modeled self-employment tax.

### Step 2 — Modeled self-employment tax

$166,230.00 × 15.3% = **$25,433.19**

The evaluation model applies a combined 15.3% rate and ignores the Social
Security wage-base split. A real filing uses the actual SE tax computation
(12.4% up to the Social Security wage base plus 2.9% Medicare), which can
change this number.

### Step 3 — Deductible half of self-employment tax

$25,433.19 ÷ 2 = **$12,716.60** (unrounded $12,716.595)

One half of SE tax is deductible under IRC 164(f) in computing adjusted gross
income and is subtracted in the adjusted plan compensation calculation.

### Step 4 — Adjusted plan compensation

$180,000.00 − $12,716.60 = **$167,283.40** (unrounded $167,283.405)

Under the supplied deterministic model, adjusted plan compensation is Schedule C
profit minus half of the modeled self-employment tax. The base is the original
$180,000 profit, not the $166,230 net earnings figure. No further circular
reduction is applied.

### Step 5 — Employer (profit-sharing) contribution

20% × $167,283.40 = **$33,456.68** (unrounded $33,456.681)

The 20% rate is applied directly to adjusted plan compensation. There is no
division by 1.20. The supplied model does not use the self-employed circular
reduction; the employer contribution is simply rate × adjusted plan
compensation. (The IRS Publication 560 deduction worksheet for self-employed
individuals uses a circular calculation in an actual filing; confirm with the
CPA which method applies before filing.)

### Step 6 — Employee regular elective deferral remaining

$24,500 − $10,000 = **$14,500.00**

The IRC 402(g) regular elective-deferral limit is a per-individual limit
aggregated across all 401(k)-type plans of all employers in a year. Jordan
already deferred $10,000 into an unrelated employer's 401(k), so $10,000 counts
against the $24,500 regular limit first, leaving $14,500 of regular deferral
room in the solo plan.

### Step 7 — Employee age-50 catch-up

**$8,000.00**

Jordan is age 54 at year-end 2026, so the full 2026 catch-up limit of $8,000 is
available. The outside employer made no catch-up, so the catch-up room is not
reduced. The catch-up is a separate limit from the regular deferral limit.

### Step 8 — Total employee deferral into the solo plan

$14,500.00 + $8,000.00 = **$22,500.00**

### Step 9 — Annual additions tested against the defined-contribution limit

$14,500.00 (regular deferral) + $33,456.68 (employer) = **$47,956.68**

This is below the 2026 IRC 415(c) limit of $72,000, so the plan is within the
limit. Catch-up contributions are excluded from the 415(c) annual addition
limit, so the $8,000 catch-up is added on top and is not tested against
$72,000.

### Step 10 — Total modeled 2026 contribution

$22,500.00 + $33,456.68 = **$55,956.68**

## Contribution components

| Component | Amount |
|---|---|
| Employee regular elective deferral | $14,500.00 |
| Employee age-50 catch-up | $8,000.00 |
| Employer (profit-sharing) contribution | $33,456.68 |
| **Total modeled 2026 contribution** | **$55,956.68** |

Section 415 annual additions excluding catch-up: **$47,956.68** (within the
$72,000 limit).

## Conclusions

1. The maximum modeled 2026 one-participant 401(k) contribution for Jordan is
   **$55,956.68**, split into employee regular deferral ($14,500.00),
   age-50 catch-up ($8,000.00), and employer profit-sharing ($33,456.68).
2. The $10,000 outside-plan deferral reduces only the regular deferral room
   (from $24,500 to $14,500). It does not reduce the catch-up because the
   outside employer made no catch-up.
3. The section 415 annual additions amount excluding catch-up ($47,956.68) is
   below the $72,000 IRC 415(c) limit, so no component is capped by the
   defined-contribution limit.
4. The result is a planning estimate. It becomes a filed tax result only when
   reflected on the 2026 Form 1040 and supporting schedules after the open
   items below are confirmed.

## Evidence gaps and assumptions

The model relies on assumptions that must be confirmed before any filing. No
facts, guarantees, deductions, or compliance steps were invented.

- **Plan-document terms.** The plan must allow elective deferrals, catch-up,
  and a 20% profit-sharing contribution. Confirm available contribution types
  and the adoption deadline with the plan provider or TPA. Elective deferrals
  generally require plan adoption by plan year-end; employer profit-sharing
  contributions can generally be funded by the tax filing deadline including
  extensions. Confirm the exact deadlines with the TPA.
- **Outside deferral detail.** Confirm with the unrelated employer or payroll
  provider that the $10,000 was a regular elective deferral (not designated
  Roth or after-tax) and that no catch-up was made. This controls the remaining
  regular deferral room.
- **State-law, controlled-group, and other-plan-balance facts.** The model
  assumes no other plan balances and no controlled-group or
  affiliated-service-group issue. Confirm with the tax adviser; these can change
  the limits.
- **Self-employment tax model.** The 15.3% combined rate and the ignored Social
  Security wage-base split are an evaluation simplification. A real filing uses
  the actual SE tax computation, which changes the half-of-SE-tax deduction and
  therefore the adjusted plan compensation and employer contribution.
- **Employer contribution method.** The supplied model applies 20% directly to
  adjusted plan compensation (Schedule C profit minus half SE tax) with no
  circular reduction. The IRS Publication 560 deduction worksheet for
  self-employed individuals uses a circular calculation in an actual filing.
  Confirm with the CPA which method applies before filing.
- **2026 limit refresh.** Confirm the 2026 limits against any later IRS guidance
  before filing. The amounts here use the limits supplied for this evaluation.
- **Deposit timing.** Employee elective deferrals must be deposited as soon as
  administratively feasible under DOL rules. Confirm custodian deposit cutoffs
  and election procedures with the plan provider.
- **Form 5500-EZ threshold and due date.** Confirm the $250,000 threshold, the
  due date, and the extension rules for the filing year.

## Implementation controls

### Execution calendar

| Phase | Action | Target date | Owner | Confirmation needed |
|---|---|---|---|---|
| Plan documents | Adopt one-participant 401(k) plan document and adoption agreement | By 12/31/2026 | Plan provider / TPA | Elective deferrals require plan adoption by plan year-end; confirm with TPA |
| Plan documents | Confirm plan allows traditional/Roth deferrals, catch-up, and 20% profit-sharing | At adoption | Plan provider / TPA | Plan-document terms control available contribution types |
| Employee deferral | Set deferral election (regular + catch-up) in writing per plan terms | By 12/31/2026 | Owner / plan provider | Election timing per plan document |
| Employee deferral | Deposit employee deferrals as soon as administratively feasible | Ongoing / by tax deadline | Plan provider / custodian | DOL prompt-deposit rule; confirm custodian cutoffs |
| Employer contribution | Fund employer profit-sharing contribution | By 4/15/2027, or extended 10/15/2027 | Owner / custodian | Employer deadline is the filing deadline including extensions |
| Records | Retain plan document, adoption agreement, election, deposit confirmations, statements | Ongoing (keep 7+ years) | Owner / CPA | Confirm retention policy with adviser |
| Records | Document SE tax and adjusted-plan-compensation calculation workpaper | At tax preparation | CPA | Supports deduction on Schedule 1 / Form 1040 |
| Form 5500-EZ | Monitor total plan assets against $250,000 filing threshold | Each year-end | CPA / plan provider | Confirm threshold and rules for the filing year |
| Form 5500-EZ | If assets reach $250,000, file Form 5500-EZ by 7/31/2027 (extendable to 10/15/2027 via Form 5558) | 7/31/2027 or 10/15/2027 | CPA | Confirm current due date and extension rules |
| Tax filing | Claim deduction: 1/2 SE tax on Schedule 1; deferral + employer deduction on Schedule 1 | With 2026 Form 1040 | CPA | Final amounts are a filed result only when on the return |

### Form 5500-EZ monitoring

A one-participant plan with total assets under $250,000 at year-end generally is
not required to file Form 5500-EZ. Once total plan assets reach $250,000, an
annual Form 5500-EZ filing is generally required. For a 12/31/2026 plan
year-end, the unextended due date is 7/31/2027 (the last day of the seventh
month after the plan year-end); Form 5558 can extend the filing to 10/15/2027.
Controls:

- Track the account balance at each year-end.
- Confirm the current threshold, due date, and extension rules with the CPA for
  the filing year.
- Calendar the Form 5500-EZ due date and the Form 5558 extension deadline when
  the $250,000 threshold is crossed.

### Workbook controls

The workbook `solo_401k_contribution_workbook.xlsx` has four sheets: Inputs,
Contribution Model, Deadlines, and Sources & Assumptions. It preserves formulas
in every calculation cell so changes to the Inputs sheet flow through the
Contribution Model sheet automatically. The Sources & Assumptions sheet
separates approved sources, modeling assumptions, planning-estimate status, and
open items. The workbook was recalculated with LibreOffice and all components
reconcile: employer ($33,456.68) + regular deferral ($14,500.00) + catch-up
($8,000.00) = total ($55,956.68); regular deferral + employer = section 415
amount excluding catch-up ($47,956.68), within the $72,000 limit. Before any
deposit or filing, rerun the workbook with the final 2026 profit figure and the
actual SE tax computation.

## Planning note

If Jordan's 2026 net profit changes, the adjusted plan compensation and the
employer contribution change with it, and the total modeled contribution
changes accordingly. If the outside employer later reports a catch-up or a
different deferral amount, the remaining solo-plan deferral room changes. The
CPA can rerun the workbook with updated inputs before any deposit or filing.
This note is conditional on the facts above and is not a promise of a specific
deduction.

## Sources

- https://www.irs.gov/retirement-plans/one-participant-401k-plans
- https://www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions
- https://www.irs.gov/pub/irs-drop/n-25-67.pdf
- https://www.irs.gov/publications/p560
