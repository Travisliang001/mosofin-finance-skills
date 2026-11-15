# A/R aging and collections — Northbrook Trading Ltd, as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and every step is `[manual]`, from your uploads. (Connecting Mosofin would automate the reads — docs.mosofin.com.) No record was changed, no payment or credit applied, and **no reminder was sent**.

## (a) Read-back

Aging the receivables of **Northbrook Trading Ltd** (name user-asserted; no file carries it) **as at 30 September 2025**, in **USD**, accrual basis, from the aging detail, customer list and payment history you uploaded. Buckets are the default: Current, 1-30, 31-60, 61-90, 91-120, Over 120.

Not answered at intake, and the stated default applied:

| Input | Default applied |
|---|---|
| Disputes, credit holds, strategic tier | **Never inferred.** None assumed; ranking uses age and open balance, plus the payment history you supplied |
| Collection policy / brand voice | Neutral wording, no fees, threats, suspension or legal language |
| Credit sales for DSO | Not supplied → **DSO not computed** |
| Independent aging summary / GL control balance | Not supplied → totals are derived from the detail; **there is no independent tie-out** |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `ar_aging_detail_2025-09-30.csv` | Invoice-level A/R aging detail: customer, invoice, dates, amount, days overdue. 13 invoices + 1 credit memo, net 798,360 | Days overdue agree with an as-of date of 30 Sep 2025 for all 7 overdue rows. No entity or currency column | Yes, with limits: a single `amount` column (no separate original and open balance); credit memo CM-0312 has no due date; not-yet-due rows show 0 rather than negative days (no effect on buckets) | Yes — Steps 2, 3, 5 | **Accepted with a limit**: amount is treated as open balance; partial payments cannot be seen |
| `customer_list.csv` | Customer master: terms (all 30 days), credit limit, AP contact email. 12 customers, all 12 in the aging | No entity name | Yes | Yes — terms check, credit-limit exposure, addressee for drafts | **Accepted** |
| `customer_payment_history_12m.csv` | Paid-invoice history: 60 invoices, 5 per customer, Oct 2024–Sep 2025, with days-to-pay | No entity name | Partly: **the `days_to_pay` column disagrees with paid date − invoice date on 49 of 60 rows** (e.g. Castleton INV-18200: 10 Oct → 28 Oct is 18 days, file says 25) | Yes — ranking and tone (chronic-late-payer pattern) | **Accepted with a limit**: I use days recomputed from the dates and show the file's own figure alongside; please confirm which is right |
| `ar_aging_detail_2025-09-30_final.csv` | **Not an aging.** A staff shift rota: employee, week_1…week_4, "nights/days/off" for E08–E10 | No company, dates, customers or amounts | No | No step uses it | **Rejected** on content despite the name. If a later aging export exists, upload that. Not used. |

Still missing: an independent **A/R aging summary or GL control balance** for 30 Sep (for the tie-out); credit sales and period (for DSO); dispute / hold / tier flags and your collection policy (only if you want them reflected).

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### Aging summary (USD, open balances, 30 Sep 2025)

| Bucket | Invoices | Amount | % of gross |
|---|---:|---:|---:|
| Current | 6 | 428,103 | 53.5% |
| 1-30 | 3 | 200,127 | 25.0% |
| 31-60 | 1 | 72,046 | 9.0% |
| 61-90 | 1 | 48,031 | 6.0% |
| 91-120 | 1 | 48,200 | 6.0% |
| Over 120 | 1 | 4,003 | 0.5% |
| **Gross invoices** | **13** | **800,510** | 100% |
| Unapplied credit memo CM-0312 (Calder Print) | 1 | (2,150) | shown separately |
| **Net A/R** | | **798,360** | |

- **Overdue: 372,407 = 46.5% of gross.** Over 90 days: **52,203 = 6.5%**.
- Weighted average days past due (current floored at zero): **16.8 days**.
- **Top-five concentration: 584,371 = 73.2% of net A/R** — Harlow 248,157 (31.1%), Pennine 112,071, Castleton 88,056, Ridgeway 72,046, Marlow & Finch 64,041.
- DSO: not computed — credit sales not supplied. I can offer an `Approximate DSO (total-income proxy)` only with your approval and an income figure.
- **Reconciliation: none possible.** Totals are derived from the detail; no summary or GL balance was supplied, so this is not a tie-out. Days-overdue recomputed from due dates agree with the file for every overdue row; all invoices are on 30-day terms, consistent with the customer list.

### Exceptions

| # | Item | Detail | Next action |
|---|---|---|---|
| 1 | **Harlow Fabrication over its credit limit** | Open 48,200 + 199,957 = 248,157 against a limit of 200,000: **48,157 over**. The 199,957 invoice of 12 Sep was raised while a 95-day-old invoice was unpaid | Management review. I do not call this a credit hold — that flag is yours to set |
| 2 | **Harlow INV-20418 (48,200) skipped** | Harlow paid a later invoice (INV-18004, dated 10 Jun, 223,341) on 20 Sep but left this 28 May invoice unpaid at 95 days | Ask Harlow why this one invoice is being passed over. An old invoice skipped while newer ones are paid often has a query on it — **I am not inferring a dispute**; please confirm |
| 3 | **Unapplied credit memo CM-0312, Calder Print (2,150)** | Dated 2 Sep, no due date, not allocated. Calder's INV-20796 is 32,020 gross, **29,870 net** if the credit belongs against it | Confirm the allocation before chasing the gross amount. Draft below asks for net and says so |
| 4 | Foxhall INV-20907 (4,003) at 130 days | Oldest item; small | Escalation review under your policy |
| 5 | Payment-history file internal inconsistency | `days_to_pay` ≠ dates on 49 of 60 rows | Confirm the source |
| 6 | Document numbering | INV-20907 is dated 23 Apr but numbered after INV-20418 dated 28 May | Low; check invoice dates were not edited |

