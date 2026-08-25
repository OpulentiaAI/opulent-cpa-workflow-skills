# Whitfield settled case — contingency status, journal-entry review, and tax-loss treatment

Sterling, Marsh & Associates LLP — Matter M-2024-0018, Whitfield Family Trust v. Continental Securities
Tax year / fiscal year ended December 31, 2024. Prepared for CPA and counsel review. No deduction is claimed in this workpaper.

## 1. Scope and settled case

Per the assignment, the review is limited to the **settled** contingency matter. The Contingency Case Status Report (as of 12/31/2024) shows three contingency matters; only one is settled:

| Matter | Client | Status | Settled date | Settled gross | Sterling fee | Costs recovered | Net to client | Cost advances outstanding |
|---|---|---|---|---|---|---|---|---|
| M-2024-0016 | Meadowbrook Realty LLC | Active - Discovery | — | $0 | $0 | $0 | $0 | $0 |
| M-2024-0017 | Ferndale Logistics Inc. | Active - Pleadings | — | $0 | $0 | $0 | $0 | $0 |
| **M-2024-0018** | **Whitfield Family Trust** | **Settled** | **2024-12-15** | **$1,800,000** | **$594,000** | **$45,000** | **$1,161,000** | **$0** |

The two active matters (Meadowbrook, Ferndale) have no settlement and, under Sterling's recognition policy, remain off-balance-sheet for revenue; they are out of scope for journal-entry proposals. All analysis below concerns **M-2024-0018 Whitfield**.

## 2. Transaction inventory and posting status

I traced every Whitfield-related line in the QBO Journal Entry Register 2024 (`qbo_journal_entry_register_2024.xlsx`) and cross-referenced the Whitfield Settlement Summary, the Client Cost Advance Ledger, and the Post-Settlement Holdback Memo.

| # | Transaction | Date | Source document | Posted in QBO JE register 2024? | Action |
|---|---|---|---|---|---|
| 1 | Opening cost-advance balance $45,000 on 1300 | 2024-01-01 | JE-2024-OPEN / Cost Advance Ledger | Yes (JE-2024-OPEN) | No proposal |
| 2 | Contract-attorney AP bills (Whitfield matter) — multiple | Apr–Oct 2024 | AP bills in register | Yes (JE-BILL-2024-00322/23/24/30/33/34) | No proposal |
| 3 | AP payments to those contract attorneys | Oct–Nov 2024 | op_bank:ap_payment lines | Yes (JE-OB-000663/691/744) | No proposal |
| 4 | Settlement fee receipt — $594,000 | 2024-12-15 | Settlement Summary; register | **Yes (JE-OB-000842)** | **No proposal** |
| 5 | Cost-reimbursement receipt — $45,000 (clears 1300) | 2024-12-15 | Settlement Summary; register | **Yes (JE-OB-000843)** | **No proposal** |
| 6 | Post-settlement holdback / clawback of excess fee — $29,700 | 2025-01-09 notice; condition originated 2024 | Holdback Memo (Jan 14, 2025) | **No** | **Propose journal entry** |
| 7 | Section 7.4 interest on excess disbursement | accrues from 2024-12-15 once 2025-01-10 grace expired | Holdback Memo | No (2025 event) | Disclose; no 2024 JE |

### 2.1 Already-posted entries — no proposal (per assignment rule)

The original settlement receipt was posted in the register as two bank-transaction JEs that together equal the "Proposed Settlement Journal Entry" in the Whitfield Settlement Summary:

- **JE-OB-000842 (2024-12-15):** Dr 1000 Operating Checking $594,000 / Cr 4200 Contingency Fee Revenue $594,000 — contingency fee disbursement (SET-WFD-2024-12-15-A).
- **JE-OB-000843 (2024-12-15):** Dr 1000 Operating Checking $45,000 / Cr 1300 Client Cost Advances - Hard Costs $45,000 — cost reimbursement (SET-WFD-2024-12-15-B).

Combined effect: Dr 1000 $639,000 / Cr 4200 $594,000 / Cr 1300 $45,000 — identical to the proposed combined entry in the settlement summary. Because these entries are **already in the QBO JE register 2024**, no journal entry is proposed for the original settlement receipt, the cost-advance clearing, or any of the already-posted AP bills/payments.

## 3. The post-settlement holdback (the only unposted item)

### 3.1 Facts from the Holdback Memo (Robert Cavanaugh → James Whitmore, Jan 14, 2025)

