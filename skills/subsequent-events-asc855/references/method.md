<!-- subsequent-events-asc855 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Define the subsequent events window
- Step 2 — Gather evidence
- Step 2b — What the sweep actually looks for *(Mosofin addition)*
- Step 3 — Classify events
- Step 4 — Determine accounting treatment
- Step 5 — Document conclusions
- Outputs
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is evidence for a human conclusion.** The gateway is read-only. **Mosofin classifies nothing as Type 1 or Type 2 and posts no adjustment.**

---

## Inputs

All five preserved.

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Balance sheet date** | Date | **Required** | Fiscal calendar; confirm | `[auto]` to read, `[manual]` to confirm |
| **Issuance / availability date** | **Date + definition used** | **Required** | **Not in the books** — a process fact | `[manual]` |
| **Post-period activity** | Board minutes, legal updates, major transactions | **Required** | **Transactions: live read, full population. Minutes and legal updates: not on this surface.** | Split |
| Significant estimates | Reserves, impairments, contingencies | Recommended | **Balances readable** — and they are what the sweep tests against | `[auto]` |
| **Management updates** | Known events and developments | **Required** | **Not in the books. This is the Type 2 half.** | `[manual]` |

---

## Workflow

### Step 1 — Define the subsequent events window

`[manual]` for the end date; `[auto]` to apply.

- **Window start**: the balance sheet date.
- **Window end**: **the issuance date, or the available-to-be-issued date.**

**The two definitions give different windows, and the choice is not arbitrary.** Broadly, entities that file with a regulator evaluate through the date the statements are **issued**; others evaluate through the date they are **available to be issued** — the point at which they are complete in a form approved for issuance. **The Inputs table asks for the date *and the definition used*, and both belong in the disclosure.** Confirm which applies rather than assuming.

**`[auto]` once the window is set** — and this is where the practical gain lives. The sweep is a date-bounded query, so:

- **Run it at the start of the review.**
- **Run it again immediately before issuance**, because the window has been extending the whole time.
- Where the issuance date slips, **run it again.** It costs one query.

**The final run is the one that matters** and, in manual practice, is the one that never happens.

---

### Step 2 — Gather evidence

**All five procedures preserved — and the split is the sharpest inventory result in this skill: two are literally ledger reads.**

| Procedure | Verdict | What it becomes |
|---|---|---|
| **Read board minutes** | `[manual]` | Not on this surface — **and it is where Type 2 events surface first**, because a board hears about a fire or a lawsuit before accounting does |
| **Review significant post-period transactions** | **`[auto]`** | **Full population, not "significant"** — see below |
| **Obtain legal letter updates** | `[manual]` | Correspondence with lawyers |
| **Review cash receipts and disbursements for major items** | **`[auto]`** | **Every receipt and payment, not "major items"** |
| **Ask management for known events** | `[manual]` | **The Type 2 half. Ask by category** — see the checklist below |

#### The two automatic procedures stop being samples

Both of the `[auto]` procedures are described in the original with a **threshold** — *"significant"* transactions, *"major"* items. That threshold exists because a person cannot read every post-period transaction.

**A query can.** So:

- **Every** post-period transaction is examined, not the large ones
- **Every** receipt and payment, matched back to the balance sheet date position
- Across the **whole window**, re-runnable as it extends

**This matters more than it might seem**, because the classic Type 1 evidence is frequently *not* a large transaction. A modest receipt against a fully-provided receivable is strong evidence the provision was wrong; it will never appear on a list of major items. Similarly a small credit note against a pre-year-end invoice, which may indicate the revenue was not earned.

**Threshold-based review is biased towards large events, and Type 1 evidence is not necessarily large.**

#### The management enquiry should be a checklist, not a question

`[manual]`, and it is the half the ledger cannot do — so it deserves doing properly.

**"Has anything happened since year end?" reliably produces "no."** Ask by category:

- **Litigation** — claims filed, served, settled, threatened
- **Customers** — insolvencies, losses, major disputes
- **Financing** — facilities agreed, withdrawn, breached, refinanced
- **Ownership** — share issues, buy-backs, changes of control
- **Assets** — fires, floods, thefts, condemnations, impairments identified
- **Transactions** — acquisitions or disposals agreed
- **Regulatory** — investigations, actions, licence changes
- **People** — resignations of directors or key management
- **Commitments** — significant contracts signed, guarantees given
- **Dividends** — declared after the period end

**Each of these is a Type 2 candidate and none of them is reliably in a ledger.** The checklist is the Mosofin addition; the requirement to ask is the original's.

---

### Step 2b — What the sweep actually looks for *(Mosofin addition)*

`[auto]`. **The filter that turns a transaction extract into evidence.**

The sweep works by **comparing the post-period activity against the balance sheet date position.** These are the patterns worth surfacing, and each is a recognised (Type 1) *candidate* — the classification remains Step 3's.

