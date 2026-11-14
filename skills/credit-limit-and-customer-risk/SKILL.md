---
name: credit-limit-and-customer-risk
description: "Assesses a business customer's creditworthiness and recommends a credit limit and terms: the customer's actual days-to-pay and its trend, current exposure and overdue share, disputes and write-off history, concentration, a score, the limit, the conditions, and the triggers for review. Leads with the user's own payment experience of the customer and states that the customer's financials, bureau report and references must come from outside the books. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded receivables history. Use when the user asks to set or review a credit limit, assess a new customer's credit risk, decide payment terms, check customer concentration, or monitor credit exposure. Do not use for chasing overdue invoices (use ar-aging-and-collections) or for applying customer payments (use cash-application). Read-only: recommends a limit and terms, sets nothing, and places no hold."
---

# Credit limit: how much to lend each customer

Every invoice sent without payment up front is a loan to the customer. This skill decides **how
much to lend each one**, on what terms, and what should trigger a review. It recommends; the
credit function decides.

**Works with or without Mosofin.** With Mosofin connected it reads your whole history with the
customer. Without it, you upload the receivables history and the method is the same.

**There are two kinds of evidence, and the books hold one.** Your own experience of the customer
is in your books: every invoice and payment, so actual days-to-pay, exposure, disputes and
write-offs. Information about the customer is not: their financial statements, a credit bureau
report, trade references. **Your books are yours, not theirs.** The skill leads with your payment
experience and asks for the rest. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never sets a limit, places a hold or changes terms in any system.** Every recommendation is a
  proposal for the credit function.
- **Never computes the customer's financial ratios from your own books.** They need the customer's
  statements.
- **Never invents a score, a bureau rating or a policy ceiling.** A missing input is listed as
  missing.
- **No sanctions screening happens here.** The output says so.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–9" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which customer, and which legal entity are you contracting with?* | The contracting entity often differs from the trading name | **Ask again.** Nothing can start without it. |
| **C** | *What is being requested: terms in days, expected monthly volume, currency? Is there a limit today?* | The limit is sized against the request | Assess against current terms and historic volume, and say so. |
| **D** | *Can you supply the customer's financial statements, a credit bureau report or trade references?* | Evidence about the customer is never in your books | Base the assessment on your own payment experience only, and **say that on the face of the output.** |
| **E** | *What is your credit policy: tier ceilings, concentration limit, who approves?* | The recommendation must fit the policy | Recommend a limit with its reasoning, and list the policy check as not run. |
| **F** | *Is the customer covered by credit insurance?* | An insurer's limit is an independent view of the same customer | Assume none, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- **Read the trading history; do not ask for it.** It is the richest input and it is already
  there.
- Check whether the customer appears under several records, and whether they are also a vendor,
  which changes net exposure.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Invoice and payment history** for the customer, with dates | Required for a returning customer | XLSX or CSV |
| **Receivables ageing**, whole ledger | Required for the concentration check | XLSX or CSV |
| Customer's financial statements, bureau report, trade references (D) | Recommended | PDF |
| Credit policy (E) | Recommended | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Reviewing the credit limit for **Harlow Fabrication Ltd**, a customer of **Northbrook Trading**,
> from **your Mosofin connection**. Requested: **net 45**, about **40,000 a month**, current limit
> **60,000**. You supplied their **latest accounts**; no bureau report. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
invoice count and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read your own experience of the customer

Pull the invoices, payments, credit notes and write-offs in one batch, then gather the customer
information: [`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Analyse and score

Ratio analysis where the customer's financials were supplied, your own payment experience, the
qualitative factors, then the score: [`references/method.md`](references/method.md) Steps 2–4,
including Step 2b. Check [`references/edge-cases.md`](references/edge-cases.md) for startups,
group companies, a customer who is also a vendor, a past write-off, stale financials and too few
invoices to measure days-to-pay.

## Stage 5 — Recommend the limit, terms and monitoring, and present

The limit, the terms and conditions, the monitoring triggers, then the output:
[`references/method.md`](references/method.md) Steps 5–8. A limit below current exposure is
flagged, with a path to reach it. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the policy and the scoring method.
An assessment is redone from current data every time, never reused.

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
