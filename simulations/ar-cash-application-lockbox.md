# Lockbox cash application — Northbrook Trading Ltd, receipts 22-26 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the open-invoice and customer reads; the bank file would still come from you — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Dates:** lockbox receipts 22-26 Sep 2025, against open invoices as at 30 Sep 2025. **Currency:** USD. **Data source:** upload only.
- **C — bank/lockbox file:** supplied. **D — remittance advice:** supplied for 2 of 5 receipts; the other 3 are matched on reference, amount and payer only.
- **E/F — policy**, from your `cash_application_policy.md` (to confirm): short-pays **up to 50** written off with the **credit manager's** approval; larger deductions stay open against the customer. **Unapplied cash is held as a credit in 1100 Accounts Receivable, not 2100.**
- No bank account name or chart of accounts supplied: the cash side of each entry is "operating bank account (to name)". No reason-code set supplied: plain-language reasons used.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `lockbox_2025-09-22_to_26.csv` | Lockbox receipts: 5 rows, date, payer name, reference, amount; total 331,712 | No entity/currency in file; dated 22-26 Sep 2025 | Yes; no bank trace IDs | Steps 1-5 (the receipts) | **Accepted with a limit:** company user-asserted; no trace IDs, no deposit totals |
| `ar_aging_detail_2025-09-30.csv` | Open A/R by invoice: 13 invoices and 1 credit memo, total 798,360 | No entity in file; as at 30 Sep 2025 | Yes | Steps 2-3 (population to match) | **Accepted with a limit:** it still shows all four invoices paid in this lockbox as open (see finding 6) |
| `remittance_advice.txt` | Two customer remittance notes (Ridgeway, Castleton) | Dated 23-24 Sep 2025 | Yes | Steps 1-3 (references, deduction reason) | **Accepted with a limit:** covers 2 of 5 receipts |
| `cash_application_policy.md` | Short-pay and unapplied-cash policy (typed summary) | Names no company or date | Yes | Steps 3-4 | **Accepted with a limit:** user-supplied policy; used once you confirm the read-back |
| `lockbox_2025-09-22_to_26_final.csv` | **Not a lockbox file.** employee, week_1..week_4 with nights/days/off for E08-E10 — a staff shift rota | No company, dates or amounts | No | No step uses it | **Rejected** on content, despite the name. Upload the later lockbox file if one exists |

**Still missing:** the bank statement or deposit report for 22-26 Sep (the Step 5 tie to the bank); the chart of accounts / bank account name; your deduction reason-code set.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Applied cash register — every line PROPOSED, not applied

| Date | Payer (bank) | Amount | Invoice | Open amount | Level | Result |
|---|---|---|---|---|---|---|
| 22 Sep | PENNINE RETAIL GRP | 112,071 | INV-20537 Pennine Retail Group | 112,071 | **1** (invoice no.) | Paid in full |
| 23 Sep | CASTLETON FOODS LTD | 88,056 | INV-20574 Castleton Foods | 88,056 | **1** (invoice no. from remittance) | Paid in full; exact amount agrees |
| 24 Sep | RIDGEWAY LOG | 71,546 | INV-20611 Ridgeway Logistics | 72,046 | **1** (invoice no.) | **Short-pay 500** — see deduction case |
| 25 Sep | ASHBY ENG | 56,036 | INV-20685 Ashby Engineering | 56,036 | **1** (reference INV20685 normalised to INV-20685) | Paid in full |
| 26 Sep | UNKNOWN PAYER 4471 | 4,003 | *candidate:* INV-20907 Foxhall Garden Centres | 4,003 | **5** (proposed, not accepted) | **Unidentified — park in unapplied cash** |

Payer aliases confirmed by invoice number (for your alias list): PENNINE RETAIL GRP → Pennine Retail Group; CASTLETON FOODS LTD → Castleton Foods; RIDGEWAY LOG → Ridgeway Logistics; ASHBY ENG → Ashby Engineering.

### Deduction case list

