<!-- kpi-dashboard-builder · method.md · read for: Stages 3–6 — choosing, defining, computing and laying out the KPIs. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Select the right KPIs for the business
- Step 2 — Define each KPI precisely
- Step 3 — Compute the KPIs
- Step 4 — Add targets and benchmarks
- Step 5 — Design the layout
- Step 6 — Build trends and supporting detail
- Step 7 — Add alerts and commentary
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The operational metrics are legitimately `[manual]` where
their systems are not connected, and naming the source required is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the multi-period statements, the balances and the dimensions
do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* **by month for 24–36 months** — **the trend base for every income metric** —
  usually **[auto]**
- *`get_balance_sheet`* **at each period end over the same span** — **the trend base for every balance
  metric and ratio** — usually **[auto]**
- *`get_cash_flow_statement`* where available — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — **for DSO and DPO** — usually **[auto]**
- *`search_accounts`* — the chart, for metric definitions that name accounts — usually **[auto]**
- *`search_classes`* / *`search_departments`* / *`search_locations`* — **segment dimensions, for by-segment
  metrics** — usually **[auto]**
- *`search_employees`* — headcount, for per-employee metrics — usually **[auto]**
- *`search_items`* — for inventory metrics — usually **[auto]**
- *`get_company_info`* — legal name, currency, **fiscal calendar**, industry — usually **[auto]**

**Pull the full history in one go.** **A dashboard is trends**, and fetching 24 months costs the same round
trip as fetching one.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that metric to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a dashboard goes to a board or an investor**,
and a fixture-derived metric there is a serious matter. **Label it on the dashboard face, not in a note.**

## Step 1 — Select the right KPIs for the business

**Choose metrics that drive decisions, not vanity metrics. Tailor to industry.** Each set below carries its
verdict.

**SaaS / Subscription** — **`[manual]` unless a billing or CRM system is connected**:
- **MRR / ARR and growth rate**
- **Net new ARR** (new + expansion − churn − contraction)
- **Net revenue retention (NRR) and gross revenue retention (GRR)**
- **Logo churn and revenue churn**
- **CAC (customer acquisition cost)**
- **CAC payback period**
- **LTV and LTV/CAC ratio**
- **Magic number / sales efficiency**
- **Rule of 40** (growth % + profit margin %) — **[gated]**: **the profit half is `[auto]`**, the growth half
  needs ARR
- **Burn rate and runway** — **[auto]**; these are cash metrics
- **ARPA / ARPU** — needs a customer count

**E-commerce / Retail** — **mixed**:
- **Revenue, same-store sales growth** — **[gated]**; revenue `[auto]`, same-store needs location tagging
- **Gross margin, contribution margin** — **[auto]**
- **AOV (average order value)** — **[gated]**; needs order counts
- **Conversion rate** — **[manual]**; web analytics
- **Traffic and CAC** — **[manual]**
- **Repeat purchase rate / customer retention** — **[gated]**; derivable from invoice history where
  customers are tracked
- **Inventory turnover, days inventory** — **[auto]**
- **Return rate** — **[gated]**; credit memos are readable
- **Sell-through rate** — **[manual]**

**Professional Services** — **mostly `[manual]` without a time system**:
- **Utilization rate** — **[manual]**
- **Realization rate** (billed vs. standard) — **[manual]**
- **Average bill rate** — **[manual]**
- **Revenue per billable employee** — **[gated]**; revenue `[auto]`, **billable** headcount `[manual]`
- **Project margin** — **[gated]**; **`[auto]` where projects are tracked as classes**
- **Backlog / pipeline** — **[manual]**
- **WIP and unbilled** — **[auto]** where posted to the balance sheet

**Manufacturing** — **mixed**:
- **Gross margin, contribution margin** — **[auto]**
- **Capacity utilization** — **[manual]**
- **OEE (overall equipment effectiveness)** — **[manual]**
- **Inventory turns, days inventory** — **[auto]**
- **On-time delivery** — **[manual]**
- **Scrap / yield rate** — **[gated]**; scrap posted to an account is readable, yield is not
- **Cost variances (PPV, MUV)** — **[auto]** where variance accounts exist

**General financial (all entities)** — **`[auto]`, every one**:
- **Revenue growth (MoM, YoY)**
- **Gross / operating / net margin**
- **EBITDA and margin**
- **Operating cash flow and free cash flow**
- **Cash balance and runway**
- **DSO, DPO, DIO, cash conversion cycle**
- **Current ratio, quick ratio**
- **Debt/EBITDA, interest coverage**
- **Return on equity / assets / invested capital**

**Select 8–15 KPIs for an executive dashboard — enough to cover the business, few enough to focus. More for
a detailed operational dashboard.**

