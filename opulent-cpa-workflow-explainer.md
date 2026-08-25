# CPA Workflow Automation — Problem Set & Configuration Brief for Opulent

**From:** Randy Keller & Amir Curry, Ashland Taylor Consulting LLC
**For:** Jeremy (Opulent)
**Date:** August 17, 2026
**Source material:** Working sessions with Waqas Akhtar, CPA (WNA CPA) — Aug 9 and Aug 16, 2026

---

## 1. Why this document exists

We've spent the last two weeks in working sessions with a practicing CPA (Waqas, WNA CPA) walking through his actual client engagements step by step. This doc distills that into (a) the shape of the problems we want the Opulent system optimized for, (b) the specific workflows to automate with **expected inputs mapped to expected outputs**, and (c) what we need from you: configurations, synthetic example data, and demo material showing the agent doing the tedious work.

**The scope decision, up front:** a CPA engagement runs from client discovery through filing, but we have deliberately focused this effort on the **back half — the execution work** (categorization, reconciliation, building the books and schedules, analysis, and form mapping). That's where the hours go, that's what burns practitioners out, and that's what no existing tool actually does. Everything in this doc should be read through that lens.

The strategic frame: this is an **agentic operating system for tax and accounting professionals**, not another SaaS portal. Tools like TaxDome give CPAs a client portal; QuickBooks gives them a data dump. Nothing on the market actually *does the work* — the reconciliation, categorization, calculation, and form-mapping that consumes most of a CPA's billable hours. That's the blue ocean. Roughly 70–80% of tax professionals aren't using AI tooling in their workflow at all today, and the small/mid-market business segment (a market the big firms' service models don't reach) is underserved.

The differentiating mechanic: **the platform learns each CPA's style from their past work product.** A CPA onboards by dumping prior engagements (redacted/sanitized), and the system extracts their methodology — how they categorize, what they request, how they document — and replicates it. One CPA described it as: show it once how you do the work, and it does it that way every time.

---

## 2. Background: how CPA engagement work actually flows

For context beyond what any one CPA names, here's the general shape of small-firm tax/accounting work. A typical engagement runs:

1. **Discovery** — client interview, fact gathering. Entity type, income sources, expenditures, life/business events for the year.
2. **Document request** — customized checklist (W-2s, 1099s, K-1s, bank statements, purchase agreements, mileage logs, retirement statements...). Highly client-specific: a client with a self-directed 401(k) triggers requests a generic checklist never would.
3. **Intake** — receiving a messy pile: CSVs, PDFs, photos of receipts, purchase agreements, "here's all I have, do what you gotta do."
4. **Organization/extraction** — pulling usable data out of that pile.
5. **Itemization/categorization** — classifying every transaction into tax-meaningful buckets (travel vs. equipment vs. office expense vs. meals — each treated differently on the return).
6. **Reconciliation** — making the numbers tie out. Debits = credits, statements match ledgers, nothing double-counted or missing.
7. **Build** — constructing the actual accounting artifacts: chart of accounts, general ledger, trial balance, depreciation schedules, workpapers.
8. **Analysis** — applying tax law to the organized facts: eligibility tests (e.g., business-use thresholds), deduction optimization, multi-state allocation, choosing depreciation methods.
9. **Mapping & filing** — putting the results on the right form and line (Schedule C line items, Form 4562 depreciation, Form 1065 + K-1s), selecting the right options in tax software (Waqas uses **Drake**), and producing client-facing explanations of the outcome.

**Where the platform lives: steps 6–9. This is the scope.** We aligned on this explicitly: steps 1–5 (discovery, requests, intake, organization) have value, but existing tooling partially covers them, and frankly they're the relationship-driven part CPAs don't mind doing. Steps 6–9 are, in Amir's words, "the actual work we get paid for" — the tedious, high-pressure grind that drives people out of the profession. Reconcile, build, analyze, map: that is the automation target and where every configuration and demo should concentrate. The front-of-funnel steps come back later as a lighter-touch assist (noted as Workflow F below for completeness), but they are not the current build.

A second general truth worth designing around: **many small-business clients have no books at all.** No QuickBooks, no bookkeeper — just bank-statement CSVs. The CPA ends up doing write-up work (building books from raw transactions) before tax work can even start. That "books-from-nothing" case is common and is one of our strongest demo scenarios.

---

## 3. The workflows to automate

Each workflow below: what it is, the manual pain today, expected inputs, expected outputs. These are what we need the Opulent system configured and optimized for, and what we need example/synthetic data built around.

**Priority order: Workflows A–E are the focus — they are the execution steps (6–9).** Workflow F is documented for context but is a later phase.

### Workflow A — Raw expense classification & tax-line mapping

**The problem.** Client hands over 12 months of bank/card CSVs and expense spreadsheets. Today the CPA manually reads every row and sorts transactions into buckets — travel, equipment purchases, office expense, meals, subscriptions, etc. — because each bucket is expensed differently on the return. Waqas: "I'm not doing 12 months of CSVs by myself anymore" is the single biggest time-give-back.

