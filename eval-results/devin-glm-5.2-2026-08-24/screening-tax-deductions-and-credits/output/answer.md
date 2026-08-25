# HSA Eligibility and Funding Analysis — Chen Family, Tax Year 2026

**Prepared:** 2026-08-24
**Taxpayer:** Lee Chen, age 56 at year-end 2026, family HDHP coverage all of 2026
**Deliverables:** `hsa_eligibility_funding_memo.md`, `hsa_contribution_schedule.xlsx`
**Nature of result:** Planning estimate built from the synthetic client facts in
`source_docs/` and the cited 2026 federal rules. This is **not** a filed tax
result. Open confirmations are listed in Section 7.

---

## 1. Assignment

Determine the Chen family's month-by-month 2026 HSA eligibility, calculate both
the prorated contribution and the optional last-month-rule amount, quantify the
remaining employee funding after the employer's $2,000 contribution, and
evaluate the documented $3,200 dental reimbursement. Distinguish a planning
estimate from a filed tax result, identify assumptions and confirmations still
required (state-law, plan-document, payroll-provider, tax-adviser), and do not
invent facts, guarantees, deductions, or compliance steps.

## 2. Source documents reviewed

All files in `source_docs/` were read and treated as authoritative:

- `client_facts.md` — synthetic Chen family facts.
- `calculation_inputs.csv` — frozen numeric inputs for 2026.
- `official_guidance.md` — Rev. Proc. 2025-19, Pub. 969, IRS Notice 2026-5.

## 3. Governing 2026 federal rules (frozen answer contract)

| Rule | Value | Authority |
|---|---|---|
| 2026 family HSA contribution limit | $8,750 | Rev. Proc. 2025-19 (IRB 2025-21) |
| 2026 family HDHP minimum deductible | $3,400 | Rev. Proc. 2025-19 |
| 2026 family HDHP maximum out-of-pocket | $17,000 | Rev. Proc. 2025-19 |
| Age-55 catch-up | $1,000 | IRC 223(b)(3) |
| General-purpose FSA disqualifies HSA eligibility | — | Pub. 969 |
| Eligibility tested monthly | — | Pub. 969 |
| Last-month rule allows full-year amount; creates testing period | — | Pub. 969 |
| Employer contributions count against annual limit | — | Pub. 969 |
| Testing-period failure → income inclusion + 10% additional tax | — | IRC 223(f)(8); Pub. 969 |
| Review statutory changes affecting HDHP/HSA eligibility | — | IRS Notice 2026-5 (IRB 2026-02) |

## 4. HDHP qualification test

A 2026 family HDHP must have a deductible of at least $3,400 and out-of-pocket
exposure of no more than $17,000.

| Test | 2026 federal limit | Chen plan | Result |
|---|---|---|---|
| Family minimum deductible | $3,400 | $3,600 | PASS — $3,600 ≥ $3,400 |
| Family maximum out-of-pocket | $17,000 | $16,500 | PASS — $16,500 ≤ $17,000 |

**Conclusion:** the Chen plan qualifies as a family HDHP for 2026. Both
thresholds are satisfied with margin.

## 5. Month-by-month HSA eligibility

HSA eligibility is tested monthly (Pub. 969). Coverage by a general-purpose
health FSA is disqualifying "other health coverage" for any month it covers the
individual. The spouse's general-purpose FSA covers Lee January 1 – June 30,
2026, has no grace period or carryover, and ends June 30. No other disqualifying
coverage applies July – December.

| Month | Family HDHP | Disqualifying coverage | HSA-eligible? | Reason |
|---|---|---|---|---|
| Jan 2026 | Yes | Yes — spouse general-purpose FSA | No | General-purpose FSA disqualifies |
| Feb 2026 | Yes | Yes — spouse general-purpose FSA | No | General-purpose FSA disqualifies |
| Mar 2026 | Yes | Yes — spouse general-purpose FSA | No | General-purpose FSA disqualifies |
| Apr 2026 | Yes | Yes — spouse general-purpose FSA | No | General-purpose FSA disqualifies |
| May 2026 | Yes | Yes — spouse general-purpose FSA | No | General-purpose FSA disqualifies |
| Jun 2026 | Yes | Yes — FSA ends 6/30; full month disqualified | No | Full month still has FSA coverage |
| Jul 2026 | Yes | No | Yes | FSA ended; no other disqualifying coverage |
| Aug 2026 | Yes | No | Yes | No disqualifying coverage |
| Sep 2026 | Yes | No | Yes | No disqualifying coverage |
| Oct 2026 | Yes | No | Yes | No disqualifying coverage |
| Nov 2026 | Yes | No | Yes | No disqualifying coverage |
| Dec 2026 | Yes | No | Yes | Eligible first day of last month |

**Eligible months = 6 (July – December 2026).** Lee is HSA-eligible on
December 1, 2026, so the last-month rule is available.

## 6. Contribution calculations

