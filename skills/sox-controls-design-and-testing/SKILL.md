---
name: sox-controls-design-and-testing
description: "Designs, documents and tests internal controls over financial reporting: scoping, walkthroughs, what could go wrong, the risk and control matrix, segregation of duties tested across every transaction, design assessment, test plans, test results, deficiency evaluation and remediation. Says for each control whether its operation leaves a trace in the books, tests those at full population, and marks the rest for evidence a person must supply. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded transaction data and control documents. Use when the user asks about SOX, ICFR, internal controls over financial reporting, a risk and control matrix, control testing, segregation of duties, or control deficiencies. Do not use for a general internal audit (use internal-audit-workpaper) or for fraud red-flag testing (use fraud-detection-and-forensics). Read-only: produces the matrix, test results and a coverage sheet, and concludes on no severity."
---

# SOX controls: did the control operate?

Designs, documents and tests **internal controls over financial reporting**. It builds the risk
and control matrix, assesses each control's design, plans and runs the tests, and lays out any
deficiency with its exposure. Management and the auditors rate severity and conclude.

**Works with or without Mosofin.** With Mosofin connected, controls that leave a trace in the
books are tested across **every transaction**, and segregation of duties is tested across the
whole population. Without it, you upload the data and the method is the same.

**A control test asks whether the control operated. A read of the books asks what the data
shows.** These are different questions. A control can operate and the outcome still be wrong;
the outcome can be right with no control operating at all. Clean data is never evidence that a
control ran. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never treats clean data as proof that a control operated.**
- **Never fills in a severity rating or concludes on a material weakness.** It quantifies the
  exposure and leaves the rating to management and the auditors.
- **Never lets a control that could not be tested read as effective.**
- **Never invents materiality or a sample size.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–10" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which processes are in scope, for which company and period, and why those?* | Sets the control environment | **Ask again.** Never default the scope or the period. |
| **C** | *Is the objective design, operating effectiveness, or both?* | Decides which steps run | **Ask again.** |
| **D** | *Which controls exist, and for each: does it leave a trace in the accounting system, and where is its evidence?* | This one answer routes each control to a full-population test or to evidence a person supplies | Draft the matrix from the risks, and mark every control as evidence needed. |
| **E** | *How does each process actually work, and which systems are involved?* | Walkthroughs are not in a ledger | List the walkthroughs as not done. |
| **F** | *What are materiality and the scoping thresholds, and which prior deficiencies are open?* | Deficiencies are judged against them | Report exposures in amounts only. **Never supply a threshold.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Say whether the data records **who** created and approved each transaction. Without it,
  segregation of duties cannot be tested from the books.
- Say that Mosofin's own output is system-generated information, and its completeness is for the
  user to establish.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Process descriptions and the existing control list** | Required | PDF or XLSX |
| **Transaction data** for the in-scope processes, with user and approval fields | Required for population tests | XLSX or CSV |
| **Control evidence**: sign-offs, review records, reconciliations | Required for controls outside the books | PDF |
| Materiality (F), prior deficiencies | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Testing **operating effectiveness** of **purchase-to-pay and period close** controls at
> **Northbrook Trading** for the **year to December**, from **your Mosofin connection**.
> **Fourteen controls**: nine leave a trace in the books, five need the evidence you will supply.
> Materiality as you gave it. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it. Flag anything
unreadable, or transaction data with no user field, straight away.

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

## Stage 3 — Scope, walk through, and identify the risks

Scope the control environment, document the process, then list what could go wrong:
[`references/method.md`](references/method.md) Steps 1–3.

## Stage 4 — Build the matrix and assess design

The risk and control matrix, segregation of duties across the population, then design assessment:
[`references/method.md`](references/method.md) Steps 4–5, including Step 4b. Check
[`references/edge-cases.md`](references/edge-cases.md) for IT general controls, system-generated
reports, management review controls, small teams and outsourced processes.

## Stage 5 — Test, evaluate deficiencies, and present

Test plans, which controls can be tested at full population, the testing, deficiency evaluation
and remediation, then the output: [`references/method.md`](references/method.md) Steps 6–10,
including Step 6b. Before presenting, check the coverage and provenance sheet in
[`references/output.md`](references/output.md). Ask whether the user wants the workbook as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the matrix and which
controls leave a trace in the books. Test results are produced again each period.

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