**Expected inputs:**
- One or more transaction CSVs (bank statements, card exports, client-made expense spreadsheets; inconsistent columns, mixed personal/business)
- Client context (entity type, industry, prior-year categories if available)

**Expected outputs:**
- Every transaction categorized into tax-meaningful expense buckets
- Each bucket mapped to its destination form/line (e.g., "→ Schedule C, Line 24a Travel")
- A **flagged-items queue**: anything ambiguous is not guessed — it's surfaced as a question list for the CPA/client ("categorize what you can, ask about the rest")
- Summary totals per category, ready to populate the return

**Key behavior:** first-pass automation + human review of exceptions. Confidence-tag, don't silently guess.

### Workflow B — Books from nothing: chart of accounts → GL → trial balance

**The problem.** Real case: a meat-grocery client handed over nothing but bank-statement CSVs. No QuickBooks, no chart of accounts. Waqas manually built the chart of accounts, hand-created a general ledger categorizing every debit/credit entry, then built a trial balance and manually hunted down imbalances. There is no tool that does this today.

**Expected inputs:**
- Bank statement CSVs (possibly multiple accounts)
- Business type/description

**Expected outputs:**
- A chart of accounts appropriate to the business
- A general ledger with every transaction posted (debit/credit entries categorized)
- A trial balance where debits = credits, with any imbalance **traced to the specific entries causing it**
- An exceptions report of uncategorizable/suspect transactions

### Workflow C — Asset & vehicle depreciation analysis (the flagship demo)

**The problem.** This is the richest single example from our sessions and combines document extraction, an eligibility test, a calculation, form mapping, and client communication. Real case: doctor buys a car "for business." Client hands over purchase agreement, warranty add-ons, and a mileage log, expecting 100% bonus depreciation. The CPA manually: assembled purchase data → computed business-use percentage from the mileage log → found it was ~30%, **below the 50% threshold**, so no bonus depreciation/Section 179 → determined the allowable method and recovery period instead → found the specific Schedule C auto-expense entries and the right depreciation-method selection in Drake's dropdown (these codes are cryptic; picking wrong ones matters — vehicle depreciation is one of the most-audited items) → wrote up a client-facing explanation of why they're not getting 100%.

**Expected inputs:**
- Vehicle/asset purchase documents (purchase agreement, price, add-ons, in-service date)
- Mileage log (or usage records)
- Client income/entity context

**Expected outputs:**
- Extracted asset facts (cost basis, date placed in service, asset class)
- **Business-use % calculation** with the threshold test applied and shown
- Determination: eligible/ineligible for bonus depreciation & §179, and the applicable method + recovery period, with the depreciation math done
- A **counterfactual**: "if business use had been 100%, the deduction would have been $X; at actual use it's $Y" — this is planning gold
- Form mapping: exact Schedule C section / Form 4562 lines and the tax-software method selection to choose
- A plain-English **client memo** explaining the rule, the result, and the forward-looking planning note ("if you keep business use above 50–60% next year, X becomes available")

**Generalize this pattern** beyond vehicles: equipment, leasehold/building improvements, startup expenses — same extract → test → calculate → map → explain loop.

### Workflow D — Multi-state income & nexus handling

**The problem.** Client has 1099 income from multiple states (real case: Illinois + Arizona). CPA manually figures out sourcing, which states need returns, and how income allocates.

**Expected inputs:**
- 1099s (multiple payers, multiple states), W-2s
- Client residency/work-location facts

**Expected outputs:**
- State-by-state income sourcing summary
- Filing-requirement determination per state
- Allocation figures ready for the state returns, with the reasoning documented

### Workflow E — Loss/edge-case determination (e.g., theft/fraud loss)

**The problem.** Client's account got hacked; money unrecoverable. Which form, what treatment, is it deductible? The CPA burns time researching one-off events like this every season.

**Expected inputs:**
- Facts of the event (what happened, amounts, recovery status, business vs. personal)

**Expected outputs:**
- Determination of treatment with the governing rules cited
- The specific form/line placement (e.g., casualty/theft loss reporting)
- Documentation memo for the workpaper file

This generalizes to a broader **"deduction sweep"**: given everything known about the client (home office, self-directed 401(k) contributions, charitable contributions, SE health insurance, startup costs), produce a checklist of every deduction/credit they plausibly qualify for, flagging what's substantiated vs. what needs documentation.

### Workflow F — Discovery → customized document request (later phase — not the current focus)

**The problem.** After a discovery call, the CPA builds a client-specific document request list. Existing tools (e.g., Juno-style checklist products) offer static predefined checklists. The gap is the **customization layer**: the discovery conversation itself contains the cues (client mentions a self-directed 401(k) → request those statements).

**Expected inputs:**
- Discovery call transcript or CPA's notes
- Entity type / client profile
- (Onboarding) the CPA's past request lists as style examples

