---
name: bad-debt-and-write-offs
description: "Assesses whether receivables will be collected: derives loss rates from the business's own history, identifies specific write-off candidates, computes the allowance for doubtful accounts under the framework the user names (CECL, IFRS 9 expected credit loss, or an aged-percentage method), works out the adjustment to the existing allowance, and proposes the entries with the roll-forward. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded ageing and write-off history. Use when the user asks about bad debt, the allowance for doubtful accounts, expected credit losses, a bad debt reserve, writing off a receivable, or recovering a written-off balance. Do not use for chasing overdue invoices (use ar-aging-and-collections) or for setting a customer's credit limit (use credit-limit-and-customer-risk). Read-only: proposes entries for a person to approve and post, and writes off nothing."
---

# Bad debt: the allowance, and the write-offs

Some customers never pay. Accounting handles that in two stages. An **allowance** sets aside an
estimate for what probably will not be collected. A **write-off** removes one customer's balance
once it is certain. This skill computes the first, identifies candidates for the second, and
keeps the roll-forward that shows they agree. A person approves and posts.

**Works with or without Mosofin.** With Mosofin connected the loss rates come from your own
history: past ageings against what was later written off. Without it, you upload the ageing and
the write-off history and the method is the same.

**The books do not know why a customer is not paying.** An insolvency filing, a dispute and a
forecast of economic conditions are never in an accounting system. Age alone is never treated as
proof that a balance is lost. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal, and no
  balance is written off by this skill.
- **Never picks the reporting framework**, and never infers it from the country.
- **Never assumes a loss rate.** Rates come from history, or are stated as the user's.
- **Never proposes a write-off without the approval authority named**, and never claims tax relief
  that has not been confirmed.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–7" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company, and which period end?* | Sets the ageing date and every read | **Never default the period.** |
| **C** | *Which framework: US GAAP (CECL), IFRS 9, or local GAAP with an aged-percentage method?* | Decides the whole method | **Ask again.** The skill does not pick. |
| **D** | *Do you know of any customer in insolvency, in dispute, or with a changed credit position?* | The books cannot see this | Flag candidates by age and history only, and **say none were confirmed.** |
| **E** | *Who may approve a write-off, and up to what amount?* | A write-off without approval is just a loss | Compute the allowance, and list specific write-offs as candidates only. |
| **F** | *Under CECL or IFRS 9: what forward-looking view applies? And which tax jurisdiction?* | The forecast is yours; tax relief differs by country | Apply historical rates with no forward adjustment and no tax entry, and say so. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- Find the allowance, bad debt expense and recovery accounts, and **confirm them by name.**
- Say how many years of loss history can be derived.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Receivables ageing by customer** at the period end | Required | XLSX or CSV |
| **Write-offs and recoveries**, three to five years, by ageing bucket where possible | Required for CECL and IFRS 9, recommended otherwise | XLSX or CSV |
| **Allowance account detail** for the period | Required for the adjustment | XLSX or CSV |
| Framework (C), customer information (D), approval limits (E) | C required | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Computing the allowance for **Northbrook Trading** at **30 September** under **IFRS 9**, from
> **your Mosofin connection**, with loss rates from **four years** of history. **One customer in
> administration**, as you told me. Write-offs up to **10,000** are approved by the finance
> director. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the date, the
customer count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the evidence and choose the method

Pull the ageing, the allowance account and the write-off history in one batch, then settle the
methodology for the framework given: [`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Identify write-off candidates and compute the allowance

Specific candidates first, then the allowance on the rest:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for no loss history, a customer in
insolvency with a possible dividend, disputed and intercompany balances, government customers and
foreign currency.

## Stage 5 — Compute the adjustment, propose entries, and present

The adjustment to the existing allowance, the entries as **proposals**, then the output with the
roll-forward: [`references/method.md`](references/method.md) Steps 4–6. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the framework, the method, the
account mapping and the approval matrix. Balances and rates are derived again every period.

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
