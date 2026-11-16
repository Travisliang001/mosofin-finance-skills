# Red-flag screen: Northbrook Trading Ltd, September 2025

**For the CFO only.** Every item below is an **indicator: a question, not a conclusion about anyone.**
Many will have an innocent explanation. Nothing has been changed in any record, and no one has
been contacted. This is analysis of uploaded files, **not preserved evidence**: it has no chain of
custody. Mosofin is not connected, so the run is manual.

## Read-back

> Running a **red-flag screen**, with **no specific allegation**, on **Northbrook Trading Ltd** (USD)
> for **September 2025** (as at 30 Sep 2025), from **your uploads**. Approval limit **10,000** (matches
> your purchasing policy: managers up to 10,000, CEO above). Output goes to **the CFO only**. Counsel
> not engaged, which is acceptable for a screen with no allegation; if any item below hardens into a
> specific concern, counsel and qualified forensic investigators should lead from that point. Bank and
> payroll detail are out of scope. No area named, so the full test set. Shall I go ahead?

Assumed "yes".

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `journal_entries_2025-09.csv` | Journal entry listing: 7 entries, 16 lines, 80,468 each side, all balance; with user, entry date and posted date | Not named; Sep 2025 (one entry dated 31 Aug) | Yes; manual JEs only, not the full GL | Step 4 JE tests, threshold test | **Accepted with a limit**: company user-asserted; Benford and full-population tests cannot run |
| `open_bills_2025-09-30.csv` | Open AP bills, 12 bills, 255,264 | Not named; Sep 2025 | Yes; open bills only, no payments | Step 4 duplicate, threshold, PO tests | **Accepted with a limit**: no payments file, so paid duplicates and post-change payments untested |
| `vendor_master.csv` | Vendor master: 12 vendors, terms, tax form, entity type, bank-change date, 2025 paid, masked tax ID | Not named | Yes; no addresses, phones, bank accounts or created dates | Step 4 vendor tests | **Accepted with a limit**: address, phone, bank and new-vendor tests cannot run |
| `purchasing_policy.md` | Purchasing policy: roles, PO rule, approval limits, bank-change verification, vendor SoD | Not named | Yes | Step 3, Step 4 threshold and policy tests | **Accepted** |
| `journal_entries_2025-09_final.csv` | **An employee shift roster** (employee, week_1-4: days / nights / off), not journal entries | n/a | n/a | No step | **Rejected** on content despite its name. |

**Still missing (required for the ghost-vendor and conflict tests): the employee list**, with
addresses. Also useful: the September payments listing, the full GL for September, and vendor
addresses and created dates. I would wait for your answer here; proceeding on the accepted files.

## Flagged items, ranked (questions, not conclusions)