- A competing claim was filed by a third-party investor against the same 2021 Continental Securities private-placement proceeds in **late November 2024** (i.e., before the 12/15/2024 disbursement and before the 12/31/2024 balance-sheet date).
- The administrator's pre-disbursement review did not surface it; the 12/15/2024 wires went out without accounting for it.
- On **2025-01-09** the administrator determined **$90,000** of gross proceeds should not have been released and must be returned to escrow pending competing-claimant proceedings, expected **Q1 2025**.
- The administrator's position: the $90,000 reduces the effective gross available for fee calculation; Sterling's fee is recalculated against the adjusted gross; the **excess disbursed to Sterling is its return obligation**.
- The **cost-reimbursement wire (SET-WFD-2024-12-15-B, $45,000) is NOT subject to recall**; the return obligation falls entirely on the fee disbursement.
- Outside counsel: Sterling's return obligation is **not in question** — the legal basis for the clawback is sound and the engagement letter provides no basis to resist.
- **Section 7.4 — Interest on Excess Disbursements:** no interest if the excess is returned by **2025-01-10**; otherwise interest accrues **from 2024-12-15** on the full outstanding balance at **5% per annum, daily**, ceasing when returned in full. **The 2025-01-10 deadline was NOT met.**

### 3.2 Arithmetic (no intermediate rounding)

| Item | Amount |
|---|---|
| Original gross settlement | $1,800,000 |
| Holdback recalled to escrow | $90,000 |
| Adjusted gross available for fee calc | $1,710,000 |
| Original Sterling fee (33% × $1,800,000) | $594,000 |
| Recalculated Sterling fee (33% × $1,710,000) | $564,300 |
| **Sterling excess-fee return obligation (clawback)** | **$29,700** |
| Cost reimbursement (not subject to recall) | $45,000 |
| Original net to client | $1,161,000 |
| Recalculated net to client ($1,710,000 − $564,300 − $45,000) | $1,100,700 |
| Client-attributable share of the $90,000 holdback ($1,161,000 − $1,100,700) | $60,300 |
| Check: $29,700 + $60,300 = $90,000 | ✓ |

Provisional net exposure to Sterling = $29,700 (gross loss $29,700 − reimbursements $0 − other recovery $0). The remaining $60,300 of the $90,000 holdback is the client's reduced-net portion and does not touch Sterling's books.

### 3.3 Interest (Section 7.4) — computed for disclosure; 2025 item

Interest accrues on Sterling's $29,700 outstanding balance at 5%/year, daily, from 2024-12-15 once the 2025-01-10 grace expired:

- As of 2024-12-31 (16 days): $29,700 × 5% × 16/365 = $65.10 → **$0 recognized in 2024** (grace period still open at year-end).
- As of 2025-01-10 (26 days): $29,700 × 5% × 26/365 = $105.78 → $106 (would be owed only because the deadline is missed that day).
- As of 2025-01-14 memo date (30 days): $29,700 × 5% × 30/365 = $122.05 → **$122**.

Interest is a **2025** event (the obligation to pay interest did not exist at 12/31/2024 because Sterling could still have returned the funds by 1/10/2025 to avoid it). No 2024 JE; disclose as a subsequent event and accrue in 2025 once the grace expired and the return date is known.

## 4. Subsequent-event classification (ASC 855)

| Item | Condition existed at 12/31/2024? | Type | 2024 book treatment |
|---|---|---|---|
| $29,700 excess-fee clawback | Yes — competing claim filed late Nov 2024, before settlement and before year-end | Type I (recognized) | **Adjust 2024:** reduce contingency fee revenue and accrue return-obligation liability |
| Section 7.4 interest | No — interest only crystallized when the 1/10/2025 deadline was missed | Type II (non-recognized) | **No 2024 accrual;** disclose; accrue in 2025 |
| $90,000 escrow recovery | Uncertain — pending Q1 2025 proceedings | Contingent recovery | No asset recognized; disclose reasonable prospect of recovery |

## 5. Proposed JE (one journal entry — the only proposal)

**This is one journal entry.** No separate interest entry is proposed for 2024 (Section 7.4 interest is a 2025 Type II subsequent event; see §4 and §8).

**Label:** Proposed JE
**Date:** December 15, 2024 (date of original disbursement / settlement; the condition existed at year-end). Recognized as a Type I subsequent event adjusting the 2024 books.
**Purpose:** True down contingency fee revenue to the recalculated $564,300 and accrue the legally-sound return obligation to the settlement administrator for the $29,700 excess fee, using the live liability account 2050 Accrued Expenses. The $45,000 cost reimbursement is unaffected (not subject to recall). The net-to-client adjustment ($60,300) does not touch Sterling's books.

**Proposed JE — December 15, 2024**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| 2024-12-15 | 4200 Contingency Fee Revenue | $29,700 | |
| 2024-12-15 | 2050 Accrued Expenses | | $29,700 |

