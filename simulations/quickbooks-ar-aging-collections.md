# QuickBooks receivables ageing and collections plan — Northbrook Trading Ltd, at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would automate the reads — docs.mosofin.com.) Nothing was written to QuickBooks, no credit was applied and **no message was sent**.

## 1. Read-back

Ageing receivables for **Northbrook Trading Ltd** (user-asserted) in **QuickBooks Online** at **30 September 2025**, **USD**, **whole ledger**, from your uploaded exports. **No disputes**, as you said. Drafts signed by **the credit controller**.

| Intake question | Answer used |
|---|---|
| D — holds or promises to pay | Not answered → default: every overdue invoice treated as collectable; **none excluded** |
| E — collection stages and tone | Signatory given; stages and tone not given → default bands by days overdue, neutral tone, no fees, deadlines or legal language |
| F — customers not to be contacted | Not answered → drafts for everyone in the action bands; **question left open** |
| Accounting basis | Not stated in the exports; not asserted |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `AR_Aging_Summary_QuickBooks.csv` | QuickBooks A/R Aging Summary: 12 customers, buckets Current / 1-30 / 31-60 / 61-90 / 91 and over, total **798,360** | No company, date or currency in the file → user-asserted. Every row foots | Yes; 91+ is collapsed (split derived from detail) | Yes — independent totals for Stage 4 reconciliation | **Accepted with a limit: company, date and currency user-asserted** |
| `AR_Aging_Summary_QuickBooks_final.csv` | **Not an ageing.** A staff shift rota: employee E08–E10, week_1…week_4, "nights / days / off" | No company, no dates, no customers or amounts | No | No step uses it | **Rejected** on content despite its name. Not used. If a later summary export exists, upload that |
| `ar_aging_detail_2025-09-30.csv` | A/R Aging Detail: 13 invoices + 1 credit memo, net **798,360** | Days overdue agree with an as-of date of 30 Sep 2025 on every row; no entity or currency column | Partly: one `amount` column (no separate original vs open balance); CM-0312 has no due date; not-yet-due rows show 0, not negative days | Yes — the invoice population (Stages 3–5) | **Accepted with a limit**: `amount` read as open balance, so partial payments cannot be seen |
| `customer_list.csv` | Customer master: 12 customers, terms (all 30 days), credit limit, AP email | No entity name | Yes | Yes — addressees for drafts; terms check | **Accepted** |

Still missing (not blocking the ageing): the **A/R control-account balance** from the trial balance at 30 Sep (for the GL comparison); **credit sales and period** (for DSO); **paid-invoice history** (for payment behaviour); holds, promises to pay and no-contact customers.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Ageing (USD, open balance, 30 Sep 2025)

| Bucket | Items | Amount | % of gross |
|---|---:|---:|---:|
| Current | 6 | 428,103 | 53.5% |
| 1-30 | 3 | 200,127 | 25.0% |
| 31-60 | 1 | 72,046 | 9.0% |
| 61-90 | 1 | 48,031 | 6.0% |
| 91-120 (derived from detail) | 1 | 48,200 | 6.0% |
| Over 120 (derived from detail) | 1 | 4,003 | 0.5% |
| **Gross invoices** | **13** | **800,510** | |
| Unapplied credit memo CM-0312, Calder Print | 1 | (2,150) | |
| **Total A/R** | | **798,360** | |

- **Overdue 372,407 = 46.5% of gross** (46.6% of net). **Over 90 days 52,203 = 6.5%.**
- Weighted average days past due (current floored at 0): **16.8 days**.
- **Top-five concentration 584,371 = 73.2% of total A/R**: Harlow 248,157 (31.1%), Pennine 112,071, Castleton 88,056, Ridgeway 72,046, Marlow & Finch 64,041.
- DSO: **not computed** — no credit sales supplied.

### Summary-to-detail reconciliation (tolerance 0.01)

**Ties in total and for all 12 customers: 798,360 both sides, variance 0.00.** By bucket: 1-30, 31-60 and 61-90 agree exactly; detail 91-120 48,200 + Over 120 4,003 = 52,203 = summary "91 and over"; summary Current 425,953 = detail current invoices 428,103 less CM-0312 (2,150), which QuickBooks places in Current. This is a **summary-to-detail reconciliation only — not a GL control-account reconciliation**; no trial balance was supplied, so the A/R control account was not compared.

### Checks before anyone is chased, and exceptions

| # | Item | Detail | Next action |
|---|---|---|---|
| 1 | **Unapplied credit, Calder Print** | CM-0312 (2,150), dated 2 Sep, no due date, unallocated. Calder's overdue INV-20796 is 32,020; **29,870** if the credit belongs against it | Resolve the allocation before the Calder draft goes out |
| 2 | **Harlow Fabrication over its credit limit** | Open 48,200 + 199,957 = **248,157 vs limit 200,000: 48,157 over.** The 199,957 invoice (12 Sep) was raised while INV-20418 was ~77 days overdue | Management review. I do not call this a credit hold — that flag is yours |
| 3 | **Foxhall invoice predates the customer** | INV-20907 is dated **23 Apr 2025**, but the customer list gives Foxhall's first invoice as **10 Jul 2025** | Check the invoice date and customer before chasing the oldest item |
| 4 | Duplicate invoices | None found: no customer has two invoices of the same amount | — |
| 5 | Numbering | INV-20907 (23 Apr) is numbered after INV-20418 (28 May) | Links to item 3 |

