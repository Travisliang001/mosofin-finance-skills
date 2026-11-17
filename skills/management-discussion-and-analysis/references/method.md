<!-- management-discussion-and-analysis · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Establish the structure
- Step 2 — Draft the overview
- Step 3 — Draft results of operations
- Step 4 — Draft non-GAAP measures (if used)
- Step 5 — Draft liquidity and capital resources
- Step 6 — Draft critical accounting estimates
- Step 7 — Draft known trends and uncertainties
- Step 8 — Consistency and grounding checks
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The drivers and the forward-looking sections are
legitimately `[manual]`, and drafting them requires management's input rather than invention.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the statements, the line detail, the balances and the cash
flows do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* **current and comparative**, and **by month** — usually **[auto]**
- *`get_balance_sheet`* **at both period ends** — usually **[auto]**
- *`get_cash_flow_statement`* — **the liquidity section's spine** — usually **[auto]**
- *`search_invoices`* **with line detail** for both periods — **the price / volume / mix decomposition** —
  usually **[auto]**
- *`search_customers`* — **new versus existing customers** — usually **[auto]**
- *`get_general_ledger`* on **debt, reserves and allowance accounts** — usually **[auto]**
- *`get_aged_receivables`* / *`get_aged_payables`* — working capital movement — usually **[auto]**
- *`search_employees`* — headcount, an operating expense driver — usually **[auto]**
- *`search_accounts`* — **the chart, for scoping critical estimates** — usually **[auto]**
- *`get_company_info`* — **legal name**, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap. **If line detail is
  unavailable, say the revenue decomposition cannot be computed.**
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **MD&A is a published document, and for filers a
legal one.** A fixture-derived figure in it is not a footnote-level issue. **Stop.**

## Step 1 — Establish the structure

**A standard MD&A** — SEC **Reg S-K Item 303** framework for US filers; similar narrative for others —
**[manual]** to select, per the filing type:

1. **Overview / Executive summary** — the business, the period at a glance, key developments
2. **Results of operations** — line-by-line analysis of the income statement, period over period
3. **Non-GAAP measures** (if used) — definitions and reconciliations
4. **Liquidity and capital resources** — cash flows, sources and uses, debt, commitments
5. **Critical accounting estimates** — the judgments that most affect the financials
6. **Known trends, demands, commitments, events, and uncertainties** — forward-looking factors
7. **Off-balance-sheet arrangements** (if any)
8. **Quantitative and qualitative market risk disclosures** — **Item 7A** for SEC filers

**[auto]** scoping contribution: **sections 7 and 8 can be checked for applicability.** Off-balance-sheet
arrangements and market risk exposures leave balance-sheet traces — guarantees, derivatives, foreign
currency balances, floating-rate debt. **Their absence is worth confirming rather than assuming**, and
their presence means the section is required.

## Step 2 — Draft the overview

A concise summary covering — **[gated]**:

- **What the business does** (brief) — **[manual]**
- **Headline results** — revenue, profit, key metric movements — **[auto]**
- **Significant events in the period** — acquisitions, financings, product launches, restructurings —
  **[gated]**: **financings and acquisitions leave clear ledger traces**; product launches do not
- **The lens management uses to evaluate performance** — **[manual]**

**Keep it factual and grounded. Avoid promotional language.**

**[auto]** prompt for significant events: **large or unusual movements in debt, equity, goodwill or
intangibles during the period** point to financings and acquisitions. **Surface them so nothing material is
omitted from the overview** — an unmentioned refinancing is a conspicuous gap.

## Step 3 — Draft results of operations

**For each major income statement line, explain the period-over-period change with drivers, not just
restatement of the numbers.**

**Bad (just restates)**: *"Revenue increased $2M, from $10M to $12M, an increase of 20%."*

**Good (explains drivers)**: *"Revenue increased $2.0 million, or 20%, to $12.0 million. The increase was
driven primarily by [volume growth in X product line of $1.5M from N new customers] and [price increases of
$0.7M], partially offset by [unfavorable foreign currency translation of $0.2M]."*

**Decompose changes into drivers where possible** — each with its verdict:

