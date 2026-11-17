# AP aging and payment run: Northbrook Trading Ltd, as at 30 September 2025

Mosofin is not connected for this run, so it is manual: every figure below comes from your
uploads and is labelled as such. (Connecting Mosofin would read these straight from your books;
see docs.mosofin.com.) **Nothing has been paid, scheduled or changed. Everything here is a proposal.**

## Read-back

> AP aging for **Northbrook Trading Ltd**, **USD**, as at **30 September 2025**, from your uploaded
> open-bills list, vendor master and 12-month payment history. Default buckets (not yet due, 1-30,
> 31-60, 61-90, 91-120, over 120 days overdue). **Cash available for the run: not given.** Vendor
> tiers, payment methods, discount terms and holds: not given.

Assumptions stated up front: buckets are the skill's defaults; no vendor is treated as critical;
no discount terms exist beyond the net days in the vendor master. **Cash available is never
defaulted, so the cash-constrained payment run (Step 5) is blocked until you give it.**

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | Open AP bills: vendor, bill no., bill and due dates, amount, PO, status. 12 bills, 255,264.00 | No entity or currency named; bills dated 3-25 Sep 2025 | Yes; no original-vs-open split, no currency column | Steps 1-5 | **Accepted with a limit**: company and currency user-asserted; amount taken as open amount |
| `vendor_master.csv` | Vendor master: 12 vendors, terms days, tax form, entity type, bank-details-changed date | Not named | Yes; no discount terms, tiers or payment methods | Steps 1, 3, edge cases | **Accepted with a limit**: company user-asserted |
| `bill_payment_history_12m.csv` | Paid bills Oct 2024-Sep 2025 with due and paid dates, 92 rows | Not named | Yes | Step 3 (timing vs terms), Step 4 | **Accepted with a limit**: company user-asserted |
| `open_bills_2025-09-30_final.csv` | **An employee shift roster** (employee, week_1-4: days / nights / off), not bills | n/a | n/a | No step | **Rejected** on content despite its name. If a later bills list was meant, please upload it. |

**Still missing (required): cash available for this run**, and the run window (this week? two
weeks?). Recommended: vendor tiers, payment method per vendor, any holds or disputes, the A/P
control balance from the trial balance for the tie-out. I would wait for your answer here;
proceeding on the accepted files as instructed.

## Aging summary (reconstructed from the bill list; due-date method)

| Vendor | Not yet due | 1-30 | 31-60+ | Total |
|---|---:|---:|---:|---:|
| Kestrel Supplies (4502, INV-4471) | 95,063.00 | | | 95,063.00 |
| Orchard Packaging | 41,687.00 | | | 41,687.00 |
| Summit Freight | | **23,449.00** | | 23,449.00 |
| Pinecrest Software | 23,449.00 | | | 23,449.00 |
| Greyfriars Legal LLP | 15,633.00 | | | 15,633.00 |
| Brightline IT Services | 13,027.00 | | | 13,027.00 |
| Northgate Utilities | 13,027.00 | | | 13,027.00 |
| Vale Marketing Studio | 10,422.00 | | | 10,422.00 |
| M. Okafor Consulting | 7,816.00 | | | 7,816.00 |
| Kestrel Supplies Inc. | 6,480.00 | | | 6,480.00 |
| Dale Cleaning Co | 5,211.00 | | | 5,211.00 |
| **Total** | **231,815.00** | **23,449.00** | **0.00** | **255,264.00** |

**One bill is overdue: Summit Freight INV-4644, 23,449.00, due 22 Sep, 8 days past due.**
Everything else falls due between 3 and 25 October. Every due date agrees with the vendor's terms
on record (bill date + terms days); none was derived.

## Exceptions: resolve before paying

1. **Summit Freight changed its bank details on 16 Sep 2025**, after the bill (7 Sep) and six days
   before it fell due, and that bill is the one overdue item. **Re-verify the new details through a
   channel Summit did not supply** before any payment. Do not pay INV-4644 on the new details
   until confirmed. Also note INV-4644 (23,449.00) is about 2.9 times Summit's usual monthly bill
   of 8,017.00.
