---
name: notes-to-financial-statements
description: "Drafts and reviews the notes to the financial statements: builds the disclosure checklist for the framework and the entity, drafts the accounting policy notes and the account-detail notes from the figures, prepares commitments, contingencies, related party and subsequent events notes for a person to complete, then checks completeness and that every figure agrees with the statements. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded statements and schedules. Use when the user asks to draft or review notes or footnotes to the accounts, a disclosure checklist, an accounting policies note, or to check that notes agree with the statements. Do not use for building the statements themselves (use financial-statement-builder) or for the audit request list (use audit-prep-pbc-list). Read-only: produces draft notes with every gap flagged, and issues nothing."
---

# Notes to the accounts: what the numbers mean

The statements give the numbers; the **notes** explain what they mean, how they were arrived at,
and what else a reader needs to know. This skill builds the **disclosure checklist**, drafts the
notes from the entity's data, and flags every place where a person must supply the words.
Management reviews and issues them.

**Works with or without Mosofin.** With Mosofin connected the figures in each note are read from
the books and agreed to the statements. Without it, you upload the statements and schedules and
the method is the same.

**Figures are in the books. Policies and judgments are not.** The accounting policies in use, the
significant estimates, legal positions on contingencies and the full list of related parties come
from you. A draft with a gap shows the gap in place. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never states an accounting policy the user has not confirmed.**
- **Never drafts a legal conclusion on a contingency.** That is for whoever performs legal review.
- **Never fills a gap with plausible wording.** A missing disclosure is flagged where it belongs.
- **Never treats the checklist as complete without the framework and whether the entity is public
  or private.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–10" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, which period, and when will the accounts be issued?* | The issue date ends the subsequent events window | **Never default the period.** Without an issue date, list subsequent events candidates to today and say so. |
| **C** | *Which framework, and is the entity public or private?* | Decides the whole checklist and its volume | **Ask again.** |
| **D** | *Which accounting policies are in use, and what are the significant judgments and estimates?* | Not in the data | Draft the note structure only, with each policy marked for confirmation. |
| **E** | *Are there commitments, contingencies or related parties, and who performs legal review?* | Legal territory; relationships are not in the books | List candidates found in the books, and draft nothing on them. |
| **F** | *Do you have last year's notes and the supporting schedules for debt, leases and fixed assets?* | For consistency and the detail notes | Draft detail notes from balances only, and say the schedules were not supplied. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Agree every figure used in a note to the statements before drafting around it.
- List subsequent events candidates from postings after the period end, for the user to assess.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Financial statements** for the period and the comparative | Required | XLSX or PDF |
| **Trial balance** at the period end | Required for the detail notes | XLSX or CSV |
| **Schedules**: debt, leases, fixed assets | Required for those notes | XLSX |
| Prior year notes | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Drafting the notes for **Northbrook Trading** for the **year to 31 December**, a **private**
> company under **US GAAP**, from **your Mosofin connection**, to be issued on **20 March**.
> Policies as in **last year's notes**, which you uploaded. Legal review by **your counsel**.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the figures and build the checklist

Pull the statements and balances, then build the disclosure checklist:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Draft the notes

Accounting policies, account detail, commitments and contingencies, related parties and subsequent
events: [`references/method.md`](references/method.md) Steps 2–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for reduced disclosures for a private
company, first-time adoption, going-concern doubt, uncertain litigation and a restated
comparative.

## Stage 5 — Review completeness and consistency, and present

The completeness review, consistency and cross-references, then the output:
[`references/method.md`](references/method.md) Steps 7–9. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the draft as an Excel
file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the framework, the checklist as
tailored and the confirmed policies.

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