Lee is 56 at year-end 2026, so the age-55 catch-up ($1,000) applies. With family
HDHP coverage, the full annual limit is the family limit plus the catch-up.

### 6.1 Full annual limit

```
Full annual limit = family limit + age-55 catch-up
                 = $8,750 + $1,000
                 = $9,750
```

### 6.2 Prorated contribution (general rule)

```
Prorated = full annual limit × eligible months ÷ 12
         = $9,750 × 6 ÷ 12
         = $4,875
```

This is the safe amount. It carries **no testing-period exposure**.

### 6.3 Last-month rule (full-year contribution)

Because Lee is HSA-eligible on the first day of the last month of the tax year
(12/1/2026), Lee may elect the last-month rule and contribute the **full
$9,750**. The election triggers a **testing period**: Lee must remain
HSA-eligible (covered by an HDHP and free of disqualifying coverage) from
**December 1, 2026 through December 31, 2027**.

### 6.4 Remaining employee funding after employer contribution

Employer HSA contributions ($2,000) count against the annual limit (Pub. 969).

| Method | Total allowed | Less: employer | Remaining employee funding |
|---|---|---|---|
| Prorated (general rule) | $4,875 | $2,000 | **$2,875** |
| Last-month rule (full year) | $9,750 | $2,000 | **$7,750** |

The last-month rule increases the employee's available 2026 funding by
$7,750 − $2,875 = **$4,875**, but only if the testing period is satisfied.

### 6.5 Testing-period failure consequences

If Lee fails the testing period (loses HDHP coverage or gains disqualifying
coverage during 12/1/2026 – 12/31/2027), the excess attributable to the
last-month rule becomes taxable:

```
Income inclusion = full-year amount − prorated amount
                = $9,750 − $4,875
                = $4,875   (added to gross income)

10% additional tax = $4,875 × 10%
                   = $487.50
```

Both are reported on **Form 8889 for 2027** (the year the testing period
ends/fails). The income inclusion and additional tax apply only to the excess
funded under the last-month rule; the prorated amount remains tax-favored.

## 7. Dental reimbursement evaluation

Lee incurred and paid **$3,200** of unreimbursed dental work in September 2026,
after the HSA was established (HSA eligibility began July 2026). No deduction or
other reimbursement is claimed.

| Element | Result | Basis |
|---|---|---|
| Paid after HSA established? | Yes | HSA eligibility began July 2026; client facts state "after the HSA was established" |
| Qualified medical expense under IRC 213(d)? | Yes | Dental care is a 213(d) qualified medical expense |
| Other reimbursement claimed? | No | Client facts |
| **Eligible tax-free HSA distribution** | **$3,200** | Equals the qualified expense paid |

**Conclusion:** Lee may take a tax-free HSA distribution of **$3,200** to
reimburse the September 2026 dental expense, reported on Form 8889 for 2026.
Conditions: (a) the HSA was established before the expense was paid (given);
(b) the expense is a 213(d) qualified medical expense and not purely cosmetic
(to confirm from the invoice — cosmetic procedures are not qualified unless
reconstructive); (c) no other reimbursement was received (given); (d) records
are retained (receipt, proof of payment, no-reimbursement attestation).

**No double benefit rule:** the same dental expense cannot be reimbursed twice
(e.g., paid from the HSA and also reimbursed by the FSA or any other plan), and
it cannot be both reimbursed tax-free from the HSA and claimed as a medical
expense deduction on Schedule A or as a credit. There is **no double benefit**:
an expense reimbursed tax-free through an HSA distribution is treated as paid by
the HSA, not by the taxpayer, and is therefore excluded from the itemized
medical-expense deduction (IRC 213(f); Pub. 502) and from any credit that uses
the same qualifying expense. The client facts confirm no deduction or other
reimbursement is claimed for the $3,200, so the tax-free HSA distribution is the
sole tax treatment for that expense.

This is a planning estimate. The actual distribution is a filed-tax result only
once taken and reported on Form 8889.

## 8. Assumptions

1. The Chen plan is a qualified family HDHP for all of 2026 — supported by the
   deductible ($3,600 ≥ $3,400) and max OOP ($16,500 ≤ $17,000) tests.
2. The spouse's FSA is general-purpose and ends 6/30/2026 with no grace period
   or carryover — per client facts.
3. The HSA account was established by July 2026 — per client facts stating the
   dental expense was paid "after the HSA was established."
4. No other disqualifying coverage applies July – December 2026 — per client
   facts.
5. Lee is age 56 at 12/31/2026, so the age-55 catch-up applies — per client
   facts.
6. Employer HSA contributions total $2,000 — per client facts and
   `calculation_inputs.csv`.
7. The dental work is a qualifying (non-cosmetic) IRC 213(d) expense — inferred
   from "unreimbursed dental work"; to be confirmed from the invoice.

## 9. Evidence gaps and confirmation still required

This planning estimate becomes implementable only after the following are
confirmed. No benefit is claimed until evidence is in hand.