2. **Likely duplicate: Kestrel Supplies INV-4471 and Kestrel Supplies Inc. INV4471**, 6,480.00
   each, dated 5 and 6 Sep. Same amount, same number once normalised, near-identical vendor
   names. Pay at most one; check whether "Kestrel Supplies Inc." is a separate legal payee (no tax
   form on file for it). 6,480.00 equals 12 x its usual 540.00 bill.
3. Two different vendors carry identical amounts to other bills (Pinecrest 23,449.00 = Summit;
   Northgate 13,027.00 = Brightline). Not duplicates by the same-vendor test, but worth a look.

## Payment timing against terms (12-month history)

| Vendor | Bills | Paid vs due | Amount | Finding |
|---|---:|---|---:|---|
| **Kestrel Supplies** | 12 | **12 days early, every time** (paid day 18 on 30-day terms) | 412,296.00 | No discount on offer: cash released early for nothing |
| **Orchard Packaging** | 12 | **12 days early, every time** | 188,400.00 | Same: no discount on offer |
| Halden Property Management | 12 | 1 day late, every time (terms 0, paid next day) | 81,000.00 | Late payer pattern; check lease for late fees (Step 4); no open bill now |
| Summit, Brightline, Okafor, Kestrel Supplies Inc., Greyfriars | 11-12 each | On the due date | | Paid to terms |

Kestrel and Orchard together: 600,696.00 paid an average 12 days before due. Paying them on the
due date would hold that cash about 12 days longer each month (roughly 50,000 on average) at no
cost.

## Early-pay discounts and late penalties

No discount terms appear in the vendor master (terms are net days only), so **no discount
opportunities were identified**; if any vendor offers one outside the books, tell me. **Late
penalties: not computable**; no penalty terms supplied. Summit's 8-day lateness may be accruing a
fee under its contract.

## Proposed payment run: blocked on cash available

The constrained run cannot be built without cash available. On the default ranking, once you give
the figure, the order would be:

1. Critical vendors: none designated (please tier; Northgate Utilities is a likely candidate).
2. Past due: Summit Freight 23,449.00, **after bank-detail verification**.
3. Discounts expiring: none.
4. Due 1-7 Oct: Kestrel 4502 88,583.00 (3 Oct); Orchard INV-4573 41,687.00 (5 Oct); Kestrel
   INV-4471 6,480.00 (5 Oct), **one copy only**, pending the duplicate check.
5. Due 8-14 Oct: Brightline 13,027.00 (9 Oct); Northgate 13,027.00 (12 Oct); Okafor 7,816.00 (13 Oct).
6. Defer: Greyfriars, Vale, Pinecrest, Dale (due 17-25 Oct).

**Held, not in any run:** Kestrel Supplies Inc. INV4471 6,480.00 (duplicate); Summit INV-4644
until bank details are verified. Sum ≤ cash available will be checked when the figure arrives.

## Not done, and why

- **Tie-out to the A/P control balance**: no trial balance uploaded. The 255,264.00 is unproven.
- **Cash-constrained run**: cash available not given (never defaulted).
- **Currency**: no currency column; USD user-asserted; no FX step needed.
- **Vendor tiers, payment methods, holds, disputes**: not supplied; none assumed.
- **Credits and part-payments against open bills**: none supplied; amounts taken as open.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, as at 30 Sep 2025, USD: **user-asserted**. Source: upload (Mosofin not used, by choice). 3 files accepted with limits; 1 rejected (staff roster). Aging is **reconstructed** from bills, not report-native. No mock data. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 Parse: done (12 bills, flags run). 2 Buckets: done. 3 Discounts: done, none found; timing vs terms done. 4 Penalties: not done (no penalty terms). 5 Run: **not done**, cash available missing; ranking shown. 6 FX: not applicable. 7 Output: tables in chat; Excel (`AP_Aging_and_PaymentRun_2025-09-30.xlsx`) offered, not created. |
| Not done | Tie to A/P control (needs trial balance at 30 Sep); credits and in-flight payments (needs credit and payment listings for Sep); bank clearing of payments (needs bank statement). |

No vendor bank details appear in this output. Would you like the Excel workpaper, and what cash is
available for this run?

**Data sources:** uploads only: open_bills_2025-09-30.csv, vendor_master.csv, bill_payment_history_12m.csv.
