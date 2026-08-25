# Accounts Receivable Reconciliation: Clio vs. QBO
## Sterling, Marsh & Associates LLP - December 31, 2024 (Finalized)

---

## 1. Executive Summary

The December 2024 AR reconciliation between Clio (billing system) and QuickBooks Online (accounting system) **reconciles to zero** after correcting one known subledger posting error. The correct total AR balance per QBO is **$1,729,138.00**, which equals the Clio outstanding balance of **$1,729,138.00**.

The draft reconciliation, the billing supervisor (Rachel Whitfield), and the controller (David Park) each contained errors. Two of the three matter-level variances in the draft are fictitious - created by unnecessary adjustments that were endorsed by both reviewers. The write-down/write-off classification was debated between the reviewers, but neither reviewer's figures are correct. The correct December figures are **write-downs of $125,873.38** and **write-offs of $897.44** (combined total $126,770.82).

---

## 2. Correct Total AR Balance per QBO

### Source comparison

| Source | AR Balance |
|--------|-----------|
| QBO AR Aging Summary (raw, as reported) | $1,729,013.00 |
| QBO General Ledger - Account 1100 ending running balance | $1,729,138.00 |
| Clio billing export - sum of outstanding_balance | $1,729,138.00 |

### Determination

Both Rachel and David correctly identified the AR Aging Summary as the authoritative matter-level source. However, the aging summary contains one known subledger posting error (Bayshore Logistics, see Section 4a below) that understates the aging total by $125.00.

The QBO General Ledger confirms the correct AR balance. The GL account 1100 (Accounts Receivable) ending running balance at December 31, 2024 is **$1,729,138.00**, which exactly matches the Clio outstanding balance. The GL reflects all December 31 postings including the Northbridge IOLTA transfer (JE-OB-000918) and the Stellar Energy IOLTA transfer (JE-OB-000919).

**Correct QBO AR balance = $1,729,013.00 + $125.00 (Bayshore correction) = $1,729,138.00**

### Clio outstanding balance

Sum of `outstanding_balance` across all 243 invoice rows in `clio_billing_export_2024.csv` = **$1,729,138.00**. This figure is confirmed by 32 matters with non-zero balances and 5 matters with zero balances (M-2024-0030, 0031, 0036, 0037, 0038, all fully paid or new matters with no outstanding activity).

### Total-level variance

| Description | Amount |
|-------------|--------|
| Clio Outstanding Balance | $1,729,138.00 |
| QBO AR Balance (Aging, corrected for Bayshore) | $1,729,138.00 |
| **Total-Level Variance** | **$0.00** |

The draft reported a $125.00 total-level variance, which is entirely attributable to the Bayshore subledger error. No unresolved variance remains.

---

## 3. Matter-Level Variance Evaluation

A direct comparison of raw Clio outstanding balances to raw QBO aging balances across all 32 matters with outstanding AR reveals **exactly one variance**: Bayshore Logistics at $125.00. All other matters match to the cent.

### 3a. Bayshore Logistics Corporation (M-2024-0005) - VALID reconciling item

| Field | Value |
|-------|-------|
| Clio outstanding | $23,818.10 |
| QBO Aging | $23,693.10 |
| QBO GL AR (per-matter) | $23,818.10 |
| Variance (Clio - Aging) | $125.00 |

**Assessment: CORRECT.** Both Rachel and David correctly identified this as a known subledger posting error from the November close. The GL AR balance for Bayshore confirms $23,818.10 is the correct figure. The aging subledger is understated by $125.00. IT has an open ticket to correct the aging subledger. This is a valid reconciling item with no impact on the actual AR balance or the GL.

**Correct treatment:** Note as a reconciling item. Correct the aging subledger via IT ticket. No adjustment to the GL or Clio is required.

### 3b. Northbridge Insurance Group (M-2024-0009) - INCORRECT variance in draft

| Field | Value |
|-------|-------|
| Clio outstanding | $22,010.66 |
| QBO Aging (raw) | $22,010.66 |
| Variance (Clio - Aging) | $0.00 |
| Draft's adjusted QBO Aging | $13,237.35 |
| Draft's claimed variance | $8,773.31 |

**Assessment: INCORRECT in draft and in both reviews.** Rachel and David both stated that the December 31 IOLTA trust-to-operating transfer of $8,773.31 (JE-OB-000918) was not yet reflected in the aging, and the draft deducted this amount from the aging to arrive at an adjusted QBO balance of $13,237.35. **This adjustment is wrong. The aging already reflects the transfer.**

