<!-- income-tax-deferred-tax-rollforward · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Build the temporary differences inventory
- Step 2 — Calculate DTAs and DTLs
- Step 3 — Rollforward DTAs / DTLs
- Step 4 — Valuation allowance assessment
- Step 5 — Tie to tax provision
- Step 6 — Journal entries
- Step 7 — Disclosures
- Step 8 — Output (Mosofin addition)
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Tax basis and enacted rates are legitimately `[manual]`.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Batch independent reads into one message** — the balances, the results history, the deferred accounts and
the profile do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the accounts carrying each temporary difference's book basis, plus the deferred
  tax asset, deferred tax liability, valuation allowance and tax expense accounts** — usually **[auto]**
- *`get_trial_balance`* / *`get_balance_sheet`* — **opening and closing balances**, both for the book-basis
  items and for the deferred tax accounts themselves — usually **[auto]**
- *`get_profit_and_loss`* **for at least three years** — **the cumulative-loss evidence** — usually
  **[auto]**
- *`get_general_ledger`* on the **deferred tax and valuation allowance accounts** — **the movements, which
  are usually a single annual journal** — usually **[auto]**
- *`search_journal_entries`* — the deferred tax entries themselves — usually **[auto]**
- *`get_company_info`* — legal name, currency, **year-end** — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **deferred tax flows into the tax provision, the
effective tax rate and the published statements.** A fixture-based book basis propagates into all three.

## Step 1 — Build the temporary differences inventory

**Common temporary differences** — with the Mosofin verdict on each item's **book** side; **every tax side
is `[manual]`**:

| Difference | Book basis source | Verdict (book side) |
|---|---|---|
| **Depreciation (book vs. tax)** | accumulated depreciation and cost | **[auto]**; **tax depreciation `[manual]`** |
| **Accrued compensation and bonuses** | accrual balances | **[auto]** |
| **Allowances (bad debt, inventory reserve)** | the allowance accounts | **[auto]** |
| **Deferred revenue / contract liabilities** | the liability balance | **[auto]** |
| **Lease accounting differences** | ROU asset and lease liability | **[auto]** if recognised; see `lease-accounting-asc842-ifrs16` |
| **Stock compensation differences** | APIC and the SBC charge | **[auto]**; **the deduction basis is `[manual]`** — see `equity-compensation-accounting` |
| **Capitalized costs (software, commissions)** | the capitalised balance | **[auto]** |
| **NOLs and credits** | — | **[manual]** entirely; not a balance sheet item on the book side |

**For each item capture:**

- **Book basis** — **[auto]**
- **Tax basis** — **[manual]**
- **Temporary difference (book − tax)** — **[gated]**, computed once both sides exist
- **Reversal pattern (timing)** — **[manual]**
- **Jurisdiction and tax rate** — **[manual]**

**Mosofin addition — map each inventory item to its account, and check the map.** **[auto]**, and it
delivers the original's own fourth quality check:

- **Two inventory items mapping to the same account** → a **double count**.
- **An inventory item with no corresponding account** → a difference with **no book support**; ask where it
  comes from.
- **A material balance sheet account with no inventory item** → a **potentially missed difference**. This is
  the direction nobody checks, and it is the one that produces understated deferred balances.

**Run all three directions**, and report them separately.

## Step 2 — Calculate DTAs and DTLs

**For each temporary difference:**

- **DTA if future tax benefit** — a **deductible** temporary difference
- **DTL if future tax cost** — a **taxable** temporary difference

```
DTA/DTL = Temporary difference × enacted tax rate
```

**[gated]**: the arithmetic is `[auto]`, **the rate is `[manual]`**. **Use the rate enacted at the reporting
date for the period in which the difference is expected to reverse** — which is why the reversal pattern in
Step 1 matters and is not a formality. **Where reversal periods span a rate change, apply the rates by
period rather than one blended rate**, and say so.

## Step 3 — Rollforward DTAs / DTLs

**Rollforward by category:**

```
  Beginning balance
+ Current period deferred tax expense/benefit
+/- FX or rate changes
+/- Acquisitions/disposals
- Utilization / reversal
= Ending balance
```

**[gated]**, with **two `[auto]` anchors that make it provable:**

