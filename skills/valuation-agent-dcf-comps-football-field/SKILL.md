---
name: valuation-agent-dcf-comps-football-field
description: "Builds a valuation package from forecast cash flows and market evidence, with every assumption visible and editable: anchors the valuation date, builds the discounted cash flow, lays out the WACC inputs, calculates terminal value two ways, builds the comparable company and transaction screens, draws the football field, and bridges enterprise value to equity value. Reads the company's net debt items through a connected Mosofin workspace when the user agrees, or works from an uploaded model. Use when the user asks for a DCF with a WACC build, a comps table, a football field chart, or a valuation package for a deal or a board. Do not use for a short valuation range (use business-valuation) or for testing a model's formulas (use model-auditor-financial-model-review). Read-only: produces valuation analysis, not an opinion of value, and supplies no market data."
---

# Valuation package: DCF, comps and the football field

Builds the analyst's valuation package: a **discounted cash flow** with the cost of capital laid
open, **comparable screens**, and a **football field** that sets the ranges side by side. Every
assumption stays visible and editable, so a reader can change one and see the effect.

**Works with or without Mosofin.** With Mosofin connected the items in the bridge from enterprise
value to equity value, such as debt, cash and leases, are read from the books at the valuation
date. Without it, you upload the model and the method is the same.

**The bridge is where the books matter most; the rest is market data and your forecast.** Cost of
capital inputs, comparables and the share count come from you. **This is analysis, not an opinion
of value.** Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Produces valuation analysis, not an opinion of value.** It is not a licensed valuation
  professional, and a qualified one signs before anyone relies on the figure.
- **Never supplies market data.** Discount rate inputs, multiples, comparables and prices come
  from the user, each with its source and date.
- **Never hides an assumption inside a formula.** Each is shown with its source.
- **Never lets a terminal value pass without showing its share of the total.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–7" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which business, what valuation date, and for whom?* | The date controls everything; the audience sets whether a specialist is needed | **Ask again.** |
| **C** | *Can you supply the forecast model, with its structure and not only its outputs?* | The cash flows are yours | **Blocking** for the cash flow approach. |
| **D** | *What are the WACC inputs, with sources and dates?* | Market data | Lay out the build with each input blank. |
| **E** | *Which comparable companies and transactions should be screened?* | The universe is a judgment | Build the screen layout only. |
| **F** | *What are the diluted share count and your definition of net debt?* | No cap table in the books | Bridge to equity value in total, on the items read, and list the definition as not confirmed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the candidate bridge items: debt, leases, restricted cash and other debt-like balances.
- Flag a valuation date that is not a period end.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Forecast model** | Required | XLSX |
| **WACC inputs** with sources | Required | XLSX |
| **Comparable and transaction data** | Required for the screens | XLSX |
| Balance sheet at the valuation date and cap table | Required for the bridge | XLSX |

**Read back before starting, then wait for a yes:**

> *Building a valuation package for **Northbrook Trading** at **31 December**, for **the board**,
> on **your five-year model**, with WACC inputs and **eight comparables** from **the files you
> uploaded**. Bridge items from **your Mosofin connection**; net debt **including leases**. Shall
> I go ahead?*

On the upload path, name each file you received and say what was read from it: the model's drivers
and outputs, and the sources of market data. Flag anything unreadable straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Anchor the valuation and build the DCF

The valuation date and basis, then the discounted cash flow:
[`references/method.md`](references/method.md) Steps 1–2.

## Stage 4 — Cost of capital, terminal value and comparables

The visible WACC, terminal value, then the comparable screens:
[`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for levered cash flows discounted at WACC,
a terminal value that dominates, and terminal growth above long-run growth.

## Stage 5 — Football field, bridge, and present

The football field, the bridge to equity value, then the package:
[`references/method.md`](references/method.md) Steps 6–7, including Step 6b. Before presenting,
check the coverage and provenance sheet in [`references/output.md`](references/output.md). Ask
whether the user wants the valuation package as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the layout and the net
debt definition. **No market data is saved.**

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
