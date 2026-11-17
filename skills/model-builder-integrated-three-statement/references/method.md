<!-- model-builder-integrated-three-statement · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the historicals (grounding) — Mosofin addition
- Step 1 — Set the model architecture
- Step 2 — Normalize and map historicals
- Step 3 — Build driver-based forecast schedules
- Step 4 — Link the three statements
- Step 5 — Add model checks
- Step 6 — Deliver the working model
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The assumptions and the model construction are legitimately
the user's and the assistant's respectively.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the historicals (grounding) — Mosofin addition

**Batch independent reads into one message** — every historical period, the balances, the trial balances and
the chart do not depend on each other. **Pull the entire historical span in one go.**

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* **for every historical period, at the model's cadence** — usually **[auto]**
- *`get_balance_sheet`* **at every historical period end, including the opening date** — usually **[auto]**
- *`get_cash_flow_statement`* where the platform provides one — usually **[auto]**
- *`get_trial_balance`* at each period end — **for mapping completeness** — usually **[auto]**
- *`search_accounts`* — **the chart with types, for the account-to-line mapping** — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — **for the working capital drivers** — usually
  **[auto]**
- *`get_general_ledger`* on **debt, equity and fixed asset accounts** — for the roll-forwards — usually
  **[auto]**
- *`search_employees`* — headcount history, an opex driver — usually **[auto]**
- *`get_company_info`* — legal name, **currency, year-end** — usually **[auto]**

**Match the cadence to the model.** A monthly model needs monthly historicals; **pulling annual figures and
dividing by twelve destroys exactly the seasonality the model should capture.**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a model built on fixtures will be used to raise
money, set a budget or price a transaction.** **Stop.**

## Step 1 — Set the model architecture

**Create separate sections or tabs for** — **[manual]** construction:

- **Control panel**: scenario, forecast horizon, currency, units, and model status
- **Source historicals**: **immutable imported statements and mapping**
- **Assumptions**: **editable drivers only, clearly separated from formulas**
- **Operating forecast**: revenue, cost of sales, opex, headcount, working capital, capex, debt, tax
- **Financial statements**: P&L, balance sheet, cash flow
- **Checks**: **balance sheet, cash roll-forward, retained earnings, debt, working capital, and sign
  checks**

**Use consistent time periods across every schedule. Historical periods should flow into forecast periods
without broken formulas or manual re-entry.**

**Mosofin additions to the control panel and the source tab:**

- **The control panel records the workspace, the entity `display_name`, and the as-at date of the source
  pull.** **A model is opened months later by someone who was not in this conversation**, and those three
  facts are what make it interpretable.
- **The source historicals tab records, per line, the tool call and parameters that produced it.** That
  makes the model **refreshable** — the next build is the same calls with later dates — and it makes it
  **auditable** by a financial model review.

**Immutable means immutable.** The source tab is the imported history; **forecast formulas never write into
it**, and corrections go through the mapping, not by typing over a historical.

## Step 2 — Normalize and map historicals

**Validate that source statements tie before forecasting** — **[auto]**, all five:

- **P&L sums to reported net income**
- **Balance sheet balances in every historical period**
- **Cash flow reconciles opening cash to ending cash**
- **Retained earnings roll-forward matches net income, dividends, and other equity movements**
- **Account mappings are complete and no source rows are unmapped**

**If historicals do not tie, pause and return a source issue list before building the forecast layer.**

**This is the gate, and the workspace makes it real.** Notes on each:

| Validation | How | Note |
|---|---|---|
| **P&L sums to net income** | *`get_profit_and_loss`* | Trivially true from a platform report; **meaningful if lines were remapped** |
| **Balance sheet balances** | *`get_balance_sheet`* | **True by construction from the platform** — see `financial-statement-builder`. **It becomes a real check once mapped into model lines** |
| **Cash flow reconciles** | *`get_cash_flow_statement`*, or balance movements | **The genuine one.** Platform cash flow reports often misclassify; see `cash-flow-statement-indirect-method` |
| **Retained earnings rolls forward** | *`get_balance_sheet`*, *`get_profit_and_loss`* | **Frequently fails** — distributions, prior-period adjustments, reclassifications |
| **Mapping is complete** | *`get_trial_balance`* vs. the mapping | **The most valuable of the five.** **Every account must land on exactly one model line**, and the mapped total must equal the trial balance total |

