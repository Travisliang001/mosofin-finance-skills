<!-- cost-accounting-process-costing · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Cost Accounting (Process Costing) — Mosofin

Implements **process costing** for continuous or standardized production environments — chemicals,
food, refining, mass manufacturing — where costs flow through **departments or processes**.

**In plain words:** when you make thousands of identical units in a continuous flow, you cannot track
the cost of *one* of them. So instead you total up what a department spent in a month, work out how
many finished units that effort was equivalent to, and divide. The subtlety is that at any moment some
units are half-finished — so you convert them into **equivalent units**: two units half-done count as
one whole one.

It is **workspace-scoped**: departmental cost pools, WIP balances and cost flows come from tool calls
against a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

## The split that defines this skill

**Process costing is a quantity discipline. An accounting datasource holds money.**

That is the whole of it, and it is more severe here than in any other skill in this pack:

- **`[manual]`, and unavoidably so — the entire equivalent-unit computation.** Units in beginning WIP,
  units started, units completed, units in ending WIP, and the **percentage complete** of each — these
  are production floor measurements. No general ledger records how far through the process a batch is.
  Steps 2, 3 and much of 5 therefore depend entirely on supplied data.
- **`[auto]` — the cost pools and the cost flows.** What each department spent in the period, the WIP
  balance carried in each department's account, the movement between them, the transfer to finished
  goods and the relief to cost of sales — all readable.

**So the honest contribution is this: Mosofin cannot compute your equivalent units, but it can prove
that the cost flows your model produces actually tie to the ledger.** That is precisely the control most
often missing when process costing lives in a spreadsheet — the model balances internally, and nobody
checks it against the accounts. Step 6's reconciliation and Step 7's postings are where this skill earns
its place in a connected workspace.

**If a manufacturing, MES or inventory system is a connected datasource**, much of the `[manual]` half
may become readable — check at Gate 1 before assuming otherwise.

**Mosofin is read-only.** Every entry below is a *proposal* for a human.
