---
name: budget-builder
description: "Builds an annual operating budget by month: revenue, cost of sales, operating expenses and operating income, each line traced to a driver and a written assumption, with seasonality taken from the business's own history and a reconciliation to the targets. Works incrementally, zero-based or driver-based, by area. Reads history through a connected Mosofin workspace when the user agrees, or works from uploaded prior-year results. Use when the user asks to build or draft a budget, an annual plan or an operating plan, budget headcount or departmental spend, or document budget assumptions. Do not use for comparing actuals with a budget (use budget-vs-actual-analysis), for a re-forecast during the year (use rolling-forecast) or for a balance sheet and cash projection (use three-statement-financial-model). Read-only: produces the budget, its assumptions and a coverage sheet, and loads nothing into any system."
---

# Budget: next year's plan, line by line

A budget is next year's plan expressed in money. Done badly it is last year plus a percentage.
Done well, **every line traces to something you can argue about**: how many customers, at what
price, needing how many staff. This skill builds the second kind, by month, with the assumptions
written down.

**Works with or without Mosofin.** With Mosofin connected the base is read: two to three years of
monthly results, the seasonality in them, and the recurring spend that is contractually sticky.
Without it, you upload the history and the method is the same.

**History is in the books. The plan is not.** Revenue drivers, the hiring plan, pay, new
initiatives and the targets are yours. The skill shows what each driver did, then asks what
changes. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It does not load a budget into
  the accounting system.
- **Never assumes a growth, inflation or pay rate.** With none given, the line stays flat and the
  output says so.
- **Never presents a line without its driver and its assumption.**
- **Where a budget already exists, extends it.** It does not replace it unseen.

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
| **B** | *Which company, which fiscal year, and monthly or quarterly?* | Sets the budget period | **Never default it.** |
| **C** | *Which method for each area: incremental, zero-based or driver-based? Does a budget already exist?* | It is often a mix, and extending beats replacing | Use incremental on history, and **say that you assumed it.** |
| **D** | *What are the revenue drivers for next year: units, price, customers, churn, pipeline?* | The plan is not in the books | Show the history of each driver and ask again. No revenue budget without them. |
| **E** | *What is the headcount plan: current roles, planned hires, timing and pay?* | Usually the largest cost | Hold payroll at the current run-rate, and say so. |
| **F** | *What are the targets, the known commitments, and any escalation assumptions?* | Needed to reconcile the budget to the goal | Leave lines flat and skip the reconciliation to targets, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Check whether a budget is already loaded in the system.
- Say how many months of history the seasonality rests on.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Monthly profit and loss by line**, 24–36 months | Required for incremental and driver-based methods | XLSX or CSV |
| **Existing budget**, if there is one | Recommended | XLSX |
| Revenue drivers (D), headcount plan (E) | Required | XLSX, or type it in the chat |
| Targets, commitments, escalation (F) | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Building the **2027** monthly budget for **Northbrook Trading**, from **36 months of history**
> in **your Mosofin connection**. **Driver-based** revenue, **incremental** overheads, headcount
> from **the plan you uploaded**. Target: **12% operating margin**. No budget exists yet. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the months it
covers, the line count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the history and settle the method

Pull the monthly history in one batch, then apply the budgeting method chosen for each area:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Build revenue, cost of sales and operating expenses

The revenue budget, the cost of goods or services, then operating expenses:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for little history, fast growth, a
seasonal business, lumpy project revenue, a new launch and a cost-reduction mandate.

## Stage 5 — Assemble, document, reconcile, and present

Assemble the operating budget, write down every assumption, add a flex view, reconcile to the
targets, then the output: [`references/method.md`](references/method.md) Steps 5–9. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the method by area, the driver
definitions and the line owners.

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
