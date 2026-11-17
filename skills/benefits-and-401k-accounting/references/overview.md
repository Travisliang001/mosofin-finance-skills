<!-- benefits-and-401k-accounting · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Benefits and Retirement Plan Accounting (Mosofin)

Accounts for employee benefits — **defined contribution** and **defined benefit** retirement
plans, health and insurance benefits, **paid time off (PTO) / compensated absences**, and other
employee benefits. Recognizes the cost and liability correctly under the applicable framework.

**In plain words:** pay is not the only thing you owe employees. You may be putting money into
their retirement plan, paying for their health cover, and letting them build up holiday they
haven't taken yet. Each of those is a cost you have already incurred, and often a debt you
already owe, even though no money has moved. This skill works out how much, records it, and keeps
the running total honest.

This skill is **framework-aware** (US GAAP / IFRS — notably **ASC 715 / IAS 19** for retirement
and other post-employment benefits) and **flags where an actuary is required** (defined benefit
plans). Defined contribution and PTO accruals are handled directly; defined benefit and
post-retirement plans are structured here but **require actuarial valuation**.

It is **workspace-scoped**: every posted cost, liability balance and remittance comes from a tool
call against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

**Where the connected books help, and where they do not.**

- **`[auto]` and genuinely useful**: the benefit *costs already posted*, the *liability balances*
  carried for each benefit, the *movement* on those liabilities, and — most valuably —
  **whether withheld contributions were actually remitted, and how long they sat unremitted**.
  That last one is a compliance check with a regulatory deadline attached, and it is directly
  measurable from the books.
- **`[manual]`**: plan terms, contribution formulas, match rates, vesting schedules, PTO balances
  and pay rates, eligibility, and the entire actuarial valuation. Unless a **payroll platform is
  a connected datasource** — check at Gate 1, because it changes several verdicts at once.

**A rule this skill and Mosofin share exactly.** The original insists: *do not fabricate
actuarial figures*. Mosofin's grounding rule says the same thing more broadly — every figure
comes from a tool result in this conversation or from labelled user-supplied evidence. For
defined benefit and OPEB numbers there is no tool, so there is only the actuary's report. **A
plausible pension obligation is worse than a missing one**, because it looks like an answer.

**Mosofin is read-only.** It cannot post an accrual, remit a contribution, or amend a plan. Every
entry below is a *proposal* for a human.
