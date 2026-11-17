<!-- intangibles-and-amortization · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Intangibles and Amortization (Mosofin)

Maintains the **intangible asset register**, computes **amortization**, handles **capitalization of
internally developed intangibles**, and **tests for impairment**.

**In plain words:** some of what a business owns has no physical form — a customer list bought with an
acquisition, a patent, software written in-house. If it will earn money for years, its cost belongs on the
balance sheet and gets written off across those years. The two hard questions are how long it will last,
and — for things built rather than bought — which of the costs of building it count at all.

This skill is **framework-aware** — it applies **US GAAP or IFRS** rules as the user specifies.

It is **workspace-scoped**: the ledger balances, the capitalizations and disposals, the amortization charge
and the development spend come from tool calls against a company file connected to your Mosofin workspace
in this conversation, or from something you supplied by hand and that is labelled as such.

**Note it is no longer chart-of-accounts-agnostic in the original's sense** — it reads the entity's actual
chart rather than accepting any structure. That is a narrowing, stated rather than implied.

## The shape: totals without detail — with one important exception

**This mirrors `fixed-asset-register-and-depreciation`, and the same reasoning applies.** The general ledger
holds **cost, accumulated amortization and the amortization charge as totals per account**. **Asset-level
cost, in-service date, useful life, method and impairment history are not in the accounting system** — they
live in a register kept elsewhere. **So the register is `[manual]`.**

But the movements are readable, which gives the same three checks:

1. **Capitalizations derived from the ledger.** **Debits to the intangible accounts during the period are
   the additions** — so a register entry with no matching debit is a phantom, and **a debit with no register
   entry is an asset that will never be amortized.**
2. **Disposals likewise**, from credits and any gain-or-loss account movement.
3. **An implied-rate sanity check.** Amortization ÷ cost against the policy lives.

**And one check specific to intangibles that has no fixed-asset equivalent:**

> **Is anything being amortized at all?** **[auto]**: an intangible account carrying cost with **no
> accumulated amortization and no charge** is either an **indefinite-lived** intangible — in which case an
> **annual impairment test is mandatory**, and it is worth asking whether it is actually happening — or a
> finite-lived one whose amortization was never started or has quietly stopped. **Both are real findings,
> and the distinction between them is `[manual]`.**

**The exception — and it is what makes this skill different from fixed assets:**

> **The inputs to internally developed intangibles are in the ledger.** Salaries, contractor invoices, cloud
> and hosting costs, external development fees — **all of it is recorded, and in many entities it is already
> tagged by project, class or department.** So the **population of potentially capitalizable cost is
> substantially `[auto]`**, even though the stage determination that decides which of it qualifies is
> firmly `[manual]`.
>
> That turns Step 4 from a purely policy exercise into a grounded one: **here is what this project actually
> cost, by category and by month; now tell me when the application development stage began and ended.**

**What stays outside:** the register, every useful life, the capitalization policy, the stage determinations,
impairment testing, and any fair value.

**Mosofin is read-only.** It cannot capitalize, amortize, impair or derecognise anything. Every entry below
is a *proposal*.
