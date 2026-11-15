<!-- valuation-agent-dcf-comps-football-field · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Valuation Agent — DCF, Comps, and Football Field — Mosofin Seed

Builds a valuation from forecast cash flows and market evidence. **The output keeps WACC, terminal value, comparable screens and valuation ranges visible and editable.**

> **Do not bury valuation assumptions deep in hidden tabs or hardcoded formulas.**

Preserved as the skill's opening instruction, because it is the discipline that makes a valuation reviewable — and it is the same principle `three-statement-financial-model` applies to a model's drivers.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Be direct about the fit

**This is among the poorest workspace fits in the pack, and saying so is more useful than dressing it up.**

A valuation rests on two things, and neither is in a general ledger:

| Ingredient | Where it lives |
|---|---|
| **Forecast cash flows** | **A model.** An assertion about the future. `[manual]`, from `model-builder-integrated-three-statement`. |
| **The discount rate** | **Markets.** Risk-free rate, equity risk premium, beta — **market data, not on this surface.** |
| **Comparables** — trading and transaction | **Public filings and deal databases.** Not on this surface. |

**A ledger records what a business has done. A valuation is a statement about what it is worth to somebody**, which depends on the future and on what other assets are priced at. The absence of valuation data is consistent across the pack — see `goodwill-and-impairment-testing`, `business-combinations-asc805`, `pensions-and-postretirement-asc715`, `real-estate-and-property-accounting`.

### What *is* automatic, and it is the part most often got wrong

**The net debt and equity bridge.** Step 6 converts enterprise value to equity value, and **most of its components are balance sheet items.**

That sounds clerical. It is not, because **the bridge is where valuations quietly go wrong** — a well-argued enterprise value is destroyed by a net debt figure that missed something. And the thing most often missed has a specific cause:

> **Lease liabilities are debt, they are on the balance sheet under ASC 842 and IFRS 16, and net-debt definitions carried over from older habits omit them.**

For a lease-heavy business — retail, restaurants, logistics, anything with property — **that omission overstates equity value by the whole lease liability.** `[auto]` reads it directly. See Step 6b.

**Two further contributions**, both borrowed from skills that do them properly:

- **The model's historical base can be tied to the accounts** — the check `three-statement-financial-model` describes. **A DCF built on a model whose history does not match the ledger is built on sand**, and diligence finds it.
- **Several cash flow assumptions are measurable**: capex as a percentage of revenue, working capital days, margin history, the realised tax rate. **An assumption defended by the business's own history is a much stronger assumption**, and it is free.

### A boundary on what this produces

The Inputs table asks for the **purpose of the valuation**, and two of the listed purposes — **financial reporting and tax** — are regulated contexts where a valuation must be prepared or signed by a qualified professional. M&A and fundraising valuations are relied on by counterparties.

> **Mosofin produces valuation analysis. It does not produce an opinion of value, and it is not a licensed valuation professional.**

Where the purpose is financial reporting, tax, a transaction or an external fundraise, **say plainly that a qualified valuation specialist is required**, and treat this skill's output as working analysis feeding that process. Same discipline as `tax-planning-and-projections`.

### Three near-substitutes

**1. Book value is not enterprise value.** The balance sheet records what was paid for things, less depreciation. It does not value a business, and the gap between the two is usually most of the answer.

**2. The realised effective tax rate is not the DCF's tax rate.** Step 2 takes **cash taxes on EBIT** — a normalised, forward-looking rate on unlevered earnings. **The historical effective rate embeds one-off adjustments, prior-year items, and the effect of actual leverage** (since interest is deductible and the DCF is unlevered). Reading last year's effective rate into a DCF imports all of that. `[auto]` supplies it **as evidence**; the rate is `[manual]`. See `tax-return-prep-corporate`.

**3. A model's forecast is not evidence.** It is an assertion, and the DCF inherits its quality entirely. **The tie-backs in Step 2 test consistency, not truth.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `model-builder-integrated-three-statement` / `three-statement-financial-model` | The forecast model, explicitly out of scope — and the source of the tie-back discipline. |
| `model-auditor-financial-model-review` | Whether the model behind the DCF is sound. |
| `scenario-and-sensitivity-analysis` | The sensitivity tables, with grounded ranges from the same measurements. |
| `lease-accounting-asc842-ifrs16` | Lease liabilities in net debt, and the EBITDA basis question. |
| `pensions-and-postretirement-asc715` | Pension deficits as a debt-like item. |
| `equity-compensation-accounting` | Options, warrants and the cap table this surface lacks. |
| `statement-of-equity-changes` | The other skill whose per-share line requires a cap table. |
| `goodwill-and-impairment-testing` | Where a valuation feeds a financial reporting requirement — and needs a specialist. |
| `business-combinations-asc805` | Purchase price allocation, which needs valuations too. |
| `due-diligence-quality-of-earnings` | Who tests this analysis hardest, and what they check first. |
| `consolidation-and-eliminations` | Consolidated net debt versus summed net debt. |
| `tax-return-prep-corporate` | Why the realised effective rate is not the DCF's tax rate. |
