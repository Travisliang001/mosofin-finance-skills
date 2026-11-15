---
name: internal-audit-workpaper
description: "Plans and documents an internal audit: scoping, understanding the area, the audit program, fieldwork with workpapers, findings written as condition, criteria, cause and consequence, risk ratings, management responses, the report and follow-up. Tests whole transaction populations where the books allow it, in place of a sample, and states which procedures need observation, interviews or documents. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded transaction data and process documents. Use when the user asks to plan or run an internal audit, write an audit program, document workpapers, draft audit findings or an internal audit report, or follow up prior findings. Do not use for preparing for the external audit (use audit-prep-pbc-list) or for fraud red-flag testing (use fraud-detection-and-forensics). Read-only: produces the program, workpapers, findings and a coverage sheet, and changes no record."
---

# Internal audit: program, workpapers, findings, report

Internal audit is the organisation checking itself. Someone independent looks at how a process
**actually runs**, compares it with how it **should run**, works out why the gap exists, and
agrees a fix. This skill plans the audit, documents the work, and drafts the findings and the
report. The auditor forms the conclusions.

**Works with or without Mosofin.** With Mosofin connected, the data-based procedures run on the
**whole population** in place of a sample. Without it, you upload the data and the method is the
same.

**The books cover part of the work.** Analysis and re-performance on recorded transactions can be
read. Observation, interviews and inspecting documents cannot. And a ledger holds only what was
recorded, so a full-population test is not full assurance. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never writes a finding without criteria.** With no "should be", it is an observation.
- **Never presents an analytical result as a conclusion**, or a full-population test as full
  assurance.
- **Never rates a finding or accepts a management response for the auditor.** It proposes; the
  auditor decides.

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
| **B** | *Which area is being audited, what are the objectives, and is it operational, financial, compliance or IT?* | Everything links back to the objectives | **Ask again.** Nothing can be planned without them. |
| **C** | *Which company and period?* | Sets the population | **Never default the period.** |
| **D** | *What are the criteria: the policies, regulations or standards the area must meet?* | The "should be" half of every finding | Record observations only. No findings are written. |
| **E** | *How does the process work, and what did prior audits find?* | Process knowledge is not in a ledger; repeat findings rate higher | Plan from the data alone, and list the walkthrough as not done. |
| **F** | *Who is performing the audit, did they operate this area, and is completeness in scope?* | Independence, and whether an outside reference point is needed | **Ask again.** State any independence limit in the report. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say which fields exist in the data **before** designing tests around them.
- Record any entity left out as a scope limitation.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Transaction data** for the area and period | Required | XLSX or CSV |
| **Criteria**: policies, procedures, regulations (D) | Required for findings | PDF, or type it in the chat |
| Process documentation and walkthrough notes (E) | Recommended | PDF |
| Prior audit report and open actions | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Planning a **compliance** audit of **purchase-to-pay** at **Northbrook Trading** for the **year
> to September**, from **your Mosofin connection**. Criteria: the **purchasing policy** you
> uploaded. Performed by **internal audit**, who did not operate the area. Completeness is out of
> scope. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
row count and the fields present. Flag anything unreadable straight away.

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

## Stage 3 — Read the population, plan, and understand the area

Pull the population in one batch, then plan the audit and document how the area works:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Build the program and do the fieldwork

Write the audit program, then execute and document the workpapers:
[`references/method.md`](references/method.md) Steps 3–4. Test the whole population where it can
be read; sample only where it cannot. Check [`references/edge-cases.md`](references/edge-cases.md)
for scope limitations, independence, consulting against assurance, and a program made only of
data tests.

## Stage 5 — Findings, responses, report, and present

Develop the findings, propose ratings, record management responses, structure the report and the
follow-up, then the output: [`references/method.md`](references/method.md) Steps 5–10. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpapers as an Excel file, or the report as a document, before creating either.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11, which states exactly what may be kept.

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
