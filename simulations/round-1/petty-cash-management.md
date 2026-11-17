# Petty cash reconciliation — Northbrook Trading Ltd, September 2025

Mosofin is not connected, so this run is manual, from the count and vouchers you uploaded.

## (a) Read-back

> Reconciling the **petty cash float** of **500.00 USD** at **Northbrook Trading Ltd** for **September 2025** (as at 30 September 2025), from **your uploaded files**. Count of **182.40** by **the office manager on 30 September 2025**; **5 vouchers and 1 IOU** listed. Receipts required above **25**; **no shortage tolerance**. Shall I go ahead?

Not answered at intake, with the default applied:

- **Which float / location:** one float is listed; treated as the only one.
- **Custodian:** not stated. The office manager is named as the counter only; I have not assumed they are the custodian.
- **Authorised float:** 500.00 as written on the count sheet. No authority document and no book balance were supplied, so it is **not confirmed** against the books.
- **Approval policy:** not stated. No approver is shown on any voucher; reported, not treated as a breach.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `petty_cash_count_and_vouchers.md` | Petty cash count sheet: authorised float, cash counted with counter and date, and a listing of 5 vouchers plus 1 IOU | Count dated 30 Sep 2025. No company name or currency inside the file. Voucher 105 is dated 2025-10-02, after the count. | Yes. Vouchers total 282.60, IOU 30.00. No approver, description or voucher images. | Yes — Steps 1-3 and 5 | **Accepted with a limit**: a listing, not the receipts themselves, so "receipt: yes/no" is taken as stated; company taken from your intake answer |
| `chart_of_accounts.csv` | Chart of accounts, 29 accounts, account / name / type | No company name; includes 1010 Petty Cash and an intercompany account naming Northbrook UK, consistent with Northbrook Trading | Yes, but it has no balances | Yes — Step 4 coding | **Accepted with a limit**: accounts only; no petty cash balance, so the float cannot be tested against the books |
| `petty_cash_count_and_vouchers_final.csv` | **Not a count or voucher listing.** Columns employee, week_1..week_4 with nights / days / off — a staff shift rota | No company, period or amounts | No | No step uses it | **Rejected** on content. Set aside. If there is a later count sheet, upload that. |

**Still missing:** petty cash account detail for the period (recommended, not required); the receipts themselves; the custodian's name; who approved each voucher.

I would wait here for your yes. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Float test against the books — not run

No ledger detail or balance for account 1010 was supplied. Whether the books show a flat 500.00 (an imprest float — a fund always topped back up to the same fixed amount) is **not tested**.

### Reconciliation

Voucher 105 (Stationery, 24.50) is dated **2 October 2025 — two days after the count**. A voucher dated after the count cannot explain cash missing at the count, and the skill's rule is to defer a post-period voucher to the next reconciliation. Both views are shown; the first is the September result.

| | Voucher 105 deferred (September result) | All listed vouchers taken as in the box |
|---|---:|---:|
| Authorised float | 500.00 | 500.00 |
| Less: vouchers | (258.10) | (282.60) |
| Less: IOUs / advances | (30.00) | (30.00) |
| **Expected cash on hand** | **211.90** | **187.40** |
| Actual cash counted (office manager, 30 Sep 2025) | 182.40 | 182.40 |
| **Difference (counted − expected)** | **(29.50) short** | **(5.00) short** |

- September vouchers: 42.60 + 31.00 + 88.50 + 96.00 = 258.10. With voucher 105: 282.60.
- **Either way the fund is short.** If voucher 105 is a genuine payment made on or before 30 September and simply misdated, the shortage is **5.00**. If it was paid on 2 October, the 30 September count is **29.50** short, of which 24.50 would be cash that had left the tin before the voucher date. Please confirm the date of voucher 105.
- **No tolerance was given, so no amount is treated as acceptable.** The shortage is reported, not absorbed and not proposed for posting to Cash Over/Short. Count date 30 September 2025; counted by the office manager; custodian not stated. No cause is concluded.

