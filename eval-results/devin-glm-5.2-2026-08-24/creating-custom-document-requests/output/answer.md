# Compliant Owner-Child Employment Plan — Analysis

**Client:** Priya Patel, Patel Creative Studio (sole proprietorship)
**Employee:** Arjun, age 15 (Priya's child)
**Tax year:** 2026
**Deliverables:** `child_employment_memo.md`, `child_payroll_schedule.xlsx`
**Status:** Planning estimate — not a filed tax result.

This is the complete analysis required by the assignment. It draws exclusively
on the authoritative client facts in `source_docs/` and the cited 2026 federal
rules, distinguishes planning estimates from filed results, identifies every
assumption and outstanding confirmation, and sets out a documentation-first
implementation plan. No facts, guarantees, deductions, or compliance steps were
invented.

---

## 1. Authoritative facts and inputs

From `source_docs/client_facts.md` and `source_docs/calculation_inputs.csv`:

| Fact | Value |
|---|---|
| Employer entity | Sole proprietorship (no corporation/partnership employs the child) |
| Child | Arjun, age 15, Priya's child |
| Work performed | Product-photography tagging and file organization (real business work) |
| Documented hours (2026) | 160 |
| Comparable hourly rates | $16, $18, $20 |
| Owner proposed budget | $8,000 |
| Arjun other income | None |
| Dependent status | Claimed as a dependent on Priya's return |
| Existing 2026 IRA contribution | None |
| Child-labor lawfulness | Assumed only after counsel/payroll confirmation (unresolved here) |

From `source_docs/official_guidance.md` (the frozen 2026 answer contract):

- **Family employees:** Wages paid by a parent to a child under 18 in the
  parent's sole proprietorship generally are **not** subject to Social Security
  and Medicare (FICA) taxes; wages to a child under 21 generally are **not**
  subject to FUTA. Federal income-tax withholding and reporting rules still
  apply. Entity type matters.
  (IRS, *Family Employees*.)
- **Payroll procedures:** Use current Pub. 15 procedures for withholding forms,
  deposit rules, and Form W-2 reporting. (IRS Publication 15.)
- **2026 dependent standard deduction:** Greater of $1,350 or earned income +
  $450, capped at $16,100. (IRS IRB 2025-45.)
- **2026 IRA/Roth IRA limit:** $7,500 (under 50); single full-contribution MAGI
  threshold < $153,000. (IRS IR-2025-111 / Notice 2025-67 — confirmed via the
  official IRS announcement; not in `source_docs/` but cited here as the
  governing public source for the Roth capacity figure.)

---

## 2. Reasonable wage determination

**Method.** The client facts direct use of the **median** of the three supplied
local comparables for substantially similar entry-level work unless a documented
fact supports otherwise. No such fact is supplied.

**Comparable analysis:**

| Comparable | Rate |
|---|---|
| Rate 1 | $16.00 |
| Rate 2 | $18.00 |
| Rate 3 | $20.00 |
| **Median** | **$18.00** |

**Reasonable wage (planning estimate):**

```
Median rate          $18.00 /hour
Documented hours     160 hours
Reasonable wages     160 × $18 = $2,880
```

**Owner budget test.** The proposed $8,000 budget implies $8,000 ÷ 160 =
**$50.00/hour** — roughly 2.8× the median comparable. Paying $50/hour for
entry-level tagging and file-organization work would not be defensible as
reasonable compensation for the services actually rendered and would create
reclassification and Schedule C deduction-disallowance risk. Wages must reflect
**actual services** at a comparable market rate. The $8,000 budget is therefore
**not** the wage figure; the reasonable wage is **$2,880**. The excess of the
budget over reasonable wages is $8,000 − $2,880 = $5,120, which is not payable
as wages for the documented work.

> **Planning estimate vs. filed result.** $2,880 is a planning estimate derived
> from the supplied comparables and the 160 documented hours. The filed Schedule
> C wage deduction and Arjun's Form W-2 will reflect the hours actually worked
> and paid during 2026, supported by contemporaneous timesheets.

---

## 3. Federal payroll tax classification

Arjun is under 18, is Priya's child, and works in Priya's sole proprietorship.
Applying the family-employee rules:

| Payroll tax | Applies? | Basis |
|---|---|---|
| Social Security — employer 6.2% | **Exempt** | Child under 18, sole proprietorship |
| Social Security — employee 6.2% | **Exempt** | Child under 18, sole proprietorship |
| Medicare — employer 1.45% | **Exempt** | Child under 18, sole proprietorship |
| Medicare — employee 1.45% | **Exempt** | Child under 18, sole proprietorship |
| FUTA (federal unemployment) | **Exempt** | Child under 21 |
| Federal income tax withholding | **Applies** | Not exempted for family employees |
| Form W-2 reporting | **Required** | Annual wage reporting required |

**Employer impact.** Because FICA is exempt, Priya pays no employer Social
Security or Medicare tax and remits no employee FICA. Because FUTA is exempt, no
federal unemployment tax applies. Total federal payroll tax remitted on
Arjun's wages = **$0**. The $2,880 wages remain a deductible Schedule C business
expense (ordinary and necessary compensation for services actually rendered),
subject to the reasonableness standard in Section 2.

**Entity-type caveat.** The FICA exemption applies **only** because the employer
is the parent's sole proprietorship. It would **not** apply if the employer were
a corporation, or a partnership unless every partner is a parent of the child.
The facts confirm a sole proprietorship, so the exemption holds.

**Trade-off.** FICA exemption means Arjun earns **no Social Security work
credits** from this employment — a known consequence that should be communicated
to the client.

---

## 4. Arjun's federal income-tax position (2026)

Arjun has $2,880 of wage income, no other income, and is a dependent.

**2026 dependent standard deduction:**

```
Earned income                       $2,880
Earned income + $450                $3,330
Floor                               $1,350
Greater of floor or (EI + $450)     $3,330
Cap                                 $16,100
Standard deduction (≤ cap)          $3,330
```

**Taxable income and tax:**

```
Wage income (AGI)                   $2,880
Standard deduction                  $3,330
Taxable income (not below 0)        $0
Federal income tax                  $0
```

Because the $3,330 standard deduction exceeds the $2,880 of wages, Arjun's
taxable income is $0 and his 2026 federal income tax is **$0**.

**Withholding posture.** Although the liability is $0, federal income-tax
withholding and reporting rules still apply. Arjun may claim **exempt** from
federal income tax withholding on Form W-4 if he had no federal income tax
liability for 2025 and expects none for 2026 — conditions the facts support.
Even if exempt is claimed, the W-4 must be collected and retained, and a Form
W-2 must still be issued for 2026.

---

## 5. Roth IRA contribution capacity (2026)

A Roth IRA contribution is limited to the **lesser of earned income or the 2026
statutory limit ($7,500)**, subject to MAGI phase-outs.

```
Arjun earned income (wages)         $2,880
2026 Roth statutory limit (under 50) $7,500
MAGI (single, = wages)              $2,880
2026 single full-contribution cap   $153,000
Phase-out applies?                  No (MAGI far below threshold)
Roth IRA contribution capacity      lesser of $2,880 or $7,500 = $2,880
```

Because Arjun's earned income ($2,880) is below the $7,500 statutory limit and
his MAGI is far below the phase-out, his full wages can be contributed to a Roth
IRA for 2026, up to **$2,880**. He has no existing 2026 IRA contribution, so
the full capacity is available. The contribution deadline is the 2026 federal
tax filing deadline in 2027.

> **Planning estimate.** The $2,880 capacity depends on (a) the wages actually
> paid and reported on Arjun's 2026 Form W-2, and (b) custodian plan-document
> eligibility for a minor (see Section 7, evidence gap 5).

---

## 6. Documentation-first implementation plan

The plan is **documentation-first**: establish the supporting records before, or
contemporaneously with, paying wages, so the arrangement is defensible if
examined. This approach mirrors the records needed to substantiate the facts
(job description, timesheets, rate support, payroll records, labor-law
clearance, and retention controls).

### 6.1 Pre-employment records (before first paycheck)

1. **Written job description** — Define Arjun's duties (product-photography
   tagging, file organization), the age-appropriate scope, and that the work is
   real and necessary to the business (not personal/household labor).
