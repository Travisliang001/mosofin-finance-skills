<!-- standard-costing-and-variance-analysis · method.md · read for: Stages 3–6 — the standards, the variances and their causes. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 0 — Establish whether the books actually run standard costing *(Mosofin addition)*
- Step 1 — Define standards
- Step 2 — Compute key variances
- Step 3 — Build a variance bridge
- Step 4 — Investigate root causes
- Step 5 — Accounting treatment
- Outputs
- Quality checks
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin posts nothing.

---

## Inputs

All five preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **BOM and routings** | Materials, quantities, labour and machine standards | **Required** | **Not in the books.** A manufacturing system holds these. | `[manual]` |
| **Standard rates** | Material standard prices, labour rates, OH rates | **Required** | **Not in the books** — and **must carry effective dates** | `[manual]` |
| **Actuals** | Purchase prices, production usage, labour hours, OH actuals | **Required** | **Live read** for cost; **usage and hours only if quantities are exposed** | `[auto]`, partly conditional |
| **Production volumes** | Units produced, runs, scrap | **Required** | **Units, not value** — see Gate 2 | `[auto]` if exposed, else `[manual]` |
| **Inventory valuation policy** | Standard vs actual; variance capitalisation policy | **Required** | Not in the books; **the practice is observable** — see Step 5 | `[manual]` to state, `[auto]` to verify |

---

## Workflow

### Step 0 — Establish whether the books actually run standard costing *(Mosofin addition)*

`[auto]`. One read of the chart plus the variance accounts' history, and it determines whether the rest of this skill applies at all.

**Test 0a — Do variance accounts exist?**

**A variance account is the signature of a standard costing system.** Purchase Price Variance, Usage Variance, Labour Rate Variance, Overhead Absorption — if the chart carries them, standards are in operation. **If there is no variance account anywhere, the entity is on actual costing**, and the framework below describes something the business does not do. Say so rather than producing variances against standards nobody uses.

**Test 0b — Are the variance accounts clearing?** `[auto]`

Step 5 requires variances to be **closed to COGS, or prorated across inventory and COGS.** So a variance account should fill and empty on the close cycle.

**A variance account with a growing balance is variances that were never closed.** The consequence is direct: the balance sits on the balance sheet, inventory or cost of sales is misstated by that amount, and it compounds every period. **This is the same shape as a stale reserve and the never-amortised prepaid in `prepaid-amortization-schedule`** — an account nobody went back to.

Report the balance, its age, and the periods of inactivity.

**Test 0c — Is the variance one-sided?** `[auto]`, **and this is the important one.**

For each variance account, read the **sign and magnitude by period** over the longest available history.

| Pattern | Meaning |
|---|---|
| **Alternating favourable and unfavourable, roughly balanced** | A working standard. The variance is measuring performance, which is what it is for. |
| **The same direction every period, roughly stable** | **A stale standard**, offset from reality by a constant. The variance measures the offset, not the performance. |
| **The same direction and growing** | **A standard drifting further from reality** — typically input price inflation against a standard set years ago. |
| **A step change in one period** | Either a genuine operational event, **or a standard reset.** The effective dates from Gate 3 distinguish them. |

**State the finding with its figures**: *"PPV has been unfavourable in 22 of the last 24 months, averaging 3.1% of purchase value and rising. This pattern is consistent with a standard price that has not been reset rather than with purchasing performance."*

**That sentence changes what management does with the report** — from a procurement conversation to a standards-maintenance one — and it is available from one query.

**Test 0d — When were the standards last changed?** `[auto]` in part.

Quality check 3 requires standards to be **version-controlled and effective-dated.** The ledger cannot read a standards table, but **a standard reset shows up as a discontinuity in the variance series.** Where no discontinuity appears across the whole available history, the standards have probably not been reset in that time — which is itself the answer to the question.

---

### Step 1 — Define standards

**`[manual]`.** All preserved.

**Standards should be:**

- **Based on expected efficient operations** — not perfection, and not current sloppy practice
- **Reviewed periodically** — quarterly or annually — **or when inputs change**

**Document** all four:

- **Standard material prices**, including freight and duties as policy
- **Standard usage** — BOM plus expected scrap
- **Standard labour and machine times**
- **Overhead rates**, fixed and variable