### Voucher detail and exceptions

| Voucher | Date | Paid to | Amount | Receipt | Approver | Exception |
|---|---|---|---:|---|---|---|
| 101 | 2025-09-03 | Post office | 42.60 | yes | not shown | — |
| 102 | 2025-09-09 | Taxi | 31.00 | **no** | not shown | **No receipt, above the 25 threshold** |
| 103 | 2025-09-12 | Cleaning supplies | 88.50 | yes | not shown | — |
| 104 | 2025-09-18 | Staff lunch | 96.00 | yes | not shown | — |
| 105 | **2025-10-02** | Stationery | 24.50 | yes | not shown | **Dated outside the period and after the count** — deferred to October |
| IOU | 2025-09-25 | E08 advance | 30.00 | — | not shown | **Staff advance, not an expense** |

1. **Voucher 102 (Taxi, 31.00) has no receipt and is above the 25 threshold.** Not supported; it stays in the reconciliation as a voucher but should not be reimbursed as an expense until a receipt or an approved explanation is supplied.
2. **Voucher 105 (24.50) is dated 2 October**, outside September and after the count. Deferred to the next reconciliation unless you confirm it is misdated.
3. **IOU 30.00 to employee E08 (25 September)** is a staff advance. It is held as due from the employee until repaid, shown separately from the vouchers, and is **not** part of the replenishment or of expense. Five days old at the count.
4. **No approver is recorded on any voucher**, and no business purpose beyond the payee.

### Coding to the chart of accounts

The uploaded chart has **no account for postage, travel, cleaning or office supplies, staff meals or stationery**, no **Cash Over/Short** account and no **Due from Employee / staff advances** account. The only expense accounts are Payroll, Rent, Marketing, Software, Professional Fees, Bank Fees, Depreciation and Interest. I have not forced the vouchers into those accounts or invented account numbers. **Please say which accounts to use** (or confirm the chart extract is incomplete).

### Replenishment — PROPOSED, NOT POSTED

Replenishment equals the approved vouchers for the period.

| | Amount |
|---|---:|
| September vouchers 101-104 | 258.10 |
| of which unsupported (voucher 102, no receipt) | 31.00 |
| Supported vouchers 101, 103, 104 | 227.10 |

Proposed entry, once the accounts are confirmed and voucher 102 is resolved: Dr expense accounts (per coding, to be confirmed) 258.10 / Cr 1000 Operating Bank Account 258.10. Account 1010 Petty Cash does not move.

After a 258.10 top-up the tin would hold 440.50 in cash, against 500.00: the gap is the 30.00 IOU, the 24.50 October voucher and the 5.00 that nothing explains. Restoring the tin to a full 500.00 in cash would take 317.60 (500.00 − 182.40), but 59.50 of that is not September expense.

## (d) What was not done, and why

- **Imprest test, book balance vs float, replenishment history, Cash Over/Short trend, float sizing:** not run — no ledger detail for account 1010 was supplied.
- **Voucher coding:** not completed — the chart supplied has no suitable accounts; none were invented.
- **Receipts:** not seen; the yes/no column is as stated on the listing.
- **The physical count** is the office manager's, 30 September 2025; it was not and cannot be performed here.
- **Shortage treatment:** no tolerance, so nothing is proposed to Cash Over/Short; flagged for your investigation. No cause or person is suggested.
- **Excel workpaper** (`HeadOffice_PettyCash_2025-09.xlsx`, location name to be confirmed): not created — say yes if you want it.
- **Nothing was posted, paid, sent or changed.** The replenishment is a proposal for a person to make.

**Data sources:** count sheet and voucher listing uploaded by you (count by the office manager, 30 Sep 2025); chart of accounts uploaded by you; company, period, currency, threshold and tolerance as typed at intake. No ledger read.