**Evidence:**

1. **Raw aging equals Clio for Northbridge.** The QBO AR Aging Summary shows $22,010.66 for Northbridge - identical to the Clio outstanding balance. Clio's data confirms the $8,773.31 payment is already applied: INV-2024-0210 shows `payment_received = $8,773.31` and `outstanding_balance = $7,252.84` (= $16,026.15 - $8,773.31). The total Clio outstanding for Northbridge ($0.00 + $7,252.84 + $14,757.82 = $22,010.66) is the post-transfer balance. The aging shows the same post-transfer balance.

2. **GL AR running balance confirms the aging is correct.** The GL AR ending running balance is $1,729,138.00. The aging total is $1,729,013.00. The difference is exactly $125.00 (the Bayshore error). If the aging had NOT applied the Northbridge credit of $8,773.31, the aging total would be $8,773.31 higher than the GL (minus the $125 Bayshore error), i.e., the aging would be $1,737,786.31 - not $1,729,013.00. The fact that the aging is only $125.00 below the GL proves the Northbridge credit has been applied in the aging.

3. **GL posting detail.** JE-OB-000918 posted on 2024-12-31 with a credit to Accounts Receivable of $8,773.31 (GL running balance after entry: $1,867,072.70). The final AR running balance of $1,729,138.00 includes this credit. The aging subledger, which also totals to $1,729,013.00 (only $125 different from the GL), must also include this credit.

**Correct treatment:** No adjustment needed. Northbridge Clio = QBO Aging = $22,010.66. Variance = $0.00. The draft's deduction of $8,773.31 from the aging is erroneous and creates a false variance.

### 3c. Cascade Foods Holdings Inc. (M-2024-0020) - INCORRECT variance in draft

| Field | Value |
|-------|-------|
| Clio outstanding (raw) | $77,588.63 |
| QBO Aging (raw) | $77,588.63 |
| Variance (Clio - Aging) | $0.00 |
| Draft's adjusted Clio | $84,647.91 |
| Draft's claimed variance | $7,059.28 |

**Assessment: INCORRECT in draft and in both reviews.** Rachel and David both stated that the $7,059.28 year-end write-down on INV-2024-0232 was processed in QBO on December 31 but that the Clio outstanding balance had not yet been updated. The draft added $7,059.28 back to the Clio balance to arrive at an adjusted figure of $84,647.91. **This adjustment is wrong. Clio has already reflected the write-down.**

**Evidence:**

1. **Clio data confirms the write-down is applied.** INV-2024-0232 in the Clio export shows `fees_billed = $55,780.00`, `costs_billed = $380.00`, `write_down_amount = $7,059.28`, `total_invoice = $49,100.72` (= $55,780.00 + $380.00 - $7,059.28), and `outstanding_balance = $49,100.72`. The write-down is already embedded in the total invoice amount and the outstanding balance. The Clio outstanding for Cascade Foods ($77,588.63) is the post-write-down balance.

2. **QBO GL confirms the same treatment.** JE-INV-2024-0232 posts AR debit of $49,100.72 (net of write-down), Fee Revenue credit of $55,780.00, Reimbursed Client Costs credit of $380.00, and Fee Discounts and Write-Downs (account 4900) debit of $7,059.28. The AR booked is $49,100.72, matching Clio exactly.

3. **Aging matches Clio.** The QBO aging shows $77,588.63 for Cascade Foods, identical to the Clio outstanding balance. There is no variance.

**Correct treatment:** No adjustment needed. Cascade Foods Clio = QBO Aging = $77,588.63. Variance = $0.00. The draft's addition of $7,059.28 to the Clio balance is erroneous and creates a false variance.

### 3d. Summary of matter-level variances

| Matter | Client | Draft Variance | Correct Variance | Status |
|--------|--------|---------------|-----------------|--------|
| M-2024-0005 | Bayshore Logistics | $125.00 | $125.00 | Valid reconciling item (subledger error) |
| M-2024-0009 | Northbridge Insurance | $8,773.31 | $0.00 | Draft incorrect - aging already reflects transfer |
| M-2024-0020 | Cascade Foods Holdings | $7,059.28 | $0.00 | Draft incorrect - Clio already reflects write-down |
| All other 29 matters | Various | $0.00 | $0.00 | Matched |

---

## 4. December Write-Down and Write-Off Totals

