---
name: 1099-and-t4a-prep
description: "Prepares the population for information returns such as 1099s in the US or T4As in Canada: builds the list of reportable vendors from the year's payments, classifies payments to the right form and box on the rules the user supplies, validates the fields each form needs, reconciles the totals to the ledger, produces the filing list, and flags vendors with no tax form on file. Reads vendors and payments through a connected Mosofin workspace when the user agrees, or works from uploaded payment data. Use when the user asks to prepare 1099s or T4As, find which vendors need an information return, check for missing W-9s before year-end, or reconcile reportable payments. Do not use for auditing the vendor master in general (use vendor-onboarding-and-w9-tin) or for payroll forms (use payroll-tax-filings). Read-only: produces workpapers for a qualified professional to review, is not tax advice, and files nothing. Masks tax identifiers wherever it can."
---

# 1099 and T4A preparation: who must be reported, and for how much

Each year a business reports what it paid to contractors and certain other payees. The work is
mostly finding out **who is reportable, for how much, on which form**, and whether the details
needed are on file. This skill builds that list from the year's payments.

**Works with or without Mosofin.** With Mosofin connected the vendors and every payment in the
year are read. Without it, you upload the payment data and the method is the same.

**Rates and rules are never built in.** Tax law differs by place and changes every year, so every
rate, threshold and rule comes from you with its source and year. **The output is a computation
for a qualified tax professional to review, not advice.** The vendor's own tax form is usually the
missing piece. **Tax identifiers are shown masked wherever the task allows.** Background:
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
- **Never decides that a payee is or is not reportable where the rule is unclear.** It lists them
  for review.
- **Never displays a full tax identifier where a masked one will do**, and saves none.
- **Never files or issues a form.**

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
| **B** | *Which payer, which country's regime, and which reporting year, with exact dates?* | Never defaulted | **Ask again.** |
| **C** | *Which forms are in scope, and what are the reporting thresholds for that year, with source?* | Never built in | **Blocking.** List payments by vendor, with no reportable flag. |
| **D** | *Which vendor tax forms are on file?* | Usually the missing piece | Flag every paid vendor as form not evidenced. |
| **E** | *How were payments made: card and third-party network payments are often reported by others?* | Avoids double reporting | Include all payment methods, and say they were not separated. |
| **F** | *What filing channel will be used, and were payments made in more than one currency?* | Affects format and conversion | Produce the list in a plain table, in the currency paid. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report vendors paid above the threshold supplied with no tax form recorded, ranked by amount.
- Confirm who may see the output.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Payments by vendor** for the year, with method | Required | XLSX or CSV |
| **Vendor list** with entity type and form status | Required | XLSX or CSV |
| **Thresholds and form rules** with source | Required | PDF |
| Vendor tax forms | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Preparing the **2025 1099 list** for **Northbrook Trading**, a **US** payer, for **1 January to
> 31 December 2025**, from **your Mosofin connection**. Forms **1099-NEC and 1099-MISC**;
> thresholds from **the source you gave, for 2025**. Card payments excluded. Identifiers masked.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the year, the
vendor count and the totals. Do not repeat an identifier back in full. Flag anything unreadable
straight away.

**Then validate the upload before any work, every time.** For each file: is it the right kind of
document, for the right company and period, usable, and necessary for this skill? Give a verdict
per file, list what is still missing, and wait for the user's answer. Full wording:
[`references/mosofin-protocol.md`](references/mosofin-protocol.md), *After an upload, validate the
input before any work*.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, and read the company profile, so Stage 1's
answers do not need asking twice. On the upload path, go straight to Stage 3.

## Stage 3 — Read payments and build the reportable list

Pull vendors and payments, then the list of reportable vendors:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Classify, validate and reconcile

Payments to form and box, the required fields, then the reconciliation:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for a vendor who refuses a form, mixed
payment types to one vendor, payments through a third-party processor and cross-border vendors.

## Stage 5 — Filing list, under-documented payees, and present

The filing list, backup withholding and under-documented payees, then the output:
[`references/method.md`](references/method.md) Steps 5–7. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the form mapping by account and
vendor type. **No threshold and no identifier is saved.**

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