2. **Rate support memorandum** — Document the three comparables ($16, $18, $20),
   the median selection ($18), and the basis for the rate; retain the source of
   each comparable.
3. **Child-labor law confirmation** — Obtain counsel/payroll-provider
   confirmation that the hours, times, and tasks are lawful for a 15-year-old
   under applicable federal and state child-labor rules (work-hour and
   hazardous-occupation restrictions). **Do not begin work until cleared.**
4. **Form W-4** — Collect Arjun's Form W-4 (claim exempt if the Section 4
   conditions are met). Retain on file.
5. **Payroll-provider setup** — Confirm the sole-proprietorship / parent-
   employer / under-18 FICA exemption and under-21 FUTA exemption are correctly
   configured, and that federal income tax withholding and W-2 reporting are
   enabled.

### 6.2 Contemporaneous records (during 2026)

6. **Timesheets** — Record each session: date, start/stop times, task, and
   hours. The 160 documented hours must be substantiated by contemporaneous
   entries signed/initialed by Priya.
7. **Payroll records** — Process wages through the payroll system at $18/hour
   against actual hours, with pay stubs reflecting gross wages, $0 FICA, and
   federal income tax withholding status.
8. **Payment trail** — Pay wages to an account in Arjun's name (not commingled
   with household funds) so the payment is traceable.