### 4.1 The debate

**Rachel Whitfield (Billing Supervisor):** Proposed combining all partner-approved fee reductions into a single write-down category per the Q3 2024 firm billing policy. Draft total: write-downs $126,770.82, write-offs $0.00.

**David Park (Controller):** Pushed back, arguing that the Q3 policy only covers partner-negotiated fee adjustments on active matters, not uncollectible balance write-offs. Proposed: write-downs $109,534.63, write-offs $17,236.19.

### 4.2 Assessment of Rachel's position

Rachel's blanket combination is **incorrect**. Write-downs (partner-approved fee reductions on active matters) and write-offs (uncollectible balance removals) serve different accounting and management purposes. Write-downs are a contra-revenue item affecting realization metrics; write-offs may indicate credit risk and collection failure. Combining them obscures both metrics. The controller's pushback on this point is directionally correct.

### 4.3 Assessment of David's position

David correctly identified the need to separate write-downs from write-offs, but his specific figures are **incorrect**. David stated: "The December write-off total should be $17,236.19, and write-downs should be $109,534.63."

The $17,236.19 is the **year-total** write-off amount across all 12 months, not the December write-off total. The four matters David cited have write-offs on invoices dated in March, March, November, November, and December:

| Invoice | Matter | Client | Invoice Date | Write-Off |
|---------|--------|--------|-------------|-----------|
| INV-2024-0012 | M-2024-0003 | Crestwood Capital Partners | 2024-03-12 | $8,284.63 |
| INV-2024-0015 | M-2024-0013 | Pinnacle Therapeutics | 2024-03-13 | $502.84 |
| INV-2024-0168 | M-2024-0007 | Allerton Pharmaceuticals | 2024-11-08 | $7,182.69 |
| INV-2024-0178 | M-2024-0011 | Hartwell Construction | 2024-11-13 | $368.59 |
| INV-2024-0226 | M-2024-0011 | Hartwell Construction | 2024-12-31 | $897.44 |
| **Total (year)** | | | | **$17,236.19** |

Only **$897.44** of write-offs occurred on December-dated invoices (INV-2024-0226, Hartwell Construction, dated 2024-12-31). The remaining $16,338.75 of write-offs occurred on invoices dated in March and November.

David's write-down figure of $109,534.63 is merely the residual of $126,770.82 - $17,236.19, mixing the December combined total with year-total write-offs. This is methodologically inconsistent: you cannot split a December-only combined total using year-total write-off amounts.

### 4.4 Correct December figures

The draft Section C total of $126,770.82 represents the combined write-down and write-off activity on December-dated invoices (INV-2024-0185 through INV-2024-0243). The correct split, derived directly from the Clio billing export `write_down_amount` and `write_off_amount` columns for December-dated invoices:

| Category | Amount | Source |
|----------|--------|--------|
| Write-Downs | $125,873.38 | Sum of `write_down_amount` for 56 December-dated invoices with non-zero write-downs |
| Write-Offs | $897.44 | `write_off_amount` on INV-2024-0226 (Hartwell Construction, M-2024-0011, dated 2024-12-31) |
| **Total** | **$126,770.82** | Matches draft combined total and GL account 4900 December invoice entries |

### 4.5 GL verification

The QBO General Ledger posts all invoice-level write-downs and write-offs to account 4900 (Fee Discounts and Write-Downs), a contra-revenue account. The December invoice-related entries in account 4900 total $126,770.82 (verified by the running balance change from $685,357.62 at November 30 to $812,128.44 after the last December invoice entry), matching the Clio December combined total exactly.

Two additional non-invoice entries were posted to account 4900 in December that should NOT be included in the write-down/write-off totals:

| JE # | Description | Amount | Accounts |
|------|-------------|--------|----------|
| JE-AJE-02 | WIP YE realization haircut 2.5% | $6,125.00 | Dr 4900 / Cr 1200 (Unbilled WIP) |
| JE-AJE-01 | Bad debt reserve - aging-based YE accrual | $221,129.61 | Dr 6990 (Bad Debt Expense) / Cr 1110 (Allowance for Doubtful Accounts) |

JE-AJE-02 is a year-end WIP valuation adjustment with no matter assignment. JE-AJE-01 is a year-end allowance for doubtful accounts accrual posted to Bad Debt Expense and the allowance contra-asset account - it is not an invoice-level write-off and does not reduce AR directly.

### 4.6 Note on the controller's accounting treatment claim

