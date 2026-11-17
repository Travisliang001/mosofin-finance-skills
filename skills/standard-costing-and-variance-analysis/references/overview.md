<!-- standard-costing-and-variance-analysis · overview.md · read for: background — which variances the books can compute and which need production data. Edit here, not in SKILL.md. -->

# Standard Costing and Variance Analysis — Mosofin Seed

Implements standard cost frameworks and performs variance analysis to explain differences between standard and actual costs, for operational improvement and accurate financial reporting.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The asymmetry that shapes this skill

**Every variance has two halves. The ledger holds one of them.**

| Half | Where it lives | Verdict |
|---|---|---|
| **The standard** — BOM, routings, standard prices, standard times, overhead rates | **A manufacturing or ERP system, or a spreadsheet.** A general ledger holds costs, not bills of material. | `[manual]` |
| **The actual** — purchase prices, labour cost, overhead spend | **The ledger.** | `[auto]` |

So a variance cannot be computed from a connected workspace alone, and this skill will always need the standards supplied. **What the workspace gives you is the actual side, exactly, at transaction level — and something more useful than that.**

### The finding this conversion exists for

Variance analysis is *supposed* to measure **performance**: how did the operation do against a fair expectation?

**But a variance measures the gap between two numbers, and either one can be wrong.** If the standard is stale, the variance measures the staleness. And this is not a rare case — it is arguably the commonest condition of a standard costing system that has been running for a few years without discipline.

> **A persistently one-sided variance is not a performance problem. It is a standard that needs resetting.**

A standard material price set two years ago, in a period of rising input costs, produces an **unfavourable purchase price variance every single month**, no matter how well the buyer negotiates. Management sees twelve consecutive months of adverse PPV and concludes that purchasing is underperforming. **The correct conclusion is that the standard is out of date**, and the two look identical in a monthly variance report.

**Distinguishing them is arithmetic over the variance account's history**, and it is `[auto]`. See Step 0. This is the single most valuable thing this skill can say against a live ledger, and it directly serves the original's own instruction that standards be *"reviewed periodically or when inputs change"* and its quality check that standards be *"version-controlled and effective-dated."*

### Three near-substitutes

**1. A favourable variance is not good news.** This deserves stating because a tool will otherwise colour it green.

A favourable PPV can mean the buyer did well. It can equally mean the standard is loose, that a cheaper and lower-quality input was substituted (which will show up later as a usage or scrap variance, or as a warranty cost), or that a large opportunistic purchase was made that has created inventory the business does not need. **A favourable labour efficiency variance can mean work was rushed.** A favourable fixed overhead volume variance means more was produced than planned, which is favourable only if the output can be sold.

**Report the direction and the amount. Do not report a verdict.**

**2. The purchase price in the ledger is not the standard price.** Obvious, and worth saying because the ledger's price is right there and the standard is not. Reading actual prices and calling their average a standard converts standard costing into a slow-moving actual costing.

**3. Value is not quantity.** Several variances need **units** — quantity purchased, quantity used, hours, units produced. **Many accounting systems hold value and not quantity**, or hold quantity on some transaction types and not others. **Check before promising a usage or efficiency variance**; without units, only the price and spending variances are computable and the analysis is half an analysis. See Gate 2.

---

## Related skills

| Skill | Relationship |
|---|---|
| `inventory-to-gl-reconciliation` | Where variance balances land, and the subledger-equals-GL caveat. |
| `inventory-obsolescence-and-reserve` | Net realisable value, where adverse variances have been capitalised into stock. |
| `job-costing-and-wip` | The project-based analogue, and where production dimensions are set up. |
| `budget-vs-actual-analysis` | Variance against plan rather than against standard — related discipline, different baseline. |
| `three-way-match` | Where the actual purchase price enters the ledger. |
| `month-end-close-checklist` | Where variance closing belongs as a recurring close task. |
| `financial-statement-builder` | Where uncleared variance balances misstate inventory and COGS. |
| `scenario-and-sensitivity-analysis` | Input cost volatility, measured from the same purchase history. |

Other skills this one touches are queued for this library and will be linked here when they ship.
