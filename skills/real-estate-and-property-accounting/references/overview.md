<!-- real-estate-and-property-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Real Estate and Property Accounting — Mosofin Seed

Accounts for real estate — investment property, owner-occupied property, property under development — under the applicable framework. Handles classification, initial capitalisation including interest, subsequent measurement under the cost or fair value model, rental income, sales and disclosures.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## What this skill is, and what it is not

The original is **framework-aware** rather than framework-agnostic, and correctly so: US GAAP has no separate investment property category, while IFRS has IAS 40 with a fair value option. That distinction is preserved intact and is not softened anywhere below.

What changes in conversion is the **evidence**. This version reads one specific connected ledger. It knows which property accounts exist, what has actually been posted to them, and — crucially — **what each property has actually been doing.** That last point is what makes this skill unusually well suited to a live ledger, and it deserves setting out before the workflow.

### Classification is a conclusion about use, and use leaves a trace

Step 1 says the use determines the accounting, and that classification drives everything downstream. That is right, and it creates an obvious problem for a tool: **use is a fact about the world, not a field in a chart of accounts.**

But it is a fact about the world that generates transactions.

- A property that **earns rent from third parties** is not owner-occupied, whatever the account it sits in is called.
- A property under the IFRS **fair value model is not depreciated** — so a fair-value-model property with a monthly depreciation charge is a contradiction, not a nuance.
- A property classified **held for sale** stops being depreciated — so one that is still depreciating is either misclassified or mis-posted.
- A property still **capitalising interest** after it started generating rental income was ready for its intended use some time ago.

Each of those is a **contradiction between a stated classification and observed behaviour**, and each is one query. That is the core `[auto]` contribution of this conversion: the ledger cannot tell you what a property *is*, but it can tell you, reliably and cheaply, when the accounting does not match what the property is doing.

### A near-substitute is not a substitute

**The account name is not the classification.** An account called "Investment Property" records what somebody typed when the chart was set up, possibly years ago, possibly before the property's use changed. Classification is determined by use, and use is established from facts — who occupies the building, whether it earns rent, whether it is being actively marketed. Two of those three leave traces; the third does not. Read the traces, and confirm the classification with the user rather than inferring it from a label.

**Reading a valuation is not performing a fair value measurement.** Under the IFRS fair value model the property is remeasured at every reporting date. Mosofin can read the number somebody posted. It cannot value a building, and there is no valuation on this surface. This absence is consistent across the pack, `pensions-and-postretirement-asc715`.

### One way this skill differs from its register siblings

`fixed-asset-register-and-depreciation` and `intangibles-and-amortization` share this skill's basic shape: a register outside the books, balances inside, and a two-directional reconciliation between them. The same applies here and Step 8 sets it out.

**But the economics are different, and it changes what is worth doing.** A fixed asset register may hold four thousand items, so testing is necessarily sampled or aggregated. **A property portfolio holds five.** Each one is worth a very large amount, each has its own classification, its own measurement model, its own lease arrangements and its own history.

So the sampling logic that governs fixed assets does not apply. **Read every property, individually, every time.** It is affordable — it is five rows — and the materiality of a single classification error is enormous. A property misclassified as owner-occupied when it is investment property under IFRS changes the measurement model, the depreciation, the P&L volatility and the disclosures, all at once, for an asset worth more than most of the balance sheet.

---

## Related skills

| Skill | Relationship |
|---|---|
| `lease-accounting-asc842-ifrs16` | The lessee side, explicitly out of scope here — and the lessor side of Step 4, which coordinates with it. Also sale-leaseback. |
| `fixed-asset-register-and-depreciation` | The register discipline and the two-directional reconciliation; owner-occupied property is PP&E. |
| `intangibles-and-amortization` | The same register-outside / balances-inside shape. |
| `revenue-recognition-asc606` | Real estate sales, control transfer, and financing components. |
| `notes-to-financial-statements` | The disclosure package, including pledges and commitments. |
| `consolidation-and-intercompany-eliminations` | Why a propco's investment property is the group's owner-occupied property. |
| `intercompany-reconciliation` | Reading both sides of an intra-group rent where both entities are connected. |
| `asset-retirement-obligations-asc410` | Dismantling and restoration obligations capitalised into initial cost. |
| `debt-and-covenant-tracking` | Property-secured borrowing, and the charges that must be disclosed. |
