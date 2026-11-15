---
name: ap-invoice-processing-and-3way-match
description: "Designs and runs the accounts payable invoice workflow end to end: intake and hygiene, vendor and compliance checks, field validation, two-way or three-way match within the tolerance the user sets, exception handling, proposed coding and posting, and the audit trail, with the approval matrix applied. Says plainly whether a two-way or a three-way match was possible. Reads bills and purchase orders through a connected Mosofin workspace when the user agrees, or works from uploaded invoices and orders. Use when the user asks to set up or review the AP invoice process, define approval routing and coding standards, process a batch of supplier invoices through all checks, or write an AP procedure. Do not use for the match alone (use three-way-match), for extracting fields (use invoice-data-extractor) or for duplicates alone (use duplicate-invoice-detection). Read-only: proposes coding and exceptions, and posts and pays nothing."
---

# AP invoice processing: from intake to ready-to-pay

Before paying a supplier, three things should agree: what was **ordered**, what was **received**,
and what is being **billed**. That check sits inside a longer process: intake, vendor checks,
validation, coding, approval and an audit trail. This skill designs and runs the **whole
process**. For the match on its own, use `three-way-match`.

**Works with or without Mosofin.** With Mosofin connected it reads bills, purchase orders, vendors
and the chart of accounts. Without it, you upload the invoices and orders and the method is the
same.

**Receiving records and the approval matrix are usually outside the books.** Without receipts the
match is two-way, and the output says so. Who may approve what, and the tolerance, come from you.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never posts, approves, pays or holds an invoice, in any system.** Every step is a proposal.
- **Never invents a tolerance or an approval limit.**
- **Never presents a two-way match as a three-way match.**
- **Never treats an attachment as an approval**, or a change to bank details as routine.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and are these bills already entered, or invoices not yet in the books?* | Decides what can be read | **Ask again.** Never default the period. |
| **C** | *Where are receipts logged?* | Without them the match is two-way | Run a two-way match, and say so in the summary. |
| **D** | *What tolerance applies, as a percentage and an amount?* | Decides what is an exception | **Expect an exact match and flag every variance.** |
| **E** | *Who may approve what, up to which amount?* | The books do not record it | List approval checks as not run. |
| **F** | *Is this a design of the process, a run of a batch, or both?* | A written procedure and a batch run are different outputs | Run the batch, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether purchase orders carry line detail, and whether bills link to them.
- Report any change to vendor bank details in the period for verification, not as a finding of
  fraud.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Invoices** for the period | Required | PDF, XLSX or CSV |
| **Purchase orders** with lines | Required for matching | XLSX or CSV |
| **Receiving records** | Required for a three-way match | XLSX or CSV |
| Approval matrix and tolerances | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Processing **September's supplier invoices** for **Northbrook Trading**, already entered as
> bills, from **your Mosofin connection**, with **receipts you uploaded**. Tolerance **2% and
> 25**; approval matrix as supplied. This will be a **three-way match**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the document count,
the period and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the bills and run intake checks

Pull bills, orders and vendors, then intake and hygiene, and vendor and compliance checks:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Validate, match and handle exceptions

Field validation, the match, then exceptions: [`references/method.md`](references/method.md) Steps
3–5. Check [`references/edge-cases.md`](references/edge-cases.md) for a bill with no order link, a
bank detail change mid-process and a duplicate.

## Stage 5 — Proposed posting, audit trail, and present

Coding and posting as **proposals**, the audit trail, then the outputs:
[`references/method.md`](references/method.md) Steps 6–7 and *Outputs*. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the tolerances, the approval matrix
and the coding standards.

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
