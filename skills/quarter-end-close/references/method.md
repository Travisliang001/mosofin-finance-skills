<!-- quarter-end-close · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Run the standard monthly close
- Step 2 — Add quarter-specific tasks
- Step 3 — Specific filings and reports (if applicable)
- Step 4 — Auditor / reviewer coordination (if interim review)
- Step 5 — Year-to-date roll-forward
- Step 6 — Cumulative validation
- Step 7 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway will ask first. Expect `approval_required`; explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — Mosofin cannot do this. The evidence is not on this surface, or the judgment is not a machine's. **The step stays. The user performs it.**

A step with several parts may carry several verdicts. That is shown, not averaged.

**Everything here is a proposal.** The gateway is read-only. Mosofin posts no entries, signs no certificate, and files nothing with anybody. Where this document drafts a covenant certificate or a set of entries, it drafts them for a human to check, sign and submit.

---

## Inputs

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| Quarter ending | Date | **Required** | Fiscal calendar readable from the company record; confirm rather than assume | `[auto]` to read, `[manual]` to confirm |
| Reporting framework | US GAAP / IFRS / Other | **Required** | Not in the books. A client fact. | `[manual]` (Gate 3, then profile) |
| Filing or reporting requirements in scope | 10-Q, board pack, covenant cert, internal report | **Required** | Not in the books | `[manual]` |
| Materiality (often tighter than monthly) | Amount | Recommended | Not in the books; **but both denominators are computable** — see Step 2 | `[manual]` to set, `[auto]` to inform |
| Audit / review involvement | Does the auditor perform an interim review? | Recommended | Not in the books | `[manual]` |
| Prior quarter close documentation | For continuity | Recommended | **The prior quarter's ledger balances are readable directly** — better than the documentation, and see Step 5's reopened-period test | `[auto]` |

---

## Workflow

### Step 1 — Run the standard monthly close

**Quarter-end always includes a full monthly close.** It adds tasks on top; it does not replace. Use `month-end-close-checklist` for the underlying month, in full, and do not begin the quarterly increment until it is finished.

`[auto]` by delegation. That skill already scopes its checklist from the live chart of accounts and self-verifies the entry-based tasks. There is no reason to re-derive any of that here.

**One quarterly addition to the monthly run** `[auto]`: verify that **all three months of the quarter are closed**, not only the last one. A quarter closed on top of an unclosed second month produces roll-forwards that tie and figures that are wrong. Read the posting activity for each of the three months and confirm each has its full complement of close entries — depreciation, amortization, accruals, prepaid releases. A month missing its recurring entries is visible immediately in the entry counts and is the sort of gap that only ever surfaces at quarter-end.

---

### Step 2 — Add quarter-specific tasks

Eleven task groups. All eleven are preserved, in the original's order, each with its verdict and with whatever the workspace can genuinely contribute.

---

**Tax provision (interim)**

- Estimated annual effective tax rate (EAETR) approach for interim provisions — `[manual]`
- Apply EAETR x YTD pretax income to determine YTD tax expense — `[auto]` for the arithmetic, once the rate exists
- Discrete items (FIN 48 / IAS 12 uncertain tax positions) recognised **in the quarter they arise**, not spread — `[manual]`
- Hand off to the tax provision work

**Why the rate is `[manual]`.** EAETR is a *forecast* rate: expected full-year tax expense over expected full-year pretax income. The denominator is a projection of a year that has not happened. No ledger contains it. What the ledger contributes is the **YTD pretax income** the rate is applied to — that is `[auto]` and exact — and the prior year's actual effective rate as a sanity check on the forecast, which is also `[auto]`.

`[auto]` and worth having: **compare the YTD tax expense actually booked against EAETR x YTD pretax income.** If the client has been booking tax at a flat statutory rate all year rather than at the effective rate, the difference will be visible and will need correcting before the quarter is reported.

---

**Revenue and ARR / KPI deep-dive**

| Task | Verdict | Note |
|---|---|---|
| ARR / MRR / bookings reporting (SaaS) | `[manual]` | Contract metrics, not ledger metrics. See the near-substitute section. |
| Customer cohort analysis | `[auto]` in part | First-invoice date per customer and revenue by period are both readable, so cohorts by first-transaction date are computable. Cohorts by *signup* date are not — signup is not a transaction. See `cohort-and-unit-economics`. |
| Customer concentration / top customers | `[auto]` | Revenue by customer, ranked, with percentages. Exact, and one query. |
| Backlog / RPO | `[manual]` | Unrecognised committed revenue, including unbilled. Not in the ledger by construction. |
| Disaggregated revenue by stream / geography / customer type | `[auto]` **if** those are dimensions in the book; `[manual]` if not | Read the dimension list first. This is a chart question with a yes/no answer. |

