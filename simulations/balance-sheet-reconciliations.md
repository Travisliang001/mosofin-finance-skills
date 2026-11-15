# Balance sheet reconciliations — Northbrook Trading Ltd, 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual: every balance comes from the files you uploaded. Connecting Mosofin would pull the GL side and the A/R and A/P detail automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was posted, cleared or signed off. Every entry below is a proposal.

## Read-back and assumptions

Reconciling **all balance sheet accounts** of **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, in **USD**. Intake questions left unanswered:

- **Materiality threshold:** not given, and the skill never defaults it. Please set one. A common basis is overall reporting materiality spread across the accounts. Until you do, **every** difference is reported at its full amount and none is called "within tolerance".
- **Preparer and reviewer:** not given. Workpaper header left blank.
- **Prior-period reconciliation:** not supplied. The carry-forward check (Section 6) cannot run, and item ages rest on document dates only.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts. Debits = credits = 6,589,681 | No company name in the file. Its cash (1,230,316) and A/R (798,360) agree with the September ledger and the 30 Sep ageing | Yes | Step 2, GL side of every account | **Accepted with a limit**: company user-asserted |
| `trial_balance_september.csv` | A trial balance, 29 accounts, foots at 5,389,421, but **for a different period**. Accumulated depreciation is 50,400 lower (12 × the 4,200 monthly charge), the term loan is 60,000 higher (12 × 5,000), and cash is 763,153, which matches neither end of the September 2025 ledger. It is **one year earlier** (about September 2024) | Wrong period: its name says "september" but gives no year, and its content is 12 months before your intake period | Not for this period | No step: a prior-year TB is not the prior-period reconciliation | **Rejected** on content. If you meant to send a 30 Sep 2025 TB, the file above is used. If this is last year's, it is not needed. |
| `cash_account_ledger_2025-09.csv` | GL detail for the operating bank account. Opening 1,246,642, 15 entries, closing **1,230,316** = TB 1000 | September 2025 | Yes | Cash, Steps 2–4 | **Accepted with a limit**: account name user-asserted |
| `bank_statement_2025-09.csv` | Bank statement, running balance recomputed and foots: 1,246,642 → **1,219,776** | September 2025 | Yes | Cash, support side | **Accepted with a limit**: no account number in the file |
| `ar_aging_detail_2025-09-30.csv` | Open receivables by invoice, 12 customers, incl. one credit memo. Total **798,360** | 30 Sep 2025 | Yes | A/R support side | **Accepted with a limit**: company user-asserted |
| `open_bills_2025-09-30.csv` | Open payables, 12 bills, total **255,264** | Bills dated 3–25 Sep 2025 | Yes | A/P support side | **Accepted with a limit**: company user-asserted |
| `inventory_listing_2025-09-30.csv` | Stock listing, 15 SKUs, value column total **683,100** | 30 Sep 2025 | Yes. Qty × unit cost recomputes to 683,166: unit costs are rounded to whole dollars, so line differences of up to 25 net to 66 | Inventory support side | **Accepted with a limit**: a listing, not a count, and no valuation test |
| `fixed_asset_register.csv` | Register: 8 assets, cost and life, total cost **420,000** | No as-at date; includes an asset marked "sold Jul 2025" | Cost only. **No accumulated depreciation column** | Fixed assets (cost) support side | **Accepted with a limit**: supports 1500 cost, not 1510 accumulated depreciation |

**Still missing (required for the accounts named):** prepaid schedule (1300); allowance calculation (1150); accruals schedule (2100); payroll register and remittances (2150, 2160); sales tax return (2200); corporate card statement (2050); petty cash count (1010); Stripe payout report (1050); Northbrook UK's mirror balance (2300); loan statement or amortization schedule (2500); share register (3000); register depreciation summary (1510). Also the materiality threshold.

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Master summary

| Account | GL (USD) | Support (USD) | Difference | Status |
|---|---:|---:|---:|---|
| 1000 Operating Bank Account | 1,230,316 | 1,219,776 (statement) | bridged below | **Tied after reconciling items**, 1 item investigating |
| 1100 Accounts Receivable | 798,360 | 798,360 (ageing) | 0 | **Tied**, with presentation items |
| 1200 Inventory | 683,100 | 683,100 (listing) | 0 | **Tied to listing**; count and valuation not evidenced |
| 1500 Fixed Assets — Cost | 420,000 | 420,000 (register) | 0 | **Tied, but both include a sold asset** |
| 2000 Accounts Payable | 255,264 | 255,264 (open bills) | 0 | **Tied, but both include a likely duplicate** |
| 1510 Accumulated Depreciation | (311,200) | not supplied | — | **Not reconciled** |
| 1050 Stripe Clearing / 2150 Payroll Clearing | 6,420 / (1,200) | should be zero | 6,420 / 1,200 | **Investigating**: clearing accounts not at zero |
| 1010, 1150, 1300, 2050, 2100, 2160, 2200, 2300, 2500, 3000 | various | not supplied | — | **Not reconciled**: support never supplied |

Of 5,707,777 in gross balance-sheet balances, **3,387,040 (59%) has an evidenced supporting side**. The rest is not reconciled, and is not reported as tied.

## Findings