**Mosofin addition to selection: choose against the capability map, and show the user what they are
choosing.** Present the shortlist with each metric's verdict, so **a metric that requires a system nobody
has is declined deliberately rather than promised and then missing.** **A dashboard where three tiles read
"data not available" is a failed dashboard**; one where the user knowingly picked ten computable metrics is
not.

## Step 2 — Define each KPI precisely

**Ambiguous definitions destroy dashboards. For each KPI, document:**

- **Exact formula** — numerator and denominator
- **Data source**
- **Period basis** — point-in-time, period total, trailing-twelve-months
- **Inclusions / exclusions** — e.g. does ARR include one-time fees? does churn include downgrades?
- **Currency / units**

**Example — Net Revenue Retention:**
```
NRR = (Starting ARR + Expansion − Contraction − Churn) / Starting ARR
    measured for a cohort over a defined period (e.g., trailing 12 months)
    Excludes new-customer ARR
```

**A KPI without a precise, consistent definition will be computed differently each period and mislead. This
is the most important step.**

**Mosofin addition — make the definition executable.** For every `[auto]` metric, **the data source is a
tool call with parameters, and the formula is arithmetic over its result.** **Record it that way:**

| Definition element | Recorded as |
|---|---|
| **Exact formula** | the arithmetic, naming the accounts or lines used |
| **Data source** | **the tool, the parameters, the entity `display_name`** |
| **Period basis** | the date arguments passed |
| **Inclusions / exclusions** | **the accounts included and excluded, by number** |
| **Currency / units** | from the entity profile |

**A definition recorded this way cannot drift**, because next period is the same call with new dates.
**That is the structural answer to the problem this step exists to solve**, and it is why Step 9 persists
recipes rather than numbers.

**For `[manual]` metrics the definition still gets written in full** — formula, source system, basis,
inclusions — **because the definition is the thing that has to be agreed before anyone can supply the
number.**

## Step 3 — Compute the KPIs

**Calculate each KPI from the source data for the current period and historical periods (for trends).**
**Verify:**

- **Formulas applied consistently across periods** — **[auto]** by construction where the recipe is stored
- **No definition drift between periods** — **[auto]**, same reason
- **Reconciliation to source** — e.g. **total ARR ties to the billing system; revenue ties to the
  financials** — **[gated]**: **the financial half is `[auto]` and is exactly what the workspace proves**;
  the billing half needs that system

**Report the tie-out.** "Revenue on the dashboard equals revenue per the profit and loss for each period
shown" is a one-line assurance that costs one comparison and prevents the commonest dashboard failure — a
metric that quietly stops agreeing with the accounts.

## Step 4 — Add targets and benchmarks

For each KPI:

- **Target** — from budget, board goals, or management — **only if the user provides it; don't invent
  targets.** **[gated]**: **budget figures may be readable** where the platform holds them
- **Benchmark** — industry comparison — **only if the user provides reliable benchmark data.**
  **[manual]**, always
- **Prior period** for trend — **[auto]**
- **Status vs. target** — on track / at risk / off track — **with a clear rule** — **[gated]**: the rule is
  the user's, the evaluation is arithmetic

**State the status rule explicitly.** "At risk = within 5% below target" is a rule; a red dot is not.

## Step 5 — Design the layout

**A good dashboard:**

- **Most important KPIs first** — top-left, biggest
- **Grouped logically** — growth, profitability, efficiency, liquidity
- **Trend visible** — sparklines or small trend charts, **not just a single number**
- **Target / actual comparison** — variance shown
- **Status indicators** — colour or symbol for on / off track — **used sparingly and meaningfully**
- **Period and as-of date clearly labeled**
- **No clutter** — **every element earns its place**

**For each KPI tile: current value, trend, vs. target, vs. prior.**

**Mosofin additions to every tile**: **the as-at date** and, **where a metric is `[manual]` or supplied,
its source and date.** A dashboard mixing metrics computed this morning with a figure someone emailed last
month **needs to show which is which.**

## Step 6 — Build trends and supporting detail

Behind the headline tiles — **[gated]**:

- **Time series for each KPI** — 12+ months where available — **[auto]** for financial metrics
- **Drill-down detail for any KPI that needs context** — **[auto]**: **the account-level or
  transaction-level detail behind a financial metric is readable**, which makes drill-down real rather than
  decorative
- **Cohort views for retention metrics** — **[manual]** without a billing system
- **Waterfall / bridge for ARR or revenue movements** — **[gated]**: **a revenue bridge by segment or
  customer is `[auto]`**; **an ARR bridge is not**

## Step 7 — Add alerts and commentary

