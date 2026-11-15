---
name: healthcare-revenue-cycle-accounting
description: "Ties a healthcare provider's billing activity to the general ledger and estimates what the care actually earned: maps the revenue cycle, estimates net patient service revenue after contractual allowances, reconciles receivables and cash, sets out the reserves and key estimates, and lists the close controls. Works at aggregate level only and handles no patient detail. Reads the books through a connected Mosofin workspace when the user agrees, or works from uploaded billing summaries. Use when the user asks about net patient revenue, contractual allowances, payer mix, denials, charity care against bad debt, or reconciling a billing system to the ledger. Do not use for general receivables ageing (use ar-aging-and-collections) or for the allowance in a non-healthcare business (use bad-debt-and-write-offs). Read-only: produces the reconciliation, the estimates and proposed entries, and posts nothing."
---

# Healthcare revenue: the list price almost nobody pays

A healthcare provider bills a list price almost nobody pays. Insurers pay contracted rates,
patients pay a share, some claims are refused. The accounting job is to work out **what the care
actually earned**, hold the right reserves, and prove the billing system and the ledger tell the
same story.

**Works with or without Mosofin.** With Mosofin connected it reads revenue, the contra-revenue
accounts, receivables and cash, and computes the realisation rate the books imply. Without it, you
upload billing summaries and the method is the same.

**The billing system holds the real detail.** Charges by payer, payer contracts, denial reasons
and the charity care policy are not in the ledger. **This skill works on totals only and takes no
patient-level data.** Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never takes, stores or displays patient-level information.**
- **Never reports gross charges as revenue.**
- **Never assumes a realisation rate when one can be computed**, and never invents a contractual
  rate.
- **Never treats charity care as bad debt, or the reverse.** The policy decides.

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
| **B** | *Which provider and period?* | Sets the scope | **Never default the period.** |
| **C** | *Can you supply billing totals by payer class: charges, payments, adjustments?* | The billing system holds them | Work from the ledger alone, and say that the billing side was not seen. |
| **D** | *Are gross charges recorded in the ledger, or net only?* | Decides whether a realisation rate can be read | Check the accounts, and confirm. |
| **E** | *Do you have the receivables ageing by payer class, and denials and write-offs with reasons?* | The billing system's ageing is the real one | Use the ledger's totals, and list ageing by payer as not supplied. |
| **F** | *What is the charity care policy, and which payer contracts apply?* | Decides presentation and the allowance | Show charity care as recorded, and list the policy as not supplied. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Confirm which contra-revenue accounts are which.
- Confirm that output at aggregate level is acceptable before producing anything.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Billing summary by payer class**: charges, payments, adjustments | Required. Totals only, no patient detail | XLSX or CSV |
| **Receivables ageing by payer class** | Required | XLSX |
| **Ledger detail** for revenue, contra-revenue, receivables and cash | Required | XLSX or CSV |
| Payer contract rates and charity care policy | Recommended | PDF |

**Read back before starting, then wait for a yes:**

> *Reviewing the revenue cycle for **Lakeside Clinic** for **September**, from **your Mosofin
> connection** and **the billing summary you uploaded, totals by payer class only**. Gross charges
> **are** recorded in the ledger. Charity care per **your policy**. Shall I go ahead?*

On the upload path, name each file you received and say what was read from it: the period and the
totals by payer class. Flag anything unreadable straight away.

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

## Stage 3 — Read the accounts and map the flows

Pull revenue, contra-revenue, receivables and cash, then map the revenue cycle:
[`references/method.md`](references/method.md) Steps 0–1.

## Stage 4 — Estimate net revenue and reconcile

Net patient service revenue, then receivables and cash:
[`references/method.md`](references/method.md) Steps 2–3. Check
[`references/edge-cases.md`](references/edge-cases.md) for gross charges reported as revenue,
payer and patient receivables aged together, and rising unapplied cash.

## Stage 5 — Reserves, controls, and present

The reserves and key estimates, the close controls, then the output:
[`references/method.md`](references/method.md) Steps 4–6. Before presenting, check it against
[`references/output.md`](references/output.md). Ask whether the user wants the workpaper as an
Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the account mapping and the method.
**No patient data and no payer rates are saved.**

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
