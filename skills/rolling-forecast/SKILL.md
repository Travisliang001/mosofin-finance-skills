---
name: rolling-forecast
description: "Builds and refreshes a rolling forecast that always looks twelve or eighteen months ahead: locks the closed months as actuals, updates the drivers, challenges the projection with the business's own run-rate and seasonality, rebuilds the full-year view, scores the last forecast against what happened, and bridges every change since the prior version. Reads actuals through a connected Mosofin workspace when the user agrees, or works from uploaded monthly results. Use when the user asks for a rolling forecast, a re-forecast, a forecast refresh after month-end, a full-year outlook, or forecast accuracy tracking. Do not use for a weekly cash forecast (use cash-flow-forecast-13-week) or for variance against the budget (use budget-vs-actual-analysis). Read-only: the forward assumptions are the user's, and the skill posts nothing."
---

# Rolling forecast: actuals locked, the horizon moved on

Keeps a forecast that always looks a fixed distance ahead. Each period it **locks the closed
months as actuals**, takes the updated drivers, projects forward, and shows **what changed and
why** since the last version. It also scores the previous forecast against what happened.

**Works with or without Mosofin.** With Mosofin connected the rolling part is a live read: locking
actuals, deriving seasonality and scoring accuracy. Without it, you upload the monthly results and
the method is the same.

**The books say what happened. Only you say what will.** Pipeline, hiring, pricing and known
events are never in an accounting system, so the forward assumptions are always yours. The skill
tests them against your own run-rate and seasonality and asks questions; it does not author the
forecast. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never presents a run-rate as a forecast.** A run-rate is a challenge to the forecast, shown
  beside it.
- **Never locks a month that is not closed.** Unfinished actuals corrupt the forecast and the
  accuracy record.
- **Never supplies an FX rate or a forward-looking statement for external guidance.**

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
| **B** | *Which company, what horizon (12 or 18 months), and monthly or quarterly?* | Sets the rolling window | **Ask again.** Nothing can be projected without it. |
| **C** | *Which is the last fully closed month?* | Only closed months are locked as actuals | Test the latest month for completeness and **confirm before locking it.** |
| **D** | *What are the updated drivers: pipeline and bookings, hiring plan, price changes, known events?* | This is the forecast itself | Project nothing forward. Deliver the locked actuals and the run-rate challenge only, and say so. |
| **E** | *Do you have the prior forecast and the original budget?* | The change bridge and the accuracy score need them | Mark this a first forecast: no bridge, no accuracy score. |
| **F** | *Any foreign currency, and what rate do you assume?* | A rate is an assumption, never a fact from the books | Show the affected lines unconverted, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Read the saved profile first. The prior forecast and the accuracy record live there after the
  first run.
- With several company files, say that **reading several ledgers is not consolidating them**:
  forecast each entity separately, or take consolidated actuals from where they are prepared.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Monthly profit and loss by line**, actuals to date, ideally 24 months or more | Required | XLSX or CSV |
| **Prior forecast** | Recommended. Without it there is no change bridge | XLSX or CSV |
| **Original budget** | Recommended | XLSX or CSV |
| Drivers and assumptions (D): pipeline, headcount plan, known events | Required for any projection | XLSX, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Refreshing the **12-month** rolling forecast for **Northbrook Trading**, monthly, with actuals
> **locked through September** from **your Mosofin connection**, against **last month's forecast**
> and the **budget you uploaded**. Drivers as supplied. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the months it
covers, the line count and the totals. Flag anything unreadable, or a missing month, straight
away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Set the window and lock the actuals

Set the rolling window, then lock the closed months after testing that each close is complete:
[`references/method.md`](references/method.md) Steps 1–2.

## Stage 4 — Update the drivers, challenge them, and project

Take the updated drivers, test them against run-rate, seasonality and history, then project
forward and rebuild the full-year view: [`references/method.md`](references/method.md) Steps 3–5,
including Step 3b. Check [`references/edge-cases.md`](references/edge-cases.md) for a first
forecast, a strategy change, lumpy revenue, seasonality at the horizon edge, FX and capex.

## Stage 5 — Score accuracy, bridge the changes, and present

Score the last forecast against outturn, reconcile every change since the prior version, add a
scenario overlay if asked, then the output: [`references/method.md`](references/method.md)
Steps 6–9. Actuals and projection stay visibly distinct. Before presenting, check the coverage and
provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants the
workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. This skill depends on it more
than most: the accuracy record cannot exist without the forecast saved from the run before.

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
