# Vendor master audit — Northbrook Trading Ltd, as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. Nothing was created, edited or deactivated, and no bank detail was changed. **No sanctions screen was run or is claimed.** This is not tax advice: reportability and withholding are for you or your adviser to confirm. Tax identifiers stay masked throughout.

## Read-back

Auditing the vendor master of **Northbrook Trading Ltd**, a **US** payer, in **USD**, from **your uploaded vendor master, payments by vendor and 12-month bill payment history**. **Audit only — no onboarding.** Output for **the AP manager**, identifiers masked. Not answered, so the skill's defaults apply: **onboarding policy (D)** — none given, so I report what is recorded with no pass or fail against a policy; **sanctions screening (E)** — listed as not evidenced; **change history (F)** — the master carries one "bank details changed on" date per vendor and no log of who changed what, so change detection runs on that field only.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `vendor_master.csv` | Vendor master: 12 vendors, terms, tax form on file, entity type, last bank-change date, paid 2025, masked tax ID | No company named; no as-at date | Yes. No address, legal name vs DBA, contact, bank or country fields | Yes: Steps 0a–0d | **Accepted with a limit**: company user-asserted; completeness can be tested only on the fields present |
| `payments_by_vendor_2025.csv` | Payments by vendor with entity type and method, 12 vendors | Headed 1 Jan – 30 Sep 2025 | Yes; amounts equal the master's `paid_2025` for all 12 (total 950,780). **But the figures match 12 months, not 9** (see finding 6) | Yes: Step 0b ranking | **Accepted with a limit**: period label unreliable |
| `bill_payment_history_12m.csv` | Bill-level payments, Oct 2024 – Sep 2025, 8 of the 12 vendors (89 bills) | 12 months to Sep 2025 | Yes; 4 vendors absent (Vale, Northgate, Pinecrest, Dale) | Yes: payment proximity in Step 0c, duplicates in 0d | **Accepted with a limit**: no history for 4 vendors |
| `vendor_master_final.csv` | **Not a vendor master.** A staff shift rota: employees E08–E10, week_1–week_4, nights/days/off | No company, dates or vendors | No | No step uses it | **Rejected** on content. If a final vendor master exists, please upload it; otherwise I use `vendor_master.csv` |

Still missing: onboarding policy; who runs sanctions screening and on what service; vendor addresses, countries and bank-account identifiers (masked) for the duplicate and bank-country tests; form dates (for W-8 expiry); LLC tax classifications; a customer list for the vendor/customer overlap test.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings — Master Audit, ranked by money

**1. Actively paid vendors with no tax form on file — 4 vendors, 75,980 paid (Step 0b).**

| Rank | Vendor | Entity type | Paid (per master) | Bills in 12m | Priority |
|---:|---|---|---:|---:|---|
| 1 | Brightline IT Services | Sole proprietor | 41,800 | 11 × 3,483 | **High**: material, individual payee; request a W-9 now |
| 2 | M. Okafor Consulting | Sole proprietor | 18,500 | 11 × 1,542 | **High**: same |
| 3 | Vale Marketing Studio | LLC (classification unknown) | 9,200 | none in history | Request W-9; the LLC's tax classification decides reportability |
| 4 | Kestrel Supplies Inc. | Corporation | 6,480 | 11 × 540 | See duplicate candidate below |

A US payee who will not provide a form may need backup withholding — for your adviser to confirm. I have not decided reportability for any vendor.

**2. Bank detail change followed by a payment — Summit Freight (Step 0c).** Bank details changed **16 Sep 2025**; bill 3111 for **8,017** was paid **20 Sep 2025, four days later**. This is the one shape that should always be verified: **call Summit Freight back on a number already on file (not one from the change request)** and confirm the change. Not an accusation — most changes are legitimate. Who made the change, and who released the payment, is not recorded.

**3. Duplicate candidate — Kestrel Supplies / Kestrel Supplies Inc. (Step 0d).** Name match (fuzzy: "Inc." suffix); both Corporation, both 30 days, both on monthly ACH. Combined payments **418,780** (412,300 + 6,480). Kestrel Supplies has a W-9 (TIN ending 1000); the "Inc." record has **no form and no TIN**, so payments under it sit outside the documented record. Tax ID and bank account could not be compared (one TIN absent, no bank data). Confirm whether these are one supplier, a remit-to child, or two entities; merging is yours to do.

**4. Other items to note.**
- **LLCs with no tax classification recorded**: Orchard Packaging (188,400), Halden Property Management (81,000), Vale Marketing Studio (9,200). "LLC" alone does not determine 1099 reportability.
- **Pinecrest Software** — foreign corporation, W-8BEN-E on file, paid **42,000 by card**. No form date in the master, so W-8 expiry cannot be tested.
- **Greyfriars Legal LLP** — partnership, W-9 on file, 27,400; legal fees have their own reporting rules — adviser to confirm.
- **Halden Property Management** — terms 0 days, paid the day after each bill (12 × 6,750): consistent with rent; noted, not an exception.

**5. Tax ID format (Step 2 rule, whole master).** Eight masked IDs share the EIN shape `**-***NNNN`; full format and prefix validation cannot run on masked values. Dale Cleaning Co (sole proprietor) shows an EIN-shaped TIN — valid for a sole proprietor; not to be "corrected". IRS TIN matching is `[manual]`: I can prepare the list, not run it.

**6. The payments file's period label does not fit its figures.** It is headed 1 Jan – 30 Sep 2025, but every amount equals about twelve months of bills: Kestrel 412,300 vs 12 × 34,358 = 412,296; the bill history's Jan–Sep 2025 total is **309,222**. Same for every vendor in the history (e.g. Orchard 188,400 = 12 × 15,700; Jan–Sep 141,300). The ranking above holds either way, but the "paid 2025" figures should not be used for year-end reporting until the period is confirmed.

## What was not done, and why

- Sanctions, OFAC and PEP screening: never run here; **Pending, not clear**, for all 12 vendors. Who runs it was not answered.
- TIN matching and form validation: needs the IRS service and the forms themselves.
- Bank-account duplicate test, bank-country consistency, address match: no bank or address data in the master.
- Vendor/customer and related-party overlap (Step 0e): no customer list.
- W-8 expiry: no form dates. Pass/fail against your policy: no policy supplied.
- No Excel file created; I would ask before making `Vendor_Master_Audit_2025-09-30_Northbrook-Trading-Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, US payer, USD — user-asserted; source: upload; 12 vendors; payments 12 months to Sep 2025 (file says Jan–Sep). Bank details not supplied. Change history: one date field only, no log of who changed it. Three files accepted with limits; rota rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0a completeness: done with a limit (fields present only). 0b ranking: done. 0c bank change: done with a limit (date field only) — 1 flagged. 0d duplicates: done with a limit (name only) — 1 candidate. 0e overlap: **not done**. 1–3 onboarding: out of scope (audit only). 4 screening: **not done** — Pending. 5–8: findings in chat only |
| Not done | Screening; TIN matching; bank-account and address match; customer overlap; W-8 expiry |
| Unknowns carried forward | 4 vendors without forms (75,980); Summit Freight change unverified; Kestrel duplicate unresolved; 3 LLCs unclassified; payments-file period |
| Parameters | Match keys used: name (fuzzy, legal suffixes ignored); bank-change window: payment within 30 days of change; payment period as found in files; no policy applied |
