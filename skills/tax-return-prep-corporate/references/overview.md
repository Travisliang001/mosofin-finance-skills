<!-- tax-return-prep-corporate · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Corporate Tax Return Preparation — Mosofin Seed

Prepares the corporate income tax computation and supporting workpapers: converting book income to taxable income, computing tax depreciation and capital allowances, applying loss reliefs and credits, and producing return-ready figures and schedules.

**This is the actual filing computation, distinct from the financial-reporting provision** (`corporate-tax-provision-asc740`).

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The boundaries, preserved

> **This skill is jurisdiction-agnostic in structure and does not hardcode tax rates, allowances, or rules** — these are inputs confirmed for the entity's jurisdiction and tax year.

**The fourth source in this pack to state the discipline itself**, after `r-and-d-tax-credit`, the sales tax work and `tax-planning-and-projections`. The pattern is consistent and it is correct: **tax skills understand that parameters move.** Nothing below supplies a rate, an allowance rate, a pool classification, a restriction percentage or a deadline, and **nothing persisted from a prior run may supply one either.** Gate 2 applies the same rule to capabilities.

> **The skill organises the computation; jurisdiction-specific forms and rules must be confirmed against current official sources, and complex returns should be reviewed by a qualified local tax preparer.**

**Preserved without qualification.** A tax return is a legal filing with penalties attached. This skill assembles a computation and its workpapers; **it does not sign, file, or replace a local preparer**, and for cross-border or complex positions it does not attempt the judgment at all — see the edge cases.

---

## What a live ledger changes here

**The starting point is a single number, and it is a live read.**

Step 1 begins with **pre-tax accounting profit**, and the whole computation hangs off it. That figure, and every account behind it, is readable exactly. So is book depreciation — the largest add-back in most computations. So are asset additions and disposals, payments made, and the candidate population for most of Step 2.

**What is not readable is everything that makes it a tax computation**: which items are disallowable in this jurisdiction, the capital allowance pools and rates, the loss attributes and their restrictions, the elections available and their deadlines.

### Three near-substitutes

**1. Book profit is not taxable income.** Shared with `tax-planning-and-projections`, and here it is the skill's entire subject matter — the computation *is* the set of adjustments between them.

**2. Tax attributes are not accounting balances.** A loss carryforward, an unused credit, a capital allowance pool balance, a made election — **none of these are ledger balances.** They live in the tax computation and the prior year's return. The ledger may carry a *deferred tax asset* recognising some of them, but that is an accounting measurement subject to recoverability, **not the attribute itself.** Reading a deferred tax asset and inferring the loss carryforward is wrong in both directions and by an unpredictable amount. See `income-tax-deferred-tax-rollforward`.

**3. The provision is not the return, and their difference is not an error.** The provision is an estimate made before the computation is done; the return is the computation. **They are expected to differ**, and the difference is the **return-to-provision true-up** — a normal part of the annual cycle, not a mistake to be reconciled away. Step 10 and edge case 10 both cover it, and treating the difference as a discrepancy is a common misreading.

---

## Related skills

| Skill | Relationship |
|---|---|
| `corporate-tax-provision-asc740` | The financial-reporting provision, explicitly out of scope — and the return-to-provision true-up destination. |
| `income-tax-deferred-tax-rollforward` | Deferred tax, and why a DTA is not the loss attribute. |
| `personal-tax-return-prep` | Individual returns, explicitly out of scope. |
| `tax-planning-and-projections` | The forward-looking version, using the same book-to-tax logic. |
| `fixed-asset-register-and-depreciation` | The book register, kept separate from the tax one. |
| `r-and-d-tax-credit` | The credits lever and its cost-population sweep. |
| `related-party-disclosures-asc850` | Identifying those dealings, and evidencing arm's length. |
| `consolidation-and-eliminations` | Group filing, and why reading several ledgers is not consolidating them. |
| `year-end-close` / `month-end-close-checklist` | Whether the starting point is genuinely final. |
| `restatement-and-prior-period-adjustment` | Where a moved prior period leads. |
| `subsequent-events-asc855` | The same discipline of re-running a check immediately before the document goes out. |