**Account verification:** 4200 Contingency Fee Revenue is the live revenue account already credited for the original $594,000 fee in posted entry JE-OB-000842. 2050 Accrued Expenses is the live liability account in the Sterling chart of accounts (it had no 2024 postings in the JE register, which is consistent with recording a newly-recognized accrual at year-end). The earlier generic `2XXX Settlement Clawback Payable` placeholder is withdrawn; the live 2050 account is used instead.

**Why reduce revenue (not a separate expense):** The administrator recalculates the fee against the adjusted gross, so the true fee earned is $564,300. The $29,700 was never earned on the contested $90,000 and is a return of an over-disbursement, not a new expense. An alternative (recording a separate "settlement clawback expense") is acceptable but less faithful; the revenue-reduction treatment is preferred and is flagged for CPA/tax-counsel confirmation.

**Effect on 2024 reported contingency fee revenue:** $594,000 → **$564,300**.

**No separate interest entry for 2024.** Section 7.4 interest (~$122 by the 2025-01-14 memo date) only crystallized when the 2025-01-10 grace deadline was missed; at 12/31/2024 the grace period was still open and no interest obligation existed. Interest is therefore a 2025 event — disclosed here as a subsequent event and to be accrued in 2025 once the return date is fixed. No 2024 journal entry is proposed for interest.

## 6. Tax-loss treatment analysis

The skill framework requires separating arithmetic (done in §3) from legal classification and federal tax treatment. The "unusual loss event" here is the $90,000 holdback / $29,700 excess-fee clawback. The event is a **civil clawback by a court-supervised settlement administrator**, not theft, fraud, a hack, a scam, or a casualty.

### 6.1 Treatment matrix

| Candidate | Status | Reason | Missing fact | Authority |
|---|---|---|---|---|
| Business theft loss | rejected | No criminal conduct or theft allegation; civil clawback confirmed by outside counsel as legally sound | Not applicable — theft not in issue | https://www.irs.gov/publications/p547 |
| Personal casualty or theft | rejected | Business contingency-fee revenue, not personal-use property; no casualty event | — | https://www.irs.gov/publications/p547 |
| Bad debt | rejected | No receivable/debt owed to Sterling; $29,700 is a return of overpaid fee, not an uncollectible debt | — | https://www.irs.gov/publications/p550 |
| Capital loss | rejected | Not from a sale/exchange of a capital asset; it is a fee-revenue adjustment | — | https://www.irs.gov/publications/p544 |
| Revenue adjustment / return of overpayment | supported | $90,000 holdback existed before the 2024 balance-sheet date; true fee = 33% × $1,710,000 = $564,300; $29,700 excess reduces 2024 contingency fee revenue | Tax-year treatment of repayment (2024 accrual reduction vs 2025 IRC 1341 deduction) | https://www.irs.gov/publications/p538 |
| No current loss deduction / recovery pending | review | $90,000 remains in administrator escrow pending Q1 2025 proceedings; reasonable prospect of recovery; no loss recognized until proceedings resolve unfavorably | Outcome of Q1 2025 competing-claimant proceedings | https://www.irs.gov/publications/p547 |

### 6.2 Form map (conditional on a supported/review treatment)

| Candidate | Form | Section / line | Status | Authority |
|---|---|---|---|---|
| Business theft loss | Form 4684 | Section B | rejected | https://www.irs.gov/instructions/i4684 |
| Bad debt | Form 1065 Sch K | Line 12 | rejected | https://www.irs.gov/instructions/i1065 |
| Capital loss | Form 8949 / Sch D | Part I | rejected | https://www.irs.gov/instructions/i8949 |
| Revenue adjustment / return of overpayment | Form 1065 | Line 1b — ordinary income (fee revenue reduction) | supported | https://www.irs.gov/instructions/i1065 |
| No current loss deduction / recovery pending | Form 1065 | Disclosure only | review | https://www.irs.gov/instructions/i1065 |

Because no theft/casualty/bad-debt/capital-loss route is supported, **Form 4684 is not used**. The supported treatment is a fee-revenue adjustment that flows through Sterling's partnership return (Form 1065). The review item (escrow recovery) is disclosure-only until Q1 2025.

### 6.3 Conclusion

- The $29,700 is **not** a deductible theft/casualty/bad-debt/capital loss. It is a **reduction of 2024 contingency fee revenue** (book) and, for tax, either a 2024 accrual-revenue reduction (if the all-events test is met by 12/31/2024) or a 2025 deduction under **IRC §1341** (claim-of-right) when repaid — **reserved for CPA/tax counsel**.
- The $90,000 escrow holdback has a **reasonable prospect of recovery** (Q1 2025 proceedings); no loss is recognized on it now. If the competing claimant ultimately prevails and the $29,700 is not returned, the previously-recorded revenue reduction already reflects that outcome; if the $29,700 is returned, revenue is restored in the year of recovery.
- No federal theft-loss deduction is claimed. This workpaper stops short of filing Form 4684 or any return position.

