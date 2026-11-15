# Personal tax return — the owner of Northbrook Trading Ltd, tax year 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the documents you uploaded, and every step is `[manual]`. Connecting Mosofin would read the owner's salary and dividends from Northbrook Trading's books ([docs.mosofin.com](https://docs.mosofin.com)). **This is a computation for a qualified tax professional to review before anything is filed, not tax advice.** Nothing was filed. None of this is saved. Output is for the taxpayer only.

## Read-back

Preparing the **2025 personal return** for **the owner of Northbrook Trading Ltd** (identified in your documents as payroll employee E12), resident in **Sampleland**, filing **jointly**, **USD**. Rates from *sample rate card v1, tax year 2025* (fictitious): **personal allowance 12,000; 15% on taxable income up to 50,000; 30% above.** No separate dividend, interest or rental rate is given, so all income is taxed on the one scale — please confirm. These answers to intake questions B, C and D came from the document; please confirm them.

Unanswered, and how each is handled:
- **Tax year end:** not stated. Your intake is "as at 30 September 2025". If Sampleland's year is the calendar year, **2025 is not yet over**, so this can only be a draft; a forecast belongs in `tax-planning-and-projections`.
- **Capacity in Northbrook Trading:** the dividend is "80% of 60,000", so an **80% shareholder** and an employee. Please confirm.
- **Dependants, residency detail:** not stated; none assumed. No cross-border element was mentioned.
- **Whether 401(k)-type contributions are deductible** in Sampleland: not stated, so not deducted.

## Validation of the upload (shown before any work)

| File | What it actually is | Taxpayer / year | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `personal_tax_documents_SAMPLE.md` | **Summary** of the taxpayer's documents and rates: dividend, interest, rental, allowance, bands, estimated payments | Tax year 2025; taxpayer identified only as "the owner (E12)" | Yes, but salary and salary withholding say only "per payroll" | Steps 1–8 | **Accepted with a limit**: a summary, not the statements; every figure user-supplied, not evidenced |
| `payroll_register_2025-09.csv` | Northbrook Trading's payroll register, **September 2025 only**, 12 employees | September 2025 | **Only the taxpayer's row is relevant**; the other 11 rows are other people's pay and were **not used** | Step 2 (salary), Step 7 (withholding) | **Accepted with a limit**: one month only, cannot give the 2025 salary or withholding |
| `personal_tax_documents_SAMPLE_final.csv` | **Not a tax document.** A staff shift rota: E08–E10, week_1–week_4, "nights / days / off" | No amounts | No | No step | **Rejected** on content despite its name. Upload the documents it was meant to be |

**Still missing:**
- **Required:** the year's employer statement of salary and tax withheld for 2025 (or all 12 registers). Without it, **salary, withholding and therefore the tax and balance due cannot be computed.**
- **Recommended:** dividend voucher; bank interest statement; rental income and expense records; evidence of the 8,000 estimated payments; prior-year return (carryforwards).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. Income other than salary: 60,740.**

| Income | Gross | Withheld | Source | Basket |
|---|---:|---:|---|---|
| Dividend, Northbrook Trading Ltd, 31 Mar 2025 (80% of 60,000) | 48,000 | — | summary | Dividend |
| Bank interest | 1,240 | — | summary | Interest |
| Rental: receipts 18,000 − costs 6,500 | 11,500 | — | summary | Rental |
| **Total, excluding salary** | **60,740** | | | |
| Salary, Northbrook Trading Ltd | **not determinable** | not determinable | "per payroll"; only September supplied | Employment |

The dividend is the taxpayer's 80% share, not the company's 60,000. Rental costs are taken as allowable; that is a treatment for the reviewer to confirm.

**2. Salary for 2025 cannot be taken from one month.** September's register shows the taxpayer's gross of 14,863 and tax withheld of 1,784. Multiplying that by 12, or 9, would be an estimate of a figure that must come from the employer's year-end statement, so **the tax is not computed as a final figure**.

**3. The computation, as a function of the 2025 salary (S) and salary withholding (W):**

```
Taxable income = S + 60,740 − 12,000 = S + 48,740
Tax            = 15% × 50,000 + 30% × (S + 48,740 − 50,000)    (for S above 1,260)
               = 7,500 + 30% × (S − 1,260)
Balance due    = Tax − W − 8,000 estimated payments
```

Without salary, the other income alone gives taxable income of 48,740 and tax of 7,311 (all within the 15% band). With any salary over 1,260, every extra dollar of salary is taxed at 30%.

**Illustration only, not a figure for the return:** if 2025 salary and withholding were 12 times September's (178,356 and 21,408), taxable income would be **227,096**, tax **60,628.80**, and the balance due **31,220.80** after 21,408 withheld and 8,000 estimated payments. The actual figures replace these when the year-end statement arrives.

**4. Things for the reviewer.**
- Owner-manager with salary and dividend: the rate card has a single scale. If Sampleland taxes dividends separately, the computation changes.
- Joint filing: the spouse's income is not in the documents; joint filing normally includes it.
- Estimated payments of 8,000 are user-supplied; no evidence.
- Next year's estimated payments, deadlines and penalties: not in the rate card, so not computed.

## Statutory values used

| Value | Amount | Source | Year |
|---|---|---|---|
| Personal allowance | 12,000 | sample rate card v1 | 2025 |
| Rate band 1 | 15% on taxable income to 50,000 | sample rate card v1 | 2025 |
| Rate band 2 | 30% above 50,000 | sample rate card v1 | 2025 |
| Dividend / interest / rental rates | **none supplied**: ordinary scale applied | — | — |

## Document checklist

| Figure | Document needed | Status |
|---|---|---|
| Salary and withholding | Employer year-end statement for 2025 | **Missing — blocking** |
| Dividend 48,000 | Dividend voucher | Missing |
| Interest 1,240 | Bank interest statement | Missing |
| Rental 18,000 / 6,500 | Rent ledger, receipts | Missing |
| Estimated payments 8,000 | Payment confirmations | Missing |
| Carryforwards | 2024 return | Missing |

## Not done, and why

- Final tax and balance due: salary and withholding for the year missing.
- Standard vs itemised comparison, credits: none supplied.
- Excel workpaper `Personal_Tax_2025_[Name].xlsx`: not created; the taxpayer's name was not given. Would you like it?

## Coverage sheet (manual run)

**Environment:** taxpayer the owner of Northbrook Trading Ltd, tax year 2025, Sampleland, USD — user-asserted. Data source: upload (Mosofin gateway absent). Documents summary and register accepted with limits (register: own row only); rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 1 Framework | Done with a limit: year end and dependants unconfirmed |
| 2 Income | Done with a limit: salary not determinable |
| 3–4 Deductions | Done with a limit: allowance 12,000; rental costs as given |
| 5–6 Taxable income and tax | Formula only; illustration labelled |
| 7–8 Credits and balance | Not done: withholding for the year missing |
| 9 Checklist | Done |
| 10 Output | Tables in chat; professional review recommended |

**Data sources:** upload — personal_tax_documents_SAMPLE.md, payroll_register_2025-09.csv (taxpayer's row only).
