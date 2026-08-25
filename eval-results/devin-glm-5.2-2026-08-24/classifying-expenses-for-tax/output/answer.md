# December 2024 Client Cost Advance Reconciliation — Whitfield Contingency Matter

**Client / Matter:** Whitfield Family Trust v. Continental Securities, Matter M-2024-0018
**Firm:** Sterling, Marsh & Associates LLP
**Fee structure:** Contingency (33%)
**Responsible partner:** Robert Cavanaugh (EMP-002)
**Period:** Calendar year 2024 (December 15, 2024 settlement close)
**Reconciliation date:** August 24, 2026
**Prepared by:** Devin (CPA review package — pre-filing workpaper)

---

## 1. Scope and objective

Reconcile the client cost advance ledger (workpaper `workpaper_client_cost_advance_ledger_2024.xlsx`) to the QBO general ledger balance for account `acc_000005 / 1300 Client Cost Advances - Hard Costs` for the December 2024 close. Using the cost advance ledger methodology and the Whitfield Contingency Cost Recovery Addendum, verify that:

1. Hard costs that should be treated as client cost advances were **capitalized** to account 1300; and
2. Soft costs were **expensed** (overhead-recovered) and excluded from account 1300.

Identify and quantify any discrepancies in cost classification or capitalization treatment that must be resolved before the 2024 books are closed.

All amounts are rounded to two decimal places only in final presentation; no intermediary values were rounded.

---

## 2. Authority and methodology applied

**Cost advance ledger methodology** (`workpaper_client_cost_advance_ledger_2024.xlsx`, Methodology tab):

- **Hard costs** — "Direct out-of-pocket expenses for the client matter: filing fees, expert witness fees, court reporter and deposition costs, mediation, process server, investigator, travel for the matter, document production from third-party services." Tracked as advances.
- **Soft costs** — "Indirect or overhead-recovered costs: in-house copies, postage, in-house printing, telephone charges. Recovered on invoice as reimbursable charge but not separately tracked as advance."
- **Firm-advanced (contingency matters)** — "For contingency matters where cost recovery occurs at settlement, accumulated advances are held on `acc_000005 / 1300 Client Cost Advances - Hard Costs`. Cleared at settlement against cost reimbursement from settlement administrator or client."

**Whitfield Contingency Cost Recovery Addendum** (`Whitfield_Contingency_Cost_Recovery_Addendum.pdf`, effective March 8, 2023; internal file copy reviewed for December 2024 close):

- Firm-paid reimbursable costs "should be recorded to account 1300 Client Cost Advances Hard Costs and cleared only when the related cost recovery is received."
- Matter-direct professional services are reimbursable client cost advances when firm-paid. Explicit cost-type treatment:

| Cost type | Treatment for Whitfield |
|---|---|
| Contract attorney document review | Reimbursable client cost advance when firm paid |
| Overflow counsel for matter direct litigation work | Reimbursable client cost advance when firm paid |
| Settlement memo and settlement document preparation | Reimbursable client cost advance when firm paid |
| In-house copies, postage, and routine office overhead | Soft cost or overhead recovery, **not account 1300** |

- Controller close note: "confirm account 1300 captures all firm paid reimbursable Whitfield costs before settlement cost recovery is cleared."

These two documents are the governing authority for the capitalization vs. expense test. The addendum controls over the generic ledger methodology for Whitfield-specific cost types.

---

## 3. Reconciliation: cost advance ledger 1300 rollforward to QBO/GL

### 3.1 QBO/GL activity on account 1300 (source: `qbo_general_ledger_detail_2024.xlsx`)

| Date | JE # | Memo | Debit | Credit | Running balance |
|---|---|---|---:|---:|---:|
| 2024-01-01 | JE-2024-OPEN | Opening balance — Whitfield cost advances | 45,000.00 | — | 45,000.00 |
| 2024-12-15 | JE-OB-000843 | Whitfield settlement — litigation cost reimbursement from settlement administrator | — | 45,000.00 | 0.00 |

**QBO/GL ending balance, account 1300, 12/31/2024: $0.00**

