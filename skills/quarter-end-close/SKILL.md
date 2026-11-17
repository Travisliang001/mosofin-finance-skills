---
name: quarter-end-close
description: "Runs the quarter-end close on top of the monthly close: the quarter-specific tasks such as the tax provision, estimates review, subsequent events, going-concern facts and covenant tests, the reports and filings in scope, coordination with an interim reviewer, the year-to-date roll-forward, and a check that nothing was posted into a closed quarter. Marks which tasks the books can evidence and which need a person. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and schedules. Use when the user asks to run or plan a quarter-end close, prepare quarterly reporting, a board pack or a lender certificate, or check a closed quarter for late postings. Do not use for the monthly close (use month-end-close-checklist) or for computing loan covenants in depth (use debt-and-covenant-tracking). Read-only: produces the checklist, the schedules and a coverage sheet, and posts nothing."
---

# Quarter-end close: the monthly close, plus the quarter's own work

A quarter-end is two things stacked together. First a **monthly close**: cut-offs,
reconciliations, accruals. Then the **quarterly increment**: tax provision, estimates, subsequent
events, going concern, covenants, segment disclosure. This skill plans and tracks both, and says
who does each task.

**Works with or without Mosofin.** With Mosofin connected the monthly layer is mostly read from
the books, and so are the year-to-date roll-forward and any entry posted into a closed quarter.
Without it, you upload the trial balances and the method is the same.

**The increment is a different kind of work.** Most of it is judgment and outside documents: a
covenant definition is in the loan agreement, a subsequent event may never reach the ledger, a
going-concern view belongs to management. Those tasks stay on the list with an owner.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Entries are proposals.
- **Never drops a task it cannot perform.** It stays, marked for a person.
- **Never computes a covenant on book figures as if they were the agreement's definitions.**
- **Never authors a forward-looking statement or a going-concern conclusion.** It presents the
  facts; management assesses and signs.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–7" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and which quarter, on what fiscal calendar?* | A quarter is not always three calendar months | **Never default it.** Confirm against the fiscal year-end on record. |
| **C** | *Which reports are due this quarter: a filing, a board pack, a lender certificate, a management report?* | Each needs different work | **Ask again.** With none named, run the close tasks only. |
| **D** | *What do the covenants say, in the agreement's own definitions?* | Book figures are not covenant figures | Give the book components only, labelled as inputs. |
| **E** | *Is an auditor performing an interim review, and what is materiality for the quarter?* | Decides whether the reviewer steps apply | Skip the reviewer steps and say so. **Never supply materiality.** |
| **F** | *Are segments tracked in the books, and did anything unusual happen in the quarter?* | Segment work and one-off events need to be known up front | Read the dimensions in use, and ask again about events. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Check that all three months of the quarter are closed before starting the increment.
- Read the saved profile: the list of obligations and definitions persists from the last quarter.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance at the quarter end**, and at the prior quarter end and prior year end | Required | XLSX or CSV |
| **General ledger detail** for the quarter | Required for the late-posting and cut-off tests | XLSX or CSV |
| Covenant definitions (D), reporting obligations (C) | Recommended | PDF, or type it in the chat |
| Schedules held outside the books: leases, equity awards, tax | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Running the **Q3** close for **Northbrook Trading**, **July to September**, from **your Mosofin
> connection**. Due this quarter: the **board pack** and the **lender certificate**, with covenant
> definitions as you supplied. No interim review. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
account count and the totals. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Run the monthly close for the last month

The standard monthly close comes first: [`references/method.md`](references/method.md) Step 1,
which follows `month-end-close-checklist`.

## Stage 4 — Add the quarter's own tasks and reports

The quarter-specific tasks, the filings and reports in scope, and reviewer coordination:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for a mid-quarter event, a change in
estimate, the first or last quarter of the year, an acquisition and foreign currency.

## Stage 5 — Roll forward, validate, and present

The year-to-date roll-forward, the cumulative validation including entries posted into a closed
quarter, then the output: [`references/method.md`](references/method.md) Steps 5–7. Before
presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the obligations in
scope, the covenant definitions and the task owners.

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
