# Invoice match: Northbrook Trading Ltd, open bills at 30 September 2025

**Match performed: three-way for PO-1040, PO-1041, PO-1043; two-way by omission for the two
services orders PO-1042 and PO-1045** (policy requires a signed service confirmation; none was
uploaded). Seven bills carry no PO and sit outside the match. Manual run: no Mosofin connection.

## Read-back

> Matching **September 2025's open bills** (as at 30 Sep 2025) for **Northbrook Trading Ltd**, in
> **USD**, against purchase orders and goods receipts, all **uploaded by you**. Tolerance taken
> from your uploaded policy: **price 2%, quantity exact, total-amount limit 25**. Approval matrix
> from the same file: J. Marsh up to 10,000; A. Reyes (CEO) above 10,000. Services orders need a
> signed service confirmation. No foreign-currency orders. Exceptions owned by the **AP manager**.
> This will be a **three-way match for goods, two-way by omission for services** (no
> confirmations supplied). Shall I go ahead?

Intake B, C, D, E and F were answered inside the policy file; I use them as confirmed by the
read-back. Assumed "yes, go ahead with the accepted files".

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `purchase_orders.csv` | 5 POs, one line each: vendor, item, qty, unit price, approver, approval date | No entity or currency named | Yes; no PO issue date, only approval date | Steps 1-4, exceptions 1-6, 11-13 | **Accepted with a limit**: company and currency user-asserted; receipt-before-PO tested against approval date |
| `goods_receipts.csv` | 3 goods receipts with qty and condition | Not named; dated Sep 2025 | Yes | Steps 2-4, exceptions 3, 4, 7, 8, 15 | **Accepted with a limit**: company user-asserted; no receiver name |
| `open_bills_2025-09-30.csv` | AP open-bills list, 12 bills, 255,264.00 | Not named; Sep 2025 | Header only: no line items, no tax, no currency | Steps 1-4 | **Accepted with a limit**: header-level match only; exception 14 cannot run |
| `approval_matrix_and_tolerances.md` | Policy note: matrix, tolerances, services rule, FX, owner | Not named | Yes | Steps 3-5, exceptions 11, 12 | **Accepted** (facts confirmed in read-back) |
| `open_bills_2025-09-30_final.csv` | **An employee shift roster** (employee, week_1-4: days/nights/off), not bills | n/a | n/a | No step uses it | **Rejected**: content is a staff rota despite the file name. If a later bills list was meant, upload it. |

Still missing: **signed service confirmations for PO-1042 (Summit Freight) and PO-1045 (M.
Okafor Consulting)**. They block those two matches, not the run.

## Match summary

| Bill | Vendor | PO | GRN | Bill amount | PO value | Received value | Matched | Disputed / held | Basis | Recommendation |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 4502 | Kestrel Supplies | PO-1040 | GRN-771 | 88,583.00 | 87,016.80 | 87,016.80 | 87,016.80 | 1,566.20 | PO no. (header) | **Hold**; or pay matched, dispute 1,566.20 |
| INV-4573 | Orchard Packaging | PO-1041 | GRN-772 | 41,687.00 | 41,687.00 | 37,518.30 | 37,518.30 | 4,168.70 | PO no. (header) | **Hold**; request credit memo for 10 cartons |
| INV-4644 | Summit Freight | PO-1042 | none (service) | 23,449.00 | 23,449.00 | n/a | 0.00 | 23,449.00 | PO no. (header) | **Hold**: PO unapproved, no confirmation |
| 4715 | Brightline IT Services | PO-1043 | GRN-774 | 13,027.00 | 13,027.02 | 13,027.02 | 0.00 | 13,027.00 | PO no. (header) | **Hold**: approved beyond authority |
| INV-4857 | M. Okafor Consulting | PO-1045 | none (service) | 7,816.00 | 7,816.00 | n/a | 0.00 | 7,816.00 | PO no. (header) | **Hold** until signed confirmation |

No bill is recommended for payment in full today. All bills are header-only, so every match is
header level: bill total against PO qty x price and received qty x price.

## Exceptions

