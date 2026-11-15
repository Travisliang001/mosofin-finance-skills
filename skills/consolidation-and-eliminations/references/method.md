<!-- consolidation-and-eliminations · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Determine the consolidation scope
- Step 2 — Align to common framework and currency basis
- Step 3 — Currency translation
- Step 4 — Build the consolidation workpaper
- Step 5 — Elimination entries
- Step 6 — Non-controlling interest (NCI)
- Step 7 — Equity-method investments
- Step 8 — Consolidated statements
- Step 9 — Tie-outs
- Step 10 — Output
- Step 11 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*, not
an absence.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — every entity's
trial balance can be requested together, since they do not depend on each other. Never serialize
them.

The server is **stateless**: pass `data_source_id` on **every** call. In this skill you are reading
several company files in one conversation, so **passing the wrong id silently reads the wrong
entity** — and a consolidation built on a mis-attributed trial balance is wrong in a way that is very
hard to spot. Label every result with its entity as you receive it.

Typical opening batch, **per in-scope entity**:

- *`get_trial_balance`* **at the consolidation date, same accounting method for all** — the core input
  — usually **[auto]**
- *`get_balance_sheet`* and *`get_profit_and_loss`* — for cross-checking and for the statement build —
  usually **[auto]**
- *`search_accounts`* — **to locate the intercompany accounts, the investment-in-subsidiary account
  and the equity accounts** — usually **[auto]**
- *`get_general_ledger`* on the intercompany accounts — **the transactions behind each IC balance**,
  which is what resolves a mismatch — usually **[auto]**
- *`search_invoices`* / *`search_bills`* filtered to group counterparties — **intercompany revenue and
  expense** — usually **[auto]**
- *`search_customers`* / *`search_vendors`* — to identify which counterparties are group entities —
  usually **[auto]**
- *`search_journal_entries`* — manual intercompany entries, a frequent source of one-sided IC postings
  — usually **[auto]**
- *`get_company_info`* — legal name, base currency, year end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap, **naming the entity**.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url` and treat that entity as `[manual]`.

Check the **`mock` flag` per entity**. `mock: true` anywhere in a group means the consolidated
statements rest partly on fixture data — say which entity, and do not present the consolidation as
reportable.

## Step 1 — Determine the consolidation scope

For each entity, determine whether it is **consolidated**, **equity-method**, or **neither** —
**[manual]**, since control depends on agreements the books do not hold:

**Consolidate (full consolidation) when the parent has control:**

- **US GAAP (ASC 810)**: control via majority voting interest, **OR** a **variable interest entity
  (VIE)** where the parent is the **primary beneficiary** — an entity controlled through contractual
  arrangements rather than shares
- **IFRS (IFRS 10)**: control = **power over the investee + exposure to variable returns + ability to
  use power to affect returns**

**Equity method (ASC 323 / IAS 28)**: **significant influence** (typically 20–50% ownership) but not
control. **The investment is one line; not consolidated.**

**Fair value / cost** (< 20%, no significant influence): investment carried at fair value or cost;
**not consolidated**.

**Document the determination for each entity.** This skill handles full consolidation;
**equity-method investments are carried as a single line.**

**[auto]** contribution: the connected file list and the investment accounts on the parent's balance
sheet together show which entities the parent has an investment in — a useful cross-check that the
scope list is complete. **An investment account with no corresponding entity in the scope list is a
question worth asking.**

## Step 2 — Align to common framework and currency basis

Before consolidating — **[gated]**:

- **All entities must report under the same accounting framework** (convert local-GAAP subs to group
  GAAP if needed) — **[manual]**
- **All entities must have the same reporting period** (or close enough — adjust for significant
  transactions in any gap) — **[auto]** to detect a mismatch from the profiles
- **All entities must use consistent accounting policies** (depreciation methods, inventory costing,
  etc.) — **adjust if a sub differs** — **[manual]**, though a chart-of-accounts comparison across
  entities (**[auto]**) often surfaces the differences

**[auto]** and worth doing here: compare the entities' **charts of accounts** side by side
(*`search_accounts`* per entity). Accounts that exist at one entity and not another, or that carry the
same name with a different type, are exactly what makes a line-by-line sum go wrong — and they are
mechanically detectable. See `chart-of-accounts-designer` for harmonisation.

