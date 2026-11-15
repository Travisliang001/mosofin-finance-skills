# Petty cash reconciliation — Head office float — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the petty cash account and its top-up history directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Reconciling the **head office float** of **500.00** at **Northbrook Trading Ltd** for **September 2025**, **USD**, from **the count sheet and voucher listing you uploaded**. Custodian: **the office manager**. Count of **182.40** by **the office manager on 30 September 2025**. Float, count, counter and date arrived inside the count sheet; used once you confirm them here. **4 vouchers and 1 IOU** in the tin, plus 1 voucher dated after the count. Receipts required above **25** (your answer); **no shortage tolerance** (your answer). Coding from **your chart of accounts**. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `petty_cash_count_and_vouchers.md` | Cash count sheet with float, count, counter, date; voucher listing (101–104, 3–18 Sep, 258.10), one IOU (30.00), and one later voucher (105, 2 Oct, 24.50) | Names Northbrook Trading Ltd, head office float, USD, count 30 Sep 2025: **matches** | Yes; a listing, not the receipt images; no approver column | Steps 1–3, 5–6 | **Accepted.** Limit: vouchers are a listing; receipts themselves not seen; approvals not recorded |
| `chart_of_accounts.csv` | Chart of accounts, 36 accounts, incl. 1010 Petty Cash, 1160 Employee Advances, 6950 Cash Over and Short | No entity named (2300 "Intercompany Payable - Northbrook UK" is consistent with Northbrook) | Yes | Step 4 coding | **Accepted with a limit**: company user-asserted |
| `petty_cash_count_and_vouchers_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a count or voucher file despite its name | None | n/a | No step uses it | **Rejected.** If a later count sheet exists, upload it instead |

**Still missing (recommended, not blocking):** petty cash account (1010) ledger detail and the Cash Over and Short (6950) history, ideally 12 months. Without them the imprest test, the replenishment history and the shortage trend cannot run.

## Imprest test (Step 0b) — not run

Whether the book balance of 1010 Petty Cash equals 500 and moves only on top-ups **could not be tested**: no ledger detail was uploaded. A book balance would not stand in for the count in any case.

## Reconciliation (Step 3)

```
Authorised float                                  500.00
Less: vouchers in the tin (101–104)              (258.10)
Less: IOU, E08 advance 25 Sep                     (30.00)
Equals: expected cash on hand                     211.90
Actual cash counted, office manager, 30 Sep       182.40
Difference (counted − expected)                   (29.50)   CASH SHORT
```

**The float is 29.50 short.** There is no tolerance, so this is not posted to Cash Over and Short; it is **flagged for investigation**. It is reported with the amount, the custodian (the office manager) and the count date (30 Sep 2025), and nothing is concluded about its cause.

**Voucher 105 (Stationery, 24.50, dated 2 Oct 2025) does not reduce the shortage.** It is dated after the count, so it could not have been in the tin on 30 September. It belongs to the October reconciliation. Netting it in would leave the shortage at 5.00, which would be wrong.

## Vouchers and coding (Steps 2 and 4)

| Voucher | Date | Payee | Amount | Receipt | Proposed account (your chart) | Exceptions |
|---|---|---|---:|---|---|---|
| 101 | 3 Sep | Post office | 42.60 | yes | 6900 Postage and Delivery | Approver not recorded |
| 102 | 9 Sep | Taxi | 31.00 | **no** | 6800 Travel and Meals | **No receipt, above the 25 threshold.** Approver not recorded |
| 103 | 12 Sep | Cleaning supplies | 88.50 | yes | 6700 Office Supplies (or 6160 Repairs and Maintenance; your call) | Approver not recorded |
| 104 | 18 Sep | Staff lunch | 96.00 | yes | 6800 Travel and Meals | Approver not recorded; business purpose not stated |
| IOU | 25 Sep | E08 advance | 30.00 | — | **1160 Employee Advances** (Due from employee), **not an expense** | Track until repaid |
| 105 | 2 Oct | Stationery | 24.50 | yes | October: 6700 Office Supplies | **Dated after the count**: next period |

Your policy does not say whether vouchers need an approver; none is recorded on any voucher, so all four are flagged.

## Replenishment (Step 5) — PROPOSED, NOT POSTED

Replenishment = vouchers in the period = **258.10**, to the penny. If you hold voucher 102 until a receipt or a signed explanation is found, the replenishment is 227.10.

| DR / CR | Account | Amount |
|---|---|---:|
| DR | 6900 Postage and Delivery | 42.60 |
| DR | 6800 Travel and Meals (102 taxi 31.00 + 104 staff lunch 96.00) | 127.00 |
| DR | 6700 Office Supplies (103) | 88.50 |
| CR | 1000 Operating Bank Account | 258.10 |

The entry balances (258.10 = 258.10). 1010 Petty Cash stays at 500; only the bank moves. After this top-up the tin would hold **440.50**. Add the 30.00 IOU and it is still **29.50 short of 500** until the shortage is resolved. The IOU stays in 1160 until E08 repays it. No tax is shown on the vouchers, so no input tax line.

## Decisions needed from you

1. Investigation of the 29.50 shortage: who looks into it, and whether to recount. 2. Voucher 102: is a receipt or signed explanation available? 3. Coding of voucher 103. 4. Do vouchers need an approver? 5. Please upload the 1010 and 6950 ledger detail so the imprest test and the shortage trend can run.

## What was not done, and why

- **Imprest invariant (Step 0b), replenishment history, float sizing, Cash Over and Short trend**: these need the 1010 and 6950 ledger detail, which was not uploaded.
- **Receipts themselves**: listing only; receipt images not seen.
- **Workpaper**: shown as tables. Say if you want `HeadOffice_PettyCash_2025-09.xlsx`.
- **Posting**: nothing posted, paid, sent or changed. The replenishment and any shortage entry are yours to post.

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, head office float, September 2025, USD. Stated in the count sheet and matching the intake answers. Data source: **upload**. Files: count and vouchers — accepted (listing only); chart of accounts — accepted with limit (company user-asserted); `petty_cash_count_and_vouchers_final.csv` — **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 0 **not done** (no ledger); 0b **not done**; 1 done (float 500 per count sheet, not checked against the books); 2 done; 3 done: short 29.50; 4 done, from your chart; 5 proposed, 258.10; 6 shortage flagged, not posted; 7 tables in chat; 8 not offered until you approve the results |
| Count | `[manual]`: 182.40, office manager, 30 Sep 2025 |
| Not done | Book balance vs float; imprest movement test; replenishment frequency; shortage trend. All need the 1010 / 6950 ledger detail upload |

**Data sources:** count sheet and voucher listing supplied by you (counted by the office manager, 30 Sep 2025); chart of accounts supplied by you; no ledger read.
