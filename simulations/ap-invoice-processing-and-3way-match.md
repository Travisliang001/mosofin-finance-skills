# AP invoice processing and match — Northbrook Trading Ltd, September 2025 bills

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would automate the bill, PO and vendor reads — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Period:** September 2025, as at 2025-09-30. **Currency:** USD. **Data source:** upload only.
- **B:** bills already entered (12 open bills). **F:** run the batch (no SOP drafted).
- **C — receipts:** goods-receipt notes uploaded for 3 POs. Service POs (freight, consulting) need a signed service confirmation; none uploaded, so those are **2-way only**.
- **D — tolerance**, from your `approval_matrix_and_tolerances.md`: **price 2%, quantity exact, total 25**. Taken as **both** tests must pass (the stricter reading); where that decides an exception I show the other reading too. Please confirm.
- **E — approvals**, same file: J. Marsh (manager) up to 10,000; A. Reyes (CEO) above 10,000. These are PO approvals; no bill-level approval evidence was supplied.
- Not given: PO-required threshold; capitalisation threshold; vendors exempt from matching. None assumed.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | 12 entered bills, total 255,264: vendor, number, dates, amount, PO link | No entity/currency in file; dated 3-25 Sep 2025 | Yes, but **no line detail, tax, or account coding** | Steps 1, 3, 4 | **Accepted with a limit:** unit price inferred as total ÷ PO quantity; coding cannot be reviewed |
| `purchase_orders.csv` | 5 POs with item, qty, unit price, approver, date | No entity in file; Aug-Sep 2025 | Yes | Step 4 (match), Step 2/7 (approval) | **Accepted with a limit:** company user-asserted; PO-1044 missing from sequence |
| `goods_receipts.csv` | 3 GRNs (771, 772, 774) | No entity; 4-10 Sep 2025 | Yes | Step 4 (3-way) | **Accepted with a limit:** GRN-773 missing from sequence; no service confirmations |
| `vendor_master.csv` | 12 vendors: terms, tax form, entity type, bank-change date | No entity in file | Yes | Steps 2, 3 | **Accepted with a limit:** company user-asserted |
| `chart_of_accounts.csv` | 36 accounts with type | No entity in file | Yes | Step 6 (coding) | **Accepted with a limit:** no utilities or cleaning account |
| `approval_matrix_and_tolerances.md` | Approval limits and tolerances (typed policy) | Names no company or date | Yes | Steps 4-5, 7 | **Accepted with a limit:** a summary of policy, user-supplied; figures used once you confirm the read-back |
| `open_bills_2025-09-30_final.csv` | **Not a bill listing.** employee, week_1..week_4 with nights/days/off for E08-E10 — a staff shift rota | No company, period or amounts | No | No step uses it | **Rejected** on content, despite the name. Upload the later bills listing if one exists |

**Still missing:** signed service confirmations for PO-1042 (freight) and PO-1045 (consulting); bill-level approvals; invoice images or line detail (tax and line checks); the PO-required threshold.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Match results (5 PO-linked bills, 174,562; links are on the bill, so **linked**, not inferred)

| Bill | Vendor | PO value | Received | Billed | Match type | Verdict |
|---|---|---|---|---|---|---|
| 4502 | Kestrel Supplies | 4,000 x 21.7542 = 87,016.80 | 4,000 (GRN-771) | 88,583.00 | **3-way** | **Exception — price.** 22.1458/unit, +1.80% (inside 2%) but total +1,566.20 (over 25). Exception under the both-tests reading; within tolerance if price % alone governs |
| INV-4573 | Orchard Packaging | 100 x 416.87 = 41,687.00 | **90** (GRN-772) | 41,687.00 | **3-way** | **Exception — quantity.** Billed 100, received 90: **4,168.70 billed for cartons not received.** Hold that part; 37,518.30 matches |
| INV-4644 | Summit Freight | 23,449.00 | no service confirmation | 23,449.00 | **2-way only** | Amount matches. **Exceptions:** PO has **no approver** (23,449 needs CEO approval); no service confirmation; **bank details changed 16 Sep 2025**; bill due date is 30 days vs **15-day terms** |
| 4715 | Brightline IT | 6 x 2,171.17 = 13,027.02 | 6 (GRN-774) | 13,027.00 | **3-way** | Amounts match (−0.02). **Exception — approval:** PO approved by J. Marsh, whose limit is 10,000, for 13,027.02; and approved **12 Sep, after the bill (9 Sep) and receipt (10 Sep)** — an after-the-fact PO. No W-9 on file |
| INV-4857 | M. Okafor Consulting | 7,816.00 | no service confirmation | 7,816.00 | **2-way only** | Amount matches; approver within limit. **Exception:** no signed service confirmation; no W-9 (sole proprietor) |

