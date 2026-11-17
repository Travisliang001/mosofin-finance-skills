<!-- cohort-and-unit-economics · method.md · read for: Stages 3–6 — cohorts, retention, CAC, LTV and the ratios. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Define cohorts
- Step 2 — Build the retention cohort table
- Step 3 — Derive retention curves
- Step 4 — Compute customer lifetime
- Step 5 — Compute CAC
- Step 6 — Compute LTV
- Step 7 — Compute the key ratios
- Step 8 — Assess health
- Step 9 — Segment analysis
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not
an absence — and here the gaps (channel, cost-to-serve) are precisely where the most valuable
findings usually sit, so naming them tells the user what to instrument next.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — customer sales,
invoice history, the customer master and the P&L do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_customer_sales`* with a **monthly** breakdown over the full history — **revenue per customer
  per period**, the raw material of the entire cohort triangle — usually **[auto]**
- *`search_invoices`* over the full history — **first-invoice dates (acquisition) and per-invoice
  detail** — usually **[auto]**
- *`search_customers`* / *`get_customer`* — the customer master, status and geography — usually
  **[auto]**
- *`search_sales_receipts`* — revenue from customers who never receive an invoice, common in
  transactional models — usually **[auto]**
- *`search_credit_memos`* / *`search_refund_receipts`* — credits and refunds that must reduce cohort
  revenue — usually **[auto]**
- *`get_profit_and_loss`* with a monthly breakdown — **sales & marketing spend** and **gross margin**
  — usually **[auto]**
- *`search_accounts`* — to identify which accounts constitute acquisition cost — usually **[auto]**
- *`search_items`* — plan or product tier, for segmentation — usually **[auto]**
- *`get_company_info`* — currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — retention curves and an LTV/CAC verdict
built on it would drive real investment decisions from imaginary customers.

## Step 1 — Define cohorts

**A cohort = customers grouped by when they were acquired** (e.g. "Jan 2025 cohort" = all customers
who started in Jan 2025).

Decide — **[gated]**:

- **Cohort period** (monthly is standard; quarterly for smaller volumes). **[auto]** to check volume:
  if monthly cohorts average a handful of customers, the curves will be noise — recommend quarterly
- **What "acquired" means** — **first payment? contract start? signup?** **[auto]** for *first
  invoice* and *first payment*, which are both readable and often differ by weeks; **[manual]** for
  signup, which lives in a product system. **State the definition used**, because it shifts every
  cohort boundary
- **Segmentation** — analyze all customers together, or split by plan / channel / geography

## Step 2 — Build the retention cohort table

**The classic triangle: rows = cohorts, columns = periods since acquisition (Month 0, 1, 2, …). Each
cell = the metric for that cohort at that age.** **[auto]** to construct from customer revenue by
month.

Two common versions:

**Logo (customer count) retention**:
```
Cell = % of the cohort's original customers still active at that age
```

**Revenue retention** (more important for most businesses):
```
Cell = revenue from the cohort at that age / cohort's revenue at Month 0
```

**Revenue retention can exceed 100% if expansion (upsell) outpaces churn — the hallmark of a strong
subscription business.**

**Build both tables. Add an average retention curve across cohorts.**

One definitional care point that a connected workspace forces you to confront: **"still active" is not
a field in the books.** It must be defined as *transacted within the period* (or within a tolerance
window for irregular billing). Say which definition you used — a quarterly-billing customer looks
churned in two of every three months under a naive monthly test.

Net revenue of **credits and refunds** (*`search_credit_memos`*, *`search_refund_receipts`*,
**[auto]**), or a refunded month overstates retention.

## Step 3 — Derive retention curves

From the cohort table, plot the average retention by age — **[auto]**:

- **Logo retention curve** (typically declining)
- **Revenue retention curve** (may decline, flatten, or rise depending on expansion)

Identify:

- **Early churn** (Month 0–3 drop — onboarding / fit issues)
- **Steady-state retention** (where the curve flattens — the "sticky" core)
- **Net expansion** (if revenue retention rises over time)

Average across cohorts **only over ages every cohort has actually reached**. Averaging Month 18 across
cohorts where only the oldest two have reached Month 18 mixes a cohort average with a survivorship
artefact.

## Step 4 — Compute customer lifetime

From retention — **[auto]**:

- **Average customer lifetime ≈ 1 / churn rate** (for a constant monthly churn rate)
  - e.g. **2% monthly churn → ~50 month average lifetime**
- Or, **more accurately, derive from the actual retention curve** (sum of survival probabilities)

**Use the actual curve where available rather than the simplistic 1/churn formula, which assumes
constant churn.** In a connected workspace the actual curve *is* available, so the shortcut should be
shown only as a comparison — and where the two differ materially, that difference is a finding: it
means churn is front-loaded and the simple formula is overstating lifetime.

Where the curve has not yet flattened, say the lifetime is **bounded below** by observed data rather
than extrapolating a tail nobody has seen.

## Step 5 — Compute CAC

```
CAC = Total sales & marketing spend in a period / Number of new customers acquired in that period
```

**[auto]** for both terms once the account set is confirmed: spend from the P&L
(*`get_profit_and_loss`*, *`get_general_ledger`*), new customers from first-invoice dates.

Decisions that matter — **[manual]**:

- **Fully-loaded vs. paid-marketing-only**: **fully-loaded CAC includes sales salaries, commissions,
  marketing spend, tools, and overhead. Paid-only is just ad spend. Fully-loaded is the honest
  number. State which.** **[auto]** to compute either once the user names the accounts — and worth
  computing **both**, since the gap between them is often startling and is itself the argument for
  using the honest one
- **Attribution lag**: **spend in one period may acquire customers in the next. Use a sensible
  matching window.**
- **Blended vs. by-channel**: **blended CAC hides channel differences; by-channel CAC reveals which
  channels are efficient.** **[manual]** in an accounting-only workspace — channel is not a ledger
  field. **Report blended CAC and say explicitly that the channel view could not be produced**, so
  the limitation is visible rather than implied

## Step 6 — Compute LTV

**LTV = the total contribution a customer generates over their lifetime.**

```
LTV = Average revenue per customer per period
      × Gross margin %        ← use contribution margin, not revenue
      × Average lifetime (in periods)
