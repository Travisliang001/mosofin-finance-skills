<!-- cost-accounting-process-costing · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Map the production flow
- Step 2 — Build the physical units schedule
- Step 3 — Compute equivalent units
- Step 4 — Compute cost per equivalent unit
- Step 5 — Assign costs to output
- Step 6 — Reconcile cost rollforward
- Step 7 — Accounting postings and close
- Step 8 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** In this skill the quantity half is legitimately
`[manual]` — that is the nature of process costing in an accounting workspace, and saying so clearly is
the correct outcome.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the departments, the
cost ledger, the WIP balances and the inventory accounts do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_departments`* / *`search_classes`* — **the departments or processes** — usually **[auto]**
- *`get_profit_and_loss`* filtered by department — **costs added by department** — usually **[auto]**
- *`get_general_ledger`* on the production cost accounts, by department — **direct materials, labour and
  overhead added in the period** — usually **[auto]**
- *`search_accounts`* — **the WIP account per department, finished goods, and cost of sales** — usually
  **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **opening and closing WIP and FG balances** — usually
  **[auto]**
- *`get_general_ledger`* on the WIP accounts — **the transfers between departments and out to finished
  goods** — usually **[auto]**
- *`search_bills`* / *`search_purchases`* — materials purchased into the process — usually **[auto]**
- *`search_time_activities`* — labour hours by department, where tracked — usually **[auto]**
- *`search_items`* — the item master for finished goods — usually **[auto]**
- *`search_journal_entries`* — prior period cost-flow entries — usually **[auto]**
- *`get_company_info`* — currency and calendar — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — a cost per unit computed on it would flow into
inventory valuation and into the price list.

## Step 1 — Map the production flow

Define — **[manual]** for all three, with the dimension list as a starting point:

- **Where materials are added** (start vs mid-process). This single fact determines the material
  equivalent-unit percentage: material added entirely at the start means ending WIP is **100% complete
  for materials** however little processing has happened
- **Conversion cost pattern** (labor + overhead) — usually assumed to accrue evenly through the process
- **Transfer pricing between departments** (usually cost) — at cost, no margin arises internally; at
  anything else, an internal profit must be eliminated from inventory

**[auto]** contribution: the department list and the pattern of transfers already posted between WIP
accounts (*`get_general_ledger`*) reveal the **actual** production sequence, which occasionally differs
from the one described. Compare the two.

## Step 2 — Build the physical units schedule

For each department — **[manual]**, entirely:

```
- Beginning WIP units
+ Units started
= Units to account for
```

Then:

```
- Units completed and transferred out
+ Ending WIP units
= Units accounted for
```

**The two totals must agree.** A difference is spoilage, evaporation, shrinkage or a counting error —
and the first quality check exists to force that question rather than let the schedule silently absorb
it. Ask for the expected normal loss so an abnormal one can be distinguished.

## Step 3 — Compute equivalent units

Compute equivalent units for — **[manual]**:

- **Direct materials**
- **Conversion costs**

They differ precisely because materials and conversion enter the process at different rates.

By method:

- **Weighted-average**: **blends beginning WIP and current period.** Simpler; the cost per unit mixes
  last period's costs with this one's
- **FIFO**: **isolates current-period work.** More precise, and the better choice when input prices are
  moving, because it shows this period's actual cost per unit

**State the method on the output.** The two produce different unit costs from identical facts, and a
period-to-period comparison across a method change is meaningless.

## Step 4 — Compute cost per equivalent unit

- **Weighted-average**: `Cost per EU = (Costs in beginning WIP + costs added) / equivalent units`
- **FIFO**: `current period costs / current period equivalent units`

**[auto]** for the numerator in both cases — costs added and the cost carried in beginning WIP are
readable. **[manual]** for the denominator. **The arithmetic is `[auto]` once both exist**, and the
result should be presented with its inputs visible, since a unit cost with no visible denominator cannot
be reviewed.

## Step 5 — Assign costs to output

Assign:

- **Costs to units completed and transferred out**
- **Costs to ending WIP**

**[auto]** arithmetic on the Step 3 and 4 results.

## Step 6 — Reconcile cost rollforward

Ensure:

- **Total costs to account for = costs assigned to transferred out + ending WIP**

**[auto]**, and this is where the connected workspace matters most. Do **two** reconciliations, not one:

1. **Internal**: the model's costs to account for equal the costs it assigned. This proves the
   arithmetic.
2. **To the ledger** — *the Mosofin addition*: the model's **beginning WIP equals the opening WIP account
   balance**, its **costs added equal the period's postings to that department**, its **transfers out
   equal the transfers posted**, and its **ending WIP equals the closing WIP account balance**
   (*`get_balance_sheet`*, *`get_general_ledger`*).

**A model that reconciles internally but not to the ledger is a model of a business that does not
exist.** Any difference is real: unposted costs, costs posted without a department tag, a transfer made
in the model but not in the books, or a manual entry to WIP that bypassed the process entirely. Report
each difference with its amount; do not force either side.

## Step 7 — Accounting postings and close

Typical accounting flows — **[auto]** to verify against what was actually posted:

- **Costs accumulate in WIP (by department)**
- **Transfers move cost from Dept A WIP to Dept B WIP**
- **Completions move to Finished Goods**
- **Shipments relieve to COGS**

Example transfers (conceptual). `DR` is a debit, `CR` a credit. **Mosofin does not post** — these are
proposals:

```
DR WIP - Dept B                     XXX
    CR WIP - Dept A                     XXX
