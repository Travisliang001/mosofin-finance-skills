---
name: kpi-dashboard-builder
description: "Builds a KPI dashboard for a business: picks the metrics that fit the industry and the audience, defines each one precisely, computes it with its trend, adds targets and alerts, and lists every metric it declined because the data lives in another system. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded financial statements and operational exports. Use when the user asks for a KPI dashboard, a financial or metrics dashboard, a board KPI page, an executive scorecard, or help deciding which key metrics to track. Do not use for a variance report against budget (use budget-vs-actual-analysis), for the statement set itself (use financial-statement-builder) or for a multi-entity cash forecast dashboard (use multi-entity-forecast-dashboard). Read-only: produces a dashboard, its definitions and a coverage sheet, and posts nothing."
---

# KPI dashboard: a few figures that mean the same thing every month

Chooses, defines, computes and lays out the **key performance indicators** for a business. It
picks metrics that fit the industry and the audience, writes a precise definition for each,
computes it with its trend, and adds targets and alerts. A person decides what to act on.

**Works with or without Mosofin.** With Mosofin connected it reads two to three years of monthly
statements in one go. Without it, you upload the statements and the method is the same.

**The books supply the financial metrics, and little else.** Margins, cash, runway, DSO and the
ratios are arithmetic over the statements. Churn, ARR, utilisation and conversion live in billing,
CRM, time or production systems. The skill computes what it can read and **names the system each
missing metric needs**, in a Not Available tab. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never approximates an operational metric from the ledger.** Recognised revenue is not ARR, a
  revenue decline is not churn, and an invoice count is not a customer count. A metric with no
  source is left blank and listed.
- **Never invents a target, a benchmark or a metric definition.**

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
| **B** | *Who is the dashboard for? Board, executives, a department or investors* | Decides the depth and the number of metrics | **Ask again.** Nothing can be designed without it. |
| **C** | *What industry and business model? SaaS, retail, services, manufacturing or another* | The right metrics differ by model | Build the general financial set only, and say so. |
| **D** | *Which period, and how often will it be refreshed?* | Sets every read and the trend length | **Never default the period.** |
| **E** | *Which operational systems do you run, connected or not? Billing, CRM, time tracking, production* | Decides whether industry metrics are possible at all | Assume none. The dashboard is financial only, and the Not Available tab says what is missing. |
| **F** | *Do you have targets, and how are your current KPIs defined?* | A target gives a metric its status; an existing definition shows where drift began | Show no targets, and **say that none were supplied.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Take the industry and the fiscal calendar from the company profile, and confirm them.
- With several company files, ask whether the dashboard is **per entity or consolidated**. The two
  answer different questions and are never mixed in one view.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Monthly profit and loss**, 24–36 months | Required | XLSX or CSV |
| **Balance sheet at each month end**, same months | Required | XLSX or CSV |
| Receivables and payables ageing | Recommended, for DSO and DPO | XLSX or CSV |
| Operational exports: billing, CRM, time or production | Optional. Without them the industry metrics are listed as not available | CSV |
| Audience (B), business model (C), targets and current definitions (F) | Required for B, recommended for the rest | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Building a **board** dashboard for **Northbrook Trading**, a **services** business, on **36
> months to September**, refreshed **monthly**, from **your Mosofin connection**. No billing or
> time system is connected, so the metrics will be **financial only**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the months it
covers, the row count and the totals. Flag anything unreadable, or a gap in the monthly series,
straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the history and choose the metrics

Pull the full monthly history in one batch, then select the KPIs for this industry and audience:
[`references/method.md`](references/method.md) Steps 0–1. Fewer, decision-useful metrics beat a
long list. Record every metric considered and declined.

## Stage 4 — Define, compute and set targets

Write each definition down to the accounts and the period convention, compute the metric, then add
the targets the user supplied: [`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for short history, seasonal businesses,
real-time requests, multi-entity groups and mixed currencies.

## Stage 5 — Lay out, add trends and alerts, and present

Layout, trends and supporting detail, alerts and commentary, then the output:
[`references/method.md`](references/method.md) Steps 5–8. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants an Excel file or an
HTML dashboard before creating either, and stamp the as-at date and the entity on its face.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the metric set, the definitions and
the query recipes. **Persist the recipe, never the number.**

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
