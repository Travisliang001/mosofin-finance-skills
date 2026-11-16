# A/P aging and payment run — Northbrook Trading Ltd, as at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the bill, payment and terms reads — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **As-of date:** 2025-09-30. **Currency:** USD (no other currency in any file). **Data source:** upload only.
- **Not answered at intake:**
  - **Cash available for the payment run: not given.** The skill never defaults it, so the run below is a ranked list with the cash it would need; the constraint check (payments ≤ cash) cannot be done until you give the figure.
  - Aging buckets: not given — the skill's defaults are used (not yet due, 1-30, 31-60, 61-90, 91-120, over 120).
  - Vendor priority tiers, payment method per vendor, holds/disputes: not given — none assumed.
  - Run window: not given — "this week" taken as 1-7 Oct and "next week" as 8-14 Oct, for ranking only.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | Open A/P by bill: 12 bills, vendor, bill no, bill and due dates, amount, PO, status; total 255,264 | No entity/currency in file; bills dated 3-25 Sep 2025 | Yes; minimum bill fields present (currency taken from intake) | Steps 1-5 (the aging itself) | **Accepted with a limit:** company user-asserted; no A/P control balance to tie to |
| `vendor_master.csv` | Vendor master, 12 vendors: terms_days, tax form, entity type, bank-details change date, paid 2025, masked tax ID | No entity in file | Yes | Step 1 (due date vs terms), Step 5 (bank-change check) | **Accepted with a limit:** company user-asserted; no discount or penalty terms, no payment method |
| `bill_payment_history_12m.csv` | 96 paid bills, Oct 2024 - Sep 2025, with paid dates (872,076) | No entity in file; **4 paid dates are 2025-10-05, after the as-of date** | Yes | Step 1 (already paid? terms pattern), Step 5 | **Accepted with a limit:** see finding 4 on the post-dated payments |
| `open_bills_2025-09-30_final.csv` | **Not an A/P listing.** Columns employee, week_1..week_4, values nights/days/off for E08-E10 — a staff shift rota | No company, period or amounts | No | No step uses it | **Rejected** on content, despite the name. If a later open-bills listing exists, upload that |

**Still missing:** cash available for the run (**required** for payment-run mode); the A/P control balance at 30 Sep (trial balance) for the tie-out; vendor tiers and payment methods; any holds or disputes.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Aging summary (reconstructed from the bill listing, aged from due date)

| Bucket | Bills | Amount |
|---|---|---|
| Not yet due (per the due dates on the bills) | 12 | 255,264 |
| 1-30 days overdue and older | 0 | 0 |
| **Total** | 12 | **255,264** |

Not tied to the A/P control balance — no trial balance was uploaded. On the bills' own due dates nothing is overdue. Two due dates contradict the vendor's terms, and one of them changes the bucket:

### Exceptions (Sheet 5)

1. **Summit Freight INV-4644, 23,449 — due date conflicts with terms, and bank details changed.** Bill shows 30 days (due 7 Oct); the vendor master says **15 days**, and all 12 prior Summit bills were 15-day bills paid on the due date. On 15-day terms it was **due 22 Sep and is 8 days overdue** (1-30 bucket). Summit's **bank details were changed on 2025-09-16**. Re-verify the new bank details with Summit through a contact you already hold, not one supplied in the change request, **before** any payment. Hold from the run until verified.
2. **Northgate Utilities 5141, 13,027 — due date conflicts with terms.** Bill shows 30 days (21 Oct); vendor master says 21 days → due **12 Oct**. Not overdue either way; it moves into next week's run.
3. **Likely duplicate — Kestrel Supplies INV-4471 (5 Sep) and Kestrel Supplies Inc. INV4471 (6 Sep), 6,480 each.** Same amount, same number once punctuation is removed, one day apart, under a second vendor record. "Kestrel Supplies Inc." has no tax form and no tax ID on file. Pay at most one; exclude INV4471 from the run until you confirm which legal payee is real.
4. **Four bills paid after the as-of date are missing from the open list — 7,848.** The history shows bills dated 5 Sep paid on **5 Oct 2025**: Brightline 3161 (3,483), M. Okafor 3261 (1,542), Kestrel Supplies Inc. 3311 (540), Greyfriars 3361 (2,283). At 30 Sep they were unpaid, yet none is in `open_bills_2025-09-30.csv`. Either the open list is incomplete by 7,848, or those payment dates are wrong. Please confirm before relying on the 255,264 total.
5. **No W-9 on file** for Brightline IT, M. Okafor, Kestrel Supplies Inc. and Vale Marketing — raise before year-end information returns; not a reason to hold payment here.

