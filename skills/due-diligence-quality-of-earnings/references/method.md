<!-- due-diligence-quality-of-earnings · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Define the lens and the QofE scope
- Step 2 — Validate the base numbers
- Step 3 — Build the adjusted EBITDA bridge
- Step 3b — The recurring "one-time" test (Mosofin addition)
- Step 4 — Assess revenue quality
- Step 5 — Assess working capital
- Step 6 — Net debt and debt-like items
- Step 7 — Maintenance vs. growth capex
- Step 8 — Forecast assessment (if management provided)
- Step 9 — Identify risks and observations
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Verdicts below assume the target is connected.** Where it is not, read every `[auto]` as `[manual]` —
the analysis is identical, the data simply arrives from the data room.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the multi-year P&L,
the monthly balance sheets, customer revenue and the ledger extracts do not depend on each other. Never
serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, for the target:

- *`get_profit_and_loss`* **monthly, over 3+ years** — the earnings base, the seasonality, and the raw
  material for the recurring-item test — usually **[auto]**
- *`get_balance_sheet`* **monthly, over 24–36 months** — **the working capital series** — usually **[auto]**
- *`get_trial_balance`* at each year end — account-level detail — usually **[auto]**
- *`get_general_ledger`* — **the transactions behind the numbers**, where one-offs and related-party flows
  live — usually **[auto]**
- *`get_customer_sales`* monthly by customer — **concentration, churn and mix** — usually **[auto]**
- *`get_cash_flow`* — capex and actual cash generation — usually **[auto]**
- *`search_accounts`* — the debt, cash and debt-like accounts, and the fixed-asset accounts — usually
  **[auto]**
- *`get_vendor_expenses`* / *`search_vendors`* — **related-party and owner spend**, once the parties are
  named — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — receivable and payable quality — usually **[auto]**
- *`search_items`* — product and service mix — usually **[auto]**
- *`search_journal_entries`* — **manual entries around period ends**, a classic recognition-quality signal
  — usually **[auto]**
- *`get_company_info`* — legal name, year-end, industry — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a QofE sets a purchase price.** An adjusted
EBITDA figure derived from fixtures, multiplied by eight, is a very expensive error.

## Step 1 — Define the lens and the QofE scope

**The QofE lens is different from a statutory audit:**

- **An audit assesses whether the financials are presented fairly** under GAAP / IFRS
- **QofE assesses whether reported earnings are representative of sustainable, recurring economic
  performance** — **what a buyer can expect to recur**

QofE typically covers:

- **Adjusted / normalized EBITDA** (the headline)
- **Quality and sustainability of revenue**
- **Quality of working capital**
- **Net debt and debt-like items**
- **Capex requirements** (maintenance vs. growth)
- **Forecast plausibility** (if provided)
- **Risks and exposures**

**State the period covered** (e.g. LTM as of date, plus prior 2 years) — **[auto]** to confirm the data
actually reaches back that far, which is worth doing before promising three years of analysis.

## Step 2 — Validate the base numbers

**Before adjusting, validate the reported numbers** — **[gated]**:

- **Are the financials reliable** (audited / reviewed / management-prepared)? — **[manual]**
- **Reconcile reported financials to the GL / underlying data** — **[auto]** where the target is connected,
  and worth doing: reports and ledgers can disagree, and the difference is a finding
- **Identify accounting policy choices and whether they're appropriate** — **[gated]**
- **Identify any accounting errors or policy changes during the period**
  (`restatement-and-prior-period-adjustment`) — **[auto]** to spot the symptom: a step-change in a ratio
  with no operational explanation, or a large prior-year adjustment entry

**A QofE on unreliable underlying data is unreliable.** Say so explicitly where the base is weak; it is a
limitation on everything downstream, not a footnote.

## Step 3 — Build the adjusted EBITDA bridge

**Start with reported EBITDA and adjust for:**

**One-time / non-recurring items** (genuinely unusual, not expected to recur) — **[gated]**: **[auto]** to
find candidates as outliers in the ledger, **[manual]** to conclude they are non-recurring:

- **Restructuring costs**
- **Legal settlements**
- **M&A transaction costs**
- **Major insurance claims** (income or expense)
- **One-time bad debt write-offs**
- **Litigation costs** (genuinely one-time)

**Non-operating items** — **[auto]** to identify from the accounts:

- **Gains / losses on asset sales**
- **FX gains / losses** (if non-operating)
- **Other income / expense not core to operations**

**Owner / related-party normalizations** (private-company common) — **[gated]**: **[auto]** to quantify
once the parties are named, **[manual]** for the market benchmark:

