# Augusta Rule (IRC § 280A(g)) Execution Memorandum

**To:** Taylor (owner) / Willow Strategy Inc. (S corporation) board file
**From:** Tax workpaper (draft for CPA review)
**Re:** Proposed company rental of owner's residence for documented business meetings — Tax Year 2026
**Date prepared:** August 24, 2026
**Status:** Planning estimate. Not a filed tax result. Confirm all items in § VI before implementation.

---

## I. Facts (from `source_docs/`, authoritative)

- **Renter:** Willow Strategy Inc., an S corporation legally separate from its owner, Taylor.
- **Lessor:** Taylor, owner of a residence in Chicago's West Loop. The taxpayer and residence are **synthetic**; no real address is used.
- **Rental use in 2026:** The residence is **not otherwise rented** during 2026 (client representation — verify before filing).
- **Planned events:** **14 one-day** leadership and client-planning meetings, each **9:00 a.m. – 5:00 p.m.**, **eight attendees**, with a **documented business agenda**.
- **Proposed rate:** **$1,800 per day** (client-proposed; **not adopted** — see § IV).
- **Rate evidence:** `calculation_inputs.csv` contains five publicly listed Chicago meeting-space **asking** rates retrieved **2026-07-27**. Per the engagement letter, the **median normalized eight-hour daily rate** is the **frozen planning benchmark**.
- **Process controls the client has committed to:** written rental agreement; disinterested corporate action where possible; per-event invoice; payment from the corporate account.
- **Excluded uses:** no overnight lodging, no personal entertainment, no mixed personal events. State and local lodging/sales taxes are **outside** this evaluation.

---

## II. Authority applied (2026 federal)

| Authority | Holding applied | URL |
|---|---|---|
| **IRC § 280A(g)** | A dwelling unit used as a residence that is rented for **fewer than 15 days** in the taxable year: rental income is **excluded from gross income** and **no rental-use deductions** are allowed. | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A |
| **IRS Pub. 527** | Describes the <15-day rule and the reporting treatment for a home used as a residence. | https://www.irs.gov/publications/p527 |
| **IRC § 162** | The **company's** deduction is a **separate question**: the expense must be ordinary and necessary; compensation-like or related-party amounts require particular support for **business purpose** and **reasonableness**. | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162 |

Refresh each source for later-law changes before using this workpaper for an actual taxpayer.

---

## III. Rate support and annual payment

### A. Comparable asking-rate evidence (`calculation_inputs.csv`, retrieved 2026-07-27)

| ID | Venue / location | Capacity | Normalized 8-hr day rate |
|---|---|---:|---:|
| CHI-01 | Large Focus Room, Michigan Ave | 8 | $288 |
| CHI-02 | VC Studio, Regus West Loop | 6 | $363 |
| CHI-03 | Small Boardroom, Regus 125 S Wacker | 8 | **$385 — median** |
| CHI-04 | MR-15B, Spaces 1 N State St | 8 | $553 |
| CHI-05 | MR03, Signature 110 N Wacker | 8 | $754 |

Sorted rates: **288, 363, 385, 553, 754**. With five observations the median is the third value = **$385/day**.

### B. Frozen planning benchmark and annual payment

- **Frozen planning benchmark daily rate = $385/day** (median of the five normalized asking rates).
- **Annual payment at benchmark = $385 × 14 days = $5,390.**
- These figures are reproduced by live formulas in `rental_event_log.xlsx` (Event Log `K19` and Sources & Assumptions `B6`).

### C. Reasonableness test of the proposed $1,800/day rate

| Measure | Value |
|---|---:|
| Proposed daily rate | $1,800 |
| Benchmark daily rate (median) | $385 |
| **Proposed-to-benchmark ratio** | **4.68×** |
| Proposed annual (14 days) | $25,200 |
| Benchmark annual (14 days) | $5,390 |
| **Excess over benchmark (annual)** | **$19,810** |

**Conclusion:** The proposed $1,800/day rate is **not supportable** as an ordinary-and-necessary, reasonable rental charge for comparable Chicago meeting space. It is ~4.7× the median comparable asking rate. The $19,810 annual excess is at risk of disallowance under § 162 and recharacterization (see § IV.B). **Adopt the $385/day benchmark** (or refreshed quotes obtained near implementation) as the execution rate.

---

## IV. The two distinct tax analyses

§ 280A(g) and § 162 are **independent** questions. The owner's exclusion does **not** determine the company's deduction.

### A. Owner (Taylor) — § 280A(g) analysis

- **Day-count test:** 14 rental days < 15 → **the § 280A(g) exclusion applies.**
- **Income:** Rental payments received are **excluded from Taylor's gross income**. The statute contains **no dollar cap** on the excluded amount; the exclusion turns on the **number of days**, not the rate.
- **Deductions:** **No rental-use deductions** are allowed. Depreciation, utilities, insurance, repairs, and cleaning allocable to the 14 rental days are **not deductible** by Taylor. (Personal-residence mortgage interest and real-estate taxes remain deductible on Schedule A subject to the usual limits, unchanged by the rental.)
- **Reporting:** Per Pub. 527, no Schedule E is required for the rental activity itself when the <15-day rule is met. The excluded rental income is **not** reported as rental income.
- **Cliff risk:** The 15-day limit is a **cliff, not a phase-out**. A **15th rental day** (even a partial day) **collapses the exclusion for the entire year**: all 2026 rental income becomes taxable on Schedule E, and rental-use deductions (including depreciation) become allowable subject to the § 280A rental-use limitation. The cumulative day-count guard in `rental_event_log.xlsx` (cell `B21`) is the control.

