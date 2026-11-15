---
name: model-auditor-financial-model-review
description: "Performs the last review before a financial model is sent out: freezes the scope, ties the model's historical figures to the books, reviews formula integrity, checks that the statements and schedules agree with each other, reviews the scenarios and sensitivities, and delivers an issue log with a pass or hold call. Reads the source figures through a connected Mosofin workspace when the user agrees, and works from the model the user uploads. Use when the user asks to review, audit or sanity-check a financial model before it goes to a board, lender or investor, or to tie a model's actuals to the books. Do not use for building a model (use three-statement-financial-model or model-builder-integrated-three-statement) or for running scenarios (use scenario-and-sensitivity-analysis). Read-only: produces an issue log and a recommendation, changes no model, and gives no opinion on the assumptions."
---

# Model review: the last pass before it goes out

The last check before a model is sent to a board, a lender or an investor. It ties the model's
**history to the books**, checks the **formulas**, tests that the statements and schedules agree,
and returns an **issue log with a pass or hold call**. The model's owner fixes it.

**Works with or without Mosofin.** With Mosofin connected the model's historical figures are tied
to the books they claim to come from. Without it, you supply the source statements and the method
is the same.

**The model itself is never in the workspace.** You upload it. And this is a review of mechanics
and sources: whether the assumptions are reasonable is the owner's judgment, not this skill's.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never edits the model.** Every issue is logged for the owner.
- **Never judges whether an assumption is right.** It checks that it is visible, sourced and
  applied as stated.
- **Never calls a pass on tabs it did not review.** The scope is stated on the log.
- **Never treats a stale history as an error**, or the reverse. It reports when the actuals were
  extracted.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *What is the model for, and who receives it?* | Sets how strict the review is | **Ask again.** |
| **C** | *Can you upload the model, and is the scope the whole model, selected tabs, or one issue?* | The model is not in the workspace | **Blocking.** |
| **D** | *Which entity or group does the model represent, and when were its actuals extracted?* | Decides what it is tied to | **Ask again.** |
| **E** | *What is the materiality threshold?* | Separates a finding from a rounding difference | Report every difference, and say no threshold was supplied. |
| **F** | *Are there known problem areas?* | Focuses the review | Review all tabs in scope evenly. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether the books have changed since the model's actuals were extracted.
- Confirm how the model's lines map to accounts.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **The financial model** | Required | XLSX |
| **Source statements** the history was drawn from | Required if Mosofin is not used | XLSX or PDF |
| Account-to-line mapping | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Reviewing **the lender model** for **Northbrook Trading**, whole model, with actuals extracted
> on **5 October**, tied to **your Mosofin connection**. Materiality **10,000**. Known concern:
> **the debt schedule**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the tabs, the
periods and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the source and freeze the scope

Pull the source figures, then fix the scope of the review:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Tie out, review formulas and check the statements

The source tie-out, formula integrity, and statement and schedule checks:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for a stale history, a line that aggregates
several accounts, and a consolidated model tied to one entity.

## Stage 5 — Scenarios, issue log, and present

The scenario and sensitivity review, the issue log with the pass or hold call, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the issue log as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the account mapping and the
materiality threshold.

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
