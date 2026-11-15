---
name: ar-cash-application-lockbox
description: "Applies customer receipts from a lockbox, ACH or wire file to open invoices: normalises the receipts, matches them through a hierarchy from exact reference to amount and payer, handles short-pays, deductions and unidentified cash, proposes the entries, and ties the applied total to the bank. Reads open invoices through a connected Mosofin workspace when the user agrees, or works from uploaded bank and remittance files. Use when the user has a lockbox or bank deposit file and remittance advice to apply, asks about deductions and short-pays at volume, or needs unapplied cash cleared from a bank file. Do not use for applying payments already recorded in the books without a bank file (use cash-application) or for the bank account itself (use bank-reconciliation). Read-only: proposes applications and entries for a person to post, and applies nothing."
---

# Lockbox cash application: which invoices did each payment settle?

Money arrives by transfer, card or a batch of cheques collected at a **lockbox**. Someone has to
work out which invoices each payment was meant to settle. This skill starts from the **bank or
lockbox file**, matches each receipt, handles short-pays and deductions, and proposes the
applications. A person posts them.

**Works with or without Mosofin.** With Mosofin connected the open invoices and customer records
are read. Without it, you upload them and the method is the same.

**The bank file and the remittance advice are never available through Mosofin.** You supply them.
This is the file-driven companion to `cash-application`, which works from payments already
recorded in the books. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never accepts a fuzzy match on its own.** It is proposed with its basis, for a person to
  confirm.
- **Never writes off a short-pay without the policy and the approver.**
- **Never calls a tie between two sets of book figures a tie to the bank.**
- **Never guesses between two invoices of the same amount.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–6" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and which dates?* | Sets the receipts and the open invoices | **Never default the period.** |
| **C** | *Can you supply the bank or lockbox file?* | The starting point, and never in the books | **Blocking.** For payments already recorded, use `cash-application`. |
| **D** | *Is there remittance advice: email, EDI or PDF?* | The biggest driver of match quality | Match on reference, amount and payer only, and say so. |
| **E** | *What is the deduction policy: write-off limit and approver?* | Decides how short-pays are treated | Leave every short-pay open as a deduction. |
| **F** | *Which account holds unapplied cash, and how do payers' names differ from customer names?* | Needed for unidentified receipts | Confirm the account by name; build the alias list as matches are confirmed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Confirm the unapplied cash account by its real name.
- Say that the tie to the bank rests on the file supplied, not on a bank connection.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Bank or lockbox file** for the dates | Required | CSV or XLSX |
| **Remittance advice** | Recommended | PDF, CSV or pasted |
| **Open receivables**, by invoice | Required | XLSX or CSV |
| Deduction policy | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Applying **the lockbox file for 22–26 September** for **Northbrook Trading**, against open
> invoices from **your Mosofin connection**, with **remittances you uploaded**. Short-pays under
> **50** written off with **the credit manager's** approval; unapplied cash in **the account you
> confirmed**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the dates, the
receipt count and the total. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the open invoices and normalise the receipts

Pull the open invoices and customers, then normalise the receipts:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Match and handle exceptions

The match hierarchy, then the exceptions: [`references/method.md`](references/method.md) Steps
2–3. Check [`references/edge-cases.md`](references/edge-cases.md) for two invoices at the same
amount, several combinations that sum to a receipt, and a fuzzy match.

## Stage 5 — Propose entries, tie to the bank, and present

The entries as **proposals**, the tie to the bank file, then the outputs:
[`references/method.md`](references/method.md) Steps 4–5 and *Outputs*. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 6. Persist the payer alias list, the deduction
policy and the unapplied cash account.

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
