<!-- tax-planning-and-projections · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Tax Planning and Projections — Mosofin Seed

Forward-looking tax estimation and planning: projecting tax liability, computing estimated and quarterly payments, and evaluating the tax impact of decisions before they are made. Helps individuals and businesses plan cash for tax and make tax-aware decisions.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Two boundaries the original sets, both preserved intact

### 1. No parameters, ever

> **This skill is jurisdiction-agnostic and does not hardcode rates, brackets, thresholds, or rules — all are inputs confirmed against current sources.**

**Nothing below supplies a rate, a bracket, a threshold, an allowance or a relief limit**, and **nothing persisted from a prior run may supply one either.** A bracket stored last year is last year's bracket, and tax parameters change annually and sometimes mid-year.

This is the third source in the pack to state the discipline itself, after `r-and-d-tax-credit` and the sales tax work — **tax skills consistently understand that rates move.** The conversion extends the same instinct to capabilities: **Gate 2 reads the capability map fresh every run**, for exactly the reason the original refuses to store a rate.

### 2. Legitimate planning only

> **Tax planning has legal and financial consequences and depends heavily on specific circumstances; this skill projects and illustrates options, and recommends qualified professional advice before acting. It identifies legitimate planning, never evasion.**

**Preserved in full, and it applies to Mosofin without modification.** Step 6 sets out the line and nothing in this conversion moves it. Two additions that follow from having live data rather than a conversation:

- **Mosofin reads. It cannot conceal.** The gateway has no write path, so it cannot alter a record, remove a transaction or reclassify income. That is a structural fact worth stating, not a claim about intent.
- **A request to make income invisible is not a planning question.** If a request amounts to concealing income, inflating deductions, or constructing a transaction without substance, **it falls outside this skill entirely** — see Step 6. Say so plainly and stop; do not produce a partial version.

**And a boundary on the output itself**: this skill produces **projections and illustrations**, not advice. **A qualified professional signs off before anybody acts.** The original says this in its opening, its Step 6, and its final quality standard, and it is repeated here because a tool that reads real financial data and produces specific numbers will be read as advising whether or not it says it is.

---

## What a live ledger contributes, and what it cannot

**The shape is the same as `rolling-forecast`**, and the cross-reference is deliberate: **a projection is actuals-to-date plus a forward estimate.** The first half is a live read; the second is a judgment.

**What the workspace supplies:**

- **Year-to-date profit or income**, exactly, by source — the base of Step 1
- **Payments already made** — withholding, prior estimates, tax paid — the comparison in Step 3
- **The prior year's tax charge**, which is the safe-harbour base
- **The actual cash position**, which is what Step 4's set-aside plan is really about
- **Whether the reserve exists** — see Step 4b

**What it does not:**

- **Every rate, bracket, threshold and relief.** Current-sourced, always.
- **The forward half of the projection** — how the rest of the year goes.
- **The book-to-tax adjustments** — see below.
- **Personal circumstances**, for an individual: filing status, dependants, other income, residency.
- **The decision.**

### A near-substitute is not a substitute

**1. Book profit is not taxable income.** This is the central one.

The ledger gives you **profit as the accounts measure it.** Taxable income is that figure adjusted for **disallowable expenses, capital allowances or tax depreciation, timing differences, and reliefs** — which is precisely the work `tax-return-prep-corporate` exists to do. **Projecting tax by applying a rate to book profit is wrong by exactly the adjustments the return is for**, and it is wrong in a direction that varies by business: capital-intensive companies diverge most, and they are the ones most likely to be surprised.

**Use the book-to-tax logic**, per Step 1. Where the adjustments are not yet known, **say the projection is on a book basis and flag it**, rather than presenting an unadjusted figure as a tax estimate.

**2. The tax charge in the accounts is not the tax payable.** The provision is an accounting estimate including deferred tax; the payment is a cash obligation with its own timetable. **They differ, sometimes very substantially**, and confusing them produces a set-aside plan for the wrong number. See `corporate-tax-provision-asc740`.

**3. Year-to-date annualised is not a projection.** Exactly as in `rolling-forecast`: annualising the year so far ignores seasonality, known events and the pipeline. **It is a useful benchmark to test a projection against**, and it is not one.

---

## Related skills

| Skill | Relationship |
|---|---|
| `tax-return-prep-corporate` | The filing, explicitly out of scope — and the source of the book-to-tax logic Step 1 needs. |
| `personal-tax-return-prep` | The individual side, and the reminder that the workspace holds business books, not a person's tax position. |
| `corporate-tax-provision-asc740` | The book provision, explicitly out of scope — and why the charge is not the payable. |
| `rolling-forecast` | The income projection's forward half, its seasonality, and the discipline of re-anchoring on actuals. |
| `budget-builder` | The plan the projection can be built from. |
| `cash-flow-forecast-13-week` | Where the tax payment lands in the short-horizon cash plan. |
| `scenario-and-sensitivity-analysis` | Step 7, with ranges grounded in observed variability. |
| `r-and-d-tax-credit` | The credits lever, and the completeness sweep for unclaimed relief. |
| `fixed-asset-register-and-depreciation` | Capital allowance elections and asset timing. |
