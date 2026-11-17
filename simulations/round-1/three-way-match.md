# Order–receipt–invoice match — Northbrook Trading Ltd, open bills at 30 September 2025 (upload path)

The Mosofin tools are not present, so this run is manual, from your uploads only. Nothing was paid, held, released or changed; every line below is a recommendation for a person.

## (a) Read-back

Matching **the open vendor bills at 30 September 2025** of **Northbrook Trading Ltd** (USD) against the purchase orders and goods receipts **you uploaded**. Policy taken from your uploaded matrix: **price tolerance 2%, quantity exact, total-amount limit 25**; PO approval limits J. Marsh (manager) 10,000, A. Reyes (finance director) 50,000, CEO above; services orders (freight, consulting) need a signed service confirmation instead of a goods receipt; no foreign currency; exceptions owned by the **AP manager**. All six intake questions are answered by that file, so no default was needed.

**Which match this is:** three-way for the three goods orders that have a receipt (PO-1040, 1041, 1043); **two-way by omission** for the two services orders (PO-1042, 1045), because no service confirmation was uploaded; **no match possible** for seven bills that carry no PO reference.

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | Open vendor bill listing: vendor, bill no, dates, amount, PO ref, status. 12 bills, total 255,264 | Bill dates 3–25 Sep 2025; no entity or currency column | Partly: **header amounts only — no bill lines, quantity, unit price or tax** | Yes — invoice leg (Steps 1–4) | **Accepted with a limit**: match is at header level; billed quantity and price are inferred from the total, and the tax test cannot run |
| `purchase_orders.csv` | PO register: 5 POs, one line each, with qty, unit price, approver and approval date | No entity, currency, PO date or PO total column (total computed as qty × price) | Yes | Yes — PO leg, tests 1, 5, 6, 11, 12 | **Accepted with a limit**: only an approval date, not an issue date |
| `goods_receipts.csv` | Goods receipt log: 3 receipts with PO ref, date, qty, condition | Receipts 4–10 Sep 2025; no receiver name, vendor or line detail | Yes | Yes — receipt leg, tests 3, 4, 7, 8, 15 | **Accepted with a limit**: covers PO-1040, 1041, 1043 only; GRN-773 is absent from the sequence |
| `approval_matrix_and_tolerances.md` | Policy note: approval limits, tolerances, services rule, owner. Marked "sample document… fictitious company" | No company name or effective date | Yes | Yes — intake B, C, D, E, F. Its last line (short-pay write-off, unapplied cash account) belongs to cash application and is set aside | **Accepted** |
| `open_bills_2025-09-30_final.csv` | **Not a bill listing.** A staff shift rota: employee, week_1…week_4, values "nights/days/off" for E08–E10 | No company, dates or amounts | No | No step uses it | **Rejected** — the name suggests a final bills file but the content is a rota. If a later bills export exists please upload it. Not used. |

Still missing: signed **service confirmations** for PO-1042 (Summit Freight) and PO-1045 (M. Okafor Consulting) — required by your own policy; **bill line detail** (qty, unit price, tax); purchase orders or approvals for the seven non-PO bills; paid-invoice history (for the duplicate test against prior payments). None of the files names the company or currency — taken from your intake answer.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

### Match summary — PO-backed bills (174,562 of 255,264)

| Bill | Vendor | PO | PO value (qty × price) | Received | Billed | Variance | Match run | Recommendation |
|---|---|---|---:|---|---:|---:|---|---|
| 4502 | Kestrel Supplies | PO-1040 | 4,000 × 21.7542 = 87,016.80 | 4,000 good (GRN-771, 4 Sep) | 88,583.00 | **+1,566.20 (+1.80%)** | three-way | **Hold** |
| INV-4573 | Orchard Packaging | PO-1041 | 100 × 416.87 = 41,687.00 | **90** good (GRN-772, 7 Sep) | 41,687.00 | 10 units not received = **4,168.70** | three-way | **Pay matched part 37,518.30, dispute 4,168.70** (after approval issue cleared) |
| INV-4644 | Summit Freight | PO-1042 | 1 × 23,449.00 | no service confirmation | 23,449.00 | 0.00 | two-way by omission | **Hold** |
| 4715 | Brightline IT Services | PO-1043 | 6 × 2,171.17 = 13,027.02 | 6 good (GRN-774, 10 Sep) | 13,027.00 | −0.02 (within tolerance) | three-way | **Hold** (process exceptions) |
| INV-4857 | M. Okafor Consulting | PO-1045 | 1 × 7,816.00 | no service confirmation | 7,816.00 | 0.00 | two-way by omission | **Hold** pending confirmation |

Match basis for every line: PO reference on the bill, then single-line PO (no line number or SKU on the bill). Header checks: PO reference and vendor name agree on all five; currency and entity cannot be checked from the files.

### Exceptions

