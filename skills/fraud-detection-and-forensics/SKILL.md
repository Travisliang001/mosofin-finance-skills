---
name: fraud-detection-and-forensics
description: "Screens accounting records for fraud indicators and structures an investigation: a fraud risk assessment, analytical red-flag tests across the whole transaction population, a framework for following up flagged items, loss measurement, and a report with control fixes. Reports patterns with counts and amounts and never concludes that a person committed fraud. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded ledgers and vendor and employee lists. Use when the user asks for a fraud risk assessment, red-flag or anomaly testing, a check for ghost vendors or duplicate payments, a Benford's Law test, forensic accounting support, or help structuring an investigation. Do not use for duplicate payments alone (use duplicate-invoice-detection) or for routine journal entry review (use journal-entry-review). Read-only: produces indicators, a workplan and a coverage sheet, accuses no one, and changes no record."
---

# Fraud detection: patterns, not people

Looks through accounting records for patterns that sometimes indicate theft or manipulation:
payments that look duplicated, suppliers that look invented, numbers that look shaped. It assesses
where the business is exposed, runs the analytical tests, and structures the follow-up. **It finds
patterns. It does not find people.**

**Works with or without Mosofin.** With Mosofin connected the tests run across the whole
transaction population, with the vendor and employee lists beside it. Without it, you upload the
records and the method is the same.

**Three limits apply on every run.** A flag is a question, not an answer, however easy the test
was to run. The output names real people who have done nothing wrong until shown otherwise. And a
read through Mosofin is analysis, **not preserved evidence**: it has no chain of custody. A real
investigation is led by qualified forensic professionals and legal counsel. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system**, and never suggests that anyone
  change a record while a concern is open.
- **Never concludes that a person committed fraud**, and never infers motive from the data.
  Patterns are reported with counts and amounts; people conclude.
- **Never lets a test that could not run read as a clean result.**
- **Never saves findings, flagged items or names** for a later run.
- **Where a specific allegation exists, stops and escalates before analysing.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–9" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What is this: a risk assessment, a screen for red flags, or support for an investigation?* | Decides everything that follows | **Ask again, before any data is read.** |
| **C** | *Is there a specific allegation, and is legal counsel engaged?* | An investigation is led by counsel and forensic professionals, and may be privileged | With an allegation and no counsel, **stop and say who should lead.** |
| **D** | *Who may see the output, and who approves access to the data?* | The output names people, and an approval prompt can tip someone off | **Ask again.** Nothing is produced without a named recipient. |
| **E** | *Which company, which period, and which area of concern if any?* | Focuses the tests | Never default the period. With no area named, run the full test set. |
| **F** | *What are the approval limits and the relevant policies?* | The just-under-the-limit test needs the limit | List that test as not run. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say what is out of reach: **bank and payroll detail** are not in the accounting system.
- For investigation support, say that records must be preserved by qualified people before or
  alongside any querying.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **General ledger detail** or the journal entry listing for the period, with user and date posted | Required | XLSX or CSV |
| **Payments and bills** for the period | Required for the vendor tests | XLSX or CSV |
| **Vendor list** and **employee list**, with addresses and bank details where held | Required for the ghost-vendor and conflict tests | XLSX or CSV |
| Approval limits and policies (F) | Recommended | PDF, or type it in the chat |
| Bank statements, payroll register | Optional. Without them those tests are listed as not run | PDF or CSV |

**Read back before starting, then wait for a yes:**

> *Running a **red-flag screen**, with no specific allegation, on **Northbrook Trading** for the
> **year to September**, from **your Mosofin connection**. Approval limit **5,000**. The output
> goes to **you and the audit committee chair only**. Bank and payroll detail are out of scope.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
row count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Settle the engagement, then read the evidence

Confirm the engagement type and its boundaries **first**, then pull the population in one batch:
[`references/method.md`](references/method.md) Step 1, then Step 0. The order is deliberate.

## Stage 4 — Assess the risk and run the tests

Apply the risk framework, assess where the business is exposed, then run the analytical tests:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for tipping off, privilege, false positives,
the limits of Benford's Law, management override and small entities.

## Stage 5 — Structure the follow-up, measure, and present

The follow-up framework for flagged items, loss measurement, the report and control fixes, then
the output: [`references/method.md`](references/method.md) Steps 5–8. A loss is never measured
from indicators alone. Before presenting, check it against
[`references/output.md`](references/output.md), and send it only to the recipients named in
Stage 1. Ask whether the user wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the method only. **Never the
findings, the flagged items or any name.**

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
| [`references/tools-and-glossary.md`](references/tools-and-glossary.md) | When you need a tool name or a term |
