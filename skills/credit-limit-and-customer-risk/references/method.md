<!-- credit-limit-and-customer-risk · method.md · read for: Stages 3–6 — the credit assessment itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Gather customer information
- Step 2 — Quantitative analysis (if financials available)
- Step 2b — Your own payment experience (Mosofin addition to the quantitative analysis)
- Step 3 — Qualitative analysis
- Step 4 — Build a credit score (or use one)
- Step 5 — Recommend a credit limit
- Step 6 — Set terms and conditions
- Step 7 — Ongoing monitoring
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence — and in a credit decision the gaps are exactly where a bureau report or a set of accounts must
be obtained.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the customer record,
the invoice history, the payment history and the aging do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_customers`* / *`get_customer`* — the customer record: name, address, terms, active status —
  usually **[auto]**
- *`get_customer_balance`* — **current exposure** — usually **[auto]**
- *`get_aged_receivables`* — **how much of that exposure is overdue, and by how long** — usually **[auto]**
- *`search_invoices`* over the full history — **every invoice, its date and its due date** — usually
  **[auto]**
- *`search_payments`* over the full history — **every payment and its date**, giving **days-to-pay** —
  usually **[auto]**
- *`get_customer_sales`* with a monthly breakdown — **trading volume and its trajectory** — usually
  **[auto]**
- *`search_credit_memos`* / *`search_refund_receipts`* — **disputes and credits issued** — usually
  **[auto]**
- *`search_vendors`* — **to test whether the customer is also a vendor** — usually **[auto]**
- *`get_general_ledger`* on the bad-debt and allowance accounts — **prior write-off history** — usually
  **[auto]**
- *`search_terms`* / *`get_term`* — the terms currently granted — usually **[auto]**
- *`get_company_info`* — your entity's currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it must never support a credit decision, a
limit, or an adverse assessment of a real, named business.

## Step 1 — Gather customer information

For each customer being evaluated, collect — **[manual]** unless noted:

- **Legal entity details** (registration, age, jurisdiction) — trading name and address **[auto]**;
  registration and legal entity **[manual]**
- **Industry and business model**
- **Ownership structure**
- **Public vs. private**; listed exchange and ticker if listed
- **Recent financial statements** (typically last 2–3 years)
- **Banking references**
- **Trade references**
- **Credit bureau report** (if commissioned)

**Flag missing essentials. A small SMB customer may not have audited financials — adjust expectations.**

**[auto]** and worth adding as a distinct block: **your own relationship record** — first invoice date
(how long you have traded), total lifetime revenue, current exposure, and whether the account is active.
"We have traded with them for six years" is a fact, and it belongs alongside the bureau report rather
than beneath it.

## Step 2 — Quantitative analysis (if financials available)

**Compute key ratios from the customer's financials** — **[manual]** throughout. These are *their*
numbers, not yours.

**Liquidity**
- **Current ratio** = Current Assets / Current Liabilities (target typically > 1.0; varies by industry)
- **Quick ratio** = (Cash + AR + Marketable Securities) / Current Liabilities (target typically > 0.8)
- **Cash ratio** = Cash / Current Liabilities

**Leverage**
- **Debt-to-Equity** = Total Liabilities / Total Equity
- **Debt-to-Assets** = Total Liabilities / Total Assets
- **Interest coverage** = EBIT / Interest Expense

**Profitability**
- **Gross margin, operating margin, net margin**
- **Return on assets, return on equity**
- **Trend over the last 3 years** (improving / declining) — the trend usually matters more than the level

**Cash flow**
- **Operating cash flow positive and growing?**
- **Free cash flow positive?**
- **Working capital adequate for the business cycle?**

**Size**
- **Total revenue, total assets, employee count**
- **Larger entities generally lower risk for the same balance amount**

**Compare to industry benchmarks if available (the user must provide; do not assume).**

**If no financials are available, say so and rely on Step 2b.** Do not leave this section blank as though
the analysis were merely incomplete — an unanalysed customer is a different decision from an analysed
one.

## Step 2b — Your own payment experience (Mosofin addition to the quantitative analysis)

**[auto]** throughout, and this is the section a connected workspace uniquely provides. It is
quantitative evidence of the same kind as Step 2, drawn from your own ledger rather than their accounts:

- **Actual days-to-pay** — mean, median and spread, measured from invoice date and from due date
  (*`search_invoices`* against *`search_payments`*). State the sample size; three invoices is not a
  pattern
- **The trend in days-to-pay** — deterioration is the single earliest warning available, and it precedes
  bureau downgrades
- **Payment behaviour by size** — do they pay small invoices promptly and stretch large ones?
- **Current exposure and its aging** — how much is out, how much is overdue
- **Peak historic exposure** — a limit below what they have already owed you tells you something
- **Trading volume trend** — including any **sudden increase**, which is a Step 7 trigger and often
  precedes a failure
- **Credit notes and disputes** — frequency and value; a customer who disputes routinely is slow to pay
  by design
- **Write-off history** — whether this customer, or a similarly named one, was written off before
- **Whether they are also a vendor** — which changes net exposure (see the edge case)

Present this alongside Step 2, not after it. Where the customer's financials are unavailable — which for
smaller customers is normal — **this is the analysis**.

## Step 3 — Qualitative analysis

- **Management**: experience, reputation, stability — **[manual]**
- **Industry health**: growing, stable, declining — **[manual]**
- **Customer concentration of the customer**: their dependence on a few of their own customers is a risk
  — **[manual]**
- **Recent events**: leadership changes, M&A, litigation, regulatory action — **[manual]**
- **Geographic / political risk**: cross-border trade with sanctioned countries, currency controls —
  **[manual]**; note that **no sanctions screening is available here**
- **Years in operation**: longer history = lower risk usually — **[manual]** for their age; **[auto]** for
  how long they have traded with *you*
- **Payment behavior with other suppliers**: from trade references and the bureau report — **[manual]**,
  and worth contrasting explicitly with their behaviour toward you, which is **[auto]**. A customer who
  pays others well and you poorly is telling you something specific

## Step 4 — Build a credit score (or use one)

**If the user has a scoring model, apply it. Otherwise, use a simple tiered approach** — **[gated]**: the
inputs are mixed, the assignment is judgment:

| Tier | Indicators |
|------|-----------|
| **A — Low risk** | Strong financials, long history, top-tier bureau rating, no negative signals. Extend full requested credit. |
| **B — Standard** | Acceptable financials, decent history, no major flags. Extend with monitoring. |
| **C — Watchlist** | Weak in some metric, short history, or modest concerns. Limited credit + closer monitoring. |
| **D — High risk** | Significant negative signals. Cash-on-delivery only, or pre-payment, or letter of credit, or credit insurance. |
| **F — Decline** | Bankruptcy, sanctions, fraud indicators, or fundamental viability concerns. No credit. |

**The tier comes from a holistic view, not a single ratio.**

**State which evidence supported the tier**, and specifically whether it rests on the customer's
financials, on your own payment experience, or on both. A tier A assigned with no financials and six
years of flawless payment is a defensible judgment; a tier A assigned with neither is not.

## Step 5 — Recommend a credit limit

Common methods (apply per user policy):

**Method 1 — Percentage of the customer's net worth or working capital**
e.g. 5–10% of the customer's working capital for an unsecured trade credit line. **[manual]** — needs
their balance sheet.

**Method 2 — Multiple of expected monthly volume**
e.g. 1.5–2.0× monthly expected trade volume to handle peaks and reasonable payment delays. **[gated]**:
**historic monthly volume is [auto]**, the expected forward volume is the request.

**Method 3 — Credit insurance backed limit**
If credit insurance is in place, **the insurance company sets the insurable limit; the entity may match or
be more conservative.** **[manual]**.

**Method 4 — Tier-based ceiling**
Each tier (A/B/C/D) has a maximum limit per the entity's policy. **[gated]** once the policy is stored.

**State the rationale explicitly. Don't just put a number.**

**[auto]** cross-check worth applying to any method: compare the proposed limit against **peak historic
exposure** and against **current exposure**. A limit below what the customer already owes needs a stated
plan; a limit far above anything they have ever ordered is theoretical.

## Step 6 — Set terms and conditions

Beyond the limit, consider — **[manual]** to decide, **[auto]** to see what is currently in place:

- **Payment terms**: Net 30 / Net 60 / 2/10 Net 30 / on receipt
- **Currency**
- **Collateral or guarantee requirements** (personal guarantee, parent guarantee, security interest)
- **Required documents** (credit application, financials, trade references)
- **Specific stop conditions** (any overdue > 30 days triggers hold)

**[auto]** and worth reporting: whether the terms **actually applied on recent invoices** match the terms
on the customer record. They frequently diverge, and a customer being invoiced on Net 60 while the record
says Net 30 is extending credit nobody approved.

## Step 7 — Ongoing monitoring

For existing customers, set up monitoring:

- **Periodic limit review** — annually for stable customers, quarterly for watchlist, more often for high
  risk. **[gated]**: the due date is trackable from the stored review cadence

**Triggers for ad-hoc review** — and **four of these six are `[auto]`**, which turns monitoring from an
intention into a running query:

- **First payment delay** — **[auto]**
- **Sudden increase in ordering pattern** — **[auto]**, and one of the more reliable distress signals: a
  customer in trouble often orders heavily just before failing
- **Public bad news about the customer** — **[manual]**
- **Industry downturn** — **[manual]**
- **Customer's customers in distress** — **[manual]**
- **Failure to provide updated financials** — **[gated]**: trackable against the stored review cadence

Run the `[auto]` triggers across the whole customer base, not only the customer under review. That is
where they earn their value.

## Step 8 — Output

**For a single credit review** → recommendation memo + supporting analysis.
**For a portfolio review** → an `.xlsx` with one row per customer.

**Single review output:**

- **Customer summary**
- **Quantitative analysis** (ratios + trends) — **and the payment-experience block from Step 2b**
- **Qualitative analysis**
- **Trade reference summary**
- **Bureau report summary**
- **Tier assignment** — with the evidence it rests on
- **Recommended limit and rationale**
- **Terms and conditions**
- **Monitoring plan**

**Portfolio output (.xlsx):**

**Sheet 1: Portfolio Summary** — total customers, total exposure, by tier. Add a header block: workspace
name; each in-scope company file by `display_name`; each excluded one and why; whether any figure rests
on `mock` data.

**Sheet 2: Customer Reviews**

| Customer | Industry | Tier | Current Limit | Recommended Limit | Action (Increase / Maintain / Reduce / Hold) | Rationale | Next Review Date |

Add **Days-to-pay (mean / trend)** and **Peak exposure** — the two `[auto]` columns most likely to change
a decision.

**Sheet 3: Watchlist** — customers in tier C or worse, or with recent triggers. **Include every customer
flagged by an automated trigger**, whether or not they were part of the requested review.

**Sheet 4: Concentration Analysis** — top N customers by exposure; % of total A/R; comparison to the
entity's risk policy. **[auto]** in full, and in a multi-entity workspace **computed at group level**.

**Sheet 5: Coverage — NEW, Mosofin-specific**

| Input or task | Customer | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | Sample size | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

Every row drawn from the customer's own financials or a bureau report reads `manual` with its source.
Every row drawn from your trading history reads `auto` with its sample size.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Credit_Review_[CustomerOrPortfolio]_[YYYY-MM-DD].xlsx`

