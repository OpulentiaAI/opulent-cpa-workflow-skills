# Section 280A(g) Home-Rental Arrangement — Complete Analysis

**Matter:** Willow Strategy Inc. (S corporation) rental of owner Taylor's Chicago residence for documented business meetings — Tax Year 2026.
**Deliverables produced:** `augusta_rule_execution_memo.md` (execution memo) and `rental_event_log.xlsx` (event & documentation log with `Sources & Assumptions` sheet).
**Nature of output:** Planning estimate built on synthetic client facts and 2026 federal authority. **Not a filed tax result.** All items in § 7 require confirmation before implementation.

---

## 1. Facts taken as authoritative (`source_docs/`)

- **Renter:** Willow Strategy Inc., an S corporation legally separate from owner Taylor.
- **Lessor:** Taylor; residence in Chicago's West Loop. Taxpayer and residence are **synthetic**; no real address is used.
- **2026 rental use:** Residence is **not otherwise rented** in 2026 (client representation — verify).
- **Planned events:** **14 one-day** leadership and client-planning meetings; each **09:00–17:00**, **8 attendees**, **documented business agenda**.
- **Proposed rate:** **$1,800/day** (client-proposed; **not adopted** — see § 4).
- **Rate evidence:** `calculation_inputs.csv` — five publicly listed Chicago meeting-space **asking** rates retrieved **2026-07-27**. Per the engagement, the **median normalized eight-hour daily rate** is the **frozen planning benchmark**.
- **Committed process controls:** written rental agreement; disinterested corporate action where possible; per-event invoice; payment from the corporate account.
- **Excluded:** no overnight lodging, personal entertainment, or mixed personal events. State/local lodging and sales taxes are **outside** this evaluation.

## 2. Authority applied (2026 federal)

| Authority | Holding applied | URL |
|---|---|---|
| IRC § 280A(g) | Dwelling used as a residence rented **< 15 days** in the year → rental income **excluded from gross income**; **no rental-use deductions** allowed. | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A |
| IRS Pub. 527 | Describes the <15-day rule and reporting treatment for a home used as a residence. | https://www.irs.gov/publications/p527 |
| IRC § 162 | **Company's** deduction is a **separate question**: ordinary and necessary; compensation-like/related-party amounts need particular support for **business purpose** and **reasonableness**. | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162 |

Each source must be refreshed for later-law changes before use for an actual taxpayer.

## 3. Rate support and annual payment

### 3.1 Comparable asking-rate evidence

From `calculation_inputs.csv` (retrieved 2026-07-27):

| ID | Venue / location | Capacity | Normalized 8-hr day rate (USD) |
|---|---|---:|---:|
| CHI-01 | Large Focus Room, Michigan Ave | 8 | 288 |
| CHI-02 | VC Studio, Regus West Loop | 6 | 363 |
| CHI-03 | Small Boardroom, Regus 125 S Wacker | 8 | **385 (median)** |
| CHI-04 | MR-15B, Spaces 1 N State St | 8 | 553 |
| CHI-05 | MR03, Signature 110 N Wacker | 8 | 754 |

Sorted: **288, 363, 385, 553, 754**. Five observations → median is the third value = **$385/day**.

### 3.2 Frozen planning benchmark and annual payment

- **Benchmark daily rate = $385/day** (median of the five normalized asking rates).
- **Annual payment at benchmark = $385 × 14 = $5,390.**
- Reproduced by live workbook formulas: Event Log `K19` (line-total sum) and `Sources & Assumptions!B6` (benchmark × 14). Recalculation confirms: hours/event = 8; total hours = 112; line total/event = $385; annual = $5,390; cumulative days = 14; day-count guard = **PASS**.

### 3.3 Reasonableness test of the proposed $1,800/day rate

| Measure | Value |
|---|---:|
| Proposed daily rate | $1,800 |
| Benchmark daily rate (median) | $385 |
| **Proposed-to-benchmark ratio** | **4.68×** |
| Proposed annual (14 days) | $25,200 |
| Benchmark annual (14 days) | $5,390 |
| **Excess over benchmark (annual)** | **$19,810** |