## Step 3 — Currency translation

For each sub whose functional currency differs from the group presentation currency, translate per
**ASC 830 / IAS 21** — **[gated]**: the balances are **[auto]**, **every rate is [manual]**.

**Current rate method (functional currency = local currency)** — most common:

- **Assets and liabilities → closing (period-end) rate**
- **Equity → historical rates** (rate at the date of each equity transaction)
- **Income and expenses → average rate for the period** (approximation of transaction-date rates)
- **Resulting translation difference → Cumulative Translation Adjustment (CTA) in OCI**

**Temporal / remeasurement method (functional currency = parent's currency, sub keeps records in
local)**:

- **Monetary items → closing rate**
- **Non-monetary items** (inventory, PP&E, equity) **→ historical rates**
- **Income / expenses → average rate, except those tied to non-monetary items** (depreciation, COGS)
  **at historical**
- **Resulting difference → P&L (remeasurement gain / loss), not OCI**

**Determine functional currency first** — the currency of the **primary economic environment** — **then
apply the right method.** The distinction is not cosmetic: the same subsidiary translated the two ways
puts the difference in two different statements, and only one of them affects reported profit.

**For hyperinflationary economies (IAS 29 / ASC 830 special rules), additional restatement applies.**

Record **every rate with its source and date**. A translated trial balance whose rates cannot be
reproduced cannot be reviewed.

## Step 4 — Build the consolidation workpaper

Lay out a columnar workpaper:

```
                    Parent   Sub A    Sub B    Combined  Eliminations  Consolidated
Account             (group   (trans-  (trans-  (sum)     DR    CR       (net)
                    ccy)     lated)   lated)
Cash                 ...      ...      ...      ...                      ...
AR                   ...      ...      ...      ...             (elim)   ...
IC Receivable        ...      ...      ...      ...             (elim)   ...
...
Revenue              ...      ...      ...      ...                      ...
IC Revenue           ...      ...      ...      ...      (elim)          ...
...
```

**Sum the translated TBs, then apply elimination entries, arriving at consolidated.** **[auto]** to
build the entity columns and the sum; **[gated]** to map differing account names onto common lines,
which should be **shown as a mapping**, not applied silently.

## Step 5 — Elimination entries

`DR` is a debit, `CR` a credit; every entry balances.

**A. Intercompany balances** (from `intercompany-reconciliation`):
```
DR  IC Payable (Sub)                          $X
    CR  IC Receivable (Parent)                    $X
```
**Eliminate matched IC receivables / payables. Any residual mismatch must be resolved first (don't
eliminate an unmatched amount).**

**[auto]** where both entities are connected, and this is the standout capability of this skill: read
both sides (*`get_trial_balance`*, *`get_general_ledger`* on the IC accounts at each entity),
**quantify the difference, and investigate it in the transactions** before proposing any elimination.
The usual causes — a payment in transit, a one-sided journal, an FX difference, a cut-off timing
difference — are all visible in the ledgers.

**B. Intercompany revenue and expenses**:
```
DR  IC Revenue (selling entity)               $Y
    CR  IC COGS / Expense (buying entity)         $Y
```
**[auto]** to identify: invoices at one entity whose customer is another group entity, matched against
bills at the counterparty (*`search_invoices`*, *`search_bills`*, *`search_customers`*,
*`search_vendors`*).

**C. Unrealized intercompany profit in inventory**:
When one entity sold inventory to another at a markup and **the buyer still holds it at period-end**,
the markup is **unrealized from the group's perspective**:
```
DR  COGS / Retained Earnings                  $unrealized profit
    CR  Inventory                                 $unrealized profit
```
**Reverses when the inventory is sold externally.** **[gated]**: intercompany sales are **[auto]**;
**the markup percentage and how much remains unsold are usually [manual]** without inventory-level
detail at the buyer.

**D. Unrealized profit in fixed assets** (intercompany asset sales):
Similar — **eliminate the gain and adjust depreciation for the stepped-up basis.** The depreciation
adjustment recurs every year for the asset's life, so record it as a standing elimination.

