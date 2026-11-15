---
name: real-estate-and-property-accounting
description: "Accounts for real estate held as investment property, owner-occupied property or property under development: reads what each property has actually done before classifying it, sets initial measurement including capitalised interest, applies the cost or fair value model, handles rental income on the lessor side, sales, impairment indicators and disclosures. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded property schedules. Use when the user asks about investment property, capitalising development costs or interest, land and building allocation, straight-lining rent as a landlord, a property sale, or IAS 40. Do not use for leases as a tenant (use lease-accounting-asc842-ifrs16) or for other fixed assets (use fixed-asset-register-and-depreciation). Read-only: produces the schedules and proposed entries, and never supplies a valuation."
---

# Property accounting: what each property is, and what it does

Property is accounted for by **what it is used for**: held to earn rent, occupied by the business,
or under development. The framework matters too, since IFRS has a separate investment property
category with a fair value option and US GAAP does not. This skill classifies each property,
measures it and proposes the entries.

**Works with or without Mosofin.** With Mosofin connected it reads what has been posted to each
property and **what each property has actually earned and cost**, which tests the classification
stated. Without it, you upload the property schedules and the method is the same.

**Valuations, lease terms and the land and building split are not in the books.** A fair value
comes from a valuer, the rent terms from the lease, and the intended use from you. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a fair value or a valuation input.**
- **Never picks the measurement model.** Under IFRS the election is the user's and close to
  irreversible.
- **Never classifies a property against how it actually behaves without saying so.**
- **Never concludes on impairment.** It lists the indicators.

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
| **B** | *Which company and period, and US GAAP or IFRS?* | The framework governs everything | **Ask again.** Never default the period. |
| **C** | *What is each property used for: rented out, occupied, under development, held for sale?* | Decides classification | Show what each property earned and cost, and ask. |
| **D** | *Under IFRS, cost model or fair value model for investment property? Do you have valuations?* | An election, and a valuer's figure | Use the cost model as recorded, and say so. |
| **E** | *How was the price split between land and buildings, and on what basis?* | Land is not depreciated | Use the split in the books, and list the basis as not supplied. |
| **F** | *What are the lease terms for tenanted property: term, escalations, rent-free periods, incentives?* | The books have the cash, not the contract | Report rent as billed, with no straight-lining. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report, per property, the rent earned and the costs posted, before the interview.
- Report costs capitalised to a property after it came into use.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Property schedule**: cost, date, use, land and building split | Required | XLSX |
| **Ledger detail** for the property accounts and rental income | Required | XLSX or CSV |
| **Tenant leases**, or a summary of terms | Required for rental income | PDF or XLSX |
| Valuations | Required for the fair value model | PDF |

**Read back before starting, then wait for a yes:**

> *Accounting for **three properties** of **Northbrook Trading** for the **year to 31 December**
> under **US GAAP**, from **your Mosofin connection**. **Two rented out, one occupied.** Land and
> building split as in the books; lease terms from **the schedule you uploaded**. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the property, the
period and the totals. Flag anything unreadable straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, check which read tools are enabled, read the saved profile, and interview only for
what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Read the property position and classify

What each property has done, then its classification:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Measure, at the start and afterwards

Initial measurement including capitalised interest, then subsequent measurement:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for component depreciation, mixed-use
property, transfers between classifications and held-for-sale criteria.

## Stage 5 — Rental income, sales, impairment, and present

Rental income, sales, impairment indicators and disclosures, with entries as **proposals**, then
the output: [`references/method.md`](references/method.md) Steps 4–8. Before presenting, check the
coverage and provenance sheet in [`references/output.md`](references/output.md). Ask whether the
user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist each property's
classification, the measurement model and the land and building split.

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