- **Price vs. volume vs. mix** for revenue — **[gated]**, **and computable from invoice line detail.**
  **The one driver the workspace can genuinely supply**, and the most important one. Where lines carry
  quantity and unit price, build the bridge: volume effect at prior prices, price effect on prior volumes,
  mix effect from the change in what was sold
- **Input cost vs. efficiency vs. volume** for COGS — **[gated]**: **volume is `[auto]` from the same line
  detail; input cost movement is `[auto]` where purchase prices are readable; efficiency is the residual**
  and needs explanation
- **Headcount, compensation, discretionary spend** for operating expenses — **[gated]**: **headcount is
  `[auto]`**, the split between compensation and discretionary is `[auto]` by account, **why discretionary
  spend moved is not**
- **Rate vs. balance** for interest — **[gated]**: **balances are `[auto]`; the effective rate is
  derivable**, and the decomposition follows
- **One-time vs. recurring** items — **[gated]**: see a quality-of-earnings review, which runs the
  same test the other way. **A "one-time" item that appeared in each of the last three years is readable**,
  and calling it one-time in an MD&A is exactly the characterisation regulators challenge

**Cover each line**: **revenue, COGS / gross profit, each operating expense category, operating income,
other income / expense, tax, net income. Discuss margins (gross margin %, operating margin %) and their
changes.** **[auto]** throughout for the figures.

**Mosofin discipline on attribution:** **write the movement from the data and the driver from management.**
Where a driver is supplied without support, **it goes in the draft and into the Sheet 2 log as
management-asserted** — not because it is doubted, but because the document's grounding claim should
distinguish computed figures from stated explanations.

## Step 4 — Draft non-GAAP measures (if used)

If the entity uses non-GAAP measures — adjusted EBITDA, free cash flow, ARR — **[gated]**:

- **Define each measure clearly** — **[manual]**
- **Explain why management uses it** — decision-usefulness — **[manual]**
- **Reconcile to the nearest GAAP measure** — **[auto]** on the GAAP side; **the adjustments are the
  entity's**
- **Present GAAP measures with equal or greater prominence** — an **SEC requirement**
- **Don't exclude normal, recurring cash operating expenses to inflate the measure** — **an SEC scrutiny
  area**

**[auto]** check on that last point, and it is worth running: **each adjustment tested for recurrence across
prior periods.** **An add-back that appears every year is not non-recurring**, and its exclusion is exactly
what draws scrutiny. **Report the recurrence count per adjustment**, where the same test appears.

**And note the specific case**: **share-based compensation** is commonly excluded from adjusted EBITDA. It
is a real, recurring cost. **Whether that exclusion is acceptable is the entity's judgment; flagging that it
is recurring is ours.**

## Step 5 — Draft liquidity and capital resources

Cover — **[gated]**, and the split is uneven:

- **Cash position and changes** — **[auto]**
- **Cash flow analysis**: operating, investing, financing — **explain the drivers of each** (links to
  `cash-flow-statement-indirect-method`) — **[gated]**: the figures `[auto]`, the drivers as above
- **Sources of liquidity**: **cash on hand** — **[auto]** — **credit facilities, drawn and undrawn** —
  **[manual]**: **undrawn capacity is not in the ledger** — **expected operating cash** — **[manual]**
- **Uses of liquidity**: **capex plans, debt service, dividends, working capital needs** — **[gated]**:
  **historical capex, debt service and dividends are `[auto]`; plans are `[manual]`**
- **Debt profile**: **maturities, interest rates, covenants** — compliance status per
  `debt-and-covenant-tracking` — **[gated]**: **balances `[auto]`, the agreement `[manual]`**
- **Capital commitments**: **purchase obligations, lease commitments** — **[gated]**: **lease commitments
  are `[auto]` where recognised** (see `lease-accounting-asc842-ifrs16`); purchase obligations are
  contractual
- **Ability to meet obligations**: **forward-looking liquidity assessment** — **[manual]**, and **legal
  review territory**

**This section often draws the most investor and regulator attention. Be specific and forward-looking where
management has a basis.**

**Two Mosofin cautions for this section specifically:**

**Cash on hand is not available liquidity.** **Restricted cash, cash held in subsidiaries that cannot
distribute it, and cash committed to near-term obligations** are all excluded in substance and included on
the balance sheet. **In a group, report cash by entity where it matters** — see the cross-entity step.

