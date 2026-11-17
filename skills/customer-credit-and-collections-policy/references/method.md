<!-- customer-credit-and-collections-policy · method.md · read for: Stages 3–6 — drafting the policy and testing it against actual behaviour. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Segment customers
- Step 2 — Define credit policy
- Step 3 — Collections cadence
- Step 4 — Disputes and deductions
- Step 5 — Governance
- Step 6 — KPIs
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the aging, the sales
history, the invoice and payment history and the write-off history do not depend on each other. Never
serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_aged_receivables`* — the current aging, by customer and bucket — usually **[auto]**
- *`search_customers`* / *`get_customer`* — the customer base and the terms held against each — usually
  **[auto]**
- *`get_customer_sales`* with a monthly breakdown — **revenue and concentration by customer** — usually
  **[auto]**
- *`search_invoices`* over the full history — invoice dates, due dates and amounts — usually **[auto]**
- *`search_payments`* over the full history — **when each was actually paid, giving days-to-pay** —
  usually **[auto]**
- *`search_credit_memos`* — **credits issued, the best available proxy for disputes and deductions** —
  usually **[auto]**
- *`get_general_ledger`* on the bad-debt and allowance accounts — **write-off history** — usually
  **[auto]**
- *`get_customer_balance`* — exposure per customer — usually **[auto]**
- *`search_terms`* / *`get_term`* — the terms catalogue actually in use — usually **[auto]**
- *`get_profit_and_loss`* — revenue, for the DSO denominator and bad-debt percentage — usually **[auto]**
- *`get_company_info`* — currency, calendar, industry — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — a policy sized against fixture volumes will fit
no real business, and a segment built on it names real customers on invented behaviour.

## Step 1 — Segment customers

**Segment by value and risk: revenue, margin, payment behavior, disputes, concentration.**

**[auto]** for four of the five, and this is where the skill earns its place:

- **Revenue** — by customer, with trend (*`get_customer_sales`*)
- **Margin** — **[gated]**: revenue is **[auto]**, but cost-to-serve per customer usually is not. A
  company-wide margin applied uniformly tells you nothing about *relative* customer profitability — say
  so rather than presenting a uniform figure as a segmentation dimension
- **Payment behavior** — **[auto]**: actual days-to-pay per customer, its trend and its consistency
  (*`search_invoices`* against *`search_payments`*). **State the sample size per customer**; a segment
  assignment resting on two invoices is a guess
- **Disputes** — **[gated]**: credit memos and refunds are a good proxy (*`search_credit_memos`*), though
  a dispute resolved without a credit leaves no trace
- **Concentration** — **[auto]**: each customer's share of total receivables and total revenue

Produce a segment grid — typically value on one axis and payment risk on the other — and **populate it
with real customers and real counts**. The policy then follows the shape of the base: a long tail of
small slow payers needs automation, a short list of large ones needs relationships, and most books have
both and need two different playbooks.

## Step 2 — Define credit policy

**[manual]** to decide, with the segmentation as the evidence base:

- **Onboarding requirements** — what a new customer must provide before credit is granted, by segment
- **Initial limits and terms** — see `credit-limit-and-customer-risk` for the per-customer method
- **Monitoring triggers** — several of which are `[auto]` to run once defined; see that skill's Step 7
- **Order hold rules** — the point at which supply stops
- **Exception approvals** — who can override, up to what, and how it is recorded

Two `[auto]` inputs worth putting in front of whoever writes this:

- **The terms actually in use across the base**, from the terms catalogue and from what invoices actually
  carried. Entities routinely discover they are operating six sets of terms nobody chose
- **How often the current de facto hold rule bites** — how many customers would be on hold today under a
  proposed rule. A rule that would stop supply to a third of the book will not survive contact with the
  sales team, and it is better to know that now

## Step 3 — Collections cadence

**Define actions by aging bucket (0-15, 16-30, 31-60, 61-90, 90+), including templates and escalation.**

**[manual]** for the actions, templates and escalation. **[auto]** for the sizing, which is what makes the
cadence realistic:

- **How many customers and how much value sit in each bucket today** (*`get_aged_receivables`*)
- **How many accounts each step would touch per week**, which determines whether the cadence needs
  automation or can be done by a person
- **The historic transition rate between buckets** — what share of 31-60 becomes 61-90 — which shows where
  the cadence is actually failing

A cadence designed without those numbers is usually either unenforceable or aimed at the wrong bucket.

## Step 4 — Disputes and deductions

**Reason codes, evidence requirements, SLAs, and accounting impact.** **[manual]** to design; **[gated]**
to inform:

- **Reason codes** — the catalogue is a design decision, but **[auto]** to see what actually happens:
  credit memos by value and frequency (*`search_credit_memos`*) show which dispute types dominate, and
  the code set should cover those first
- **Evidence requirements** — what closes each dispute type
- **SLAs** — the turnaround each type gets
- **Accounting impact** — per `credit-memo-and-refund-handler`: a short-pay is not a write-off, and a
  deduction pending investigation is not a credit

**[auto]** and worth surfacing: **the value of credits issued as a percentage of revenue**, by customer.
A customer generating persistent credits is a process problem upstream — in pricing, shipping or spec —
and collections cannot fix it.

## Step 5 — Governance

**[manual]** throughout:

- **Credit committee** — who sits on it, what it decides, how often it meets. Size it to the book: a
  committee for twelve accounts is theatre
- **Override documentation** — every exception recorded with who approved it and why. Without this the
  policy erodes invisibly
- **Separation of duties** — the person who grants credit is not the person who writes it off, and
  neither is the person who applies the cash. **Mosofin cannot verify any of this**; it is a design and
  an assertion, and the coverage sheet should say so

## Step 6 — KPIs

**DSO, CEI, % current AR, bad debt %, dispute cycle time, promise-to-pay kept rate.**

**Four are `[auto]`, and computing the baseline before the policy exists is the point:**

- **DSO (days sales outstanding)** — **[auto]**: ending A/R ÷ credit sales × days in period. **State the
  denominator**: true credit sales, or a total-revenue proxy. See `ar-aging-and-collections`
- **CEI (collection effectiveness index)** — **[auto]**: how much of what was collectable actually got
  collected in the period, as a percentage. Roughly:
  `(beginning A/R + credit sales − ending total A/R) ÷ (beginning A/R + credit sales − ending current A/R) × 100`.
  **CEI is the better measure of the collections team's performance than DSO**, because DSO moves with
  sales volume and mix while CEI does not — worth explaining to whoever will be measured on it
- **% current A/R** — **[auto]**: the share of the book not yet overdue
- **Bad debt %** — **[auto]**: write-offs as a percentage of revenue, from the bad-debt account

**Two are `[manual]`:**

- **Dispute cycle time** — needs dispute open and close dates, which live in a case system, not the ledger
- **Promise-to-pay kept rate** — needs the promise, which was made in a conversation. **[gated]** at best:
  where a promised date is recorded somewhere, whether it was met is then `[auto]`

**Report the current baseline for all four automated KPIs, with the periods used**, and define the
measurement cadence. A policy launched without a baseline cannot be evaluated, and in practice never is.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The segmentation model** — the axes, the cut-offs, and the rule that assigns a customer to a segment.
  **Not the customer assignments**, which are re-measured
- **The credit policy**: onboarding requirements, initial limits and terms by segment, monitoring
  triggers, order hold rules, exception approval authority
- **The collections cadence** — the action, owner and template for each aging bucket
- **The dispute reason code catalogue**, with evidence requirements and SLAs per code
- **The governance model**: committee composition and cadence, override documentation requirements,
  separation-of-duties design
- **The KPI definitions** — especially **the DSO denominator** and the exact CEI formula used, so the
  measure stays comparable over time
- **The baseline period**, so improvement is measured from a stated starting point
- The replay recipe: the exact sequence of reads that produced the segmentation and the KPI baseline

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist customer names with their segment, payment behaviour, dispute history or KPI values.**
A stored record that a named customer is a "slow payer" or sits in a high-risk segment is commercially
sensitive and, if it reached them, damaging. **Persist the model and the definitions; re-measure the
assignments.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — segments by revenue quartile × days-to-pay band; hold at 60 days past due; DSO on true credit
sales" — not "hold at 60 days past due". Entities differ in customer mix and in what their sales teams
will tolerate, and an unlabelled hold rule applied to the wrong company file stops supply to customers
nobody intended. Record the chosen **scenario** (single vs multi, whether one policy governs all) as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every segment assignment and KPI value is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Detailed policy / SOP.** The credit and collections operating model: onboarding, limits, terms,
  monitoring, holds, exceptions, cadence, disputes, governance. **With each step marked `[auto]`,
  `[gated]` or `[manual]` in this workspace**, so the policy describes a process that can actually run.
- **Segmentation and scorecard example.** Populated with the **real customer base**: counts and values per
  segment, with days-to-pay sample sizes shown.
- **Templates for outreach.** By aging bucket and segment. **Marked `REVIEW REQUIRED - NOT SENT`** —
  Mosofin sends nothing; see `ar-aging-and-collections`.
- **Dispute reason code catalog.** Informed by the credits actually issued, so the codes cover what
  happens rather than what might.
- **KPI definitions and cadence.** With **the measured baseline for DSO, CEI, % current A/R and bad debt
  %**, the periods used, and the two manual KPIs named as requiring a system that captures them.

**Coverage sheet — NEW, Mosofin-specific.**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Periods / sample | Policy | `mock` | Gap — what could not be evidenced and who owns it |

Governance and separation of duties read `manual` — **designed, not verified**. That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer the policy as a Word document only where the host can make one; otherwise give it as text in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs it):
`Credit_Collections_Policy_[YYYY-MM-DD]_[EntityName]`, where `[EntityName]` is the company file's
`display_name`. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something, **name the tool that would have covered it** instead of estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One segmentation, one policy, one
baseline.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one `data_source_id`,
every segment and KPI carrying its entity's `display_name`. Then:

- **A customer trading with several entities is one credit relationship.** Segment them once, at group
  level, after matching across entities. Segmenting per entity puts the same customer in three different
  bands and produces three inconsistent treatments — which the customer will notice.
- **KPIs are meaningful per entity and at group level, but not blended carelessly.** DSO especially:
  each entity has its own sales base, so a group DSO needs group credit sales, not an average of the
  entity figures.
- **One policy or several?** Settled at Gate 1. A single group policy is simpler to govern and often
  wrong for an entity with a very different customer mix; separate policies are better fitted and harder
  to enforce consistently. **State which was chosen and why.**
- **Order hold has to be enforceable per entity.** A group hold decision that one entity's order system
  cannot implement is a policy that will be quietly ignored there.
- **Compare the KPI baselines across entities.** A large gap in CEI between entities with similar customer
  mixes is a process finding, and it is usually the most actionable output of a group-level review.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
