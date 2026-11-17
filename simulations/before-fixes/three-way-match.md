# Invoice match — Northbrook Trading Ltd — open bills at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read bills and POs directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back (Stage 1)

Matching **the 12 open bills at 30 September 2025** for **Northbrook Trading Ltd** (user-asserted), **USD** (user-asserted; no file states a currency), against the **purchase orders and goods receipts you uploaded**. From `approval_matrix_and_tolerances.md` (facts that arrived inside a file; used once you confirm them here): **price 2%, quantity exact, total 25**; PO approval **J. Marsh up to 10,000, A. Reyes (CEO) above 10,000**; **services orders (freight, consulting) need a signed service confirmation** in place of a receipt; **no foreign-currency orders**; exceptions owned by **the AP manager**. This will be a **three-way match for the goods POs** and a **two-way match by design for the services POs**. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `purchase_orders.csv` | 5 POs, one line each, with approver and approval date (PO-1040 to PO-1045; PO-1044 absent) | No entity or currency; approvals 25 Aug – 12 Sep 2025 | Yes; no PO date column, so approval date stands in | Steps 1–4 (PO leg, tests 1–6, 11–13) | **Accepted with a limit**: company user-asserted; PO date = approval date |
| `goods_receipts.csv` | 3 goods receipts (GRN-771, 772, 774), with condition | No entity, vendor or receiver; 4–10 Sep 2025 | Yes | Receipt leg; tests 3, 4, 7, 8, 15 | **Accepted with a limit**: company user-asserted; no receiver name or vendor on receipts |
| `open_bills_2025-09-30.csv` | AP open-bill listing, 12 bills, 3–25 Sep 2025, total **255,264** | No entity or currency; dates in September | Header-level only: no lines, quantities, unit prices or tax | Invoice leg | **Accepted with a limit**: company user-asserted; **header-level match only**; tax test (14) cannot run |
| `approval_matrix_and_tolerances.md` | Policy note: approval matrix, tolerances, services rule, FX, owner | No entity named | Yes | Steps 3–4 (tolerance, tests 11–12), owners | **Accepted with a limit**: company user-asserted |
| `open_bills_2025-09-30_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a bill listing despite its name | None | n/a | No step uses it | **Rejected.** If a later bill listing exists, upload it instead |

**Still missing:** **signed service confirmations for PO-1042 (Summit Freight) and PO-1045 (M. Okafor Consulting)** — required by your policy; they block those two bills only. Vendor master (optional) not supplied, so payment terms are not checked. Payment history not supplied, so test 9 (duplicate of a *paid* invoice) cannot run.

## Findings — header-level match, tolerance per your policy

| PO | Vendor | Bill | Legs | PO value | Received | Billed | Variance | Status | Recommendation |
|---|---|---|---|---:|---|---:|---:|---|---|
| PO-1040 | Kestrel Supplies | 4502 | 3-way | 87,016.80 (4,000 × 21.7542) | 4,000, good | 88,583.00 | **+1,566.20 (1.80%)** | Exception 1: inside 2% price, **breaks total tolerance of 25** | **Hold**, or pay 87,016.80 and dispute 1,566.20 |
| PO-1041 | Orchard Packaging | INV-4573 | 3-way | 41,687.00 (100 × 416.87) | **90**, good | 41,687.00 | 0 vs PO; **+4,168.70 vs receipt** | **Exception 4: short shipment billed in full** (10 × 416.87) | **Partial pay 37,518.30**, request credit for 4,168.70 |
| PO-1042 | Summit Freight | INV-4644 | 2-way by design | 23,449.00 | no confirmation | 23,449.00 | 0 | **Exception 11 (Critical): PO has no approver or approval date**; 23,449 needs the CEO. Service confirmation missing | **Hold** |
| PO-1043 | Brightline IT Services | 4715 | 3-way | 13,027.02 (6 × 2,171.17) | 6, good | 13,027.00 | −0.02 | **Exception 12 (Critical): approved by J. Marsh (limit 10,000) for 13,027.02.** Received 10 Sep and billed 9 Sep, **before the PO was approved on 12 Sep** — process exception though amounts agree | **Hold** for CEO retro-approval |
| PO-1045 | M. Okafor Consulting | INV-4857 | 2-way by design | 7,816.00 | no confirmation | 7,816.00 | 0 | Amounts agree; approval within J. Marsh's limit. **Signed service confirmation missing** | **Hold** until confirmation arrives |

Match basis: PO reference on the bill, then vendor name (all five agree to the PO vendor exactly). All bills are header-only; the PO-1040 implied price of 22.1458 against 21.7542 is what the totals imply, not a billed price.

**Bills outside the match — not matched: no PO.** Seven bills, **80,702** in total: Greyfriars Legal LLP 15,633; Vale Marketing Studio 10,422; Northgate Utilities 13,027; Pinecrest Software 23,449; Dale Cleaning Co 5,211; Kestrel Supplies INV-4471 6,480; Kestrel Supplies Inc. INV4471 6,480. Your policy note does not say whether these kinds of spend need a PO — please confirm. No PO inferred for any of them.

**Possible duplicate:** **Kestrel Supplies `INV-4471` (5 Sep) and Kestrel Supplies Inc. `INV4471` (6 Sep), both 6,480**: same invoice number once punctuation is removed, same amount, vendor name differing only by "Inc.", one day apart. Hold one pending confirmation with the vendor. Also noted, as a pattern only: two pairs of bills from different vendors carry identical amounts (23,449 Summit Freight / Pinecrest Software; 13,027 Brightline / Northgate Utilities). Possibly coincidence; worth a glance.

**Population view.** PO-1040's 1.80% sits just inside the 2% price tolerance (one instance; no pattern can be called from one month). GRNI (received, not billed) at 30 Sep: **nil** — all three receipts are billed. Open PO commitments not invoiced: **nil**. PO-1044 and GRN-773 are missing from the sequences: please confirm they were cancelled.

**Summary of recommendations (proposals only — nothing paid, held or released by me).** Pay in full now: none. Partial pay: 37,518.30 (PO-1041). Matched but held: 87,016.80 (PO-1040, pending the 1,566.20 dispute), 13,027.00 (PO-1043), 7,816.00 (PO-1045). Held on approval: 23,449.00 (PO-1042). Disputed: 1,566.20 + 4,168.70 = **5,734.90**. Owner for every exception: **AP manager**, per your policy.

## Tests that ran and did not

| Test | Ran? |
|---|---|
| 1 price over, 2 price under | Ran, header level (PO-1040 over; PO-1043 under by 0.02, within tolerance) |
| 3 qty over, 4 short shipment billed | Ran for 3 goods POs at header level (PO-1041 exception 4) |
| 5 item not on PO, 6 PO not invoiced | Ran at header level; none |
| 7 received not billed (GRNI), 8 billed not received | Ran for goods POs; none. Services POs: confirmations missing |
| 9 duplicate of a paid invoice | **Not run**: no payment history. Open-vs-open duplicate flagged above |
| 10 currency | **Not run on data**: no currency on any document; policy says no FX orders |
| 11 PO not approved, 12 wrong authority | Ran (PO-1042, PO-1043) |
| 13 vendor mismatch | Ran PO vs bill; receipts carry no vendor |
| 14 tax | **Not run**: no tax on the bill listing |
| 15 damaged goods | Ran: all receipts "good" |

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, open bills at 30 Sep 2025, USD — **user-asserted**. Data source: **upload**. Legs: POs (single-line), receipts (goods only), bills (header only). Files: POs, receipts, bills, policy — accepted with limits above; `open_bills_2025-09-30_final.csv` **rejected** (shift rota). Tolerance: price 2%, qty exact, total 25; matrix as in policy file |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 done (header fields only); 2 done at header level; 3 done; 4 done, tests 9, 10, 14 not run; 5 proposals made; 6 tables in chat (offer `Match_Population_2025-09_NorthbrookTradingLtd.xlsx` — not "3Way", as two POs are two-way) |
| Not done | Line-level match (no bill lines); tax; paid-duplicate test; payment terms vs vendor master; tie of open bills to the AP control account — needs bill line detail, payment history, vendor master, AP ledger balance |
| Parameters | Tolerances and matrix from policy file; matching basis PO reference then vendor; population 12 open bills, 3–25 Sep 2025 |

Nothing has been paid, held, released, posted or sent. Every recommendation is for the AP manager to act on.