- **Owner compensation above / below market**
- **Related-party rents at above / below market**
- **Personal expenses run through the business**
- **Family members on payroll without commensurate roles**

**Run-rate adjustments** — **[manual]**:

- **Annualizing the effect of price changes implemented mid-period**
- **Adjusting for known contract wins / losses post-period**
- **Recently completed cost actions**

**Pro-forma adjustments** (for transactions during the period) — **[manual]**:

- **Pro-forma effect of acquisitions / divestitures as if owned or divested for the full period**
- **New facility opening costs vs. mature run-rate**

**Accounting adjustments** — **[manual]**:

- **Restate to the buyer's accounting policies if material** (revenue cutoff, inventory method,
  capitalization)

**Critical discipline — what should NOT be in adjusted EBITDA:**

- **Stock-based compensation** — a real economic cost, and recurring
- **"One-time" expenses that recur every year** — not actually one-time
- **Cherry-picked add-backs without symmetric treatment of one-time income**
- **Hypothetical synergies** — those belong in valuation, not in historical QofE EBITDA

**Each adjustment must have:**

- **A description and rationale**
- **Quantification with support**
- **A test: is this genuinely non-recurring, or just convenient?**

**Display as a clear bridge: Reported EBITDA → adjusted EBITDA, with each adjustment labeled.**

## Step 3b — The recurring "one-time" test (Mosofin addition)

**The original's first and most important edge case is that "one-time" items which recur should not be
adjusted.** In a connected workspace **this is testable rather than arguable.**

**[auto]**: for **every add-back category in the bridge**, look at **the same account or category in each
of the prior years** (*`get_profit_and_loss`* multi-year, *`get_general_ledger`*). Report, per adjustment:

| Add-back | This year | Year -1 | Year -2 | Year -3 | Appears every year? |

**An add-back that appears in all three prior years is not non-recurring**, whatever it is called. Legal
settlements, restructuring, "exceptional" bonuses and one-off consultancy are the usual offenders, and a
business that restructures annually is simply a business with restructuring costs.

This single table is often the most valuable page in a buy-side QofE and the most uncomfortable one in a
sell-side draft. **Run it on every bridge, including your own.** It is also the discipline that keeps
sell-side work defensible: an add-back that survives this test will survive the buyer's diligence.

Two companions, both `[auto]`:

- **Symmetry check** — the original insists on symmetric treatment. **List one-time *income* items
  alongside the expense add-backs.** A bridge containing only expense add-backs has almost certainly been
  filtered
- **Magnitude context** — express total adjustments as a percentage of reported EBITDA. A bridge where
  adjustments exceed reported EBITDA is not a normalisation; it is a reconstruction, and it should be
  labelled as one

## Step 4 — Assess revenue quality

- **Revenue by customer**: **concentration** (top 5 / 10 customers as % of revenue), **customer churn**,
  customer-level trends — **[auto]** (*`get_customer_sales`*), and one of the strongest automated outputs
  here
- **Revenue by product / service**: mix and trends — **[auto]** where items are used
- **Revenue by geography** — **[gated]**
- **Recurring vs. non-recurring revenue split** (subscription, contracts, one-time projects) —
  **[gated]**: repeat-purchase patterns are measurable, the contractual basis is **[manual]**
- **Revenue recognition policies**: aggressive vs. conservative; **cutoff testing at period-ends** —
  **[auto]** for a powerful proxy: invoice volume and value in the **last days of each period** against a
  normal run-rate, plus credit notes issued **early in the following period**. That pattern is what
  pulled-forward revenue looks like
- **Pricing trends**: stable, increasing, decreasing — **[auto]** where items carry prices
- **Customer cohorts**: retention, expansion (`cohort-and-unit-economics`) — **[auto]**
- **Backlog / pipeline visibility** — **[gated]**; open estimates and orders are readable

**Quality issues: high concentration, declining retention, aggressive recognition, recurring revenue
inflated by one-time items.**

## Step 5 — Assess working capital

- **Monthly working capital** (AR, inventory, AP, accrued liabilities) **over 24–36 months** — looking for
  **trends and seasonality** — **[auto]**, and this is the input that normally consumes the most analyst
  time. A monthly balance sheet series across three years is a single set of reads
- **Compute days metrics**: **DSO, DIO, DPO, cash conversion cycle** (`kpi-dashboard-builder`) — **[auto]**
- **Identify abnormal items**: **stretched payables, depleted inventory, AR aging deterioration** —
  **[auto]**, and each is a classic pre-sale window-dressing signal: paying suppliers later and running
  stock down both flatter the cash position at a convenient moment
- **Determine the "normalized" working capital target** for the deal — typically the average monthly
  working capital over LTM or another defined period — **[gated]**: the arithmetic is **[auto]**, the
  methodology is negotiated
