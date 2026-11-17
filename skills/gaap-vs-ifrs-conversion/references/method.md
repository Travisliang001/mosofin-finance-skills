<!-- gaap-vs-ifrs-conversion · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding) — Mosofin addition
- Step 1 — Scope the conversion
- Step 2 — Identify the differences by area
- Step 3 — Classify each difference
- Step 4 — Quantify the conversion adjustments
- Step 5 — First-time adoption (if applicable)
- Step 6 — Build the reconciliation
- Step 7 — Restate the statements and policies
- Step 8 — Output
- Step 9 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with plain-language
wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool added.

**Never drop a task because no tool covers it.** Every policy here is legitimately `[manual]`, and saying so
is the honest result.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding) — Mosofin addition

**Run before the Gate 3 interview**, because what you read determines what you need to ask.

**Batch independent reads into one message** — the accounts, the balance sheet, the P&L and the profile do
not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — **the full chart of accounts**, which is the scoping instrument — usually **[auto]**
- *`get_trial_balance`* at the conversion date — usually **[auto]**
- *`get_balance_sheet`* current and comparative — usually **[auto]**
- *`get_profit_and_loss`* for the period — usually **[auto]**
- *`get_general_ledger`* on any account whose balance drives a difference area — usually **[auto]**
- *`get_company_info`* — legal name, currency, country, year-end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — **a conversion reconciliation built on fixtures
produces a bridge between two sets of imaginary statements**, and it is often prepared for a listing, a
lender or a group parent.

## Step 1 — Scope the conversion

**Identify which areas are likely to differ between the two frameworks for this entity, based on its
activities. Not every difference applies to every entity. Prioritize by materiality and likelihood.**

**[auto]**, and this is where the workspace earns its place. From the chart of accounts and the balance
sheet, determine which of Step 2's areas are actually live:

| Area | Live if the accounts show… | Verdict |
|---|---|---|
| **Inventory** | any inventory balance | **[auto]** to detect; costing method `[manual]` |
| **PP&E** | fixed asset and accumulated depreciation accounts | **[auto]** to detect |
| **Impairment** | impairment charges, or material long-lived assets | **[auto]** to detect |
| **Development costs / R&D** | R&D expense, or capitalised development intangibles | **[auto]** to detect |
| **Leases** | right-of-use assets and lease liabilities, **or their absence alongside rent expense** | **[auto]**, and **the absence is the finding** |
| **Financial instruments** | investments, loan receivables, allowances | **[auto]** to detect |
| **Revenue** | always live, but differences are narrow | **[gated]** |
| **Provisions / contingencies** | provision and accrual balances | **[auto]** to detect |
| **Income taxes** | current and deferred tax balances | **[auto]** to detect |
| **Other** — capitalised interest, pensions, share-based payment | interest capitalised in assets, pension liabilities, SBC expense and APIC movement | **[auto]** to detect |

**Report the scoping result explicitly, including the areas ruled out and why.** *"No inventory balance, so
the LIFO difference does not apply"* is a documented scoping conclusion, and the original's own quality
standard asks for exactly that — **document why an area was assessed as immaterial or inapplicable.**

**One scoping result deserves special attention: rent expense with no lease liability.** Under both ASC 842
and IFRS 16 most leases are capitalised. **An entity with material rent expense and no right-of-use asset
has either no leases in scope or an unrecognised conversion issue** — and it is readable in one query.

## Step 2 — Identify the differences by area

**Major US GAAP vs. IFRS differences — illustrative; confirm current standards, as both frameworks
evolve.** **[manual]** throughout on the entity's actual treatment; `[auto]` only on whether the area
exists.

**Inventory**:
- **LIFO is permitted under US GAAP but prohibited under IFRS** — a LIFO entity **must convert to FIFO or
  weighted-average** (significant). See `inventory-costing-fifo-lifo-wavg`.
- **Inventory write-down reversals: prohibited under US GAAP, permitted (up to original cost) under IFRS.**

**Property, plant & equipment**:
- **IFRS allows a revaluation model** (carry at fair value); **US GAAP uses cost model only.**
- **Component depreciation is required under IFRS**, more common practice.
- **Impairment: different models** — see below.

**Impairment**:
- **US GAAP (long-lived assets)**: two-step-ish, **recoverability test using undiscounted cash flows
  first.**
- **IFRS (IAS 36)**: one-step, **recoverable amount** — higher of fair value less costs and value in use,
  **discounted**; **impairment reversals permitted (except goodwill)**; **US GAAP generally prohibits
  reversals.**
- **Goodwill impairment models differ.**

**Development costs / R&D**:
- **US GAAP**: generally **expense R&D as incurred**, with specific software exceptions.
- **IFRS (IAS 38)**: **research expensed, but development costs capitalized when criteria are met.**
  Coordinate with `intangibles-and-amortization`, the R&D tax credit work.

**Leases**: **both now capitalize most leases (ASC 842 / IFRS 16) but with differences — IFRS 16 has a
single lessee model; ASC 842 retains operating vs. finance lease expense patterns.** See
`lease-accounting-asc842-ifrs16`.

