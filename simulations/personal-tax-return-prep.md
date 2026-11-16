# Personal tax workpaper — owner of Northbrook Trading Ltd — tax year 2025

**Computation for review by a qualified tax professional. Not tax advice. Nothing is filed.** Mosofin is not connected, so this run is manual and every figure comes from your uploads. (Connecting Mosofin would read the owner's salary and dividends straight from the books: [docs.mosofin.com](https://docs.mosofin.com).) Shown to the taxpayer only; nothing about the taxpayer is saved.

## Read-back

Preparing the **2025 personal return** for **the owner of Northbrook Trading Ltd** (employee code E12 on the payroll register), resident in **Sampleland**, filing **jointly**. Salary and dividend from **Northbrook Trading Ltd**; other income from **your uploaded documents**. Rates from **"sample rate card v1, tax year 2025"** (user-supplied, marked fictitious and for testing). Output to **the taxpayer only**. Shall I go ahead?

Notes on the intake: you gave the period as *September 2025*; the taxpayer document gives **tax year 2025**, which is what a personal return needs, so I use 2025 once you confirm it. The taxpayer, residency and filing status came from inside the document and count as answered on your confirmation. Currency: the business is in USD; the currency of Sampleland's tax is not stated — **assumed USD, confirm**.

## Validation of the uploads (shown before any work — I would wait for your answer here)

| File | What it actually is | Person / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `personal_tax_documents_SAMPLE.md` | The taxpayer's income summary and a rate card with a named source and year | Owner (E12), Sampleland, joint, tax year 2025 | Readable; figures are typed amounts, not the underlying statements | Steps 1–8 | **Accepted with a limit:** a summary, not source documents. Every figure in it is **user-supplied, not evidenced** (no dividend voucher, bank interest statement, rental ledger or payment receipts) |
| `payroll_register_2025-09.csv` | Employer payroll register for **one month, September 2025**, 12 employees; every row foots (gross − tax − social security − 401k = net) | Northbrook Trading Ltd, Sep 2025 | Only the taxpayer's own row (E12) is used; the other 11 employees' rows are third parties and are not read into the work | Step 2 salary, Step 7 withholding | **Accepted with a limit:** one month only. It **cannot** give 2025 salary or 2025 tax withheld, and I will not multiply a month by twelve |
| `personal_tax_documents_SAMPLE_final.csv` | **Not a tax document.** A staff shift rota (E08–E10, days / nights / off by week) | No person, year or money | Nothing relevant | None | **Rejected:** the content is a rota, whatever the name says |

**Still missing (required):** (1) the taxpayer's **full-year 2025 employer statement** — total salary and total tax withheld (the "per payroll" figures); (2) the **spouse's income and documents** — the return is joint and the rate card has one schedule; (3) source documents for the dividend, interest, rental income and costs, and proof of the 8,000 estimated payments. **Recommended:** the 2024 return (carry-forwards); confirmation whether the 401k (595 in September) or social-security contributions get relief under the rate card.

*Proceeding as if you answered "go ahead with the accepted files". The salary figure is blocked; everything that does not need it is computed below.*

## Framework (Step 1)

Jurisdiction Sampleland; tax year 2025; resident (no cross-border element stated); joint filing. Statutory values used — all from **sample rate card v1, tax year 2025** (user-supplied):

| Value | Amount | Source and year |
|---|---|---|
| Personal allowance | 12,000 | sample rate card v1, 2025 |
| Rate band 1 | 15% of taxable income up to 50,000 | sample rate card v1, 2025 |
| Rate band 2 | 30% above 50,000 | sample rate card v1, 2025 |

The card has no separate dividend, interest or rental rate, no joint-filing band and no credits; I have taxed all income on the single schedule. **Confirm with the professional that this is the whole rule set** — a dividend rate or a joint band would change the answer.

## Income by type (Step 2)

| Type | Gross | Withheld | Source | Basis |
|---|---|---|---|---|
| Employment — salary, Northbrook Trading Ltd | **Blocked** (September only: 14,863) | **Blocked** (September only: 1,784) | Payroll register, Sep 2025 | Need full-year employer statement |
| Dividend, Northbrook Trading Ltd, 31 Mar 2025 | 48,000 | — | Tax document | Taxpayer's 80% share of a 60,000 dividend (48,000 = 0.8 × 60,000 ✔); user-supplied |
| Bank interest | 1,240 | — | Tax document | User-supplied |
| Rental: receipts 18,000 less costs 6,500 | 11,500 net | — | Tax document | User-supplied; which costs are allowable is for the reviewer |
| **Total excluding salary** | **60,740** | | | |

## Taxable income and tax (Steps 4–6)

| | Amount |
|---|---|
| Income excluding salary | 60,740 |
| Less personal allowance | (12,000) |
| Taxable income excluding salary | 48,740 |
| Plus full-year salary **S** | **S** (blocked) |

Taxable income of 48,740 + S passes the 50,000 band edge once salary exceeds **1,260**, which a full year of salary certainly will (September alone is 14,863). So, once S is supplied:

**Tax before credits = 7,500 + 30% × (S − 1,260)**
(7,500 is 15% of the first 50,000.)

**Balance due (refund if negative) = that tax − full-year salary tax withheld − 8,000 estimated payments.**

I have not put a number on S or on the withholding: a September-times-twelve figure would be an estimate of a figure that has to come from the employer's statement.

## Credits and payments (Step 7)

Estimated payments 8,000 (user-supplied, receipts needed). Salary withholding: full year blocked. No credits are given on the rate card; none applied.

## Open items for the reviewer

1. Full-year salary and withholding for 2025 — **blocks the tax figure**.
2. Joint filing with no spouse figures and a single-person schedule — confirm how joint filing works under this card.
3. Relief for the 401k / retirement contributions (595 in Sep) and social-security contributions (1,137 in Sep) — not on the card, not applied.
4. Whether dividends and interest have their own rates or allowances in Sampleland.
5. Rental cost allowability, and any capital allowance on the property.
6. Filing and payment deadlines, next-year estimated payments, and any underpayment penalty — not on the card, not computed.
7. The rate card is marked fictitious and for testing: it must be replaced by the official 2025 source before anything is filed.

## Document checklist (Step 9)

| Figure | Document needed | Status |
|---|---|---|
| Salary and tax withheld, 2025 | Employer's annual statement | **Missing** |
| Dividend 48,000 | Dividend voucher / board minute showing the 80% holding | Missing (summary only) |
| Interest 1,240 | Bank interest statement | Missing |
| Rental 18,000 / 6,500 | Rental ledger, receipts | Missing |
| Estimated payments 8,000 | Payment confirmations | Missing |
| Spouse's income | Spouse's documents | Missing |
| Carry-forwards | 2024 return | Missing |

## Not done, and why

The tax liability and the balance due are not stated as numbers: full-year salary and withholding are required inputs I do not have. Capital gains: none reported. I would ask before creating `Personal_Tax_2025_[Name].xlsx` (name to be supplied by you; not taken from the documents). Nothing was posted, filed, paid or saved. **Have a qualified tax professional review this before anything is filed.**

## Coverage sheet (manual run)

| Section | Entry |
|---|---|
| Environment | Taxpayer: owner of Northbrook Trading Ltd; Sampleland resident; joint; tax year 2025; currency assumed USD — all user-asserted; source: upload (Mosofin not used, by choice) |
| Files | Tax document accepted with limit (summary, unevidenced); payroll register accepted with limit (Sep 2025 only, own row only); `_final.csv` rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 framework done; 2 income done except salary (blocked); 3 rental net done, allowability open; 4 allowance applied; 5 taxable income done as formula; 6 tax done as formula; 7 credits partial; 8 balance due as formula; 9 checklist done; 10 tables in chat |
| Not done | Full-year salary and withholding; spouse's income; prior-year carry-forwards; deadlines and penalties |

**Data sources:** uploads — `personal_tax_documents_SAMPLE.md` (user-supplied figures and rate card v1, 2025), `payroll_register_2025-09.csv` (row E12 only).
