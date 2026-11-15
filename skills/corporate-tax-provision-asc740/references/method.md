<!-- corporate-tax-provision-asc740 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Start from pre-tax book income
- Step 2 — Identify permanent differences
- Step 3 — Identify temporary differences
- Step 4 — Compute current tax
- Step 5 — Compute deferred tax
- Step 6 — Valuation allowance (DTA realizability)
- Step 7 — Uncertain tax positions
- Step 8 — Allocate tax (intraperiod allocation)
- Step 9 — Effective tax rate reconciliation
- Step 10 — Assemble and tie out
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

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the P&L, the
multi-year history, the deferred tax accounts and the chart of accounts do not depend on each other.
Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* for the year — **pre-tax book income**, and the tax line already posted —
  usually **[auto]**
- *`get_profit_and_loss`* for the **prior three or more years** — **the cumulative-loss evidence for the
  valuation allowance** — usually **[auto]**
- *`get_profit_and_loss`* filtered by class / department — pre-tax income by jurisdiction where
  dimensions map to them — usually **[auto]**
- *`search_accounts`* — **the deferred tax, income tax payable and tax expense accounts**, and
  **candidate permanent-difference accounts** (fines, penalties, entertainment) — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — **opening and closing deferred tax balances** —
  usually **[auto]**
- *`get_general_ledger`* on the deferred tax and tax payable accounts — the movement, and any amounts
  taken to OCI or equity — usually **[auto]**
- *`get_general_ledger`* on depreciation, accrual, provision and deferred-revenue accounts — **the book
  side of the main temporary differences** — usually **[auto]**
- *`search_journal_entries`* — prior provision entries and true-ups — usually **[auto]**
- *`search_bill_payments`* / *`search_purchases`* — **tax actually paid**, for the payable
  reconciliation — usually **[auto]**
- *`get_company_info`* — legal name, country, fiscal year end — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support a provision that goes into
published financial statements and, ultimately, a tax filing position.

## Step 1 — Start from pre-tax book income

**Begin with pre-tax income from the financial statements, by jurisdiction where the entity operates in
multiple tax regimes** (each jurisdiction has its own rate and rules) — **[auto]** in total;
**[gated]** by jurisdiction.

Take pre-tax income **before** the tax line, and state the figure and its source. Where a tax charge is
already posted, note it: you are rebuilding the provision, and the existing charge is the thing you may
be about to replace.

## Step 2 — Identify permanent differences

**Permanent differences are items treated differently for book and tax that never reverse** — they
change the effective rate but create no deferred tax:

- **Non-deductible expenses** (certain fines / penalties, some entertainment, certain executive comp,
  etc. — **jurisdiction-specific**)
- **Tax-exempt income** (e.g. certain municipal interest)
- **Non-taxable income items**
- **Tax credits** (affect tax but not book pre-tax income)
- **Permanent book-tax basis differences**

**These affect the effective tax rate but create no deferred tax.**

**[gated]**, with a real automated contribution: **scan the chart of accounts and the ledger for
candidate accounts** — anything named for fines, penalties, entertainment, donations, or similar
(*`search_accounts`*, *`get_general_ledger`*) — and present them as a **prompt list** with their
balances. Whether each is actually non-deductible is jurisdiction law and **[manual]**. This is
completeness support, not a determination.

## Step 3 — Identify temporary differences

**Temporary differences are timing differences that will reverse** — book and tax recognize the item in
different periods:

- **Depreciation** (book vs. tax methods / lives — **often the largest**)
- **Accruals not yet deductible for tax** (bonus, warranty, allowance for credit losses)
- **Deferred revenue** (taxed when received but recognized later for book, or vice versa)
- **Stock-based compensation**
- **Lease accounting differences** (ASC 842 ROU asset / liability vs. tax)
- **Reserves and provisions**
- **Capitalized vs. expensed items**
- **Unrealized gains / losses**

**Each temporary difference creates a deferred tax asset (future deductible) or deferred tax liability
(future taxable).**