- **Flag KPIs that breached a threshold or trend adversely** — **[auto]** given the rules
- **Brief commentary on notable movements** — link to `budget-vs-actual-analysis` for variance drivers —
  **[gated]**: **the movement is `[auto]`, the driver usually is not.** See that skill, where the same split
  applies
- **Highlight the 2–3 things the audience most needs to know** — **[manual]** judgment

**Describe movements; attribute them only with evidence.** "Gross margin fell 3.1 points" is `[auto]`;
"because of the supplier price increase" is a claim needing support.

## Step 8 — Output

**Deliver the dashboard. Two common forms:**

**Option A — Excel dashboard (`.xlsx`):**

- **Dashboard tab**: the visual layout with tiles, trends, status
- **Data tab**: the underlying KPI calculations by period
- **Definitions tab**: **the precise definition of every KPI** — **and, for `[auto]` metrics, the tool call
  and parameters behind it**
- **Source tab**: links to source data and tie-outs

**Build with live formulas so it refreshes when source data updates.**

**Add two Mosofin tabs:**

- **Coverage tab**: | KPI | Entity (`display_name`) | Verdict | Source | As-at date | `mock` | Gap |
- **Not Available tab**: **every metric considered and declined for lack of a data source**, with the system
  that would supply it. **This is what turns a short dashboard into a deliberate one.**

**Option B — Interactive HTML dashboard:**

**If the user wants an interactive web dashboard, build it as a self-contained HTML/JS artifact. Include the KPI tiles, charts, and
filters; keep data in-memory (no external calls).**

*Mosofin note*: **in-memory data means the values are a snapshot** — **stamp the as-at date and the entity
prominently**, because an HTML file circulates and outlives its data.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `KPI_Dashboard_[EntityName]_[YYYY-MM].xlsx`

`[EntityName]` is the company file's `display_name`, or the group name for a consolidated dashboard.

**Grounding:** every computed metric traces to a tool result in this conversation; every supplied metric is
labelled with its source and date. End with a single **Data sources** line. Where a metric could not be
computed, **name the system required** instead of estimating it.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The metric set** chosen for this entity and audience, **and the metrics declined with their reason**
- **The full definition of each metric** — formula, basis, inclusions and exclusions
- **The query recipe for every `[auto]` metric** — **the tool, the parameters, the accounts.** **The most
  valuable stored asset here, because it is what makes definition drift impossible**
- **The account and dimension map** each metric depends on
- **The status rules** — what counts as on track, at risk, off track
- **The layout** — grouping, order, which metrics lead
- **The target source** — budget, board, management — **and the cadence for refreshing them. Not the target
  values**
- **The benchmark sources** the user trusts, **by citation**
- **The reporting frequency and audience**
- **Which operational systems would need connecting** to unlock the declined metrics
- The replay recipe: the exact sequence of reads that produced the trend base

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist metric values, trends, targets or any figure.** All state, and **a dashboard's whole purpose
is to show current values** — a stored number would be shown as current and be wrong. **Persist the recipe;
recompute the value.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — board dashboard, 11 metrics, gross margin excludes freight (5200), DSO on trailing 3-month
revenue, targets from board plan refreshed annually" — not "11 metrics, DSO on trailing 3-month". **Metric
definitions name accounts, and accounts are entity-specific**, so a recipe applied to another company file
computes something different under the same label. Record the chosen **scenario** (single vs multi,
per-entity vs consolidated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One metric set, one trend base.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`, every
metric carrying its entity's `display_name`. Then the points specific to metrics:

- **Ratios do not consolidate by addition.** **A group margin is group profit over group revenue — not the
  average of the entities' margins**, and not their sum. **Compute every ratio from consolidated
  components**, never from the components' ratios. This is the most common multi-entity dashboard error and
  it is silent.
- **Consolidated metrics need intercompany eliminated first.** **Group revenue that includes intra-group
  sales is overstated**, and so is every margin and growth figure built on it.
  **Compute from consolidated figures, not from summed entity figures.**
- **Per-entity dashboards and a group dashboard answer different questions.** Ask which; **producing both is
  often right**, and mixing them in one view is not.
- **Currency**: entities in different currencies cannot have their metrics added at all. **Translate first**
  and **state the rate basis on the dashboard**, since a
  growth rate can be entirely an FX movement.
- **Cash and runway are group questions with an entity catch**: cash trapped in a subsidiary that cannot
  distribute it is not group liquidity in any useful sense. **Show cash by entity where that matters.**
- **A metric available in one entity and not another** cannot be shown as a group figure. **Report coverage
  per entity.**

Capability is checked **per entity** at Gate 2; the coverage sheet shows each metric's verdict per company
file.