**Financial instruments**: **classification and impairment — expected credit loss models — differ between US
GAAP (CECL) and IFRS 9.**

**Revenue**: **ASC 606 and IFRS 15 are largely converged, but some application differences exist.** See
`revenue-recognition-asc606`.

**Provisions / contingencies**: **recognition threshold differs** — "probable" means different things;
**IFRS uses present-obligation / IAS 37.**

**Income taxes**: **ASC 740 vs. IAS 12 differences** — classification, recognition of deferred tax on
certain items, intra-period allocation.

**Other**: **capitalization of interest, defined benefit plans (ASC 715 vs. IAS 19), share-based payments
(ASC 718 vs. IFRS 2 — e.g. graded vesting), and presentation differences.**

**For each applicable area, document the source treatment, the target treatment, and the nature of the
difference.**

**Mosofin contradiction check.** **[auto]**: certain accounts are framework-revealing. **A revaluation
surplus** implies IFRS (or a local GAAP permitting it) — it cannot exist under US GAAP. **A LIFO reserve**
implies US GAAP. **An impairment reversal** in the ledger cannot be US GAAP. **Where the account evidence
contradicts the stated source framework, raise it before converting anything** — either the framework
assertion is wrong or the accounting is.

## Step 3 — Classify each difference

**[manual]**, and the classification drives the mechanics:

- **Recognition difference**: **an item recognized under one framework but not the other** — e.g.
  capitalized development costs
- **Measurement difference**: **measured differently** — e.g. revaluation, impairment amount, inventory
  method
- **Presentation / disclosure difference**: **same numbers, different presentation / classification**
- **Timing difference**: **recognized in different periods**

**This classification determines whether a conversion adjustment affects the balance sheet, income
statement, equity, or just presentation.**

**Presentation differences deserve a note**: they change **no** number in the reconciliation, which makes
them easy to overlook and easy to under-deliver. **They still require work** — reordering the balance sheet,
changing terminology, restructuring disclosures. Track them separately so they are not lost among the
adjustments that carry amounts.

## Step 4 — Quantify the conversion adjustments

**For each material difference, compute the adjustment** — **[gated]**: the arithmetic is `[auto]`, the
inputs are the `[manual]` schedules:

- **Restate the affected balances and results under the target framework**
- **Determine the adjustment to assets / liabilities, the income statement effect, and the equity effect**
- **Track the deferred tax effect of each adjustment** — a conversion adjustment usually creates or changes
  a temporary difference; see the tax provision work

**Build each adjustment as a conversion entry with full support.**

**The deferred tax point is the one most often missed**, and the original flags it twice for that reason.
**Every recognition, measurement and timing adjustment changes the gap between book and tax carrying
amounts.** **[auto]** support: the current and deferred tax accounts and the effective rate are readable,
which grounds the gross-up — but the **applicable rate and the recoverability assessment are `[manual]`**.

## Step 5 — First-time adoption (if applicable)

**If converting to IFRS for the first time (IFRS 1)** — **[manual]** throughout:

- **Establish the transition date** — the opening balance sheet date
- **Apply IFRS retrospectively, with IFRS 1's mandatory exceptions and optional exemptions**, which can
  simplify certain areas — e.g. **deemed cost for PP&E, business combinations**
- **Recognize the cumulative conversion adjustment in opening retained earnings** — or appropriate equity —
  **at the transition date**
- **Prepare the required IFRS 1 reconciliations** — **equity and total comprehensive income from previous
  GAAP to IFRS**

**[auto]** contribution: **the opening balances at the transition date are readable** (*`get_trial_balance`*,
*`get_balance_sheet`* at that date), which is the starting point the reconciliations bridge from. Everything
else — the exemptions elected, the retrospective application — is judgment with lasting consequences.

## Step 6 — Build the reconciliation

**Produce the bridge between frameworks** — **[auto]** arithmetic once the adjustments exist:

```
Net income (source GAAP)
+/− each conversion adjustment (with tax effect)
= Net income (target framework)

Equity (source GAAP)
+/− each conversion adjustment (with tax effect)
= Equity (target framework)
```

**These reconciliations are the headline deliverable — they show exactly how and why the two frameworks
differ for this entity, line by line.**

**Mosofin note on the starting point:** the **source** net income and equity are `[auto]` and should be
**tied to the connected books explicitly**, with the tool call and as-at date recorded. **A reconciliation
whose opening figure cannot be traced to the source statements is not a reconciliation** — and it is the
one figure in this whole skill that the workspace can prove.

## Step 7 — Restate the statements and policies

- **Produce the financial statements under the target framework** — **[gated]**; hand off to
  `financial-statement-builder`, which handles framework presentation and the cross-statement tie-outs
- **Rewrite the accounting policies to the target framework** (`notes-to-financial-statements`) —
  **[manual]**
