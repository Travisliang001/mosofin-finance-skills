<!-- intercompany-reconciliation · overview.md · read for: background — what is reconciled, and what reading both sides live changes. Edit here, not in SKILL.md. -->

# Intercompany Reconciliation (Mosofin)

Matches **intercompany balances and transactions** across entities of a consolidated group. Identifies
**mismatches**, proposes **settlements**, and prepares **elimination entries** for consolidation.

**In plain words:** when companies in the same group trade with each other, every transaction should appear
twice — once as a sale in one set of books and once as a purchase in the other, in equal and opposite
amounts. In practice they frequently do not match, because one side posted late, used a different rate, or
never posted at all. This finds the differences, explains them, and works out what to settle.

**This skill is multi-entity by nature. It can reconcile any number of entities pairwise.**

It is **workspace-scoped**: each entity's intercompany ledger, its functional currency and its chart of
accounts come from tool calls against company files connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## This is the skill the workspace fits best — and the one gate that must not be skipped

**Nearly every other skill in this pack needs something the accounting system does not hold.** This one needs
**two entities' ledgers, matched against each other** — and in a Mosofin workspace **both are live, at the
same moment, in the same conversation.**

The original assumes a **CSV or XLSX export per entity**, exchanged by email and already stale by the time
anyone opens it. Here:

- **The entity list is Gate 1's output.** Step 1's primary input is a tool result, not a question.
- **Each entity's IC ledger is `[auto]`**, at transaction level, with **reference numbers, dates, amounts
  and counterparty names** — exactly the fields Step 2 matches on.
- **Both sides are read in the same batch**, as at the same instant. **No version skew between sides**,
  which is itself a recurring cause of phantom mismatches.
- **Functional currency per entity is `[auto]`** from each company profile.
- **Matching is a pure data operation over two readable datasets** — the part of this skill that is usually
  the slowest becomes the fastest.

**And the gate that must not be skipped:**

> **A pair can only be reconciled if BOTH sides are connected.** If entity B is not in the workspace, you
> have **A's view of the balance — and A's view of the balance is not the balance.** A single-sided read
> tells you what A thinks B owes it, which is precisely the number in question.
>
> **Never present a single-sided figure as a reconciliation.** List the pair as **not reconciled**, name the
> missing counterparty, and say what would be needed. This is the most likely failure mode of this skill in
> a real workspace, because groups rarely have every entity connected.

**What stays outside:** the group reporting currency choice, **every FX rate**, the intercompany agreement
and its pricing methodology, and the inventory holdings needed to compute unrealized intercompany profit.

**Mosofin is read-only** — which here is a feature. **It cannot force a match by adjusting one side's
books**, which is exactly what Step 5 warns against.
