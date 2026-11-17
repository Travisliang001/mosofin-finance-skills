<!-- construction-percentage-of-completion · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Construction Percentage-of-Completion Accounting (Mosofin)

Accounts for long-term construction (and similar over-time) contracts under **ASC 606 / IFRS 15** —
recognizing revenue and cost **as performance progresses**, using an appropriate input or output
**measure of progress**, tracking **WIP** and billings, and recognizing **loss contracts**.

**In plain words:** if you are building something that takes two years, you cannot wait until the end
to record any revenue — that would show two years of costs and then a sudden windfall. Instead you
recognise revenue as the work gets done. The hard part is deciding **how done you are**, and the
standard answer is: as much as the costs you have spent are of the costs you expect to spend in total.
Which means the whole system rests on an estimate of a number nobody knows yet.

The legacy "percentage-of-completion" terminology persists in practice; under ASC 606 / IFRS 15 this is
**over-time recognition with a measure of progress**. This skill applies the current standards
correctly.

It is **workspace-scoped**: costs incurred, billings and customer records come from tool calls against
a company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

## The split that defines this skill

Cost-to-cost progress has a numerator and a denominator, and a connected workspace can supply exactly
one of them.

**`[auto]` — costs incurred to date, and billings to date**, per contract, **provided the entity
actually tags them by job.** Construction businesses commonly do, using customers, classes, projects
or departments as job codes. Where they do, the numerator and the billings side of the WIP schedule
are readable directly.

**`[manual]`, always — the estimated total cost at completion.** It is a forward-looking judgment
made by the project manager, and it is not, and never will be, in the ledger. It also happens to be
the number that drives **everything**: percentage complete, cumulative revenue, gross profit, the
catch-up adjustment, and whether a contract is recognised as a loss. A small revision to it moves
every figure in the workpaper.

**So state clearly, every run: the costs are measured, the estimate is supplied, and the answer is only
as good as the estimate.**

**One check to run before anything else.** If cost transactions carry **no job tag at all** — everything
posting to a single cost-of-sales account with no customer, class or project — then **the books cannot
support contract-level accounting**, and per-contract costs are `[manual]` in their entirety. That is
a finding worth delivering on its own: it is the change that would make every subsequent period
automatic.

**Mosofin is read-only.** Every entry and provision below is a *proposal* for a human.
