# Red-flag screen — Northbrook Trading Ltd, September 2025 (upload path)

**For the CFO only. Do not forward.** This document lists vendors and user names against indicators; most of them will have done nothing wrong. **Every flag is a question, not a conclusion about any person.** These reads are analysis, not preserved evidence: they carry no chain of custody.

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]`. Connecting Mosofin would automate the reads — docs.mosofin.com. Nothing was changed, sent or paid, and no one was contacted.

## (a) Read-back

**Red-flag screen** (analytical detection), **no specific allegation**, counsel not engaged (not required while there is no allegation; if one arises, stop and engage counsel and a forensic professional). **Northbrook Trading Ltd** (user-asserted; no file names it), **September 2025, as at 30 September 2025**, **USD**. **Approval limit 10,000** (your answer; `purchasing_policy.md` agrees: managers to 10,000, CEO above). Recipient: **the CFO only**. No area of concern named → the full test set is run where the data allows.

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `journal_entries_2025-09.csv` | Journal listing: number, effective date, posted-on date, user, account, debit, credit, memo. 14 lines, 7 entries | Effective 31 Aug–30 Sep 2025, posted 22 Sep–3 Oct; no company | Every entry balances; DR = CR = 79,799. No approver or manual/system source column | Yes — financial-statement tests (Step 4) | **Accepted with a limit: company user-asserted; approval not evidenced; journals only, not the full ledger** |
| `open_bills_2025-09-30.csv` | Open bills listing: vendor, bill no., dates, amount, PO, status. 12 bills | Bill dates 3–25 Sep 2025; no company | Foots to **255,264**; all vendors are in the master | Yes — vendor and duplicate tests | **Accepted with a limit: open bills only; no paid bills or payments** |
| `vendor_master.csv` | Vendor master: 12 vendors, terms, tax form, entity type, bank-details-changed date, paid 2025 (total 950,780), masked tax id | No company | No addresses, phones, bank account numbers or created dates | Yes — vendor tests | **Accepted with a limit**: address, phone and bank matching cannot run |
| `purchasing_policy.md` | Purchasing policy, 5 rules | Not dated | Yes; confirms the 10,000 limit. Ends with an unrelated sentence about an internal audit and completeness scope, which I set aside | Yes — just-under-limit and policy tests | **Accepted** |
| `journal_entries_2025-09_final.csv` | **Not a journal listing.** A staff shift rota: employee E08–E10, week_1…week_4, "nights/days/off" | No company, accounts or amounts | No | No step | **Rejected** on content despite the name. Not used. |

**Still missing (required):** the **employee list** with addresses and bank details (ghost-vendor and conflict tests); **payments made in September** (duplicate-payment test). Also useful: the full September GL (Benford population, revenue vs deposits); vendor addresses, phones, bank details and created dates; who created and approved each vendor and bill (policy rule 5).

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Analytical red flags — ranked by strength, then amount

Population: 7 journals (79,799), 12 open bills (255,264), 12 vendors. With populations this small, false positives are likely and every item needs an innocent explanation ruled out first.

| # | Item | Indicator(s) | Area | Amount | Evidence needed | Status |
|---|---|---|---|---:|---|---|
| 1 | Kestrel Supplies INV-4471 (5 Sep) and **Kestrel Supplies Inc.** INV4471 (6 Sep) | **Possible duplicate**: same amount, same invoice number with the hyphen removed, one day apart, under two vendor records. "Kestrel Supplies Inc." has **no tax form**, and its only 2025 payment is 6,480 — the same amount again. Neither bill has a PO | Disbursement | 6,480 (×2; 12,960 exposure) | Both invoice images; who created the "Inc." vendor and when; the earlier 6,480 payment | **Question — high**. Hold payment pending review |
| 2 | Summit Freight INV-4644 | **Bank details changed 16 Sep 2025**; open bill 23,449 falls due 7 Oct to the new details. Policy rule 4 requires telephone verification on a known number | Disbursement | 23,449 | Evidence of the call-back, by whom, on what number | **Question — high**. Verify before payment |
| 3 | JE-0904 | Manual revenue entry DR AR / CR Sales by a user who posted nothing else this month; **posted on a Sunday** (28 Sep); round **50,000**; generic memo "Revenue adjustment"; **5× the approval limit**, approval not evidenced | Financial statement | 50,000 | Supporting invoice or contract; approver; whether it reversed in October | **Question — high** |
| 4 | JE-0907 | **9,999 — one below the 10,000 limit**; **blank memo**; posted after period end (Fri 3 Oct) to accrued liabilities | Financial statement | 9,999 | Support for the marketing accrual; who approved | **Question — high** |
| 5 | Ten bills from ten different vendors | **Invoice numbers fall on one arithmetic sequence** (4502, 4573, 4644, 4715 … 5283, step 71, with 4786 and 4928 absent) and bill dates fall every second day (3–25 Sep, with 11 and 15 Sep absent). Independent suppliers do not share a numbering series | Disbursement | 242,304 (10 bills) | Original invoices from each vendor; how the listing was produced (an export artefact would explain it) | **Question — medium** |
| 6 | Repeated identical amounts across vendors | **13,027** (Brightline IT 4715; Northgate Utilities 5141) and **23,449** (Summit Freight INV-4644; Pinecrest Software INV-5212) | Disbursement | 72,952 | Invoices for all four | **Question — medium** |
| 7 | Bills over 1,000 with **no PO** (policy rule 1) | Greyfriars Legal 15,633; Vale Marketing 10,422; Northgate Utilities 13,027; Pinecrest Software 23,449; Dale Cleaning 5,211; both Kestrel 6,480 bills | Control | 80,702 (7 bills) | Whether legal and utility bills are exempt in practice. Vale 10,422 and Greyfriars 15,633 also exceed 10,000 and need CEO approval | **Control gap** |
| 8 | Vendors with **no tax form** | Brightline IT Services (sole proprietor; 41,800 paid; 13,027 open); M. Okafor Consulting (sole proprietor; 18,500; 7,816 open); Vale Marketing Studio (9,200; 10,422 open); Kestrel Supplies Inc. (6,480; 6,480 open) | Vendor master | 75,980 paid in 2025 | W-9s; vendor validation records | **Control gap** |
| 9 | JE-0905 | Effective 31 Aug, **posted 22 Sep** — back-dated 22 days into August | Financial statement | 3,800 | August close date; why missed | Question — low |

Not flagged after testing: JE-0901, 0902, 0903, 0906 (routine period-end entries, below the limit, memo and accounts consistent; posted 1–3 Oct). Halden Property Management (0-day terms, 81,000 paid = 9 × 9,000) is consistent with monthly rent.

**Fraud-risk view by scheme type (opportunity only; nothing here is about any person's circumstances):** asset misappropriation via disbursements — **elevated** (duplicate vendor record, unverified bank change, missing tax forms, PO bypass); financial-statement manipulation — **elevated** (large manual revenue entry, just-under-limit accrual); corruption — **not testable** from these files.

## (d) Tests not run — a test not run is not a test passed

| Test | Why not | What it would show | How to obtain |
|---|---|---|---|
| Vendor vs employee address / phone / bank | No employee list; no vendor addresses or bank details | Fictitious vendors | Employee list and full vendor master |
| Duplicate **payments** | No payment listing | Whether either Kestrel bill or the earlier 6,480 was paid twice | September payments / bank statement |
| Benford's Law | 19 amounts in total — far below a valid population | Shaped numbers | Full-year GL |
| Sudden new vendors | No vendor created dates | Created-and-paid-quickly vendors | Vendor master with created dates |
| Segregation of duties (policy rule 5) | No creator / approver data | One person creating and paying a vendor | Audit log |
| Goods receipt before payment (rule 3) | No receipts | Payment without receipt | Receiving records |
| Revenue vs deposits, voids/refunds, lapping, reserve smoothing | No GL, bank, credit memos or prior periods | Skimming, lapping, earnings management | Full GL, bank statements, credit memos, 12 months of P&L |
| Payroll schemes; corruption | No payroll register; not visible in a ledger | Ghost employees; kickbacks | Payroll register; out of scope for analytics |

No loss is quantified: nothing here is substantiated. If any item becomes an allegation, preserve records first and bring in counsel and a qualified forensic professional before further analysis.

## (e) Control remediation (proposals)

Hold the duplicate Kestrel bills and the Summit payment until reviewed; enforce call-back verification on bank changes; collect W-9s before first payment; enforce PO-before-order above 1,000; require a memo and evidenced approval on every manual journal, and second approval on manual revenue entries.

## (f) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — user-asserted. Source: upload. Four files accepted (three with limits); `journal_entries_2025-09_final.csv` rejected (staff rota). Recipient: CFO only. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 engagement settled (screen, no allegation) · 0 inputs read · 2–3 risk by scheme done with limit · 4 tests: 9 run (populations above), 8 not run (section d) · 5 framework stated · 6 **not done** (nothing substantiated) · 7 remediation proposed · 8 tables in chat; no `.xlsx` — I would ask whether you want `Forensic_Analysis_2025-09_Northbrook Trading Ltd.xlsx` · 9 not offered; nothing about any person will be saved. |
| Not done | Every test in section (d), with the upload that would allow it. |

**Data sources:** user uploads — `journal_entries_2025-09.csv`, `open_bills_2025-09-30.csv`, `vendor_master.csv`, `purchasing_policy.md`.