**E. Investment in subsidiary against subsidiary equity** (the core consolidation elimination):
```
DR  Common Stock (Sub)                        $sub's equity
DR  APIC (Sub)
DR  Retained Earnings (Sub at acquisition)
DR  Goodwill (if any)                          $goodwill
    CR  Investment in Subsidiary (Parent)         $investment carrying value
    CR  Non-controlling Interest                   $NCI's share
```
**This eliminates the parent's investment account against the sub's equity, recognizing goodwill and
NCI.** (Purchase accounting detail in the business combination accounting.) **[gated]**: the sub's current
equity and the parent's investment balance are **[auto]**; **retained earnings at acquisition and
goodwill are [manual]**.

**F. Intercompany dividends**:
```
DR  Dividend Income (Parent)                  $dividend received from sub
    CR  Dividends Declared (Sub)                  $dividend
```
**[auto]** to detect from both entities' equity and income accounts.

## Step 6 — Non-controlling interest (NCI)

When the parent owns **less than 100%** of a sub, the **NCI** (minority shareholders) get their
proportional share — **[gated]**: the sub's equity and income are **[auto]**, **the ownership
percentage is [manual]**.

- **NCI on the Balance Sheet**: NCI's % × the subsidiary's net equity — at fair value under the
  **full-goodwill** method, or at proportional share under the **partial-goodwill** method (an IFRS
  option)
- **NCI on the Income Statement**: NCI's % × the subsidiary's net income — **presented as an
  allocation of consolidated net income, not an expense**:

```
Consolidated Net Income                        $total
  Attributable to NCI                          $(NCI share)
  Attributable to parent shareholders          $(remainder)
```

**NCI roll-forward:**
```
Opening NCI
+ NCI share of sub net income
+ NCI share of sub OCI
− NCI dividends
+/− Acquisitions / disposals of NCI
= Closing NCI
```

## Step 7 — Equity-method investments

For entities with **significant influence but not control** — **[gated]**, and note the asymmetry: if
the associate is **not** a connected company file, its results are entirely **[manual]**:

```
Investment in Associate (opening)
+ Share of associate net income
+ Share of associate OCI
− Dividends received from associate
+/− Other adjustments
= Investment in Associate (closing)
```

**One line on the consolidated BS; share of income one line on the consolidated IS. No line-by-line
consolidation.**

## Step 8 — Consolidated statements

After eliminations, build the consolidated:

- **Balance Sheet** (hand to `financial-statement-builder`)
- **Income Statement** (with NCI allocation)
- **Statement of Comprehensive Income** (including CTA in OCI)
- **Statement of Cash Flows** (consolidated — `cash-flow-statement-indirect-method`)
- **Statement of Changes in Equity** (including NCI column — `statement-of-equity-changes`)

Note for the cash flow statement specifically: **intercompany cash movements must be eliminated
there too**. A transfer between two group entities is a real outflow and a real inflow in the entity
statements and **nothing at all** at group level.

## Step 9 — Tie-outs

All **[auto]** to compute once the eliminations are drafted:

1. **Each elimination entry balances** (debits = credits)
2. **Consolidated BS balances** (Assets = Liabilities + Equity including NCI)
3. **Consolidated net income** = sum of entity net incomes − eliminations of intercompany profits
4. **NCI on BS** = NCI roll-forward closing balance
5. **CTA in OCI** = sum of translation differences across subs
6. **Intercompany balances fully eliminated** (no IC receivable / payable in consolidated)
7. **Intercompany revenue / expense fully eliminated** (no IC revenue / expense in consolidated)
8. **Consolidated equity attributable to parent** = parent's standalone equity + parent's share of
   post-acquisition retained earnings of subs

Tie-outs 6 and 7 are the ones a connected workspace lets you prove rather than assert, because you can
re-read both sides after eliminating.

## Step 10 — Output

Deliver an `.xlsx` consolidation workpaper.

**Sheet 1: Consolidation Workpaper** — the columnar layout: entities, sum, eliminations, consolidated.
Add a header block: workspace name; **every entity by `display_name` with its role and ownership %**;
each excluded company file and why; **any group member with no connected file**; the consolidation
date; whether any entity's data carries `mock: true`.

