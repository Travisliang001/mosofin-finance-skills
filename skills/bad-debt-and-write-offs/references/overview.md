<!-- bad-debt-and-write-offs · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Bad Debt and AR Write-Off (Mosofin)

Assesses **accounts receivable (A/R)** collectibility, computes the **allowance for doubtful
accounts** (or **expected credit loss** under CECL / IFRS 9), and processes specific
**write-offs**.

**In plain words:** some customers never pay. Accounting handles that in two stages. First, you
set aside an estimate for the money you probably won't collect — that estimate is the
**allowance**, and it reduces the receivable on your balance sheet without pointing at anyone in
particular. Second, when a specific customer is definitely not going to pay, you remove their
balance entirely — that is a **write-off**. This skill does both, and keeps the running record
that shows they agree.

This skill is **jurisdiction-agnostic** and **standards-agnostic** for the methodology — it
applies the framework the user specifies (CECL under US GAAP, IFRS 9 ECL, or a simpler
aged-receivable percentage method common under many local GAAPs).

It is **workspace-scoped**: every balance, aging, and account name comes from a tool call
against a company file connected to your Mosofin workspace in this conversation, or from
something you supplied by hand and that is labelled as such.

**One thing this skill does unusually well from a connected workspace, worth naming up front.**
The original insists that **loss rates come from the entity's historical data, not assumed** —
and in a Mosofin workspace that history is genuinely derivable. Prior-period agings can be
pulled as-of past dates, and the movement on the bad-debt expense and allowance accounts is
readable transaction by transaction. So the entity's *own* loss experience by aging bucket is
usually **`[auto]`**, not a number someone has to guess. That is the difference between a
supportable allowance and a plausible one.

What remains stubbornly `[manual]`: whether a specific customer is insolvent, whether a dispute
will be won, what the economy will do next year, and what the local tax rules permit.

**Mosofin is read-only.** It cannot post an allowance, write off a balance, or claim a tax
recovery. Every entry below is a *proposal* for a human to review and post.