| # | Bill / PO | Exception | Severity | Figures | Recommended action | Owner |
|---|---|---|---|---|---|---|
| 1 | 4502 / PO-1040 | **Price overbilling** (ex. 1). Implied unit price 22.1457 vs PO 21.7542 | High | +1,566.20, **+1.80%**: inside the 2% price tolerance but **breaks the 25 total-amount limit** | Hold; ask Kestrel for a credit or the price clause; or pay 87,016.80 and dispute 1,566.20 | AP manager |
| 2 | INV-4573 / PO-1041 | **Short shipment billed in full** (ex. 4). Ordered 100, received 90, billed 100 | High | 10 x 416.87 = **4,168.70** over-billed | Request credit memo; pay 37,518.30 at most | AP manager |
| 3 | INV-4644 / PO-1042 | **PO not approved** (ex. 11): no approver, no approval date | **Critical** | 23,449.00 | Hold; obtain retroactive approval from A. Reyes (amount > 10,000) | AP manager |
| 4 | INV-4644 / PO-1042 | **Billed, not received** (ex. 8): service with no signed confirmation (two-way by omission) | High | 23,449.00 | Hold until confirmation | AP manager |
| 5 | 4715 / PO-1043 | **Approved by wrong authority** (ex. 12): J. Marsh approved 13,027.02, above the 10,000 manager limit | **Critical** | 13,027.02 (3,027.02 over limit) | Hold; CEO approval required | AP manager |
| 6 | 4715 / PO-1043 | **Goods received before the PO was approved**: GRN-774 on 10 Sep, PO approved 12 Sep (bill dated 9 Sep, also before approval) | Process exception | Amounts agree (0.02 favourable) | Retroactive approval, by the right authority | AP manager |
| 7 | INV-4857 / PO-1045 | **Billed, not received** (ex. 8): consulting, no signed confirmation | High | 7,816.00 | Hold until confirmation | AP manager |
| 8 | INV-4471 and INV4471 | **Likely duplicate invoice** (ex. 9): "Kestrel Supplies" vs "Kestrel Supplies Inc." (likely duplicate vendor record), same 6,480.00, invoice number equal once normalised, dated 5 and 6 Sep | **Critical** | 6,480.00 at risk | Reject one copy; merge the vendor records; neither has a PO | AP manager |

No price underbilling, quantity overbilling, item-not-on-PO, currency, vendor-mismatch or
damaged-goods exceptions were found (all three receipts are condition "good").

## Not matched: no PO (7 bills, 80,702.00)

Greyfriars Legal LLP 15,633.00; Vale Marketing Studio 10,422.00; Northgate Utilities 13,027.00;
Pinecrest Software 23,449.00; Dale Cleaning Co 5,211.00; Kestrel Supplies 6,480.00; Kestrel
Supplies Inc. 6,480.00. The policy file does not say whether legal, marketing, utilities, software
or cleaning spend needs a PO; please confirm. Note that Northgate (13,027.00) and Pinecrest
(23,449.00) repeat the exact amounts of Brightline's and Summit's PO-backed bills; different
vendors, so not duplicates under exception 9, but worth a look by whoever owns vendor review.

## Population findings

| Finding | Scope | Count | Value | Action |
|---|---|---:|---:|---|
| Variance just inside price tolerance | Kestrel Supplies | 1 | 1,566.20 (1.80% vs 2%) | One instance only, not yet a pattern; watch next period |
| Unreceipted / unconfirmed services bills | Summit, Okafor | 2 | 31,265.00 | Obtain confirmations |
| PO approval breaches (none / beyond authority) | PO-1042, PO-1043 | 2 | 36,476.02 | Review approval workflow |
| Possible duplicate vendor record | Kestrel Supplies / Kestrel Supplies Inc. | 1 pair | 6,480.00 | Vendor master clean-up |
| GRNI at 30 Sep (received, not billed) | All GRNs | 0 | 0.00 | Every receipt has a bill; no accrual from this population |

PO-1044 is missing from the PO sequence; not in the uploads, so not tested.

## Not done, and why

- **Exception 14 (tax)**: bills carry no tax field. **Not run.**
- **Exception 6** ran: every PO has a bill. **Exception 7**: no receipt without a bill.
- **Line-level matching**: bills are single totals, so every match is header level; the implied
  unit price is stated, not inferred beyond the totals.
- **Same user across PO / receipt / bill**: no creator or receiver names uploaded. Not run.
- **Contract price clauses** for Kestrel: not supplied; the 1.80% may be legitimate.
- **Payment, holds, releases**: none made. Recommendations only. No fraud is concluded.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025 (30 Sep 2025), USD, all **user-asserted**. Source: upload. 4 files accepted (3 with limits above), 1 rejected (staff roster). Legs: invoices (header only), POs (one line each), goods receipts (3, with condition). |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 Extract: done with a limit (header-only bills). 2 Match: done, header level. 3 Tolerances: done (2% / exact / 25). 4 Exceptions: 1-13 and 15 run; 14 not run; 3, 4, 7, 8, 15 ran for goods only. 5 Resolutions: proposed. 6 Output: tables in chat; Excel offered, not created. |
| Not done | Tie of bills to the AP control account (needs trial balance); tax test (needs tax per bill); service confirmations; approver/creator SoD test (needs user names); prior-period GRNI baseline. |
| Parameters | Price 2%, qty exact, total 25. Matching precedence: PO number, header level. Approval matrix as uploaded. Workpaper name if wanted: `Match_Population_2025-09_Northbrook Trading Ltd.xlsx` (not "3Way": two services orders were two-way). |

Would you like this as an Excel workpaper?