```

Or, using the retention curve and discounting:
```
LTV = Σ over periods [ (revenue per period × gross margin %) × survival probability × discount factor ]
```

**Critical: LTV must be on a margin (contribution) basis, not revenue. A customer paying $100/month
at 20% margin is worth far less than one at 80% margin. Using revenue overstates LTV — a common and
serious error.**

**[auto]** for revenue per period, lifetime and company-level gross margin. **[gated]** for the
margin actually applied: using one company-wide percentage for every customer is a defensible
simplification **only if stated**, and it is the assumption that hides negative-contribution
customers. Where the user can supply cost-to-serve variation — by plan, by size, by service
intensity — apply it and say so.

**Include expansion in the revenue-per-period if the cohort data shows net expansion** — **[auto]**
to detect, since it is exactly what the revenue retention curve measures.

## Step 7 — Compute the key ratios

**LTV/CAC ratio**:
```
LTV / CAC
```
**A common rule of thumb is ≥ 3.0 indicates healthy unit economics, but this is a guideline, not a
law — interpret in context (growth stage, margin profile, payback). State it as a benchmark, not a
target the user must hit.**

**CAC payback period**:
```
CAC / (Average revenue per customer per period × Gross margin %)
```
**How many periods to recover the acquisition cost on a contribution basis. Shorter is better; this
drives cash dynamics (long payback = cash-hungry growth).** Where the entity is cash-constrained,
payback matters more than LTV/CAC — connect it to `cash-flow-forecast-13-week`.

**Contribution margin per customer**: **revenue − cost-to-serve (variable), per customer per period.**

All **[auto]** arithmetic on the inputs above; the interpretation is the user's.

## Step 8 — Assess health

Synthesize a verdict — **[gated]**:

- **Is LTV/CAC healthy, and is the LTV computed on margin (not revenue)?**
- **Is payback short enough for the entity's cash position?**
- **Is net revenue retention strong (expansion offsetting churn)?**
- **Are later cohorts retaining better than earlier ones (improving product / fit)?** — **[auto]**,
  and one of the most valuable outputs: comparing cohort curves against each other is direct evidence
  of whether the product is getting stickier
- **Are CAC and payback trending the right way?** — **[auto]** across periods

**A business can show strong aggregate growth while unit economics deteriorate (rising CAC, falling
retention) — cohort analysis exposes this.** Say it plainly when the data shows it; this is the whole
point of the exercise, and the finding is often unwelcome.

## Step 9 — Segment analysis

Where data allows, repeat for segments:

- **By acquisition channel** (which channels produce the best LTV/CAC?) — **[manual]**, the biggest
  gap in an accounting-only workspace
- **By plan / tier** — **[auto]** where plans map to items or products (*`search_items`*,
  *`search_invoices`*)
- **By customer size** — **[auto]**, banding customers by their own revenue
- **By geography** — **[auto]** in part, from customer addresses (*`get_customer`*)

**Often one segment subsidizes another; segment views guide where to invest.** Run every segment the
data supports, and **name the ones it does not** — "we could not analyse by channel" is actionable
advice about instrumentation, not a shrug.

## Step 10 — Output

Deliver an `.xlsx` workbook.

**Sheet 1: Unit Economics Summary** — CAC, LTV (margin-based), LTV/CAC, payback, contribution margin,
with the health verdict and definitions. Add a header block: workspace name; the entity by
`display_name`; each excluded company file and why; **the earliest cohort available**; the acquisition
definition used; whether any figure rests on `mock` data.

**Sheet 2: Logo Retention Cohort Table** — the triangle, with average curve.

**Sheet 3: Revenue Retention Cohort Table** — the triangle, with average curve and net-expansion view.

**Sheet 4: Retention Curves** — chart data for logo and revenue retention by age. **Mark the age
beyond which not every cohort has data.**

**Sheet 5: CAC Detail** — by period, blended and by channel; fully-loaded vs. paid. **Where channel is
unavailable, the column says so rather than being omitted.**

**Sheet 6: LTV Calculation** — the full build, **on a margin basis**, with and without discounting,
**stating whether one company-wide margin was applied to all customers**.

**Sheet 7: Segment Analysis** — unit economics by channel / plan / segment, with unavailable segments
named.

**Sheet 8: Definitions** — precise definition of every metric, including **"active"** and
**"acquired"** as operationalised here.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Metric or input | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Periods / sample | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Cohort_Unit_Economics_[EntityName]_[YYYY-MM].xlsx`