**[gated]** throughout, and the split is consistent: **the book side of every item on this list is
`[auto]`** — book depreciation, the accrual balances, the deferred revenue balance, the ROU asset and
lease liability, the allowance for credit losses (*`get_general_ledger`*, *`get_balance_sheet`*) — while
**the tax side is `[manual]`** in every case. Present the schedule with the book column populated and
the tax column awaiting input; that is the honest and most useful form, and it is most of the clerical
work done.

## Step 4 — Compute current tax

```
Pre-tax book income
+/− Permanent differences
+/− Temporary differences (the current-year originations/reversals)
= Taxable income (book basis estimate of the return)
× Statutory tax rate
= Current tax expense (before credits)
− Tax credits
= Current tax expense / (payable)
```

**[auto]** arithmetic on **[manual]** rate and difference inputs.

**This estimates the current-year tax liability. It should tie reasonably to the eventual tax return
(with a return-to-provision true-up later).** **[auto]** and worth doing: compare the computed payable
against the tax actually paid and the payable carried in the ledger — a large divergence usually means a
difference has been missed rather than that the rate is wrong.

## Step 5 — Compute deferred tax

Deferred tax is computed on the **cumulative** temporary differences — not the current year's movement:

```
For each temporary difference:
  Cumulative temporary difference × enacted future tax rate = deferred tax balance

Deferred tax asset (DTA): future deductible differences + NOLs + credit carryforwards
Deferred tax liability (DTL): future taxable differences
```

**Use the enacted (US GAAP) / enacted or substantively enacted (IFRS) tax rate expected to apply when
the difference reverses — not necessarily the current rate. If a rate change is enacted, remeasure
deferred balances at the new rate (the remeasurement hits the provision in the period of enactment).**

```
Deferred tax expense / (benefit) = Change in net deferred tax balance
                                   (ending DTA/DTL − beginning DTA/DTL)
                                   excluding amounts booked to OCI or equity
```

**[auto]** for the opening balance and for isolating OCI and equity movements (*`get_general_ledger`* on
the deferred tax accounts shows where each movement went); **[manual]** for the enacted future rate.
**The exclusion of OCI and equity amounts is the step most often missed**, and it is directly checkable
here because the ledger shows the counterparty account of every deferred tax movement.

## Step 6 — Valuation allowance (DTA realizability)

**A deferred tax asset is only valuable if the entity will have future taxable income to use it
against.** This is the most judgmental area in the provision and the most scrutinised.

**US GAAP (ASC 740)**: **recognize the full DTA, then reduce it by a valuation allowance if it's "more
likely than not" (>50%) that some or all won't be realized.**

**IFRS (IAS 12)**: **recognize the DTA only to the extent it's probable that future taxable profit will
be available** — a recognition threshold rather than a separate allowance. The two frameworks reach a
similar economic answer by different mechanics, and **the presentation differs**: US GAAP shows a gross
DTA and an allowance; IFRS shows a net asset.

**Assess realizability using:**

- **Sources of future taxable income** — reversing taxable temporary differences, future operating
  income, tax-planning strategies, carryback potential. **[gated]**: reversing DTLs are **[auto]** from
  the schedule; forecasts and planning strategies are **[manual]**
- **Positive and negative evidence** — **cumulative losses are strong negative evidence**
- **A history of recent losses heavily weights toward an allowance**

**[auto]**, and this is the standout contribution of the skill: **compute cumulative pre-tax results over
the last three years** (*`get_profit_and_loss`*). A cumulative loss position is objective, verifiable
negative evidence, and it is the single item auditors weigh most heavily. **Present it as measured
evidence with the periods stated**, rather than as an impression — and note that it is difficult to
outweigh with forecasts alone.

**Document the assessment. The valuation allowance change flows through the provision.**

## Step 7 — Uncertain tax positions

**US GAAP (ASC 740, formerly FIN 48)** — **two-step**, both **[manual]**:

1. **Recognition**: is it **more likely than not** the position will be sustained on its technical
   merits, **assuming examination**? The assumption of examination matters — you may not consider the
   chance of not being audited.
