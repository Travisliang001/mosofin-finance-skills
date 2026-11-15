---
name: petty-cash-management
description: "Reconciles a petty cash float: tests that cash counted plus vouchers equals the authorised float, reads the vouchers, codes each to a ledger account, computes the replenishment, and reports any shortage or overage, with the proposed entry. Checks that the petty cash balance in the books equals the authorised float and only moves on replenishment. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded count and vouchers. Use when the user asks to reconcile petty cash, replenish a float, process petty cash vouchers, or explain a petty cash shortage. Do not use for a bank account (use bank-reconciliation) or for employee expense claims (use expense-report-processor). Read-only: produces the reconciliation and a proposed entry, and never stands in for the physical count."
---

# Petty cash: cash plus receipts equals the float

A tin of cash for small purchases, topped back up to a fixed amount each time it runs down. At any
moment **the cash plus the receipts should equal that fixed amount**. Checking that they do is the
whole control. This skill does the check, codes the vouchers and computes the top-up.

**Works with or without Mosofin.** With Mosofin connected it reads the petty cash balance in the
books and its history of top-ups. Without it, you supply the float amount and the method is the
same.

**The count is the one input nothing here can supply.** The books say what should be in the tin;
only counting says what is. The vouchers are paper, and they come from you too. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never accepts a book balance in place of a physical count.**
- **Never assumes a receipt threshold or a shortage tolerance.**
- **Never concludes theft.** A shortage is reported with its amount, the custodian and the count
  date.

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
| **B** | *Which company, which float, and which period?* | Sets the scope | **Never default the period.** |
| **C** | *What is the authorised float amount?* | The figure everything must equal | Use the balance in the books, and **say it was not confirmed.** |
| **D** | *What was the cash count, who counted it, and when?* | Nothing else can supply it | **Blocking.** No reconciliation without a count. |
| **E** | *Can you supply the vouchers and receipts for the period?* | The other half of the equation | Reconcile cash to the float only, and report the difference as unsupported. |
| **F** | *Who is the custodian, and what are the receipt threshold and the shortage tolerance?* | Policy, not data | Apply no threshold and no tolerance, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report whether the balance in the books equals the authorised float, and whether it moved other
  than on replenishment.
- Take the accounts for coding from the real chart of accounts.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Cash count**, with date and counter | Required | Type it in the chat |
| **Vouchers and receipts** | Required | PDF, images, or a listing |
| **Petty cash account detail** for the period | Recommended | XLSX or CSV |

**Read back before starting, then wait for a yes:**

> *Reconciling the **head office float** of **500** at **Northbrook Trading** for **September**,
> from **your Mosofin connection**. Count of **182.40** by **the office manager on 30 September**;
> **23 vouchers** uploaded. Receipts required above **25**; no tolerance. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the voucher count,
the dates and the total. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read the books and test the float

Pull the petty cash account, test the float, then capture the count:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Read the vouchers and reconcile

Parse the vouchers, compute the reconciliation, then code each voucher:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for staff advances, a voucher with no
receipt, a voucher dated outside the period and a change of custodian.

## Stage 5 — Replenish, handle differences, and present

The replenishment as a **proposal**, the handling of any shortage or overage, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the float amount, the custodian,
the thresholds and the coding of recurring items.

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
