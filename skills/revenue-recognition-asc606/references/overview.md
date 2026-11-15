<!-- revenue-recognition-asc606 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Revenue Recognition (ASC 606 / IFRS 15) — Mosofin Seed

Applies the five-step revenue-recognition model to customer contracts. Produces the analysis, the recognition schedule, and the entries that flow from it. Handles point-in-time and over-time recognition, multiple performance obligations, variable consideration, and contract modifications.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The one sentence this whole skill turns on

> **An invoice is not revenue.**

That is the entire point of ASC 606 and IFRS 15, and it is exactly what a tool connected to a general ledger will get wrong — because **a general ledger is organised around invoices.** Invoices are what it stores, what it totals, what it ages, what it reports. Revenue under the standard is a conclusion about *performance*, and performance is described in a contract that the accounting system has never seen.

So the honest division for this skill is unusually clean and unusually lopsided across its eleven steps:

- **Steps 1 to 4 — identify the contract, identify the performance obligations, determine the transaction price, allocate it —** are read out of an **agreement**. The ledger contributes very little, and the little it contributes is worth having (see the SSP note below) but does not change the character of the work. **Largely `[manual]`.**
- **Steps 5 to 11 — the schedule, the contract balances, the entries, the modifications, the costs, the disclosures —** are arithmetic and bookkeeping once the analysis exists. **Largely `[auto]`.**

And there is a third thing the workspace can do that the original could not, which is arguably the most valuable of all: **test whether the books apply the standard at all.** That is Step 0.

The original is **standards-aware** — ASC 606 or IFRS 15, substantially converged with a few genuine differences (the shipping and handling election, licensing nuances) — and that is preserved. It is also **chart-of-accounts-agnostic** and **jurisdiction-agnostic for tax**: rev rec timing under GAAP is independent of tax reporting in most jurisdictions, and book-to-tax differences belong in the tax provision work. All of that stands. What is no longer agnostic is the *evidence*, which now comes from one specific connected ledger.

### Three near-substitutes, all of which produce confident wrong answers

**1. The billing schedule is not the recognition schedule.** They coincide only when performance and billing happen to align, which is the exception rather than the rule. A schedule built from invoice dates is a billing schedule wearing the standard's clothes.

**2. Deferred revenue is not RPO.** Remaining performance obligations include committed amounts **not yet billed**; deferred revenue captures only what *has* been billed and not yet recognised. Reporting the deferred revenue balance as RPO understates it systematically, and the gap widens with contract length. Consistent with `quarter-end-close`, which makes the same point about the KPI pack.

**3. Cash received is not a contract.** Step 1's five criteria include collectibility being probable, and none of the five are visible in a bank line. A payment tells you money arrived, not that a contract exists in the standard's sense.

---

## Related skills

| Skill | Relationship |
|---|---|
| `customer-invoicing` | Explicitly out of scope — the billing process, which this skill deliberately separates from revenue. |
| `ar-aging-and-collections` | Receivables, and the payment history that informs the collectibility criterion in Step 1. |
| `journal-entry-builder` | Formats the entries in Step 7. |
| `multicurrency-fx-revaluation` | FX on receivables and contract assets — separate from revenue. |
| `quarter-end-close` | Where RPO, disaggregation and contract balances appear in the quarterly pack. |
| `deferred-revenue-schedule` | The balance this skill's Step 6 produces, maintained period to period. |
