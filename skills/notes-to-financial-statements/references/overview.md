<!-- notes-to-financial-statements · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Notes to Financial Statements (Mosofin)

Drafts and reviews the **notes (footnotes)** accompanying financial statements. Covers **accounting
policies, account-level detail disclosures, commitments, contingencies, related parties, and subsequent
events**. Works from a **disclosure checklist** tailored to the entity's framework and activities.

**In plain words:** the statements give the numbers; the notes explain what they mean, how they were arrived
at, and what else a reader needs to know before relying on them. Most of a set of accounts, by page count,
is notes.

This skill is **framework-aware** (US GAAP / IFRS / local GAAP). **Disclosure requirements are extensive and
framework-specific; this skill builds the structure and drafts content from the entity's data, flagging
where management judgment or legal review is needed.**

It is **workspace-scoped**: the roll-forwards, breakdowns, comparatives, tie-outs and concentration measures
come from tool calls against a company file connected to your Mosofin workspace in this conversation, or
from something you supplied by hand and that is labelled as such.

## What the workspace drafts, and what it must never draft

**The account-detail notes are substantially computable.** Roll-forwards, component breakdowns, maturity
tables where a schedule exists, comparatives, disaggregations — **these are the bulk of the note pages, and
most of them are queries.**

**Three contributions worth naming:**

1. **The tie-out is native.** Step 3 requires that **"note totals must tie to the BS/IS face"**, and Step 8
   repeats it. **That is the workspace's core competence** — the note figures and the statement figures come
   from the same reads, and **any difference is a real one rather than a transcription error.**
2. **Subsequent events have a readable candidate population.** **[auto]**: **transactions posted after the
   reporting date** — a debt issuance, an acquisition, a large disposal, a significant write-off. **Step 6
   is the note most likely to miss something material**, because it depends on someone remembering what
   happened after year-end. **A list of everything material that hit the books since is a better starting
   point than memory.**
3. **Concentration disclosures are measurable.** **[auto]**: **revenue by customer, purchases by supplier,
   revenue by geography or segment** — the concentration edge case asks for exactly these, and they are
   arithmetic.

**And the boundary, which the original states in its final quality standard and which this skill must hold
absolutely:**

> **No invented policy, contingency outcome, or legal opinion.**
>
> **Policies are not in the data.** Step 2 says *"Pull the actual policy from the entity's data — do not
> assume"* — **and the data records results, not policies.** The ledger shows that depreciation was charged;
> **it does not say the entity's policy is straight-line over five years.** Some policies can be *inferred*
> from the pattern and **every inference must be confirmed**, not asserted. **The same rule as
> a GAAP to IFRS conversion**: a balance is not a policy.
>
> **Contingencies and legal positions are further still.** **Litigation wording has legal consequences**,
> and the original is right that **legal counsel must review it.** **Draft from management's input; never
> characterise an outcome, never estimate a loss that has not been estimated for you, and never opine.**

**Mosofin is read-only**, and this skill writes nothing back. **The notes are part of the entity's published
accounts, and they are the entity's.**
