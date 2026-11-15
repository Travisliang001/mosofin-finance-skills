---
name: model-builder-integrated-three-statement
description: "Builds a working, formula-driven financial model from historicals plus the user's assumptions: reads the historical income statement and balance sheet, maps accounts to model lines, shows what each driver has actually been, builds driver-based forecast schedules, links the three statements, and adds checks. Never generates the assumptions. Reads historicals through a connected Mosofin workspace when the user agrees, or works from uploaded statements. Use when the user asks to build a working financial model quickly from their actuals, map historicals into a model, or set up drivers and checks. Do not use when the full build of debt, tax and circularity is the point (use three-statement-financial-model), for an operating budget (use budget-builder) or for testing assumptions (use scenario-and-sensitivity-analysis). Read-only: produces the working model and a coverage sheet, and posts nothing."
---

# Model builder: from your actuals to a working model

Takes what the business has actually done, works out the handful of **rates and ratios** that
describe how it operates, lets you say how they change, and carries the result through all three
statements. The output is a **live, formula-driven model** protected by checks, not a static
export.

**Works with or without Mosofin.** With Mosofin connected the historical statements are read,
mapped to model lines, and each driver's history is measured. Without it, you upload the
statements and the method is the same.

**The foundation is read. The forecast is yours.** Growth, margin, working capital, capex, debt,
tax and headcount assumptions are never generated. Each is shown beside its own history, and you
set it. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never fills in an assumption.** A missing one stays blank and is listed.
- **Never delivers a static export in place of a working model**, unless the user asks for one.
- **Never builds on historicals that do not tie.** An unmapped account or a balance sheet that
  does not roll forward is fixed first.
- **Never uses an open period as the opening balance sheet without saying so.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and what is the model for: fundraising, the board, a lender or internal use?* | Sets the standard of evidence | **Ask again.** |
| **C** | *What horizon, and monthly, quarterly or annual?* | Sets the model's shape | **Never default it.** |
| **D** | *What are your assumptions for growth, margin, working capital, capex, debt, tax and headcount?* | Never generated | Build the historical side and the driver history only, with the forecast blank. |
| **E** | *Must the historicals match published or audited statements?* | The model's history should agree with them | Use the books as they stand, and say so. |
| **F** | *Do you have the debt, lease, equity and fixed asset schedules?* | Balances are in the books; schedules are not | Forecast those lines from balances only, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Confirm the mapping of accounts to model lines. This is where judgment enters.
- Confirm the opening date against the last closed period.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Historical income statements and balance sheets**, by period | Required | XLSX or CSV |
| **Chart of accounts**, or an account-to-line mapping | Required | XLSX |
| **Assumptions** | Required for the forecast | XLSX, or type it in the chat |
| Debt, lease, equity and fixed asset schedules | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Building a **three-year monthly** working model for **Northbrook Trading**, for **the board**,
> on **24 months of historicals** from **your Mosofin connection**, opening at **30 September**,
> the last closed month. Assumptions as you supplied; no audited statements to match. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the periods it
covers and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the historicals and set the architecture

Pull the historicals, then set the model architecture:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Map historicals and build the forecast schedules

Normalise and map the historicals, then build the driver-based schedules:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for historicals that do not tie, an
unmapped account, annual history for a monthly model, and a driver with no history.

## Stage 5 — Link, check, deliver, and present

Link the three statements, add the checks, then deliver the working model:
[`references/method.md`](references/method.md) Steps 4–6. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the working model as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the account mapping and the driver
definitions.

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