**Customer concentration deserves emphasis.** It is `[auto]`, it is exact, it is a required disclosure in several frameworks, and it is one of the few quarterly KPIs the ledger actually owns outright. It also moves — a customer that was 8% of revenue last quarter and is 19% this quarter is a disclosure item and a risk item at once.

---

**Lender covenant testing**

- Compute each covenant ratio (debt-to-EBITDA, interest coverage, fixed charge coverage, and so on) — see `debt-and-covenant-tracking` — `[auto]` for the arithmetic, `[manual]` for the definitions
- Compare to the covenant threshold — `[auto]`
- Document compliance or breach — `[gated]`, because the conclusion goes outside the building
- Prepare the covenant compliance certificate if required — `[manual]` to sign and submit; Mosofin drafts only

**Read the near-substitute section above before running this.** The arithmetic is trivial and the definitions are everything. Record each covenant's definition — the exact add-backs, the exact exclusions, the annualisation convention — in the client profile the first time it is established, so that this quarter's work makes next quarter's cheaper.

`[auto]` and genuinely valuable: **compute the headroom, not just the pass/fail.** A covenant passed at 3.4x against a 3.5x threshold is not the same news as one passed at 1.9x, and the certificate does not say so. Trend the ratio across the available quarters and show which direction it is moving. A covenant that has tightened for three consecutive quarters is a finance conversation that should happen now rather than at the point of breach.

---

**Forecasting / re-forecast**

- Updated full-year forecast based on quarterly actuals — `[manual]` for the forecast, `[auto]` for the actuals it is built on
- Rolling 12-month forecast refresh — `[manual]`; see `rolling-forecast`
- Cash flow forecast update — `[manual]`; see `cash-flow-forecast-13-week`

The ledger is a record of what happened. A forecast is an assertion about what will. Mosofin supplies the base — YTD actuals by account, by month, with the seasonality visible — and stops there. The projection is management's, and it should be labelled as management's on the face of anything that shows it.

---

**Variance analysis (full quarter)**

- QTD and YTD versus budget and prior year — `[auto]` **against prior year**; `[auto]` **against budget only if the budget is loaded into the book**, otherwise `[manual]`
- Driver-based explanations (price, volume, mix, FX) — `[auto]` for **price and volume and mix** where units are on the transaction lines; `[manual]` for the narrative
- Hand off to `budget-vs-actual-analysis`

Prior-year comparison is free and exact — it is the same ledger, twelve months earlier. Budget comparison depends entirely on whether a budget exists as data. Check; do not assume. And as the MD&A puts it: the arithmetic of a variance is not an explanation of it. Computing that revenue fell 6% is `[auto]`. Saying why is not.

---

**Subsequent events review**

- Events between quarter-end and the report issue date — **partly `[auto]`**, see below
- Categorise: recognised (Type 1) versus non-recognised (Type 2) — `[manual]`
- Recognised: the condition existed at quarter-end, therefore **adjust** the financials — `[manual]`
- Non-recognised: the condition arose after, therefore **disclose** if material — `[manual]`

**What the ledger can genuinely find** `[auto]` — read transactions posted *after* the quarter-end date, up to today, and look for:

- a **credit note or refund** issued after quarter-end against an invoice dated before it — the condition almost certainly existed at quarter-end; a strong Type 1 candidate
- a **write-off** of a receivable that was outstanding at quarter-end
- a **payment received** on a receivable that was provided against — evidence the provision was too high
- a **customer with a material quarter-end balance and no activity at all since** — a collectibility indicator
- **inventory sold after quarter-end below its carried cost** — net realisable value evidence
- **large post-quarter reversals** of entries made before it

That is a real and useful list, it is one query, and it is more systematic than the usual approach of asking people what they can remember.

**What it absolutely cannot find** — and this must be said in the same breath, because the list above is seductive: a lawsuit filed. A fire. A key customer lost. A financing signed. A regulatory action. An acquisition agreed. A director resigning. **None of these are transactions, and most Type 2 events are precisely of that kind.**