## 7. Evidence gaps (open items)

| Gap | Document / fact needed | Why needed | Owner | Status |
|---|---|---|---|---|
| Tax-year treatment of the $29,700 repayment | CPA/tax-counsel memo applying the all-events test at 12/31/2024 and IRC §1341 | Determines 2024 revenue reduction vs 2025 deduction | CPA / tax counsel | open |
| Q1 2025 competing-claimant outcome | Administrator final order / court ruling | Determines whether the $90,000 escrow is released back or permanently lost | Partner / outside counsel | open |
| Section 7.4 interest finalization | Administrator interest statement (return date + accrued interest on $29,700) | Determines 2025 interest expense and whether borne by Sterling or passed to client | Controller | open |
| Posted-entry tie-out | QBO confirmation that JE-OB-000842 and JE-OB-000843 are the only Whitfield settlement postings | Confirms original settlement already posted → no duplicate JE proposed | Controller | open |
| Engagement-letter fee basis | Whitfield engagement letter (33% pre-trial contingency; any clawback language) | Confirms recalculated fee of $564,300 and no basis to resist clawback | Partner | open |

## 8. Implementation controls

1. **Prevent double-posting.** The original settlement receipt is already in the register (JE-OB-000842 / JE-OB-000843). Do not re-post the $594,000 fee or the $45,000 cost reimbursement. The only new entry is the $29,700 clawback true-down.
2. **Live liability account.** Credit the live chart-of-accounts liability account **2050 Accrued Expenses** (not a new/generic account). 2050 had no 2024 postings in the JE register, which is expected for a newly-recognized year-end accrual; the countparty detail (settlement administrator) is captured in the JE memo and matter/party tags.
3. **Subsequent-event cutoff.** Book the $29,700 clawback in 2024 (Type I — condition existed at year-end). Do **not** accrue Section 7.4 interest in 2024 (Type II — crystallized 1/10/2025); disclose it in the subsequent-events note and accrue in 2025 once the return date is known.
4. **Two-step recognition.** Record the liability now (revenue true-down); clear the liability against Operating Checking when the wire returns to escrow in 2025; restore revenue (or record recovery income) only if the $29,700 is later returned to Sterling after the Q1 2025 proceedings.
5. **Matter-level tagging.** Tag the clawback JE to Matter M-2024-0018, Class = Litigation, Party = Continental Securities Settlement Administrator, so contingency-case reporting and the 1300 rollforward remain reconciled.
6. **Reconciliation.** After posting, re-tie: (a) 1300 ending balance = $0 (unchanged, cost reimbursement not recalled); (b) 4200 contingency fee revenue = $564,300 for Whitfield; (c) 2050 Accrued Expenses carries the $29,700 return obligation; (d) the Cost Advance Ledger and Whitfield Settlement Summary still reconcile (the $45,000 cost recovery is unaffected).
7. **Segregation of duties.** The proposing partner (Cavanaugh) is the responsible partner on the matter; the controller (Whitmore) should post and an independent reviewer approve, given the partner's involvement in the underlying event.
8. **Documentation.** Retain the 2025-01-09 administrator notice, the executed disbursement instructions, the competing-claimant filing, and outside counsel's conclusion in the matter file to support the recognized subsequent event.
9. **Authority refresh.** IRS sources cited were accessed 2026-08-24 and reflect current published guidance; confirm the 2024-form versions (Form 4684, Form 1065) at filing since this workpaper uses the current-year instructions as the live reference.

## 9. Review items reserved for CPA / counsel

- Whether the all-events test is satisfied at 12/31/2024 such that the $29,700 reduces 2024 accrual revenue, or whether IRC §1341 (claim-of-right) requires/dictates a 2025 deduction upon repayment.
- Whether any portion of the $90,000 holdback is Sterling's loss vs. the client's, and the pass-through treatment to the Whitfield Family Trust (the $60,300 client share is outside Sterling's books but may affect client reporting).
- Final Section 7.4 interest amount and characterization (deductible business interest vs. penalty) once the return date is fixed.
- Whether the engagement letter or settlement agreement contains indemnity or fee-recovery language that could alter the $29,700 obligation.
- State-law characterization is **not** an open theft question here (theft is rejected because the clawback is civil and conceded), so no state-law theft memo is required — but counsel should confirm there is no separate criminal referral.

## 10. Validator

`python3 scripts/validate_loss.py` against the five contract files in `output/` returns:

```
PASS: provisional net loss 29700.00 with 6 candidates
```

Supporting files: `output/event.json`, `output/event_facts.json`, `output/treatment_matrix.csv`, `output/form_map.csv`, `output/evidence_request.csv`.