- **The buyer "buys" a normalized working capital level; deviations at close adjust the purchase price**
  (the **WC target mechanism**)

**This is a heavily-negotiated deal item — get the methodology right.** Show the target under **more than
one method** (average, median, peak-to-trough) — the spread between them is exactly what the negotiation
is about, and quantifying it early is worth more than defending one number.

## Step 6 — Net debt and debt-like items

The **"cash-free debt-free"** valuation basis means defining net debt precisely:

```
Net debt = Total debt − Cash
```

**But there's more — "debt-like items"** that economically behave like debt and reduce equity value.
**[gated]**: balances are **[auto]**, the classification is negotiated, and several items are
**[manual]** because they are off-balance-sheet:

- **Unfunded pension obligations**
- **Tax liabilities** (uncertain positions, unpaid tax due)
- **Deferred compensation, accrued bonuses earned by the seller**
- **Earnouts payable**
- **Capital lease obligations** (operating lease debate per the deal)
- **Customer deposits that are economically refundable**
- **Restructuring accruals**
- **Litigation accruals likely to settle in cash**
- **Off-balance-sheet commitments expected to crystallize** — **[manual]** by definition

**Cash-like items** (items that behave like cash but might be excluded by the buyer):

- **Restricted cash**
- **Cash in foreign jurisdictions with repatriation cost**
- **Customer cash deposits**

**Define a deal net debt that reflects the economic substance. This is also heavily negotiated.**

**[auto]** sweep worth running: scan the whole balance sheet for **interest-bearing or obligation-like
balances**, not only accounts named "loan" (*`search_accounts`*, *`get_balance_sheet`*). This is the same
technique as in `debt-and-covenant-tracking`, and in a deal each item found moves the price
pound-for-pound. **Coordinate the definition with `business-valuation`** — a QofE and a valuation using
different net debt definitions will not reconcile, and someone will notice at the worst moment.

## Step 7 — Maintenance vs. growth capex

**Reported capex includes both maintenance** (replacement to keep operating capacity) **and growth**
(expansion). For QofE and EBITDA-multiple valuation, distinguish:

- **Maintenance capex**: **the level needed to sustain current operations — a real recurring cash cost**
- **Growth capex**: **discretionary expansion**

**Free cash flow to equity holders uses total capex; for normalization, isolate maintenance capex as the
"real" recurring requirement. Document the split methodology.**

**[gated]**: **total capex is `[auto]`** (*`get_cash_flow`*, *`get_general_ledger`* on fixed-asset
accounts), and the **individual additions are readable**, which supports the split — but **the split
itself is judgment**, and it is one sellers naturally push toward "growth". A useful `[auto]` cross-check:
compare capex against depreciation over several years. **Sustained capex well below depreciation suggests
under-investment** — the business is being run for cash, and the buyer will inherit a catch-up.

## Step 8 — Forecast assessment (if management provided)

If the deal is based partly on forecast — **[gated]**: the forecast is **[manual]**, the history to test it
against is **[auto]**:

- **Test management's assumptions against history and external benchmarks** — the historical growth,
  margin and working capital trends are readable, which makes this a comparison rather than an opinion
- **Identify aggressive assumptions** (growth rates, margin expansion, working capital improvements)
- **Build a sensitivity around base / downside cases**
- **Note that this is forward-looking and inherently uncertain**

**QofE primarily validates history; forecast critique is supporting.** The most persuasive form of that
critique is simply putting the forecast next to the last three years' actuals on the same axes.

## Step 9 — Identify risks and observations

- **Customer concentration / contract risk** — **[auto]** for concentration
- **Key person dependency** — **[manual]**
- **Pending litigation / regulatory matters** — **[manual]**; see
  `contingencies-and-litigation-asc450`, whose legal-spend sweep applies here too
- **Tax exposures** (uncertain positions, historical compliance gaps) — **[manual]**
- **Accounting policy aggressiveness** — **[gated]**
- **System / data limitations** — **[auto]** to observe: how far the history reaches, whether dimensions
  are used, whether the ledger supports the analysis at all
- **Working capital seasonality / volatility** — **[auto]**
- **Deferred items** (deferred revenue / costs) **and their reality** — **[gated]**

**Each risk is an item the buyer would want addressed** — price, escrow, indemnity, or a representation in
the agreement.

## Step 10 — Output

Deliver a comprehensive `.xlsx` workbook (typical QofE binder structure).

**Sheet 1: Executive Summary** — adjusted EBITDA, key adjustments, normalized WC target, deal net debt,
top observations. Add a header block: workspace name; **which company file is the target, by
`display_name`, or that the target is not connected**; the engagement side; the LTM date; **the earliest
period the data supports**; whether any figure rests on `mock` data.

