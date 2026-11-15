# Duplicate invoice scan — Northbrook Trading Ltd — open bills at 30 September 2025, with 12 months of payments

Mosofin is not connected, so this run is manual: every rule is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read bills, payments and the vendor master directly ([docs.mosofin.com](https://docs.mosofin.com)). Nothing has been held, voided, merged or paid; every action below is a **proposal**.

## Read-back

Scanning **Northbrook Trading Ltd** (user-asserted), **USD** (user-asserted; no file states a currency): the **12 open bills at 30 September 2025**, compared with **12 months of paid bills (Oct 2024 – Sep 2025)** so duplicates straddling the period are caught. Defaults stated, not asked: **sensitivity Standard** (flag High and above; Medium matches listed for review), **Rule 3 window 7 days**. No recurring-supplier list or prior cleared clusters supplied. **Rule 7 (same bank account, different vendors) will not run** — no bank details are available. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `open_bills_2025-09-30.csv` | AP open-bill listing: 12 bills, 3 – 25 Sep 2025, vendor invoice numbers, PO where present; total **255,264** | No entity or currency | Yes | Rules 1–6, 8 | **Accepted with a limit**: company user-asserted |
| `bill_payment_history_12m.csv` | Paid bills, 96 rows, 8 vendors × 12 monthly bills, Oct 2024 – Sep 2025; total **872,076** | No entity or currency | Yes, but **no payment method** and the bill numbers (3000–3361, in blocks of 50 per vendor) look like **internal system numbers, not vendor invoice numbers** | Rules 1–3, 5, 9; paid status | **Accepted with a limit**: company user-asserted; Rule 9 degrades to Rule 2; open-vs-paid invoice-number match not possible; **population incomplete** (see below) |
| `vendor_master.csv` | Vendor master, 12 vendors: terms, tax form, entity type, **date bank details changed**, paid 2025, masked tax ID | No entity | Yes. No addresses, no active/inactive flag, no bank details | Rule 4, Step 4 aliases, population check | **Accepted with a limit**: company user-asserted; address and inactive-record checks not possible |
| `open_bills_2025-09-30_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a bill listing, despite its name | None | n/a | No step uses it | **Rejected.** If a later bill listing exists, upload it instead |

**Population gap — the payment history is not the whole population.** The vendor master shows **950,780 paid in 2025**; the history shows **661,905** paid in 2025 — **288,875 missing**. Four vendors (Vale Marketing 9,200, Northgate Utilities 22,100, Pinecrest Software 42,000, Dale Cleaning 5,400) have 2025 payments and no history at all, and every other vendor's history falls short of its master total. A scan of a partial population can return false negatives that look clean.

**Still missing:** the **complete paid-bill register for 2025 with vendor invoice numbers and payment method** (required for a full scan and Rule 9); **vendor credits** (Rule 10); **vendor addresses and active/inactive status**; your list of known recurring suppliers. Would wait here; proceeding on the accepted files.

## Flagged clusters — unpaid first

| Cluster | Records side by side | Rule | Confidence | Amount | Paid? | Proposed action |
|---|---|---|---|---:|---|---|
| **C1** | Kestrel Supplies `INV-4471`, 5 Sep 2025, 6,480, no PO **vs** Kestrel Supplies Inc. `INV4471`, 6 Sep 2025, 6,480, no PO | **Rule 6** (same number `INV4471` once punctuation is removed, two vendor records) + Rule 4 (same amount, names Jaro-Winkler **0.95**) | **High** | 6,480 each; cluster 12,960 | **Both open** | **Hold one before payment** and confirm with Kestrel; costs nothing to fix now. Two findings: a duplicate bill and a duplicate vendor record |
| **C2** | Summit Freight `INV-4644`, 7 Sep 2025, **23,449**, PO-1042 — vendor **bank details changed 16 Sep 2025**, after the bill and before it falls due (7 Oct) | Fraud-adjacent pattern (not a duplicate rule) | **High risk** | 23,449 | Open | **Do not pay until the bank change is verified by call-back** to a contact on file from before the change. Also: bill is 2.9× Summit's usual monthly 8,017, and due 30 days after the bill against Summit's 15-day terms |

**Listed for review (Medium/Low, below the Standard threshold):**
- **Different vendors, identical amounts, same month:** Summit Freight `INV-4644` and Pinecrest Software `INV-5212`, both 23,449 (7 and 23 Sep); Brightline IT `4715` and Northgate Utilities `5141`, both 13,027 (9 and 21 Sep). Names are not similar, so no alias rule fires; possibly coincidence, worth a glance before paying.
- **Rule 5 sequence:** Kestrel Supplies `INV-4471` (5 Sep) carries a lower number than `4502` (3 Sep) and a different format. Explained if C1 is a re-keyed old invoice — another reason to check it.

**Exposure:** High — **6,480 unpaid** (C1, one copy); plus **23,449 at payment-diversion risk** (C2). Already-paid duplicates found: **none** in the history supplied — on an incomplete population.

## Vendor aliases to merge (proposal — Mosofin cannot merge)

| Group | Records | Evidence | Recommendation |
|---|---|---|---|
| A1 | Kestrel Supplies / Kestrel Supplies Inc. | Name differs only by "Inc." (JW 0.95); both Corporation, 30 days; **Kestrel Supplies has a W-9 and tax ID ending 1000, "Kestrel Supplies Inc." has no tax form and no tax ID**; same invoice number in C1 | Confirm with Kestrel whether "Inc." is the same legal entity. If yes, merge into the record with the W-9 and clean up retroactively. If no one at Kestrel recognises the second record, treat it as a **possible fictitious vendor** — it has been paid 540 monthly (6,480 in 2025 per master) |

## Recurring patterns — not flagged

All eight vendors in the history bill an **identical amount every month, about 30 days apart**, with a new number each time (e.g. Halden Property Management 6,750 rent; Kestrel Supplies 34,358). That is a recurring pattern, not a duplicate; no overlaps within 7 days. Please confirm which are contracted recurring charges so they can be stored as such.

Also noted (vendor hygiene, not duplicates): **no tax form on file** for Brightline IT Services and M. Okafor Consulting (sole proprietors), Kestrel Supplies Inc. and Vale Marketing Studio.

## Rules run

| Rule | Ran? | Records | Matches |
|---|---|---:|---|
| 1 Exact number + same vendor | Ran on open bills; **not** open-vs-paid (history numbers are internal) | 108 | 0 |
| 2 Same amount + vendor + date | Ran | 108 | 0 |
| 3 Same amount + vendor within 7 days | Ran | 108 | 0 (C1 matched under Rules 4/6) |
| 4 Same amount + similar vendor | Ran | 108 | 1 (C1) |
| 5 Sequence anomaly | Ran on open bills only (numbering differs between files) | 12 | 1 (review) |
| 6 Same number across vendors | Ran | 108 | 1 (C1) |
| **7 Same bank account** | **Not run** — no bank details. **Owner: AP manager, in the AP or banking system.** A clean scan does not mean this fraud test passed | — | — |
| 8 Round-number clusters | Ran | 108 | Recurring only, filtered |
| 9 Two payment channels | **Degraded to Rule 2**: no payment method | 96 | 0 |
| 10 Unapplied credit memo | **Not run**: no credits supplied | — | — |

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, USD — **user-asserted**. Data source: **upload**. Open bills, history, vendor master accepted with limits; `open_bills_2025-09-30_final.csv` **rejected** (shift rota). Sensitivity Standard; N = 7 |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Population | 12 open + 96 paid = **108 records scanned**; available per vendor master: **288,875 of 2025 payments not supplied** |
| Steps 1–5 | Done with the limits above; Step 5 recovery: nothing paid twice found |
| Not done | Rule 7, Rule 10, Rule 9 (degraded), open-vs-paid number match, inactive vendors, addresses |

**Data sources:** upload — `open_bills_2025-09-30.csv`, `bill_payment_history_12m.csv`, `vendor_master.csv`.
