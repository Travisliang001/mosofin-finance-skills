---
name: vendor-onboarding-and-w9-tin
description: "Audits the vendor master and supports onboarding of new vendors: measures completeness weighted by what each vendor is actually paid, detects changes to bank details, finds duplicate vendors and vendors that are also customers or related parties, then sets out the documents to collect and the tax-form validation for the payer's jurisdiction, such as a W-9 or W-8 in the US. Reads vendor and payment records through a connected Mosofin workspace when the user agrees, or works from an uploaded vendor list. Use when the user asks to audit the vendor master, onboard a vendor, check for missing tax forms before year-end, detect bank detail changes, or find duplicate vendors. Do not use for matching invoices (use three-way-match) or for duplicate payments (use duplicate-invoice-detection). Read-only: changes no vendor record, and masks bank and tax identifiers wherever the analysis allows."
---

# Vendor master: who you pay, and what you hold on them

Two jobs. **Onboarding a new vendor** is document work: a tax form, a bank letter, a registration
certificate. **Auditing the vendor master** is a read of what is already recorded: who is missing
a tax form, whose bank details changed, who appears twice. This skill does the second from the
books and sets out the first.

**Works with or without Mosofin.** With Mosofin connected it reads the vendor records and what
each vendor was paid, so gaps are ranked by money at risk. Without it, you upload the vendor list
and the method is the same.

**The documents are never in the accounting system**, and neither is sanctions screening, which is
run by you on your own service. **This skill handles bank and tax identifiers.** It reads what is
recorded, reproduces them nowhere outside the deliverable, and works on masked or partial
identifiers wherever it can. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never creates, edits or deactivates a vendor**, and never changes bank details.
- **Never displays a full bank account number or tax identifier where a masked one will do.**
- **Never performs or claims a sanctions screen.** It records who ran it and when.
- **Never treats a bank detail change as fraud.** It is reported for verification by call-back.
- **Gives no tax advice.** Withholding rules are the user's or their adviser's to confirm.

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
| **B** | *Which company, and is this an audit of the vendor master, onboarding of new vendors, or both?* | The two halves use different inputs | Run the audit, and say so. |
| **C** | *What is the payer's jurisdiction?* | It determines every validation rule | **Ask again.** |
| **D** | *What does your onboarding policy require: documents, form expiry, a threshold for one-time payees?* | The standard gaps are measured against | Report what is recorded, with no pass or fail. |
| **E** | *Who runs sanctions screening, on what service?* | Never done here | List screening as not evidenced. |
| **F** | *Does the system record changes to vendor records, and who can edit vendors?* | Needed to detect bank detail changes | List change detection as not run, and say why. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report actively paid vendors with no tax form on record, ranked by amount paid.
- Confirm who may see the output before producing it. It holds bank and tax identifiers.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Vendor list**: name, address, tax identifier status, terms | Required | XLSX or CSV |
| **Payments by vendor** for the year | Required to rank the gaps | XLSX or CSV |
| **Tax forms** for vendors being onboarded | Required for onboarding | PDF |
| Onboarding policy | Recommended | PDF, or type it in the chat |

**Read back before starting, then wait for a yes:**

> *Auditing the vendor master of **Northbrook Trading**, a **US** payer, from **your Mosofin
> connection**, against **the onboarding policy you uploaded**. Screening is run by **your
> compliance team**. Output to **you and the AP manager only**, identifiers masked. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the vendor count
and the period. Do not repeat an identifier back in full. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Audit the vendor master

Completeness, completeness weighted by payments, bank detail changes, duplicates and related
parties: [`references/method.md`](references/method.md) Step 0 and its parts.

## Stage 4 — Onboard and validate

The form type, the fields and their validation for the jurisdiction:
[`references/method.md`](references/method.md) Steps 1–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a vendor who refuses a form, a sole
proprietor, a change of legal name and a vendor in a sanctioned country.

## Stage 5 — Screening record, bank verification, set-up, and present

The record of screening, bank-detail verification by call-back, terms and classification, then the
output: [`references/method.md`](references/method.md) Steps 4–8. Before presenting, check the
coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether the
user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the jurisdiction and
the onboarding policy. **No bank detail or tax identifier is saved.**

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