**Sheet 2: Adjusted EBITDA Bridge** — detailed by adjustment, with rationale and quantification.

**Sheet 3: Recurring "One-Time" Test — NEW, Mosofin-specific** — every add-back against the prior three
years, with the symmetry check and adjustments as a percentage of reported EBITDA.

**Sheet 4: Revenue Quality** — by customer, product, recurring / non-recurring; trends and concentration;
**period-end invoicing pattern**.

**Sheet 5: Margin Analysis** — gross and EBITDA margin trends; drivers.

**Sheet 6: Working Capital Analysis** — monthly WC, days metrics, **the normalized target under more than
one methodology**.

**Sheet 7: Net Debt and Debt-Like Items** — deal net debt walk with itemized debt-like and cash-like items,
**including the balance-sheet sweep results**.

**Sheet 8: Capex Analysis** — maintenance vs. growth split, historical and prospective, **with the capex
versus depreciation comparison**.

**Sheet 9: Forecast Assessment** (if applicable) — plausibility analysis against actual history.

**Sheet 10: Quality Observations & Risks** — itemized with severity.

**Sheet 11: Open Items / Specialist** — items requiring tax DD, legal DD, IT DD.

**Sheet 12: Coverage — NEW, Mosofin-specific**

| Task | Source (target's ledger / data room / supplied) | Verdict (auto / gated / manual) | Tool used | Periods available | Policy | `mock` | Gap |

**For a presentation-ready document, deliver as a report** (`docx` or `pptx`).

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `QofE_[Target]_[YYYY-MM-DD].xlsx`

Use the target's `display_name` where it is a connected company file. Every file states which datasource
and `display_name` it covers, or that the target was not connected.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something, **name the source required** instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

A deal iterates over months, so persisting the framework matters.

On an explicit yes, persist the **decisions**:

- **The adjustment framework**: which categories this business legitimately adjusts for, and the test
  applied to each
- **The net debt definition** — itemised, and **agreed with `business-valuation`** so the two reconcile
- **The working capital target methodology** — the measure, the period, and the alternatives shown
- **The maintenance / growth capex split methodology**
- **The related-party register** — who the related parties are and which vendors correspond to them.
  **Names and roles, not amounts**
- **The engagement side and the deal perimeter**
- **The data limitations found** — how far the history reaches, what the ledger does and does not support
- The replay recipe: the exact sequence of reads that produced the base, the WC series and the recurring
  test

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist adjusted EBITDA, the working capital target, deal net debt, customer names with revenue,
owner compensation figures, or any deal term.** This is among the most commercially sensitive material in
the pack: **a stored adjusted EBITDA is a negotiating position**, owner compensation is personal data, and
customer revenue detail would damage the target if it circulated. Much of it is also likely to be under an
NDA. **Persist the methodology; never the numbers.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Harbour
Supplies (target, sell-side) — net debt includes finance leases and deferred consideration; WC target on
LTM average; owner comp normalised to market for the role" — not "WC target on LTM average". Record the
chosen **scenario** (which file is the target, the perimeter, the side) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run — and **in a deal the connected set changes at
close**, often adding the target. **Decisions are the user's; state is the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — and here it may mean the deal completed, lapsed, or the data-room access
ended. **Ask.**

---

## Both entity scenarios

**Single-entity target.** The workflow above against one `data_source_id`. One bridge, one WC target, one
net debt.

**Multi-entity or carve-out target.** The analysis runs **once per entity**, each call targeting exactly
one `data_source_id`, every figure carrying its entity's `display_name`. Then:

- **A group target consolidates before it normalises.** Intercompany revenue and cost must be eliminated
  first, or adjusted EBITDA is overstated by whatever the entities charge each other. See
  `consolidation-and-eliminations`.
- **A carve-out is the hardest case in this skill.** A division being sold has never had standalone
  financial statements: shared costs — head office, IT, insurance, the CEO's time — were never allocated
  to it, and the standalone cost base must be **constructed**. **State clearly that carve-out figures are
  constructed rather than reported**, and show the allocation basis for every shared cost. Buyers
  scrutinise this harder than any add-back.
- **Stranded costs are the mirror image**: costs that stay with the seller after the carve-out but were
  previously absorbed by the division. They affect the seller's own future earnings, not the target's.
- **Entities inside the perimeter and outside it must be named explicitly.** A deal perimeter that differs
  from the connected set is normal, and analysing the connected set instead is a silent, material error.
- **Related-party flows between perimeter and non-perimeter entities become third-party costs
  post-deal** — often at different prices. That is a normalisation, and frequently a large one.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
