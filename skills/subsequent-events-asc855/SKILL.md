---
name: subsequent-events-asc855
description: "Performs a subsequent events review under ASC 855 or IAS 10: sets the window from the balance sheet date to the issue date, sweeps the books for post-period activity that bears on period-end estimates, asks management by category for events the books cannot show, classifies each event as recognised or disclosed only, sets out the treatment, and documents the conclusions. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded post-period ledger detail. Use when the user asks for a subsequent events review, events after the balance sheet date, whether something after year-end needs adjusting or disclosing, or to refresh the review before issuing accounts. Do not use for the notes as a whole (use notes-to-financial-statements) or for contingencies in depth (use contingencies-and-litigation-asc450). Read-only: produces the event list, classifications and a coverage sheet, and concludes for no one."
---

# Subsequent events: what happened after the balance sheet date

Between the balance sheet date and the day the accounts are issued, things happen. Some **confirm
conditions that existed at the period end** and adjust the figures. Others are new and are
**disclosed only**. This skill finds the candidates, classifies them and documents the treatment.
Management concludes.

**Works with or without Mosofin.** With Mosofin connected the sweep of post-period activity can be
run again cheaply, right up to the day before issue. Without it, you upload the post-period ledger
detail and the method is the same.

**A sweep of the books is strong for adjusting events and weak for the rest.** A receivable that
goes bad shows up in the ledger. A lawsuit filed, a fire, or an acquisition agreed may not. Those
come from management, asked by category. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never treats a clean sweep as a complete review.** Events outside the books are asked for.
- **Never decides whether an event is recognised or disclosed only without the facts of when the
  condition arose.**
- **Never closes the review before the issue date.** The window runs until then.
- **Never authors the disclosure of a legal matter.**

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
| **B** | *Which company and balance sheet date?* | The start of the window | **Never default it.** |
| **C** | *When will the accounts be issued, or be available to be issued, and which definition applies?* | The end of the window | Run the sweep to today, and say the window is still open. |
| **D** | *Which period-end estimates matter most: reserves, impairments, contingencies?* | These are what the sweep tests | Test every reserve and accrual account found. |
| **E** | *Has management had any of these since the period end: litigation, financing, an acquisition or disposal, a casualty, a major customer loss?* | The books cannot show these | **Ask again, by category.** List the enquiry as not answered. |
| **F** | *Are there board minutes or legal updates since the period end?* | Evidence outside the books | List them as not reviewed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report post-period receipts, write-offs, settlements and credit notes that bear on period-end
  balances.
- Offer to run the sweep again just before the issue date.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Ledger detail from the balance sheet date to today** | Required | XLSX or CSV |
| **Period-end balances for the estimates being tested** | Required | XLSX |
| Board minutes and legal updates | Recommended | PDF |
| Management's list of known events | Required for the events the books cannot show | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Reviewing subsequent events for **Northbrook Trading** from **31 December** to an issue date of
> **20 March**, from **your Mosofin connection**. Testing the **bad debt allowance, the inventory
> reserve and one legal accrual**. Management reports **one customer insolvency** in January.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the dates it covers
and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Define the window

The window and the definition that applies: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Gather evidence and classify

The ledger sweep and management's events, then classification:
[`references/method.md`](references/method.md) Steps 2–3, including Step 2b. Check
[`references/edge-cases.md`](references/edge-cases.md) for a window that extends after the review,
reissued statements, a dividend declared after the date, and going-concern events.

## Stage 5 — Set out the treatment, document, and present

The accounting treatment and the documented conclusions, then the outputs:
[`references/method.md`](references/method.md) Steps 4–5 and *Outputs*. Before presenting, check
the coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether
the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the list of estimates
tested and the enquiry categories. Events are never carried into a later run.

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