| # | Item | Indicator | Amount | Evidence still needed |
|---|---|---|---:|---|
| 1 | **JE-0904**, 28 Sep, posted by user a.reyes (the CEO's login): Dr Accounts Receivable / Cr Sales Revenue, memo "Revenue adjustment" | Manual revenue entry two days before period end, round amount, by senior management (management-override risk), no customer or invoice reference | **50,000** | The customer invoice or contract behind it; whether it reverses in October; who approved it |
| 2 | **JE-0907**, dated 30 Sep, posted 3 Oct by s.patel: Dr 6200 Marketing / Cr 2100 Accrued Liabilities, **no memo** | **9,999: one dollar under the 10,000 approval limit**; no description; post-close accrual | **9,999** | The supplier, invoice or PO supporting the accrual; who approved it |
| 3 | **Summit Freight bank details changed 16 Sep 2025**; open bill INV-4644 23,449 fell due 22 Sep | Bank-detail change shortly before a payment falls due (payment-diversion pattern). Policy 4 requires telephone verification on a known number | 23,449 | Evidence the call-back was made; whether any payment has gone to the new details (no payments file) |
| 4 | **Kestrel Supplies INV-4471** (5 Sep) and **Kestrel Supplies Inc. INV4471** (6 Sep) | Near-duplicate vendor records (name differs by "Inc."), same amount, same invoice number once normalised. Kestrel Supplies Inc. has no tax form and no tax ID on file, and already shows 6,480 paid in 2025 | 6,480 (each) | Whether these are one supplier; whether 6,480 was already paid once |
| 5 | **JE-0905**: dated 31 Aug, posted 22 Sep, legal fee "missed in August" | Entry back-dated into a prior period three weeks after it closed | 3,800 | Supporting invoice; whether August was locked |
| 6 | **Seven bills over 1,000 with no PO** (Greyfriars, Vale, Northgate, Pinecrest, Dale, both Kestrel 6,480 bills) | Policy 1: every purchase over 1,000 needs a PO approved first | 80,702 | Whether any category is exempt in practice |
| 7 | **Vendors with no tax form or tax ID**: Brightline IT Services, M. Okafor Consulting, Kestrel Supplies Inc., Vale Marketing Studio | Unvalidated vendors (two sole proprietors); open bills 13,027 + 7,816 + 6,480 + 10,422 | 37,745 open | W-9s; who created these vendors |
| 8 | Identical amounts across unrelated vendors: Pinecrest 23,449 = Summit 23,449; Northgate 13,027 = Brightline 13,027 | Repeated identical amounts | 36,476 | Invoices for each |
| 9 | Vendor invoice numbers from ten different vendors fall on one sequence (4502, 4573, 4644, 4715 ... 5283, step 71) | Unusual numbering pattern across vendors | n/a | Original vendor invoices; may be how bills were keyed |

**False-positive expectation:** on a population this small most of these will clear. Items 1-4 are
the strongest. No loss is measured: nothing here is substantiated (Step 6 needs investigators).

## Risk assessment by scheme (Step 2-3)

| Scheme type | Opportunity seen in the data | Residual view |
|---|---|---|
| Financial statement manipulation | Senior user posts revenue directly (item 1); post-close and back-dated accruals (items 2, 5); one preparer (s.patel) posts 6 of 7 entries, no approver field | **Higher**: JE approval control not evidenced |
| Disbursement / vendor | Near-duplicate vendor, bank change, unvalidated vendors, no-PO spend | **Higher**: vendor-master controls look weak |
| Payroll | Not testable (no payroll or employee data) | Unknown, not clean |
| Corruption | Largely not testable from ledgers | Unknown, not clean |

Nothing here says anything about any person's circumstances or motive. A user name on an entry is
a login, not necessarily the person.

## Control remediation to consider

Approval and review of manual JEs, with revenue entries by management reviewed by someone
independent; no-memo entries blocked; vendor-master de-duplication and W-9 before first payment;
evidenced call-back on every bank-detail change; PO enforcement for spend over 1,000.

## Tests not run

| Test | Why | What it would show | How to obtain |
|---|---|---|---|
| Vendor vs employee address / phone match | No employee list; vendor master has no addresses | Fictitious vendors | Employee and vendor address lists |
| Vendor vs employee bank account match | No bank details | The most probative ghost-vendor test | Bank master data, by authorised staff |
| Ghost employees, duplicate direct deposit, terminated still paid | No payroll register | Payroll schemes | Payroll register |
| Paid duplicates; payments after bank change | No payments file | Whether money has left | Sep payments listing, bank statement |
| Benford's Law | 16 JE lines and 12 bills: far too small | Fabricated amounts | Full GL population |
| Sudden new vendors; vendor creator vs payment approver (policy 5) | No created dates or user fields | Same-day create-and-pay; SoD breach | Vendor audit log |
| Revenue cut-off / reversals after period end | No October data | Whether JE-0904 reverses | October GL and credit notes |
| Corruption, kickbacks | Not visible in ledgers | Conflicts of interest | Out of reach of analytics |

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD: **user-asserted**. Source: upload. 4 files accepted (3 with limits); 1 rejected (staff roster). Employee list missing. Recipient: CFO only. Analysis, not preserved evidence. No mock data. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 Engagement: red-flag screen, no allegation. 2-3 Risk framework: done with a limit. 4 Tests: JE, threshold, duplicate, near-duplicate vendor, bank change, PO policy, tax form, identical amounts: done; others above: **not done**. 5 Follow-up: evidence needed listed per item. 6 Loss: **not done**, nothing substantiated. 7 Report: this summary. 8 Output: Excel (`Forensic_Analysis_2025-09_Northbrook Trading Ltd.xlsx`) offered, not created. |
| Not done | Tie to GL (needs full September GL); payments and bank (needs payments listing, bank statement). |

Nothing from this screen will be saved for a later run. Would you like the Excel workpaper?

**Data sources:** uploads only: journal_entries_2025-09.csv, open_bills_2025-09-30.csv, vendor_master.csv, purchasing_policy.md.
