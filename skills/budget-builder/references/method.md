<!-- budget-builder · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Choose and apply the budgeting method
- Step 2 — Build the revenue budget
- Step 3 — Build the cost of goods / services budget
- Step 4 — Build the operating expense budget
- Step 5 — Assemble the operating budget
- Step 6 — Document assumptions
- Step 7 — Build flex / sensitivity (optional but recommended)
- Step 8 — Reconcile to strategic targets
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence
tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*,
not an absence — and in a forward-looking skill most of the judgment is legitimately manual.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the monthly
P&L, the customer sales history, the vendor spend and the existing budget do not depend on each
other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* with a **monthly** breakdown, over **several years** — the base, the
  seasonality, and every historical cost ratio — usually **[auto]**. This is the single most
  important read in the skill
- *`search_budgets`* — **any budget already held in the system** — usually **[auto]**
- *`search_accounts`* — the chart of accounts, to structure the budget on the entity's real lines
  — usually **[auto]**
- *`get_general_ledger`* — detail behind any line, and the payroll-loading derivation — usually
  **[auto]**
- *`get_customer_sales`* — revenue by customer, for concentration and retention shape — usually
  **[auto]**
- *`search_invoices`* / *`search_items`* — units, prices and product mix — usually **[auto]**
- *`get_vendor_expenses`* — recurring cost commitments by supplier — usually **[auto]**
- *`search_employees`* — the current roster — usually **[auto]**
- *`search_classes`* / *`search_departments`* — the department structure the budget will use —
  usually **[auto]**
- *`get_balance_sheet`* — the opening position, and depreciation-bearing assets — usually **[auto]**
- *`get_company_info`* — fiscal calendar and base currency — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it can demonstrate the model's structure
but **cannot support a budget anyone commits to**. A budget built on fixtures will be approved,
distributed, and measured against.

## Step 1 — Choose and apply the budgeting method

**Incremental budgeting**: start from prior year actuals, apply growth / inflation adjustments.
**Fast, but perpetuates existing spend.** Good for stable cost lines. **[auto]** for the base
(*`get_profit_and_loss`*); the adjustment is **[manual]**.

**Zero-based budgeting (ZBB)**: every line built from zero, justified afresh. **Rigorous,
time-consuming.** Good for discretionary spend and cost-reduction drives. **[manual]** by
definition — though the history is still worth showing, as the thing each line must be justified
*against*.

**Driver-based budgeting**: model lines as functions of business drivers (revenue = units ×
price; support cost = customers × cost-to-serve). **Most useful and dynamic — recommended for
revenue and variable costs.** **[gated]**: the historical *relationships* are measurable —
revenue per customer, cost as a percentage of revenue, cost per unit — while the future driver
values are the user's.

**Often a hybrid: driver-based for revenue and variable costs, incremental for stable overheads,
ZBB for discretionary categories. State the approach per line.** Record the method in the
assumptions register alongside each line, so a reader knows whether a number was derived,
extrapolated, or rebuilt.

## Step 2 — Build the revenue budget

**Model revenue from drivers, not a single growth rate where possible.**

**Subscription / SaaS**:
```
Beginning ARR / MRR
+ New bookings (from pipeline × close rate, or sales capacity × productivity)
+ Expansion / upsell
− Churn / contraction
= Ending ARR / MRR
Revenue recognized per the recognition pattern (per revenue-recognition-asc606)
```
**ARR / MRR** are annual and monthly recurring revenue — the run-rate of subscriptions in force.
**Churn** is revenue lost from customers leaving; **contraction** from customers downgrading;
**expansion** the reverse. **[gated]**: historical churn, expansion and beginning ARR are
derivable from customer-level revenue history (*`get_customer_sales`*, *`search_invoices`*);
pipeline and close rate are **[manual]**.

**Product / units**:
```
Revenue = Units sold × Average selling price
```
By product line, channel, or geography. **Build seasonality into monthly units.** **[auto]** for
historical units and average selling price where items are tracked (*`search_items`*,
*`search_invoices`*, *`read_invoice`*).

**Services**:
```
Revenue = Billable capacity × Utilization × Bill rate
```
Or project-based: pipeline of projects × value × timing. **[gated]**: where time is tracked,
historical utilization and effective bill rate are derivable (*`search_time_activities`* against
*`get_customer_sales`*).

**Retail / e-commerce**:
```
Revenue = Traffic × Conversion × Average order value
```
Plus same-store growth and new-store contribution. **[gated]**: average order value and
transaction counts are derivable (*`search_sales_receipts`*, *`search_invoices`*); traffic and
conversion sit in systems the books do not see, so they are **[manual]** unless a commerce
platform is connected.