**Sheet 2: Currency Translation** — per sub: local TB, **rates applied with their source and date**,
translated TB, CTA computation.

**Sheet 3: Elimination Entries** — each elimination with full detail and rationale, marked as
**proposals**.

**Sheet 4: NCI Calculation and Roll-Forward**

**Sheet 5: Equity-Method Investments** — roll-forward for associates.

**Sheet 6: Consolidated Statements** — BS, IS, equity, cash flow.

**Sheet 7: Tie-Outs** — the Step 9 validations.

**Sheet 8: Intercompany Mismatch — NEW, Mosofin-specific**

| IC relationship | Entity A (`display_name`) balance | Entity B (`display_name`) balance | Difference | Investigated cause | Resolved before elimination? |

This sheet enforces the final quality standard. **An unresolved difference is reported, not
eliminated.**

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

**Per entity**, since capability varies across a group.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Consolidation_[YYYY-MM]_[GroupName].xlsx`

Every file lists which datasources and `display_name`s it consolidates, and names any group member
whose figures were supplied rather than read.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource **and by entity**. Where
the data does not cover something — every FX rate, every ownership percentage — **name the source
required** instead of estimating.

## Step 11 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

Consolidation runs every period, so this step matters a great deal here.

On an explicit yes, persist the **decisions**:

- **The group structure**: every entity by `display_name`, its role (parent / consolidated /
  equity-method / out of scope), its parent, and its **ownership percentage**. The single
  highest-value artefact in this skill
- **Functional currency per entity** and the translation method that follows, plus the group
  presentation currency
- **The account mapping** across entities onto common consolidation lines — which differing account
  names roll into which group line
- **The intercompany account pairs**: which account at which entity faces which account at which
  counterparty. This is what makes the mismatch check automatic next period
- **Standing eliminations**: the recurring ones, especially the fixed-asset depreciation adjustment
  that recurs for an asset's whole life
- **The NCI measurement option** chosen (full or partial goodwill) and the framework
- **Acquisition-date retained earnings and goodwill per subsidiary** — fixed facts that do not change
- **The rate sources** — where closing, average and historical rates come from. **Not the rates
  themselves**
- The replay recipe: the exact sequence of reads, per entity, that produced the trial balances

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files;
set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Do not persist FX rates, balances, or the consolidated statements.** Rates go stale immediately and
re-using them is exactly the error the rate-source preference exists to prevent; balances are the
period's results.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading (parent) owns 80% of quickbooks / Harbour Supplies (consolidated, EUR functional,
current-rate method); IC pair: Northbrook 1450 ↔ Harbour 2450" — not "80% owned". A group's whole
structure is relational, and an unlabelled ownership percentage applied to the wrong pair misstates
NCI and consolidated equity together. Record the chosen **scenario** (which entities, in which roles)
as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run — **and in a group the connected set changes
whenever an entity is acquired, disposed of, or reconnected**. **Decisions are the user's; state is
the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is
no longer connected is **flagged** — and in this skill that flag is significant: it may mean a
subsidiary was disposed of, which changes the consolidation scope, or merely that a connection lapsed,
which does not. **Ask which.**

---

## Both entity scenarios

**Single-entity.** This skill does not apply — there is nothing to consolidate. If only one company
file is in scope, say so and point to `financial-statement-builder` for standalone statements.

**Multi-entity.** The whole skill. Steps 0–9 read **once per entity**, each call targeting exactly one
`data_source_id`, every figure labelled with its entity until Step 4 deliberately combines them. The
specific disciplines:

- **Never combine before eliminating.** The combined column is an intermediate, not a result.
- **Measure every intercompany mismatch before eliminating it** — Sheet 8. This is the one rule most
  often broken under time pressure, and the one a connected workspace makes easy to keep.
- **Capability differs per entity**, so state which entities' figures were read and which were
  supplied. A consolidation where two of five trial balances were pasted in has a different assurance
  level from one where all five were read.
- **A group member with no connected file is named as a gap**, and the consolidation is described as
  covering the entities it actually covers.
- **Multi-tier groups consolidate bottom-up** — see the edge case; the reading order matters.
