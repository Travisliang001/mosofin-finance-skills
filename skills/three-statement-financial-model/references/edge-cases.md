<!-- three-statement-financial-model · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All eleven preserved, in order.

**Circular reference from interest-on-cash**: **handle explicitly — opening balances, or iterative calculation with a switch. Never leave an uncontrolled circularity.** `[manual]`, and **test stability across the scenario range**, not only at base.

**Negative cash before the revolver**: **the revolver / cash-sweep should automatically draw to keep cash at a minimum and sweep excess to repay. Build the mechanism so cash never goes implausibly negative without a financing response.** `[auto: computed]`. **`[auto: read]` for the realistic minimum**: the business's actual historical minimum cash balance is a better floor than a round number, and **whether a facility actually exists is a fact** — a model drawing on a revolver the company does not have is modelling a financing that would have to be negotiated.

**Multi-entity / consolidated model**: **build entity-level models, then consolidate. More complex; keep eliminations explicit.** `[auto: read]` per entity; **`[manual]` for the eliminations.** See Gate 1 — **the error compounds across the horizon.**

**Multi-currency**: **model in functional currency per entity; translate for consolidation. FX assumptions as inputs.** `[manual]` for the FX assumption — **never supplied by this file**, consistent with `rolling-forecast` and `recurring-transaction-builder`. See the foreign currency translation work, and its warning that **CTA absorbs translation errors silently**, which in a model means a translation error that does not break the balance check.

**Deferred taxes**: **a simple model uses an effective rate; a rigorous one tracks deferred tax assets and liabilities. State which.** `[manual]`; `[auto: read]` for the realised rate.

**Leases (ASC 842 / IFRS 16)**: **ROU assets and lease liabilities add schedules; lease payments split between principal (financing) and interest (operating). Build a lease schedule if material.** `[auto: read]` for the existing ROU asset and lease liability balances; **`[manual]` for the schedule**, which lives outside the ledger. **A model omitting the lease schedule understates both assets and debt**, which distorts leverage — the metric a lender looks at first.

**Stock-based compensation**: **non-cash expense — add back in the cash flow; builds APIC in equity.** `[auto: read]` for the historical charge; **`[manual]` for the forecast**, which needs grant data and there is **no cap table on this surface.**

**Acquisitions in the forecast**: **add purchase accounting — goodwill, fair-value step-ups. Affects all three statements.** `[manual]`. **A modelled acquisition changes the opening balance sheet of every subsequent period**, so it cannot be bolted onto the income statement alone.

**Working capital seasonality**: **if intra-year, a monthly model captures it; an annual model uses period-end balances. Match granularity to need.** **`[auto: read]` to detect whether seasonality exists** — monthly working capital days across the history show it immediately. **An annual model in a seasonal business understates peak working capital**, and peak working capital is what determines the facility the business needs.

**Model used for fundraising or valuation**: **extra rigour on assumptions defensibility. Ensure the model is clean enough to hand to a diligence team.** **This is where Step 3b pays for itself** — measured drivers with their ranges are exactly what a diligence team asks for, and having them ready changes the tenor of the process.

**Hardcoded plugs**: **never plug the balance sheet to force a balance. If it doesn't balance, find the error. A plug hides a real problem.** **`[auto: computed]` to detect** — a constant in a statement formula is mechanically findable in a model being built here. **And note the distinction from Step 3**: a revolver is a modelled mechanism; a plug is a typed number. **Same word, opposite things.**
