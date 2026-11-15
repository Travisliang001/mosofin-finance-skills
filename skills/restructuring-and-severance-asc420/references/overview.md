<!-- restructuring-and-severance-asc420 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Restructuring and Severance (ASC 420 / IAS 37) — Mosofin Seed

Supports recognition, measurement and tracking of restructuring liabilities: severance, lease and facility exit costs, contract termination costs, and other exit activities.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The structural problem, stated first

Most skills in this pack analyse something that is already in the books. **This one is needed before anything is in the books.**

A restructuring accrual is recognised **when the obligation arises** — on commitment and communication — which is *before* anybody is paid, often months before. So at the moment this skill is most useful, the ledger's contribution is close to nil:

- The **plan** is a board paper.
- The **communication** is a meeting and a letter.
- The **employee list** is an HR spreadsheet.
- The **severance amounts** are in individual agreements and statutory entitlements.
- The **contract penalties** are in the contracts.

**None of that is accounting data**, and the accrual has to be built entirely from it. That is why Step 2 below is almost wholly `[manual]` and why saying so plainly matters more than dressing it up.

**What the ledger is good for is everything after.** Once the reserve exists, a connected workspace does three things well, and all three are things that go wrong in practice:

1. **Roll the reserve forward** — every line of Step 3 is a live read.
2. **Check that the recognition matched the arrangement** — if severance was taken in full at announcement and the employees stayed on payroll for six months, the future-service question was probably answered wrong.
3. **Test whether the reserve is still live.** This is the strongest single finding available, and it has its own step below.

So the shape of this skill under Mosofin is: **manual to set up, automatic to maintain, and automatic to challenge.**

### A confidentiality note, which is not boilerplate here

The inputs to this skill are **a list of named individuals who are about to lose their jobs**, frequently before it has been announced to them.

That is among the most sensitive data any of these skills touches. Treat it accordingly: compile only what the accrual requires, keep it inside the deliverable, do not put names into anything that leaves the engagement, and do not carry the list between workspaces. Where the accrual can be built and presented **by cost type and headcount rather than by name**, do that — the accounting rarely needs the names, and the working paper is safer without them.

### A near-substitute is not a substitute

**A plan is not a commitment, and a board approval is not a communication.** Recognition under ASC 420 hinges on commitment to the plan **and** communication to those affected; under IAS 37 it hinges on a detailed formal plan **and** a valid expectation raised in those affected. Both frameworks require something to have reached the employees. **A signed board minute on its own does not trigger recognition** — and neither the minute nor the announcement is in the ledger, so the recognition date is a `[manual]` fact that must be evidenced, not inferred from when someone happened to post an entry.

**Cash paid is not expense recognised.** That is the entire point of an accrual, and it is the source of the double-count in Step 3b below.

---

## Related skills

| Skill | Relationship |
|---|---|
| `lease-accounting-asc842-ifrs16` | Where the facility exit element belongs before any cease-use liability is contemplated. |
| `payroll-journal-entry-builder` / `payroll-reconciliation` | The payroll side of Test C — severance paid through wages while the accrual stands. |
| `journal-entry-builder` | Formats the accrual, payment and release entries. |
| `recurring-transaction-builder` | The schedule where a benefit is recognised across a service period. |
| `notes-to-financial-statements` | The destination for the disclosure summary. |
| `restatement-and-prior-period-adjustment` | The change-in-estimate versus error distinction on a revision. |
| `subsequent-events-asc855` | A plan communicated after the period end. |
| `pensions-and-postretirement-asc715` | Curtailments and settlements triggered by terminations. |
| `quarter-end-close` | Where the restructuring reserve appears in the quarterly estimates review. |
| `consolidation-and-eliminations` | A restructuring spanning several connected entities. |