So the query gives a **partial** subsequent events review, and the partiality is not a detail. Record on the log which events were found by reading the ledger and which by asking management, and record that the ledger sweep cannot establish completeness. See `subsequent-events-review`.

---

**Going-concern assessment**

- Quarterly review of the entity's ability to meet its obligations for twelve months from issuance — `[manual]`
- Document liquidity, debt maturities, funding plans — `[auto]` for the facts, `[manual]` for the assessment

**The facts the workspace supplies** `[auto]`: current cash balance and its trend over the available quarters; the operating cash burn or generation per month; the current ratio and working capital at each quarter end; total debt on the balance sheet; receivables ageing concentration.

**The facts it does not** `[manual]`: **debt maturity dates**. These live in loan agreements. A balance sheet shows what is owed, not when it falls due, unless somebody has classified it into current and non-current by hand — and that classification is itself the thing being tested. Undrawn facility headroom is likewise not in the ledger. Neither is a funding plan, a letter of support, or a shareholder's intention.

**And a rule carried over from the MD&A, which applies here with full force: never author a forward-looking statement.** Twelve-months-from-issuance is a management assertion with legal weight. Mosofin presents the liquidity facts, clearly and with their figures. Management makes the assessment and signs it.

---

**Estimates and reserves review**

Seven, all preserved:

| Estimate | Verdict | What the workspace contributes |
|---|---|---|
| Allowance for doubtful accounts | `[auto]` roll-forward and rate trend, `[manual]` judgment | See `bad-debt-and-write-offs`. Ageing is live; collectibility is not. |
| Inventory reserves | `[auto]` roll-forward, `[manual]` judgment | See `inventory-obsolescence-and-reserve` and `inventory-to-gl-reconciliation`. |
| Warranty reserves | `[auto]` roll-forward, `[manual]` judgment | Claims experience is readable if claims are transactions; the failure-rate assumption is not. |
| Litigation accruals | `[manual]` | Legal assessment. Not on this surface at all. |
| Restructuring reserves | `[auto]` roll-forward, `[manual]` judgment | The plan and its timing are outside the books. |
| Earn-out / contingent consideration revaluation | `[manual]` | A valuation. |
| Impairment indicators for long-lived assets | `[auto]` for **some** indicators, `[manual]` for the test | See below. |

**On impairment indicators specifically:** the original says to review indicators and test only if one suggests testing. Several indicators *are* readable — a sustained operating loss in a segment, an asset group whose associated revenue has fallen materially, a sustained decline in overall performance. Others — market capitalisation below book value, adverse regulatory change, a change in the manner of use — are not. Present the readable indicators as indicators and do not represent the review as complete. Testing itself needs fair values, which are not on this surface: the goodwill impairment test.

**The `[auto]` test that is worth more than any single roll-forward: has the reserve rate actually moved?**

Compute each reserve as a percentage of its base — allowance over gross receivables, inventory reserve over gross inventory, warranty reserve over the relevant revenue — for every quarter available. Then look at the series.

**A rate that is identical to four decimal places for eight consecutive quarters is not being reviewed. It is being copied.** That is a control finding, it is available from arithmetic alone, and it is exactly what an interim reviewer will ask about. It does not prove the rate is wrong — a stable business can have a stable rate. It proves nobody looked, which is the thing the quarterly estimates review exists to prevent.

The mirror finding is equally useful: **a rate that jumps sharply in one quarter and stays there** is a methodology change, and a methodology change is a disclosure item. Sheet 3 has a column for it.

---

**Stock-based compensation refresh**

- Update vesting, forfeitures, and current-period expense — `[manual]`
- Hand off to the equity compensation accounting

`[manual]`, and unavoidably so. **There is no cap table on this surface.** Grants, vesting schedules, forfeiture events and exercise activity live in an equity administration system or a spreadsheet, not in the general ledger. What the ledger holds is the *result* — the expense somebody calculated and posted.

That does give one `[auto]` check worth running: **is the stock compensation expense moving in a way that makes sense?** A flat monthly charge that has not changed across eight quarters, in a company that has been granting and vesting throughout, is a schedule that stopped being refreshed. This absence is consistent across the pack — see also an IPO readiness review, `financial-statement-builder`, a financial model review.

---

**Segment reporting** (if reportable segments exist)

- Segment P&Ls — `[auto]` **if segments are a dimension in the book**, otherwise `[manual]`
- Reconciliations to consolidated — `[auto]` under the same condition
- Segment disclosure — `[manual]`; see segment reporting