Terms check: every invoice's due date is invoice date + 30, agreeing with the customer list.

### Collection plan — ranked by age, then open balance (owner and status blank for you)

| Rank | Customer | Overdue | Oldest days | Band | Reason / next action |
|---|---|---:|---:|---|---|
| 1 | Harlow Fabrication Ltd | 48,200 | 95 | Over 90 — escalation review | Largest exposure (248,157), over credit limit. Management contact |
| 2 | Foxhall Garden Centres | 4,003 | 130 | Over 90 — escalation review | Oldest; confirm invoice date first (item 3) |
| 3 | Tideswell Hotels | 48,031 | 67 | 61-90 — management review, direct contact | A person makes the call |
| 4 | Ridgeway Logistics | 72,046 | 41 | 31-60 — formal follow-up | Request a payment date |
| 5 | Pennine Retail Group | 112,071 | 12 | 1-30 — friendly reminder | Largest overdue balance |
| 6 | Calder Print | 32,020 (29,870 net) | 20 | 1-30 — friendly reminder | **Held** — unapplied credit |
| 7 | Ashby Engineering | 56,036 | 3 | 1-30 — friendly reminder | Confirm receipt |

Payment behaviour was not applied to the ranking: no paid-invoice history was supplied.

### Drafts — every one **REVIEW REQUIRED - NOT SENT**, signed "Credit Controller, Northbrook Trading Ltd"

- **ap@harlow.example** — "Invoice INV-20418, due 27 June 2025, has an open balance of USD 48,200. Total due on your account at 30 September: USD 48,200 overdue (a further USD 199,957 falls due 12 October). Could you let us know the payment status?" *For management review under your escalation policy (not supplied — no escalation wording added).*
- **ap@foxhall.example** — "Invoice INV-20907, due 23 May 2025, open balance USD 4,003. Could you confirm its payment status?" *Do not send until item 3 is resolved.*
- **ap@tideswell.example** — "Invoice INV-20722, due 25 July 2025, open balance USD 48,031. We would appreciate a confirmed payment date." *Supports a direct call; a person decides.*
- **ap@ridgeway.example** — "Invoice INV-20611 was due on 20 August 2025; open balance USD 72,046. Please confirm the date payment will be made."
- **ap@pennine.example** / **ap@ashby.example** — "A reminder that invoice [INV-20537, USD 112,071, due 18 Sep / INV-20685, USD 56,036, due 27 Sep] is now due. Please confirm it was received and when payment is scheduled."
- **ap@calder.example** — "Invoice INV-20796, due 10 September, open balance USD 32,020." **HELD — not to go out until credit memo CM-0312 (USD 2,150) on this account is allocated.** Figure not adjusted.

## 4. What was not done, and why

| Task | Status | What would allow it |
|---|---|---|
| A/R control account vs ageing (GL comparison) | **Not done** | Trial balance or A/R account balance at 30 Sep |
| DSO | Not computed | Credit sales and the period |
| Payment-behaviour (days-to-pay) ranking | Omitted | Paid-invoice history |
| Open vs original balance; partial payments | Not visible | Detail export with both columns |
| Holds, promises, no-contact list, escalation and fee policy | Defaults applied, none excluded | Your flags and policy |
| Customer confirmation of balances | Not on any accounting surface | Audit confirmation |
| Applying CM-0312, setting a hold, sending any draft | **Not done — read-only** | A person, in QuickBooks |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, as at 30 Sep 2025 (user-supplied), USD — all user-asserted. Basis: not shown in exports, not asserted. Source: **upload** (Mosofin not connected). Fixture flag: n/a. Files: summary *accepted with a limit*; detail *accepted with a limit*; customer list *accepted*; `AR_Aging_Summary_QuickBooks_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task is `[manual]`.
- **C — Field provenance:** customer, invoice, dates, amount, summary buckets, terms, limits, emails = user-supplied export; days past due, buckets, 91-120/Over-120 split, totals, %s, WADPD, concentration, over-limit = calculated from those fields; DSO, payment history, disputes/holds = unavailable.
- **D — Steps:** resolve request — done; normalise — done with a limit (single amount column); reconcile summary-to-detail — done, ties; GL comparison — **not done**; unapplied-credit and duplicate checks — done; ranking and drafts — done on defaults.
- **E — Unknowns carried forward:** CM-0312 allocation; Foxhall invoice date; Harlow over-limit decision; CM-0312 has no due date.
- **F — Parameters:** buckets Current/1-30/31-60/61-90/91-120/Over 120; tolerance 0.01; DSO not computed; ranking by age and open balance only.

Would you like this as a workbook (`QuickBooks_AR_Aging_Collections_Northbrook_Trading_Ltd_2025-09-30.xlsx`)? Only on your yes.
