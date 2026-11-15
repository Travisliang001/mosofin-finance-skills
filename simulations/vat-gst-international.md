# VAT workpapers — Northbrook UK Ltd, Q3 2025 (July–September), GBP (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. **This is a computation for a qualified tax professional to review, not tax advice.** Nothing was filed, paid, registered or posted; every figure below is a proposal.

## Read-back

Preparing the **Q3 2025 VAT return** workpapers for **Northbrook UK Ltd**, registered in **one country since 2019** (the country is not named in any file; I take it as the UK from the company name, user-asserted), from **your uploaded transaction listing**. Rates from **'sample rate card v1, tax year 2025'**: standard 20%, exports of goods zero-rated, staff entertainment blocked. **No partial exemption, no special schemes, quarterly returns** (all from your rules file; used once you confirm this read-back). Establishment (question D) not answered: I treat the home country as the only establishment. E-invoicing obligations not answered: I assumed none. Zero-rated and exempt treatment taken from the tax codes as recorded; I did not review it.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `vat_transactions_2025-Q3.csv` | Sales and purchase listing with net, VAT code and VAT: 3 sales, 4 purchase lines (one is a reverse-charge output posting) | No company or currency named; dated 14 Jul – 19 Sep 2025, inside Q3 | Yes. Every VAT amount recomputes at its code (98,000 × 20% = 19,600; 41,000 × 20% = 8,200; 6,000 × 20% = 1,200; 900 × 20% = 180). No counterparty country or VAT numbers | Yes: Steps 3–5, 7 | **Accepted with a limit**: company/currency user-asserted; place of supply and customer VAT numbers cannot be checked |
| `vat_rules_SAMPLE.md` | Rate card and rules summary, with source and year; also states the VAT control balance at 30 Sep 2025 (11,580 payable) | Tax year 2025; country not named | Yes as a summary. Marked fictitious sample rates. The control balance is one figure, not account detail | Yes: rates (Steps 3, 5), reconciliation (Step 8) | **Accepted with a limit**: rates used only as you supplied them; control balance user-supplied, not evidenced |
| `vat_transactions_2025-Q3_final.csv` | **Not a VAT listing.** A staff shift rota: employees E08–E10, week_1–week_4, nights/days/off | No company, dates or amounts | No | No step uses it | **Rejected** on content. If a final transaction listing exists, please upload it; otherwise I use `vat_transactions_2025-Q3.csv` |

Still missing: **VAT control account detail** (required for the reconciliation; only a closing balance arrived); prior returns filed (recommended); customer and supplier countries and VAT numbers; proof of export for the zero-rated sale.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. Registration (Step 1).** One registration, since 2019, user-asserted. The listing shows supplies in one country plus one export and one EU service purchase; no evidence of supplies requiring a second registration. Thresholds were not supplied and none are needed for this population.

**2. Output VAT (Step 3).**

| Rate category | Net | VAT |
|---|---:|---:|
| Standard 20% (UK customer A 60,000; UK customer B 38,000) | 98,000 | 19,600 |
| Zero-rated — export of goods to Northbrook Trading Ltd (2 Aug) | 14,570 | 0 |
| Exempt | none recorded | — |
| **Total sales** | **112,570** | **19,600** |

The zero-rated export is to a **related company**. Zero-rating needs proof of export, which is not in the listing — `[manual]` check. If proof is missing the VAT at 20% would be 2,914, borne by the supplier.

**3. Reverse charge (Step 4/4b).** EU software vendor, 5 Sep, net 6,000: **both legs are booked** — input 1,200 and output 1,200 — so the net-nil check **passes (1,200 − 1,200 = 0)**. Both legs must still appear on the return: output tax includes 1,200 and input tax includes 1,200. Note the output leg is posted as a "purchase" line with VAT −1,200; on the return it belongs with output tax, not as a negative input. Supplier VAT number and country not recorded.

**4. Input VAT (Step 5).** Since no exempt supplies are recorded, Step 5b (partial exemption) is not triggered and full recovery is consistent.

| Item | Net | VAT | Recoverable |
|---|---:|---:|---:|
| UK supplier, 22 Jul | 41,000 | 8,200 | 8,200 |
| EU software vendor (reverse-charge input leg) | 6,000 | 1,200 | 1,200 |
| Staff entertainment, 19 Sep — **blocked** per your rules | 900 | 180 | **0** |
| **Total** | **47,900** | **9,580** | **9,400** |

The 180 on staff entertainment is **not recoverable** and is excluded; it is a cost.

**5. Proposed return figures (Step 7) — for review, not filed**

| Line | Amount |
|---|---:|
| Output VAT: sales 19,600 + reverse charge 1,200 | **20,800** |
| Input VAT recoverable: 8,200 + reverse charge 1,200 | **9,400** |
| **Net VAT payable** | **11,400** |
| Total sales, net of VAT | 112,570 |
| Total purchases, net of VAT | 47,900 |

**6. Reconciliation to the VAT control account (Step 8).** Control balance per your rules file: **11,580 payable**. Computed Q3 liability: **11,400**. **Difference: 180 — equal to the blocked entertainment VAT.** If the 180 had been recovered through the control account, the balance would be 11,220 (180 *below* the return), not 180 above it; so the 180 more likely reflects an opening balance or another posting. It cannot be resolved without the control account detail. The collected-not-remitted test (does the account clear each quarter?) **could not run**: one balance, no movements, no prior returns.

**7. Detections**

| Detection | Population | Value | Cash effect | Reporting effect | Action |
|---|---|---:|---|---|---|
| Reverse charge not accounted | none | 0 | — | — | Both legs booked; report both |
| Blocked cost recovered | 1 line (staff entertainment) | 180 | 180 if claimed | Overstated input tax | Exclude; confirm the control-account posting |
| Control account ≠ return | — | 180 | Possibly 180 | Unreconciled | Upload control-account detail |
| Zero-rated export, related party, no evidence seen | 1 sale | 14,570 net | 2,914 if disallowed | — | Hold proof of export |
| Exempt supplies with full recovery | none | — | — | — | — |

## What was not done, and why

- Place-of-supply determinations, establishment, and the zero-rated classification of the export: yours to make; I set out the facts only.
- VAT number validation (e.g. VIES) for the EU vendor: external service; no number is recorded.
- Control-account reconciliation and the clearing test: need the account detail and prior returns.
- Bad debt relief sweep: no receivables ageing uploaded.
- No Excel file created; I would ask before making `VAT_GST_UK_2025-Q3_Northbrook-UK-Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook UK Ltd, GBP, Q3 2025 — user-asserted; one registration since 2019, country not named; source: upload. Transactions accepted with a limit; rules file accepted with a limit; rota rejected. Tax codes exposed per line; counterparty country not recorded. Rates: 'sample rate card v1, tax year 2025' (fictitious) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 registration: done with a limit. 2 place of supply: **not done** (human). 3 output VAT: done. 4/4b reverse charge: done, net nil, both legs present. 5 input VAT: done, 180 blocked. 5b partial exemption: done — not triggered. 6 schemes: none per your file. 7 return: done (proposal). 8 reconciliation: done with a limit — 180 unexplained, clearing test not run. 9 output: chat tables only |
| Not done | Control account to returns filed (needs the account detail and filed returns); GL tie of output and input VAT (needs the GL VAT accounts) |
| Unknowns carried forward | 180 control-account difference; proof of export for the 14,570 related-party sale; EU vendor VAT number; country of registration |
| Parameters | Standard 20%, exports zero-rated, entertainment blocked — all from 'sample rate card v1, tax year 2025'; quarterly; no partial exemption; no schemes. To be re-confirmed next period, not reused |