### 3.2 Cost advance ledger 1300 rollforward (source: workpaper, "1300 Rollforward" tab)

| Item | Amount |
|---|---:|
| Opening balance Jan 1, 2024 | 45,000.00 |
| 2024 additions (AP bills posted to 1300) | 0.00 |
| Settlement cost recovery — Whitfield (Dec 15, 2024) | (45,000.00) |
| **Ending balance Dec 31, 2024** | **0.00** |

### 3.3 Tie result

| Measure | QBO/GL | Cost ledger | Difference |
|---|---:|---:|---:|
| 1300 opening 1/1/2024 | 45,000.00 | 45,000.00 | 0.00 |
| 1300 additions 2024 | 0.00 | 0.00 | 0.00 |
| 1300 settlement clearing | (45,000.00) | (45,000.00) | 0.00 |
| 1300 ending 12/31/2024 | 0.00 | 0.00 | 0.00 |

**The cost advance ledger reconciles to the QBO/GL for the amounts actually recorded on account 1300.** The numerical tie is clean. The discrepancy described in Section 5 is not a reconciliation difference between the two records — it is a substantive classification/capitalization error in which reimbursable hard costs never reached account 1300 in either system.

### 3.4 Cross-ties to other source records (workpaper "Tie-Out" tab, independently recomputed)

| Source | Source total | Ledger total | Difference | Status |
|---|---:|---:|---:|---|
| IOLTA cost disbursements (trust-paid) — `iolta_bank_transactions.csv` | 29,400.00 | 29,400.00 | 0.00 | Tie (recomputed: 29,400.00) |
| Clio billed costs (per-matter rollup) — `clio_billing_export_2024.csv` | 47,587.09 | 47,587.09 | 0.00 | Tie (recomputed: 47,587.09) |
| Whitfield cost recovery at settlement — `workpaper_whitfield_settlement_summary.xlsx` | 45,000.00 | 45,000.00 | 0.00 | Tie |

Independent recomputation confirms: IOLTA `cost_disbursement` amount_out = 29,400.00; Clio `costs_billed` = 47,587.09. No Whitfield rows appear in either the IOLTA transactions or the Clio billing export — Whitfield had **zero trust-paid costs and zero Clio-billed costs in 2024**. All 2024 Whitfield cost activity flowed through accounts payable / operating cash.

---

## 4. Hard cost capitalization test

### 4.1 Hard costs already capitalized to 1300 (2023 carryover)

The $45,000.00 opening balance is the accumulated 2023 litigation cost advance, recovered at settlement. Per the settlement summary, the categorical breakdown is:

| Category | Amount |
|---|---:|
| Expert witnesses (forensic accounting; securities valuation) | 24,000.00 |
| Court reporter and deposition transcripts | 9,500.00 |
| Mediation fees | 4,500.00 |
| Filing fees, process servers, document production | 4,500.00 |
| Travel and other case costs | 2,500.00 |
| **Total capitalized and recovered** | **45,000.00** |

All five categories are hard costs under the methodology. **No soft costs were capitalized to 1300.** Soft-cost expensing treatment for the opening pool is correct.

### 4.2 2024 Whitfield hard costs that were NOT capitalized to 1300

A matter-tagged search of the QBO/GL (`M-2024-0018`) found six 2024 vendor bills coded to account `5000 Contract Attorney Fees — Matter Direct` (an operating expense) instead of account `1300 Client Cost Advances — Hard Costs`. Each is a matter-direct professional service cost type that the addendum expressly classifies as a reimbursable client cost advance when firm-paid. Each was billed to accounts payable and paid from the operating checking account (firm-advanced, not trust-paid).

