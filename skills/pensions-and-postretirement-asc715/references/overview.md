<!-- pensions-and-postretirement-asc715 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Pensions and Postretirement Benefits — ASC 715 / IAS 19 (Mosofin)

Supports accounting for **defined benefit pension plans and other postretirement benefits**, translating
**actuarial reports** into **journal entries, rollforwards, and disclosures**.

**In plain words:** a defined benefit plan promises people an income after they retire. Working out what
that promise is worth today requires assumptions about how long they will live, what they will be earning
when they leave, and what investment returns will be — which is why an actuary does it, not an accountant.
The accounting job is turning the actuary's answer into the books correctly.

It is **workspace-scoped**: the employer contributions, the recorded liability, the recorded expense and the
AOCI balance come from tool calls against a company file connected to your Mosofin workspace in this
conversation. **The actuarial report comes from the actuary**, and it is labelled as such.

## Everything flows from one external document

**This is the most externally-dependent skill in the pack, and that should be said plainly.**

**The actuarial valuation report supplies:** the benefit obligation, service cost, interest cost, expected
and actual return on plan assets, actuarial gains and losses, prior service cost, the effect of any
settlement or curtailment, the discount rate, and every demographic and financial assumption behind them.

> **None of it is on this surface, and none of it can be estimated here.** **`[manual]`, all of it.**
> **Never derive a service cost, an obligation, a discount rate or an actuarial gain** — these are the
> outputs of a specialist model, and an accounting system contains nothing that approximates them.

**But the workspace brackets the exercise at both ends, and that turns out to be the useful part:**

1. **Employer contributions are `[auto]`.** **The cash the employer paid into the plan is a payment out of
   the bank account** — **one line of the plan asset roll-forward that the ledger owns exactly.**
2. **The recorded position is `[auto]`.** **The pension liability or asset on the balance sheet, the pension
   expense in the P&L, and the AOCI pension component** are all readable.
3. **So the recorded-versus-actuarial check is possible** — and it is the contribution that matters:

> **Does the balance sheet carry the funded status the actuary computed? Does the expense equal the net
> periodic benefit cost? Does the AOCI movement match the remeasurement?**
>
> **Three comparisons, each with one side `[auto]`.** **Pension entries are annual, manual, complex and
> rarely revisited** — which is precisely the profile of an entry that gets posted once, slightly wrong, and
> carried forward for years. **Checking them against the report is cheap here and almost never done.**

**Mosofin is read-only.** It cannot post a pension entry or a remeasurement. Every entry below is a
*proposal*.