2. **Measurement**: if yes, **measure at the largest benefit with >50% cumulative probability of being
   realized.**

**Record a liability (or reduce the DTA / benefit) for the unrecognized portion. Track interest and
penalties per the entity's policy.**

**IFRS (IFRIC 23)**: **reflect uncertainty using the most likely amount or expected value, whichever
better predicts resolution.**

**Maintain a UTP register with the position, assessment, and reserve.** **[auto]** only for what has
already been recorded — the UTP liability account and its movement. **Mosofin will not assess a tax
position's technical merits**; that is tax law and judgment, exactly as in
`contingencies-and-litigation-asc450`.

## Step 8 — Allocate tax (intraperiod allocation)

**Tax expense is allocated among:**

- **Continuing operations** (the main provision)
- **Discontinued operations**
- **Other comprehensive income** (e.g. tax on AOCI items)
- **Items charged directly to equity** (e.g. certain stock comp)

**Each component carries its related tax. The provision in the income statement is the
continuing-operations piece.**

**[auto]** support: the ledger shows which deferred tax movements were posted against OCI or equity
rather than the P&L, which is exactly the split this step requires. Reconcile the two — the allocation
you compute should match how the entries were actually posted, and a difference is a finding.

## Step 9 — Effective tax rate reconciliation

**Reconcile the statutory rate to the effective rate — a required disclosure and a key analytical
check:**

```
Tax at statutory rate (pre-tax income × statutory rate)        $ / %
+/− Permanent differences (e.g., non-deductibles)               $ / %
+/− State/local or other jurisdiction taxes                     $ / %
+/− Foreign rate differential                                   $ / %
+/− Tax credits                                                 $ / %
+/− Valuation allowance change                                  $ / %
+/− Uncertain tax positions                                     $ / %
+/− Rate change remeasurement                                   $ / %
+/− Other                                                       $ / %
= Total tax provision / Effective tax rate                      $ / %
```

**The ETR reconciliation must arrive exactly at the computed total provision and ETR. It explains why
the effective rate differs from the statutory rate.**

**[auto]** arithmetic. Treat the **"Other"** line as a discipline: a material unexplained residual means
a reconciling item is missing, not that the reconciliation is finished. State the threshold above which
"Other" must be broken out.

## Step 10 — Assemble and tie out

```
Current tax expense
+ Deferred tax expense / (benefit)
= Total income tax provision (continuing operations)
```

Tie-outs — all **[auto]** to compute:

- **Total provision = ETR reconciliation total**
- **Ending deferred tax balances = opening + deferred expense / (benefit) + OCI / equity pieces**
- **Net deferred tax balance classification** (non-current under current US GAAP and IFRS)
- **Current tax payable ties to the estimated return liability**
- **Provision flows to the income statement; payable / deferred to the balance sheet**

## Step 11 — Output

Deliver an `.xlsx` provision workpaper.

**Sheet 1: Provision Summary** — current + deferred = total provision; ETR. Add a header block:
workspace name; each entity by `display_name` **with its jurisdiction**; each excluded company file and
why; **every rate used with its source and year**; whether any figure rests on `mock` data.

**Sheet 2: Book-to-Tax Reconciliation** — pre-tax income → taxable income, with permanent and temporary
differences.

**Sheet 3: Temporary Differences & Deferred Tax** — each temporary difference, cumulative balance, rate,
deferred tax, opening / closing. **Mark each row's book side as read and its tax side as supplied.**

**Sheet 4: Valuation Allowance Assessment** — positive / negative evidence, conclusion, allowance
amount. **Include the measured cumulative pre-tax result for the last three years, with the periods
stated.**

**Sheet 5: Uncertain Tax Positions Register** — positions, assessments, reserves, interest / penalties.

**Sheet 6: ETR Reconciliation** — statutory to effective, in $ and %.

**Sheet 7: Deferred Tax Rollforward** — opening → P&L → OCI / equity → closing, by component.