1. **The beginning and ending balances must agree to the balance sheet.** **[auto]** —
   *`get_balance_sheet`* at both dates. **A rollforward that does not tie to the recorded deferred tax
   balance means either the workpaper or the ledger is wrong**, and since the entry is usually a single
   annual journal from a workpaper kept elsewhere, drift is common.
2. **The current period movement must agree to the deferred tax expense in the P&L**, adjusted for anything
   taken to OCI or equity. **[auto]** — *`get_profit_and_loss`*, *`get_general_ledger`*.

**Report both ties with their differences quantified**, including zero. **Rate changes deserve their own
line** — a rate change revalues the entire deferred balance and runs through the provision, and folding it
into "current period expense" hides one of the largest single movements the schedule ever shows.

## Step 4 — Valuation allowance assessment

**Assess whether DTAs are realizable based on positive and negative evidence:**

- **Cumulative recent losses (negative evidence)** — **[auto]** ⭐ **Compute cumulative pre-tax results over
  the recent period, typically three years.** This is **objectively verifiable** evidence and it carries
  more weight than any forecast. **A cumulative loss position is very difficult to overcome**, and stating
  it plainly, with the figures, is the most useful thing this skill does in Step 4.
- **Forecast future taxable income** — **[manual]**. No forecast on this surface, and **subjective evidence
  weighs less than objective evidence** where the two conflict.
- **Reversal of existing DTLs** — **[gated]**: the DTL balances are `[auto]`; **whether they reverse in the
  same period and the same jurisdiction as the DTAs is `[manual]`.** DTLs only support DTAs where the
  timing and the jurisdiction actually match.
- **Tax planning strategies** — **[manual]**. Must be prudent, feasible and available.

**Document conclusion and quantify valuation allowance where required.**

**Report the cumulative-loss computation explicitly, with the years and amounts**, whichever way it comes
out. A conclusion that a valuation allowance is not required, from an entity in a three-year cumulative
loss, needs the positive evidence set out in detail — and the figure is what forces that.

## Step 5 — Tie to tax provision

**The tie-out should reconcile to the total tax provision (current + deferred) and rate reconciliation.
Coordinate with `corporate-tax-provision-asc740`.**

**[gated]**: **the recorded total tax expense and its split are `[auto]`**; the current tax computation is
`[manual]`. **Prove the deferred half against the ledger**, and hand the current half to the provision
skill. **The rate reconciliation is where deferred errors surface** — an unexplained reconciling item in the
effective rate is frequently a deferred balance that was never trued up.

## Step 6 — Journal entries

`DR` is a debit, `CR` a credit. **Mosofin does not post** — these are proposals:

**Deferred tax provision entry (simplified):**
```
DR/CR Deferred Tax Expense/Benefit      XXX
    CR/DR Deferred Tax Liability            XXX
    DR/CR Deferred Tax Asset                XXX
```

**Valuation allowance (if required):**
```
DR Income Tax Expense                  XXX
    CR Valuation Allowance - DTA          XXX
```

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).
**Where a deferred movement relates to an item recognised in OCI or equity** — an OCI-recognised hedge, a
share-based payment excess benefit — **the tax follows the item**, not the P&L. **[auto]** support: whether
the entity has OCI or equity movements at all is readable, which tells you whether the question arises.

## Step 7 — Disclosures

**Prepare disclosure-ready:**

- **Components of deferred taxes** — **[gated]**; the categories come from Step 1
- **Valuation allowance rollforward** — **[gated]**; **the recorded balance and movement are `[auto]`**
- **Expiration of NOLs / credits** — **[manual]**; **expiry dates are not in a ledger**, and they are the
  part users care about
- **Rate recon support** — **[gated]**; see `corporate-tax-provision-asc740`

## Step 8 — Output (Mosofin addition)

The original lists deliverables but does not specify a workpaper. Produce one.

Deliver an `.xlsx` workpaper:

**Sheet 1: Temporary Difference Inventory** — per item: **book basis, tax basis, difference, reversal
pattern, jurisdiction, rate.** Add three Mosofin columns: **the account carrying the book basis**, **the
verdict per side**, and **the source of the tax basis**. Plus the header block: workspace name; the entity
by `display_name`; each excluded company file and why; whether any figure rests on `mock` data.

