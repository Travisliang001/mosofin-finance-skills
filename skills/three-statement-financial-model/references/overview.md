<!-- three-statement-financial-model · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Three-Statement Financial Model — Mosofin Seed

Builds a fully integrated three-statement model in which the income statement, balance sheet and cash flow statement are linked by formulas, so that a change in any driver flows correctly through all three **and the balance sheet balances.**

This skill is the **integration layer** above `budget-builder` and `rolling-forecast`. It produces a live, auditable model.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## An inversion worth stating up front

Across this pack I have repeatedly warned that **a balancing balance sheet proves nothing** — in `financial-statement-builder`, a restatement review, segment reporting and elsewhere. The reason is always the same: **double entry guarantees it.** An accounting system cannot produce an unbalanced balance sheet, so the tie-out demonstrates that the software works.

**A spreadsheet model is not an accounting system, and nothing forces it to balance.**

There is no double entry in a model. Every link is a formula somebody wrote, and any one of them can be wrong. So when Step 5 says *the balance check must equal zero in every period*, **that is a genuine test** — and a non-zero result means a real, findable error: a cash flow item not linked, a schedule not flowing, or something double-counted.

**With one important qualification.** The model's **historical columns** are drawn from the ledger, and **they will balance by construction** — they inherit double entry from their source. So:

> **The balance check is meaningful in the forecast columns and guaranteed in the historical ones.**

A model whose only balancing periods are the historical ones has not been tested at all. **Check the forecast periods, and check the transition period first** — the boundary between actual and forecast is where linking errors most often live, because it is where two different construction methods meet.

---

## What the workspace supplies, and the surprise in it

The obvious contribution is the historical base. Input row 1 asks for **historical financials, at least one to two years**, and that is `[auto]` and exact — three linked statements, by period, with every account behind them.

**The less obvious contribution is that several of the model's "assumptions" are not assumptions at all.**

| Input the original marks as an assumption | What it actually is |
|---|---|
| **Working capital assumptions — DSO, DPO, DIO** | **Measurable.** The client's own realised days, per period, over the whole history — with their range and their trend. |
| **Depreciation policy** | **Depreciation on the existing asset base is already determined**, not assumed. Only depreciation on *planned* capex is a forecast. |
| **Debt schedule — existing debt** | **The opening balance is a fact.** Only new borrowings are a plan. |
| **Tax rate** | **The realised effective rate** is computable and is the best starting evidence for the assumed one. |
| **Operating margins** | **The historical margin range** is measurable, and is what any assumed margin should be defended against. |

**This matters because a model's credibility rests on its assumptions**, and an assumption that could have been measured but was invented is the easiest thing for a diligence team to take apart. Where the client's own history answers the question, **use it and say you did** — see Step 3b.

### Three near-substitutes

**1. Historical actuals are not a base case.** The ledger gives the starting position and the observed behaviour of every driver. **It does not give the forecast**, which is management's, exactly as in `rolling-forecast`.

**2. A model that balances is not a model that is right.** The balance check tests the *linking*. It says nothing about whether the assumptions are sensible, and a beautifully-linked model built on wrong drivers produces wrong answers that tie perfectly. **The check is necessary and nowhere near sufficient.**

**3. Mosofin cannot inspect an existing workbook's formulas.** The original's description includes *"refining or auditing an existing integrated model."* **Mosofin does not open an .xlsx and read its formulas, trace its precedents, or find its hardcodes.** It can build a model, and it can compare a model's *outputs* against the ledger's actuals. **Auditing the construction is a different job**, and say plainly which of the two is being done.

---

## Related skills

| Skill | Relationship |
|---|---|
| `budget-builder` | The operating build this integrates, explicitly out of scope on its own. |
| `rolling-forecast` | The other layer above the operating build — and it shares the measured drivers and seasonality. |
| `scenario-and-sensitivity-analysis` | Step 8's handoff, using the same measured driver ranges. |
| `cash-flow-statement-indirect-method` | The integrator's structure. |
| `fixed-asset-register-and-depreciation` | Committed depreciation versus capex depreciation. |
| `working-capital-optimization` | Where the measured working capital drivers lead operationally. |