**And the forward-looking assessment is management's.** *"The Company believes its existing cash and
facilities are sufficient to meet its obligations for at least twelve months"* is a statement with legal
weight and a specific evidentiary basis. **Draft it only from what management states, and log it.**

## Step 6 — Draft critical accounting estimates

**Identify the estimates that:**

- **Require the most subjective or complex judgment, AND**
- **Could materially change if different assumptions were used**

**Common critical estimates** — with the Mosofin verdict on scoping each:

- **Revenue recognition judgments** — variable consideration, SSP — **[gated]**
- **Allowance for credit losses** — **[auto]** to scope; the balance and its movement are readable
- **Inventory valuation** — **[auto]** to scope
- **Goodwill and intangible impairment** — **[auto]** to scope; see the goodwill impairment test
- **Income tax** — valuation allowances, uncertain positions — **[auto]** to scope; see
  the deferred tax roll-forward
- **Business combination fair values** — **[gated]**
- **Stock-based compensation assumptions** — **[gated]**; see the equity compensation accounting
- **Loss contingencies** — **[manual]**; see `contingencies-and-litigation-asc450`

**For each: describe the estimate, the judgment involved, and the sensitivity** — how the financials would
change under different reasonable assumptions. **This is distinct from the accounting policy note, which
describes the method — MD&A describes the judgment and uncertainty.**

**Mosofin contribution — scope, then size.** **[auto]**: **read the balance sheet to see which of these
estimates actually exist here and how large each is.** An entity with no goodwill has no goodwill impairment
estimate; one whose allowance for credit losses is 0.2% of receivables has a less critical estimate than one
at 12%. **Scoping and sizing are readable; sensitivity is not** — and **sensitivity is the part MD&A is
actually asking for.**

## Step 7 — Draft known trends and uncertainties

**The forward-looking heart of MD&A. Discuss trends, events, and uncertainties that are reasonably likely to
materially affect future results** — **[manual]** throughout, with `[auto]` evidence where it exists:

- **Market / demand trends** — **[manual]**
- **Input cost trends** — **[gated]**: **historical input cost movement is readable**; the trend forward is
  not
- **Competitive dynamics** — **[manual]**
- **Regulatory changes** — **[manual]**
- **Customer concentration developments** — **[auto]**: **revenue concentration by customer, and its
  movement, is directly measurable** — one of the few genuinely evidenced items in this section
- **Foreign currency exposure** — **[gated]**: **balances by currency are readable**
- **Interest rate exposure** — **[gated]**: **floating-rate debt balances are readable**
- **Seasonality** — **[auto]**: **measurable from the monthly history**, and better measured than asserted

**Forward-looking statement safe harbor**: **for public filers, forward-looking statements should be
accompanied by cautionary language. Flag all forward-looking statements; recommend the entity's standard
safe-harbor language and legal review.**

**The Mosofin rule for this section is absolute: every forward-looking statement in the draft must trace to
something management said.** **Historical trends may be measured and stated as history. The extrapolation is
management's.** *"Input costs rose 8% over the year"* is `[auto]`. *"Input costs are expected to continue
rising"* is not, and must come from management or not appear.

## Step 8 — Consistency and grounding checks

- **Every number in the MD&A ties to the financial statements or supporting schedules** — **[auto]**, and
  **this is the check the workspace performs natively**
- **Percentages and dollar changes are arithmetically correct** — **[auto]**
- **The narrative is consistent with the notes and the primary statements** — **[gated]**
- **No promotional or misleading characterizations** — **[manual]** judgment
- **Forward-looking statements flagged** — **[gated]**; every one logged
- **Tone is balanced** — discusses both favorable and unfavorable developments — **[manual]**
- **Non-GAAP measures reconciled and not over-emphasized** — **[gated]**

**Mosofin additions to the check set:**

- **The comparative agrees to what was filed** — **[gated]**, and important. **The ledger's prior year may
  differ from the published prior year** if audit adjustments were never posted. **An MD&A citing a
  comparative that does not match the filed statements is a visible inconsistency**
- **Every driver is classified** — computed, or management-asserted
- **Every "one-time" characterisation was tested for recurrence**

