---
name: year-end-close
description: "Runs the year-end close on top of the monthly and quarterly close: checks that all twelve months are closed, works through the annual procedures such as counts, impairment, tax true-up, estimates and disclosures, lists the statutory filings in scope, supports the audit, closes the year and opens the new one, then verifies that the books stayed locked and the new year opened clean. Marks which tasks the books can evidence and which need a person. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded trial balances and schedules. Use when the user asks to run or plan a year-end close, prepare for annual accounts, check retained earnings rolled forward correctly, or confirm nothing was posted into a closed year. Do not use for the monthly close (use month-end-close-checklist), the quarter (use quarter-end-close) or the auditor's request list (use audit-prep-pbc-list). Read-only: produces the checklist, the schedules and a coverage sheet, and posts nothing."
---

# Year-end close: the most rigorous close of the year

Year-end is also a month-end and a quarter-end, so this skill sits on top of both. It adds the
**annual procedures**: counts, impairment, the tax true-up, year-end estimates, disclosures and
filings. Then it closes the year, opens the new one, and **checks that both steps held**.

**Works with or without Mosofin.** With Mosofin connected it can verify that all twelve months
are closed, that nothing was posted into the year after it was locked, and that the new year
opened with the right balances. Without it, you upload the trial balances and the method is the
same.

**Most of the annual layer is outside the books.** A physical count, a valuation for the goodwill
test, an actuary's report, the cap table and the auditor's findings are documents and judgments.
Those tasks stay on the list with an owner and a date. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It locks nothing and posts no
  closing entry; every entry is a proposal.
- **Never drops a task it cannot perform.** It stays, marked for a person.
- **Never treats a locked year as an unchanged year.** It checks.
- **Never authors a going-concern conclusion or a forward-looking statement**, and never supplies
  materiality.

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
| **B** | *Which company, which fiscal year-end, and which framework: US GAAP, IFRS or local GAAP?* | Sets the period and the procedures | **Never default the year-end**, and never infer the framework from the country. |
| **C** | *Is there an audit, a review, a compilation or none? Which firm, and what timeline?* | Decides whether the audit steps apply, and sets the calendar backwards | Skip the audit steps, and say so. |
| **D** | *Which statutory filings are in scope?* | The filing list drives a whole step | List the common filings as questions for the user. |
| **E** | *What major events happened this year: an acquisition, a disposal, new equity or debt, a restructuring?* | Each brings its own year-end work | **Ask again.** The books show traces, not the full story. |
| **F** | *What did last year's auditor raise, and what is year-end materiality?* | Last year's findings come back | Carry nothing forward, and say so. **Never supply materiality.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Report which of the twelve months are closed before anything else.
- Read the saved profile: the filing list and last year's carry-forward items live there.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Trial balance at the year end** and at the prior year end | Required | XLSX or CSV |
| **General ledger detail** for the year, and for the new year to date | Required for the lock and opening-balance tests | XLSX or CSV |
| **Fixed asset register, count results, lease and equity schedules** | Recommended | XLSX |
| Filing list (D), events (E), prior-year findings (F) | Recommended | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Running the year-end close for **Northbrook Trading** at **31 December**, under **US GAAP**,
> from **your Mosofin connection**. A **full audit**, fieldwork from **9 February**. Events this
> year: **one debt facility drawn**. Filings as you listed. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
account count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Run the monthly and quarterly close, and check all twelve months

The standard closes first, then the check that every month of the year is closed:
[`references/method.md`](references/method.md) Steps 1–1b.

## Stage 4 — Annual procedures, filings and the audit

The year-end procedures, the statutory and regulatory filings, and audit support:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for an acquisition, a change of fiscal
year, going-concern doubt, a restatement, the subsequent events window and a new accounting
standard.

## Stage 5 — Close the year, verify, reflect, and present

Close the year and open the new one, verify the books stayed locked and the new year opened
clean, the lessons for next year, then the output:
[`references/method.md`](references/method.md) Steps 5–7, including Steps 5b and 5c. Before
presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the filing list, the
task owners and the items to carry into next year.

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
