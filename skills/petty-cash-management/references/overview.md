<!-- petty-cash-management · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Petty Cash Management (Mosofin)

Reconciles **petty cash floats (imprest funds)**, processes **vouchers**, calculates **replenishments**, and
produces **GL posting inputs**. Works for any currency and any petty cash policy.

**In plain words:** a tin of cash for small purchases, topped back up to a fixed amount each time it runs
down. At any moment the cash plus the receipts should equal that fixed amount. Checking that they do is the
entire control.

This skill is **jurisdiction-agnostic**. It uses the entity's COA for accounts and the entity's stated float
policy for thresholds.

It is **workspace-scoped**: the petty cash account balance, the replenishment history and the Cash
Over/Short trend come from tool calls against a company file connected to your Mosofin workspace in this
conversation. **The physical count and the vouchers are external, and always will be.**

## Small money, real controls — and one invariant the workspace can test

**Petty cash is the smallest balance in most sets of accounts and one of the more common places money goes
missing**, precisely because the amounts look too trivial to check carefully. **The discipline matters more
than the sums.**

**The physical count is `[manual]`, absolutely.** **The ledger says what should be in the tin; only counting
says what is.** The same rule as the inventory count in `inventory-to-gl-reconciliation` and the asset count
in `fixed-asset-register-and-depreciation`.

**But three things are readable, and the first is genuinely valuable:**

> **The imprest invariant.** **Under an imprest system the GL petty cash balance never moves.** Expenses are
> recorded at replenishment, against the bank; **the float account sits at the authorised amount
> permanently.**
>
> **[auto]**: **read the petty cash account's movement.** **If it moves, the fund is not being run as an
> imprest float** — either expenses are being posted to it directly as they occur, or the float has been
> topped up or reduced without authority. **Both are findings, and both are one query.**

2. **The replenishment history.** **[auto]**: how often, how much, and by what route. **A float replenished
   weekly is undersized for its policy; one not replenished in a year is dormant** — and a dormant float
   still holds cash somebody is responsible for.
3. **The Cash Over/Short trend.** **[auto]**: **persistent small shortages in one location or under one
   custodian is a pattern**, and patterns are what matter here. **Report it as a pattern, never as an
   allegation** — see `fraud-detection-and-forensics` for the discipline.

**Mosofin is read-only.** It cannot post the replenishment or the discrepancy. Every entry below is a
*proposal*.
