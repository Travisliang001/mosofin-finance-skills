---
name: vat-gst-international
description: "Supports VAT and GST across countries: registration obligations, place of supply, output tax on sales, the reverse charge and a check that it nets to nil, input tax on purchases and the effect of partial exemption, special schemes, return preparation, and the reconciliation of the VAT accounts to returns. Reads sales, purchases and the VAT accounts through a connected Mosofin workspace when the user agrees, or works from uploaded data. Use when the user asks about VAT or GST returns, reverse charge, input tax recovery, partial exemption, place of supply, or reconciling the VAT account. Do not use for US sales tax (use sales-tax-us-multistate). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# VAT and GST: output tax, input tax, and the return

VAT is charged on sales and recovered on purchases, and the difference is paid over. Across
borders the question becomes **where** a supply is taxed and **who** accounts for it. This skill
works through output tax, the reverse charge, input tax, and reconciles the VAT accounts to the
return.

**Works with or without Mosofin.** With Mosofin connected sales, purchases and the VAT accounts
are read. Without it, you upload them and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Which supplies are zero-rated or exempt
is the most consequential determination, and it is yours. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system, and files nothing.** Every entry and
  every figure is a proposal.
- **Produces computations and illustrations, not tax advice.** A qualified tax professional
  reviews before anything is filed or acted on.
- **Never supplies a rate, threshold, bracket or rule.** Each comes from the user, with its source
  and its year, and is never carried over from an earlier run.
- **Never decides whether a supply is standard-rated, zero-rated or exempt.**
- **Never decides the place of supply for the user.** It sets out the facts that determine it.
- **Never registers, files or pays.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 1–9" always mean the steps in `references/method.md`.*

Before reading any data, collect what the books cannot tell you, in **one short batch**, not one
question at a time. Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which entity and period, and in which countries are you registered, since when?* | Sets every rule that applies | **Ask again.** Never default the period. |
| **C** | *What are the current rates, thresholds and rules, with their source and year?* | Never built in, never carried forward | **Blocking.** Assemble the figures from the books, and compute no tax. |
| **D** | *Where is the business established, and are there fixed establishments elsewhere?* | Drives registration and place of supply | Treat the home country as the only establishment, and say so. |
| **E** | *Which supplies are zero-rated and which exempt? Is there a partial exemption method?* | Decides output tax and input recovery | Use the tax codes as recorded, and say they were not reviewed. |
| **F** | *Which special schemes are in use, and are there e-invoicing obligations?* | Changes the return | Assume none, and **say that you assumed it.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say how the chart separates countries: one pair of VAT accounts or several.
- Report reverse-charge entries that do not net to nil.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Sales and purchases with tax codes** for the period | Required | XLSX or CSV |
| **VAT account detail** | Required for the reconciliation | XLSX or CSV |
| **Rates and thresholds** with source | Required | PDF or XLSX |
| Returns filed | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing the **Q3 VAT return** workpapers for **Northbrook UK**, registered in **one country
> since 2019**, from **your Mosofin connection**. Rates from **the source you gave**. Zero-rated
> and exempt supplies **as you listed**; no partial exemption; no special schemes. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
country and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Registration and place of supply

The obligations and where each supply is taxed: [`references/method.md`](references/method.md)
Steps 1–2.

## Stage 4 — Output tax, reverse charge and input tax

Output tax, the reverse charge and its net-nil check, input tax and partial exemption, and special
schemes: [`references/method.md`](references/method.md) Steps 3–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for zero-rated against exempt, an invalid
customer VAT number, import VAT and digital services to consumers.

## Stage 5 — Return, reconciliation, and present

Return preparation, the reconciliation, then the output:
[`references/method.md`](references/method.md) Steps 7–9. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the registrations, the
treatment of each supply type and the schemes in use. **No rate is saved.**

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