| Customer | Invoice | Short-pay | Reason (their remittance) | Credit memo that explains it? | vs write-off limit 50 | Treatment |
|---|---|---|---|---|---|---|
| Ridgeway Logistics | INV-20611 | **500.00** | Damaged pallet, their ref DM-118 | None — the only open credit is Calder Print CM-0312 | **Over** | **Stays open as a deduction against Ridgeway** (not written off). Needs a proof-of-delivery / damage claim review; reason code: damaged goods |

### Unapplied cash

| Received | Payer | Amount | Age at 30 Sep | Candidate | Status |
|---|---|---|---|---|---|
| 26 Sep | UNKNOWN PAYER 4471, no reference | 4,003 | 4 days | Foxhall Garden Centres INV-20907, 4,003, **130 days overdue** — the only open item at that amount | Exact amount, but the payer cannot be tied to Foxhall. **Not applied.** Held as a credit in 1100 until Foxhall or the bank confirms the payer. Escalate if still unidentified after your usual window |

### Proposed entries — PROPOSED, NOT POSTED

| | Dr | Cr | Amount |
|---|---|---|---|
| E-1 Pennine | Operating bank (to name) | 1100 A/R — INV-20537 | 112,071 |
| E-2 Castleton | Operating bank | 1100 A/R — INV-20574 | 88,056 |
| E-3 Ridgeway | Operating bank | 1100 A/R — INV-20611 | 71,546 (500 left open on the invoice as a deduction) |
| E-4 Ashby | Operating bank | 1100 A/R — INV-20685 | 56,036 |
| E-5 Unknown | Operating bank | 1100 A/R — unapplied credit (per your policy, not 2100) | 4,003 |
| **Total** | | | **331,712** |

### Other points

6. **The 30 Sep aging does not reflect any of this week's receipts.** INV-20537, INV-20574, INV-20611 and INV-20685 (328,209 between them) are all still shown open at 30 Sep, although paid 22-25 Sep. Either the receipts have not been posted, or the aging was run before they were. After E-1 to E-5, open A/R would be 798,360 − 331,712 = **466,648** (including the 500 Ridgeway deduction and with the 4,003 sitting as an unapplied credit).
7. **Calder Print CM-0312 (−2,150) is an open credit** against Calder's open INV-20796 (32,020). Not part of this lockbox; worth applying or refunding.

### Step 5 — Tie to bank: NOT DONE

Daily lockbox totals: 22 Sep 112,071; 23 Sep 88,056; 24 Sep 71,546; 25 Sep 56,036; 26 Sep 4,003 = **331,712**. No bank statement or deposit report was supplied, so these cannot be tied to deposits, and no fee or batch-split difference can be tested. This is not a bank reconciliation.

## (d) What was not done, and why

- **Tie to bank deposits**: no bank statement / deposit report.
- **Review of receipts already recorded**: none appear recorded in the aging; every line is a proposal to apply, not a review.
- **Duplicate-payment check against earlier receipts**: no receipt history beyond this week (no overpays arose).
- **Reason codes**: your code set not supplied.
- **Excel workpaper** `AR_CashApplication_2025-09-26.xlsx`: not created — say yes if you want it.
- **Nothing was applied, written off, posted or changed.** Every match, deduction and entry is a proposal for a person.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, receipts 22-26 Sep 2025, USD — user-asserted. Source: upload. 4 files accepted with a limit; `lockbox_2025-09-22_to_26_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (trace IDs blank — not in file); 2 done (4 at level 1, 1 at level 5 proposed only); 3 done (1 deduction, 1 unidentified, 0 overpays); 4 done (proposals); 5 **not done** (no bank statement) |
| Not done | Bank tie (bank statement / deposit report); bank trace IDs (bank file with trace numbers) |

**Data sources:** user uploads — `lockbox_2025-09-22_to_26.csv`, `ar_aging_detail_2025-09-30.csv`, `remittance_advice.txt`, `cash_application_policy.md`.