**Document every revenue assumption. Build monthly with seasonality** — and derive the seasonal
shape from the entity's own monthly history rather than assuming one.

## Step 3 — Build the cost of goods / services budget

For variable costs, tie to revenue / volume drivers — **[auto]** for every historical ratio
below, which is what makes this step evidence-based rather than assumed:

- **COGS = Units × unit cost, or Revenue × COGS %** (*`get_profit_and_loss`* monthly gives the
  historical percentage, and its stability or drift)
- **Direct labor** for services
- **Hosting / infrastructure** for SaaS (often scales with usage)
- **Materials, freight, fulfillment**

**Build gross margin and check it against historical and target margins.** A budgeted margin that
departs from history needs a stated reason — a price rise, a supplier change, a mix shift — not
just a better number.

## Step 4 — Build the operating expense budget

By department / function — use the entity's **real** department structure
(*`search_departments`*, *`search_classes`*, **[auto]**) rather than a generic one.

**Personnel (usually the largest line)** — **[gated]**:

- **Roster of existing employees with current comp** — the roster is **[auto]**
  (*`search_employees`*); **compensation is [manual]** unless payroll is connected
- **Planned hires by role, start month, salary** — **[manual]**
- **Apply employer-side payroll taxes and benefits loading** (per entity, per jurisdiction —
  **don't assume a rate; use the entity's actual loading**). **[auto]** to derive: total employer
  payroll taxes and benefits divided by total wages over the last full year
  (*`get_general_ledger`*, *`get_profit_and_loss`*). **This is the difference between meeting the
  quality standard and merely claiming to** — show the derivation and the period it came from
- **Merit increases / promotions** (timing and %) — **[manual]**
- **Bonus and commission accruals** — **[gated]**; historical bonus cost is **[auto]**
- **Stock-based compensation** — **[manual]**

**Non-personnel by category** — **[auto]** for every historical base, **[manual]** for the change:

- **Rent and facilities** (from lease schedules — the schedule is **[manual]**, the historical
  charge **[auto]**)
- **Software and subscriptions** (*`get_vendor_expenses`* shows the recurring base clearly)
- **Marketing** (often driver-based: **CAC** × new customers, or % of revenue). *CAC* is customer
  acquisition cost — marketing spend divided by customers won
- **Professional fees**
- **Travel**
- **Insurance**
- **Depreciation and amortization** (from the fixed-asset register and intangibles schedules —
  registers are **[manual]**; the historical charge and the assets on the balance sheet are
  **[auto]**)
- **Other**

**Apply the chosen method per line. Build monthly.**

## Step 5 — Assemble the operating budget

```
Revenue (by stream)
− Cost of goods/services
= Gross profit (and gross margin %)
− Operating expenses (by department/category)
= Operating income (EBIT) and operating margin %
− / + Other income/expense (interest, FX)
− Tax (estimated effective rate)
= Net income
```

**Show monthly, with quarterly and annual totals.** **EBIT** is earnings before interest and tax —
the profit from operating the business, before financing and tax. The **effective tax rate** is
**[manual]**: derive the historical rate for reference (*`get_profit_and_loss`*, **[auto]**) but
**never assume a forward rate** — it depends on the jurisdiction and the entity's position.

## Step 6 — Document assumptions

**Every budget needs a clear assumptions register:**

