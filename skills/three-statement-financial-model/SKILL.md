---
name: three-statement-financial-model
description: "Builds an integrated three-statement financial model: the income statement, the supporting schedules for working capital, fixed assets, debt and equity, the cash flow statement that links them, and a balance sheet that must balance in every period, with circularity resolved, checks built in and scenarios on top. Measures each driver from the business's own history before any assumption is set. Reads history through a connected Mosofin workspace when the user agrees, or works from uploaded financial statements. Use when the user asks to build a three-statement model, an integrated financial model, a linked income statement, balance sheet and cash flow projection, or a model for fundraising or planning. Do not use for an operating budget alone (use budget-builder), for a re-forecast (use rolling-forecast) or for testing assumptions on an existing model (use scenario-and-sensitivity-analysis). Read-only: produces the model and a coverage sheet, and posts nothing."
---

# Three-statement model: three statements, linked, and it must balance

Builds a model where the **income statement, balance sheet and cash flow statement** are linked
by formulas, so a change in any driver flows through all three. The cash flow statement is the
link, and the balance sheet must balance in every period. The assumptions are yours.

**Works with or without Mosofin.** With Mosofin connected the historical columns are read from
the books, and each driver is **measured** from history before you set it: days of receivables,
margins, capex against depreciation. Without it, you upload the statements and the method is the
same.

**In a model, balancing is a real test.** An accounting system balances by construction. A
spreadsheet does not: every link is a formula somebody wrote. So a balance check that is not zero
is a genuine error to find, and it is never closed with a plug. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never inserts a hardcoded plug** to make the balance sheet balance.
- **Never sets an assumption for the user**: not a growth rate, a capex plan, a borrowing, an FX
  rate or a tax rate. It shows the history and asks.
- **Never mixes history and forecast without marking which is which.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–9" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What is the model for: fundraising, diligence or internal planning? Which company?* | Sets how rigorous it must be | **Ask again.** |
| **C** | *What horizon, and monthly, quarterly or annual?* | Sets the model's shape | **Never default it.** |
| **D** | *What are the operating drivers: revenue build, margins, operating costs?* | The forecast is yours | Show the measured history of each driver and ask again. |
| **E** | *What is planned for capex, borrowing and repayment, and equity?* | None of it is in the books; debt terms are in the loan agreements | Hold capex at depreciation and debt at its current schedule, and **say that you assumed it.** |
| **F** | *Tax by a single effective rate or in detail? How should interest circularity be handled?* | Both change the build | Ask for the rate. Break circularity with prior-period balances, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say how many periods of history will be loaded as the model's historical columns.
- With several company files, say that a consolidated model needs consolidated history.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Income statements and balance sheets**, two to three years, by period | Required | XLSX or CSV |
| **Fixed asset and debt schedules** | Recommended. Without them those schedules start from balances only | XLSX |
| Drivers (D), capex, debt and equity plans (E), tax approach (F) | Required for the forecast | XLSX, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Building a **three-year monthly** model for **Northbrook Trading**, for **internal planning**,
> with **24 months of history** from **your Mosofin connection**. Drivers as you supplied; capex
> per **your plan**; the term loan on its **agreed schedule**; tax at the **effective rate you
> gave**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods it
covers and the totals. Flag anything unreadable, or a balance sheet that does not balance,
straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Architect the model and build the income statement

Lay out the model, then build the income statement:
[`references/method.md`](references/method.md) Steps 1–2.

## Stage 4 — Schedules, measured drivers, cash flow and balance sheet

The supporting schedules, the drivers measured from history, the cash flow statement, then the
balance sheet: [`references/method.md`](references/method.md) Steps 3–5, including Step 3b. Check
[`references/edge-cases.md`](references/edge-cases.md) for interest circularity, negative cash
before the revolver, deferred taxes, leases and seasonal working capital.

## Stage 5 — Resolve circularity, add checks, and present

Circularity, outputs and checks, scenarios, then the output:
[`references/method.md`](references/method.md) Steps 6–9. The balance check is zero in every
period before anything is shown. Before presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the model as an Excel
file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the model structure
and the driver definitions.

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
