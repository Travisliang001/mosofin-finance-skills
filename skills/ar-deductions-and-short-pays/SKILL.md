---
name: ar-deductions-and-short-pays
description: "Works the open customer deductions and short payments: lists every amount a customer held back, ages it, sorts it by reason (damage, shortage, pricing, promotion, freight, unexplained), checks each against its evidence (proof of delivery, carrier report, promotion agreement, contract terms) and the write-off policy, and decides valid, invalid or needs backup. Catches the same invoice deducted twice. Proposes credit memos for valid deductions, small-balance write-offs within policy, and dispute letters for invalid ones. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded deduction lists and backup. Use when the user asks about deductions, short pays, chargebacks from retailers, customer disputes, or clearing old deductions out of receivables. Do not use for matching full payments to invoices (use cash-application) or chasing overdue invoices (use ar-aging-and-collections). Read-only: produces the deduction log, proposed credit memos, write-offs and dispute drafts, and posts nothing."
---

# Customer deductions and short pays: valid, invalid, or needs backup

When a customer pays less than the invoice and says why, the difference is a **deduction**. Left
alone, deductions pile up in receivables, age past the point anyone can dispute them, and get
written off in bulk. This skill works each one: **what reason, what evidence, valid or not**, and
the next step. A person approves every credit, write-off and letter.

**Works with or without Mosofin.** With Mosofin connected it reads the invoices, payments and
credit memos behind each deduction. Without it, you upload the deduction list and the backup, and
the method is the same.

**A deduction is a claim, not a fact.** The customer's reason code says what they claim. Only
the evidence (a signed delivery note, a carrier's damage report, a promotion agreement, the
contract's freight terms) decides whether it is valid. Without evidence either way, the answer is
"needs backup", never a guess. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** It issues no credit memo, writes
  nothing off and sends no letter. Every one is a proposal.
- **Never writes off above the policy limit**, and never proposes a write-off without naming who
  approves it under the policy.
- **Never calls a deduction valid or invalid without evidence.** No evidence is "needs backup".

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Collect the basics in **one short batch**. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and as at what date?* | Sets the ageing and every read | **Never default the date.** |
| **C** | *Where are open deductions kept? A deduction log, a separate receivables account, or open invoice balances* | Decides where the population comes from | Treat every partly paid invoice as a candidate deduction, and say so. |
| **D** | *What is the write-off policy? The limit, and who approves* | Decides which small items can be cleared | **No write-offs proposed**; every item is worked. Say so. |
| **E** | *What backup do you have? Proofs of delivery, carrier reports, promotion agreements, contracts* | The evidence that decides valid or invalid | Every item without backup is "needs backup". |
| **F** | *How long do customers allow for a dispute? Any customer-specific rules* | Old deductions are hard to recover | Flag anything over 90 days as at risk. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Ask for the backup (E) all the same: proofs of delivery and agreements are not in the books.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Open deductions**: customer, invoice, payment date, amount held back, reason given | Required | XLSX or CSV |
| **Backup**: proofs of delivery, carrier damage reports, promotion or pricing agreements, contract terms | Required to decide valid or invalid. Without it every item is "needs backup" | PDF, text, or type it in the chat |
| Remittance advices for the short payments | Recommended. They carry the customer's own reason | PDF or text |
| Open receivables and customer list | Recommended | XLSX or CSV |
| Write-off and dispute policy (D, F) | Recommended | Any, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Working **Acme Supply**'s open deductions **as at 31 March 2026**, from **the deduction log you
> uploaded**, with **the backup file and your write-off policy** (write-off up to 100, approved by
> the finance manager). Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date it
covers, the row count and the totals. Flag anything unreadable, or for the wrong date, straight
away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile. On the upload
path, go straight to Stage 3.

## Stage 3 — Build the deduction log

Read the invoices, payments and credit memos in one batch, and build one row per deduction with
its age: [`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Check each deduction against its evidence

Look for duplicates first, then decide each deduction by its reason code and its backup:
[`references/method.md`](references/method.md) Steps 3–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for partial evidence, repeat claimants and
deductions taken on a credit already issued.

## Stage 5 — Propose the resolutions and present

Credit memos for valid items, write-offs within policy, dispute drafts for invalid ones, backup
requests for the rest: [`references/method.md`](references/method.md) Steps 5–6 and *Outputs*.
Before presenting, check it against [`references/output.md`](references/output.md). Ask whether
the user wants the log as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the reason-code map, the policy and
the customer rules.

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