| Pattern | Why it is Type 1 evidence |
|---|---|
| **A customer with a balance at the period end enters insolvency afterwards** | **The classic case.** The customer's financial condition existed at the balance sheet date; the insolvency revealed it. Adjust the allowance. |
| **A pre-period receivable is written off after the period end** | Same. The uncollectibility generally existed at the date. |
| **A pre-period receivable is paid after the period end, having been provided against** | **Evidence the provision was too high** — the mirror case, and one nobody looks for because it is good news. |
| **A credit note or refund issued after the period end against a pre-period invoice** | The revenue may not have been earned, or the goods were faulty at the date. See `revenue-recognition-asc606`. |
| **Inventory sold after the period end below its carrying cost** | **Net realisable value evidence** at the balance sheet date. See `inventory-obsolescence-and-reserve`. |
| **A pre-period liability settled at a different amount** | Evidence of the correct amount of an obligation that existed. |
| **A litigation or claim settlement paid after the period end** | Evidence of the amount of a liability existing at the date, where the claim predates it. |
| **A customer with a material period-end balance and no activity at all since** | A collectibility indicator — weaker, but free. |
| **A large reversal after the period end of an entry made before it** | Worth explaining either way. |

**And the complementary read**: for each **significant estimate** identified at Gate 3 — allowances, reserves, contingencies — **look for post-period transactions that bear on it.** That is a direct, targeted test of exactly the estimates the review exists to challenge, and it is more focused than sweeping the whole ledger and hoping something stands out.

**Every row produced is a candidate with evidence attached, not a conclusion.**

---

### Step 3 — Classify events

**`[manual]`, and this is the crux of the whole standard.**

- **Recognised** (ASC 855 spells this **"recognized subsequent events"**) — the event **provides evidence of conditions existing at the balance sheet date.**
- **Non-recognised** (ASC 855: **"nonrecognized subsequent events"**) — the conditions **arose after the balance sheet date**, but disclosure may still be required.

**Why no amount of data settles this.**

The distinction turns on **when the condition existed** — not when the transaction occurred, not when it was posted, and not when anyone found out. **The transaction is identical in both cases.**

A customer failing in February: if their financial difficulties existed at 31 December, the receivable was impaired then and the event is **recognised**. If the business was sound at 31 December and failed because of a fire in January, the condition **arose after** and the event is **non-recognised**.

**Same customer, same balance, same insolvency, same date — and opposite accounting treatments**, decided by facts about the customer's condition that are not in your ledger and are frequently not in theirs either.

This is structurally identical to the error-versus-estimate distinction in `restatement-and-prior-period-adjustment`: **the amounts are the same either way, and the answer is a question about the world.** In both cases the honest move is to present the evidence, state the question, and let a person answer it with the basis documented.

**`[auto]` supplies one genuinely useful input**: how soon after the period end the event occurred. **A customer failing on 3 January is very unlikely to have been sound on 31 December.** Proximity is evidence — not proof, and it must be labelled as evidence — but it is the kind of thing that materially assists the judgment and is trivially computed.

---

### Step 4 — Determine accounting treatment

`[auto]` to compute; **`[manual]` to decide.** Both preserved.

**For recognised events:**

> **Adjust the financial statements and document.**

`[auto]` for the quantification — the adjustment to an allowance, a write-down to net realisable value, the correction of a settled liability are all arithmetic once the classification is made. `[auto]` to draft the entry; hand off to `journal-entry-builder`. **`[manual]` to post.**

**For non-recognised events:**

> **Disclose if material.**

`[manual]` — the materiality judgment and the disclosure language. **`[auto]` for one input**: where the event has a quantifiable effect, quantify it, since materiality is assessed against something and the something is usually readable.

**A note on what "adjust" means and does not.** A recognised event adjusts the financial statements **for a condition that already existed** — it is **not** a correction of an error, and it is **not** a change in estimate arising from new circumstances. All three adjust the accounts and all three are different things with different disclosure consequences. See `restatement-and-prior-period-adjustment` for the error case; **conflating them is a common and consequential mistake.**

---

### Step 5 — Document conclusions

`[auto]` to populate; `[manual]` to conclude. **Maintain a subsequent events log**, with all five fields preserved:

| Field | Verdict |
|---|---|
| **Event description** | `[auto]` for ledger-derived events; `[manual]` otherwise |
| **Date** | **`[auto]` — and record both the event date and, where relevant, the posting date**, per the near-substitute note |
| **Category (recognised / non-recognised)** | **`[manual]`** — left blank by Mosofin |
| **Accounting impact** | `[auto]` to quantify; `[manual]` to decide |
| **Disclosure required** | `[manual]` |

**Two Mosofin additions to the log, and both matter:**