**Two `[auto]` inputs to the standard-setting exercise**, which is where the ledger legitimately helps without setting the standard itself:

- **Actual purchase prices by item and vendor, over time, with volumes.** A standard price is a forward-looking policy decision, and **the recent actual price distribution is the best available evidence for it.** Present the distribution — median, range, trend — not a single average.
- **The current gap.** Where an existing standard is being reviewed, the accumulated variance says exactly how far it has drifted: **a standard producing 3.1% adverse PPV is 3.1% below the market.** That converts "the standards feel old" into a number.

**Note the "expected efficient operations" phrase carefully.** A standard set to recent actuals bakes in whatever inefficiency currently exists, and the variance then reports zero forever — which is a system that has stopped measuring anything. **The ledger supplies evidence about what things cost, not about what they should cost.**

---

### Step 2 — Compute key variances

**`[auto]` for the arithmetic once standards and quantities are available.** All eight preserved, with their formulas exactly.

**Materials**

```
Price variance (PPV):  (Actual price - Standard price) x Actual quantity PURCHASED
Usage variance:        (Actual quantity used - Standard quantity allowed) x Standard price
```

**Note the two different quantities, because it is the commonest error in this step.** PPV uses quantity **purchased**; usage variance uses quantity **used**. That is deliberate: **the price variance is recognised when the material is bought, the usage variance when it is consumed**, and in a period where purchases and consumption differ — which is most periods — using one quantity for both misstates them both. `[auto]` gets it right consistently, which is a small but genuine benefit.

**Labour**

```
Rate variance:        (Actual rate - Standard rate) x Actual hours
Efficiency variance:  (Actual hours - Standard hours allowed) x Standard rate
```

**"Standard hours allowed" means standard hours for the actual output achieved**, not for the planned output. Quality check 1 says exactly this — *volume and standard hours allowed computed correctly* — and it is the other routine arithmetic error. `[auto]`.

**Overhead** — all four preserved:

| Variance | What it measures | Verdict |
|---|---|---|
| **Variable OH spending variance** | Whether variable overhead cost more per unit of activity than standard | `[auto]` |
| **Variable OH efficiency variance** | The overhead consequence of using more or fewer activity units than allowed | `[auto]` with quantities |
| **Fixed OH spending variance** | Whether fixed overhead spend differed from budget | **`[auto]`, and the most directly readable of the eight** |
| **Fixed OH volume variance** (under/over absorption) | **A volume effect, not a cost effect** — see below | `[auto]` with volumes |

**The fixed overhead volume variance is the one most often misread**, so it is worth stating plainly. **It does not measure cost control.** It arises because fixed overhead is absorbed at a rate based on planned volume, and actual volume differed. Produce less than planned and fixed overhead is under-absorbed — an adverse variance — **without anybody having spent a penny more than budgeted.**

**Reporting it alongside spending variances without that distinction invites the wrong conversation.** Under-absorption is a production-volume issue, and the remedy is in the sales and planning function, not the factory's cost control.

---

### Step 3 — Build a variance bridge

**`[auto]`, and it is a rare thing in this pack — a tie-out that genuinely reaches across two systems.**

> Bridge from standard cost of production to actual cost:
> - **Start with standard cost** — based on standard inputs and **actual output quantity**
> - **Add variances by category**
> - **Tie to actual costs incurred**

**Why this tie-out means something.** Most reconciliations in this pack tie one part of a ledger to another part of the same ledger, and tie by construction (see `financial-statement-builder`). **This one does not.** The standard cost comes from the BOM and routings — **outside** the accounting system — and the actual cost comes from the ledger. **If the two ends meet, something real has been demonstrated:** that the standards, the quantities and the recorded costs are mutually consistent.

**If they do not meet**, the residual is informative and each shape points somewhere specific:

| Residual shape | Likely cause |
|---|---|
| Equal to a whole cost category | A variance category not computed — commonly an overhead component |
| Proportional to volume | A BOM or routing that does not match what is actually produced |
| Equal to an unposted variance balance | Test 0b — variances raised but not closed |
| Small and persistent | Rounding, or freight and duties treated inconsistently between standard and actual (see Step 1's policy point) |
| Erratic | Costs coded outside the accounted-for categories, or production quantities that do not reconcile |

**Never force the bridge to tie.** Carry the residual and name it, exactly as `ar-aging-and-collections` refuses to force a summary-to-detail tie.

---

### Step 4 — Investigate root causes

`[manual]` to conclude; **`[auto]` evidence for three of the five drivers.** All five preserved.

| Driver | Mosofin evidence | Verdict |
|---|---|---|
| **Supplier price changes** | **`[auto]`, directly** — actual purchase price by item and vendor over time. This is the largest single driver of PPV and it is fully readable, including **which vendor** and **when the change occurred.** | `[auto]` |
| **Scrap / yield changes** | `[auto]` **where quantities are exposed** — quantity used against standard allowed, by period | `[auto]` conditional |
| **Learning curve, downtime** | **Not in the books.** Operational facts. | `[manual]` |
| **Mix changes** | `[auto]` **where a product dimension exists** — the shift in production mix between products with different standard costs | `[auto]` conditional |
| **Volume changes affecting absorption** | **`[auto]`** — the fixed overhead volume variance is precisely this, and volumes are readable | `[auto]` |

**The supplier price driver deserves emphasis** because it converts the most common variance into a specific, actionable statement. Not *"PPV was adverse by 84,000"* but *"78% of the adverse PPV came from three items, all from one supplier, whose prices rose in March and have not come back."* **That is one query and it is the whole root cause for the majority of material price variance.**

**And it feeds straight back to Step 0's stale-standard test**: a supplier price that rose in March and stayed there, against a standard that has not moved, is not a recurring performance failure. **It is one price change being re-reported every month.**

---

### Step 5 — Accounting treatment

`[auto]` to draft and to verify practice; **`[manual]` for the policy and to post.**

**Policy options**, both preserved:

- **Expense variances as incurred**
- **Capitalise a portion into inventory (WIP / FG)** where material and where policy allows

**Typical variance postings** (simplified):

```
DR  Purchase Price Variance           XXX
    CR  Inventory / AP                    XXX

DR  Usage Variance                    XXX
    CR  WIP / Inventory                   XXX
```

> **Close variances to COGS or prorate across inventory and COGS based on materiality and policy.**

**`[auto]` to verify the policy is actually being followed**:

- **Is the stated policy what the entries do?** A policy of proration, with every variance closed wholly to COGS, is a policy that exists on paper only.
- **Is the proration proportionate?** Where variances are prorated, the split between inventory and COGS should broadly follow the split of the related production between stock and sold. `[auto]` to check the ratio.
- **Are variances being closed at all?** Test 0b.
- **Is capitalised variance material?** Capitalising variances into inventory carries a real risk: **if the variances are adverse and persistent, inventory is being carried above the cost an efficient operation would have incurred**, which is a net realisable value question. See `inventory-obsolescence-and-reserve`.

**That last point is worth flagging in any period where Test 0c found a persistent adverse variance being capitalised**, because it is the mechanism by which a stale standard quietly inflates the balance sheet.

---

## Outputs

All four of the original's outputs preserved, plus two Mosofin additions. Delivered as an `.xlsx` workpaper.

**Sheet 1: Variance Report by Product / Line / Plant**
| Level | Standard cost | Actual cost | PPV | Usage | Rate | Efficiency | Var OH spend | Var OH eff | Fixed OH spend | Fixed OH volume | Total |

`[auto]` given standards and quantities. **Direction and amount only — no favourable/adverse verdict colouring**, per the first near-substitute. **Fixed OH volume variance is shown in its own block**, separated from the spending variances, so it is not read as a cost-control result.

**Sheet 2: Explanations and Root-Cause Hypotheses**
`[manual]` for conclusions; **`[auto]` for the supplier price analysis, mix shift and volume effect**, each with its figures. **Labelled hypotheses**, as the original does — the word is well chosen and is preserved.

**Sheet 3: Recommended Operational Actions**
**`[manual]`.** Mosofin identifies which items and vendors drove the variance; **what to do about it is an operational decision** involving supplier relationships, alternatives and quality trade-offs that are not in a ledger.

**Sheet 4: Proposed Accounting Entries and Close Approach**
Marked **PROPOSED — NOT POSTED.** With the policy-versus-practice check from Step 5.

**Sheet 5: Standards Health** *(Mosofin addition)*
The Step 0 tests — the sheet that tells you whether the variance report means what it appears to mean:

| Test | Account | Finding | Periods | Amount | % of base | Recommended action |
|---|---|---|---|---|---|---|

Variance accounts and whether they clear. One-sidedness by variance type, with the run of consecutive same-direction periods. Apparent date of last standard reset. Capitalised variance exposure.

**Sheet 6: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet, **including whether quantities were available** — because half the variances depend on it.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Standard_Costing_Variances_[YYYY-MM]_[EntityName].xlsx`

Entity `display_name` on every sheet, and **plant identified** where several are in scope. If any read returned `mock: true`, say so in the file name and on Sheet 1.

---

## Quality checks

*(The original's own section heading, preserved. All three checks kept, with verdicts.)*

- **Volume and standard hours allowed computed correctly.** **`[auto]`** — and note it means standard hours for the **actual** output, not the planned output. This is the routine arithmetic error and automation removes it.
- **Variances reconcile to total cost difference.** **`[auto]`** — Step 3's bridge, and **it is a genuine cross-system tie**, not a construction artifact. **Never forced.**
- **Standards version-controlled and effective-dated.** **`[manual]` to maintain; `[auto]` to challenge** — Test 0c and 0d infer from the variance series whether the standards have in fact been reset, which is the substance behind the formality.

**Five Mosofin additions:**

- **Standard costing is confirmed to be in operation** before variances are computed against it.
- **Variance accounts are checked for clearing**, since an uncleared balance misstates inventory or COGS.
- **One-sidedness is tested and reported**, because a persistent variance measures the standard rather than the performance.
- **No favourable/adverse verdict is asserted** — direction and amount only.
- **Whether quantities were available is stated**, since usage, efficiency and volume variances depend on it.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any standard.** A standard rate in a seed is the worst possible version of the staleness this skill exists to detect.

**What is worth persisting into the workspace-scoped skill:**

1. **The chart mapping** — which accounts hold each variance type, which hold actual cost by category. This makes every subsequent run automatic.
2. **Whether quantities are available**, and on which transaction types.
3. **The standards' effective dates and reset history**, so Test 0c has a baseline to interpret against rather than inferring one.
4. **The freight and duty policy**, which is the commonest source of an unexplained bridge residual.
5. **The variance capitalisation policy** and the proration basis.
6. **The overhead absorption basis and planned volume**, with the date the plan was set.
7. **Vendor price baselines by item**, so a price change is reported as a change rather than re-derived each month.
8. **Findings already explained** — a one-sided variance the client has acknowledged and scheduled a reset for should not be re-raised as new every month.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — supplier prices and BOMs are commercially sensitive.

**The evolved version reports change**: which vendor prices moved this month, which variances are drifting one way, and whether the standards are still fit. That is a shorter and far more useful report than a monthly restatement of the same eight numbers.

---

## Anti-patterns

- **Reading a persistent one-sided variance as a performance problem.** It is usually a stale standard.
- **Colouring favourable variances green.** A favourable variance can mean a loose standard, a substituted input, or an unwanted bulk purchase.
- **Reading the fixed overhead volume variance as cost control.** It is a volume effect.
- **Using quantity purchased for the usage variance**, or quantity used for the price variance.
- **Using planned output for standard hours allowed** instead of actual output.
- **Deriving quantities by dividing value by standard price.** It makes the usage variance zero by construction.
- **Forcing the bridge to tie.** The residual is informative — this is one of the few genuine cross-system tie-outs in the pack.
- **Setting the standard to recent actuals.** The variance then measures nothing.
- **Capitalising persistent adverse variances without an NRV check.**
- **Summing variances across a standard reset.**
- **Aggregating plants into one PPV.** It describes no factory.
- **Chasing a supplier for an FX movement.**
- **Computing variances where no variance accounts exist.** The entity is on actual costing.
- **Recommending operational actions.** Identify the items and vendors; the decision involves quality and supply considerations that are not in the data.
- **Saying "posted".** The gateway reads.