**Expected outputs (two-step, per Waqas's design):**
1. The **professional-standard baseline request** for that client type (the generic 80%)
2. A **transcript-driven custom addendum**: "based on this conversation, also request: …" (the nuanced 20%), in the CPA's own request style

### Cross-cutting: client-facing explanation memos

Nearly every workflow ends with the CPA translating the result for the client — especially when reality disappoints expectations (the 100%-bonus-depreciation client). Every analytical output should have a one-click "client memo" rendering: plain English, the rule, the numbers, the planning takeaway. This is also strong demo material because it's visibly valuable to non-CPAs watching.

---

## 4. Anchor client profiles for example data

Build synthetic datasets around these two real (sanitized) engagement shapes. Waqas is documenting both and will run his sanitized materials through the platform directly, so your synthetic data should match these shapes.

**Profile 1 — Multi-member LLC (Form 1065), first year with this CPA**
- 8 members; brick-and-mortar storefront
- Raw, unorganized data dump; nothing pieced together
- Building/asset improvements; equipment purchases; entered a lease; pays numerous 1099 contractors; pile of startup expenses
- Exercises: Workflows A, B, C (asset/improvement depreciation, startup-cost treatment), plus K-1 allocation across 8 members

**Profile 2 — High-earning individual, W-2 + Schedule C (first year of side LLC)**
- Physician; ~$1.5M total income (~$400–500K W-2, remainder 1099)
- No prior-year comparison possible (first year of the business — builds from scratch)
- Delivered as a pile of CSVs: expenses, asset purchases (laptops, desks, chairs, equipment), travel
- Vehicle purchased "for business," actual business use ~30% → fails 50% threshold (Workflow C flagship)
- Home office; self-directed 401(k); charitable contributions; theft/fraud loss from a hacked account (Workflow E); 1099s from two states, IL + AZ (Workflow D)
- Exercises: A, C, D, E, the deduction sweep, and the client memo

---

## 5. What we need from Opulent / Jeremy

1. **System configuration tuned to the execution workflows (A–E)** — particularly: robust CSV/tabular ingestion with messy, inconsistent schemas; document extraction from purchase agreements and logs; reconciliation logic that ties numbers out and traces imbalances; calculation transparency (show the math and the threshold tests, never just the answer); and form/line-level mapping output. Don't spend cycles on intake/portal/checklist features — that's not the build.
2. **Skill-from-examples onboarding.** The core mechanic: a CPA uploads sanitized past work product (folder of a prior engagement: raw inputs + the finished workpapers/forms) and the platform infers the method and style. We want the onboarding framework robust and dynamic — a "recipe" any CPA can walk through, not per-CPA hand-curation. Screen recordings of a CPA doing the work are also viable training input.
3. **Synthetic example data** for both anchor profiles: realistic 12-month transaction CSVs, purchase agreements, mileage logs, 1099/W-2 sets, so we can run end-to-end demos without touching real client data.
4. **Demo videos** of the agent doing the tedious work — the marketing asset. Priority order: (1) Workflow C vehicle depreciation end-to-end including the client memo, (2) Workflow A "12 months of CSVs categorized in minutes with a flag queue," (3) Workflow B books-from-nothing to a tied-out trial balance. The pitch motion is live, hands-on demos where a CPA watches their own workflow get built in real time — these videos are the door-opener for those sessions.
5. **Security posture we can state plainly.** The thesis includes an ephemeral, secure working environment for sensitive data (client financials, HIPAA-adjacent material). CPAs are conservative here — Waqas hand-transcribes client calls rather than use recording tools he doesn't trust. We need the one-paragraph version of Opulent's data handling (ephemerality, retention, isolation) that we can put in front of a skeptical practitioner, plus built-in **redaction/sanitization** so a CPA can feed past work in with PII washed out automatically.

## 6. Input → output quick-reference

| # | Workflow | Inputs | Outputs |
|---|----------|--------|---------|
| A | Expense classification | Transaction CSVs, client context | Categorized buckets → form/line mapping, totals, flag queue |
| B | Books from nothing | Bank CSVs, business description | Chart of accounts, GL, tied-out trial balance, exceptions |
| C | Asset/vehicle depreciation | Purchase docs, mileage/usage log | Business-use %, eligibility test, depreciation calc + counterfactual, form/software mapping, client memo |
| D | Multi-state | Multi-state 1099s/W-2s, residency facts | Sourcing summary, filing determinations, allocations |
| E | Loss & edge cases / deduction sweep | Event facts, full client picture | Treatment determination + form placement, deduction checklist, workpaper memo |
| F | Discovery → request *(later phase)* | Call transcript, client profile, past examples | Baseline request list + transcript-driven custom addendum |

---

The through-line: **ingest mess, apply the CPA's own method, show your work, land it on the right line, and explain it to the client.** Optimize for that loop and every workflow above falls out of it.

— Randy Keller
Ashland Taylor Consulting LLC
