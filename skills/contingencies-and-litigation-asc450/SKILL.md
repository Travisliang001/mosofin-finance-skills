---
name: contingencies-and-litigation-asc450
description: "Evaluates and accounts for contingencies such as litigation, claims, assessments and warranties under ASC 450 or IAS 37: sweeps the books for legal spend and settlements that point to matters missing from the list, classifies each matter on the likelihood and estimate management supplies, sets out the treatment, measures the accrual and proposes the entry, and drafts the disclosure for legal review. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded matter list and ledger detail. Use when the user asks about a loss contingency, a litigation accrual, a legal reserve, a warranty provision, or contingent liability disclosure. Do not use for general period-end accruals (use accruals-and-deferrals) or for events after year-end (use subsequent-events-asc855). Read-only: applies management's assessment, never supplies a probability, and posts nothing."
---

# Contingencies: likely, and can it be measured?

Sometimes a business may have to pay for something not yet settled: a lawsuit, a claim, a
warranty. The accounting question is **how likely it is, and whether a number can be put on it**.
Likely and measurable goes in the accounts; only possible goes in the notes. This skill applies
management's assessment, measures the accrual and drafts the disclosure.

**Works with or without Mosofin.** With Mosofin connected it reads existing accruals, settlements
paid and legal spend, and sweeps for **matters that are costing fees and are not on the list**.
Without it, you upload the matter list and ledger detail and the method is the same.

**Every probability and every estimate is management's**, usually supported by counsel. Legal
spend is not a probability. And some matters are privileged and must not be written into a shared
workpaper. Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never supplies a probability or an estimate of loss.**
- **Never infers the likelihood of loss from the amount of legal spend.**
- **Never writes a privileged matter into the workpaper without the user's say-so.**
- **Never nets an insurance recovery against the liability**, and never records a gain
  contingency.

Full wording: [`references/mosofin-protocol.md`](references/mosofin-protocol.md). **Read it before
the first tool call.**

---

## Stage 1 — Intake: ask these first, in one message

*Stages 1–6 are this card's. "Steps 0–6" always mean the steps in `references/method.md`.*

Before reading any data, collect the basics in **one short batch**, not one question at a time.
Ask only what you cannot already see.

| # | Ask | Why it matters | If unanswered |
|---|---|---|---|
| **A** | *Use Mosofin as the data source for this run, or upload the data yourself?* | Decides the path. Mosofin is the connection to the user's books and other linked platforms; with it the skill reads from there, without it the user uploads and the checks are the same | **Never assume.** Ask only if the Mosofin tools are present. If they are absent, skip this and say once that the run is manual. |
| **B** | *Which company and period, and US GAAP or IFRS?* | The thresholds differ between the two | **Never default the period.** Ask for the framework. |
| **C** | *What matters are open: name, type, status, counsel?* | The population is not in the ledger | Run the completeness sweep only, and list what it found as leads. |
| **D** | *For each matter, what is management's view of likelihood and of the amount or range, and who gave it?* | Never supplied here | **Blocking** for that matter. List it as not assessed. |
| **E** | *Which vendors are your lawyers, and is any matter privileged or restricted?* | Needed for the sweep and for what may be written down | Confirm the firms the spend pattern suggests. **Ask about privilege before producing a workpaper.** |
| **F** | *Do you have counsel's letters, the insurance terms and last year's disclosure?* | The support for the assessment | List each as not supplied. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report legal vendors with spend and no matter on the list.
- Read the existing accruals and settlements paid in the period.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Matter list** with management's assessment | Required | XLSX, or type it in the chat |
| **Ledger detail** for legal expense, accruals and settlements | Required | XLSX or CSV |
| Counsel's letters and insurance terms | Recommended | PDF |
| Prior year disclosure | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Evaluating contingencies for **Northbrook Trading** at **31 December** under **US GAAP**, from
> **your Mosofin connection**. **Three matters** on your list, each with **the general counsel's**
> assessment. Law firms confirmed. **One matter is privileged** and will be left out of the
> workpaper. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period, the
matter count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the books and sweep for missing matters

Pull accruals, settlements and legal spend, then the completeness sweep:
[`references/method.md`](references/method.md) Steps 0–0b.

## Stage 4 — Classify and set out the treatment

Each matter classified on management's assessment, then the treatment:
[`references/method.md`](references/method.md) Steps 1–2. Check
[`references/edge-cases.md`](references/edge-cases.md) for IFRS thresholds, a loss that is
probable and cannot be estimated, gain contingencies and insurance recoveries.

## Stage 5 — Measure, draft disclosures, controls, and present

The accrual as a **proposal**, the draft disclosures for legal review, the controls, then the
outputs: [`references/method.md`](references/method.md) Steps 3–5 and *Outputs*. Before
presenting, check it against [`references/output.md`](references/output.md). Ask whether the user
wants the workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 6. Persist the framework and the list of legal
vendors. Assessments are obtained again every period.

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