| # | Bill / PO | Exception (test no.) | Severity | Detail | Recommended action | Owner |
|---|---|---|---|---|---|---|
| 1 | 4502 / PO-1040 | Price overbilling (1) | High | Implied unit price 22.1458 vs PO 21.7542: +1.80%, inside the 2% price tolerance, but the bill is 1,566.20 over the PO, far beyond the total limit of 25. Outside tolerance on the total test | Hold; request credit memo for 1,566.20 or a documented override | AP manager |
| 2 | PO-1040 | Approved by wrong authority (12) | Critical | PO value 87,016.80 approved by J. Marsh, limit 10,000. Needs CEO (above 50,000) | Hold until ratified by the CEO | AP manager |
| 3 | INV-4573 / PO-1041 | Short shipment billed in full (4) | High | 100 ordered and billed, 90 received. Overbilled 10 × 416.87 = 4,168.70 | Pay 37,518.30, dispute 4,168.70 or request credit; confirm whether the 10 are still coming | AP manager |
| 4 | PO-1041 | Approved by wrong authority (12) | Critical | 41,687.00 approved by J. Marsh, limit 10,000. Needs finance director | Hold until ratified by A. Reyes | AP manager |
| 5 | INV-4644 / PO-1042 | PO not approved (11) | Critical | Approver and approval date both blank on a 23,449.00 order | Hold; obtain approval (finance director level) | AP manager |
| 6 | INV-4644 / PO-1042 | Billed, not evidenced as received (8) | High | Freight is a service; your policy requires a signed service confirmation and none was supplied | Obtain the confirmation | AP manager |
| 7 | 4715 / PO-1043 | Approved by wrong authority (12) | Critical | 13,027.02 approved by J. Marsh, limit 10,000 | Ratification by finance director | AP manager |
| 8 | 4715 / PO-1043 | Goods received and billed before the PO was approved (process exception) | High | Bill dated 9 Sep, goods received 10 Sep, PO approved 12 Sep. Amounts agree, which is what hides it | Retroactive PO approval, documented | AP manager |
| 9 | INV-4857 / PO-1045 | Billed, not evidenced as received (8) | High | Consulting; no signed service confirmation. Approval is in order (A. Reyes, limit 50,000) | Obtain the confirmation, then pay 7,816.00 | AP manager |
| 10 | INV-4471 and INV4471 | Probable duplicate bill (9) | Critical | "Kestrel Supplies" INV-4471, 5 Sep, 6,480 and "Kestrel Supplies Inc." INV4471, 6 Sep, 6,480 — same amount, same number bar the hyphen, vendor name variant, one day apart | Hold one of the two (6,480); confirm with the vendor; check whether two vendor records exist | AP manager |
| 11 | 7 bills, 80,702 | No purchase order — cannot be matched | High (control gap) | Greyfriars Legal 15,633; Vale Marketing 10,422; Northgate Utilities 13,027; Pinecrest Software 23,449; Dale Cleaning 5,211; Kestrel 6,480 × 2 | Not matched, not passed. Route through non-PO approval; state which categories (utilities, legal) are exempt from POs | AP manager |

### Population findings

| Finding | Scope | Count | Value | Note |
|---|---|---|---:|---|
| POs approved above the approver's limit | J. Marsh | 3 of 5 POs | 141,730.82 | A pattern with figures, not an allegation |
| Variance just inside the price tolerance | Kestrel Supplies | 1 | 1,566.20 | 1.80% against a 2% limit; one instance only, watch next period |
| Non-PO spend in open bills | 7 bills | 7 of 12 | 80,702 (31.6%) | |
| Identical amounts, different vendors | 13,027 (Brightline, Northgate); 23,449 (Summit, Pinecrest) | 2 pairs | — | Reported as an oddity for a person to look at; different vendors and bill numbers, so not raised as duplicates |
| Sequence gaps | GRN-773 and PO-1044 not in the files | 2 | — | Confirm the PO and receipt files are complete |
| Goods received not invoiced at 30 Sep (an accrual) | — | 0 | 0.00 | Every receipt supplied has a bill. The 10 cartons short on PO-1041 are an open commitment, not a liability |

Amount cleared to pay now on the evidence supplied: **0.00**. Matched and payable once approvals are ratified: 37,518.30 (Orchard) and, on confirmation/ratification, 13,027.00 (Brightline), 7,816.00 (Okafor), 23,449.00 (Summit). Disputed: 1,566.20 + 4,168.70 = **5,734.90**, plus 6,480.00 probable duplicate.

## (d) What was not done, and why

| Test / task | Status | Reason |
|---|---|---|
| Tests 3, 4, 7, 8, 15 on PO-1042 and PO-1045 | **Not run — not passed** | No service confirmation; two-way by omission |
| Line-level quantity and price comparison (tests 1–3) | Header level only | Bills have no line detail; billed quantity/price inferred from totals |
| Test 9, duplicates against invoices already paid | Run only within the open bills | No paid-invoice history supplied |
| Test 10, currency mismatch; entity header check | Not run | No currency or entity field in any file; USD and Northbrook taken from intake |
| Test 14, tax mismatch | Not run | No tax amounts on bills or POs |
| Tests 11–12 on the seven non-PO bills | Not run | No PO exists to test |
| Receiver name / same person across stages | Not run | Receiver and bill-entry user not in the files |
| Contract price-adjustment clause for Kestrel | Not checked | Contract not supplied; could legitimise the 1.80% |
| Any conclusion of fraud; any payment or hold | Not done | Patterns are reported; people conclude and act |

If you want this as a workbook I would name it `Match_Population_2025-09_Northbrook Trading Ltd.xlsx` (not "3Way", since two orders were matched on two legs only) — only on your yes.

**Data sources:** user uploads only — `open_bills_2025-09-30.csv`, `purchase_orders.csv`, `goods_receipts.csv`, `approval_matrix_and_tolerances.md`. No Mosofin connection used.
