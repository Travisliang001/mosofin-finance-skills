<!-- inventory-obsolescence-and-reserve · method.md · read for: Stages 3–6 — identifying slow and obsolete stock and sizing the reserve. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Define reserve policy
- Step 2 — Identify slow-moving and excess
- Step 3 — LCNRV / NRV test
- Step 4 — Quantify reserve
- Step 5 — Book and track
- Step 6 — Reporting and disclosures
- Step 7 — Output (Mosofin addition)
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** The forecast and the physical condition are legitimately
`[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the items, the sales history, the purchase history and the
reserve account do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_items`* / *`search_products`* — **the item master: SKU, quantity on hand, cost, location** —
  usually **[auto]**
- *`search_invoices`* / *`search_sales_receipts`* **with line detail**, over **at least 24 months** —
  **movement by SKU: the core input** — usually **[auto]**
- *`search_purchases`* / *`search_bills`* **with line detail** — **last receipt dates and purchase prices** —
  usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **the inventory balance and the reserve balance** —
  usually **[auto]**
- *`get_general_ledger`* on **the reserve and write-off accounts** — **prior additions and write-offs: the
  back-test population** — usually **[auto]**
- *`get_profit_and_loss`* — obsolescence expense by period — usually **[auto]**
- *`search_accounts`* — inventory, reserve, obsolescence expense accounts — usually **[auto]**
- *`get_company_info`* — legal name, currency, industry — usually **[auto]**

**Pull a long history deliberately.** Movement analysis over three months finds nothing; **over two years it
finds the pattern.** And the reserve back-test needs prior periods by construction.

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap. **If line-level sales
  detail is unavailable, say that movement analysis cannot run.**
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **fixture movement history produces a fictional
slow-moving list**, and the reserve derived from it is meaningless.

## Step 1 — Define reserve policy

**Define** — **[gated]**: the policy is the user's, **the evidence for it is `[auto]`**:

- **Aging buckets** — e.g. **0–90, 91–180, 181–365, 365+ days**
- **Reserve % by bucket (based on history)**
- **Special handling** — **seasonal items, end-of-life, customer-specific**

**Mosofin addition — derive the rates from history rather than assuming them.** **[auto]**, and this is the
core contribution:

For each aging bucket, look back at the items that sat in that bucket in prior periods and ask **what
actually happened to them**:

| Outcome | How it is read |
|---|---|
| **Eventually sold at or above cost** | Sales lines at a price ≥ carrying cost |
| **Sold below cost** | Sales lines below cost — **the realised loss rate** |
| **Written off entirely** | Write-off account movements by item |
| **Still on hand** | Still in the item master, now in an older bucket |

**The resulting loss rate per bucket is an evidenced reserve percentage** — this business's own experience,
not a benchmark. **Present it alongside whatever rate is currently in use**, and let the difference be the
discussion. A 25% rate against a derived 6% is over-reserving; the reverse is under-reserving. **Either way
the conversation is now about evidence.**

**State the aging basis** with the buckets: **lot-tracked dates, or last-purchase-date proxy.** They are not
equivalent and the difference must not be silent.

## Step 2 — Identify slow-moving and excess

**For each SKU** — **[gated]**, mostly `[auto]`:

- **Compute days on hand and months of supply** — **[auto]**: quantity on hand ÷ average usage rate.
  **State the usage window used** — trailing 3, 6 or 12 months give very different answers for seasonal
  goods
- **Compare to forecast demand** — **[manual]**: **no forecast on this surface.** Where none is supplied,
  **compare to historical demand instead and say so** — it is a weaker test, and calling it a forecast
  comparison would be wrong
- **Flag no-move items** — no sales or usage in N days — **[auto]**, and the highest-value single query
  here

**Report each item with its evidence**: quantity, carrying value, last sale date, units sold in the last 12
months, months of supply. **A no-move list without carrying values is not actionable**; the reserve follows
the value, not the count.

**And apply the special-handling categories from Step 1 before presenting the list.** **Spare parts,
seasonal lines and end-of-life items with committed customers will all appear as no-move**, and every one of
them is a false positive. **Filtering them out is what makes the list credible** — an obsolescence list that
flags the critical spares is one nobody will trust again.

## Step 3 — LCNRV / NRV test

**Determine if inventory should be written down** — **[gated]**:

- **Compare cost to expected selling price less costs to sell / complete** — **the price is `[auto]`; the
  costs are `[manual]`**
- **For raw materials, consider whether finished goods NRV is below cost** — **[gated]**: raw materials are
  not written below cost merely because their own replacement price fell; **the test is whether the finished
  good they go into can still be sold profitably.** That needs the bill of materials, which is `[manual]`
  unless an ERP is connected

**Mosofin evidence — items already selling below cost.** **[auto]**: **compare recent realised sales prices
per item to carrying cost.** An item consistently selling below its carrying value is not a projection —
**it is a documented, realised loss rate**, and it is the strongest NRV evidence available. **Report the
count of such sales and the average shortfall.**

**Note the relationship with Step 4, since the two overlap and double-counting is easy:** **LCNRV is a
valuation adjustment on items you expect to sell; the obsolescence reserve covers items you expect not to
sell.** An item both slow-moving and below cost should be reserved once, on the more severe basis — not
twice.

## Step 4 — Quantify reserve

**Common methods** — **[gated]**:

- **Aging-based reserve model** — **[auto]** to compute once buckets and rates exist, **and now with derived
  rates**
- **Specific identification for known obsolete items** — **[gated]**: the items are `[manual]` to identify
  where condition is involved, `[auto]` where the trigger is movement
- **Forecast-based excess calculation** — **excess units × expected loss rate** — **[manual]** on the
  forecast; **[auto]** on the units once an expected demand figure exists

