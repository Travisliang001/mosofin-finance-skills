---
name: inventory-obsolescence-and-reserve
description: "Finds excess, slow-moving and obsolete inventory and sizes the reserve: movement by item, days on hand, every item with no sales or usage in a set number of days, the lower of cost and net realisable value test, the reserve by ageing bucket, a roll-forward tied to the ledger, and the proposed entry. Derives reserve rates from what past slow stock actually realised where the history allows. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded stock listing and movement history. Use when the user asks about obsolete or slow-moving stock, an inventory reserve or write-down, excess inventory, net realisable value, or dead stock. Do not use for reconciling inventory to the ledger (use inventory-to-gl-reconciliation) or for freeing cash from stock levels (use working-capital-optimization). Read-only: produces the analysis, a proposed entry and a coverage sheet, and posts nothing."
---

# Inventory reserve: stock that will not sell for what it cost

Stock is recorded at cost, but some of it will never sell for that: it is out of date, there is
too much of it, or nobody has wanted it for two years. This skill finds that stock, tests it
against **net realisable value**, sizes the **reserve**, and proposes the entry. A person posts
it.

**Works with or without Mosofin.** With Mosofin connected, movement by item, days on hand, recent
selling prices and the reserve balance are all read. Without it, you upload the stock listing and
the movement history and the method is the same.

**Two things are never in the books.** The **condition** of the stock: damaged, expired or
quarantined items are invisible unless you say so. And the **demand forecast**: without it, excess
is measured against history, not the plan. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** The reserve entry is a proposal.
- **Never treats no movement as obsolete on its own.** Seasonal, end-of-life and customer-specific
  stock are checked first.
- **Never reserves the same item twice**, once as slow-moving and again as below cost.
- **Never assumes a reserve rate without saying so.** The policy is the user's; a derived rate is
  shown as a proposal.

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
| **B** | *Which company, and as at what date?* | Sets every read and the ageing | **Never default the date.** |
| **C** | *What are your ageing buckets and reserve rates, and which costing method do you report under?* | The policy decides the reserve | Propose buckets and rates derived from history, and **wait for a yes.** |
| **D** | *Is any stock known to be damaged, expired or quarantined?* | Condition is invisible in the books | Assume none, and **say that you assumed it.** |
| **E** | *Which items need special handling: seasonal, end-of-life, made for one customer?* | Prevents false alarms in the no-movement list | Flag every no-movement item, and say none were excluded. |
| **F** | *Do you have a demand forecast, and what are the write-off approval limits?* | Excess against plan needs the plan | Measure excess against past usage only, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Check whether the system tracks lots and dates. Where it does not, the ageing rests on a proxy,
  and the output says which.
- Confirm the costing method the system uses against the one reported.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Stock listing**: item, quantity, cost, location, and lot or date where held | Required | XLSX or CSV |
| **Movement history**: sales and usage by item by month, 12 months or more | Required | XLSX or CSV |
| **Recent selling prices** by item | Required for the net realisable value test | XLSX or CSV |
| **Reserve account detail** for the period | Required for the roll-forward | XLSX or CSV |
| Policy (C), condition (D), special items (E), forecast (F) | C required, the rest recommended | Type it in the chat, or XLSX |

**Read back before starting, then wait for a yes:**

> *Assessing inventory for **Northbrook Trading** at **30 September**, from **your Mosofin
> connection**. Buckets **0–90, 91–180, 181–365 and over 365 days**, rates as in your policy,
> **weighted average cost**. **Two pallets quarantined**, as you listed. No forecast supplied.
> Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
item count and the total value. Flag anything unreadable straight away.

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

## Stage 3 — Read the stock and settle the policy

Pull the item list, the movement history, selling prices and the reserve account in one batch,
then settle the reserve policy: [`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Find slow and excess stock, and test value

Identify slow-moving and excess items, then run the net realisable value test:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for a last-purchase date used as an ageing
proxy, double counting, raw materials whose own price fell, and usage measured over the wrong
window.

## Stage 5 — Size the reserve, propose the entry, and present

Quantify the reserve, propose the entry and the roll-forward, the disclosures, then the output:
[`references/method.md`](references/method.md) Steps 4–7. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the buckets, the rates, the
special-handling list and the costing method. Quantities and values are read again every run.

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