**This batch is a 3-way match for 3 bills (143,297) and a 2-way match for 2 (31,265).** It is not a 3-way match overall.

### Bills with no PO (7 bills, 80,702) — not matched

Greyfriars Legal INV-4999 15,633; Vale Marketing INV-5070 10,422; Northgate Utilities 5141 13,027; Pinecrest Software INV-5212 23,449; Dale Cleaning INV-5283 5,211; Kestrel Supplies INV-4471 6,480; Kestrel Supplies Inc. INV4471 6,480. With no PO-required threshold given, I cannot say which needed a PO; each needs a manager or CEO approval under the matrix (four exceed 10,000), and no approval evidence was supplied.

### Intake, vendor and field checks

1. **Duplicate:** Kestrel Supplies INV-4471 (5 Sep) and Kestrel Supplies Inc. INV4471 (6 Sep), 6,480 each — same number without the hyphen, second vendor record with no tax form or tax ID. Treat as one invoice until the payee is confirmed.
2. **Bank-detail change — Summit Freight, 16 Sep 2025.** Verify by phone on a number already on file before any payment. This control is a gap for the AP manager, not a check performed here.
3. **Terms vs due date:** Summit 15 days (due 22 Sep, not 7 Oct); Northgate 21 days (due 12 Oct, not 21 Oct).
4. **Tax forms missing:** Brightline, M. Okafor, Kestrel Supplies Inc., Vale Marketing. Pinecrest is a foreign corporation (W-8BEN-E).
5. **Sequence gaps:** PO-1044 and GRN-773 — confirm neither exists.

### Exception matrix

| Exception | Bills | Tolerance | Owner | Evidence that closes it |
|---|---|---|---|---|
| Price/total variance | 4502 (+1,566.20) | 2% / 25 | AP manager → buyer | Corrected invoice or buyer approval of the new price |
| Quantity variance | INV-4573 (10 cartons, 4,168.70) | exact | AP manager → receiving | GRN for the 10 cartons, or credit note |
| PO approval missing / over limit / after the fact | INV-4644, 4715 | matrix | CEO | CEO sign-off |
| Service not confirmed | INV-4644, INV-4857 | — | AP manager | Signed service confirmation |
| Bank-detail change | INV-4644 | — | AP manager | Call-back verification |
| Duplicate | INV-4471 / INV4471 | — | AP manager | Vendor statement; void one in your system |

### Proposed coding — PROPOSAL, not posted (bills carry no coding to review)

Dr 1200 Inventory: Kestrel 88,583 (or 87,016.80 if price not approved), Orchard 41,687. Dr 6900 Postage and Delivery: Summit 23,449 (or 1200 if freight-in is capitalised). Dr 1500 Fixed Assets - Cost: Brightline laptops 13,027 (subject to your capitalisation threshold). Dr 6400 Professional Fees: Okafor 7,816, Greyfriars 15,633. Dr 6200 Marketing: Vale 10,422. Dr 6300 Software: Pinecrest 23,449. Northgate (utilities) and Dale (cleaning): **no matching account in your chart — please name one**. Cr 2000 Accounts Payable throughout. No tax line: no tax data on the bills.

**KPIs:** first-pass match rate on the 5 PO bills: **2 of 5** pass the amount match cleanly (4715, INV-4857); **0 of 5** pass with controls included. Population: 5 PO-linked bills dated 3-13 Sep 2025. Cycle time: not computed (no payment data).

## (d) What was not done, and why

- **Line-level, tax and total-math checks**: no invoice lines or tax on the bills.
- **Coding review**: bills carry no account; coding above is a proposal, not a review.
- **Bill approvals, bank-detail verification, tax-form validity, service confirmations**: `[manual]` controls with named owner (AP manager); not performed.
- **Cycle time**: no payment history.
- **SOP / Word procedure**: not drafted — you asked to run the batch. **Excel** `AP_InvoiceProcessing_2025-09-30.xlsx`: not created — say yes if you want it.
- **Nothing was posted, approved, paid, held or changed.** Every verdict and entry is a proposal.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD — user-asserted. Source: upload. 6 files accepted with a limit; `open_bills_2025-09-30_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (duplicate found; fraud signals limited to the bank-change date); 2 done with a limit; 3 done for terms only; 4 done — 3-way for 3, 2-way for 2, none for 7; 5 done; 6 proposed, not reviewed; 7 references only |
| Not done | Tax and line checks (invoice images); approvals (sign-off records); service confirmations; cycle time (payment history) |

**Data sources:** user uploads — `open_bills_2025-09-30.csv`, `purchase_orders.csv`, `goods_receipts.csv`, `vendor_master.csv`, `chart_of_accounts.csv`, `approval_matrix_and_tolerances.md`.