This one is genuinely binary and the answer comes from the chart, which is why it is a Gate 3 question. If the client tracks segments as classes, locations, departments or another dimension on the transactions, then segment P&Ls and their reconciliation to the consolidated total are live reads and the reconciliation will tie by construction. If segments are assembled in a spreadsheet outside the books, none of it is available and the whole task is the user's.

Read the dimension list. Do not infer segments from account names — an account called "North Region Sales" is a chart-of-accounts convention, not a segment structure, and building a segment note on it will produce something that cannot be reconciled or maintained.

---

**Disclosure controls and ICFR**

- Quarterly testing of in-scope controls — `[manual]`; see `sox-controls-design-and-testing`
- Sub-certifications from sub-process owners — `[manual]`
- Disclosure committee meeting (for SEC filers) — `[manual]`

All three are `[manual]` and none of them should be dressed up otherwise. A control test is an examination of whether a control **operated**, which usually means inspecting evidence of a human action — a review signature, an approval, a reconciliation someone prepared and someone else checked. A sub-certification is a person taking responsibility in writing. A disclosure committee is a meeting.

**One narrow `[auto]` contribution**, and it should be described accurately: for controls whose operation leaves a trace in the ledger, the trace is readable. Whether entries above a threshold carry an approver where the system records one. Whether the reconciliations that were supposed to happen produced entries. Whether anything was posted to a closed period.

That is population evidence about *some* controls, and it is genuinely stronger than sampling, because it covers everything rather than twenty-five items. It is also **not a control test**, because it says what happened in the data and not whether the control operated as designed. See `internal-audit-workpaper`, which works through this distinction properly.

---

**A note on interim materiality, since the input table flags it**

The original notes quarterly materiality is often tighter. There is an interim-specific subtlety underneath that, and it matters for SEC filers: **an error must be assessed against the interim period and against the expected full year.** Something immaterial to a quarter can be material to the year; something material to a quarter may wash out over it. Both denominators are required.

`[auto]`: present both. YTD pretax income and the relevant full-year base are computable, and showing the two denominators side by side is a small thing that keeps the assessment honest. `[manual]`: the threshold and the conclusion, which are the user's.

---

### Step 3 — Specific filings and reports (if applicable)

Four families, all preserved. None of them is something Mosofin submits.

**For SEC-filing entities** — all `[manual]` to file:
- 10-Q drafting — `[auto]` for the financial statements that go in it (`financial-statement-builder`), `[manual]` for the document
- Management's Discussion and Analysis; the variance arithmetic is `[auto]`, the narrative is not, and **no forward-looking statement is ever authored here**
- Item 4 (Controls and Procedures) certifications — `[manual]`
- Exhibits (CEO / CFO certifications, material contracts) — `[manual]`

**For lender-driven reporting:**
- Compliance certificate — `[manual]` to sign; drafted from Step 2's covenant work
- Required financial statements — `[auto]` to produce, `[manual]` to issue
- Borrowing-base certificate (asset-based lenders) — `[auto]` in part: eligible receivables and eligible inventory are computed from ageing and stock data that are readable, **but the eligibility rules are in the agreement** — concentration caps, ineligible ageing buckets, cross-ageing, foreign account exclusions. Same trap as covenant EBITDA. Get the rules, record them, then the computation is mechanical.
- Covenant calculation worksheet — `[auto]` for the arithmetic

**For investor reporting:**
- Board pack — see `management-reporting-pack`; largely `[auto]` for the figures
- Investor update / shareholder letter — `[manual]`
- KPI dashboard — `[auto]` for ledger-derived KPIs, `[manual]` for the rest; see `kpi-dashboard-builder`

**For internal management:**
- Quarterly performance review materials — `[auto]` for the figures
- Department / business unit P&Ls — `[auto]` **if** those are dimensions in the book
- Project profitability reviews — `[auto]` **if** projects are tracked as a dimension; see `job-costing-and-wip`

Notice the pattern running through three of these four families: **the arithmetic is available and the document is not.** Mosofin produces figures with provenance. A human writes, reviews, signs and submits. That boundary is not a limitation to be worked around; for a document that goes to a regulator or a lender, it is the correct division of labour.

---

### Step 4 — Auditor / reviewer coordination (if interim review)

If the auditor performs a SAS 100 / ISRE 2410 quarterly review, all five items are preserved:

