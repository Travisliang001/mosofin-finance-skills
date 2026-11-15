<!-- gaap-vs-ifrs-conversion · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# GAAP vs. IFRS Conversion (Mosofin)

Converts financial statements between **US GAAP and IFRS** (or local GAAP), identifying differences,
computing conversion adjustments, and reconciling the frameworks. Supports **group reporting alignment**,
**cross-border requirements**, and **first-time IFRS adoption**.

**In plain words:** the same business, the same transactions, two rulebooks — and the rulebooks disagree
about when to recognise things and what to measure them at. Converting means finding every place they
disagree for *this* business, working out how much each disagreement is worth, and showing how one set of
numbers becomes the other.

**This skill identifies and structures the major framework differences and builds the conversion mechanics.
Many differences involve significant judgment and technical complexity; the skill flags areas requiring
technical accounting expertise and audit involvement and does not oversimplify genuinely complex
conversions.**

It is **workspace-scoped**: the source balances, the chart of accounts and the scoping evidence come from
tool calls against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

## A ledger records results, not policies — and what that means here

This is the judgment that shapes everything below.

**Every conversion difference is a policy difference. Almost no policy is visible in a general ledger.**

- **Whether inventory is on LIFO** is a costing decision. The ledger shows an inventory balance.
- **Whether development costs were capitalized** is a policy. If they were expensed, **there is no account
  to find** — the evidence of the policy is the *absence* of an asset.
- **Which impairment model was applied** is a method. The ledger shows an impairment charge, or nothing.
- **Whether PP&E was revalued** is an election. Only the presence of a revaluation surplus hints at it.

**So the accounting policies are `[manual]`, and asking for them is not a formality — it is the input.**

**But the workspace contributes something genuinely useful, and it is not the balances:**

> **It scopes the conversion.** Step 1 says *"not every difference applies to every entity."* **Reading the
> chart of accounts and the balance sheet tells you exactly which of the ten difference areas are live
> here** — one query. No inventory account and the LIFO question is moot. No lease liability and ASC 842 /
> IFRS 16 needs checking rather than converting. No intangibles and no capitalised development. **A
> ten-area checklist becomes a three-area workplan before anyone opens a policy manual.**

And two more:

- **Materiality scoping is `[auto]`.** Balance sizes tell you which differences could matter, which is what
  the original's materiality input is for.
- **Contradiction detection is `[auto]`.** **The books do not declare a framework** — that is an assertion
  the user makes. But a **revaluation surplus** account in books said to be US GAAP, or **LIFO reserve** in
  books said to be IFRS, is a readable contradiction worth raising before anything is converted.

**Mosofin is read-only.** It cannot restate anything, post a conversion adjustment, or change a policy.
Every entry below is a *proposal*.
