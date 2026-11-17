<!-- esg-sustainability-reporting · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Define reporting scope and boundaries
- Step 2 — Define the metric catalog
- Step 3 — Build the data pipeline and controls
- Step 4 — Reporting and narrative
- Step 4b — Output (Mosofin addition)
- Step 5 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** In this skill the physical and social measurements are
legitimately `[manual]`, and a catalog that names their owners and sources is the deliverable.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

Pull the `[auto]` / `[gated]` reads before designing anything, because the activity data you actually have
determines which metrics are realistically reportable this year.

**Batch independent reads into one message** — spend by category, the vendor list, travel accounts and
headcount do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_company_info`* — legal name, currency, country, industry — usually **[auto]**
- *`search_accounts`* — **the expense categories**, which are the raw material of the spend-based
  estimate — usually **[auto]**
- *`get_profit_and_loss`* by period **and by class / department / location** — **spend by category, and
  where possible by site** — usually **[auto]**
- *`search_vendors`* + *`get_vendor`* — **the supplier list** — usually **[auto]**
- *`search_bills`* / *`search_expenses`* / *`search_purchases`* — **spend by supplier and category**, which
  is the Scope 3 dataset — usually **[auto]**
- *`get_general_ledger`* on the utility, fuel, travel and freight accounts — usually **[auto]**
- *`search_employees`* — **headcount**, the intensity denominator — usually **[auto]**
- *`search_locations`* / *`search_classes`* / *`search_departments`* — **site or segment structure** —
  usually **[auto]**
- *`search_fixed_assets`* or the asset accounts — vehicles and plant, which indicate Scope 1 sources —
  usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data. **An ESG disclosure is a public statement**, often
a regulated one; a fixture-derived figure inside one is a serious matter. Say so plainly rather than
footnoting it.

## Step 1 — Define reporting scope and boundaries

- **Organizational boundary** — **equity share vs. control approach.** Under **equity share** you count
  emissions in proportion to your ownership; under **control** you count 100% of what you control and
  nothing of what you do not. **The two give materially different totals for the same group**, which is
  why the choice is disclosed and held constant.

  **[gated]**: Gate 1 gives the **connected entity list**, and the financial statements give **ownership
  percentages and consolidation treatment** (*`get_balance_sheet`*, investment accounts). That is a real
  starting point — **the equity-share approach and the financial consolidation percentages are the same
  underlying numbers.** What the workspace cannot tell you is which *sites* are operated, leased or
  franchised, and that is where control-approach boundaries usually turn.

- **Operational boundary** — **Scope 1 / 2 / 3 categories.** Scope 1 is what you burn directly; Scope 2 is
  the electricity you buy; Scope 3 is everything else in your value chain, up and down. **[manual]** to
  decide, **[auto]** to inform: **the expense category list is a good prompt for which Scope 3 categories
  are actually relevant** to this business.

- **Time period and frequency.** **[auto]** from the profile — and **align the ESG period to the fiscal
  period** wherever possible. Where they differ, say so; a reader will assume they match.

**Record the boundary decision explicitly, with its date.** Boundary changes are the most common cause of
year-on-year figures that are not comparable, and they must be disclosed and restated.

## Step 2 — Define the metric catalog

Typical categories:

- **Environmental**: energy, emissions, water, waste
- **Social**: headcount, DEI, safety
- **Governance**: policies, incidents, compliance

For each metric define:

- **Definition and units** — **[manual]**. **Units are where this goes wrong**: state kWh, tCO₂e, m³,
  tonnes, FTE explicitly, and never let a currency amount stand in for a physical unit.
- **Owner and source system** — **[manual]**, and the most valuable column in the catalog. Every metric
  gets a named human and a named system. "The workspace" is a valid answer for the spend-based ones; for
  the rest it is not.
- **Calculation steps** — **[manual]**, including the **emission factor with its source, version and
  year**.
- **Data quality controls** — **[manual]** to design; see Step 3.

**Add a Mosofin column: the capability verdict and the data-quality tier.** Per metric:

| Metric | Typical verdict | Notes |
|---|---|---|
| **Scope 3 purchased goods & services (spend-based)** | **[auto]** activity data | Spend by category from the ledger × a spend factor. **Complete and reconciled — but the lowest-quality tier.** |
| **Scope 3 business travel** | **[auto]** activity data | Travel and mileage spend. Distance-based is better where a travel system exists. |
| **Supplier list and spend ranking** | **[auto]** | The engagement target list. Genuinely strong here. |
| **Energy consumption (kWh)** | **[manual]** | **Spend ≠ consumption.** Meter reads or supplier statements only. |
| **Scope 1 fuel and vehicles** | **[gated]** | Ledger shows fuel *spend* and vehicle assets; litres are `[manual]`. |
| **Scope 2 electricity** | **[manual]** | Needs kWh and a grid factor. Neither is here. |
| **Water, waste** | **[manual]** | Volumes and tonnages; spend is a poor proxy and should not be used. |
| **Headcount / FTE** | **[auto]** | The intensity denominator. |
| **Revenue and emissions intensity denominators** | **[auto]** | Revenue per `get_profit_and_loss`. |
| **DEI, safety, governance** | **[manual]** entirely | Not accounting data in any form. |

**Where a metric is `[manual]`, the catalog entry is still written in full** — definition, units, owner,
calculation, controls. **A catalog of metrics the entity cannot yet produce is the point of the exercise,
not a failure of it.**

## Step 3 — Build the data pipeline and controls

- **Source extraction** — **[auto]** for the ledger-derived metrics: the tool calls in Step 0 *are* the
  extraction, and they are repeatable, which is exactly what an assurance provider wants. `[manual]`
  everywhere else; document how each source is obtained and by whom.
- **Transformation and calculations** — **[manual]** to design. **Record the factor applied, its version,
  and the arithmetic**, so a third party can reproduce the number.
- **Review controls and approvals** — **[manual]**. Who checks the figure before it is published, against
  what, and with what evidence of having done so.
- **Change management and version control** — **[manual]**. **Factors are revised annually and boundaries
  move.** Version the catalog, and record which factor version produced which published figure.
- **Evidence retention for assurance** — **[manual]** to operate, **[auto]** to support: ledger-derived
  activity data is **already retained, already reconciled, and already reconcilable to audited financial
  statements.** That is the strongest evidence position of any metric in the catalog, and it is worth
  saying so — a spend-based Scope 3 figure that ties to the audited P&L has a provenance story that a
  spreadsheet of meter readings does not.

**Mosofin control addition — the reconciliation test.** Every spend-based activity figure should
**reconcile to the financial statements**: total categorised spend used in the ESG calculation, compared to
total operating expenditure per the P&L, with the difference explained. **[auto]**, and it is the check that
turns a plausible number into an assurable one. Spend excluded from the ESG scope should be excluded
*deliberately*, not by accident.

## Step 4 — Reporting and narrative

- **Produce tables and trend charts.** **[gated]** — the financial series is `[auto]`; the physical series
  depends on `[manual]` data.
- **Explain methodology and limitations.** **[manual]**, and this is where the Mosofin work must land
  honestly. **State for every figure whether it is measured, calculated from physical data, or estimated
  from spend** — and never let a spend-based estimate appear in a table beside a metered figure without
  that label.
- **Align with the chosen framework where applicable.** **[manual]** — the framework is the user's choice.

**On year-on-year movements in spend-derived figures**: **a change in spend is not a change in impact.**
Prices move, and so do volumes. Where a spend-based metric moves, say what portion could be price. If you
cannot separate them, say that too. **Publishing a price-driven fall as an environmental improvement is
greenwashing, whether or not anyone intended it.**

## Step 4b — Output (Mosofin addition)

The original lists deliverables but does not specify a workpaper. Produce one, so the design and the
evidence travel together.

Deliver an `.xlsx` workpaper:

**Sheet 1: Scope and Boundary** — the organizational boundary with each entity by `display_name`, the
consolidation approach, the operational boundary by Scope, the period. Plus the header block: workspace
name; each excluded company file and why; whether any figure rests on `mock` data.

**Sheet 2: Metric Catalog / Data Dictionary** — definition, units, owner, source system, calculation,
factor and version, controls, **capability verdict and data-quality tier**.

**Sheet 3: Activity Data — Ledger-Derived** — spend by category and by supplier, with the accounts used
and the period, ready to have factors applied.

**Sheet 4: Supplier Ranking** — suppliers by spend, descending, for Scope 3 engagement targeting.

**Sheet 5: Data Collection Templates** — one per `[manual]` metric, naming the owner and the source.

**Sheet 6: Control Design Checklist** — assurance-ready, including the reconciliation test.

**Sheet 7: Reporting Calendar and Owners** — what is due, when, from whom.

**Sheet 8: Reconciliation to Financial Statements — Mosofin-specific** — categorised spend used, versus
total operating expenditure, with differences explained.

**Sheet 9: Coverage** — Mosofin-specific

| Metric / task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | Data-quality tier | As-at date | Policy | `mock` | Gap |

Most environmental rows read `manual`. **That is the honest and useful result** — it is the collection plan.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`ESG_Reporting_[YYYY]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`, or the group name for a consolidated boundary.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every physical quantity, every factor, every social metric — **name the source required**
instead of estimating.

## Step 5 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The metric catalog** — definitions, units, owners, source systems. The core asset, and it does not
  change year to year
- **The boundary decision**: organizational (equity share vs. control) and operational (which Scope 3
  categories are in), with the entities included
- **The category mapping**: which ledger accounts feed which activity-data line — **the join that makes
  every subsequent year a single run**
- **The emission factor *source and version policy*** — which database, which vintage, who updates it.
  **Not the factors themselves**
- **The framework** and the disclosure calendar
- **The control design** and the assurance level intended
- The replay recipe: the exact sequence of reads that produced the spend-based activity dataset

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist published metric values, emission totals, or supplier-level environmental data.** Supplier
emissions data is frequently shared in confidence, and a published ESG figure is a point-in-time statement
that must be recomputed, not recalled.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Manufacturing — control approach, Scope 1+2+3 cats 1/6, utilities to accounts 6200–6240, DEFRA factors
updated each June" — not "control approach". **The boundary is entity-specific by definition**, and an
unlabelled boundary applied to the wrong company file produces a disclosure covering the wrong
organization. Record the chosen **scenario** (single vs multi, and whether the ESG boundary matches the
financial one) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and the activity data, the factors and every metric value are state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere. **In ESG this matters
more than usual: an entity dropping out of the boundary changes the total, and that change must be
disclosed and the prior year restated, not absorbed silently.**

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One boundary, one activity dataset.

**Multi-entity.** Steps 0–4b run **once per entity**, each call targeting exactly one `data_source_id`,
every activity figure carrying its entity's `display_name`. Then:

- **Choose the consolidation approach and apply it consistently.** **Equity share** — count each entity's
  emissions in proportion to ownership, which lines up directly with the ownership percentages behind the
  financial consolidation. **Control** — count 100% of controlled entities and 0% of the rest, which lines
  up with which entities are consolidated at all. **State which, and never mix them.**
- **The ESG boundary and the financial boundary often differ, and the difference must be deliberate.**
  A joint venture equity-accounted in the financials may be fully in scope for ESG if operationally
  controlled; a dormant consolidated entity may be immaterial and excluded. **List every difference
  explicitly** — an unexplained difference between the two boundaries is exactly what an assurance provider
  will ask about first.
- **Do not eliminate intercompany spend from Scope 3 without thinking.** For a **group-level** disclosure,
  intercompany purchases are internal and would **double-count** — one entity's purchase is another's
  production. For an **entity-level** disclosure they are genuine upstream purchases. The right answer
  depends on the reporting unit, and the intercompany figures are readable (see
  `consolidation-and-eliminations`).
- **Factors are jurisdiction-specific.** Grid electricity factors differ enormously by country, so a group
  with entities in several countries needs several factor sets, keyed by entity. Never apply one country's
  grid factor across a group.
- **Currency matters for spend-based factors.** A spend factor is expressed per unit of a particular
  currency in a particular year. Converting spend and applying a foreign factor introduces an error nobody
  will see. Record the currency alongside every spend-based input.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each metric's verdict per company
file.
