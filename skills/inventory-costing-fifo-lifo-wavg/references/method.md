<!-- inventory-costing-fifo-lifo-wavg · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 0b — Establish the platform's method (Mosofin addition)
- Step 1 — Confirm method eligibility and consistency
- Step 2 — Determine the cost basis
- Step 3 — Apply the costing method
- Step 4 — Build the cost flow
- Step 5 — Lower of cost and NRV (or LCM)
- Step 6 — Period-end entries
- Step 7 — Method-comparison analysis (if useful)
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** NRV inputs and the physical count are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the items, the purchase history, the sales history and the
balances do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_items`* / *`search_products`* — **the item master, quantity on hand, and any average cost
  field** — usually **[auto]** where an items module exists
- *`search_purchases`* / *`search_bills`* **with line detail** — **purchases with date, quantity and unit
  cost: the layer inputs** — usually **[auto]**
- *`search_invoices`* / *`search_sales_receipts`* **with line detail** — **sales with date, quantity and
  price: the consumption side, and the NRV anchor** — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the inventory balance**, opening and closing — usually
  **[auto]**
- *`get_profit_and_loss`* — **COGS as recorded** — usually **[auto]**
- *`get_general_ledger`* on **inventory and COGS** — movements, and whether COGS posts per sale — usually
  **[auto]**
- *`search_accounts`* — inventory, COGS, freight-in and write-down accounts — usually **[auto]**
- *`get_company_info`* — legal name, currency, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap. **If line-level detail is
  unavailable, say that layer reconstruction is not possible.**
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **inventory and COGS are usually the largest
figures on a merchandising entity's statements**, and a fixture-based cost flow misstates both.

## Step 0b — Establish the platform's method (Mosofin addition)

**Run before Step 1.** **[gated]**, and it frames everything after it.

Ask, and corroborate from the data:

1. **Which method does the platform apply?** Usually stated in its documentation or item settings; often
   FIFO or weighted-average, **rarely LIFO.**
2. **Which method does the entity report on?**
3. **If they differ, where is the difference recorded?** A LIFO reserve, a costing adjustment journal, or
   nowhere.

**[auto]** corroboration: **compare the platform's inventory value to the value implied by the entity's
method** once the cost flow is built in Step 4. **The difference is the reserve or the adjustment** — and
**if no such entry exists in the ledger, the reported figures and the ledger disagree**, which is the
finding.

**Also establish periodic versus perpetual `[auto]`**: **does COGS post with each sale, or only at period
end?** Read the COGS account's movement pattern. **This is not a preference question — it is observable**,
and it decides which variant of LIFO and weighted-average applies.

## Step 1 — Confirm method eligibility and consistency

- **LIFO: permitted under US GAAP, prohibited under IFRS. Don't apply LIFO under IFRS** (see
  a GAAP to IFRS conversion) — **[manual]** to confirm the framework, **[auto]** to flag the contradiction
  if LIFO is asserted alongside IFRS
- **Method must be applied consistently period to period; a change is a change in accounting policy with
  retrospective application** — and **tax implications for LIFO under US GAAP**
- **Different methods can apply to different inventory categories if consistent within each category**

**[auto]** consistency check: **compare this period's implied cost flow to the prior period's.** A change in
the relationship between purchase prices and COGS, with no policy change recorded, suggests the method
changed in practice even if not on paper.

## Step 2 — Determine the cost basis

**Inventory cost includes** (per both frameworks) — **[gated]**:

- **Purchase price** — net of trade discounts, rebates — **[auto]** from bill lines
- **Freight-in, duties, taxes not recoverable** — **[gated]**: readable **if separately posted**, but often
  charged to an expense account instead of into inventory
- **Conversion costs for manufactured inventory** — **direct labor + fixed and variable production overhead
  allocated based on normal capacity** — **[manual]**; the allocation is a costing exercise, see
  `cost-accounting-job-order` and `cost-accounting-process-costing`
- **Other costs to bring to present location and condition** — **[manual]**

**Excluded: storage costs not part of production, abnormal waste, selling costs, general admin.**

**Ensure cost components in the inputs reflect this — don't include selling / admin in inventory cost.**

**Mosofin check — freight-in expensed rather than capitalised.** **[auto]**: **freight and duty on purchase
invoices posted to an expense account** rather than into inventory **understates inventory and overstates
current-period cost.** Read the freight accounts against purchase activity; a consistent relationship
suggests it is being expensed as a policy, which may or may not be intended.

**And the reverse**: **selling or admin costs sitting in the inventory account** overstate the asset.

## Step 3 — Apply the costing method

**FIFO (First-in, first-out)** — **[gated]**, reconstructable:
- **Earliest costs flow to COGS; latest costs remain in ending inventory**
- **Build layers chronologically; consume from the oldest layer first**
- **Same result under periodic and perpetual**

**LIFO (Last-in, first-out) — US GAAP only** — **[gated]**, reconstructable, **but rarely what the platform
holds**:
- **Latest costs flow to COGS; earliest costs remain in ending inventory**
- **Build layers chronologically; consume from the newest layer first**
- **Periodic LIFO can differ from perpetual LIFO** — timing of sales relative to purchases
- **Can also use dollar-value LIFO with pools and indices** — more complex; **flag for the entity's chosen
  approach** — **[manual]**, since the index is external

**Weighted-average** — **[gated]**:
- **Periodic (weighted-average cost)**: **single average for the period = total cost available / total units
  available**; applied to all sales and ending inventory
- **Perpetual (moving-average)**: **average recomputed after each purchase**; sales use the average at the
  time of sale
- **These produce different results — match to the entity's system**, which Step 0b established from the
  data

**Specific identification** — **[gated]**:
- **Each item tracked individually** — used for unique or high-value items like vehicles, jewelry, custom
  work
- **COGS = cost of the specific items sold; ending inventory = cost of specific items on hand**
- **[auto]** where serialised items are tracked individually in the platform; **[manual]** otherwise

## Step 4 — Build the cost flow

For the chosen method — **[gated]**, and this is the reconstruction:

- **Lay out opening inventory + all purchases** — with **date, qty, unit cost, layer** — **[auto]** from
  purchase lines
- **Apply sales / issues per the method's flow rule** — **[auto]** from sales lines
- **Compute COGS** — cumulative cost of units sold
- **Compute ending inventory** — remaining units × their costs
- **Validate: opening + purchases − sales (in units and cost) = ending (units) + COGS (cost)** — **[auto]**

**The validation is not optional and it is free.** **Run it in units and in cost separately**, and report
both. A unit reconciliation that fails means transactions are missing from the population; **a cost
reconciliation that fails means the layer logic is wrong.** They are different faults.

**Then the Mosofin comparison**: **the ending inventory you computed against the inventory balance in the
ledger.** Where the methods agree, they should match. **Where they differ, the difference is the LIFO
reserve or the costing adjustment from Step 0b** — and it should be a recorded figure, not a surprise.

## Step 5 — Lower of cost and NRV (or LCM)

**After costing, value inventory at the lower of cost and net realizable value:**

**IFRS (IAS 2): lower of cost and NRV.** **NRV = estimated selling price − estimated costs to complete and
sell.** **Write-down to NRV is recognized; subsequent recovery (up to original cost) is reversed.**

**US GAAP (post-ASU 2015-11, for non-LIFO inventory): lower of cost and NRV** — same as IFRS in concept.
**For LIFO and retail method: lower of cost or market (LCM)** with **the historical market = replacement
cost capped by ceiling / floor.**

**For each item (or appropriate grouping):**

- **Compute NRV** (or market for LCM-applicable) — **[gated]**
- **If cost > NRV: write down to NRV** — **[auto]** comparison
- **Recognize the write-down in COGS** (or a separate line)
- **Track the cost-to-NRV adjustment**

**US GAAP generally prohibits reversing inventory write-downs** — the new lower cost is the new cost.
**IFRS permits reversals if NRV recovers, up to original cost. Apply correctly.**

**Mosofin addition — anchor NRV in realised prices.** **[auto]**: **for each item, read the actual selling
prices achieved in recent months** (*`search_invoices`* line detail). This gives:

- **The realised price**, which is better evidence than a list price nobody achieves
- **The price trend** — an item whose realised price has been falling is the one most likely below cost
- **Items sold below cost already**, which is a direct, evidenced write-down candidate rather than an
  estimate

**Costs to complete and sell remain `[manual]`.** **A realised selling price is not NRV** until they are
deducted — but it is the half of the calculation that is usually hardest to support, and here it is
evidenced.

**[auto]** also: **replacement cost for LCM is approximated by recent purchase prices** for the same item.
Not the same as a market quote, and it should be labelled as an approximation — but it is a defensible
starting point when nothing else exists.

## Step 6 — Period-end entries

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

**Periodic system**: book the cost of goods sold from the computation:
```
DR  COGS                   $cost of inventory sold
    CR  Inventory               $cost of inventory sold

