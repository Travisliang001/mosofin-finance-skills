---
name: inventory-costing-fifo-lifo-wavg
description: "Applies an inventory costing method to compute ending inventory and cost of goods sold: establishes which method the accounting system itself applies, confirms the method is allowed under the framework, sets the cost basis, builds the FIFO or LIFO layers or the weighted average, tests the lower of cost and net realisable value, proposes the period-end entries, and compares methods where that helps. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded purchase and sales history. Use when the user asks about FIFO, LIFO, weighted-average or specific identification, cost of goods sold, inventory layers, a costing method change, or valuing ending inventory. Do not use for slow or obsolete stock (use inventory-obsolescence-and-reserve), for tying inventory to the ledger (use inventory-to-gl-reconciliation) or for standard cost variances (use standard-costing-and-variance-analysis). Read-only: produces the costing and proposed entries, and posts nothing."
---

# Inventory costing: which cost belongs to what was sold

If the same item was bought three times at three prices and two were sold, which price was the
cost of the sale? There is no physically correct answer, so there are conventions: **FIFO, LIFO,
weighted average, specific identification**. This skill applies the one you use, and computes
**ending inventory and cost of goods sold**.

**Works with or without Mosofin.** With Mosofin connected it reads purchases and sales by item
where the system holds line detail, and establishes **which method the system itself applies**.
Without it, you upload the history and the method is the same.

**The method on record and the method reported can differ.** The opening layers, the costs to
complete and sell, and how freight and duties are allocated are not in the books and come from
you. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never picks the costing method**, and never applies LIFO under IFRS.
- **Never rebuilds opening layers by assumption.** Without them, layer-based costing starts from
  what the user supplies.
- **Never reports a method comparison as a recommendation to change.**

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
| **B** | *Which company and period?* | Sets every read | **Never default the period.** |
| **C** | *Which method do you report under, and US GAAP or IFRS?* | Decides eligibility and the value test | **Ask again.** |
| **D** | *Is the system periodic or perpetual, and is standard costing in use?* | Changes the whole computation | Read whether cost of sales posts per sale, and confirm. |
| **E** | *What are the opening quantities and layers, and which costs are included: freight, duties, conversion?* | The balance is in the books; the layers are not | Use weighted average on the opening balance, and **say that layers were not supplied.** |
| **F** | *What are the costs to complete and sell, for the value test?* | Net realisable value needs them | Compare cost with recent selling prices only, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say which method the accounting system applies, and whether it matches the method reported.
- Say whether line-level purchase and sales detail by item is available, or values only.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Purchases by item**: date, quantity, unit cost | Required | XLSX or CSV |
| **Sales or issues by item**: date, quantity | Required | XLSX or CSV |
| **Opening inventory**: quantity and cost, or layers | Required | XLSX |
| Selling prices and costs to complete and sell | Recommended, for the value test | XLSX |

**Read back before starting, then wait for a yes:**

> *Costing inventory for **Northbrook Trading** for **September** under **FIFO** and **US GAAP**,
> from **your Mosofin connection**. The system is **perpetual** and applies **average cost**,
> which differs from the method reported. Opening layers from **the file you uploaded**. Shall I
> go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
item count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the transactions and establish the system's method

Pull purchases, sales and items, establish the method the system applies, then confirm eligibility
and consistency: [`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Cost basis, method and cost flow

The cost basis, the costing method and the cost flow:
[`references/method.md`](references/method.md) Steps 2–4. Check
[`references/edge-cases.md`](references/edge-cases.md) for periodic against perpetual differences,
a LIFO liquidation, consigned and in-transit stock, and standard costing.

## Stage 5 — Value test, entries, comparison, and present

Lower of cost and net realisable value, the period-end entries as **proposals**, the method
comparison, then the output: [`references/method.md`](references/method.md) Steps 5–8. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 9. Persist the method, the cost components
included and the closing layers, with their date.

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
