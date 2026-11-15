---
name: aml-kyc-procedures
description: "Supports the design and documentation of an anti-money-laundering and know-your-customer programme: frames the regulatory context the user states, sets up the risk-based approach, customer due diligence and enhanced due diligence, records screening done on the user's own tool, describes ongoing monitoring of transactions in the books, and sets out escalation to the responsible officer. Reads transaction activity through a connected Mosofin workspace when the user agrees, or works from uploaded customer and transaction data. Use when the user asks about AML or KYC procedures, customer due diligence, risk rating customers, beneficial ownership, transaction monitoring rules, or documenting an AML programme. Do not use for fraud red-flag testing (use fraud-detection-and-forensics) or for vendor tax forms (use vendor-onboarding-and-w9-tin). Read-only: produces framework documents and review lists for the responsible officer, is not legal or compliance advice, screens no one and files nothing."
---

# AML and KYC: knowing who you are dealing with

Businesses in regulated sectors must know who they are dealing with, check them against official
lists, watch for unusual activity, and report suspicion. This skill builds the **framework and
documentation** for a risk-based programme, and prepares review lists for the **responsible
officer**. It does not make compliance decisions.

**Works with or without Mosofin.** With Mosofin connected it reads customer transaction activity
for the monitoring step. Without it, you upload the activity and the method is the same.

**This is support for a compliance function, not legal or compliance advice.** The regime that
applies, identity and ownership evidence, and screening on your own tool all come from you. **A
qualified person decides what is suspicious and what is filed.** Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.**
- **Never performs sanctions, PEP or adverse-media screening.** It records the tool used, the date
  and the result supplied.
- **Never decides that activity is suspicious, and never drafts a filing as final.** It refers to
  the responsible officer by name.
- **Never tips off.** Nothing in the output is written for the customer, and nothing suggests
  contacting them.
- **Never states a legal threshold or requirement from memory as settled.** The user confirms the
  regime.
- **Never saves identity or screening data.**

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–10" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which entity, and under which jurisdictions and regulatory regime?* | Never inferred from the country on record | **Ask again.** |
| **C** | *What products or services are offered?* | Decides whether the entity is covered at all | **Ask again.** |
| **D** | *Who is the responsible officer, by name and role?* | Every escalation goes to a person | **Blocking** for any review list. |
| **E** | *Is there an existing AML policy, and which screening tool do you use?* | Build on it, do not replace it | Draft a framework outline only, and list screening as not evidenced. |
| **F** | *Is monitoring in scope, and for which period?* | Sets the transaction read | Skip monitoring, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say what sits outside the books: identity documents, ownership evidence and screening results.
- Confirm who may see the output. It concerns identifiable people.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Existing AML policy** | Recommended | PDF |
| **Customer list** with risk attributes | Required for risk rating | XLSX |
| **Transaction activity** for the period | Required for monitoring | XLSX or CSV |
| Screening results from your tool | Required to record screening | PDF or CSV |

**Read back before starting, then wait for a yes:**

> *Documenting the AML programme for **Northbrook Payments**, regulated in **the regime you
> named**, offering **payment services**, with transaction activity from **your Mosofin
> connection** for **Q3**. Responsible officer: **the compliance lead you named**. Screening on
> **your own tool**. Output to **the officer only**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
record counts. Flag anything unreadable straight away.

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

## Stage 3 — Read the activity and frame the context

Pull transaction activity, then the regulatory context and the risk-based approach:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Due diligence, screening and monitoring

Customer and enhanced due diligence, the record of screening, and ongoing monitoring:
[`references/method.md`](references/method.md) Steps 3–6. Check
[`references/edge-cases.md`](references/edge-cases.md) for strict-liability sanctions, opaque
ownership, structuring and tipping off.

## Stage 5 — Escalation, records, and present

Escalation to the responsible officer, recordkeeping and governance, then the output:
[`references/method.md`](references/method.md) Steps 7–9. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 10. Persist the regime, the risk-rating method
and the monitoring rules. **No identity, ownership or screening data is saved.**

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
