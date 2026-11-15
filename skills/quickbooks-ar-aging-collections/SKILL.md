---
name: quickbooks-ar-aging-collections
description: "Produces a receivables ageing and a collections plan from a QuickBooks Online company file: pulls the ageing summary and detail before asking the user for anything, normalises the invoice table, reconciles summary to detail, asks only for what is materially missing, ranks customers into action bands, and drafts collection messages for a person to send. Reads QuickBooks through a connected Mosofin workspace when the user agrees, or works from uploaded QuickBooks ageing exports. Use when the user asks for QuickBooks receivables ageing, who owes money in QuickBooks, a collections priority list from QuickBooks, or draft reminder emails for overdue QuickBooks invoices. Do not use when the books are not in QuickBooks (use ar-aging-and-collections) or for applying payments (use cash-application). Read-only: writes nothing to QuickBooks and sends no message."
---

# QuickBooks receivables: ageing and a collections plan

Builds an **evidence-backed receivables ageing** and a **collections plan** from a QuickBooks
Online company file. It pulls every input it can before asking you for anything, reconciles the
summary to the detail, ranks who to chase, and drafts the messages. A person sends them.

**Works with or without Mosofin.** With Mosofin connected, QuickBooks is read through the gateway.
Without it, you upload the ageing summary and detail exports from QuickBooks and the method is the
same.

**This skill is specific to QuickBooks. For any other system, use `ar-aging-and-collections`.**
Dispute status and promises to pay are not accounting fields, so they come from you. The shape of
the QuickBooks reads is described in
[`references/quickbooks-mcp-readonly.md`](references/quickbooks-mcp-readonly.md), which is
orientation only: the live tool list is the authority. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes to QuickBooks**, and never sends, schedules or logs a message to a customer.
- **Never takes a tool name from a reference file.** Names come from the live tool list each run.
- **Never forces the summary to agree with the detail.** A difference is shown and named.
- **Never chases a customer before checking for unapplied payments and credits.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. Section names in italics are headings in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which QuickBooks company, and as at what date?* | Sets every read | **Never default the date.** |
| **C** | *Is the request the whole ledger, or particular customers?* | Sets the population | Run the whole ledger, and say so. |
| **D** | *Are any invoices disputed, on hold, or covered by a promise to pay?* | Not accounting fields | Treat every overdue invoice as collectable, and **say none were excluded.** |
| **E** | *What are your collection stages and tone, and who signs the messages?* | The drafts follow your practice | Use three bands by days overdue and a neutral tone, and say so. |
| **F** | *Are there customers who must not be contacted?* | Relationships the books cannot show | Draft for everyone in the action bands, and list the question as open. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Re-derive whether the ageing is on a cash or accrual basis from the report itself; do not assert
  it.
- Pull the ageing summary and detail together, then ask only for what is materially missing.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **A/R Aging Summary** export from QuickBooks | Required | XLSX or CSV |
| **A/R Aging Detail** export, same date | Required | XLSX or CSV |
| Customer contact list | Recommended, for the drafts | XLSX or CSV |
| Disputes, holds and promises to pay | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Ageing receivables for **Northbrook Trading** in **QuickBooks Online** at **30 September**,
> through **your Mosofin connection**, whole ledger. **Two invoices in dispute**, as you listed.
> Drafts signed by **the credit controller**; no customers excluded. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the report, its
date, the customer count and the total. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Resolve the request and pull the reports

What is being asked, the automatic input plan, then the two core reports:
[`references/method.md`](references/method.md), *Resolve the request* to *Pull and reconcile*,
parts 1–2.

## Stage 4 — Normalise, reconcile, and ask only for what is missing

The invoice table, the summary-to-detail reconciliation, then the material gaps:
[`references/method.md`](references/method.md), *Pull and reconcile* parts 3–4 and *Request only
material missing inputs*.

## Stage 5 — Prioritise, draft, and present

The two checks before anyone is chased, the action bands, the draft correspondence and the
deliverables: [`references/method.md`](references/method.md), *Analyze and prioritize* to
*Completion checks*. Before presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the collection stages,
the tone and the customers not to be contacted. Balances are read again every run.

---

## Files

| File | Read when |
|---|---|
| [`references/mosofin-protocol.md`](references/mosofin-protocol.md) | Before the first tool call |
| [`references/gates.md`](references/gates.md) | Stage 2, Mosofin path |
| [`references/method.md`](references/method.md) | Stages 3–6 |
| [`references/output.md`](references/output.md) | Before presenting |
| [`references/overview.md`](references/overview.md) | Background, or when a user asks why |