**Use one method per population and say which.** Running an aging model and a forecast-based excess
calculation over the same items and adding them together double-counts, which is the commonest error in
reserve build-ups.

**Mosofin addition — back-test the existing reserve.** **[auto]**, and it should accompany every reserve
proposal:

```
Prior period reserve balance
  compared to
Actual write-offs and below-cost sales since
  =  Over- or under-reserved
```

**A reserve consistently far above what was ever used is a cushion, not an estimate**, and an auditor will
say so. **One consistently exhausted is too low.** The pattern is readable across several periods and it is
the single best evidence of whether the model works.

## Step 5 — Book and track

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

**Entry example (reserve approach):**
```
DR Inventory Obsolescence Expense     XXX
    CR Inventory Reserve                  XXX
```

**Write off specific items (when disposed):**
```
DR Inventory Reserve                  XXX
    CR Inventory                           XXX
```

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).

**Note the two entries do different things**, which is worth stating because they are frequently confused:
**the first creates the provision against items still held; the second uses it when the item actually
goes.** A write-off booked to expense rather than against the reserve **double-counts the cost** — once when
reserved, again when written off. **[auto]** check: **write-offs posted to expense while a reserve balance
exists** is a readable pattern.

## Step 6 — Reporting and disclosures

**Provide rollforward** — **[auto]**, and it must tie to the ledger:

```
  Beginning reserve
+ Additions
- Write-offs/usage
= Ending reserve
```

**[auto]**: the reserve account's opening balance, movements and closing balance are all readable, so
**the roll-forward is not a free-standing schedule — it must agree to the account.** Report the difference,
including zero.

## Step 7 — Output (Mosofin addition)

The original lists deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper:

**Sheet 1: Reserve Summary** — the proposed reserve by method and population, and the movement from the
existing balance. Plus the header block: workspace name; the entity by `display_name`; each excluded company
file and why; **the aging basis — lot-tracked or last-purchase proxy**; whether any figure rests on `mock`
data.

**Sheet 2: Reserve Policy** — buckets, rates, special handling. **With the derived rates alongside the rates
in use**, and the derivation evidence.

**Sheet 3: SKU Exception List with Rationale** — **the original's named deliverable.** Per item: quantity,
carrying value, last sale date, units sold in 12 months, months of supply, bucket, **rationale**, and
**whether a special-handling category applies**.

**Sheet 4: Movement Analysis** — days on hand and months of supply by item, **with the usage window
stated**.

**Sheet 5: LCNRV Test** — cost versus realised price less costs to sell, **with the realised prices and
their dates**, and items already selling below cost identified.

**Sheet 6: Reserve Back-Test — NEW, Mosofin-specific** — prior reserves against actual write-offs and
below-cost sales, over several periods.

**Sheet 7: Reserve Roll-Forward** — the four lines, **tied to the reserve account with the difference
shown**.

**Sheet 8: Journal Entries** — both entries, marked as **proposals**.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Record explicitly that physical condition — damaged, expired, quarantined — is `[manual]` and was not
assessed here**, with its owner.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Inventory_Reserve_[YYYY-MM]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — the forecast, the condition, the costs to sell — **name the source required** instead of
estimating.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The aging bucket definitions** and **the aging basis** — lot-tracked or proxy
- **The reserve rate methodology** — **how the rates are derived from history, and over what window.** Not
  the rates themselves, which are recomputed
- **The special-handling categories and the items in them** — **spare parts, seasonal lines, end-of-life
  with commitments.** **The most valuable stored asset here**, because it is what keeps the exception list
  credible, and it is rebuilt painfully every time it is lost
- **The usage window** for days-on-hand and months-of-supply
- **The no-move threshold** — what N days means for this business
- **The account map**: inventory, reserve, obsolescence expense, write-off
- **The costing method**
- **The write-off policy and approval thresholds**
- **Which reserve method applies to which population**, so the populations do not overlap
- The replay recipe: the exact sequence of reads that produced the movement history and the back-test

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist SKU quantities, carrying values, reserve amounts or item-level costs.** All state.
**And never persist the exception list itself** — an item flagged as slow-moving last quarter may be
this quarter's best seller, and a stale list carried forward becomes a self-fulfilling write-off.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Distribution — buckets 90/180/365, last-purchase proxy, rates derived on trailing 8 quarters, spares
category excluded from no-move, N=365" — not "buckets 90/180/365". **Bucket definitions and special
categories are entity-specific**, and applying one entity's spare-parts exclusions to another either hides
real obsolescence or flags critical stock. Record the chosen **scenario** (single vs multi) as a preference
too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One item master, one movement history,
one reserve.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one `data_source_id`, every
item and value carrying its entity's `display_name`. Then:

- **Stock held in one entity and sold by another** splits the two inputs this skill needs. **The holding
  entity has the quantity; the selling entity has the movement.** **Read both**, and compute months of
  supply against **group** demand rather than the holding entity's own sales, which may be nil.
- **An item that is dead in one entity may be current in another.** Before reserving, **check whether the
  stock could be transferred and sold elsewhere in the group** — that is a business decision, but the data
  showing demand elsewhere is `[auto]` and it changes the answer.
- **Reserve on group cost, not the holding entity's cost**, where the stock was bought intra-group at a
  mark-up. **Reserving against
  an inflated intra-group cost double-counts a loss the group never had.**
- **Aging restarts on intra-group transfer** in most systems, which **makes transferred stock look new.**
  A readable and material distortion: check whether old stock has been moved between entities.
- **Policies should be consistent across entities** for consolidation. Different bucket definitions or rates
  produce a group reserve that means nothing. **Flag differences.**
- **NRV is assessed in the market where the item will actually sell**, which may be another entity's market
  with different realised prices.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
