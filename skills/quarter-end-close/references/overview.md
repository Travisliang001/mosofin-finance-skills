<!-- quarter-end-close · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Quarter-End Close — Mosofin Seed

Plans and executes the incremental procedures required at quarter-end, beyond a normal monthly close. Built for entities with a quarterly reporting obligation: SEC filers, borrowers with covenant tests, companies on a quarterly board cadence.

This is a **seed skill**. It is written to run against a live Mosofin workspace and to be rewritten the first time it does, because a client's quarterly obligations are not knowable in advance.

---

## What this skill is, and what it is not

The original described itself as **system-agnostic**. The reporting logic still is — an estimated annual effective tax rate works the same way in every ledger on earth. The **evidence** is not. This version reads one specific connected set of books, knows what is actually in them, and is correspondingly less portable. That is a real trade and it is stated here rather than glossed over.

### The shape of the problem, stated once, up front

A quarter-end close is two things stacked on each other:

1. **A monthly close.** Cutoffs, reconciliations, accruals, entries, tie-outs. The ledger does most of this work and `month-end-close-checklist` already knows how to make it do so.
2. **The quarterly increment.** Tax provision, subsequent events, going concern, covenant testing, estimates review, sub-certifications, segment disclosure.

The second layer is not more of the first. **It is a different kind of work.** Look at what the increment is actually made of:

- an **estimated annual effective tax rate**, which needs a full-year forecast that does not exist in any ledger
- **subsequent events**, which are by definition things that happened after the period closed, and mostly are not transactions at all
- a **going-concern assessment**, which is forward-looking for twelve months from issuance
- an **estimates and reserves review**, whose entire subject matter is the part of the accounts that is *not* a transaction
- **covenant testing**, where the definitions live in a credit agreement and not in the chart of accounts
- **sub-certifications and a disclosure committee**, which are people signing things

So the honest headline for this skill is: **the monthly close is where the ledger does the work; the quarterly increment is where the judgment does.** A large share of the steps below are `[manual]`, and that is not a deficiency in the gateway. It is what quarterly reporting is.

### Which does not mean the workspace contributes little

Two blocks of this skill are almost entirely automatic, and the original treats both as clerical drudgery:

- **Step 5, the year-to-date roll-forwards.** Seven of them, plus the trial-balance continuity test. Every component is a live read. This is hours of work in a manual close and it is one batched query here.
- **Step 6, cumulative validation.** Four of the five tests are live reads that tie one part of the ledger to another.

And there is a third contribution the original could not have had at all, because it requires *history*: a live ledger holds eight or twelve quarters of posting behaviour, and that behaviour has a shape. Reserve rates that never move. Quarters that were closed and then reopened. And the big one:

**If Q4's journal-entry volume dwarfs Q1 through Q3, the quarters were never really closed.** The year-end audit found everything, and Q4 absorbed the lot. Every interim number that was reported during that year was a placeholder. That finding is the whole justification for quarterly close discipline, and it is one query against posting counts.

---

## Related skills

| Skill | Relationship |
|---|---|
| `month-end-close-checklist` | The foundation. Step 1 runs it in full; the quarterly work sits on top and never replaces it. |
| `year-end-close` | Q4 goes there, not here. |
| `debt-and-covenant-tracking` | Covenant ratios, thresholds and the definitions that govern them. |
| `budget-vs-actual-analysis` | QTD and YTD variance against plan. |
| `management-reporting-pack` | The board pack. |
| `cash-flow-statement-indirect-method` | QTD and YTD cash flow. |
| `bad-debt-and-write-offs` | AR allowance roll-forward and rate. |
| `inventory-obsolescence-and-reserve` / `inventory-to-gl-reconciliation` | Inventory reserve roll-forward, and the same-database caveat. |
| `sox-controls-design-and-testing` | Quarterly control testing and sub-certifications. |
| `internal-audit-workpaper` | Why a population read is not a control test. |
| `subsequent-events-review` | Type 1 and Type 2 classification in depth. |
| `financial-statement-builder` | The statements that go into the 10-Q or the board pack. |
| `rolling-forecast` / `cash-flow-forecast-13-week` | The re-forecast. |
| `cohort-and-unit-economics` / `kpi-dashboard-builder` | The KPI deep-dive, and which parts of it the ledger owns. |
| `audit-pbc-list-manager` | The interim review PBC list. |
| `consolidation-and-intercompany-eliminations` | Where quarterly reporting is consolidated across connected entities. |