### 6.3 Year-end and retention records

9. **Form W-2** — Issue Arjun a 2026 Form W-2 showing wages (actual paid
   amount), with FICA/FUTA boxes reflecting the exemptions. File per Pub. 15
   deadlines.
10. **Schedule C wage deduction** — Report wages paid as a Schedule C business
    expense, supported by timesheets, the rate memorandum, and the W-2.
11. **Roth IRA establishment and contribution** — Open a Roth IRA for Arjun with
    a custodian that accepts minor accounts (custodial/guardian IRA), confirm
    plan-document eligibility, and contribute up to the lesser of earned income
    or $7,500 (= $2,880) by the 2026 tax filing deadline.
12. **Retention** — Retain the job description, rate memorandum, timesheets, pay
    stubs, W-4, W-2, and child-labor clearance for the federal recordkeeping
    period (generally at least 4 years for employment tax records; follow the
    tax adviser's retention guidance).

---

## 7. Evidence gaps and confirmations required

This evaluation is a **planning estimate**, not a filed result. The following
must be confirmed before implementation:

| # | Item | Why it matters |
|---|---|---|
| 1 | State child-labor law clearance | Facts assume lawfulness "only after counsel/payroll confirmation." Federal FICA/FUTA exemptions do not authorize unlawful child labor. |
| 2 | Payroll-provider exemption configuration | Confirm FICA (under 18) and FUTA (under 21) exemptions are set correctly and FIT withholding/W-2 are enabled. |
| 3 | Actual hours worked and paid | Filed wage deduction and W-2 reflect actual paid hours, not the 160-hour estimate. |
| 4 | Comparable sources | Document the origin of each $16/$18/$20 comparable so the $18 median is substantiable. |
| 5 | Roth IRA custodian plan-document eligibility for a minor | Some custodians require a guardian/custodial IRA; confirm account type and mechanics. |
| 6 | 2026 Roth IRA limit confirmation | $7,500 per IRS IR-2025-111 / Notice 2025-67; confirm no later adjustment before contributing. |
| 7 | Tax-adviser review of the full arrangement | Confirm reasonableness, Schedule C treatment, and any state obligations. |
| 8 | State payroll and income tax | This analysis is federal-only; state withholding, unemployment, and income-tax rules are not analyzed. |
| 9 | Later-law changes | Official guidance directs confirmation of later-law changes before use for an actual taxpayer. |

---

## 8. Summary of conclusions (planning estimates)

| Question | Conclusion |
|---|---|
| Reasonable 2026 wage | **$2,880** (160 h × $18 median comparable) |
| Owner $8,000 budget | Not used — implies $50/h, unreasonable for the work |
| FICA (Social Security + Medicare) | **Exempt** (child under 18, sole proprietorship) |
| FUTA | **Exempt** (child under 21) |
| Federal income tax withholding | **Applies**; Arjun likely claims exempt on W-4 |
| Form W-2 | **Required** |
| Total federal payroll tax remitted | **$0** (all exempt; FIT expected $0 if W-4 exempt) |
| Arjun 2026 taxable income | **$0** (wages $2,880 < $3,330 standard deduction) |
| Arjun 2026 federal income tax | **$0** |
| Roth IRA capacity (2026) | **$2,880** (earned income below $7,500 limit) |
| Documentation-first plan | Section 6 — establish records before/with pay |

All figures are planning estimates pending the confirmations in Section 7 and
the actual hours paid during 2026.

---

## 9. Deliverables produced

- `child_employment_memo.md` — the client-facing compliance memorandum with the
  full analysis, calculations, conclusions, evidence gaps, and implementation
  controls.
- `child_payroll_schedule.xlsx` — a six-sheet workbook (`Inputs`, `Wage
  Calculation`, `Payroll Taxes`, `Income Tax & Roth`, `Payroll Schedule`,
  `Sources & Assumptions`) with **live formulas preserved** in all calculation
  cells and a dedicated `Sources & Assumptions` sheet documenting every source,
  assumption, evidence gap, and disclaimer. Formula results were verified by
  recalculation: reasonable wages = $2,880; taxable income = $0; federal income
  tax = $0; total payroll tax = $0; Roth capacity = $2,880.