`[EntityName]` is the company file's `display_name`; in a multi-entity run, one per entity plus a
combined view where customers are genuinely shared. Every file states which datasource and
`display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does
not cover something, **name the tool that would have covered it** instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The cohort definition**: cohort period, what "acquired" means, and the "active" test — the three
  choices that make one run comparable to the next. Change any of them and every historical curve
  moves
- **The S&M account set** and whether CAC is fully-loaded or paid-only
- **The margin basis**: company-wide gross margin, or a per-segment cost-to-serve map if one exists
- **The segmentation available**, and which segments are known to be unavailable and why
- **The discount rate**, if a discounted LTV is used
- **Cohorts known to be distorted** by a one-time event, so they are excluded from averages
  consistently
- The replay recipe: the exact sequence of reads that produced the triangle

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist customer names, customer-level revenue, or the cohort tables.** Customer revenue
detail is commercially sensitive and identifies real businesses or individuals; the tables are a
snapshot. Persist the *definitions and the method*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — monthly cohorts, acquired = first invoice, active = invoiced within 45 days,
fully-loaded CAC from accounts 6200–6260" — not "monthly cohorts". Entities can have quite different
billing rhythms, and an unlabelled "active" window applied to the wrong company file manufactures
churn that did not happen. Record the chosen **scenario** (single vs multi, whether customers are
shared, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every cohort figure is state, rebuilt each time.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is
no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One triangle, one set of unit
economics.

**Multi-entity.** The analysis runs **once per entity**, each call targeting exactly one
`data_source_id`, every cohort carrying that entity's `display_name`. Then:

- **Ask whether customers are shared before combining anything.** A customer billed by two group
  entities is **one customer**. Counting them twice inflates acquisitions, halves apparent revenue per
  customer, and understates lifetime — every headline metric moves in a flattering direction, which
  is why it goes unnoticed. Match on customer name and identifier across entities before aggregating.
- **A customer's cohort is when they joined the *group*, not when they first bought from a second
  entity.** Cross-selling an existing customer to another entity is expansion, not acquisition, and
  treating it as acquisition both inflates the new cohort and depresses its apparent CAC.
- **CAC is a group question where marketing is centralised.** If one entity carries the marketing
  spend and others acquire the customers, per-entity CAC is meaningless. Compute it at the level the
  spend and the acquisition actually share.
- **Compare retention curves across entities.** Different curves for the same product usually mean
  different service quality or different customer mixes — a genuine operational finding.
- **Capability is checked per entity**: the customer-sales tool may be enabled for one company file
  and not its sibling, so one entity's triangle can be evidenced and another's not. The coverage sheet
  shows this per file.