**The mapping check deserves emphasis.** **An unmapped account is the commonest way a model's historicals
quietly differ from the accounts** — the model foots internally, the trial balance foots, and they are not
the same number. **Test it explicitly: sum the mapped accounts and compare to the trial balance total.**

**Produce the source issue list** where anything fails: **the account, the period, the amount, and which
validation it broke.** **Then stop.** Building a forecast on unreconciled history is the failure this step
exists to prevent.

## Step 3 — Build driver-based forecast schedules

**Forecast from drivers rather than hardcoded outputs** — **[manual]** for the forward values, **[auto]** for
every historical value:

- **Revenue**: **volume × price, customers × ARPU, bookings to revenue, same-store growth**, or other
  business-specific drivers — **[gated]**: **historical volume and price are computable from invoice line
  detail** where it exists; customer counts are `[auto]`; **ARPU and bookings need the billing system** —
  see `kpi-dashboard-builder`
- **Gross margin**: **unit economics, mix, direct cost drivers, or explicit margin assumptions** —
  **[auto]** historically, by period and by segment
- **Opex**: **headcount, department spend, percent of revenue, fixed/variable split, or contract-level
  assumptions** — **[auto]** historically: **spend by department, headcount, and the ratio to revenue**;
  **the fixed/variable split is `[manual]` judgment**
- **Working capital**: **DSO, DIO, DPO, deferred revenue days, prepaids, accrued expenses, or turnover
  ratios** — **[auto]** historically, **all of them**, and **the most reliably computable driver set in the
  model**
- **Capex and depreciation**: **additions, useful lives, depreciation method, disposals, and accumulated
  depreciation** — **[gated]**: **historical additions and depreciation are `[auto]`** from the asset
  accounts; **useful lives and methods are `[manual]`** — see `fixed-asset-register-and-depreciation`
- **Debt and interest**: **opening debt, draws, repayments, amortization, cash sweep, rates, and
  covenants** — **[gated]**: **balances and the effective historical rate are `[auto]`**; **the amortisation
  schedule, the sweep mechanics and the covenants are `[manual]`** — see `debt-and-covenant-tracking`
- **Taxes**: **book tax rate, cash taxes, NOLs, valuation allowance, and timing differences when material** —
  **[gated]**: **the historical effective rate is `[auto]`**; **NOLs and the statutory rate are `[manual]`**

**Keep assumptions visible and editable. Never bury assumptions inside formulas.**

**Mosofin practice — present history beside every assumption field.** For each driver, the assumptions tab
should show:

| Driver | Historical periods | Assumption |
|---|---|---|
| DSO | 44 / 47 / 51 days | *(user input)* |
| Gross margin | 61.2% / 59.8% / 58.4% | *(user input)* |
| Opex % of revenue | 38% / 41% / 43% | *(user input)* |

**Three periods of history against every input.** It costs nothing, it makes each assumption arguable, and
**it exposes the assumption nobody would defend if they saw the trend** — a margin forecast at 62% against
three years of decline, for instance.

**Never fill the assumption column.** Present the history; the forecast is the user's.

## Step 4 — Link the three statements

**Connect the model in this order** — **[manual]** construction:

1. **P&L produces net income.**
2. **Working capital, capex, debt, tax, equity, and fixed asset schedules produce balance sheet movements.**
3. **Cash flow statement starts with net income, adjusts for noncash items and working capital, then
   investing and financing flows.**
4. **Ending cash from cash flow links to balance sheet cash.**
5. **Retained earnings links from prior retained earnings plus net income less dividends and
   distributions.**
6. **Balance sheet check confirms assets equal liabilities plus equity.**

**Every forecasted statement line should either link to a supporting schedule, a historical source row, or a
named assumption.**

**That last sentence is the model's integrity rule**, and it is testable: **every forecast cell traces to one
of three places.** Anything else is a hardcode — which is exactly what
a financial model review will find.

**The opening balance sheet is the join** between the `[auto]` history and the `[manual]` forecast. **Get it
from the source tab, not by typing it**, and **confirm it is the last closed period** — an opening position
taken from an open month will move.

## Step 5 — Add model checks

**At minimum include** — **[manual]** to build, and **each mirrors a check the workspace performs on the
history**:

- **Balance sheet check by period**
- **Cash roll-forward check**
- **Retained earnings roll-forward check**
- **Debt roll-forward check**
- **Fixed asset roll-forward check**
- **Working capital sign check**
- **Formula consistency check across periods**
- **Hardcode-in-formula check for forecast periods**
- **Missing source mapping check**