**A Source column** — `ledger sweep`, `management enquiry`, `board minutes`, `legal update`. **Without it, a log looks uniformly evidenced**, and it is not: the ledger-derived rows are exhaustive over transactions while the rest depend on somebody having mentioned something.

**A completeness statement at the head of the log**, in plain terms: *the transactional sweep covered the full population of post-period transactions from [date] to [date]; non-transactional events are covered only by the enquiries recorded below.* That sentence is what stops the log being read as a complete review.

---

## Outputs

All four of the original's outputs preserved, plus two Mosofin additions. Delivered as an `.xlsx` workpaper.

**Sheet 1: Subsequent Events Log**
The five fields, **plus Source and the completeness statement.** Category column left blank for the preparer and reviewer.

**Sheet 2: Recommended Adjusting Entries** (if applicable)
For recognised events. Marked **PROPOSED — NOT POSTED.**

**Sheet 3: Draft Disclosure Language**
For non-recognised material events. Marked **DRAFT.** `[manual]`.

**Sheet 4: Sign-Off Checklist**
`[manual]` — every procedure in Step 2, with who performed it and when, **including the two automatic ones, which still need an owner.** Plus the date the final sweep was run.

**Sheet 5: Ledger Sweep Detail** *(Mosofin addition)*
| Pattern | Counterparty | Period-end position | Post-period transaction | Date | Days after period end | Amount | Candidate type |
|---|---|---|---|---|---|---|---|

Every candidate from Step 2b, with its evidence and its proximity to the period end. **"Candidate type" is a suggestion for the preparer, visibly distinct from Sheet 1's Category column.**

**Sheet 6: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Subsequent_Events_[YYYY-MM-DD]_[EntityName].xlsx`

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and **at the head of the log** — a clean fixture log is indistinguishable from a clean real one.

---

## Output Quality Standards

*(A Mosofin addition — the original has no Output Quality Standards section.)*

- **The window is defined with both its dates and the definition used** — issued, or available to be issued.
- **The sweep is re-run immediately before issuance**, and the sign-off records the date of the final run.
- **All five evidence procedures appear**, including the three Mosofin cannot perform, each with a named owner.
- **The management enquiry is made by category**, not as an open question.
- **Every log entry carries its source** — ledger sweep, enquiry, minutes, legal.
- **The completeness limitation is stated on the log itself**: the sweep is exhaustive over transactions and silent on everything else.
- **Event date and posting date are recorded separately.**
- **Proximity to the period end is shown** for every candidate, and labelled as evidence rather than proof.
- **The classification column is left for the preparer.** Mosofin proposes candidates and classifies nothing.
- **Favourable candidates are surfaced as diligently as adverse ones.**
- **Recognised, error, and change-in-estimate are kept distinct.**
- **Adjusting entries are proposed, never posted.**
- **A nil result is documented as a performed procedure with a stated scope.**
- **File naming consistent.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh.

**What is worth persisting into the workspace-scoped skill:**

1. **The sweep patterns and the accounts they run against**, tuned to this client's chart — so subsequent runs are one call rather than a rebuild.
2. **The significant estimates list**, since the targeted read against them is the highest-yield part of the sweep.
3. **The management enquiry checklist**, tailored to this business — a manufacturer's categories differ from a lender's.
4. **The issuance-date definition** that applies to this entity.
5. **Prior-period events and their classifications**, with reasoning — because the same kind of event will recur and should be treated consistently.
6. **Customers and counterparties previously flagged**, so a recurring slow payer is not re-raised as a fresh insolvency indicator every year.
7. **Who performs each of the three manual procedures.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — this log names failing customers and disputed counterparties.

**The evolved version runs the sweep as a standing query** — cheap enough to run monthly, so that the annual review is a confirmation rather than an investigation, and so the final pre-issuance run is routine.

---

## Anti-patterns

- **Calling a completed ledger sweep a completed review.** It covers Type 1; Type 2 comes from people.
- **Running the sweep once.** The window extends until issuance; re-run before it.
- **Confusing posting date with event date.** One locates the event; the other says when the business found out.
- **Listing every post-period transaction.** That is an extract, not a log.
- **Applying a "significant items" threshold** to an automated sweep. Type 1 evidence is often small.
- **Classifying events.** The distinction turns on when a condition existed; present the evidence.
- **Treating proximity as proof.** A failure on 3 January is usually evidence, and sometimes a January fire.
- **Sweeping only for adverse evidence.** A provided receivable that gets paid is equally a recognised event.
- **Conflating a recognised event with an error or a change in estimate.** Three different things, three different disclosures.
- **Adjusting for a non-recognised event.** It discloses; it does not adjust.
- **Asking "has anything happened?"** Ask by category.
- **Leaving a blank log.** A nil result is a conclusion with a stated scope.
- **Presenting a fixture-derived nil result.** It is indistinguishable from a real one.
- **Saying "posted" or "classified".** The gateway reads.