**Sheet 2: Inventory Mapping Checks — NEW, Mosofin-specific** — the three directions: double counts,
inventory items with no account, **material accounts with no inventory item**.

**Sheet 3: DTA / DTL Calculation** — difference × rate, by item and jurisdiction, **with the enactment date
of each rate**.

**Sheet 4: Rollforward** — the six lines by category, **with rate changes on their own line**.

**Sheet 5: Rollforward Tie-Out — NEW, Mosofin-specific** — opening and closing against the balance sheet,
and movement against the P&L deferred expense, **each with the difference quantified**.

**Sheet 6: Valuation Allowance Assessment** — positive and negative evidence, **with the computed cumulative
results by year shown**, and the conclusion.

**Sheet 7: Tie to Provision** — deferred half proved to the ledger; current half referenced to
`corporate-tax-provision-asc740`.

**Sheet 8: Journal Entries** — marked as **proposals**, with real account names.

**Sheet 9: Disclosure Tables** — components, valuation allowance roll-forward, **NOL and credit expirations
by year**, rate reconciliation support.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | `mock` | Gap |

**Every tax basis and every rate row reads `manual` with its source.** That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming (Mosofin addition — the original specifies none):**
`Deferred_Tax_Rollforward_[YYYY]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, and the taxpayer and jurisdiction.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — tax basis, rates, NOLs — **name the source required** instead of estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The temporary difference inventory** — which differences this entity has — **and the account carrying
  each one's book basis.** The most valuable stored asset here, and it changes rarely
- **The reversal pattern** assumed for each difference, and its basis
- **The jurisdiction map**: which entity, which taxpayer, which jurisdictions
- **The account map**: DTA, DTL, valuation allowance, current and deferred tax expense
- **The rate *source*** — where enacted rates are obtained and who confirms them. **Not the rates**
- **The valuation allowance conclusion and its reasoning**, with the date reached — **and the cumulative-loss
  measurement basis** used
- **The tax basis source** per difference — which schedule, from whom, at what cadence
- **The OCI / equity allocation policy** for deferred movements
- The replay recipe: the exact sequence of reads that produced the book bases and the tie-outs

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist tax rates, tax bases, deferred balances, NOL amounts or valuation allowance figures.** All
state. **Rates change by legislation and a stale rate silently misstates every deferred balance on the
schedule** — which then flows into the provision and the effective tax rate.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading Ltd — differences: depreciation, bonus accrual, bad debt allowance, deferred revenue; book bases in
1500/2110/1210/2400; single jurisdiction; VA released 2025 on three-year cumulative income" — not
"differences: depreciation, bonus accrual". **Jurisdiction and inventory are entity-specific**, and applying
one taxpayer's inventory to another creates differences that do not exist and misses ones that do. Record
the chosen **scenario** (single vs multi, and the tax grouping) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One taxpayer, one inventory, one
rollforward.

**Multi-entity.** Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`, every
difference and balance carrying its entity's `display_name` **and its jurisdiction**. Then the points
specific to deferred tax:

- **Deferred tax is computed per taxpayer per jurisdiction, not per reporting entity.** **The legal entity
  structure, the tax consolidation group and the reporting group frequently differ**, and the ledger knows
  none of it. **Ask, and store the map.**
- **DTAs in one entity do not offset DTLs in another** unless they are in the same taxpayer and jurisdiction
  and a legal right of offset exists. **Presenting a group net deferred balance without testing that is a
  common and material presentation error.**
- **A valuation allowance is assessed per taxpayer.** **Group profitability does not support a
  loss-making subsidiary's DTAs** where the losses cannot be used against group profits. **The cumulative-loss
  test therefore runs per entity**, not once for the group — and it is `[auto]` per entity.
- **Rates differ by jurisdiction**, and applying one entity's rate across a group misstates every balance.
  Store rates keyed by jurisdiction, and re-obtain them.
- **Intercompany profit in stock or fixed assets creates a deferred tax effect on consolidation** that
  exists in neither entity's own books. See `consolidation-and-eliminations` — the elimination creates the
  difference, so it must be computed at group level.
- **Foreign currency**: deferred balances are translated like other balance sheet items, and **the FX
  movement is a separate line in the rollforward** — see `foreign-currency-translation-asc830`. Do not fold
  it into the deferred expense.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
