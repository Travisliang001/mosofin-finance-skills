<!-- construction-percentage-of-completion · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Confirm over-time recognition criteria
- Step 2 — Identify performance obligations
- Step 3 — Determine the transaction price
- Step 4 — Choose and apply the measure of progress
- Step 5 — Compute cumulative revenue, cost, and gross profit
- Step 6 — Apply changes in estimate (catch-up method)
- Step 7 — Recognize loss contracts (provision for onerous contracts)
- Step 8 — Track WIP (contract assets / liabilities)
- Step 9 — Modifications
- Step 10 — Disclosures
- Step 11 — Output
- Step 12 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not an
absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the job dimensions,
the cost ledger, the invoice history and the customer list do not depend on each other. Never
serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_classes`* / *`search_departments`* / *`search_customers`* — **the job codes**, and whether
  jobs are tagged at all — usually **[auto]**
- *`get_profit_and_loss`* filtered by class / department / customer — **cost and revenue per job** —
  usually **[auto]** where tagging exists
- *`get_general_ledger`* on the cost accounts — **costs incurred to date, by category and by job** —
  usually **[auto]**
- *`search_bills`* / *`search_purchases`* — subcontractor and materials costs by job — usually **[auto]**
- *`search_purchase_orders`* — **committed but not yet incurred costs**, a useful input to the estimate
  at completion — usually **[auto]**
- *`search_time_activities`* — labour hours by job, for a labour-hours input method — usually **[auto]**
- *`search_invoices`* / *`read_invoice`* — **billings to date per contract** — usually **[auto]**
- *`search_estimates`* — quoted contract values, a starting point for the transaction price — usually
  **[auto]**
- *`search_accounts`* — the contract asset, contract liability and loss provision accounts — usually
  **[auto]**
- *`get_customer_balance`* — amounts outstanding per customer — usually **[auto]**
- *`get_company_info`* — currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support recognised revenue on a real
contract or a loss provision.

## Step 1 — Confirm over-time recognition criteria

Revenue is recognized **over time** if **any** of — **[manual]**, all three depend on contract terms:

- **The customer simultaneously receives and consumes benefits as the entity performs** (e.g. ongoing
  services)
- **The entity creates or enhances an asset the customer controls as it is created** (e.g. construction
  on the customer's land)
- **The entity creates an asset with no alternative use AND has an enforceable right to payment for
  performance to date**

**If none apply, revenue is recognized at a point in time** (when control transfers — e.g. delivery).

**For construction, the third criterion — no alternative use plus a right to payment for work performed
plus a reasonable margin — is most often the basis for over-time. Confirm per contract.** It turns on
the contract's termination clause, which is a legal reading, not an accounting one.

## Step 2 — Identify performance obligations

Per ASC 606 / IFRS 15 (see `revenue-recognition-asc606`) — **[manual]**:

- **Identify distinct goods / services in the contract**
- **Many construction contracts have a single combined performance obligation** (integrated
  construction) **but some have multiple** (e.g. construction + maintenance)
- **Account for each performance obligation separately**

The practical test: could the customer benefit from the parts on their own, and are they separately
identifiable within the contract? Integrated construction usually fails that test, which is why one
combined obligation is the norm.

## Step 3 — Determine the transaction price

- **Fixed consideration plus variable consideration** (variations, claims, performance bonuses,
  **liquidated damages** / penalties) — **[gated]**: the contracted base may be visible as an estimate
  (*`search_estimates`*), the variable elements are **[manual]**
- **Variable consideration estimated using expected value or most likely amount, constrained to
  amounts highly probable not to reverse** — **[manual]**. *The constraint* is the discipline that
  stops optimistic claims inflating revenue
- **Significant financing component** if payment timing differs materially from performance —
  **[gated]**: heavily front- or back-loaded billing is visible in the invoice pattern
- **Allocate the transaction price to performance obligations based on relative standalone selling
  prices** — **[manual]**

## Step 4 — Choose and apply the measure of progress

**The measure should faithfully depict progress toward complete satisfaction.**

**Input methods**:

- **Cost-to-cost** (most common in construction): **% complete = costs incurred to date ÷ total
  estimated costs at completion.** Apply the % to the transaction price for cumulative revenue.
  **[gated]** — numerator `[auto]` where jobs are tagged, denominator `[manual]`
- **Other inputs**: labor hours (**[auto]** where time is tracked by job —
  *`search_time_activities`*), time elapsed (where appropriate)

**Output methods**:

- **Surveys of work performed, milestones reached, units produced / delivered, time elapsed**
- **Often more faithful but harder to measure reliably** — and **[manual]** in an accounting-only
  workspace, since surveys and milestones live on the site, not in the ledger

**Cost-to-cost caveats** — all three matter and two are `[manual]`:

- **Exclude inefficient costs (waste, rework due to errors) from the numerator — they don't represent
  progress.** **[manual]**: the ledger records the cost, not that it was rework. Ask the project
  manager; including them **inflates % complete and pulls revenue forward**
- **Exclude uninstalled materials from the numerator until installed** (an ASC 606 specific rule),
  unless the customer obtains control and the entity is essentially providing a procurement service —
  **[gated]**: materials purchases are visible, whether they are installed is not
- **Update estimated total costs continuously; changes drive the recognition through a catch-up** —
  **[manual]**, and the reason Step 6 exists

**[auto]** and worth surfacing: **open purchase orders per job** (*`search_purchase_orders`*) show
**committed but unincurred cost**. That is not the estimate at completion, but it is a hard floor
under it — and an estimate at completion below costs already incurred plus committed is demonstrably
stale.

## Step 5 — Compute cumulative revenue, cost, and gross profit

For each contract, at each measurement date — **[auto]** arithmetic:

```
% complete = costs incurred to date / estimated total costs

