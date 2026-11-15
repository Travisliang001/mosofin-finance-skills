<!-- lease-accounting-asc842-ifrs16 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Lease Accounting — ASC 842 / IFRS 16 (Mosofin)

Accounts for leases under **ASC 842** (US GAAP) or **IFRS 16** — classifying leases, measuring the
**right-of-use (ROU) asset** and **lease liability**, building **amortization schedules**, recording
entries, handling **modifications and reassessments**, and producing **disclosures**.

**In plain words:** renting something for years is, economically, buying the use of it on credit. Both
standards now say so: the right to use the asset goes on the balance sheet, and so does the obligation to
pay. The work is turning a contract full of options and escalations into two numbers and a schedule.

This skill is **framework-aware**. **The two standards differ importantly: IFRS 16 has a single
on-balance-sheet lessee model; ASC 842 keeps an operating vs. finance distinction affecting expense
pattern. Apply the entity's framework.**

It is **workspace-scoped**: the recorded balances, the lease expense, the cash paid and the completeness
evidence come from tool calls against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## The shape — and the one query that earns this skill its place

**This mirrors `fixed-asset-register-and-depreciation` and `intangibles-and-amortization`**: the ledger
holds **ROU asset and lease liability balances, the expense, and the cash paid** — as totals. **The lease
register is not in the accounting system.** Terms, options, escalations, discount rates and classification
inputs all live in contracts and a schedule kept elsewhere. **So the register is `[manual]`, and so is every
rate.**

The same two-directional reconciliation applies. **But this skill has something the other two do not:**

> **Unrecognised leases are findable.** **Under both ASC 842 and IFRS 16, nearly every lease goes on the
> balance sheet.** So:
>
> **Rent or lease expense with no corresponding right-of-use asset means leases that were never
> recognised.** **[auto]**, one comparison — and in practice a very common finding, particularly in smaller
> entities that adopted the standard for their largest property lease and stopped.
>
> And going further: **recurring, equal payments to the same vendor over an extended period are the
> signature of a lease.** **[auto]** — read the payment history by vendor and look for the pattern. **This
> is discovery, not just checking**: it finds the copier contract, the vehicle hire, the equipment rental
> and the second office that nobody put on the schedule.

Three more things the workspace does here:

- **The schedule must tie to the ledger.** Opening and closing ROU and liability balances, and the period's
  interest, amortization and lease expense, are all readable — **so the schedule has independent anchors at
  both ends.**
- **The operating-lease plug is verifiable.** ASC 842 operating leases should produce **level total
  expense**. **[auto]**: read the actual lease expense by month. **If it is not level, the plug mechanic has
  gone wrong** — the exact mechanical error the edge cases name.
- **Cash paid for leases is `[auto]`**, which is both a required disclosure and the input to the
  completeness test.

**What stays outside:** every contract, every discount rate, the "reasonably certain" judgments, the
classification inputs, and the register itself.

**Mosofin is read-only.** It cannot recognise a lease, post a schedule or remeasure anything. Every entry
below is a *proposal*.
