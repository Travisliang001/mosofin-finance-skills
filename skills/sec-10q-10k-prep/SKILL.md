---
name: sec-10q-10k-prep
description: "Organises the preparation of a 10-Q or 10-K: builds the calendar from close to filing, sets up the tie-out of every number in the draft to its source, checks the comparatives against what was actually filed, runs the disclosure checklist, and lays out the drafting, review and sign-off workflow. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and prior filings. Use when the user asks to prepare a 10-Q or 10-K, plan an SEC filing calendar, tie out a filing draft, check comparatives against a prior filing, or run a disclosure checklist for an SEC filer. Do not use for the close itself (use quarter-end-close or year-end-close), the notes (use notes-to-financial-statements) or the narrative (use management-discussion-and-analysis). Read-only: produces the calendar, tie-outs and checklist, and files nothing."
---

# 10-Q and 10-K preparation: from close to filing

Builds the process around an SEC filing: the **calendar** from close to filing date, the
**tie-out** of every number in the draft, the disclosure checklist, and the review and sign-off
workflow. The filing itself is management's, with counsel and auditors.

**Works with or without Mosofin.** With Mosofin connected the figures behind the draft are read
from the books and tied to it. Without it, you upload the trial balances and the method is the
same.

**For a filer, the authoritative statements are the ones in the filed document, not the ones in
the accounting system.** So comparatives are checked against what was filed, and the draft itself,
the prior filings and filer status are documents you supply. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never files, submits or signs anything**, and never gives a legal view on a disclosure.
- **Never takes a comparative from the books without checking it against the prior filing.**
- **Never sets a deadline without the filer status.** It depends on public float, which is not in
  the books.
- **Never authors a forward-looking statement or a non-GAAP definition.**

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
| **B** | *Which company, which form, and which period?* | A 10-K is not a fourth 10-Q | **Never default the period.** |
| **C** | *What is the filer status, and what are the filing and earnings dates?* | Sets every deadline | Build the task list with no dates, and say so. |
| **D** | *Can you supply the prior filings and the current draft?* | The filed document is the authority | Tie the books to themselves only, and list the comparative check as not done. |
| **E** | *What significant events happened in the period?* | Each brings disclosures | **Ask again.** The books show traces, not the full story. |
| **F** | *Who reviews what, does XBRL apply, and which non-GAAP measures are used?* | The reviewer matrix and consistency of measures | Leave reviewers open; treat non-GAAP measures as none, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Read the saved profile: the reviewer matrix and the non-GAAP definitions persist from the last
  filing.
- Report any entry posted into a prior period since its filing.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance** for the period and comparatives | Required | XLSX or CSV |
| **Prior filings** | Required for the comparative check | PDF |
| **Current draft** | Required for the tie-out | PDF or DOCX |
| Reviewer matrix, calendar, non-GAAP definitions | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Preparing the **10-Q** for **Northbrook Holdings** for **Q3**, an **accelerated filer**, filing
> on **7 November**, from **your Mosofin connection** and **the draft and prior filings you
> uploaded**. Events: **one debt refinancing**. XBRL applies. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the form, the
period and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Build the calendar

The close-to-file calendar: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Tie out, check comparatives, and run the checklist

Tie-out discipline, comparatives against what was filed, then the disclosure checklist:
[`references/method.md`](references/method.md) Steps 2–3, including Step 2b. Check
[`references/edge-cases.md`](references/edge-cases.md) for a change in filer status, a first
filing after an IPO, a late auditor adjustment and a subsequent event.

## Stage 5 — Drafting workflow, sign-offs, and present

The drafting workflow, the controls and sign-offs, then the outputs:
[`references/method.md`](references/method.md) Steps 4–5 and *Outputs*. Before presenting, check
the coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether
the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the calendar template,
the reviewer matrix and the non-GAAP definitions.

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
