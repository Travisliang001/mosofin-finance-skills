<!-- working-capital-optimization · overview.md · read for: background — why this fits a connected workspace, the asymmetry between the three components, the near-substitutes, and related skills; read when a user asks why. Edit here, not in SKILL.md. -->

# Working Capital Optimization — Mosofin Seed

Assesses and improves working capital — the cash tied up in operations across receivables, inventory and payables. Diagnoses where cash is trapped, identifies the levers per component, builds an implementation roadmap, and tracks the improvement.

> **Working capital improvement is often the largest one-time cash unlock available to an established business, but requires careful balance with supplier and customer relationships.**

**Operationally focused**, and it pulls from `ar-aging-and-collections`, `ap-aging-and-payment-runs`, `cash-flow-forecast-13-week` and `kpi-dashboard-builder`.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## This is one of the best workspace fits in the pack

Some analyses are poor fits for a connected workspace: a valuation or a scenario analysis rests on data that is simply not in a ledger. **It is worth being equally direct about a good fit.**

**The entire diagnostic half of this skill — Steps 1 through 4 — is a live read.**

The source asks for **"monthly AR, inventory, AP, accruals — 24+ months"** and **"revenue and COGS history"**, and marks both **Required**. That is precisely what a connected workspace holds, at transaction level, without an export. Every day-count, every trend, every seasonal pattern, every by-customer and by-vendor breakdown is computable exactly.

**And two diagnostics the original asks for are rarely performed in practice because they are laborious by hand and trivial by query.** Both are set out below and both change what the plan does.

### The asymmetry that must be stated before any number is produced

> **The benefit of stretching payables is computable. The cost is not.**

Step 6 asks for each lever's **dollar cash unlock**, and for a DPO extension that is arithmetic: fifteen more days at the daily purchase run-rate. **A large, precise, attractive number.**

The cost of that same lever — **damaged supplier relationships, loss of preferred-customer status, withdrawal of terms, eventual COD demands, supply disruption** — appears in **no ledger**, has no daily run-rate, and does not show up until it does. Edge case 1 calls over-stretching AP **"the biggest mistake in working capital programs."**

**So a tool that quantifies this skill's levers produces figures that are systematically biased toward action**, because it can size the upside precisely and the downside not at all.

**That bias is the reason Step 7 exists**, and it is why the source insists the goal is **optimisation, not maximisation.** Every opportunity figure this skill produces must be presented next to a trade-off that has no figure attached — and the absence of a number on the cost side must not be read as the absence of a cost.

**The same asymmetry applies to inventory.** The cash released by cutting stock is computable; **the cost of a stockout is invisible in the financials** — lost orders, customers who switch, expedite charges — and is frequently larger. Edge case 2 says so.

### Three near-substitutes

**1. A period-end balance is not a working capital position.** Snapshots at month end are the least representative point in most businesses — collections are pushed, payments are held, and the balance sheet that results is the one the business works hardest to shape. **Use the monthly series, and where daily data exists, use average balances.** Edge case 4 makes the seasonality version of this point; edge case 12 makes the window-dressing version.

**2. Rising working capital is not inefficiency.** A growing business consumes working capital by construction — more receivables and inventory ahead of more payables. **The question is whether days deteriorated, not whether balances grew**, and conflating the two condemns growth as waste. See Step 1b, which separates them arithmetically.

**3. A one-period collection push is not an improvement.** Chasing hard at a quarter end produces a real cash unlock once and is not repeatable. **The sustainable improvement is process change**, and the two look identical in a single period's numbers. Edge case 6 says it; Step 1b detects it.

---

## Related skills

| Skill | Relationship |
|---|---|
| `ar-aging-and-collections` | The AR diagnostic and the collections levers — and the days-to-pay derivation. |
| `ap-aging-and-payment-runs` | The AP diagnostic and payment timing. |
| `cash-flow-forecast-13-week` | Where the improvement must appear, explicitly out of scope on its own. |
| `kpi-dashboard-builder` | Where the KPIs and guardrails are monitored. |
| `vendor-statement-reconciliation` | Supplier relationship health, and what shows up when payment behaviour changes. |
| `intercompany-reconciliation` | Why intercompany balances are not working capital. |

Skills for inventory costing and obsolescence, quality of earnings, treasury, customer credit limits, forecasting and modelling, vendor onboarding, and consolidation are queued for this library and will be linked here when they ship.