## Step 9 — Output

Deliver the MD&A as a structured document plus a grounding workpaper:

**Document: MD&A Draft** — **formatted narrative in standard order**, **marked DRAFT FOR MANAGEMENT
REVIEW**, with **forward-looking statements visibly marked** in the draft itself so a reviewer can see them
in context.

**Workpaper (`.xlsx`):**

**Sheet 1: Variance Analysis Backing** — **every period-over-period change with the dollar and percent and
the driver attribution.** Add a **Driver Basis** column: computed, or management-asserted.

**Sheet 2: Number Tie-Out** — **each figure cited in the MD&A traced to its source.** **In a Mosofin run
this means the tool, the parameters, the entity `display_name` and the as-at date** — which makes the
tie-out reproducible rather than merely asserted.

**Sheet 3: Non-GAAP Reconciliations** — if applicable, **with the recurrence count for each adjustment**.

**Sheet 4: Forward-Looking Statements Log** — **each forward-looking statement flagged for safe-harbor and
legal review.** Add **the source**: which management statement it came from. **A forward-looking statement
with no source does not go in the draft.**

**Sheet 5: Critical Estimates Summary** — **each estimate with judgment and sensitivity**, plus **the
balance and its materiality** from the scoping read.

**Sheet 6: Revenue Bridge — NEW, Mosofin-specific** — price, volume and mix decomposition, with the line
population used and the method stated.

**Sheet 7: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming:** `MDA_[YYYY]_[EntityName]`

`[EntityName]` is the legal name from the profile, or the group name.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where a driver could not be
evidenced, **it is attributed to management** rather than presented as analysis.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The structure** used for this filing type, and which sections apply
- **The non-GAAP measure definitions** and their reconciliation basis — **not the values**
- **The critical estimate list** for this entity, and why each is critical
- **The tie-out recipe** — which reads produce which figures. **The asset that makes the grounding workpaper
  reproducible**
- **The revenue bridge method** — which line fields, which population, how mix is defined
- **The driver taxonomy** the entity uses — its own language for price, volume, mix, FX and one-offs
- **The KPI and non-GAAP definitions**, cross-referenced to `kpi-dashboard-builder`
- **The review and sign-off path**, including who performs legal review
- **The safe-harbour language reference** — by reference, not by content
- The replay recipe: the exact sequence of reads that produced the statements and the bridge

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist financial figures, narrative text, drafts, drivers or forward-looking statements.** All
state — **and a stored narrative reused next period is boilerplate, which is the one thing this skill exists
to avoid.** **Persist the structure and the method; redraft every word.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Group — 10-K MD&A, adjusted EBITDA excludes SBC and restructuring, critical estimates: credit losses,
goodwill, tax valuation allowance; revenue bridge from invoice lines by product class" — not "10-K MD&A,
adjusted EBITDA excludes SBC". **Estimate lists and bridge methods are entity-specific**, and applying one
entity's critical estimates to another describes judgments that do not exist there. Record the chosen
**scenario** (single vs multi, consolidated) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One set of figures, one narrative.

**Multi-entity.** **An MD&A almost always describes the consolidated group**, so:

- **Ground the narrative in consolidated figures**, not the parent's and not a sum of entities.
  **Intercompany revenue must be eliminated first** — see `consolidation-and-eliminations` — or the revenue
  discussed is overstated and every margin built on it is wrong.
- **A disconnected group member means the underlying figures are incomplete.** Say so before drafting; this
  is a published document.
- **Segment discussion, where required, follows the reporting segments** — which may or may not map to legal
  entities. **Ask; do not assume the connected file list is the segment structure.**
- **Cash by entity matters in the liquidity section.** **Group cash that sits in a subsidiary which cannot
  distribute it is not available to meet the parent's obligations**, and MD&A readers care about exactly
  that distinction. **Report it where material.**
- **Currency effects need separating**, and constant-currency analysis is a standard MD&A device — see
  `foreign-currency-translation-asc830`. **A group whose revenue rose 6% in reported terms and fell 2% at
  constant rates has one honest sentence available**, and it is the second one.
- **Covenants may sit at group or entity level**, and the liquidity section should say which — see
  `debt-and-covenant-tracking`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
