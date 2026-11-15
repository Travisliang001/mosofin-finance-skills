---
name: cost-accounting-job-order
description: "Costs work by job, project or order: tests how much direct cost in the books carries no job tag, defines the job cost structure, sets overhead pools and rates, accumulates materials and labour by job, applies overhead, rolls work in progress forward, and treats under- or over-applied overhead, with margin by job. Reads job-tagged costs through a connected Mosofin workspace when the user agrees, or works from uploaded job cost data. Use when the user asks for job costing, project or job profitability, work in progress by job, overhead allocation to jobs, or an overhead rate. Do not use for continuous production (use cost-accounting-process-costing), for standard cost variances (use standard-costing-and-variance-analysis) or for coding a single transaction (use gl-coding-assistant). Read-only: produces job cost sheets, the roll-forward and proposed entries, and posts nothing."
---

# Job costing: what each job really cost

When every job is different, you cannot know whether you made money until you can see what **that
job** cost: its materials, the hours spent on it, and a fair share of overhead. This skill
attaches all three to the right job, rolls **work in progress** forward, and shows margin by job.

**Works with or without Mosofin.** With Mosofin connected it reads costs wherever they carry a job
tag, and measures **how much direct cost has no tag at all**. Without it, you upload the job cost
data and the method is the same.

**A job cost is only as good as the tagging.** Labour rates without payroll, machine hours, which
accounts belong in the overhead pool and each job's status are not in the books and come from you.
Background: [`references/overview.md`](references/overview.md).

## Rules that never bend

- **Asks before using Mosofin.** A connected account is not permission to read it.
- **Reads nothing until Stage 1 is answered** and you have confirmed the read-back.
- **Never writes, updates or deletes anything, in any system.** Every entry is a proposal for a
  person to post.
- **Never spreads untagged cost across jobs to make them add up.** It is reported as untagged.
- **Never invents a labour rate or an overhead rate.**
- **Never reports job margin without saying how much cost was left out of it.**

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
| **B** | *Which company and period?* | Sets every read | **Never default the period.** |
| **C** | *How are jobs tagged: customer, class, project or department?* | This is how costs are read by job | **Ask again.** With no job dimension in use, say that job costing cannot be read from the books. |
| **D** | *Which jobs are open and which are closed?* | Decides what stays in work in progress | Treat every job with activity as open, and say so. |
| **E** | *Which accounts form the overhead pool, what is the allocation base, and is the rate predetermined?* | A policy decision | Report direct cost by job only, with no overhead applied. |
| **F** | *What are the labour rates, and how do jobs earn revenue: time and materials, fixed fee, milestones?* | Hours may be in the books; rates usually are not | Report hours without cost, and margin as not computed. |

**Then, depending on the answer to A:**

**Mosofin path — confirm, don't ask.**
- Read back the workspace and the company file **by name** and wait for an explicit yes (Gates 0–1
  in [`references/gates.md`](references/gates.md)).
- Report the share of direct cost with no job tag before anything else.
- Say whether time is tracked in the system, or only cost.

**Upload path — hand over one checklist.**

| Upload | Needed? | Format |
|---|---|---|
| **Job list** with status | Required | XLSX |
| **Costs by job**: materials and labour hours, with dates | Required | XLSX or CSV |
| **Overhead accounts and the budget** for a predetermined rate | Required to apply overhead | XLSX |
| Labour rates and revenue by job | Recommended | XLSX |

**Read back before starting, then wait for a yes:**

> *Costing jobs for **Northbrook Trading** for **September**, tagged by **project**, from **your
> Mosofin connection**. Overhead applied on **labour hours** at the **predetermined rate you
> supplied**. **Six percent of direct cost is untagged** and will be shown apart. Shall I go
> ahead?*

On the upload path, name each file you received and say what was read from it: the period, the job
count and the totals. Flag anything unreadable straight away.

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

## Stage 3 — Read the costs and test the tagging

Pull the job-tagged costs, test for untagged postings, then define the job cost structure:
[`references/method.md`](references/method.md) Steps 0–1, including Step 0b.

## Stage 4 — Overhead, accumulation and work in progress

Overhead pools and rates, costs by job, overhead applied, and the work in progress roll-forward:
[`references/method.md`](references/method.md) Steps 2–5. Check
[`references/edge-cases.md`](references/edge-cases.md) for a purchase treated as a material issue,
hours without rates, one-off items in the pool and work in progress stranded on a closed job.

## Stage 5 — Overhead variance, reporting, and present

Under- or over-applied overhead, reporting and controls, then the outputs:
[`references/method.md`](references/method.md) Steps 6–7 and *Outputs*. Before presenting, check
it against [`references/output.md`](references/output.md). Ask whether the user wants the
workpaper as an Excel file before creating one.

## Stage 6 — Offer to save *(optional)*

Only after the results have been shown, and only on an explicit yes:
[`references/method.md`](references/method.md) Step 8. Persist the job dimension, the overhead
pool, the allocation base and the rate, with its date.

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