In a multi-entity run, state which entities' exposure the review covers. Every file states which
datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the customer's own financials, any bureau data — **name the source required** instead of
estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The credit policy**: tier definitions, the ceiling per tier, the concentration limit, and the approval
  authority for each level
- **The limit method** the entity uses, and the multiples or percentages within it
- **The review cadence** per tier
- **The monitoring triggers** and their thresholds — what counts as a "sudden increase", how many days
  late counts as a first delay
- **The stop conditions** that trigger an automatic hold
- **The days-to-pay derivation method** — the lookback window and whether it measures from invoice or due
  date. **Not the derived values**
- **Customers with guarantees, insurance or special terms in place**, by customer reference
- The replay recipe: the exact sequence of reads that produced the payment history

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist customer credit assessments, tier assignments, bureau data, the customer's financial
figures, or exposure amounts.** A stored adverse assessment of a named business is a defamatory-risk
document and a commercially sensitive one; bureau data is usually licensed and may not be redistributed;
exposures are stale immediately. **Persist the policy and the method, never the verdict.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — tier ceilings A $250k / B $100k / C $25k; concentration limit 20% of A/R; review annually,
quarterly for C" — not "tier ceilings A $250k…". Entities differ in size and appetite, and an unlabelled
ceiling applied to the wrong company file authorises exposure nobody approved. Record the chosen
**scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and a customer's payment behaviour is state, re-measured every review.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One exposure, one limit.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`,
every figure carrying its entity's `display_name`. Then the aggregation, which is the point:

- **One customer, one credit exposure.** A customer owing three group entities is **one counterparty
  risk**. Each entity may see a comfortable balance while the group's total is large. **Match the
  customer across entities by name and identifier, then sum.** This is the finding a single-entity view
  structurally cannot produce.
- **Set the limit at group level, then allocate it.** Three entities each granting an independent limit
  produces a group exposure nobody authorised. Decide the total, then split it.
- **Payment behaviour may differ by entity** — a customer paying one group company promptly and another
  slowly is usually a dispute or a relationship problem rather than a credit problem. Compare rather than
  averaging.
- **Concentration is a group measure.** A customer at 8% of receivables in each of three entities is at
  8% of the group's too — but a customer at 25% in the largest entity may dominate the group. Compute it
  on the group's total.
- **A write-off at one entity is evidence for all of them.** Check the write-off history across every
  connected entity, not only the one being reviewed.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each input's verdict per company
file.
