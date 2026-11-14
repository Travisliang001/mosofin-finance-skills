---
name: scenario-and-sensitivity-analysis
description: "Tests how a financial outcome changes as assumptions move: best, base and worst scenarios, single- and two-variable sensitivity tables, a tornado ranking of the drivers, breakeven and threshold analysis, and probability weighting, on top of a model or plan the user already has. Proposes each driver's range from what that driver has actually done in the books, so the ranking reflects the business and not a blanket plus or minus ten percent. Reads history through a connected Mosofin workspace when the user agrees, or works from an uploaded model and history. Use when the user asks for scenario analysis, sensitivity analysis, a tornado chart, a stress test, a what-if, breakeven, or which assumptions matter most. Do not use for building the forecast itself (use rolling-forecast) or for tracking covenants (use debt-and-covenant-tracking). Read-only: produces the analysis and a coverage sheet, and posts nothing."
---

# Scenarios and sensitivities: which assumptions matter

Tests how an outcome changes when the assumptions behind it move. It builds **scenarios**,
**sensitivity tables** and a **tornado ranking** of the drivers, and finds the point where a
threshold breaks. It works **on top of a model or plan you already have**; it does not build one.

**Works with or without Mosofin.** Most of this is pure calculation and needs no accounting system.
Mosofin changes one input, the one that decides whether the answer means anything: **the ranges.**

**A tornado ranks drivers by the range you gave them.** Flex every driver by the same ten percent
and the chart ranks the model's structure, not the business's risk. With Mosofin connected, each
range is proposed from what that driver actually did over the history in the books. You accept,
adjust or override it. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never applies a mechanical range without saying so.** Every range states its source: observed
  history, or the user's judgment.
- **Never invents a probability, a distribution or a covenant definition.**
- **Never authors a forward-looking statement.** Scenarios are the user's stories; the skill
  computes them.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–11" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What decision is this for, and which model or plan does it sit on?* | The analysis needs the model's structure, not only its outputs | **Ask again.** With outputs only, say that the user must run the scenarios in their own model. |
| **C** | *Which outcome matters: net income, EBITDA, cash runway, a covenant ratio?* | The choice changes the ranking | **Ask again.** Never pick the metric. |
| **D** | *Which drivers should vary, and do you have a range in mind for each?* | The drivers are the user's choice | Propose ranges from observed history and **wait for a yes.** |
| **E** | *Do you want named scenarios, and what is the story behind each?* | A coherent scenario is authored, not computed | Run sensitivities only, with no named scenarios. |
| **F** | *Any thresholds to test: a covenant level, minimum cash, breakeven? Any probability weights?* | Sets the breakeven and expected-value work | Skip those steps and list them as not run. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say how many months of history each driver's range rests on.
- With several company files, say that a group model needs consolidated history; several ledgers
  added together are not that.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **The model or plan**, with its assumptions visible | Required | XLSX |
| **Monthly history** for the drivers, 24 months or more | Recommended. Without it ranges are the user's judgment, and the output says so | XLSX or CSV |
| Scenario definitions (E), thresholds and weights (F) | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Testing **cash runway** in **Northbrook Trading's 2027 plan**, varying **revenue growth, gross
> margin, DSO and headcount cost**, with ranges from **48 months of history** in **your Mosofin
> connection**. Three named scenarios as you described, and a **minimum cash** threshold. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the model's
drivers and outputs, the months of history. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Clarify the question and ground the ranges

Settle the question, isolate the drivers, then propose each range from observed history:
[`references/method.md`](references/method.md) Steps 1–2, including Step 2b.

## Stage 4 — Run the scenarios and sensitivities

Discrete scenarios, single-variable sensitivity, the tornado, two-variable tables and breakeven:
[`references/method.md`](references/method.md) Steps 3–7. Check
[`references/edge-cases.md`](references/edge-cases.md) for drivers that move together,
non-linear responses, circular models, unrealistic combinations and asymmetric ranges.

## Stage 5 — Weight, synthesise, and present

Probability weighting and Monte Carlo where asked, the synthesis, then the output:
[`references/method.md`](references/method.md) Steps 8–11. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md): which figures were read
and which were only calculated. Ask whether the user wants the workbook as an Excel file before
creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the driver list, the
accepted ranges with their source, and the thresholds.

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
