<!-- budget-builder · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Budget Builder (Mosofin)

Builds an annual operating budget — revenue, cost of goods / services, operating expenses, and the
resulting operating income — by period (typically monthly), grounded in explicit **drivers** and
assumptions.

**In plain words:** a budget is next year's plan expressed in money. Done badly it is last year's
numbers with a percentage added. Done well, every line traces to something you can argue about —
how many customers, at what price, needing how many staff. This skill builds the second kind.

This skill is **industry-aware** and **method-flexible** (incremental, zero-based, or
driver-based budgeting). It produces a budget; the integrated balance sheet and cash flow
projection live in `three-statement-financial-model`.

It is **workspace-scoped**: every historical figure comes from a tool call against a company file
connected to your Mosofin workspace in this conversation, or from something you supplied by hand
and that is labelled as such.

**What the connected books contribute, and it is more than it first appears.** A budget is about
the future, so most of it is necessarily assumption. But the *base* it is built on is history, and
that history is fully readable. Three things in particular turn stated standards of this skill
into evidenced ones:

1. **Real seasonality.** Monthly actuals across several years give the entity's own seasonal
   shape. The edge case below says "don't divide annual by 12" — here you don't have to guess the
   pattern, you can measure it.
2. **The entity's actual payroll loading rate.** The quality standards insist the loading rate
   comes from the entity, **not** assumed. Historical wages against employer taxes and benefits in
   the ledger gives exactly that ratio.
3. **Any budget already in the system.** Where the accounting platform holds a budget, it is
   readable — so this skill can **extend or revise an existing budget** rather than silently
   replacing one that people already agreed.

What stays `[manual]`: the drivers themselves, the hiring plan, strategic initiatives, inflation
assumptions, and the targets the budget must hit. Those are decisions, and the skill's job is to
make them explicit, not to invent them.

**Mosofin is read-only.** It cannot write a budget back into the accounting system. The workbook
is the deliverable; loading it is a human action.
