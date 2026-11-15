# Internal audit — purchase-to-pay compliance — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every procedure is `[manual]` on your uploads. Connecting Mosofin would pull the bill, PO and vendor populations directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

**Compliance** audit of **purchase-to-pay** at **Northbrook Trading Ltd** (user-asserted), **September 2025** (as at 30 Sep 2025), **USD** (user-asserted), from **your uploads**. From `purchasing_policy.md` (facts inside a file; please confirm): criteria are **policy clauses 1–5**; performed by **internal audit, who did not operate this area**; **completeness is out of scope**. Objective (from the audit type): *assess compliance of September purchasing, receiving and bills with the purchasing policy.*

Not answered: **E — how the process works and prior audit findings.** Default applied: planned from the data alone; **walkthrough not done**; repeat findings cannot be identified. Also unknown: **who holds the CEO approval** (clause 2) — needed to test approval limits.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | Open bills: 12 rows, 10 vendors, bill dates 3–25 Sep 2025, total **255,264**; PO reference on 5 | No entity or currency; date from name and rows | Yes. **Open bills only** — no paid bills, so clause 3 (receipt before payment) is tested on what is about to be paid | P1, P3, P4, P5 | **Accepted with a limit**: company user-asserted; paid September bills not included |
| `purchase_orders.csv` | Purchase orders: 5 POs (PO-1040–1043, 1045), qty, price, approver, approval date | No entity; approval dates 25 Aug–12 Sep 2025 | Yes; **no order-placed date** and no approver role | P1, P2, P3 | **Accepted with a limit**: "approved before order placed" tested against receipt and bill dates instead |
| `goods_receipts.csv` | Goods received notes: 3 GRNs (GRN-771, 772, 774), 4–10 Sep 2025 | No entity | Yes | P3, P4 | **Accepted with a limit**: company user-asserted |
| `vendor_master.csv` | Vendor master: 12 vendors, terms, tax form, entity type, **bank details changed on**, paid 2025 | No entity | Yes; **no "created by" field**, no payment approver | P5, P6, P7 | **Accepted with a limit**: clause 5 not testable from it |
| `purchasing_policy.md` | Purchasing policy, 5 clauses, plus auditor and scope statement | No entity or date | Yes — the criteria | Every finding | **Accepted** (criteria user-supplied) |
| `purchase_orders_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not purchase orders despite its name | None | n/a | No procedure uses it | **Rejected.** If a revised PO file exists, upload it instead |

**Still missing:** (1) **approver roles / CEO name** (clause 2); (2) **paid bills and payment approvals** for September (clause 3 on payments made; clause 5); (3) **vendor creation log** — who created each vendor (clause 5); (4) **telephone verification evidence** for bank-detail changes (clause 4); (5) process notes and prior audit report (E). I would wait here; proceeding on the accepted files as instructed.

## Audit program (full population wherever readable — no sampling)

| Ref | Clause | Procedure | Type | Population | Result |
|---|---|---|---|---|---|
| P1 | 1 | Every bill > 1,000 has a PO | Re-perform | 12 bills, 255,264 (100%) | **7 exceptions, 80,702** |
| P2 | 1 | Every PO approved, and approved before receipt / bill | Inspect | 5 POs (100%) | **2 exceptions** (PO-1042, PO-1043) |
| P3 | 2 | Approver within limit (manager ≤ 10,000; CEO above) | Inspect | 5 POs | **Not concluded** — 3 POs > 10,000; roles unknown |
| P4 | 3 | Bill quantity ≤ quantity receipted | Re-perform | 5 PO-backed bills | **1 exception** (PO-1041); 2 services with no GRN |
| P5 | 4 | Bank-detail changes verified by phone | Inspect + inquire | 1 change (Summit Freight) | **Not testable from data** — evidence needed |
| P6 | 5 | Vendor creator ≠ payment approver | Inspect | — | **Not testable** — no creator or approver data |
| P7 | — | Duplicate vendors and bills (analytical) | Analyse | 12 vendors, 12 bills | 1 pair (observation) |
| P8 | all | Walkthrough; inquiry for causes | Observe / inquire | — | **Not done** — auditor fieldwork |

No trial balance was uploaded, so the 255,264 of open bills is not tied to the accounts-payable balance; completeness of the bill population is out of scope and **not** claimed.

## Findings (proposed — condition, criteria, consequence; cause and rating are yours)

**F1 — Seven bills totalling 80,702 have no purchase order.** *Condition:* Greyfriars Legal 15,633; Vale Marketing 10,422; Northgate Utilities 13,027; Pinecrest Software 23,449; Dale Cleaning 5,211; Kestrel Supplies INV-4471 6,480; Kestrel Supplies Inc. INV4471 6,480 — **7 of 12 bills, 31.6% of open bill value**, every one over 1,000. *Criteria:* clause 1. *Consequence:* 80,702 committed with no evidenced pre-approval. *Cause:* not determined — ask (utilities and legal may be treated as exempt in practice; the policy grants no exemption). Proposed rating: **high**.

**F2 — PO-1042 (Summit Freight, 23,449) has no approver and no approval date.** *Criteria:* clauses 1 and 2 (above 10,000 needs the CEO). *Consequence:* 23,449 unapproved, and the bill (due 22 Sep) is **overdue and open** for a vendor whose **bank details changed on 16 Sep 2025** — after the bill was received. No telephone verification is evidenced (clause 4). Paying this bill to the new details before verification is the classic payment-diversion pattern. Proposed rating: **high**. Recommendation: hold payment until the change is verified on a known number.

**F3 — PO-1043 (Brightline IT, 13,027.02) was approved on 12 Sep, after the bill (9 Sep) and the receipt (10 Sep).** *Criteria:* clause 1 (approval **before** the order). The PO documents a purchase already made. It is also above 10,000 and approved by J. Marsh — compliant only if J. Marsh is the CEO. Proposed rating: **medium**.

**F4 — PO-1041 (Orchard Packaging): billed for 100 cartons, 90 receipted.** Bill 41,687 = 100 × 416.87; GRN-772 shows 90. **4,168.70 billed for goods not received.** *Criteria:* clause 3. The bill is open, so the breach is prevented only if payment is held to 37,518.30 or a credit note is obtained. Proposed rating: **medium**.

**Pending — approval limits (clause 2).** PO-1040 87,016.80 and PO-1041 41,687.00 (A. Reyes) and PO-1043 13,027.02 (J. Marsh) are all above 10,000. Compliant only if the approver is the CEO; tell me who is and I will conclude.

## Observations (no criterion in the policy, so not findings)

- **Possible duplicate:** Kestrel Supplies INV-4471 (5 Sep) and **Kestrel Supplies Inc.** INV4471 (6 Sep), 6,480 each. Kestrel Supplies Inc. is a second vendor record with no tax form, already paid **6,480** in 2025. Exposure **6,480** on the open pair, possibly more on the earlier payment. Route to AP for review before payment.
- **PO-1040 billed 1,566.20 over the PO:** 88,583 vs 4,000 × 21.7542 = 87,016.80 (22.1458 a unit, +1.8%). The policy sets no price tolerance.
- **Sequence gaps:** PO-1044 and GRN-773 are missing from the files. Ask whether they were cancelled.
- **No tax form on file** for Brightline IT, M. Okafor Consulting, Kestrel Supplies Inc. and Vale Marketing Studio — outside this policy; relevant to 1099 work.

No exceptions in a test is not evidence that a control operated: nothing here shows clauses 4 and 5 work.

## Not done, and why

Causes, final ratings and management responses (auditor and management, by asking — not inferred). Walkthrough (P8). Clause 4 and 5 testing (no verification log, no vendor-creation or payment-approval data). Clause 2 conclusion (approver roles). Clause 3 on paid bills (no paid-bill file). Repeat-finding check (no prior report). Report as a document and workpapers `Internal_Audit_P2P_2025_Northbrook Trading Ltd.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Bills, POs, GRNs, vendor master: accepted with limits; policy: accepted. `purchase_orders_final.csv`: **rejected** (shift rota). Independence: internal audit did not operate the area (per policy file). Completeness out of scope |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done on uploads · 1 plan done · 2 from data only, **walkthrough not done** · 3 program done (full population) · 4 workpapers P1–P4, P7 done; P5, P6 **not testable** · 5 F1–F4 condition / criteria / consequence; **cause not obtained** · 6 ratings **proposed only** · 7 **not done** (no management responses) · 8 structure above · 9 follow-up: test definitions P1–P7 as above, to re-run · 10 tables here; xlsx offered · 11 not offered |
| Not done | Approver roles; paid bills; vendor creation log; phone-verification evidence; prior audit report; walkthrough and interviews |

Nothing was posted, sent or changed. **Data sources:** upload — `open_bills_2025-09-30.csv`, `purchase_orders.csv`, `goods_receipts.csv`, `vendor_master.csv`, `purchasing_policy.md`.