| # | Bill date | Bill / JE | Vendor | Cost type (per memo) | Addendum classification | Amount expensed to 5000 |
|---|---|---|---|---|---|---:|
| 1 | 2024-04-30 | BILL-2024-00333 | Westfield Legal Services LLC | Overflow attorney services — Whitfield securities | Overflow counsel → hard cost advance | 4,000.00 |
| 2 | 2024-08-15 | BILL-2024-00322 | Jennifer Kao Law PLLC | Document review — Whitfield securities | Contract attorney document review → hard cost advance | 4,000.00 |
| 3 | 2024-08-31 | BILL-2024-00334 | Westfield Legal Services LLC | Overflow attorney services — Whitfield settlement | Overflow counsel → hard cost advance | 4,000.00 |
| 4 | 2024-09-15 | BILL-2024-00323 | Jennifer Kao Law PLLC | Pre-settlement document review — Whitfield | Contract attorney document review → hard cost advance | 4,000.00 |
| 5 | 2024-09-25 | BILL-2024-00330 | Marcus Avila, Esq. | Settlement memo and supporting brief — Whitfield | Settlement memo preparation → hard cost advance | 3,500.00 |
| 6 | 2024-10-15 | BILL-2024-00324 | Jennifer Kao Law PLLC | Settlement document preparation — Whitfield | Settlement document preparation → hard cost advance | 4,000.00 |
| | | | | | **Total misclassified hard costs** | **23,500.00** |

Calculation: 4,000.00 + 4,000.00 + 4,000.00 + 4,000.00 + 3,500.00 + 4,000.00 = **23,500.00**.

Each of these six cost types is named in the addendum as a reimbursable client cost advance when firm-paid. They were firm-paid (AP → operating cash; confirmed via `op_bank:ap_payment` entries OBT-000285, OBT-000602, OBT-000663, OBT-000691, OBT-000744). They should have been debited to account 1300 and cleared at settlement. Instead they were debited to account 5000 and expensed in 2024.

### 4.3 Corrected 1300 rollforward (as it should have been)

| Item | As recorded | Per addendum (corrected) | Variance |
|---|---:|---:|---:|
| Opening balance Jan 1, 2024 | 45,000.00 | 45,000.00 | 0.00 |
| 2024 additions (firm-paid Whitfield hard costs) | 0.00 | 23,500.00 | (23,500.00) |
| Settlement cost recovery — Whitfield | (45,000.00) | (68,500.00) | 23,500.00 |
| **Ending balance Dec 31, 2024** | **0.00** | **0.00** | **0.00** |

The ending balance is zero under both treatments, but the income-statement and cash-recovery effects differ materially (Section 6).

---

## 5. Soft cost expensing test

- **Soft costs in the 1300 opening pool:** None. The $45,000 opening breakdown consists exclusively of hard-cost categories. Soft costs were correctly excluded from 1300.
- **Soft costs in 2024 Whitfield activity:** No Whitfield-tagged in-house copy, postage, printing, or telephone charges appear in the GL. The addendum's soft-cost category (in-house copies, postage, routine office overhead) was not capitalized to 1300. **Soft-cost expensing treatment is correct for Whitfield.**
- **Secondary classification discrepancy (trust-paid, no 1300 impact):** In the 2024 Activity Detail tab, three disbursements to **Heritage Litigation Support** ("Document production / copies") are labeled **Soft** (CCA-2024-0001 $500.00; CCA-2024-0010 $900.00; CCA-2024-0017 $1,550.00; total 2,950.00). Heritage Litigation Support is a third-party vendor and the methodology defines "document production from third-party services" as a **Hard** cost, reserving "Soft" for *in-house* copies/postage/printing. These should be labeled Hard. Because they were paid from client trust (IOLTA) with no firm advance and no 1300 GL impact, the mislabeling does not affect the 1300 reconciliation, but it is a classification inconsistency that should be corrected in the cost ledger for matter-cost reporting accuracy.

---

## 6. Discrepancies to resolve

### Discrepancy 1 (primary, material): Whitfield firm-paid hard costs expensed instead of capitalized — $23,500.00

