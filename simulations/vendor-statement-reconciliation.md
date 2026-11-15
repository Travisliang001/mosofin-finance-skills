# Vendor statement reconciliation — Kestrel Supplies / Northbrook Trading Ltd, 30 September 2025

Mosofin is not connected, so this run is manual on the files you uploaded; every step is `[manual]`. (Connecting Mosofin would automate the ledger side — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Ledger cutoff:** 2025-09-30. **Currency:** USD.
- **Vendor:** Kestrel Supplies — the only statement supplied. **Statement cutoff:** 30 September 2025 (same as the ledger; no reconciling window).
- **Statement scope:** three open invoices and a balance due, no payments or brought-forward balance shown — read as an open-item statement. Not confirmed with the supplier.
- **Not answered at intake:** dispute log (none supplied — treated as "no disputes known", so no difference is classed as a dispute); reconciliation policy / which vendors and how often (none stated; only Kestrel is reconciled, because only its statement exists); owners and target dates for exceptions (yours to set).

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `kestrel_supplies_statement_2025-09.txt` | Supplier statement of account from Kestrel Supplies: 3 invoice lines, balance due | Addressed to Northbrook Trading Ltd; as at 30 Sep 2025; no currency or account reference printed | Yes. Lines foot: 88,583 + 6,480 + 3,920 = 98,983 = balance due | Yes — the statement side (Steps 1-3) | **Accepted with a limit**: currency assumed USD; no account reference to check against the vendor record |
| `open_bills_2025-09-30.csv` | Open AP bills listing, 12 bills, 11 vendor names, columns vendor / bill_no / dates / amount / po / status | No entity name in the file; date in the file name; all bills dated September 2025, all open | Yes. Total 255,264. | Yes — the ledger side (Steps 1-3) and vendor ranking | **Accepted with a limit**: open items only, no paid or credit items for September, so "paid but not applied" cannot be fully tested |
| `bill_payment_history_12m.csv` | Paid-bill history, 32 bills, 8 vendor names, Dec 2024 - Jun 2025, with paid dates | No entity name; stops at June 2025 (latest paid date 2025-06-28) | Yes for what it holds | Yes — payments in transit, duplicate-vendor check | **Accepted with a limit**: nothing after June 2025, so July-September payments cannot be seen |
| `kestrel_supplies_statement_2025-09_final.csv` | **Not a statement.** Columns employee, week_1..week_4 with nights / days / off — a staff shift rota | No company, no dates, no amounts | No | No step uses it | **Rejected** on content. Set aside. If Kestrel issued a later statement, upload that. |

**Still missing:** dispute log (recommended); payment register for July-September 2025 (recommended); invoice copy for 4388.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Duplicate-vendor check (run before any "missing invoice" conclusion)

The ledger holds **two vendor records: "Kestrel Supplies" and "Kestrel Supplies Inc."** Both carry bills in the payment history (Kestrel Supplies 3000-3003 at 34,358; Kestrel Supplies Inc. 3300-3303 at 540) and both carry open bills now. Both records were read for this reconciliation.

### Normalisation applied

Document numbers treated as text; prefix `INV`, hyphens and leading zeros removed for comparison (`INV-4471` = `INV4471` = `4471`). Statement amounts are positive invoices; no credits or payments on the statement.

### Summary

| | USD |
|---|---|
| Statement balance (Kestrel, 30 Sep 2025) | 98,983 |
| Ledger balance — record "Kestrel Supplies" (4502 + INV-4471) | 95,063 |
| Ledger balance — record "Kestrel Supplies Inc." (INV4471) | 6,480 |
| **Ledger balance, both records** | **101,543** |
| **Difference (statement − ledger)** | **(2,560)** |
| Explained: invoice 4388 on statement, not on books | +3,920 |
| Explained: INV-4471 recorded twice on books | (6,480) |
| Unexplained | 0 |

Against the "Kestrel Supplies" record alone the difference is 98,983 − 95,063 = 3,920, which is invoice 4388.

### Matched items

| Statement doc | Ledger doc | Date (stmt / ledger) | Amount | Match tier | Notes |
|---|---|---|---|---|---|
| 4502 | Kestrel Supplies 4502 | 2025-09-03 / 2025-09-03 | 88,583 | 1 — document number | PO-1040 |
| INV-4471 | Kestrel Supplies INV-4471 | 2025-09-05 / 2025-09-05 | 6,480 | 1 — document number | Exact number, date and amount |

### Exceptions

| # | Item | Type | Amount | Likely cause | Proposed next action | Owner / target date |
|---|---|---|---|---|---|---|
| 1 | Invoice **4388**, dated 2025-08-14, on the statement, **not on the books** | Missing invoice — candidate unrecorded liability | 3,920 | Not in open bills or paid history under either Kestrel record. Either never received, received and not entered, or the supplier's error. Not seen as paid (payment data stops in June, so a July-September payment cannot be ruled out). | Ask Kestrel for a copy of invoice 4388. If the liability is confirmed and the document has not arrived by close, accrue it; do not post an invoice from the statement line. | Yours to assign |
| 2 | **INV4471**, 2025-09-06, 6,480 under "Kestrel Supplies Inc." — same number (after normalisation) and amount as INV-4471, 2025-09-05, under "Kestrel Supplies" | Duplicate on the books, across two vendor records | 6,480 | The same invoice entered twice, one day apart, under a second vendor record. The statement shows it once. AP and expense are overstated by 6,480, and both copies are open and due 5 / 6 October — **risk of paying it twice**. | Hold one copy from the next payment run; confirm against the invoice which record is right; draft reversal below. | Yours to assign |
| 3 | Two vendor records for one supplier | Vendor master | — | "Kestrel Supplies" and "Kestrel Supplies Inc." Whether these are one supplier or two legal entities is not provable from the files (the Inc. record has its own 540 bills). | Confirm with the supplier; if one, merge is your decision in your system. | Yours to assign |

No missing credit notes, payments in transit or misapplied payments appear: the statement shows no credits or payments, and no Kestrel payment is recorded after 2025-06-23.

### Position after the proposed corrections

Ledger 101,543 − 6,480 duplicate + 3,920 (if 4388 is confirmed) = **98,983**, equal to the statement.

### Proposed entries — PROPOSED, NOT POSTED

| # | Entry | Dr | Cr | Kind |
|---|---|---|---|---|
| 1 | Reverse duplicate bill INV4471 (Kestrel Supplies Inc.): Dr Accounts Payable 6,480 / Cr the expense or inventory account the duplicate was coded to (not shown in the files) 6,480 | 6,480 | 6,480 | Correction of a book error |
| 2 | Only if 4388 is confirmed and no invoice has arrived: Dr expense / inventory (per the invoice) 3,920 / Cr Accrued liabilities 3,920, reversing when the invoice is entered | 3,920 | 3,920 | **Accrual, not an invoice posting** |

### Vendor prioritisation (limited — from the open-bills file only)

Kestrel is the largest open balance (101,543 of 255,264 total open AP, 40%). Next: Orchard Packaging 41,687; Summit Freight 23,449; Pinecrest Software 23,449; Greyfriars Legal 15,633. No vendor shows a credit balance. No statement has been supplied for any of them; whether any has ever been reconciled is unknown. Every vendor in the history billed every two months to June 2025 and none shows an August bill — the Kestrel statement's August invoice 4388 is consistent with August bills not reaching the ledger, which is worth checking for the other suppliers too.

## (d) What was not done, and why

- **Disputes:** no dispute log supplied; nothing classed as disputed.
- **July-September payments:** not in the files; "paid but not applied by the supplier" cannot be tested for 4388.
- **Invoice copies:** not seen. Nothing can be booked from a statement line.
- **Statement scope, currency and account reference:** not confirmed with Kestrel; no contact was made with the supplier.
- **Full vendor ranking** (annual spend, never-reconciled, broken pattern): only partly possible from two extracts.
- **Owners and target dates** for the exceptions: yours to set. Exception ageing: first reconciliation, age 0.
- **Excel workpaper** (`Vendor_Statement_Recon_KestrelSupplies_2025-09-30.xlsx`): not created — say yes if you want it.
- **Nothing was posted, sent, paid or changed.** Entries are drafts for you to review and enter yourself.

Parameters: both cutoffs 2025-09-30; document-number normalisation as above; match tier 1 only; USD, no conversion.
