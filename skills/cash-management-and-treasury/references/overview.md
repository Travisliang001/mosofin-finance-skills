<!-- cash-management-and-treasury · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Cash Management and Treasury (Mosofin)

Designs and operates corporate **treasury** — bank account structures, **cash pooling** and
concentration, short-term investing of surplus cash, payments and disbursement controls, FX
management, and liquidity policy. Focuses on **how cash is held, moved, and managed**, distinct from
forecasting and statutory cash flow reporting.

**In plain words:** most businesses accumulate bank accounts the way lofts accumulate boxes — one
per entity, one per currency, one opened for a project that ended years ago. Treasury is the
discipline of deciding how many accounts you actually need, how much cash to keep in each, what to
do with the surplus, who is allowed to move it, and how to stop someone tricking you into sending it
to the wrong place.

This skill is **structure-and-policy-oriented** (not a single transactional process) and integrates
with `cash-flow-forecast-13-week` (for the operational forecast) and `debt-and-covenant-tracking`
(for facility management).

It is **workspace-scoped**: every account balance and movement comes from a tool call against a
company file connected to your Mosofin workspace in this conversation, or from something you
supplied by hand and that is labelled as such.

**What a connected workspace does and does not give you here.** This is a *design* skill, so much of
it is judgment. But **Step 1 — the cash landscape map, which the original rightly calls "the
foundation" — is substantially `[auto]`**, and that is the step people most often get wrong by
working from memory:

- **Every cash account and its balance**, across every connected entity
- **Dormant and low-activity accounts** — directly detectable, since an account with no movement for
  months is visible in the ledger. The original notes that "most entities have more accounts than
  they realize"; here you can prove it rather than suspect it
- **Actual inflow and outflow volumes and their predictability**, by account
- **Several treasury KPIs**, including days of cash on hand and the bank-fee trend

**And what it cannot see at all — which is most of the control layer:**

- **Which bank holds each account.** The chart of accounts has an account name, not a banking
  relationship
- **Signatories, online access permissions, and approval limits** — the core of Step 5
- **Whether a payment was approved, by whom, or under dual control**
- **Facility terms, covenants, undrawn availability**
- **Trapped cash** — a regulatory or contractual restriction is not a ledger field

So expect a strong evidenced map and a policy built on `[manual]` inputs. **Never present the
control section as tested**; Mosofin can describe the controls that should exist, and can sometimes
detect that one is absent, but it cannot confirm one operated.

**Mosofin is read-only.** It cannot open or close an account, move cash, execute an investment, or
change a permission. Everything below is a *proposal* for a human.
