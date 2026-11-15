# Invoice extraction — Northbrook Trading Ltd — 1 invoice

Mosofin is not connected, so this run is manual: extraction is from your document, and every validation is against the files you uploaded, not the books. Connecting Mosofin would check posted bills, payments and coding history directly ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Extracting invoices billed to **Northbrook Trading Ltd** (user-asserted; Bill-To validation target), period **September 2025**, entity currency **USD** (user-asserted), from **your uploads**. Output format not stated — default **xlsx**, offered below, tables here meanwhile. Validation against `vendor_master.csv` only; **no posted bills or payments were supplied**, so the duplicate and already-paid checks can only use what the vendor master shows.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `invoice_kestrel_INV-4471.txt` | A vendor invoice (text): Kestrel Supplies, INV-4471, 1 line, total 6,480.00 USD; 1 page | Bill to Northbrook Trading Ltd; dated 5 Sep 2025 — matches intake | Yes; legible, foots | Steps 1–6 | **Accepted** |
| `vendor_master.csv` | Vendor master: 12 vendors — terms, tax form, entity type, bank-change date, paid 2025, masked tax ID | No entity named; no date | Yes; **no bank details, no addresses** | Validation: vendor match, terms, duplicate-vendor signal | **Accepted with a limit**: company user-asserted; cannot support address, remit-to or bank comparison |
| `invoice_kestrel_INV-4471_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not an invoice or invoice extract despite its name | None | n/a | No step uses it | **Rejected.** If another invoice was meant, upload the document itself |

**Still missing:** (1) **posted bills / open AP and September payments** for Kestrel Supplies and Kestrel Supplies Inc. — needed for the duplicate and already-paid checks (the highest-value checks here); (2) open purchase orders, for PO matching (no PO number appears on the invoice). I would wait here; proceeding on the accepted files as instructed.

## Extracted invoice (Sheet 1)

| Field | Value |
|---|---|
| Vendor | Kestrel Supplies |
| Vendor tax ID | null (not on invoice) |
| Vendor address | null (not on invoice) |
| Invoice # | INV-4471 |
| Invoice date | 2025-09-05 |
| Due date | 2025-10-05 (calculated: Net 30; not printed) |
| Payment terms | Net 30 |
| Bill to | Northbrook Trading Ltd |
| PO # | null |
| Currency | USD (explicit ISO code) |
| Subtotal | 6000.00 |
| Tax | 480.00 (sales tax 8%, single rate, no jurisdiction named) |
| Shipping / discount | null / null |
| Total due | 6480.00 |
| Tax-inclusive? | No (tax added to subtotal) |
| Remit to | "account ending 4471" — masked here as shown |
| Document type / confidence | Invoice · **High** (clear, all printed fields read) |

**Line items (Sheet 2):** 1 line — qty **300**, "Steel bracket SB-20", product code SB-20, unit price **20.00**, subtotal **6000.00**; no service period (goods).

**Math check:** 300 × 20.00 = 6,000.00; 6,000.00 × 8% = 480.00; 6,000.00 + 480.00 = **6,480.00 = total due. Foots.**

**Source (Sheet 4):** `invoice_kestrel_INV-4471.txt`, 1 page, text — no OCR needed.

## Validation results (Sheet 5)

| Check | Result | Evidence | Verdict |
|---|---|---|---|
| Vendor match | **Matches two records**: "Kestrel Supplies" (terms 30, W-9, tax ID ending 1000, paid 2025 412,300) **and "Kestrel Supplies Inc."** (terms 30, **no tax form**, paid 2025 **6,480**) | vendor_master.csv | **Duplicate vendor record** — history split, duplicate check weakened |
| Duplicate / already paid | **Not run against bills or payments (none supplied).** Signal: Kestrel Supplies Inc. shows **6,480 paid in 2025 — exactly this invoice's total** | vendor_master.csv `paid_2025` | **Possible prior payment of this invoice under the duplicate record — resolve before paying** |
| Bill-To | Northbrook Trading Ltd = entity named at intake | Invoice | Matches |
| Terms | Net 30 = vendor master 30 days | vendor_master.csv | Matches |
| PO match | No PO # on invoice; no PO file supplied | — | Not run |
| Currency | USD explicit; entity currency USD | Invoice | Plausible |
| Remit-to vs vendor master | Invoice gives only "account ending 4471"; vendor master holds no address or bank details. Note the account ending **4471 equals the invoice number** | — | Cannot compare — worth a question |
| **Bank-detail comparison** | **NOT RUN** — no vendor bank details or prior Kestrel invoices supplied. It would show whether account ending 4471 is the account Kestrel has been paid to. Perform it against the vendor's banking record in the payment system; verify any change **by phone on a known number, never one on the invoice** | — | **NOT RUN** |

**Validation status: Review** — not Clean. It becomes **Stop** if the 6,480 paid to "Kestrel Supplies Inc." turns out to be this invoice. Extraction confidence (High) and validation status are separate: this is a clear document with an open question.

## Proposed next steps (proposals only — nothing entered)

1. Pull Kestrel Supplies and Kestrel Supplies Inc. bills and payments for 2025 and look for INV-4471 / 6,480 under either record. Do not pay until resolved.
2. Ask AP whether "Kestrel Supplies Inc." is the same supplier; if so, merge in your system (your action, not mine) so the history is not split. It also has no tax form on file.
3. Confirm "account ending 4471" against Kestrel's known bank record by phone.
4. GL coding: inventory purchase (SB-20) — hand to `gl-coding-assistant` if wanted.

## Not done, and why

Duplicate and already-paid checks against posted bills and payments (not supplied). PO match (no PO number, no PO file). Bank-detail comparison (NOT RUN — no bank records). Coding from history (no ledger). Workbook `Invoices_Extracted_2025-09-30_1invoices.xlsx` offered; not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Invoice: accepted. Vendor master: accepted with limit. `invoice_kestrel_INV-4471_final.csv`: **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 vendor master only · 1 done (1 document, 1 page) · 2 done (tax ID, address, PO null) · 3 done (1 line) · 4 done, foots · 5 remit-to captured; **bank check NOT RUN** · 6 done: Invoice, one-time (no history), High; status **Review** · 7 tables here; xlsx offered · 8 not offered |
| Not done | Posted bills and payments; POs; vendor bank records; coding history |

Nothing was posted, sent or changed. **Data sources:** upload — `invoice_kestrel_INV-4471.txt` (p. 1), `vendor_master.csv`.