**Sheet 8: Disclosure-Ready Figures** — for `notes-to-financial-statements` (deferred tax components,
ETR recon, NOLs, UTP rollforward).

**Sheet 9: Open Items / Rate Confirmations** — **statutory rates and enacted future rates flagged for
confirmation**, plus every other `[manual]` input outstanding.

**Sheet 10: Coverage — NEW, Mosofin-specific**

| Input or task | Entity (`display_name`) / jurisdiction | Verdict (auto / gated / manual) | Tool used / external source | Periods used | Policy | `mock` | Gap — what could not be evidenced and who supplied it |

**Every rate row reads `manual` with its source and year, or is listed as outstanding.** A rate with no
source is a defect.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

**File naming:** `Tax_Provision_[YYYY]_[EntityName].xlsx`

`[EntityName]` is the company file's `display_name`, one per entity plus a group summary. Every file
states which datasource, `display_name` and jurisdiction it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every rate, every tax basis — **name the source required** instead of estimating.

## Step 12 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A general
"yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The jurisdiction map** — which entity is taxed where, and how dimensions map to jurisdictions
- **The temporary-difference schedule structure** — which items this entity has, and which accounts feed
  each one's book side. The largest clerical saving on every future run
- **The permanent-difference candidate accounts**, and the determination reached on each (deductible or
  not), with the year it was reached
- **The account map**: deferred tax asset, deferred tax liability, valuation allowance, income tax
  payable, current and deferred tax expense, UTP liability
- **The framework**, and under IFRS the fact that DTAs are presented net of the recognition threshold
  rather than gross with an allowance
- **The rate sources** — where statutory and enacted future rates are obtained. **Not the rates
  themselves**
- **The valuation allowance conclusion and its date**, and the evidence relied on
- **The interim-provision method** if interim reporting applies
- The replay recipe: the exact sequence of reads that produced pre-tax income and the deferred balances

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist tax rates, taxable income, deferred balances, NOL amounts, or uncertain tax position
assessments.** Rates go stale and reusing one is the exact failure the standard forbids; **a stored UTP
assessment is a written record of a position the entity believes may not survive examination**, which is
sensitive in the same way a litigation assessment is. Persist the *structure and the sources*.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks / Northbrook
Trading — taxed in [jurisdiction]; deferred tax accounts 1850/2850; temporary differences: depreciation,
bonus accrual, deferred revenue; rates from the group tax adviser" — not "temporary differences:
depreciation…". Entities in different jurisdictions have different rates, different permanent
differences and different rules, and an unlabelled schedule applied to the wrong company file misstates
a published tax charge. Record the chosen **scenario** (single vs multi, and which set) as a preference
too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and **a tax rate is neither: it is the law's**, and must be re-sourced each year.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`, for one jurisdiction. One provision,
one ETR reconciliation.

**Multi-entity.** Steps 0–11 run **once per entity and jurisdiction**, each call targeting exactly one
`data_source_id`, every figure carrying its entity's `display_name` and jurisdiction. Then:

- **Compute per entity first, always.** Rates differ, rules differ, and deferred balances belong to the
  entity that will actually pay or save the tax. A pooled computation at a blended rate is not a
  provision.
- **The foreign rate differential is a group-level reconciling item.** It exists precisely because
  subsidiaries are taxed at rates other than the parent's statutory rate — so it can only be computed
  once each entity's own tax has been determined.
- **Losses do not automatically shelter profits elsewhere.** Whether a loss in one entity can offset
  profit in another depends on group relief, consolidation or grouping rules in that jurisdiction — a
  **[manual]** legal question. Never net entity results without confirming it.
- **Valuation allowances are assessed per entity.** A group that is profitable overall can contain an
  entity with a cumulative loss position and an unrecoverable DTA. The measured three-year history must
  be computed **per entity**, not for the group.
- **Global minimum tax regimes** operate at group level and are outside the per-entity computation —
  flag for a specialist; see the edge case.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each input's verdict per company
file.