(For write-down to NRV:)
DR  COGS / Write-down expense   $write-down
    CR  Inventory                   $write-down
```

**Perpetual system: COGS is recorded with each sale; the period-end activity is the NRV / LCM adjustment
and reconciliation.**

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**), and
**which system applies was established in Step 0b from the data** rather than assumed.

## Step 7 — Method-comparison analysis (if useful)

**If evaluating methods, compute COGS and ending inventory under each** — **[gated]**, and **the workspace
makes this genuinely cheap**: once the transaction history is loaded, running it through three flow rules is
arithmetic.

- **FIFO typically gives the highest ending inventory and lowest COGS in rising-price environments** (and
  vice versa)
- **LIFO typically gives the lowest ending inventory and highest COGS in rising prices — and lowest taxable
  income** (LIFO's tax appeal under US GAAP); **but creates outdated inventory values on the BS**
- **Weighted-average smooths**

**Show the P&L and tax impact of each** (link to the tax provision work for tax effects of LIFO).

**[auto]** addition worth including: **whether prices actually rose over the period.** The three
characteristics above are conditional on rising prices, and **the purchase price trend is readable per
item.** In a falling-price period the conclusions invert — **state the direction rather than reciting the
rule.**

## Step 8 — Output

Deliver an `.xlsx` workpaper:

**Sheet 1: Method & Eligibility** — **method chosen, framework, system type, consistency check.** Add the
Mosofin rows: **the method the platform applies**, **the method the entity reports**, and **where the
difference is recorded**. Plus the header block: workspace name; the entity by `display_name`; excluded
company files; whether any figure rests on `mock` data.

**Sheet 2: Cost Flow** — **layer detail (FIFO / LIFO) or average computation (WAVG), with COGS and ending
inventory.** **Marked as read or reconstructed**, and if reconstructed, from which transaction population.

**Sheet 3: Per-Item / Pool Detail** — item-level costing.

**Sheet 4: NRV / LCM Valuation** — **cost vs. NRV (or LCM) per item, write-downs, reversals where
permitted.** Add **the realised selling prices used** and their dates, and **costs to complete and sell with
their source**.

**Sheet 5: Journal Entries** — period-end entries, marked as **proposals**.

**Sheet 6: Method Comparison** (if requested) — **FIFO vs. LIFO vs. WAVG impact on COGS, ending inventory,
gross profit, tax**, with **the observed price direction stated**.

**Sheet 7: Tie-Out** — **units and cost reconciliation; ties to GL** (hand to
`inventory-to-gl-reconciliation`). **Both reconciliations reported separately**, units and cost.

**Sheet 8: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

Record whether **line-level detail was available**, since layer reconstruction depends on it entirely.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Inventory_Costing_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — costs to complete, conversion costs, the count — **name the source required** instead of
estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The costing method** the entity reports on, **and the method the platform applies**, and **where the
  difference is recorded**
- **The framework** and the NRV / LCM rules that follow, including the reversal treatment
- **The system type** — periodic or perpetual — and therefore which variant applies
- **The pooling and grouping basis** for costing and for NRV assessment
- **The cost components policy**: what goes into inventory cost here, and **whether freight-in is
  capitalised or expensed**
- **The account map**: inventory, COGS, freight-in, write-down, LIFO reserve
- **The NRV basis** — which realised-price window, and where costs to complete come from. **Not the values**
- **The layer reconstruction recipe** — which populations, which fields, which date range
- **Whether standard costing is in use**, and how variances are allocated
- The replay recipe: the exact sequence of reads that produced the purchase and sales populations

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist quantities, unit costs, layer stacks, inventory values or NRV figures.** All state, and all
of it changes with every transaction. **And never persist item-level cost data as a reference** — unit costs
are commercially sensitive, and supplier pricing in particular is often confidential.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Distribution — reports FIFO, platform applies FIFO, perpetual, freight-in capitalised, NRV from trailing
3-month realised prices" — not "reports FIFO". **Method and system are entity-specific**, and applying one
entity's method to another produces a cost flow that is simply wrong. Record the chosen **scenario** (single
vs multi) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One method, one cost flow, one tie-out.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`, every
quantity and cost carrying its entity's `display_name`. Then the points specific to inventory:

- **Inventory sold between group entities carries a mark-up that is not group profit.** Where the buying
  entity still holds the stock, **the unrealized intercompany profit must be eliminated on consolidation** —
  see `consolidation-and-eliminations` and `intercompany-reconciliation`. **[gated]**: **the intercompany
  purchase quantities and prices are readable in both entities**, so the elimination can be computed, **but
  only if the goods still on hand can be identified** — which needs item-level tracking on both sides.
- **The buying entity's cost is the selling entity's price.** So **the group's cost of that inventory is the
  original entity's cost**, not what the second entity paid. **Never take the holding entity's carrying value
  as group cost.**
- **Methods must be consistent for consolidation.** Different costing methods for the same inventory class
  across entities make the group figure incoherent. **Flag differences.**
- **Inventory held on behalf of another group entity** — a distribution company holding stock owned by the
  manufacturer — **belongs to the owner, wherever it sits.** See the consignment edge case; the same
  reasoning applies within a group.
- **NRV is assessed where the inventory will be sold**, which may be a different entity in a different
  market with different realised prices. **Do not apply one entity's realised prices to another's stock.**
- **Currency**: each entity costs in its own functional currency; **inventory is a non-monetary item held at
  historical rates** — see `foreign-currency-translation-asc830`.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