**Conclusion:** $1,800/day is **not supportable** as an ordinary-and-necessary, reasonable charge for comparable Chicago meeting space (~4.7× the median comparable asking rate). The $19,810 annual excess is at risk of disallowance under § 162 and recharacterization (§ 4.2). **Adopt the $385/day benchmark** (or refreshed quotes obtained near implementation) as the execution rate.

## 4. The two distinct tax analyses

§ 280A(g) and § 162 are **independent**. The owner's exclusion does **not** determine the company's deduction.

### 4.1 Owner (Taylor) — § 280A(g)

- **Day-count test:** 14 rental days < 15 → **exclusion applies.**
- **Income:** Rental payments are **excluded from Taylor's gross income**. The statute has **no dollar cap** — the exclusion turns on the **number of days**, not the rate.
- **Deductions:** **No rental-use deductions.** Depreciation, utilities, insurance, repairs, and cleaning allocable to the 14 rental days are **not deductible** by Taylor. Personal-residence mortgage interest and real-estate taxes remain deductible on Schedule A under the usual limits, unchanged by the rental.
- **Reporting:** Per Pub. 527, no Schedule E is required for the rental activity when the <15-day rule is met; the excluded rental income is not reported as rental income.
- **Cliff risk:** The 15-day limit is a **cliff, not a phase-out**. A **15th rental day** (even partial) **collapses the exclusion for the entire year**: all 2026 rental income becomes taxable on Schedule E, and rental-use deductions (including depreciation) become allowable subject to the § 280A personal-use fraction and passive-activity rules. The cumulative day-count guard in `rental_event_log.xlsx` (cell `B21`) is the control.
- **Substance caveat:** Although § 280A(g) imposes no rate limit, the IRS may challenge a related-party "rental" that lacks business purpose or is a device to shift income. An unreasonable rate undermines substance and feeds the company-side analysis. A market-supported rate protects both sides.

### 4.2 Company (Willow Strategy Inc.) — Section 162 (IRC § 162)

- **Separate question:** The company's deduction is governed by Section 162 (IRC § 162), **not** § 280A(g). Taylor's exclusion does not entitle the S corporation to a deduction.
- **Ordinary and necessary:** Renting meeting space for documented leadership and client-planning meetings is, on its face, ordinary and necessary — **if the charge is reasonable**.
- **Related party / reasonableness:** Taylor is a related party (owner). Related-party and compensation-like amounts receive **particular scrutiny** for business purpose and reasonableness. The **$1,800/day proposed rate fails this test** (4.68× median comparable).
- **Treatment of the excess at the proposed rate:**
  - **Benchmark-supported portion ($5,390/year at $385/day):** deductible as rent, subject to the documentation controls in § 6.
  - **Excess ($19,810/year):** **not deductible as rent.** Likely recharacterizations (to be confirmed by the tax adviser):
    1. **Constructive distribution / dividend** to shareholder Taylor (S-corp distribution treatment; affects basis and any accumulated adjustments account), and/or
    2. **Additional compensation** to Taylor (W-2 wages, subject to payroll/FICA taxes and withholding).
  - Because Willow is an S corporation, any disallowed expense **increases corporate income that flows through to Taylor** on Schedule K-1; the recharacterization determines whether Taylor is taxed once (flow-through) or also via a separate dividend/wage channel.
- **Recommendation:** Operate at the **$385/day benchmark**. At $5,390/year the entire payment sits within market support, the company deduction is defensible under § 162, and the arrangement is far less vulnerable to recharacterization.

### 4.3 Counterfactual (one assumption changed)

Hold all facts constant except the **rental day count**: if a **15th** rental day is added in 2026, the § 280A(g) exclusion is **lost for the entire year**. Taylor would then report **all** 2026 rental income on Schedule E and could claim rental-use deductions (depreciation, utilities, etc.) subject to the § 280A personal-use fraction and passive-activity rules; the company's § 162 rate analysis would be unchanged. This isolates the day-count cliff — not the rate — as the single point of failure on the owner side.

## 5. Conclusions