David stated that "uncollectible balance write-offs post to Bad Debt Expense rather than the Fee Revenue contra account." The actual QBO GL does not support this claim for invoice-level write-offs. All four matters with write-offs (Crestwood, Allerton, Hartwell, Pinnacle) have their write-off amounts posted to account 4900 (Fee Discounts and Write-Downs) as part of the invoice journal entries, not to account 6990 (Bad Debt Expense). The only Bad Debt Expense entry in the GL is the year-end reserve accrual (JE-AJE-01). This may indicate a gap between the controller's stated policy and the actual system configuration, which should be addressed as an implementation control item.

---

## 5. Final Reconciliation Result

### 5.1 Reconciliation summary

| Item | Amount |
|------|--------|
| Clio Outstanding Balance (all matters) | $1,729,138.00 |
| QBO AR Balance (per Aging Summary, raw) | $1,729,013.00 |
| Add: Bayshore subledger error correction | $125.00 |
| **QBO AR Balance (corrected)** | **$1,729,138.00** |
| **Total Variance** | **$0.00** |

### 5.2 Reconciling items

| # | Matter | Item | Amount | Resolution |
|---|--------|------|--------|------------|
| 1 | M-2024-0005 | Bayshore Logistics aging subledger posting error | $125.00 | Known IT ticket; GL correct at $23,818.10; no AR impact |

### 5.3 Items removed from the draft (incorrect adjustments)

| # | Matter | Draft Adjustment | Amount | Reason Removed |
|---|--------|-----------------|--------|----------------|
| 1 | M-2024-0009 | Northbridge IOLTA transfer deducted from aging | $8,773.31 | Aging already reflects the transfer; GL AR balance confirms |
| 2 | M-2024-0020 | Cascade Foods write-down added back to Clio | $7,059.28 | Clio already reflects the write-down; GL and Clio data confirm |

### 5.4 Corrected Section D (Reconciliation Conclusion)

| Item | Amount |
|------|--------|
| Total-Level Variance (Clio vs QBO Aging, raw) | $125.00 |
| Less: Bayshore aging subledger error (reconciling item) | ($125.00) |
| Northbridge IOLTA timing difference | $0.00 |
| Cascade Foods write-down timing difference | $0.00 |
| **Net Unresolved Variance** | **$0.00** |
| **Status** | **RECONCILED** |

The draft's reported "Net Unresolved Variance" of $15,832.59 was based on two incorrect adjustments ($8,773.31 + $7,059.28 = $15,832.59) that have been removed.

### 5.5 Corrected December write-down and write-off activity

| Category | Draft Amount | Controller's Amount | Correct Amount |
|----------|-------------|--------------------|--------------------|
| Write-Downs | $126,770.82 | $109,534.63 | $125,873.38 |
| Write-Offs | $0.00 | $17,236.19 | $897.44 |
| Total | $126,770.82 | $126,770.82 | $126,770.82 |

---

## 6. Evidence Gaps

1. **Bayshore subledger error root cause.** The $125.00 Bayshore aging error is attributed to a November close subledger posting error with an open IT ticket. The specific root cause (e.g., a mis-keyed payment, a duplicate entry, or a batch processing error) is not documented in the provided materials. The IT ticket number and resolution timeline should be attached to the audit file.

2. **Q3 2024 billing policy memo.** Rachel and David reference a Q3 2024 firm billing policy memo regarding write-down classification. The actual policy document is not in the provided source files. The policy's exact scope (partner-negotiated fee adjustments vs. all fee reductions) should be verified before finalizing the classification policy.

3. **Aging report generation timestamp.** Rachel states the aging "still shows the pre-transfer balance" for Northbridge, implying the aging was generated before the IOLTA transfer posted. However, the evidence shows the aging reflects the transfer. The exact generation timestamp of the aging report would confirm whether it was produced before or after December 31 close. This gap is moot for the reconciliation result since the GL confirms the balance, but it would explain the reviewers' erroneous assumption.

4. **Clio-to-QBO integration configuration.** The timing of write-down and payment synchronization between Clio and QBO is not documented. Understanding whether Clio pushes updates to QBO in real-time, daily batch, or per-billing-cycle would help explain why the reviewers assumed timing differences that do not actually exist.

