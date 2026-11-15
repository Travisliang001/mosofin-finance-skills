---
name: restatement-and-prior-period-adjustment
description: "Handles the correction of an error in previously issued financial statements: sweeps the books for entries posted into closed periods, sets out whether the item is an error or a change in estimate, quantifies it across every affected period, lays out the materiality assessment for management and the auditors, works through the correction method, computes the corrections, and prepares the disclosures and control follow-up. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded statements and ledger detail. Use when the user asks about a prior period error, a restatement, a prior period adjustment, a revision, or entries posted to a closed year. Do not use for a change in estimate handled prospectively (use accruals-and-deferrals) or for routine closing entries (use closing-entries-and-trial-balance). Read-only: produces the quantification, proposed corrections and disclosures, and concludes on no materiality."
---

# Restatement: correcting an error in issued accounts

When issued financial statements turn out to contain an **error**, it has to be assessed,
quantified across every period it touched, and corrected in the right way. This skill does the
quantification, lays out the assessment, computes the corrections and drafts the disclosures.
Management, the audit committee and the auditors conclude.

**Works with or without Mosofin.** With Mosofin connected it sweeps for **entries posted into
periods that were already closed**, which is often how an error is found. Without it, you upload
the statements and ledger detail and the method is the same.

**The issued statements are documents, not ledger balances.** The books may have moved since. And
whether something is an error or a change in estimate turns on **what was known at the time**,
which is not in any ledger. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never concludes that an error is material or immaterial.** It sets out the quantitative and
  qualitative factors.
- **Never decides between a full restatement and a revision.**
- **Never treats a change in estimate as an error, or the reverse, on its own judgment.**
- **Never takes the issued figures from the ledger.** They come from the issued statements.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–8" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and what is the error and how was it found?* | How it was found feeds the root cause | **Ask again.** With none described, run the sweep for prior-period postings only. |
| **C** | *Can you supply the issued statements for each affected period?* | The authority for what was reported | Quantify against the books as they stand, and say that issued figures were not supplied. |
| **D** | *ASC 250 or IAS 8, and is the entity public or private?* | Decides the method and the regulatory consequences | **Ask again.** |
| **E** | *What was known at the time?* | Separates an error from a change in estimate | Set out both treatments, and decide neither. |
| **F** | *What materiality benchmarks do you and your auditors use?* | The assessment is measured against them | Show the error against revenue, profit and equity. **Never supply a threshold.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report every entry posted into a closed period, with its date, amount and source.
- Say whether the books still agree with the issued statements for each period.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Issued financial statements** for each affected period | Required | PDF |
| **Ledger detail** for the accounts affected, all periods | Required | XLSX or CSV |
| Materiality benchmarks | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Assessing an error in **revenue cut-off** at **Northbrook Trading**, found during **the Q3
> close**, affecting **the last two years**, under **ASC 250**, a **private** company. Issued
> statements **uploaded**; books from **your Mosofin connection**. Benchmarks as your auditors
> use. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the periods and the
totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Sweep the books and classify the item

Entries posted into prior periods, then error against change in estimate:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Quantify, and lay out materiality and method

The error across all affected periods, the materiality factors, and the correction method:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for qualitative materiality, several errors
together, interim periods, tax effects and covenants.

## Stage 5 — Compute corrections, disclosures, controls, and present

The corrections as **proposals**, the disclosures, the control and governance follow-up, then the
output: [`references/method.md`](references/method.md) Steps 5–8. Before presenting, check the
coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether the
user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the framework and the
materiality benchmarks. The matter itself is not carried into a later run.

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
