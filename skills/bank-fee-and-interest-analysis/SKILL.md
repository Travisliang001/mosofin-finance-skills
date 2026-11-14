---
name: bank-fee-and-interest-analysis
description: "Analyses bank fees and interest: sorts every charge into a category, ties it to the general ledger, finds miscoded and missing postings, computes the cost per wire, payment and deposit against real transaction volumes, shows the trend, and sizes each way to bring the cost down. States plainly when it saw only the fees recorded in the books and not the bank statement. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded ledger detail and bank statements. Use when the user says bank fees are too high, asks to analyse bank charges, wire or merchant fees, tie out interest income, check fee coding, or prepare to renegotiate banking services. Do not use for reconciling the bank account (use bank-reconciliation) or for payment processor payouts (use merchant-and-payment-processor-rec). Read-only: produces the analysis, proposed entries and a coverage sheet, and posts nothing."
---

# Bank fees and interest: what the bank costs per transaction

Banks charge for many small things, and the charges are easy to stop noticing. This skill gathers
them, **sorts them into categories**, checks they were recorded correctly, works out the **cost per
transaction**, and sizes each way to reduce it. A person decides what to renegotiate.

**Works with or without Mosofin.** With Mosofin connected it reads the fee, interest and cash
accounts, and counts the wires, payments and deposits that drive the fees. Without it, you upload
the ledger detail and the method is the same.

**The bank statement is never available through Mosofin, on any path.** Mosofin connects the
books, not the bank. A fee netted out of a deposit, or debited and never coded, is not in the
books, so a books-only analysis under-reports the total. Ask for the statements. Without them the
output says, on its face, that only posted fees were examined. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It recodes nothing, closes no
  account and contacts no bank. Every entry is a proposal.
- **Never calls a total from the books "total bank fees"** unless the statements were supplied.
- **Never estimates a fee or a rate.** A recommendation carries its saving, the count it rests on
  and the assumption behind it.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and which period? Thirteen months or more shows the year-on-year trend.* | Sets every read | **Never default the period.** |
| **C** | *Can you supply the bank statements, or the bank's account analysis statement?* | The only evidence of fees that never reached the books | Analyse posted fees only, list "missing postings" as not run, and **say so on the face of the output.** |
| **D** | *Which banking products do you use? Accounts, wires, ACH, lockbox, merchant services* | A product with no fees recorded against it is a finding | Report the categories found, and do not flag an empty one. |
| **E** | *Do you have the bank's fee schedule or rate sheet?* | Compares what was paid with what was promised | Report the rate paid per transaction only. |
| **F** | *Does the bank apply an earnings credit rate?* | It changes the true cost of the account | Assume none, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Find the bank fee, interest and cash accounts in the chart of accounts, and **confirm them with
  the user** by their real names.
- Ask for the bank statements (C) all the same.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Ledger detail** for the bank fee, interest income, interest expense and cash accounts | Required | XLSX or CSV |
| **Bank statements**, or the **account analysis statement**, for the period | **Required to find fees missing from the books.** Without them the skill still runs on posted fees and says so | PDF or CSV |
| Payment, deposit and receipt listings for the period | Recommended. They supply the transaction counts behind each unit rate | XLSX or CSV |
| Fee schedule (E), product list (D), earnings credit rate (F) | Recommended | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Analysing bank fees and interest for **Northbrook Trading** for the **13 months to September**,
> from **your Mosofin connection**, with the **account analysis statements you uploaded**. Products:
> two operating accounts, wires and merchant services. No fee schedule supplied. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period it
covers, the row count and the totals. Flag anything unreadable, or covering the wrong period,
straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the fees and build the categories

Pull the fee, interest and cash ledgers with the payment and deposit counts in one batch, then
build the fee categories and map each to its account:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Classify, tie to the ledger, and trend

Classify every line, tie it to the ledger and detect coding issues, then analyse trend and
variance: [`references/method.md`](references/method.md) Steps 2–4. Run the netting check: a
deposit smaller than the receipts it covers almost always had a fee deducted. Check
[`references/edge-cases.md`](references/edge-cases.md) whenever something looks unusual.

## Stage 5 — Size the savings, propose entries, and present

Cost reduction options, each sized, then the correcting entries as **proposals**, then the
outputs and coverage sheet: [`references/method.md`](references/method.md) Steps 5–6 and
*Outputs*. Before presenting, check it against [`references/output.md`](references/output.md).
Ask whether the user wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the account mapping, the product
list and the fee schedule.

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
