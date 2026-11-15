---
name: tax-planning-and-projections
description: "Projects a tax liability for the year and shows the effect of decisions before they are made: the income base from the books plus the user's forward view, the projected tax on rates the user supplies, estimated and quarterly payments, how much cash to set aside, a comparison of options, and sensitivity to the assumptions. Reads year-to-date results through a connected Mosofin workspace when the user agrees, or works from uploaded figures. Use when the user asks for a tax projection, estimated tax payments, how much to set aside for tax, or the tax effect of a decision they are considering. Do not use for the return itself (use tax-return-prep-corporate or personal-tax-return-prep) or for the provision in the accounts (use corporate-tax-provision-asc740). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# Tax projection: what the year is likely to cost

Projects the **tax for the year** before it ends: the income so far plus your view of the rest,
the tax on it, the payments due on account, and the cash to set aside. It also shows what a
decision under consideration would do to the figure.

**Works with or without Mosofin.** With Mosofin connected the year-to-date results are read from
the books. Without it, you supply them and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system, and files nothing.** Every entry and
  every figure is a proposal.
- **Produces computations and illustrations, not tax advice.** A qualified tax professional
  reviews before anything is filed or acted on.
- **Never supplies a rate, threshold, bracket or rule.** Each comes from the user, with its source
  and its year, and is never carried over from an earlier run.
- **Never recommends a course of action.** It shows each option's effect and names the difference
  between a timing benefit and a saving.
- **Never presents an arrangement with no commercial purpose as planning.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–8" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Who is the taxpayer, in which jurisdiction, and for which tax year?* | Sets every rule that applies | **Ask again.** |
| **C** | *What are the current rates, thresholds and rules, with their source and year?* | Never built in, never carried forward | **Blocking.** Assemble the figures from the books, and compute no tax. |
| **D** | *What do you expect for the rest of the year?* | The forward half is not in the books | Project the year at the run-rate to date, and **say it is a run-rate, not a forecast.** |
| **E** | *What book-to-tax adjustments do you expect, and what is the safe-harbour rule for estimates?* | Taxable income is not book income | Use book profit unadjusted, and say so. |
| **F** | *Which decisions are you considering?* | Each is modelled as an option | Produce the base projection only. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say how many months of actuals the projection rests on.
- For an owner-managed business, ask which personal circumstances are in scope.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Year-to-date profit and loss** | Required | XLSX or CSV |
| **Rates and rules** with source and year | Required | Type it in the chat, or PDF |
| Prior year return or computation | Recommended | PDF |
| Forward assumptions | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Projecting **2026 corporate tax** for **Northbrook Trading**, in **the jurisdiction you
> named**, on **nine months of actuals** from **your Mosofin connection** plus **your forecast for
> Q4**. Rates from **the source you gave, for 2026**. One option to compare: **buying equipment
> before year-end**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Project the income base

Actuals to date plus the forward view: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Compute the tax, the payments and the set-aside

The projected tax, estimated payments and set-aside planning:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for marginal against effective rates,
crossing a threshold, and safe harbours.

## Stage 5 — Compare options, test sensitivity, and present

The options, the line between planning and avoidance, sensitivity, then the output:
[`references/method.md`](references/method.md) Steps 5–8. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the taxpayer type and
the adjustments that recur. **No rate or threshold is saved.**

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