**Caveat on rate and substance:** Although § 280A(g) imposes no rate limit, the IRS may challenge a related-party "rental" that lacks business purpose or is a device to shift income. An unreasonable rate undermines the **substance** of the arrangement and feeds directly into the company-side analysis below. Adopting a market-supported rate protects both sides.

### B. Company (Willow Strategy Inc.) — § 162 analysis

- **Separate question:** The company's deduction is governed by § 162, **not** § 280A(g). Taylor's exclusion does not entitle the S corporation to a deduction.
- **Ordinary and necessary:** Renting meeting space for documented leadership and client-planning meetings is, on its face, an ordinary and necessary business expense — **provided the charge is reasonable**.
- **Related party / reasonableness:** Taylor is a related party (owner). Related-party and compensation-like amounts receive **particular scrutiny** for business purpose and reasonableness. The **$1,800/day proposed rate fails this test** (4.68× median comparable).
- **Treatment of the excess ($19,810/year at the proposed rate):**
  - The **benchmark-supported portion ($5,390/year at $385/day)** is deductible as rent, subject to the documentation controls in § V.
  - The **excess ($19,810/year)** is **not deductible as rent**. Likely recharacterizations, to be confirmed by the tax adviser:
    1. **Constructive distribution / dividend** to shareholder Taylor (S-corp distribution treatment; affects Taylor's basis and any accumulated adjustments account), and/or
    2. **Additional compensation** to Taylor (W-2 wages, subject to payroll/FICA taxes and withholding).
  - Because Willow is an S corporation, any disallowed expense **increases corporate income that flows through to Taylor** on Schedule K-1; the recharacterization determines whether Taylor is taxed once (flow-through) or also via a separate dividend/wage channel.
- **Recommendation:** Operate at the **$385/day benchmark**. At $5,390/year the entire payment sits within market support, the company deduction is defensible under § 162, and the arrangement is far less vulnerable to recharacterization.

### C. Counterfactual (one assumption changed)

Hold all facts constant except the **rental day count**: if a **15th** rental day is added in 2026, the § 280A(g) exclusion is **lost for the entire year**. Taylor would then report **all** 2026 rental income on Schedule E and could claim rental-use deductions (depreciation, utilities, etc.) subject to the § 280A personal-use fraction and the passive-activity rules; the company's § 162 analysis for the rate would be unchanged. This illustrates that the day-count cliff — not the rate — is the single point of failure on the owner side.

---

## V. Implementation controls (must be in place before the first meeting)

1. **Written rental agreement** executed before the first meeting, stating the $385/day rate, the 14-day 2026 cap, and the business purpose.
2. **Disinterested corporate action** — approval by disinterested directors/shareholders where possible; document the approval in the corporate record.
3. **Per-event invoice** from Taylor to Willow (invoice numbers `WSI-2026-01` … `WSI-2026-14` in the event log) showing date, agenda, hours, attendees, and the day rate.
4. **Payment from the corporate account** to Taylor, matched to each invoice; no commingling.
5. **Contemporaneous event log** — `rental_event_log.xlsx` is the template: each event records date, day of week, start/end, hours (formula), meeting type, documented agenda, attendee count, day rate (linked to the benchmark), line total (formula), invoice number, payment status, documentation status, and a **cumulative rental-day count (formula)**.
6. **Day-count guard** — the workbook's `B21` cell flags PASS/FAIL against the 15-day cliff. Monitor before scheduling any additional residence use.
7. **Annual rate refresh** — re-pull comparable quotes before each plan year; update the benchmark cell (`Sources & Assumptions!B5`) only with documented, dated evidence.
8. **No personal use** on rental days — no overnight lodging, entertainment, or mixed personal events (per the client facts).
9. **Tax-adviser / CPA sign-off** on rate support, business purpose, reasonableness, and the S-corp flow-through/recharacterization analysis before filing.
10. **Payroll-provider confirmation** if any portion of an above-market rate is treated as compensation.

---

## VI. Evidence gaps and confirmations still required

- **Comparables are asking rates, not completed arm's-length transactions** — refresh and, if possible, obtain executed-transaction evidence near implementation.
- **Comparability adjustments** not yet quantified: CHI-02 seats 6 (vs. 8 attendees); amenities, taxes, booking/service fees, cancellation terms, and exact West-Loop proximity differ across listings.
- **Verify** the residence is not rented through any other channel in 2026 (e.g., personal-platform rentals), which would count toward the 15-day limit.
- **Confirm** state and local lodging/sales-tax obligations (explicitly outside this evaluation).
- **CPA confirmation** of the S-corp flow-through and any constructive-distribution/compensation treatment if an above-market rate is ever used.
- **Corporate-governance confirmation** that disinterested approval can be and has been documented.
- **Refresh all cited authority** for later-law changes before relying on this workpaper for an actual taxpayer.

---

## VII. Deliverables

- `augusta_rule_execution_memo.md` — this memorandum.
- `rental_event_log.xlsx` — Event Log (14 events, live formulas, day-count guard) + Sources & Assumptions sheet (benchmark, comparables, authority, assumptions, evidence gaps).

---

*Draft tax workpaper for CPA review. Not a filing position, tax advice, or a guarantee of any tax result. The taxpayer and residence are synthetic.*