Cumulative revenue = transaction price × % complete
Cumulative cost = costs incurred to date
Cumulative gross profit = cumulative revenue − cumulative cost
                       = (transaction price − estimated total cost) × % complete
                       (i.e., total estimated gross profit × % complete)
```

**Period revenue / cost / GP = cumulative current period − cumulative prior period.**

Show the two forms of cumulative gross profit side by side; they must agree, and a difference means the
transaction price and estimated cost inputs are inconsistent with the recorded costs.

## Step 6 — Apply changes in estimate (catch-up method)

When estimated total costs or the transaction price change — **[gated]**:

- **Recompute cumulative revenue and GP at the new % complete using the revised estimates**
- **The difference between the new cumulative and the previously-recognized amount = catch-up
  adjustment in the current period (not retrospective)**
- **Treat as a change in estimate (prospective; not an error)**

**This is the "cumulative catch-up" mechanic — important not to retroactively restate.**

**[auto]** to compute once the revised estimate is supplied, and **[auto]** to detect that a revision
occurred if prior estimates were stored at Step 12. **Show the catch-up separately from the period's
ordinary recognition** — otherwise a large estimate revision looks like a trading result, which is
exactly the wrong conclusion for a reader to draw.

## Step 7 — Recognize loss contracts (provision for onerous contracts)

**If estimated total cost exceeds the transaction price — the contract will lose money:**

- **Recognize the entire expected loss immediately, not over the remaining contract period**
- **The previously-recognized gross profit (if any) is reversed; the remaining-to-be-incurred loss is
  accrued**

```
Provision for loss = (Estimated total cost − Transaction price) − (Cost incurred to date − Revenue recognized to date)
                   (recorded so the contract's net position reflects the full expected loss)
```

**US GAAP and IFRS both require immediate loss recognition for onerous contracts. This is a critical
anti-deferral rule — don't spread the loss over remaining performance.**

**[auto]** to identify every loss contract the moment the estimates are supplied — comparing estimated
total cost against transaction price across the register takes no judgment at all. **Run this test on
every contract every period**; it is the highest-consequence check in the skill, and a frequent
restatement area precisely because nobody wants to be the one to raise it.

## Step 8 — Track WIP (contract assets / liabilities)

For each contract, at each date — **[auto]** once revenue is computed and billings read:

```
Revenue recognized to date
vs.
Billings to date

Revenue recognized > Billings → Contract Asset (Costs and estimated earnings in excess of billings / Unbilled receivable)
Revenue recognized < Billings → Contract Liability (Billings in excess of costs and estimated earnings / Deferred revenue)
```

**Show contract-by-contract; do not net contract assets against liabilities across different contracts
(present separately).** Netting across contracts hides both an unbilled asset the entity should be
collecting and an overbilling it may have to perform against — two different problems, cancelled into
one meaningless number.

## Step 9 — Modifications

Contract modifications (scope / price changes — **variations**) — **[manual]**:

- **Approved modifications affect the transaction price and total estimated costs**
- **Treated as part of the existing contract if the modification doesn't add distinct goods / services,
  or as a separate contract if it does**
- **Catch-up the cumulative recognition for changes to the existing contract**

## Step 10 — Disclosures

For `notes-to-financial-statements`:

- **Policy for revenue recognition over time and measure of progress**
- **Contract balances (assets, liabilities, receivables) and significant changes** — **[auto]** from
  Step 8
- **Remaining performance obligations (backlog) and when expected to be recognized** — **[gated]**:
  transaction price minus revenue recognised is computable, but **only enforceable amounts count**, so
  the enforceability judgment is `[manual]`
- **Significant judgments** — **[manual]**
- **Loss contract provisions** — **[auto]** to identify, **[manual]** to explain

## Step 11 — Output

Deliver an `.xlsx` workpaper.

**Sheet 1: Contract Register** — each contract: customer, scope, price, dates, performance obligation
structure. Add a header block: workspace name; the entity by `display_name`; each excluded company file
and why; **the job-tagging dimension used**; whether any figure rests on `mock` data.

**Sheet 2: Cost & Estimate Tracking** — per contract: **estimated total cost (with revisions and the
date of each)**, costs incurred to date, % complete. **Mark, per contract, whether costs were read from
the ledger or supplied**, and **add committed cost from open purchase orders** as a cross-check on the
estimate.

**Sheet 3: Revenue & Margin Recognition** — cumulative and period revenue, cost, gross profit, **with
catch-up adjustments shown separately**.

**Sheet 4: WIP Schedule** — contract asset (**CIE** / unbilled) and contract liability (**BIE** /
deferred revenue) **per contract, not netted**.

**Sheet 5: Loss Contract Provisions** — identification of loss contracts; full loss recognition.

**Sheet 6: Billings Reconciliation** — billings vs. revenue recognized; cash received.

**Sheet 7: Modifications Log** — variations, claims, approval status, impact on price / cost.

**Sheet 8: Disclosures** — including remaining performance obligation backlog.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Contract | Entity (`display_name`) | Costs incurred (auto / manual) | Estimate at completion (always manual — date, owner) | Billings (auto / manual) | Tool used | Policy | `mock` | Gap |

The **estimate-at-completion column carries its date and owner on every contract**. An estimate more
than one period old is the most likely cause of a wrong answer here, and this column makes staleness
visible.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Construction_POC_[YYYY-MM]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`; one file per entity plus a combined view where a
contract spans entities. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every estimate at completion — **name the person who supplied it** instead of
estimating.

## Step 12 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The job-tagging convention** — which dimension is the job code, and how job codes map to contracts.
  The thing that makes every future run automatic
- **The contract register**: each contract's customer, transaction price, performance obligation
  structure, and over-time criterion relied on
- **The measure of progress** chosen per contract, and why
- **The cost-account set** that constitutes contract cost, and which accounts are excluded
- **The estimate-revision history** — each contract's successive estimates at completion **with dates
  and owners**. Persist the *history*, not as a current value to reuse: it is what makes a stale
  estimate visible and a catch-up explainable
- **Who owns the estimate** for each contract
- **Contracts identified as loss-making**, and when
- The replay recipe: the exact sequence of reads that produced costs and billings by job

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist customer names with contract values, margins, or claim positions.** Contract pricing
and margin are commercially sensitive, and a claim position is potentially privileged. Persist the
*structure, the conventions and the ownership*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Construction — jobs tagged by Class; cost accounts 5000–5400; cost-to-cost on all contracts;
estimates owned by the commercial manager" — not "jobs tagged by Class". Sibling entities in a
construction group frequently tag jobs differently, and an unlabelled convention applied to the wrong
company file reads costs from the wrong dimension entirely. Record the chosen **scenario** (single vs
multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and **an estimate at completion is state**: re-confirm it every period rather than
reusing it.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is
no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One contract register, one WIP
schedule.

**Multi-entity.** Steps 0–11 run **once per entity**, each call targeting exactly one `data_source_id`,
every contract carrying its entity's `display_name`. Then one cross-entity step, and in construction it
is a real issue rather than a formality:

- **One contract delivered through several group entities.** A main contractor subcontracting to a
  group specialist is normal. **Each entity accounts for its own contract** — the main contractor for
  the head contract, the subsidiary for its subcontract — and **the margin the subsidiary charges the
  main contractor is unrealised at group level** until the work is delivered to the external customer.
  Identify these (*`search_customers`*, *`search_vendors`* for group counterparties) and hand the
  elimination to `consolidation-and-eliminations`.
- **Do not double-count the same physical work.** The subsidiary's revenue and the main contractor's
  cost are the same transaction. At group level, only the head contract's revenue exists.
- **Job codes are usually entity-local.** The same site may carry different job codes at each entity;
  map them explicitly before comparing.
- **Loss contracts must be assessed at both levels.** A subcontract can be profitable while the head
  contract loses money, or the reverse. The group provision follows the group's position on the
  external contract.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each contract's verdict per
company file.