| Task | Verdict | Note |
|---|---|---|
| Quarterly PBC list (smaller than year-end) | `[auto]` to assemble the ledger-derived items | Trial balances, transaction detail, ageings, roll-forwards — these are most of a PBC list and they are all live reads. See `audit-pbc-list-manager`. |
| Auditor walkthroughs of significant estimates | `[manual]` | A conversation. |
| Analytical procedures | `[auto]` to prepare | Period-over-period and ratio analysis are exactly what the workspace is good at. The auditor performs their own; supplying the same analysis in advance shortens the review. |
| Management representation letter (interim) | `[manual]` | Management represents; not a machine. |
| Resolve auditor inquiries before filing | `[auto]` in part | Many inquiries are "show me the detail behind this balance", which is a query. Some are not. |

An interim review is substantially **analytical** rather than substantive, which is unusually well matched to what a live ledger read can supply. Preparing the analytics before the auditor asks is one of the higher-value `[auto]` contributions in the whole quarter.

---

### Step 5 — Year-to-date roll-forward

**This step is `[auto]` end to end**, and it is the largest single block of manual quarterly work the workspace removes.

Both tie tests, preserved:

- **Trial balance YTD ties to opening plus three (or six, or nine) months of activity** — `[auto]`
- **Balance sheet balances tie to prior quarter-end plus period activity** — `[auto]`

And all seven roll-forwards, each opening plus activity equals closing, each a live read:

| Roll-forward | Verdict | Cross-reference |
|---|---|---|
| AR allowance | `[auto]` | `bad-debt-and-write-offs` |
| Inventory reserves | `[auto]` | `inventory-obsolescence-and-reserve` |
| Deferred tax positions | `[auto]` for the movement, `[manual]` for the substance | the deferred tax roll-forward |
| Equity (paid-in capital, retained earnings, other comprehensive income) | `[auto]` | `financial-statement-builder` |
| Fixed assets (gross and accumulated depreciation) | `[auto]` for the GL side; **the register is outside** | `fixed-asset-register-and-depreciation` |
| Intangibles | `[auto]` for the GL side; register outside | the intangibles register |
| Lease balances | `[auto]` for the GL side; **the lease schedule is outside** | the lease accounting |

**Three of the seven carry the same caveat and it is worth stating plainly:** fixed assets, intangibles and leases each have a *register* that lives outside the accounting system. The roll-forward of the GL balance is automatic and will tie to itself perfectly. That is not the same as agreeing to the register, which is the reconciliation that actually matters. The relevant skills each handle the two-directional check; this step produces the GL leg and says so.

**And now the quarterly-specific test the original does not have** `[auto]`:

**Has a prior period been reopened?**

Compare this quarter's opening balances to the prior quarter's closing balances **as they stand in the ledger today**. They should be identical. If they are not, somebody has posted into a period that was closed and, in all likelihood, already reported.

For an entity with a filing obligation this is not a bookkeeping irritation. **The figures that were reported to a lender, a board or a regulator are no longer the figures in the books.** Every subsequent quarter's comparatives are affected. It needs to be identified, quantified and escalated, not silently absorbed into the current quarter.

The test is one comparison and it takes seconds. Run it every quarter. Then extend it: read for **any entry posted into the prior quarter after the prior quarter's close date**, list them with their dates, amounts and sources, and put them on Sheet 8. See a restatement review for what to do when the total is material.

---

### Step 6 — Cumulative validation

Five tests, all preserved, and here the verdicts split cleanly.

| Test | Verdict | Note |
|---|---|---|
| YTD revenue ties to invoices issued YTD, net of credits | `[auto]` | Both sides are live reads. A variance here means revenue was posted by journal rather than by invoice — which may be entirely proper (accruals, deferrals) but should be identified rather than discovered. |
| YTD COGS ties to the inventory roll | `[auto]` | Subject to the caveat in `inventory-to-gl-reconciliation`: where the subledger and the GL are the same database, this ties by construction and proves nothing about the physical stock. |
| **Cash YTD reconciles to bank statement YTD activity** | **`[manual]`** | **Bank statements are not on this surface.** Book cash tied to book cash is the same number twice. See the near-substitute section. |
| Equity walks from the beginning of the year to current | `[auto]` | Opening equity plus net income plus other comprehensive income plus capital movements less distributions. Exact. |
| Cash flow statement for QTD and YTD | `[auto]` to produce | See `cash-flow-statement-indirect-method`. Built from balance sheet movements and net income, all of which are live. |