| # | Item | Owner | Why needed |
|---|---|---|---|
| 1 | Plan-document HDHP status and 2026 deductible/OOP figures | Plan administrator | Confirms HDHP qualification and the $3,600 / $16,500 inputs |
| 2 | FSA plan document — general-purpose, ends 6/30/2026, no grace period/carryover, no run-out extending disqualifying coverage | Plan administrator | Confirms July eligibility start and June disqualification |
| 3 | HSA custodian account-opening date and account type (HSA, not HRA/FSA) | HSA custodian | Required for the dental distribution (must be established before payment) |
| 4 | No other disqualifying coverage July – Dec 2026 and through testing period to 12/31/2027 (no Medicare Part A, Tricare, non-HDHP, etc.) | Client / coverage statements | Confirms the 6 eligible months and testing-period maintenance |
| 5 | Date of birth documentation | Client | Confirms age-55 catch-up |
| 6 | W-2 Box 12 code W and payroll-provider coding of the $2,000 employer contribution | Payroll provider | Confirms employer contribution counts against the limit and is reported |
| 7 | Dental invoice describing the procedure | Client / provider | Confirms non-cosmetic 213(d) qualified expense |
| 8 | IRS Notice 2026-5 statutory changes affecting HDHP/HSA eligibility | CPA / tax adviser | Refresh authority before implementation |
| 9 | State HSA conformity (e.g., California and New Jersey do not conform; contributions/earnings may be state-taxable) | State tax adviser | State-law HSA treatment varies; affects state filing |

## 10. Implementation controls

- **Do not exceed the limit.** Total contributions (employer + employee) must not
  exceed the chosen method's cap ($4,875 prorated, or $9,750 last-month rule).
  Excess contributions incur excise tax under IRC 4973 unless withdrawn.
- **Choose the method deliberately.** The prorated method ($4,875) is safe with
  no testing-period risk. The last-month rule ($9,750) adds $4,875 of capacity
  but requires HDHP eligibility through 12/31/2027.
- **Maintain the testing period.** If the last-month rule is elected, calendar
  the 12/1/2026 – 12/31/2027 testing period and avoid disqualifying coverage
  (general-purpose FSA, Medicare Part A, non-HDHP plan, etc.) during it.
- **Substantiate the dental distribution.** Retain the receipt, proof of
  payment, and a no-other-reimbursement attestation; report the $3,200
  distribution on Form 8889 for 2026.
- **Refresh authority.** Review IRS Notice 2026-5 and any later 2026 guidance
  before implementation; confirm state conformity with a state tax adviser.
- **Distinguish estimate from filed result.** These figures are a planning
  estimate. The filed tax result is established only when contributions are made
  and reported on Form 8889 and the return is filed.

## 11. Conclusions

| Question | Answer |
|---|---|
| HDHP qualifies for 2026? | Yes — deductible $3,600 ≥ $3,400; max OOP $16,500 ≤ $17,000 |
| HSA-eligible months in 2026 | 6 (July – December); Jan – Jun disqualified by spouse's general-purpose FSA |
| Full annual limit (family + catch-up) | $9,750 |
| Prorated contribution | $4,875 |
| Last-month-rule contribution | $9,750 (testing period 12/1/2026 – 12/31/2027) |
| Employer contribution | $2,000 (counts against limit) |
| Remaining employee funding — prorated | $2,875 |
| Remaining employee funding — last-month rule | $7,750 |
| Testing-period failure: income inclusion | $4,875 |
| Testing-period failure: 10% additional tax | $487.50 (Form 8889, 2027) |
| Dental reimbursement | $3,200 tax-free HSA distribution available (Form 8889, 2026), subject to recordkeeping and non-cosmetic confirmation |

## 12. Deliverables

- `hsa_eligibility_funding_memo.md` — client-facing planning memo.
- `hsa_contribution_schedule.xlsx` — formula-driven workbook with four sheets:
  `Eligibility`, `Contributions`, `Dental Reimbursement`, and
  `Sources & Assumptions`. Calculation cells preserve live formulas; values were
  verified by recalculation (full annual limit $9,750; prorated $4,875;
  last-month rule $9,750; remaining employee funding $2,875 / $7,750; income
  inclusion $4,875; 10% tax $487.50; dental distribution $3,200; eligible
  months 6).

## 13. Sources

- Rev. Proc. 2025-19 — 2026 HSA figures: https://www.irs.gov/irb/2025-21_IRB
- IRS Publication 969 — HSA eligibility, last-month rule, FSA disqualification,
  employer contributions: https://www.irs.gov/publications/p969
- IRS Notice 2026-5 — statutory changes affecting HDHP/HSA eligibility:
  https://www.irs.gov/irb/2026-02_IRB
- IRC 223 — HSA contribution limits, catch-up, testing-period income inclusion
  and 10% additional tax.
- Form 8889 — HSA contributions and distributions reporting:
  https://www.irs.gov/forms-pubs/about-form-8889
