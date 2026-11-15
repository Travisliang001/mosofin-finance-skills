---
name: xbrl-tagging-checklist
description: "Gives a disciplined approach to XBRL and inline XBRL tagging for SEC filings: the tag map, governance over custom extensions, dimensional tagging, calculation and consistency checks, the calculation relationships the statements imply, and the validation and independent review workflow. States plainly that it cannot read the filing draft or the tagged file, which the user supplies. Reads the financial statement structure through a connected Mosofin workspace when the user agrees, or works from an uploaded draft and tag map. Use when the user asks about XBRL or iXBRL tagging, a tag map, custom extensions, calculation errors, or XBRL validation and review. Do not use for preparing the filing as a whole (use sec-10q-10k-prep) or for the notes (use notes-to-financial-statements). Read-only: produces the tag map review and checklist, and tags or files nothing."
---

# XBRL tagging: the map, the extensions, the checks

XBRL tagging labels every figure in a filing with an element from the taxonomy. This skill
provides the discipline around it: the **tag map**, the rules for **custom extensions**,
dimensional tagging, calculation checks and the review workflow. The tagging tool and the filing
agent do the tagging.

**Works with or without Mosofin.** With Mosofin connected it reads the structure of the statements
and derives which totals should add up, as a check on the calculation relationships. Without it,
you supply the statements and the method is the same.

**This is the narrowest fit in the library.** Tagging works on the filing draft and the tagged
file, and neither can be read through Mosofin. You supply the draft, the taxonomy version and the
prior tag map. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never assigns an element from memory.** Element names come from the taxonomy version the user
  states.
- **Never approves a custom extension.** It records the case for one and leaves the decision to
  the reviewer.
- **Never treats a valid file as a correct one.** A wrong element can pass validation.
- **Never tags or files anything.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–5" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, filing and period?* | Sets the scope | **Never default the period.** |
| **C** | *Which taxonomy version is in use?* | It changes every year | **Ask again.** |
| **D** | *Can you supply the filing draft and the prior filing's tag map?* | Neither can be read through Mosofin | Give the checklist only, with no tag review. |
| **E** | *Do you have the validation tool's output?* | The starting point for the error review | List the validation review as not done. |
| **F** | *Who performs the independent review?* | A second person must check the tags | Leave the reviewer open, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Derive the calculation relationships the statements imply, to compare with those in the tagged
  file.
- Read the saved profile: the tag map is the most valuable thing to keep from one filing to the
  next.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Filing draft** | Required | PDF or DOCX |
| **Prior tag map** | Required for consistency | XLSX |
| **Validation output** | Recommended | PDF or text |
| Taxonomy version and reviewer | Required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Reviewing XBRL tagging for the **Q3 10-Q** of **Northbrook Holdings**, on the **taxonomy
> version you named**, from **the draft and prior tag map you uploaded**. Statement structure from
> **your Mosofin connection**. Independent review by **your reporting manager**. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the filing, the
period and the number of tagged items. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Build or refresh the tag map

The tag map against the prior filing: [`references/method.md`](references/method.md) Step 1.

## Stage 4 — Extensions, dimensions and calculation checks

Extensions governance, dimensional tagging, calculation and consistency checks, and the expected
calculation relationships: [`references/method.md`](references/method.md) Steps 2–4b. Check
[`references/edge-cases.md`](references/edge-cases.md) for a taxonomy version change, comparatives
tagged from a stale figure and extension proliferation.

## Stage 5 — Validation workflow, and present

The validation and review workflow, then the outputs:
[`references/method.md`](references/method.md) Step 5 and *Outputs*. Before presenting, check the
coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether the
user wants the tag map as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the tag map, the
taxonomy version it belongs to and the extensions with their reasons.

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