**Four of five automatic, one genuinely not**, and the one that is not is the most important of the five, because it is the only test in the list that reaches outside the accounting system for its evidence. Everything else here ties one part of the ledger to another part of the same ledger. Useful — internal consistency is worth confirming — but it is not external verification, and the checklist should not let the four green ticks disguise the fact that the fifth was not performed.

---

### Step 7 — Output

An `.xlsx` close workpaper extending the monthly close template. All eight of the original's sheets, in order, with two Mosofin additions.

**Sheet 1: Quarter Close Calendar**
| Task | Type (Monthly close / Quarter-specific) | Owner | Due | Status |

Add a **Verdict** column. A calendar that shows at a glance which tasks are automatic and which need a person is a better planning document than one that treats all tasks as equal effort.

**Sheet 2: Quarter-Specific Procedures**
The detailed task list — tax provision, covenant testing, subsequent events, going concern, and the rest of Step 2. Every one of the eleven groups appears, including those that are wholly `[manual]`. **A task that Mosofin cannot perform is not omitted from the checklist; it is listed with its owner.**

**Sheet 3: Estimates Review**
| Estimate | Prior Period Balance | This Period Activity | Closing | Methodology Change Y/N | Disclosure Required Y/N |

Add a **Rate as % of base** column and a **Quarters unchanged** column. That is where the "nobody looked" finding lives, and it is invisible in the original five columns.

**Sheet 4: Roll-Forward Summary**
All seven YTD roll-forwards on one page. `[auto]`. Mark the three whose registers sit outside the books.

**Sheet 5: Subsequent Events Log**
| Event | Date | Type (Recognised / Non-recognised) | Impact | Disclosure Required Y/N |

Add a **Source** column: `ledger sweep` or `management enquiry`. And carry a completeness note at the head of the sheet: the ledger sweep finds transactional events only.

**Sheet 6: Covenant Compliance**
| Covenant | Threshold | Computed | Compliance Y/N |

Add **Definition source**, **Headroom**, and **Trend (last 4 quarters)**. The definition source column is the one that stops a ledger-derived EBITDA from quietly becoming a certified one.

**Sheet 7: Filing / Report Checklist**
What is being issued, when, by whom, with what review. Every row ends with a human name. Nothing on this sheet is submitted by Mosofin.

**Sheet 8: Final Tie-Out and Sign-Off**
Plus the reopened-period findings from Step 5, because a prior-period posting belongs in front of whoever signs.

**Sheet 9: Ledger Diagnostics** *(Mosofin addition)*
The pattern findings — things the books said without being asked:

| Finding | Evidence | Quarters covered | Amount | Recommended action |
|---|---|---|---|---|

Q4-versus-Q1-to-Q3 posting volume (see below). Reserve rates unchanged across quarters. Entries posted into closed periods. Months within the quarter missing their recurring entries. Covenant headroom trending down. Customer concentration shifts.

**The Q4 test, stated properly**, because it is the most valuable thing on this sheet: count manual journal entries, and their absolute value, by quarter across the available years. **If Q4 is several multiples of Q1 through Q3, the interim quarters were not really closed** — the year-end audit found the problems and Q4 absorbed the corrections. Every interim figure reported during those years was provisional in a way the recipients were not told about. Report it with the counts and the values, as an observation about the process, and never as an allegation about a person.

**Sheet 10: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet. Contents below.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `QuarterEndClose_[YYYY-Q#]_[EntityName].xlsx`

The entity `display_name` goes in the file name **and** in a column on every sheet. Never one file with several companies silently interleaved. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Output Quality Standards

All nine preserved, each with the verdict that says who is responsible for meeting it.

- **Monthly close fully complete before quarter-specific tasks.** `[auto]` to verify — and verify **all three months**, not only the last.
- **Tax provision documented with EAETR methodology.** `[manual]` for the rate and the documentation; `[auto]` for the YTD pretax base it is applied to.
- **Estimates reviewed and supported.** `[auto]` for the roll-forwards and the rate trend; `[manual]` for the review itself. **A rate that has not moved in eight quarters is not evidence of a review.**
- **Covenant calculations verified.** `[auto]` for the arithmetic; `[manual]` for the definitions, which come from the credit agreement and must be recorded.
- **Subsequent events log complete through the filing date.** `[auto]` for the transactional sweep; `[manual]` for completeness, **which the sweep cannot establish** — the log must say which events came from where.
- **Going-concern assessment present.** `[auto]` for the liquidity facts; `[manual]` for the assessment. Never authored by Mosofin.
- **Roll-forwards tie.** `[auto]`, all seven — with the caveat that three of them tie to the GL and not to a register.
- **File naming consistent.** `[auto]`
- **No quarter-specific task silently skipped.** `[auto]` to enforce — Sheet 2 lists all eleven groups whatever their verdict, and **a `[manual]` task is listed with an owner, never omitted because Mosofin could not do it.** This is the standard that most directly protects the integrity of the whole checklist.