- **Nature:** Six 2024 Whitfield matter-direct professional service bills totaling $23,500.00 were coded to operating expense account `5000 Contract Attorney Fees — Matter Direct` rather than capitalized to asset account `1300 Client Cost Advances — Hard Costs`, contrary to the addendum and the contingency-matter methodology.
- **Income-statement impact:** The $23,500.00 was charged to 2024 operating expense. Under the correct treatment it would have been a balance-sheet asset (no P&L effect) until cleared by recovery. 2024 operating income is understated by $23,500.00 relative to policy.
- **Recovery impact:** The settlement administrator remitted only $45,000.00 of litigation cost reimbursement (the amount on the accumulated cost advance ledger / account 1300). The $23,500.00 of 2024 firm-paid hard costs was not on the ledger and was not recovered at settlement. The firm absorbed $23,500.00 of reimbursable client costs that, per the engagement terms, should have been recovered from settlement proceeds.
- **Workpaper narrative error:** The 1300 Rollforward tab states "2024 additions: $0.00 … Late-stage Whitfield activity reflected through trust-funded or settlement-administrator channels." This is incorrect. There is **no** Whitfield IOLTA/trust activity in 2024 (zero rows in `iolta_bank_transactions.csv`), and the late-stage activity was not settlement-administrator-funded — it was firm-paid via AP and expensed to account 5000. The workpaper explanation mischaracterizes the flow and masks the capitalization failure.

### Discrepancy 2 (secondary, classification only, no 1300 impact): Heritage Litigation Support labeled Soft — $2,950.00

- Heritage Litigation Support third-party document production (CCA-2024-0001, -0010, -0017) is labeled Soft in the cost ledger but is Hard under the methodology ("document production from third-party services"). Trust-paid, so no 1300 effect; correct the label for matter-cost reporting.

### Discrepancy 3 (control gap, no quantified amount): Other contingency matters not on 1300

- Per the per-matter summary, Meadowbrook (M-2024-0016) and Ferndale (M-2024-0017) are active contingency matters with matter-level cost activity "tracked off-system" and not reflected as 1300 GL advances. A GL matter-tag search returned **zero** rows for M-2024-0016 and M-2024-0017. Contingency-matter firm-paid hard costs are not being captured on account 1300 firm-wide, indicating the Whitfield error is a systemic coding/control gap rather than an isolated transaction error.

---

## 7. Quantified reconciliation summary

| Reconciliation | Amount |
|---|---:|
| 1300 ending balance per QBO/GL, 12/31/2024 | 0.00 |
| 1300 ending balance per cost ledger, 12/31/2024 | 0.00 |
| Reconciliation difference (ledger vs. GL) | 0.00 |
| Hard costs capitalized to 1300 (2023 carryover, recovered) | 45,000.00 |
| Hard costs that should have been capitalized to 1300 in 2024 but were expensed to 5000 | 23,500.00 |
| Settlement cost recovery actually received | 45,000.00 |
| Settlement cost recovery that should have been requested/received (45,000.00 + 23,500.00) | 68,500.00 |
| Firm-paid reimbursable hard costs not recovered at settlement | 23,500.00 |
| Soft costs incorrectly capitalized to 1300 | 0.00 |
| Soft costs correctly expensed / excluded from 1300 | All Whitfield soft costs (none capitalized) |

---

## 8. Evidence gaps

The following items are not in `source_docs` and would be needed to finalize the CPA review conclusion:

1. **Executed settlement agreement and disbursement instructions.** The settlement summary states these are "retained in the matter file." Needed to confirm whether the $45,000.00 cost reimbursement was a fixed contractual amount (in which case the $23,500.00 may be a permanent firm loss) or whether it was stated as "accumulated cost advances" (in which case an additional $23,500.00 claim may still be recoverable from the client or administrator).
2. **Vendor invoices / matter file support** for the six 5000-coded bills, to confirm each was incurred for matter-direct Whitfield work (vs. general firm capacity) and therefore qualifies as a reimbursable advance under the addendum.
3. **Partner/controller write-off approval.** The addendum permits advances to be cleared only when "approved for write off by the responsible partner and controller." No write-off approval for the $23,500.00 was provided; if none exists, the expensing was not authorized under policy.
4. **Executed (not internal-copy) addendum.** The addendum on file is labeled "internal file copy"; confirm it matches the client-acknowledged engagement terms.
5. **Off-system cost ledgers for M-2024-0016 and M-2024-0017**, to test whether their firm-paid hard costs are likewise missing from account 1300 (see Discrepancy 3).
6. **Heritage Litigation Support vendor file**, to confirm whether its "document production / copies" work is third-party production (Hard) or in-house-style copying (Soft) — affects Discrepancy 2 labeling.

