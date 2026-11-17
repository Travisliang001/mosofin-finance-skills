<!-- restatement-and-prior-period-adjustment · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Restatement and Prior Period Adjustment — Mosofin Seed

Handles the correction of errors in previously-issued financial statements: assessing the error, evaluating materiality, determining the correction method, computing the corrections, and preparing restated figures with the required disclosures.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The one thing to understand before anything else

The original is **framework-aware** (ASC 250 / IAS 8) and is explicit that this work carries **audit, governance and — for public companies — regulatory implications.** All of that is preserved and none of it is softened.

What conversion adds is an observation about evidence that changes how this skill starts.

> **The current ledger's view of a prior period is not what was reported.**

A restatement concerns **previously-issued financial statements**. Those statements are a published document — a filing, a signed set of accounts, a pack sent to a lender. They are a fixed artefact, sitting in a PDF somewhere.

**The ledger is not fixed.** If anybody has posted into a closed period since those statements went out, the books' version of last year and the issued version of last year **have already diverged** — and nothing in the accounting system marks the divergence, warns about it, or prevents it.

This has two consequences, and the second one is the more interesting.

**First**, the issued figures are a `[manual]` input. They come from the document, not from a query. Reading a prior-year trial balance today and treating it as "what we reported" is exactly the error this skill exists to correct, performed by the person correcting it. Get the statements.

**Second — and this inverts the usual direction of the work** — the ledger can tell you that **an error has already been corrected without anyone assessing it.** Somebody found a problem, posted a fix into the prior year, and moved on. The books are now right and the issued statements are now wrong, and:

- nobody assessed materiality
- nobody chose a correction method
- nobody disclosed anything
- nobody told the auditors
- and every comparative in every subsequent report is drawn from a ledger that no longer matches the filing

**That is a restatement that has already happened and been left undocumented**, and finding it is one query. `quarter-end-close` runs this test as a routine control; here it is the primary detection mechanism.

Normally this skill is invoked because somebody already knows about an error and wants it sized. **The ledger lets it also be invoked the other way round** — ask the books what has quietly changed, and work backwards.

---

## Related skills

| Skill | Relationship |
|---|---|
| `quarter-end-close` | Runs the prior-period integrity test as a routine control and routes here when it finds something material. |
| `year-end-close` | The same, annually. |
| `financial-statement-builder` | Produces the restated statements — and supplies the caution that a balancing balance sheet proves only arithmetic. |
| `notes-to-financial-statements` | The destination for Sheet 7. |
| `sox-controls-design-and-testing` | The control deficiency and material weakness assessment. |
| `internal-audit-workpaper` | Why a population observation about postings is not a control test. |
| `fraud-detection-and-forensics` | Where the error stems from fraud — and the discipline of reporting figures, not allegations. |
| `debt-and-covenant-tracking` | Recomputing covenants on corrected figures, and the definitions that govern them. |
| `journal-entry-builder` | Formats the correction entries in Sheet 5. |
| `journal-entry-review` | Where a prior-period posting would have been caught at the time. |
| `consolidation-and-eliminations` | Where entity-level and group-level materiality diverge. |