**1. Cash (1000): ties after four items.**
Bank 1,219,776 + deposit in transit 12,400 (Tideswell Hotels, booked 30 Sep) − outstanding check 2291 3,150 (Orchard Packaging, 29 Sep) = **1,229,026**. Book 1,230,316 − service fee 50 (30 Sep) − ACH debit "UNKNOWN ORIG 88213" 1,240 (24 Sep) = **1,229,026**. Difference 0.
The two deposits are **timing**: no entry. The fee is **permanent**. The 1,240 debit is **investigating**: identify the originator before booking. Owner and date are needed. Full detail belongs in `bank-reconciliation`.

**2. Accounts payable (2000): likely duplicate bill, 6,480.** Kestrel Supplies INV-4471 (5 Sep, 6,480) and "Kestrel Supplies Inc." INV4471 (6 Sep, 6,480): same number without the hyphen, same amount, a day apart, under a second vendor record. Sub-ledger and GL agree, so **both are overstated by 6,480** if it is a duplicate. Permanent. Confirm against Kestrel's statement before correcting.

**3. Fixed assets (1500): a sold asset is still on the books.** FA-008 "Delivery van (sold Jul 2025)", cost 12,000, is still in the register and in the 420,000 that ties to the GL. The disposal was never recorded. On straight-line, 5 years from May 2019, it was fully depreciated by April 2024, so cost and accumulated depreciation are **both overstated by 12,000**. Any sale proceeds and the gain on sale are unrecorded. Where did the proceeds go?

**4. Accumulated depreciation (1510): not reconciled, and an indicative gap.** The register has no depreciation column. As an **indicator only**, I recomputed straight-line from cost, life and in-service month (full month, no salvage, my convention, not yours): **248,787** against GL 311,200, a gap of 62,413. The current monthly charge recomputes to 3,814 against the 4,200 booked each month (37,800 YTD / 9). This is not a reconciliation. Please send the register's depreciation summary and convention.

**5. Clearing accounts not at zero.** 1050 Stripe Clearing 6,420 debit and 2150 Payroll Clearing 1,200 credit. Both should clear to zero. Stripe transfers of 18,842 and 21,307 reached the bank in September. A Stripe payout report would show what the 6,420 is. Investigating, with high priority. Neither balance should roll forward.

**6. A/R (1100): ties, three items to clear.**
- Calder Print credit memo CM-0312 (2,150, 2 Sep) is unapplied against INV-20796 (32,020).
- Two invoices are over 90 days past due: Harlow INV-20418 (48,200, 95 days) and Foxhall INV-20907 (4,003, 130 days). Refer them to `bad-debt-and-write-offs`. The allowance (1150, 9,000) has no supporting calculation.
- The **12,400 deposit from Tideswell Hotels** on 30 Sep is not reflected in the ageing: Tideswell's INV-20722 (48,031) is still fully open. Find which account the deposit credited. Investigating.

**7. Inventory (1200): ties to the listing, valuation at risk.** Three lines have not sold in 10 months or more: LK-09 (39,792, last sale Jun 2024), PN-55 "discontinued" (26,528, Feb 2024) and TR-07 (19,896, Nov 2024), **86,216** in all. Review for lower of cost and net realisable value in `inventory-to-gl-reconciliation`. No count was supplied.

## Proposed entries (proposals only; nothing posted)

| # | Entry | Amount | Note |
|---|---|---:|---|
| 1 | DR 6500 Bank Fees / CR 1000 Operating Bank Account | 50 | September service fee |
| 2 | DR 2000 Accounts Payable / CR account the Kestrel INV4471 was charged to (not in the files) | 6,480 | Only once the duplicate is confirmed |
| 3 | DR 1510 Accumulated Depreciation / CR 1500 Fixed Assets — Cost | 12,000 | FA-008 disposal. Proceeds and gain to add once known; the gain/loss account is not in the TB |

The 1,240 ACH debit, the clearing balances and the Tideswell deposit are **investigating**, so no entry until identified. Each needs an owner and a target date, which you have not given.

## Not done, and why

- Ten accounts not reconciled, support not supplied (listed above).
- Roll-forwards (Step 6): only closing balances were given. No opening TB or GL activity for A/R, A/P, inventory or fixed assets.
- Prior-period carry-forward (Section 6): no prior reconciliation. A baseline should be set this month.
- Materiality flags: no threshold.
- Excel workpaper `BS_Recs_2025-09_Northbrook Trading Ltd.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD, all user-asserted. Data source: upload, because the Mosofin gateway is absent. Seven files accepted with limits as above. `trial_balance_september.csv` rejected: prior-year period.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Account | GL side | Support side | Gap and owner |
|---|---|---|---|
| 1000 Cash | TB + ledger, manual | statement, manual | 1,240 ACH unidentified; owner not named |
| 1100 A/R, 2000 A/P | TB, manual | ageing / open bills, manual | Duplicate 6,480; Tideswell 12,400 |
| 1200 Inventory | TB, manual | listing, manual | No count, no valuation |
| 1500 / 1510 Fixed assets | TB, manual | register (cost only), manual | Disposal; depreciation summary missing |
| All other accounts | TB, manual | **not supplied** | Schedules listed under "Still missing" |

Steps: 0–2 done with a limit; 3–5 done for the five supported accounts; 6 roll-forward **not done**; 7 ageing done, materiality **not done**; 8 tables in chat; 9 not offered.

**Data sources:** upload — trial_balance_2025-09-30.csv, cash_account_ledger_2025-09.csv, bank_statement_2025-09.csv, ar_aging_detail_2025-09-30.csv, open_bills_2025-09-30.csv, inventory_listing_2025-09-30.csv, fixed_asset_register.csv.