5. **Write-off accounting treatment.** The controller states write-offs should post to Bad Debt Expense, but the GL shows all invoice-level write-offs posting to account 4900 (Fee Discounts and Write-Downs). It is unclear whether this is a system configuration issue, a policy that has not been implemented, or a misstatement by the controller. The intended accounting treatment for write-offs should be documented and reconciled to the actual GL postings.

---

## 7. Implementation Controls

1. **Correct the Bayshore aging subledger.** The IT ticket for the $125.00 Bayshore Logistics subledger error should be prioritized and resolved before the January 2025 close. The correction should be tested to ensure it posts correctly without creating a new variance. Document the ticket number, root cause, and resolution in the reconciliation workpaper.

2. **Separate write-down and write-off tracking.** Implement separate tracking and reporting for write-downs (fee reductions on active matters) and write-offs (uncollectible balance removals) in both Clio and QBO. The current QBO GL posts both to account 4900. If the controller's policy is to route write-offs through Bad Debt Expense (6990), the Clio-to-QBO integration mapping must be updated to post write-offs to 6990 and write-downs to 4900. Until this is implemented, the split must be maintained at the reporting level using the Clio source fields.

3. **Reconciliation methodology documentation.** Document the authoritative source hierarchy for the AR reconciliation: (a) AR Aging Summary for matter-level detail, (b) GL account 1100 running balance for total AR validation, (c) Clio billing export for billing-side outstanding balances. Specify that the aging must be reconciled to the GL total as a first step, with any difference investigated before proceeding to matter-level comparisons.

4. **IOLTA transfer cutoff procedures.** Establish a documented cutoff procedure for year-end IOLTA trust-to-operating transfers. All transfers posted on December 31 should be verified to appear in both the GL and the aging subledger before the reconciliation is performed. The Northbridge and Stellar Energy transfers (JE-OB-000918 and JE-OB-000919) both posted correctly to both systems; this procedure should be formalized to prevent future incorrect timing-difference assumptions.

5. **Write-down processing verification.** Before asserting that Clio has not yet reflected a write-down, verify the Clio invoice data by checking that `total_invoice = fees_billed + costs_billed - write_down_amount - write_off_amount`. If the write-down is already embedded in the total invoice amount, no adjustment is needed. The Cascade Foods write-down (INV-2024-0232) was already reflected in Clio's `total_invoice` of $49,100.72.

6. **Reviewer evidence requirements.** Both reviewers (billing supervisor and controller) made incorrect assertions about timing differences without verifying against the primary source data. Implement a requirement that all timing-difference claims must be supported by: (a) the specific GL entry showing the posting, (b) the aging figure showing the pre- or post-posting balance, and (c) the Clio figure showing the corresponding balance. If all three do not support the claimed timing difference, the adjustment must be rejected.

7. **Year-end adjusting journal entry review.** The two year-end AJEs (JE-AJE-01 for bad debt reserve $221,129.61 and JE-AJE-02 for WIP realization haircut $6,125.00) should be reviewed and approved by the controller before posting. These entries should be excluded from the invoice-level write-down/write-off analysis but documented separately in the reconciliation workpaper as non-invoice adjustments to account 4900 and related accounts.

8. **Internal consistency check.** The draft reconciliation had an internal inconsistency: Section A showed raw totals (Clio $1,729,138.00, QBO $1,729,013.00) while the Matter Detail sheet showed adjusted totals (Clio $1,736,197.28, QBO $1,720,239.69) that did not tie to Section A. Implement a check that all sections of the reconciliation must tie to each other before submission for review.

---

## 8. Source Files Referenced

| File | Description | Key Use |
|------|-------------|---------|
| `source_docs/clio_billing_export_2024.csv` | 243 invoice rows, all matters, full year 2024 | Clio outstanding balances, write-down/write-off amounts |
| `source_docs/qbo_ar_aging_summary_2024_12_31.xlsx` | 32 matters with outstanding AR as of 12/31/2024 | QBO AR aging balances by matter |
| `source_docs/qbo_general_ledger_detail_2024.xlsx` | 4,563 GL lines, all accounts, full year 2024 | GL AR running balance, JE-OB-000918, account 4900 entries, Bad Debt Expense |
| `source_docs/Draft_AR_Reconciliation_Clio_QBO_Dec_2024.xlsx` | Draft reconciliation with Sections A-D and Matter Detail | Draft figures and adjustments under review |
| `source_docs/Senior_Review_Notes_Dec_2024.pdf` | Memos from Rachel Whitfield (Jan 6) and David Park (Jan 8) | Reviewer guidance and claims under evaluation |