**Three Mosofin additions:**

- **Every figure is attributed** — ledger-read, user-supplied, or agreement-derived. A covenant ratio built on a definition from a credit agreement is labelled as such.
- **Nothing is presented as filed, signed or posted.** The gateway is read-only. Mosofin drafts; humans sign and submit.
- **The prior-period integrity test is run every quarter.** Opening balances against last quarter's closing balances. It takes seconds and it is the only routine check that catches a reported period being changed after the fact.

---

## Seed to evolved: what happens on the first real run

This file is a **seed**, written without sight of the client's books. Every verdict in it is a prediction. The first real run replaces predictions with observations.

**What must never be frozen into a seed:** a snapshot of which tools existed and what their policies were on the day it was written. Policies tighten after incidents and loosen after reviews. A seed that hardcodes a capability map is wrong the first time anything changes and, worse, wrong *silently* — reporting `[auto]` for a capability that has been disabled for a month. **Gate 2 reads the map fresh, every run.** Do not replace it with a list.

**What is worth writing into the evolved version, after the first quarter:**

1. **The covenant package: every definition, in full.** The add-backs, the exclusions, the annualisation convention, the eligibility rules for any borrowing base. This is the single highest-value thing to persist. It is expensive to obtain, it does not change between quarters, and without it the whole covenant block is guesswork.
2. **The fiscal calendar**, confirmed rather than assumed.
3. **Which reporting obligations apply**, and their deadlines, so the calendar builds itself next quarter.
4. **Whether segments, departments and projects are dimensions in this book.** A yes/no that flips three tasks between `[auto]` and `[manual]`.
5. **The estimate methodologies and their rates**, with the quarter each was last genuinely reviewed. That history is what makes the "nobody looked" test meaningful.
6. **The Q4 posting-volume baseline**, so next year's comparison has something to compare against.
7. **The findings from this quarter**, so they are re-tested first next quarter rather than rediscovered.
8. **Any observed policy that differed from this file's defaults.**

Persist through `create_skill`, scoped to the workspace it came from. **Client facts belong in a client-scoped skill, never back in the seed** — the seed goes to the next engagement and must not arrive carrying the last client's covenant thresholds.

**The evolved version should have a shorter interview and a longer diagnostics sheet.** Quarterly cadence means four runs a year, and a skill that asks the same six questions every quarter has failed at the only thing repetition makes possible.

---

## Anti-patterns

- **Certifying a covenant off ledger EBITDA.** The agreement defines the term. The chart of accounts does not. This is the one that ends up in front of a bank.
- **Reporting the deferred revenue balance as RPO**, or a month's revenue times twelve as ARR.
- **Calling the subsequent events review complete after a ledger sweep.** The sweep finds transactions. Most Type 2 events are not transactions.
- **Authoring a going-concern conclusion.** Present liquidity facts. Management asserts.
- **Treating a stable reserve rate as evidence of review.** It is evidence of a copy-paste.
- **Ticking Step 6 with four of five tests.** The missing one is the only one that reaches outside the books.
- **Reporting a roll-forward that ties to the GL as agreement with a register.** Fixed assets, intangibles and leases each have a register outside the ledger.
- **Skipping the prior-period integrity check** because it has never found anything. It costs seconds and catches a reported quarter being altered.
- **Running this skill for Q4.** Q4 is `year-end-close`.
- **Closing the third month and calling the quarter closed.** All three months, each with its recurring entries.
- **Presenting fixture-clean diagnostics as reassurance.** Mock data has no history and passes every pattern test by construction.
- **Dropping a `[manual]` task from the checklist** because Mosofin cannot perform it. It gets an owner, not a deletion.
- **Claiming this skill is still system-agnostic.** The reporting logic is; the evidence is one connected ledger. Say which is which.
- **Saying "filed", "signed" or "posted".** The gateway reads.
