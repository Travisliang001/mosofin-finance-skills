# 1099 preparation list — Northbrook Trading Ltd, reporting year 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. It is a computation for a qualified tax professional to review, not tax advice. Nothing has been filed, issued, sent, posted or changed. Tax identifiers appear masked, as supplied, and none is saved.

## (a) Read-back

Preparing the **2025 1099 list** for **Northbrook Trading Ltd** (payer, name as you stated it), under a **US-style 1099 regime**, for **1 January to 31 December 2025**, in **USD**, from **the files you uploaded**. Form in scope: **1099-NEC** only. Threshold **600 for the year**, from **"sample rate card v1, tax year 2025"**, which is marked fictitious test data, not real tax law. Card payments are excluded because the rule card says the card network reports them. Identifiers masked.

Intake questions the files do not answer, and the default applied:
- **Exact period of the payment data.** You gave the position as at 30 September 2025; the reporting year ends 31 December 2025. The payment file is headed `paid_2025` and does not say where it stops. I treat it as **year to date, not a complete year**. This list is therefore a preparation list, not a final one.
- **Filing channel and other currencies** — not answered. Output is a plain table in the currency paid (USD assumed for all).
- **Other forms (for example 1099-MISC for rent)** — no rule or threshold supplied, so none is applied.
- **Backup withholding rate and filing due dates** — not supplied; none stated.

What I received:
- `payments_by_vendor_2025.csv` — 12 vendors, total paid 950,780; 11 by ACH, 1 by card.
- `vendor_master.csv` — the same 12 vendors with entity type, tax form on file, masked tax ID; total 950,780.
- `information_return_rules_SAMPLE.md` — regime, year, the 1099-NEC rule and threshold, three exclusions.
- `payments_by_vendor_2025_final.csv` — 3 rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `payments_by_vendor_2025.csv` | Payment totals per vendor with entity type and method | No company or dates in it; "2025" from the header only | Columns clear; foots to 950,780. One total per vendor: no payment dates, no account or description | Steps 1, 4 | **Accepted with a limit**: cannot tell services from goods or rent, cannot check payment dates, cannot net credits or reimbursements |
| `vendor_master.csv` | Vendor list with form status, entity type, masked tax ID | No company named | Columns clear; totals and entity types agree with the payment file for all 12. No addresses, no legal names as on the form, no form dates | Steps 1, 3 | **Accepted with a limit**: form status is a flag, not the signed form; address and form validity cannot be checked |
| `information_return_rules_SAMPLE.md` | Rule card for the regime | Year 2025. Marked fictitious | Usable for 1099-NEC. Silent on LLC tax classification, rent, goods, backup withholding, due dates | Steps 1, 2 | **Accepted with a limit**: 1099-NEC only |
| `payments_by_vendor_2025_final.csv` | A four-week staff shift roster (E08–E10) | No company, year, vendor or amount | Not for this skill | No step uses it | **Rejected**. The name suggests the final payment file; the content is a rota. Set aside. If a final payment export exists, please upload it |

**Still missing:** nothing on the required checklist is absent, but the payment file needs its end date confirmed. Recommended and missing: the vendor tax forms themselves; ledger detail showing what each payment was for. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

Reconciliation: payment file 950,780 = vendor master 950,780; all 12 vendors agree line by line. No general ledger was supplied, so there is no tie-out to the books.

**1. Vendors that meet the 1099-NEC rule supplied (non-corporate, not paid by card, over 600)**

| Vendor | Entity type | Tax ID (masked) | Paid 2025 | Form on file | Status |
|---|---|---|---:|---|---|
| Brightline IT Services | Sole proprietor | \*\*-\*\*\*1111 | 41,800 | **none** | Reportable on the rule; **form missing** |
| Greyfriars Legal LLP | Partnership | \*\*-\*\*\*1259 | 27,400 | W-9 | Reportable on the rule (also legal services) |
| M. Okafor Consulting | Sole proprietor | \*\*-\*\*\*1185 | 18,500 | **none** | Reportable on the rule; **form missing** |
| Dale Cleaning Co | Sole proprietor | \*\*-\*\*\*1407 | 5,400 | W-9 | Reportable on the rule |
| Subtotal | | | **93,100** | | 4 vendors |

"Services" is read from the vendor names only; the files carry no account coding. Please confirm.

**2. Non-corporate vendors over the threshold that need a decision before they go on the list**

