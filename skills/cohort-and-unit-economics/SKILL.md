---
name: cohort-and-unit-economics
description: "Analyses customers by acquisition cohort and computes unit economics: the retention table and curves, customer lifetime, CAC, LTV on margin, payback, LTV to CAC, and a view by segment. Derives each customer's start date from the first invoice and reads revenue per customer per month, and states plainly that channel and per-customer cost-to-serve are not in the books. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded customer revenue and spend data. Use when the user asks for cohort analysis, retention or churn by cohort, CAC, LTV, payback period, LTV to CAC, unit economics, or whether the business model works per customer. Do not use for a general KPI dashboard (use kpi-dashboard-builder) or for ageing receivables (use ar-aging-and-collections). Read-only: produces the cohort tables, the metrics with their definitions and a coverage sheet, and posts nothing."
---

# Cohorts and unit economics: is each customer worth winning?

Groups customers by **when they first bought**, then follows each group over time. It builds the
retention table, computes **CAC, LTV, payback and LTV to CAC**, and shows whether the business
works at the level of one customer. A person decides what to change.

**Works with or without Mosofin.** With Mosofin connected the cohort table is a read: the start
date is each customer's first invoice, and revenue per customer per month is in the books.
Without it, you upload customer-level revenue and the method is the same.

**Two things are never in the books.** The acquisition **channel**, so CAC by channel needs your
marketing data and only blended CAC can be read. And **cost-to-serve per customer**, so LTV starts
from company-level margin and says so. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never computes LTV on revenue.** LTV is on margin, with the margin basis stated.
- **Never guesses the business model, the acquisition definition, the sales and marketing accounts
  or a discount rate.** Each is the user's answer.
- **Never presents blended CAC as the whole picture.** It says that channel detail is missing.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–11" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What is the business model? Subscription, transactional, marketplace or a mix* | It changes what retention means | **Ask again.** Never infer it from the industry. |
| **C** | *Which period, and monthly or quarterly cohorts?* | Sets the window and the cohort size | **Never default the window.** Monthly is standard once it is given. |
| **D** | *When does a customer count as acquired, and when as lost?* | "Active" is not a field in the books | Propose first invoice as the start, and **wait for a yes.** |
| **E** | *Which accounts make up sales and marketing spend: fully loaded or paid only?* | It changes CAC materially | Build retention only. List CAC, payback and LTV to CAC as not run. |
| **F** | *Do you have channel data, cost-to-serve by customer, or a discount rate?* | None of these is in the books | Report blended CAC and company-level margin, undiscounted, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say how far back the customer history reaches. The earliest cohort available limits the window.
- With several company files, ask whether customers are shared across them.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Revenue by customer by month**, or the invoice list with customer, date and amount | Required | XLSX or CSV |
| **Sales and marketing spend by month** | Required for CAC | XLSX or CSV |
| **Gross margin**, company level or by customer | Required for LTV | XLSX, CSV or typed |
| Channel or plan per customer | Optional. Without it there is no view by channel | CSV |
| Business model (B), definitions (D), account set (E) | Required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Analysing **monthly cohorts** for **Northbrook Trading**, a **subscription** business, from
> **January last year to September**, from **your Mosofin connection**. A customer starts at
> **first invoice** and is lost after **90 days with no invoice**. CAC is **fully loaded** on the
> four accounts you named. No channel data. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period it
covers, the customer count, the row count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the history and build the cohort table

Pull customer-level revenue and the spend accounts in one batch, define the cohorts, then build
the retention table: [`references/method.md`](references/method.md) Steps 0–2. Use customer-level
revenue, never the aggregate, and take credits and refunds out.

## Stage 4 — Retention curves, lifetime, CAC and LTV

Derive the curves and the customer lifetime, then CAC, then LTV on margin:
[`references/method.md`](references/method.md) Steps 3–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for young cohorts, expansion masking churn,
CAC timing, one-time revenue, one-off events and short history.

## Stage 5 — Ratios, health, segments, and present

Payback and LTV to CAC, the health assessment, the segment view, then the output:
[`references/method.md`](references/method.md) Steps 7–10. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the cohort definition, the sales
and marketing account set and the margin basis. The cohorts are rebuilt from current data every
run.

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
