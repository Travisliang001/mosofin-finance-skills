---
name: sales-tax-us-multistate
description: "Supports US sales and use tax across states: joins sales by state from the books to the thresholds and registration status the user supplies to show where there is exposure, then works through registration, taxability, rates, exemptions, use tax, return preparation, the reconciliation of the liability account to returns, and marketplace sales. Reads sales by ship-to state through a connected Mosofin workspace when the user agrees, or works from uploaded sales data. Use when the user asks about sales tax nexus, which states they should be registered in, use tax on purchases, reconciling sales tax payable to returns, or exemption certificates. Do not use for VAT or GST (use vat-gst-international). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing."
---

# US sales tax: where you owe it, and whether it reconciles

A business owes sales tax in a state once it has **nexus** there, by presence or by volume of
sales. This skill shows sales by state against the thresholds you supply, flags states with sales
and no registration, and reconciles what was collected to what was filed.

**Works with or without Mosofin.** With Mosofin connected sales by ship-to state and the tax
liability account are read. Without it, you upload the sales data and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** Registration status, physical presence,
taxability decisions and exemption certificates all come from you. Background:
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
- **Never concludes that nexus exists.** It shows sales against the threshold supplied and names
  the states to review.
- **Never decides whether a product is taxable.**
- **Never registers, files or remits.**

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
| **B** | *Which entity and period?* | Sets the sales read | **Never default the period.** |
| **C** | *In which states are you registered, since when, and where do you have physical presence?* | The join that turns sales into exposure | Show sales by state only, with no exposure view. |
| **D** | *What are the current economic nexus thresholds and rates, or which tax engine do you use?* | Never built in | **Blocking** for any threshold test or rate check. |
| **E** | *What do you sell, and which items have you determined to be taxable or exempt?* | Taxability is a determination | Treat taxability as recorded in the books, and say so. |
| **F** | *Which exemption certificates are on file, and which marketplaces do you sell through?* | Both reduce what you must collect | List exempt sales as unsupported, and marketplace sales as not separated. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report states with sales and no registration on your list.
- Report purchases with no tax charged, as candidates for use tax.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Sales by ship-to state**, with tax collected | Required | XLSX or CSV |
| **Registration list** with dates | Required | XLSX, or type it in the chat |
| **Thresholds and rates** with source | Required | PDF or XLSX |
| Returns filed and exemption certificate register | Recommended | PDF or XLSX |

**Read back before starting, then wait for a yes:**

> *Reviewing sales tax for **Northbrook Trading** for **2025**, with sales by state from **your
> Mosofin connection**. Registered in **four states**, as listed; thresholds from **the source you
> gave, for 2025**. Rates applied by **your tax engine**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
states and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Nexus and the exposure join

Sales by state against thresholds and registrations:
[`references/method.md`](references/method.md) Steps 1–1b.

## Stage 4 — Registration, taxability, rates, exemptions and use tax

The obligations and determinations as supplied: [`references/method.md`](references/method.md)
Steps 2–6. Check [`references/edge-cases.md`](references/edge-cases.md) for inventory in
third-party warehouses, crossing a threshold mid-year, bundled sales, software and digital
products, and drop-shipping.

## Stage 5 — Returns, reconciliation, marketplaces, and present

Return preparation, the reconciliation, marketplace sales, then the output:
[`references/method.md`](references/method.md) Steps 7–10. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md). Ask whether the user wants
the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the registration list
and the certificate register. **No threshold or rate is saved.**

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
