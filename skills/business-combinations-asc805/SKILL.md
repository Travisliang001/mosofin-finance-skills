---
name: business-combinations-asc805
description: "Accounts for a business combination under the acquisition method of ASC 805 or IFRS 3: identifies the acquirer and the acquisition date, confirms it is a business and not an asset purchase, measures the consideration, records the identifiable assets and liabilities at the fair values a valuation specialist supplies, computes goodwill or a bargain purchase, builds the proposed acquisition entry, and tracks the measurement period and disclosures. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded deal documents. Use when the user asks about purchase accounting, a purchase price allocation, goodwill on an acquisition, contingent consideration, or ASC 805. Do not use for the group consolidation afterwards (use consolidation-and-eliminations) or for the later impairment test (use goodwill-and-impairment-testing). Read-only: produces the allocation schedule and a proposed entry, and never supplies a fair value."
---

# Business combinations: the acquisition, recorded at fair value

When one business buys another, everything acquired is recorded at **fair value on the acquisition
date**, and what is paid above that is **goodwill**. This skill works through the acquisition
method and builds the proposed entry.

**Works with or without Mosofin.** With Mosofin connected the target's book balances at the
acquisition date and the deal costs are read. Without it, you upload the deal documents and the
method is the same.

**Fair values come from a valuation specialist, and the deal terms from the agreement.** Neither
is in the books. Book values are the starting point, never the answer. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a fair value**, and never uses a book value in its place without saying so.
- **Never decides whether the purchase is a business or a group of assets.** It sets out the test.
- **Never capitalises deal costs into the purchase price.**
- **Never finalises a provisional amount.** The measurement period stays open until the user
  closes it.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–11" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Who bought whom, on exactly which date, and US GAAP or IFRS?* | Everything is measured on that date | **Never default the date.** |
| **C** | *What was paid: cash, shares, contingent amounts?* | The consideration | **Ask again.** |
| **D** | *Do you have the valuation report for the assets, liabilities and intangibles?* | Fair values are never computed here | **Blocking.** Lay out the schedule at book values, marked provisional. |
| **E** | *Was less than 100% bought, or was an interest already held?* | Changes the goodwill computation | Assume a 100% purchase with no prior interest, and **say that you assumed it.** |
| **F** | *Is there an earnout, and how is it classified?* | Decides later remeasurement | Assume none, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Say whether the acquired business is a connected company file. That decides whether its balances
  can be read.
- Report deal-related legal and advisory costs found in the books.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Purchase agreement**, or a summary of terms | Required | PDF |
| **Valuation report** | Required | PDF |
| **Target's balance sheet** at the acquisition date | Required | XLSX |
| Deal cost invoices | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Accounting for the purchase of **100% of Harlow Fabrication** by **Northbrook Trading** on **1
> July**, under **US GAAP**, for **cash plus an earnout**, from **the agreement and valuation
> report you uploaded** and balances in **your Mosofin connection**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the parties, the
date and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the books, identify the acquirer and confirm it is a business

Pull the balances, then the acquirer, the date and the business test:
[`references/method.md`](references/method.md) Steps 0–2.

## Stage 4 — Consideration, fair values and goodwill

The consideration, the assets and liabilities at fair value, then goodwill:
[`references/method.md`](references/method.md) Steps 3–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for an asset purchase, a reverse
acquisition, contingent consideration and a bargain purchase.

## Stage 5 — Entry, measurement period, disclosures, and present

The acquisition entry as a **proposal**, the measurement period, later accounting and disclosures,
then the output: [`references/method.md`](references/method.md) Steps 6–10. Before presenting,
check it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 11. Persist the deal terms and the measurement
period end date.

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
