---
name: business-valuation
description: "Estimates the value of a business or an equity interest using the standard approaches: defines the purpose, standard of value and valuation date, runs a discounted cash flow on the user's forecast, trading comparables and precedent transactions on the user's market data, triangulates to an enterprise value range, bridges to equity value, and shows the sensitivities and a report structure. Reads the company's historical figures through a connected Mosofin workspace when the user agrees, or works from uploaded statements. Use when the user asks what a business is worth, for a valuation range, a DCF with comparables, or an enterprise-to-equity bridge. Do not use for a full analyst package with visible WACC and a football field (use valuation-agent-dcf-comps-football-field) or for an impairment test (use goodwill-and-impairment-testing). Read-only: produces valuation analysis for a qualified professional, not an opinion of value, and supplies no market data."
---

# Business valuation: a range, and what drives it

Estimates what a business is worth using the three standard approaches: **discounted cash flow,
trading comparables and precedent transactions**. It brings them together into a range, bridges
from enterprise value to equity value, and shows what moves the answer.

**Works with or without Mosofin.** With Mosofin connected the company's own history, capital
structure and net debt are read as at the valuation date. Without it, you upload the statements
and the method is the same.

**The books hold the company. They do not hold the market.** The forecast, the discount rate
inputs, the comparables and the share count come from you. **The result is analysis, not an
opinion of value**: for tax, litigation or financial reporting, a qualified valuer must sign.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Produces valuation analysis, not an opinion of value.** It is not a licensed valuation
  professional, and a qualified one signs before anyone relies on the figure.
- **Never supplies market data.** Discount rate inputs, multiples, comparables and prices come
  from the user, each with its source and date.
- **Never generates the forecast.** The cash flows are the user's.
- **Never gives a single number without its range and its basis.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–12" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which business, for what purpose, and on which standard of value?* | Purpose decides the standard and who must sign | **Ask again.** |
| **C** | *What is the valuation date?* | Every figure is read as at this date | **Never default it.** |
| **D** | *Do you have a forecast and normalised earnings?* | Needed for the cash flow and the multiples | Use reported earnings, run no cash flow approach, and say so. |
| **E** | *What are the discount rate inputs and the comparable companies or transactions, with sources?* | Never supplied here | **Blocking** for that approach. |
| **F** | *What are the diluted share count and the dilutive instruments?* | Needed for value per share | Stop at equity value in total. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Read debt, cash and debt-like items as at the valuation date, and confirm the net debt
  definition.
- Say when the purpose requires a qualified valuer.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Historical financial statements**, three years | Required | XLSX or PDF |
| **Forecast** | Required for the cash flow approach | XLSX |
| **Market data**: rate inputs, comparables, transactions, with sources | Required for each approach | XLSX |
| Cap table | Required for per-share value | XLSX |

**Read back before starting, then wait for a yes:**

> *Valuing **100% of Northbrook Trading** at **31 December**, for **management planning**, on
> **fair market value**, from **your Mosofin connection**, **your forecast** and **the comparables
> you uploaded**. Three approaches; no per-share value. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods, the
sources and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the history and define the engagement

Pull the company's figures, then purpose, standard of value and date, and the approaches:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Run the approaches

The discounted cash flow, trading comparables and precedent transactions:
[`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for early-stage businesses, no comparables,
synergies and stacked premiums and discounts.

## Stage 5 — Triangulate, bridge, test, and present

The enterprise value range, the bridge to equity, adjustments, sensitivities and the report, then
the output: [`references/method.md`](references/method.md) Steps 6–11. Before presenting, check it
against [`references/output.md`](references/output.md). Ask whether the user wants the workbook as
an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 12. Persist the purpose, the standard of value
and the net debt definition. **No market data is saved.**

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