### Payment pattern (12 months, terms 30 days; days recomputed from dates, file's figure in brackets)

| Customer | Avg days to pay | Latest | Pattern |
|---|---:|---:|---|
| Harlow Fabrication | 86 (88) | 102 (100) | **Chronic late payer**, ~56 days beyond terms |
| Foxhall Garden Centres | 75 (75) | 80 (81) | Chronic late payer |
| Tideswell Hotels | 59 (62) | 69 (68) | Chronic late payer |
| Ridgeway Logistics | 46 (47) | 49 (53) | Habitually ~2 weeks late |
| Pennine Retail Group | 44 (44) | 49 (50) | Habitually ~2 weeks late |
| Calder Print | 41 (41) | 47 (47) | Habitually ~10 days late |
| Ashby Engineering | 37 (36) | 43 (42) | Slightly late |
| Other five | 24–31 | 35–39 | Near terms |

By the file's own `days_to_pay`, **every one of the 12 customers has paid 3 days slower on each successive invoice** — a book-wide slowdown worth raising. On recomputed dates the direction is the same but less regular. A late pattern is a pattern, not a default: for Harlow, Tideswell and Foxhall the current overdue items are in line with how they usually pay.

### Collection plan — ranked by age and open balance (owner and status left blank for you)

| Rank | Customer | Overdue | Days | Band | Reason / next action |
|---|---|---:|---:|---|---|
| 1 | Harlow Fabrication | 48,200 | 95 | Over 90 — escalation review | Skipped invoice, over credit limit, largest exposure (248,157). Direct contact by management; establish whether there is a query first |
| 2 | Ridgeway Logistics | 72,046 | 41 | 31-60 — formal follow-up | Usually pays at ~46 days, so due about now; request a payment date |
| 3 | Tideswell Hotels | 48,031 | 67 | 61-90 — management review | Usually pays at ~59–69 days; direct contact |
| 4 | Pennine Retail Group | 112,071 | 12 | 1-30 — friendly reminder | Largest overdue balance; usually pays ~day 44–49 |
| 5 | Calder Print | 32,020 (29,870 net) | 20 | 1-30 — friendly reminder | Settle credit memo allocation first |
| 6 | Ashby Engineering | 56,036 | 3 | 1-30 — friendly reminder | 3 days; light touch |
| 7 | Foxhall Garden Centres | 4,003 | 130 | Over 90 — escalation review | Oldest, smallest; chronic pattern |

Expected-cash note: on past behaviour Harlow's 199,957 current invoice (due 12 Oct) is unlikely to arrive before mid-December.

### Drafts — every one **REVIEW REQUIRED - NOT SENT**

**To ap@harlow.example — REVIEW REQUIRED - NOT SENT.** Subject: Invoice INV-20418. "Our records show invoice INV-20418 dated 28 May 2025 for USD 48,200 remains open, while later invoices have been settled. If there is a query on this invoice, please let us know so we can resolve it; otherwise could you confirm the date we can expect payment? Thank you."

**To ap@ridgeway.example — REVIEW REQUIRED - NOT SENT.** Subject: Invoice INV-20611. "Invoice INV-20611 for USD 72,046 fell due on 20 August 2025 and is showing as unpaid. Could you confirm the payment date? If payment has already been made, please send the remittance details."

**To ap@tideswell.example — REVIEW REQUIRED - NOT SENT.** Subject: Invoice INV-20722. "Invoice INV-20722 for USD 48,031 was due on 25 July 2025. We would appreciate a confirmed payment date, and would welcome a call if anything is holding it up."

**To ap@pennine.example / ap@ashby.example — REVIEW REQUIRED - NOT SENT.** "A friendly reminder that invoice [INV-20537, USD 112,071, due 18 Sep / INV-20685, USD 56,036, due 27 Sep] is now due. Please let us know when payment is scheduled."

**To ap@calder.example — REVIEW REQUIRED - NOT SENT.** "Invoice INV-20796 for USD 32,020 was due on 10 September. We hold credit note CM-0312 for USD 2,150 on your account; if you would like it set against this invoice, the balance payable is USD 29,870. Please confirm."

**Foxhall** — no draft: over 120 days, route to escalation review under your approved policy, which has not been supplied.

## (d) What was not done, and why

| Task | Status | Gap / what to supply |
|---|---|---|
| Summary-to-detail reconciliation; GL control balance test | **Not done** | No summary or balance sheet uploaded; totals are self-derived |
| DSO | Not computed | Credit sales and period |
| Aging on open vs original amount | Single amount column used as open balance | Export with both columns |
| Disputes, credit holds, strategic tiers | Not inferred, not applied | Your flags |
| Escalation wording, late fees | Not drafted | Your approved collection policy |
| Payments in flight (received after 30 Sep, unposted) | Not checked | Bank receipts after period end |
| Allowance / bad-debt estimate | Out of scope for this skill | — |
| Applying CM-0312, placing a hold, sending any reminder | Not done — read-only | A person does these |

Would you like this as a workbook (`Upload_AR_Aging_Collections_2025-09-30.xlsx`)? Only on your yes.

**Data sources:** user uploads only — `ar_aging_detail_2025-09-30.csv`, `customer_list.csv`, `customer_payment_history_12m.csv`. No Mosofin connection used.
