<!-- petty-cash-management · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Multiple petty cash funds at one entity**: **reconcile each separately by location or custodian.**
*Mosofin note*: **each should have its own GL account**, and where several floats share one account **the
imprest invariant cannot be tested per float** — worth reporting as a structural limitation.

**Multi-currency float (rare)**: **treat each currency as a separate float; reconcile in original
currency.**

**IOUs / staff advances**: **track as Due from Employee until repaid. Do not net into the reconciliation as
if they were vouchers.** *Mosofin note*: **the Due from Employee balance is readable**, and **an ageing IOU
is money nobody chased** — the same account and the same point as in `expense-report-processor`.

**Voucher without a receipt below the policy threshold**: **allowed if policy permits with adequate
description. Otherwise flag.**

**Voucher dated after the count**: it cannot have been in the tin at the count. It belongs to the next period and does not reduce the shortage; show it separately and say so. `[manual]` to confirm the date.

**Voucher dated outside the period**: **either pertains to a prior unreplenished cycle — capture and ask —
or is post-period, so defer to the next reconciliation.**

**Theft / fraud suspected**: **flag for management — do not silently absorb as Cash Short.** **And do not
name a suspect** — see `fraud-detection-and-forensics`.

**Replacing the custodian**: **reconcile in full at handoff; have both custodians sign off.** *Mosofin
note*: **a custodian change is exactly when a long-standing difference surfaces**, and the handoff count is
the moment to establish the position cleanly.

**The GL petty cash balance moves** — *Mosofin-specific, and the headline test*. **The fund is not being run
as an imprest float.** Expenses are posting directly, or the float has been changed without authority.

**The GL balance does not equal the authorised float** — *Mosofin-specific*. Resolve before reconciling;
everything is measured against that number.

**A float with no movement for a year** — *Mosofin-specific*. **Dormant, and still holding cash somebody is
accountable for.** It still needs a count.

**Replenishment every week** — *Mosofin-specific*. **The float is undersized**, which is an operational
observation worth making while the data is open.

**A shortage in every period, always just inside tolerance** — *Mosofin-specific, and the pattern a
tolerance-based policy cannot see*. **Report the pattern and the period count; never the accusation.**

**A nil Cash Over/Short balance** — *Mosofin-specific*. **Not proof the float ties.** It may mean no
difference has ever been recorded — which, for a fund counted regularly over years, would itself be
unusual.

**A result comes back with `mock: true`** — *Mosofin-specific*. A float reconciled against a fixture balance
proves nothing about the tin.

**A stored count or difference is reused** — *Mosofin-specific*. All state, **and a shortage attached to a
named custodian must not be carried forward.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one float's tolerance to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