```

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**),
and where the entries already exist, this step becomes a **review** of what was posted rather than a
proposal to post it — say which of the two you did.

## Step 8 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The department sequence** — which process feeds which, and how each maps to a dimension value
- **The method** — weighted-average or FIFO — so it stays consistent period to period
- **The material addition points** per department, and the conversion cost pattern
- **The account map**: WIP per department, finished goods, cost of sales, and the production cost
  accounts that feed each pool
- **The transfer pricing basis** between departments
- **Normal spoilage / yield expectations** per process, so abnormal loss can be identified
- **Who supplies the unit counts and completion percentages**, and when in the close they arrive
- The replay recipe: the exact sequence of reads that produced the cost pools and WIP balances

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist unit costs, WIP balances, unit counts or production volumes.** Unit cost is the basis
of pricing and is commercially sensitive; volumes reveal capacity. Persist the *structure and the
method*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northwood
Processing — departments Mixing → Filling → Packing tagged by Department; weighted-average; materials
added at start in Mixing, evenly in Packing" — not "weighted-average". Plants differ in sequence and in
where materials enter, and an unlabelled addition point applied to the wrong company file misstates
every equivalent-unit figure. Record the chosen **scenario** (single vs multi, and which set) as a
preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and unit counts, completion percentages and WIP balances are all state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Departmental cost of production report.** Per department: units to account for and accounted for,
  equivalent units, cost per equivalent unit, and costs assigned — **with the method stated on its
  face**.
- **Equivalent unit schedule.** Materials and conversion separately, with **the completion percentages
  used, who supplied them, and the date of the count**.
- **Cost per equivalent unit.** With its numerator and denominator both visible.
- **WIP / FG rollforward.** Per department, **reconciled to the ledger balances**.
- **Variance and reasonability checks.** Including cost per unit against the prior period, and the units
  tie-out.

**Ledger reconciliation — NEW, Mosofin-specific.**

| Model figure | Ledger figure | Difference | Explanation |

Covering opening WIP, costs added, transfers out and closing WIP, per department. **This sheet is the
skill's main contribution in a connected workspace.**

**Coverage sheet — NEW, Mosofin-specific.**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

Every unit count and completion percentage reads `manual` with its source. That is the correct, expected
result.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs it):
`Process_Costing_[YYYY-MM]_[EntityName].xlsx`, where `[EntityName]` is the company file's `display_name`.
Every file states which datasource and `display_name` it covers, and the method used.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every unit, every percentage — **name the person who supplied it** instead of
estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One department chain, one set of
cost pools.

**Multi-entity.** Steps 0–7 run **once per entity**, each call targeting exactly one `data_source_id`,
every department and pool carrying its entity's `display_name`. Then:

- **A process spanning entities is an intercompany transfer, not a departmental one.** Part-finished
  goods moving from one company's plant to another's are a sale and a purchase between legal entities,
  with a transfer price that may include margin. **That margin is unrealised at group level** until the
  goods are sold externally — hand it to `consolidation-and-eliminations`, and note that it sits in
  inventory, so it must be stripped out of the group's WIP and finished goods.
- **Cost pools are per entity and never pooled.** Each plant's overhead belongs to the entity that
  incurred it.
- **The method should be consistent across the group** for group reporting, even where each entity
  computes its own. A group mixing weighted-average and FIFO across plants cannot present a coherent
  inventory valuation policy.
- **Department names repeat across plants.** "Mixing" at two entities is two different cost centres —
  map them explicitly before any comparison.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
