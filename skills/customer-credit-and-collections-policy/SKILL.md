---
name: customer-credit-and-collections-policy
description: "Designs a credit and collections policy for a business: segments the actual customer base by revenue, payment behaviour, disputes and concentration, then sets the credit rules, the collections cadence day by day, the handling of disputes and deductions, who approves exceptions, and the KPIs with a measured baseline. Tests each rule against the real customer base before it is written down. Reads the books through a connected Mosofin workspace when the user agrees, or works from an uploaded customer list and ageing. Use when the user asks for a credit policy, a collections policy or process, a dunning schedule, how to reduce DSO or bad debt as a system, or who should approve credit exceptions. Do not use for one customer's limit (use credit-limit-and-customer-risk) or for running this month's collections (use ar-aging-and-collections). Read-only: produces the policy, the segmentation and a coverage sheet, and changes no terms."
---

# Credit and collections policy: the system, not the chase

Most businesses collect money by improvisation. This skill replaces that with a system: **who
gets credit and how much**, what happens on day 15 and on day 60, who may approve an exception,
and how you know it is working. It designs the policy; your team adopts and runs it.

**Works with or without Mosofin.** With Mosofin connected it segments your real customer base
before a line of policy is written, and measures the KPI baseline. Without it, you upload the
customer list and ageing and the method is the same.

**Policy is judgment; two parts of it are measurable.** The segmentation and four of the six KPIs
come from the books. Roles, approval limits, escalation paths and whether an order hold can
actually be enforced are yours to state. Background:
[`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never changes terms, limits or holds in any system, and never contacts a customer.**
- **Never writes a rule without testing it on the real base.** A hold rule that would stop a third
  of the customers is reported as that.
- **Never reports governance as verified.** Who approved what is not in the books.
- **Never reports DSO without its basis**, and never invents a target.

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
| **B** | *What problem is this solving: slow payment, bad debt, disputes, or no policy at all?* | It decides what the policy optimises for | **Ask again.** |
| **C** | *Which company, and as at what date?* | Sets the base that is segmented | **Never default the date.** |
| **D** | *Which of today's terms are policy, and which have simply built up over time?* | Recorded terms mix both | Treat the most common term as the standard, and **say that you assumed it.** |
| **E** | *Can orders actually be put on hold, and how?* | A hold nobody can enforce is not a policy | Leave order holds out, and say why. |
| **F** | *Who owns the customer relationship, who may approve an exception, and what are the write-off limits?* | Governance comes from people, never from the books | Draft the roles as open questions for the user to fill. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes
  (Gates 0–1 in [`references/gates.md`](references/gates.md)).
- **Read the customer list, ageing and payment history; do not ask for an export.**
- With several company files, ask whether one policy governs all of them.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Customer list with receivables ageing** | Required | XLSX or CSV |
| **Invoice and payment history**, 12 months or more | Required for segmentation by behaviour | XLSX or CSV |
| Credit notes and write-offs for the period | Recommended, for disputes and bad debt | XLSX or CSV |
| Current terms (D), hold process (E), roles and limits (F) | Recommended | Type it in the chat |

**Read back before starting, then wait for a yes:**

> *Designing a credit and collections policy for **Northbrook Trading**, to **reduce DSO**, on the
> customer base at **30 September** from **your Mosofin connection**. Standard terms **net 30**;
> orders **can be held** in the order system by the sales lead. Roles as you listed. Shall I go
> ahead?*

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

## Stage 3 — Read the base and segment it

Pull the customers, ageing and payment history in one batch, then segment by revenue, payment
behaviour, disputes and concentration: [`references/method.md`](references/method.md) Steps 0–1.
Segment on behaviour, not on the ageing alone.

## Stage 4 — Write the credit rules and the collections cadence

Credit policy by segment, the collections cadence, then disputes and deductions:
[`references/method.md`](references/method.md) Steps 2–4. Test each rule on the real base. Check
[`references/edge-cases.md`](references/edge-cases.md) for too few invoices to place a customer,
unenforceable holds, disputes that never became credits, and repeated credits to one customer.

## Stage 5 — Governance, KPIs, and present

Governance, the KPIs with a baseline captured before launch, then the outputs:
[`references/method.md`](references/method.md) Steps 5–6 and *Outputs*. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the policy
as a document or the workpaper as an Excel file before creating either.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 7. Persist the segment rules, the cadence and
the KPI definitions with the baseline date. Customer-level placements are rebuilt every run.

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
