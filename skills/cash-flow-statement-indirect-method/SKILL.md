---
name: cash-flow-statement-indirect-method
description: "Builds the statement of cash flows by the indirect method: net income reconciled to operating cash, then investing and financing, the effect of exchange rates, the supplemental disclosures, and a tie-out to the change in cash that must be exact. Reads capex, disposals, debt and equity movements from the general ledger, so they are read and not solved for. Follows US GAAP (ASC 230) or IFRS (IAS 7), with the direct method on request. Reads the books through a connected Mosofin workspace when the user agrees, or works from two uploaded balance sheets, an income statement and ledger detail. Use when the user asks to build a cash flow statement or statement of cash flows, reconcile net income to operating cash, explain why profit and cash differ, or find why the cash flow does not tie to the balance sheet. Do not use for a forward-looking cash forecast (use cash-flow-forecast-13-week) or for the full statement set (use financial-statement-builder). Read-only: produces the statement, its tie-out and a coverage sheet, and posts nothing."
---

# Cash flow statement: from profit to the change in cash

Explains why **profit and cash differ** for a period. It starts at net income, removes everything
that never involved money, adds what moved in and out through **operating, investing and
financing** activities, and ends at the change in cash. A person reviews and issues the statement.

**Works with or without Mosofin.** With Mosofin connected it reads both balance sheets, the income
statement and the general ledger behind the asset, debt and equity accounts. Without it, you upload
them and the method is the same.

**The ledger does what two balance sheets cannot.** A balance sheet change does not separate capex
from disposals from depreciation; the ledger movements do. So those figures are read, not solved
for. Where the accounting system has its own cash flow report, it is a cross-check and never a
substitute. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never inserts a plug.** The statement ends at exactly the change in cash. A difference that
  cannot be explained is reported as unexplained, with its amount.
- **Never infers the reporting framework from the country.** US GAAP or IFRS is the user's answer.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–10" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and which period? Give the period end and the comparative date.* | The statement bridges exactly these two dates | **Never default the period.** |
| **C** | *US GAAP or IFRS?* | Decides where interest, dividends, restricted cash, overdrafts and leases go | **Ask again.** Nothing can be classified without it. |
| **D** | *Which accounts count as cash and cash equivalents, and is any of it restricted?* | Sets the figure the whole statement must tie to | Propose the bank and cash accounts by name and **wait for a yes.** |
| **E** | *Was a business bought or sold in the period?* | It distorts every working-capital change and must be stripped out | Assume none, and **say that you assumed it.** |
| **F** | *Under IFRS: where do you classify interest and dividends? Indirect method, or direct as well?* | IFRS allows a choice, and it must be applied the same way every period | Required under IFRS. The method defaults to indirect. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Take the currency and the year-end from the company profile.
- With several company files, say that a group statement is **not the sum of entity statements**:
  transfers between entities must be eliminated first.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Balance sheet at the period end** | Required | XLSX, CSV or PDF |
| **Balance sheet at the comparative date**, at the same level of detail | Required. If the detail differs, the changes will not map | XLSX, CSV or PDF |
| **Income statement** for the period | Required | XLSX, CSV or PDF |
| **Ledger detail** for fixed assets, accumulated depreciation, intangibles, debt and equity | **Required for accuracy.** Without it capex, disposals and depreciation cannot be separated, and the output says so | XLSX or CSV |
| Framework (C), cash definition (D), acquisitions and disposals (E) | Required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Building the cash flow statement for **Northbrook Trading** for the **year to 30 September**,
> against **30 September last year**, under **US GAAP**, indirect method, from **your Mosofin
> connection**. Cash is the **three bank accounts** you confirmed, none restricted. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the date it is
drawn at, the line count and the totals. Flag anything unreadable, or two balance sheets at
different levels of detail, straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the evidence and fix the target

Pull both balance sheets, the income statement and the ledger extracts in one batch, then compute
the change in cash the statement must explain:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Build the three sections

Operating activities from net income, then investing, financing and the effect of exchange rates:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for non-cash transactions, leases,
restricted cash, overdrafts, acquisitions and transfers between the entity's own accounts.

## Stage 5 — Tie out and present the result

Assemble the statement and tie it to the change in cash, add the supplemental disclosures, the
direct method if asked, then the output: [`references/method.md`](references/method.md) Steps 6–9.
**Iterate until it ties exactly.** Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the framework, the classification
policy, the cash definition and the account mappings.

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