**Use a clear status convention:**

- **PASS**: no material check failures
- **WARNING**: immaterial issue or user-confirmed judgment item
- **HOLD**: **balance break, source tie-out failure, broken link, circularity, or missing required input**

**Note that checks 1 through 6 and check 9 apply to the historical columns too** — and **there they are
`[auto]`, from Step 2.** **Run them across history and forecast in the same row**, so a break is immediately
attributable to one side or the other. **A balance check that fails only in forecast periods is a modelling
error; one that fails in history is a source problem**, and the fix is completely different.

## Step 6 — Deliver the working model

**The deliverable should include** — **[manual]**:

- **Working workbook or structured model file**
- **Source mapping tab or table**
- **Assumptions tab with editable drivers**
- **Fully linked P&L, balance sheet, and cash flow**
- **Support schedules**
- **Check dashboard**
- **Short build notes covering assumptions, limitations, and unresolved items**

**Do not flatten formulas unless asked. Preserve formulas so users can edit assumptions and see the model
recalculate.**

**Mosofin additions to the deliverable:**

- **A Source & Refresh tab** — the workspace, the entity `display_name`, the as-at date, **and the tool
  calls behind each historical line**, so the model can be refreshed rather than rebuilt.
- **A Coverage tab** — | Task | Verdict | Source | As-at date | `mock` | Gap | — **making clear that the
  history is `[auto]` and every assumption is `[manual]`.**
- **The build notes state which assumptions were supplied by the user**, and **that none were generated.**
  For a fundraising or lender model that distinction matters.

**File naming (Mosofin addition — the original specifies none):**
`Model_[EntityName]_[YYYY-MM-DD].xlsx`

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**Grounding:** every historical figure traces to a tool result in this conversation; every forecast figure
traces to a schedule, a historical row or a named assumption. End with a single **Data sources** line.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The account-to-model-line mapping** — **the most valuable stored asset here**, and the thing that makes
  the next build a refresh
- **The model architecture** — tabs, sections, conventions
- **The driver definitions** — how DSO, margin, opex ratios and the rest are computed for this entity,
  **so historical values stay comparable between builds**
- **The check set** and the status conventions
- **The cadence and horizon** normally used, and for which purpose
- **The schedule sources** — where the debt, lease and fixed asset schedules come from and who maintains
  them
- **The consolidation basis**, if the model is a group model
- **The refresh recipe** — the exact sequence of reads that produced the historicals
- **Known mapping exceptions** — accounts deliberately excluded, and why

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist historical figures, driver values, assumptions, forecasts or the model itself.** All state —
**and a model built for a fundraising, a transaction or a board decision is confidential.** **Persist the
mapping and the architecture; rebuild the numbers.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Group — consolidated monthly model, Revenue maps 4000–4090, opex by department class, DSO on trailing
3-month revenue, opening at last closed month" — not "Revenue maps 4000–4090". **Mappings and driver
definitions are chart-specific**, and reusing them across entities produces historicals that look right and
are not. Record the chosen **scenario** (single vs multi, consolidated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity model.** The workflow above against one `data_source_id`.

**Consolidated model.** The historicals must be consolidated, which means:

- **Eliminate intercompany before the historicals enter the model** — see
  `consolidation-and-eliminations` and `intercompany-reconciliation`. **A model built on summed entity
  figures overstates revenue and cost by the intercompany amount**, and **every margin and every working
  capital driver computed from it is wrong.**
- **Compute drivers from consolidated figures**, not as averages of entity drivers. **Group DSO is group
  receivables over group revenue** — not the mean of the entities' DSOs.
- **Decide whether the model forecasts by entity and consolidates, or forecasts the consolidated group.**
  Both are legitimate; **the first is more work and more useful when entities behave differently**, and it
  requires eliminations in the forecast layer too — which is a set of model checks in its own right.
- **Currency**: entities in different currencies need translation before consolidation, and **the model
  needs a rate assumption for forecast periods** — a `[manual]` input that is easy to forget and material.
  See `foreign-currency-translation-asc830`.
- **A disconnected group member leaves a hole in the history** that no assumption can fill honestly. Say so.
- **Non-controlling interests** flow through the equity roll-forward and are frequently omitted from models
  built from consolidated statements. Check for them.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