### Early-pay discounts and late penalties (Steps 3-4)

No vendor record or bill carries discount terms or penalty clauses. **None identified** — not concluded that none exist; terms text was not supplied.

### Proposed payment run — PROPOSAL: no payment has been made or scheduled

| Rank | Vendor | Bill | Due | Amount | Reason in run |
|---|---|---|---|---|---|
| — | Summit Freight | INV-4644 | 22 Sep (on terms) | 23,449 | **Held**: bank-detail change unverified; overdue 8 days on 15-day terms |
| 1 | Kestrel Supplies | 4502 | 3 Oct | 88,583 | Due this week |
| 2 | Orchard Packaging | INV-4573 | 5 Oct | 41,687 | Due this week |
| 3 | Kestrel Supplies | INV-4471 | 5 Oct | 6,480 | Due this week (keep this one of the pair) |
| — | Kestrel Supplies Inc. | INV4471 | 6 Oct | 6,480 | **Excluded**: likely duplicate |
| 4 | Brightline IT Services | 4715 | 9 Oct | 13,027 | Due next week |
| 5 | Northgate Utilities | 5141 | 12 Oct (on terms) | 13,027 | Due next week (derived due date) |
| 6 | M. Okafor Consulting | INV-4857 | 13 Oct | 7,816 | Due next week |

| | USD |
|---|---|
| Due this week (ranks 1-3) | 136,750 |
| Due this week and next (ranks 1-6) | 170,620 |
| Held / excluded | 29,929 |
| Deferred, due after 14 Oct (Greyfriars 15,633, Vale 10,422, Pinecrest 23,449, Dale 5,211) | 54,715 |
| **Cash available** | **not given — constraint check not done** |

Check: 170,620 + 29,929 + 54,715 = 255,264. If cash is short, ranks run in this order and stop where cash runs out; once you name critical vendors (a utility, key supplier) they move to the top.

## (d) What was not done, and why

- **Tie-out to the A/P control balance**: no trial balance uploaded.
- **Cash constraint check and remaining cash**: cash available not given (never inferred).
- **Discount and penalty review**: no terms text beyond net days.
- **Vendor tiers, payment methods, holds**: not given; nothing assumed except the two holds above, which you must confirm.
- **Multi-currency (Step 6)**: not applicable — all USD.
- **Excel workpaper** `AP_Aging_and_PaymentRun_2025-09-30.xlsx`: not created — say yes if you want it.
- **Nothing was paid, scheduled, sent or changed.** No vendor bank details appear in this output.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, as at 2025-09-30, USD — user-asserted. Source: upload. 3 files accepted with a limit; `open_bills_2025-09-30_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (2 terms conflicts, 1 duplicate, 4 post-dated payments flagged); 2 done — reconstructed, not tied; 3-4 done with a limit (no terms text); 5 done with a limit (no cash figure); 6 not applicable; 7 tables in chat |
| Not done | A/P control tie-out (30 Sep TB); cash constraint (your cash figure); discount/penalty terms (vendor agreements) |

**Data sources:** user uploads — `open_bills_2025-09-30.csv`, `vendor_master.csv`, `bill_payment_history_12m.csv`.