- Each revenue driver and its assumed value / trajectory
- Each cost driver and ratio
- Headcount plan with timing
- **Inflation / escalation rates (from the user — don't assume)**
- FX rates assumed
- One-time items
- Strategic initiative budgets

**A budget without documented assumptions can't be defended or updated.**

**Mosofin addition to this register: mark each assumption's origin** — *derived from history*
(with the tool, the periods used, and the resulting figure), *supplied by the user* (with who),
or *not evidenced*. A reader can then see instantly which numbers are measurements and which are
opinions. Both are legitimate; conflating them is not.

## Step 7 — Build flex / sensitivity (optional but recommended)

Show how the budget flexes with key drivers:

- **Revenue ±10%**
- **A key cost ±10%**
- **Headcount timing shifts**

**[auto]** arithmetic once the model is built. Full scenario modeling lives in
`scenario-and-sensitivity-analysis`; a basic flex here helps stress-test the plan — particularly
the headcount timing case, which is where budgets most often break (see the edge case).

## Step 8 — Reconcile to strategic targets

Check the budget against:

- **Board / management targets** (growth, margin, profitability, cash burn) — **[manual]**
- **Prior year actuals** (reasonableness of the change) — **[auto]**, line by line, and the most
  useful reasonableness test available
- **Industry benchmarks** (if available) — **[manual]**
- **Unit economics** (per `cohort-and-unit-economics`) — does the budget imply healthy **CAC
  payback** and **LTV/CAC**? *LTV* is the lifetime value of a customer; *CAC payback* is how long
  it takes to earn back what you spent winning them. **[gated]**: historical unit economics are
  derivable, the budgeted ones follow from the drivers

**If the budget doesn't hit targets, iterate the drivers (with the user) rather than plugging
numbers.** A plugged budget is discovered in month two and discredits the whole plan.

## Step 9 — Output

Deliver an `.xlsx` budget workbook.

**Sheet 1: Budget Summary** — annual P&L with quarterly columns; key metrics and margins. Add a
header block: workspace name; each in-scope company file by `display_name`; each excluded one and
why; the currency; whether any figure rests on `mock` data.

**Sheet 2: Monthly Budget (P&L)** — full monthly detail by line.

**Sheet 3: Revenue Build** — driver-based revenue model with all assumptions.

**Sheet 4: Headcount Plan** — roster + hires with comp, taxes, benefits, timing. **Show the
loading rate and where it was derived from.**

**Sheet 5: OpEx Detail** — by department and category, monthly.

**Sheet 6: Assumptions Register** — every assumption, its value, and its source / rationale, **with
its origin marked** (derived / supplied / not evidenced).

**Sheet 7: Flex / Sensitivity** — basic scenarios.

**Sheet 8: Reconciliation to Targets** — budget vs. strategic targets and prior year.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Budget line or driver | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Periods used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be evidenced and who supplied it instead |

**Build the workbook with live formulas so the user can adjust drivers and see the P&L update.**
That matters more here than in most skills: a budget is a negotiating document, and it will be
changed in the meeting.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Budget_[FY]_[EntityName].xlsx`

In a multi-entity run, `[EntityName]` is the company file's `display_name`, one per entity plus a
consolidated file. Every file states which datasource, which `display_name`, and which currency it
covers.

**Grounding:** every historical figure traces to a tool result in this conversation; every
forward-looking figure traces to a stated assumption with a named owner. End with a single **Data
sources** line grouping calls by datasource. Where the data does not cover something, **name the
tool that would have covered it** instead of estimating.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customized
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The driver structure** — which revenue model this entity uses, which lines are driver-based,
  which incremental, which zero-based. This is the skeleton of next year's budget
- **The department and category map** — the real names, and who owns each line
- **The derivation recipes**, not the derived values: how the payroll loading rate is computed,
  which accounts feed each cost ratio, how seasonality is measured. Values are re-derived from
  fresh history every year; a frozen ratio defeats the point
- **The assumptions register template** — the list of assumptions this entity must always state
- Strategic targets and the format the board expects (see the edge case)
- Known commitments and their renewal dates
- The replay recipe: the exact sequence of reads that produced the historical base

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist salaries, individual compensation, the headcount plan, or the budget figures
themselves.** Compensation is personal data, an unannounced hiring plan is commercially sensitive,
and the numbers are one year's decisions. Persist the *structure and the method*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — driver-based revenue on units × ASP, payroll loading derived from FY24 at
18.4%, departments: Ops / Sales / G&A" — not "loading 18.4%". Entities have genuinely different
cost structures, and an unlabelled loading rate applied to the wrong company file misprices the
largest line in the budget. Record the chosen **scenario** (single vs multi, and which set) as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to
the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that
is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One budget, one assumptions
register, one workbook.

**Multi-entity.** Steps 0–9 run **once per entity**, each call targeting exactly one
`data_source_id`, every line and assumption carrying that entity's `display_name`. Then one
cross-entity step:

- **Consolidate at budgeted FX rates**, entity by entity, in each one's functional currency first.
  State the budgeted rate and **flag its sensitivity** — a consolidated budget can miss purely
  because a rate moved, and that should be visible as a separate line rather than buried in
  operating variances.
- **Eliminate intercompany revenue and cost** before presenting a group total, or the group's
  revenue is overstated by whatever the entities charge each other.
- **Shared costs allocated across entities** need a stated basis — headcount, revenue, or usage —
  and the same basis in the budget as in the actuals, or every future variance analysis will be
  measuring the allocation rather than the performance.
- **Derive drivers per entity, from that entity's own history.** A group-average seasonality or
  loading rate describes no entity. Where one entity is too new to have history, say so and borrow
  a sibling's shape **explicitly and labelled**.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each line's verdict per
company file.
