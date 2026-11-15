---
name: restructuring-and-severance-asc420
description: "Supports accounting for a restructuring under ASC 420 or IAS 37: identifies the cost types and when each is recognised, builds the accrual for severance, facility exit and contract termination costs, rolls the reserve forward, challenges it against what has actually been paid, and proposes the journal entries and disclosures. Works by cost type and headcount, not by name, wherever the accounting allows. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded plan details. Use when the user asks about a restructuring provision, severance accrual, exit or disposal costs, a restructuring reserve roll-forward, or ASC 420. Do not use for routine accruals (use accruals-and-deferrals) or for payroll entries (use payroll-journal-entry-builder). Read-only: produces the accrual model and proposed entries, and handles no more personal data than the standard needs."
---

# Restructuring: the liability before anyone is paid

A restructuring liability is recognised **when the obligation arises**, on commitment and
communication, often months before anyone is paid. So this skill is needed before anything is in
the books. It builds the accrual by cost type, rolls the reserve forward, and proposes the
entries.

**Works with or without Mosofin.** With Mosofin connected it reads the reserve account and what
has been paid against it, which is how the reserve is challenged. Without it, you supply the plan
and the method is the same.

**The plan, the communication and the terms are all outside the books.** And the population is
people about to lose their jobs, often before it is announced. **The working paper is built by
cost type and headcount, not by name**, and names are taken only where the accounting needs them.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never takes or stores names of affected employees unless the accounting requires it**, and
  never saves them.
- **Never recognises a cost before its trigger is evidenced.** The communication date comes from
  the user.
- **Never decides whether future service is required.** That judgment sets the pattern and is the
  user's.
- **Never shares the output beyond the people the user names.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–5" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and ASC 420 or IAS 37?* | The triggers differ in wording | **Never default the period.** |
| **C** | *What is the plan: approval date, scope, expected completion?* | Defines what is in the reserve | **Ask again.** |
| **D** | *What was communicated, to whom, when, and how is it evidenced?* | The recognition trigger | **Blocking** for severance. Recognise nothing without it. |
| **E** | *What are the affected groups, by headcount and cost, and the severance terms?* | Sizes the accrual. Names only where needed | Build the model structure only. |
| **F** | *Is future service required of any group? Which contracts and leases are being exited?* | Decides the recognition pattern and the other cost types | Assume none is required, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the reserve balance and payments against it, and any reserve with no movement.
- Confirm who may see the output before producing anything.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **The approved plan** | Required | PDF |
| **Cost by group**: headcount, severance terms, dates | Required. By group, not by name | XLSX |
| **Contracts and leases being exited**, with penalties | Required for those costs | PDF or XLSX |
| **Reserve account detail** | Required for the roll-forward | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Accounting for the **2026 restructuring** at **Northbrook Trading** for **Q4** under **ASC
> 420**, approved on **3 October** and communicated on **14 October**, from **your Mosofin
> connection** and **the plan you uploaded**. **Two groups, 38 roles**, no future service
> required. Output to **you and the CFO only**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the group count,
the headcount and the totals, with no names. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Identify cost types and recognition

Each cost type and its recognition trigger: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Build the accrual and roll the reserve forward

The accrual model, the reserve roll-forward and the challenge to it:
[`references/method.md`](references/method.md) Steps 2–3b. Check
[`references/edge-cases.md`](references/edge-cases.md) for communication after the period end, an
abandoned plan, employees who resign first, and statutory notice.

## Stage 5 — Entries, disclosures, and present

The entries as **proposals**, the disclosures and controls, then the outputs:
[`references/method.md`](references/method.md) Steps 4–5 and *Outputs*. Before presenting, check
the coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether
the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the framework and the
model structure. **No names and no individual amounts are saved.**

---

## Files

| File | Read when |
|---|---|
| [`references/mosofin-protocol.md`](references/mosofin-protocol.md) | Before the first tool call |
| [`references/gates.md`](references/gates.md) | Stage 2, Mosofin path |
| [`references/method.md`](references/method.md) | Stages 3–6 |
| [`references/edge-cases.md`](references/edge-cases.md) | Stage 4, and whenever something looks unusual |
| [`references/output.md`](references/output.md) | Before presenting |
| [`references/overview.md`](references/overview.md) | Background, or when a user asks why |
