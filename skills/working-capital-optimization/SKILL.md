---
name: working-capital-optimization
description: "Finds the cash tied up in receivables, inventory and payables: the cash conversion cycle month by month, growth separated from seasonality and from real deterioration, where collection is slow, where stock is stuck, which bills are paid early, and each lever sized in days and cash next to the trade-off it carries. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded balance sheets, ageing reports and payment history. Use when the user asks to optimise working capital, improve the cash conversion cycle, reduce DSO or DIO, extend DPO, free up cash from operations, find where cash is trapped, or check whether suppliers are paid early. Do not use for a weekly cash forecast (use cash-flow-forecast-13-week) or for chasing overdue invoices (use ar-aging-and-collections). Read-only: produces a diagnostic, a sized plan and a coverage sheet, changes no terms and contacts no one."
---

# Working capital: where the cash is trapped

Measures the cash a business has tied up in **receivables, inventory and payables**, and shows how
to release it. It computes the **cash conversion cycle** month by month, separates growth and
seasonality from real deterioration, diagnoses each component, then sizes every lever in days and
cash. A person decides which levers to pull.

**Works with or without Mosofin.** With Mosofin connected it reads the monthly balances, the
invoice-to-payment timing and the vendor payment history directly, so the diagnostic is measured,
not estimated. Without it, you upload the same history and the method is the same.

**The benefit of a lever can be computed. Its cost usually cannot.** Stretching a supplier by
fifteen days gives a precise cash figure; the damaged relationship appears in no ledger. So every
sized lever is shown beside its trade-off, and a missing number on the cost side never reads as no
cost. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never changes data, payment terms or credit limits in any system, and never contacts a
  customer or supplier.** Every lever is a proposal for a person to act on.
- **Never shows an opportunity figure without its trade-off.** The goal is optimisation, not
  maximisation.
- **Never invents a benchmark or a days target.** With none given, it compares the business to its
  own history and says so.

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
| **B** | *Which company, and how far back? Twenty-four months or more is best.* | Seasonality and trend need two full years | Use the longest history available and **say how long it is.** |
| **C** | *What payment terms did you agree with customers and with suppliers, including the exceptions?* | Recorded terms and agreed terms differ, and the gap is the diagnostic | Compare against the recorded terms only, and say so. |
| **D** | *Which relationships are off limits, and which service levels must hold?* | These are the guardrails every lever is tested against | **Ask again before recommending anything about a supplier.** Until then, list counterparty-facing levers as not reviewed. |
| **E** | *What is your cost of capital?* | Turns days released into a value | Size each lever in days and cash only. |
| **F** | *Do you have industry benchmarks for DSO, DIO and DPO?* | External data, never in the books | Use the business's own history. **Never supply a benchmark.** |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- At Gate 2, answer the **one capability question** that shapes the inventory work: does the
  system hold inventory at item level, with quantities and movement dates, or only as a value?
  **Say which** before promising an inventory diagnostic.
- Run the diagnostic read before the rest of the interview. *"Your DSO is 52 days, of which 9 are
  invoicing delay"* is a better question than *"how are collections?"*

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Monthly balance sheets**, 24 months or more: receivables, inventory, payables, accruals | Required | XLSX or CSV |
| **Monthly revenue and cost of sales** for the same months | Required | XLSX or CSV |
| **Receivables detail** with invoice dates and payment dates | Required | XLSX or CSV |
| **Payables detail** by vendor, with terms and payment dates | Required | XLSX or CSV |
| **Inventory detail** by category or SKU, with quantities and last movement | **Required for the inventory diagnostic.** Without it that section is value-only and says so | XLSX or CSV |
| Agreed terms (C), guardrails (D), cost of capital (E), benchmarks (F) | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Assessing working capital for **Northbrook Trading** over **30 months to September**, from
> **your Mosofin connection**. Inventory is held **at item level**. Customer terms **30 days**,
> supplier terms **as recorded**, no benchmarks supplied. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the months it
covers, the row count and the totals. Flag anything unreadable, or a gap in the monthly series,
straight away.

---

## Stage 2 — Confirm scope and capabilities *(Mosofin path only)*

Run Gates 0–3 in [`references/gates.md`](references/gates.md). They confirm the workspace and the
company file, answer the inventory capability question, read the company profile, and interview
only for what Stage 1 did not cover. On the upload path, go straight to Stage 3.

## Stage 3 — Diagnose the cycle and its three components

Compute DSO, DIO, DPO and the cash conversion cycle for every month, then split each movement into
volume, seasonality and deterioration. Then diagnose receivables, inventory and payables in turn:
[`references/method.md`](references/method.md) Steps 1–4. Use the monthly series, never a single
period-end balance.

## Stage 4 — Size the levers, then test them against the trade-offs

List the levers per component, size each in days and cash, and rank them:
[`references/method.md`](references/method.md) Steps 5–7. **Complete the trade-off step before
presenting any figure.** Check [`references/edge-cases.md`](references/edge-cases.md) for
over-stretched suppliers, lost sales from stock cuts, seasonal businesses, one-off collection
pushes and the real cost of factoring.

## Stage 5 — Build the roadmap and present the result

Roadmap with owners and measured baselines, KPIs with guardrails, then the twelve sheets:
[`references/method.md`](references/method.md) Steps 8–10. Before presenting, check the coverage
and provenance sheet in [`references/output.md`](references/output.md): what was measured, what was
not and why. Ask whether the user wants the workbook as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md), *Seed to evolved*. Persist the measured baseline,
the agreed terms, the guardrails and the levers already declined. Never persist the capability map,
which Gate 2 reads fresh each run.

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