---

## 9. Implementation controls required

To prevent recurrence and to resolve the December 2024 close, the following controls are required:

1. **Matter-type-driven AP coding (system control).** Configure the billing/AP system so that vendor bills tagged to a contingency matter (fee structure = Contingency) and to a matter-direct professional service cost type (overflow counsel, contract attorney document review, settlement memo, settlement document preparation, expert witness, court reporter, mediation, filing fees, process server, investigator, matter travel, third-party document production) auto-default to account 1300, not 5000. Block posting to 5000 for contingency matters without an explicit override reason.
2. **1300 rollforward-to-AP reconciliation (close control).** Each period, reconcile "1300 additions" on the rollforward to a query of AP bills tagged to contingency matters. The current workpaper's $0.00 additions line passed because no such reconciliation was performed; it would have surfaced the six $4,000/$3,500 bills immediately.
3. **Settlement close checklist (close control).** Before a contingency settlement clearing entry is posted, require: (a) 1300 balance equals the accumulated cost advance ledger including current-year firm-paid hard costs; (b) the cost-reimbursement tranche equals that balance; (c) partner and controller signed approval for any cost not recovered (write-off). The Whitfield settlement cleared $45,000.00 against a ledger that should have read $68,500.00 — this control would have caught the $23,500.00 gap pre-clearing.
4. **Workpaper narrative review (documentation control).** The "trust-funded or settlement-administrator channels" explanation in the 1300 rollforward is contradicted by the IOLTA and GL data. Require the preparer to substantiate narrative explanations against source records; reviewer to independently confirm zero IOLTA activity for the matter.
5. **Hard/soft classification reference (classification control).** Codify that third-party document production (e.g., Heritage Litigation Support) is Hard and in-house copies/postage/printing/telephone are Soft. Apply the label consistently in the cost ledger regardless of trust vs. firm funding.
6. **Firm-wide contingency cost capture (scope control).** Extend account 1300 tracking to M-2024-0016 and M-2024-0017 (and any future contingency matter). Matter-level cost tracking that never reaches the GL defeats the cost-advance asset and recovery process.
7. **Correcting entry (remediation).** For 2024, reclassify the $23,500.00 from account 5000 to account 1300 (Dr 1300 / Cr 5000) and assess whether an additional $23,500.00 cost reimbursement can be claimed from the settlement administrator or billed to the client; if unrecoverable, document partner/controller write-off approval and clear 1300 with offsetting credit to a cost-recovery-loss account rather than operating expense.

---

## 10. Conclusion

- **Reconciliation result:** The client cost advance ledger ties to the QBO/GL balance for account 1300 ($0.00 ending balance at 12/31/2024; $0.00 difference). The numerical reconciliation is clean.
- **Hard-cost capitalization:** **Not satisfied.** $23,500.00 of 2024 Whitfield firm-paid hard costs (overflow counsel, contract attorney document review, and settlement memo / settlement document preparation — all expressly designated reimbursable client cost advances in the addendum) were expensed to account 5000 instead of capitalized to account 1300. The $45,000.00 of 2023 carryover hard costs was correctly capitalized and recovered.
- **Soft-cost expensing:** **Satisfied for Whitfield.** No soft costs (in-house copies, postage, office overhead) were capitalized to account 1300. A secondary classification-label discrepancy exists for $2,950.00 of third-party document production labeled Soft (trust-paid, no 1300 impact).
- **Net unresolved discrepancy:** $23,500.00 of reimbursable hard costs were not capitalized and were not recovered at settlement; the workpaper's stated $0.00 2024 additions and its "trust-funded channels" narrative are incorrect. This must be resolved — via a correcting reclassification to 1300, a recovery claim or approved write-off, and the implementation controls in Section 9 — before the December 2024 close is finalized.