- **Address presentation differences** — e.g. **IFRS balance sheet ordering, terminology** — **[gated]**
- **Prepare target-framework disclosures**, which **often differ in extent** — **[manual]**

**IFRS disclosure requirements are generally more extensive**, so a conversion that balances perfectly can
still be incomplete as a reporting package. Say what remains to be drafted.

## Step 8 — Output

Deliver an `.xlsx` conversion workpaper:

**Sheet 1: Conversion Summary** — **net income and equity reconciliation (source → target), with each
adjustment.** Plus the Mosofin header block: workspace name; the entity by `display_name`; each excluded
company file and why; **the source and target frameworks as asserted by the user**; whether any figure rests
on `mock` data.

**Sheet 2: Difference Analysis**

| Area | Source Treatment | Target Treatment | Difference Type | Material? | Adjustment |

Add two Mosofin columns: **In scope for this entity?** and **Scoping evidence** — the account or balance
that made it live, or the absence that ruled it out.

**Sheet 3: Conversion Adjustments** — each adjustment with **computation, the entry, and tax effect**,
marked as **proposals**.

**Sheet 4: Restated Statements** — balance sheet, income statement, equity under the target framework.

**Sheet 5: First-Time Adoption** (if applicable) — **transition date, exemptions elected, opening
adjustments, IFRS 1 reconciliations.**

**Sheet 6: Policy Differences** — source vs. target policies for affected areas.

**Sheet 7: Open Items / Technical & Audit** — **judgmental and complex areas flagged for technical
accounting and audit.**

**Sheet 8: Scoping — NEW, Mosofin-specific**

| Difference area | Live here? | Evidence (account / balance / absence) | Materiality | Policy supplied? |

**Every one of the ten areas appears**, including those ruled out. The original's quality standard requires
documenting why an area was assessed as immaterial — this is where that lives.

**Sheet 9: Coverage — NEW, Mosofin-specific**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used / external source | As-at date | Policy | `mock` | Gap |

Every policy row reads `manual` with its source. That is the correct entry.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `GAAP_IFRS_Conversion_[YYYY]_[EntityName].xlsx`

Every file states which datasource and `display_name` it covers, and **the direction of conversion**.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every policy, every schedule — **name the source required** instead of estimating.

## Step 9 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The source and target frameworks**, and **the direction**
- **The applicable difference areas for this entity**, and **the documented reasons the others were ruled
  out** — this is the scoping asset, and it changes rarely
- **The policy position in each live area**, source and target — the answer to "how does this entity
  actually account for inventory / development / impairment"
- **The classification of each difference** — recognition, measurement, presentation, timing
- **The adjustment methodology** per difference, and its supporting schedule source
- **The IFRS 1 exemptions elected**, if first-time adoption — **these have lasting effects and must never be
  re-decided casually**
- **The account map**: which accounts drive which difference area
- **Whether dual reporting is ongoing**, and the cadence
- The replay recipe: the exact sequence of reads that produced the scoping and the source figures

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist balances, adjustment amounts, restated figures or reconciliation totals.** All of it is
state, and a conversion reconciliation is a point-in-time bridge that must be rebuilt, never recalled.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
GmbH — local GAAP to IFRS for group reporting, live areas: leases, development costs, provisions; inventory
ruled out (no balance); IFRS 1 deemed cost elected 2025-01-01" — not "local GAAP to IFRS". **The live-area
scoping is entity-specific by construction**, and applying one subsidiary's scope to another skips the
differences that actually matter there. Record the chosen **scenario** (single vs multi, and each entity's
current framework) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and every balance and every adjustment amount is state.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One framework pair, one scoping, one
reconciliation.

**Multi-entity.** **The common case, because group reporting alignment is the commonest reason to convert.**
Steps 0–8 run **once per entity**, each call targeting exactly one `data_source_id`, every balance and
adjustment carrying its entity's `display_name`. Then:

- **Each subsidiary may be on a different source framework.** A group with entities in three countries may
  be converting from three different local GAAPs to one IFRS. **Scope, policy and adjustments are all
  per-entity**; only the target is shared.
- **Scope each entity separately.** The live-area list for a manufacturing subsidiary and a services
  subsidiary have almost nothing in common. **Reusing one entity's scoping across the group is how material
  differences go unfound.**
- **Convert before consolidating.** Conversion adjustments belong in each entity's own restated figures;
  `consolidation-and-eliminations` then consolidates a set of statements already on one framework.
  Consolidating first and converting the total conceals which entity each difference came from.
- **Order with translation matters too.** Where entities also report in different currencies, **convert the
  framework first, then translate** — see `foreign-currency-translation-asc830`. Converting a translated
  figure mixes two effects in one adjustment.
- **Policy alignment is a group decision, not an entity one.** Where subsidiaries make different elections
  in the same live area — say, one componentising PP&E and one not — **the group must pick one**, and the
  difference between them is itself a conversion adjustment.
- **The reconciliation is presented per entity and in total.** A group-level bridge alone hides which
  subsidiary drives which movement.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file, **and Sheet 8 shows each entity's scoping separately.**