1. **Owner side (§ 280A(g)):** With 14 rental days (< 15) and no other 2026 rental use, Taylor's rental income is **excluded from gross income** and **no rental-use deductions** are allowed. The exclusion has no dollar cap but is protected only by strict day-count control.
2. **Rate:** The frozen planning benchmark is **$385/day** (median of five comparable asking rates). **Adopt $385/day.** The proposed $1,800/day is **4.68×** the benchmark and is **not supportable**.
3. **Annual payment at the adopted benchmark:** **$5,390** (14 × $385).
4. **Company side (Section 162 / IRC § 162):** At $385/day, the $5,390 annual rent is an ordinary, necessary, and reasonable business expense, deductible by the S corporation subject to documentation. At $1,800/day, **$19,810/year** would be at risk of disallowance and recharacterization as a constructive distribution and/or compensation to Taylor.
5. **Planning estimate vs. filed result:** The $385 benchmark and $5,390 annual figure are a **planning estimate** derived from dated asking-rate evidence. They are **not** a filed tax result. The filed result depends on refreshed comparables, executed agreements, contemporaneous documentation, and CPA sign-off.

## 6. Implementation controls (must be in place before the first meeting)

1. **Written rental agreement** executed before the first meeting — states the $385/day rate, the 14-day 2026 cap, and the business purpose.
2. **Disinterested corporate action** — approval by disinterested directors/shareholders where possible; documented in the corporate record.
3. **Per-event invoice** from Taylor to Willow (`WSI-2026-01` … `WSI-2026-14` in the event log): date, agenda, hours, attendees, day rate.
4. **Payment from the corporate account** to Taylor, matched to each invoice; no commingling.
5. **Contemporaneous event log** — `rental_event_log.xlsx` is the template: date, day of week, start/end, hours (formula), meeting type, documented agenda, attendee count, day rate (linked to the benchmark), line total (formula), invoice number, payment status, documentation status, and a **cumulative rental-day count (formula)**.
6. **Day-count guard** — workbook cell `B21` flags PASS/FAIL against the 15-day cliff; check before scheduling any additional residence use.
7. **Annual rate refresh** — re-pull comparable quotes before each plan year; update the benchmark cell (`Sources & Assumptions!B5`) only with documented, dated evidence.
8. **No personal use** on rental days — no overnight lodging, entertainment, or mixed personal events.
9. **Tax-adviser / CPA sign-off** on rate support, business purpose, reasonableness, and the S-corp flow-through/recharacterization analysis before filing.
10. **Payroll-provider confirmation** if any portion of an above-market rate is ever treated as compensation.

## 7. Evidence gaps and confirmations still required

- **Asking rates, not transactions:** comparables are dated **asking** rates, not completed arm's-length transactions. Refresh and, if possible, obtain executed-transaction evidence near implementation.
- **Comparability adjustments not yet quantified:** CHI-02 seats 6 (vs. 8 attendees); amenities, taxes, booking/service fees, cancellation terms, and exact West-Loop proximity differ across listings.
- **Verify** the residence is not rented through any other channel in 2026 (e.g., personal-platform rentals) — those days count toward the 15-day limit.
- **Confirm** state and local lodging/sales-tax obligations (explicitly outside this evaluation).
- **CPA confirmation** of the S-corp flow-through and any constructive-distribution/compensation treatment if an above-market rate is ever used.
- **Corporate-governance confirmation** that disinterested approval can be and has been documented.
- **Refresh all cited authority** for later-law changes before relying on this workpaper for an actual taxpayer.

## 8. Deliverables

- **`augusta_rule_execution_memo.md`** — execution memorandum containing the facts, authority, rate support, the two distinct tax analyses, the counterfactual, implementation controls, and evidence gaps.
- **`rental_event_log.xlsx`** — two sheets:
  - **Event Log:** 14 documented meetings (2026 dates, all Thursdays) with live formulas for hours (`=(TIMEVALUE(End)-TIMEVALUE(Start))*24`), line totals (`=(Hours/8)*DayRate`), cumulative rental days, a totals row, and a **PASS/FAIL day-count guard** against the 15-day cliff. Day-rate cells link to the benchmark cell on the Sources sheet.
  - **Sources & Assumptions:** the frozen $385 benchmark (with `MEDIAN` formula over the five comparables), the $5,390 annual payment, the 4.68× ratio and $19,810 excess (formulas), the cited authority with URLs, key assumptions, and the evidence-gap list.

*Draft tax workpaper for CPA review. Not a filing position, tax advice, or a guarantee of any tax result. The taxpayer and residence are synthetic.*
