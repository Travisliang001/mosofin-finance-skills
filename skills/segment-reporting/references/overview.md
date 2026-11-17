<!-- segment-reporting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Segment Reporting — Mosofin Seed

Prepares operating segment disclosures under the management approach (ASC 280 / IFRS 8). Identifies reportable segments, assembles segment financials, and reconciles them to consolidated totals.

The skill is **framework-aware**. The two standards are closely aligned — both use the management approach.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The question this skill turns on, and it is binary

**Is the segment structure a dimension inside the accounting system, or does it live outside?**

Everything follows from the answer, and it is genuinely one or the other:

| | Segments are a dimension in the book | Segments live outside |
|---|---|---|
| Segment P&Ls (Step 5) | **`[auto]`** — a ledger slice | `[manual]` |
| Quantitative tests (Step 3) | **`[auto]`** | `[manual]` |
| Reconciliation to consolidated (Step 6) | **`[auto]` — and ties by construction**, which is a warning, not a comfort | `[manual]`, and **will not tie by itself** |
| Uncoded transactions | **`[auto]` to find** | Invisible |

**Read the dimension list at Gate 3 and answer this before anything else.** Three other skills in this pack route their segment task on the same question — `quarter-end-close`, `revenue-recognition-asc606` and the 10-Q and 10-K preparation — and all three defer the detail to here.

### A near-substitute is not a substitute, and this is the sharpest one in the skill

> **A chart-of-accounts dimension is not an operating segment.**

The management approach is explicit: an operating segment is a component **whose results are regularly reviewed by the chief operating decision maker**. That is a fact about how the business is *run*.

A class, department or location in an accounting system is a fact about how the business is *coded*. It may match the CODM's view. It very often does not — it may be finer, coarser, a legacy of a structure abandoned two reorganisations ago, or something the bookkeeper set up to make a cost allocation easier.

**So reading the dimension list gives you a candidate structure, not the segments.**

Building a segment note from the dimensions, when the CODM reviews something else, breaks the core principle of the standard: **the note would describe the bookkeeping rather than the business.** It is also precisely what the original's final quality standard forbids — *no segment structure imposed that doesn't match how management runs the business* — and the connected-ledger version of this skill is more prone to it than the original, because the dimensions are right there and they look authoritative.

**Related, and worth restating from `quarter-end-close`: an account called "North Region Sales" is a chart-of-accounts convention, not a segment structure.** Building a segment note on account naming produces something that cannot be maintained and will not reconcile.

**And the CODM is a person or a committee.** Nothing in a general ledger identifies who allocates resources and assesses performance. Step 1 is `[manual]` at its root and no amount of data access changes that.

---

## Related skills

| Skill | Relationship |
|---|---|
| `management-reporting-pack` | Internal management reporting, explicitly out of scope — but it is where the CODM's actual reports live. |
| `notes-to-financial-statements` | The destination for Sheet 6. |
| `quarter-end-close` | Both route their segment task here, on the same dimension question. |
| `revenue-recognition-asc606` | Revenue disaggregation, which uses the same dimensions and the same binary. |
| `consolidation-and-eliminations` | Where a segment spans several company files, and intersegment eliminations. |
| `fixed-asset-register-and-depreciation` | Why long-lived assets by country is usually manual. |
| `financial-statement-builder` | The consolidated totals every reconciliation ties to — and why a guaranteed tie proves little. |
