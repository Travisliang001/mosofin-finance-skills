<!-- insurance-accounting-overview · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Insurance Accounting — Overview and Close Map (Mosofin)

Provides a **practical operating model for insurance accounting**, focusing on **the schedules and controls
commonly required to close and report**.

**In plain words:** insurance takes money now for a promise about later, so almost every number in the
accounts is an estimate about events that have not finished happening. Premium has to be spread across the
period it covers, claims have to be provided for before anyone knows their cost, and part of the risk has
usually been passed to somebody else. This maps how the close works and what evidence each piece needs.

**This is a close-mapping skill, not a reserving skill.** Its deliverable is **a checklist tailored to the
business model, with data sources and owners** — not computed reserves. That distinction is preserved
throughout: **reserve adequacy and IBNR are actuarial work**, and nothing here substitutes for it.

It is **workspace-scoped**: the general ledger balances, the commission revenue and the trust account
position come from tool calls against a company file connected to your Mosofin workspace in this
conversation, or from something you supplied by hand and that is labelled as such.

## The business model decides whether this skill works against the ledger at all

**The original lists "carrier vs MGA vs broker" as the first required input. In a Mosofin workspace it is
more than an input — it flips the entire capability profile.**

| | **Broker / MGA** | **Carrier** |
|---|---|---|
| **Where the books live** | **Ordinary accounting software** — which is what is connected here | **A specialised policy and claims platform**, with the GL often a summary |
| **What the revenue is** | **Commission and fee income — fully in the ledger** | Earned premium, derived from policy-level data |
| **Reserves** | Generally none of its own | **Case reserves, IBNR, LAE — actuarial** |
| **The signature control** | **Client money / fiduciary trust reconciliation — `[auto]`** | Reserve adequacy — `[manual]` |
| **Capability profile** | **Substantially `[auto]`** | **Substantially `[manual]`** |

**So settle the business model before anything else, and say what it implies.** For a broker or MGA this
skill produces a close map most of which the workspace can evidence. For a carrier it produces a close map
that is mostly a list of what must come from the policy system, the claims system and the actuary — **which
is still the right deliverable, but it is a different one**, and presenting the two as equivalent would
misrepresent both.

**One thing the workspace does exceptionally well for a broker or MGA:**

> **The fiduciary / client money reconciliation.** Brokers hold premium belonging to insureds and insurers,
> **usually under a regulatory obligation to keep it segregated and reconciled.** The trust bank balance,
> the amounts owed to insurers and refundable to clients, and the firm's own money are **all readable**,
> and **the reconciliation between them is one of the few genuinely `[auto]` regulatory controls in this
> entire pack.** A shortfall in client money is a serious regulatory matter, and it is a subtraction.

**What stays outside regardless of model:** the policy administration system, the claims system, **every
actuarial estimate**, reinsurance treaty terms, and loss development data by accident year.

**Mosofin is read-only.** It cannot post a reserve, a premium entry or a cession. Every entry below is a
*proposal*.