| Vendor | Entity type | Paid 2025 | Form on file | Why it is for review |
|---|---|---:|---|---|
| Orchard Packaging | LLC | 188,400 | W-9 | An LLC can be taxed as a corporation; the W-9 says which, and I have not seen it. The name suggests goods, which the 1099-NEC rule (services) does not cover |
| Halden Property Management | LLC | 81,000 | W-9 | LLC classification unknown. If this is rent it is not non-employee compensation; rent sits on another form (1099-MISC) for which no rule was supplied |
| Vale Marketing Studio | LLC | 9,200 | **none** | Services by name, so reportable if not taxed as a corporation; with no form on file the classification cannot be shown |
| Subtotal | | **278,600** | | 3 vendors |

All non-corporate, non-card vendors: 7 vendors, **371,700**. I have not decided the three in table 2 either way.

**3. Reportable or likely reportable vendors with no tax form on file**

Brightline IT Services 41,800, M. Okafor Consulting 18,500, Vale Marketing Studio 9,200: **69,500 across 3 vendors**. Without a W-9 there is no certified name, tax ID or entity type to report. Request the forms now. In a US-style regime a payee who does not certify can trigger backup withholding (holding back part of future payments); the rule card is silent on this, so please confirm the rule and rate with your tax professional. The master shows a masked ID for each of them; where that ID came from, if not a form, should be checked.

**4. Possible duplicate vendor: "Kestrel Supplies" and "Kestrel Supplies Inc."**

Two records with different masked IDs (ending 1000 and 1222): 412,300 with a W-9, and 6,480 with no form. Both are marked Corporation, so neither is reportable under the rule and the split does not change the list today. It should still be resolved: if they are one company the records should be merged (combined 418,780); if they are two, the second has no form on file and its "Corporation" type is unsupported.

**5. Excluded vendors**

| Vendor | Entity type | Method | Paid 2025 | Reason (per rule card) |
|---|---|---|---:|---|
| Kestrel Supplies | Corporation | ACH | 412,300 | Corporation, not legal services |
| Summit Freight | Corporation | ACH | 96,200 | Corporation |
| Northgate Utilities | Corporation | ACH | 22,100 | Corporation |
| Kestrel Supplies Inc. | Corporation | ACH | 6,480 | Corporation; entity type not evidenced by a form |
| Pinecrest Software | Foreign corporation | Card | 42,000 | Foreign payee with a W-8BEN-E on file; also paid by card, which the card network reports |
| Subtotal | | | **579,080** | 5 vendors |

Check: 93,100 + 278,600 + 579,080 = 950,780.

For Pinecrest, a foreign payee can fall under a non-resident withholding return instead of a 1099; no rule was supplied, so that is flagged for your tax professional, not assessed.

**6. Other points**
- **Greyfriars Legal LLP** is a partnership, so it is reportable on the general rule; the "corporations except legal services" exception is not needed. If any of the 27,400 was settlement money passed through the firm, it belongs in a different box; not determinable here.
- **Summit Freight** changed bank details on 16 September 2025. Not a 1099 matter, but worth confirming with the vendor by a known phone number.
- The threshold of 600 is far below every amount in the file; no vendor is near it.

## (d) What was not done, and why

- **No final reportable decision** for Orchard Packaging, Halden Property Management and Vale Marketing Studio — entity classification and payment nature are unclear; this skill lists them for review.
- **Form and box allocation beyond 1099-NEC Box 1** — no rule for 1099-MISC or any other form was supplied.
- **Services versus goods, reimbursements, vendor credits** — no ledger or payment detail.
- **Tie-out to the general ledger, vendor statements and prior-year filings** — not supplied.
- **Legal name, address, signed and current form, tax ID format** — the forms and addresses were not supplied; masked IDs cannot be format-checked.
- **Backup withholding reconciliation** — no withholding account or rule supplied. That is "not evidenced", not "nothing withheld".
- **Payments after the file's end date** — the list must be re-run on the full year to 31 December 2025.
- **Payer block (name, address, tax ID), filing channel, due dates** — not supplied.
- **Excel workpaper** — not created; say if you want it.
- **Filing or issuing any form** — never done by this skill. A person files after professional review.

**Data sources:** user-uploaded `payments_by_vendor_2025.csv`, `vendor_master.csv`, `information_return_rules_SAMPLE.md` (rules: "sample rate card v1, tax year 2025", fictitious sample). No ledger read.
