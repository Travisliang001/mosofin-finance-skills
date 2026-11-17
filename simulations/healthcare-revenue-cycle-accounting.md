# Revenue cycle review — Lakeside Clinic, September 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded, at aggregate level only: no patient-level data was received or used. Nothing has been posted, sent or changed.

## (a) Read-back

Reviewing the revenue cycle for **Lakeside Clinic** for **September 2025**, in **USD**, from **the billing summary you uploaded (totals by payer class only)** and **the ledger totals you uploaded**. Gross charges **are** recorded in the ledger (gross patient revenue 1,160,000). Charity care per **your policy: free care below 200% of the poverty guideline, presented as a deduction from revenue**. Company, period and currency are as you stated them.

Taken from the files, for you to confirm: that gross charges are in the ledger, the charity care policy, and the payer classes (Medicare, Commercial, Self-pay). Not answered anywhere: **payer contract rates** and **denial reason codes** (listed as not supplied), and **whether the 18,000 of charity care is inside the 26,000 of bad debt expense or in addition to it**.

What I received:
- `billing_summary_by_payer_2025-09.csv` — 3 payer classes; columns for gross charges, contractual adjustments, payments, denials, charity care and receivables in three age bands.
- `clinic_gl_summary_2025-09.md` — ledger totals for September: revenue, contra-revenue, bad debt, receivables, allowance, unapplied cash, and the charity care policy.
- `billing_summary_by_payer_2025-09_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `billing_summary_by_payer_2025-09.csv` | Billing system totals by payer class, with a receivables ageing by payer class | **Content names no clinic, period or currency** (only the file name says 2025-09) | Yes; totals only, no patient detail; columns identifiable | Steps 1–5: billing side of every tie, realisation, ageing | **Accepted with a limit**: company and period user-asserted. It also serves as the ageing by payer class; payer and patient (self-pay) balances are separable by class only |
| `clinic_gl_summary_2025-09.md` | Ledger totals and the charity care policy | Lakeside Clinic, September 2025 | Yes | Steps 2–5: ledger side | **Accepted with a limit**: totals, not ledger detail (the checklist asks for detail). Every figure user-supplied; no postings, dates or users, so cutoff and write-off concentration cannot be tested |
| `billing_summary_by_payer_2025-09_final.csv` | A four-week staff shift roster for employees E08–E10 | No clinic, date or amount | Not for this skill | No step uses it | **Rejected**. The name suggests a final billing summary; the content is a rota. Set aside. If a final billing summary exists, please upload it |

**Still missing:** ledger detail for revenue, contra-revenue, receivables and cash (required; totals received), prior months for a realisation trend and reserve back-test, bank deposits for the cash tie, payer contract rates and denial reason codes (recommended). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. Revenue cycle map.** Charge capture, remittance posting and collections land in the ledger (gross revenue, contractual allowances, cash). Claim submission and payer adjudication do not: the 30,000 of September denials are visible only in the billing summary, without reasons.

**2. Billing to ledger tie.**

| Item | Billing summary | Ledger | Difference |
|---|---:|---:|---:|
| Gross charges | 1,160,000 | 1,160,000 | 0 |
| Contractual adjustments | 496,000 (252,000 + 244,000 + 0) | 480,000 | **16,000 more in billing** |
| Patient receivables | 309,000 (55,000 + 158,000 + 96,000) | 309,000 | 0 |

**Contractual adjustments differ by 16,000.** The billing system recorded 496,000; the ledger 480,000. Until it is explained (unposted adjustments, timing, or a misposting), net revenue in the ledger is **16,000 higher** than the billing system supports.

**3. Charity care is recorded as bad debt, against your policy.** The ledger shows "charity care recorded as bad debt: 18,000", and the billing summary shows 18,000 of self-pay charity care. Your policy presents charity care as a deduction from revenue. Charity care is never bad debt: it was never going to be pursued. As recorded, expense is overstated by 18,000 and revenue overstated by 18,000.

**4. Net patient service revenue.**

| | Ledger as recorded | Billing basis, policy applied |
|---|---:|---:|
| Gross charges | 1,160,000 | 1,160,000 |
| Contractual adjustments | (480,000) | (496,000) |
| Charity care (deduction from revenue) | — | (18,000) |
| **Net patient service revenue** | **680,000** | **646,000** |
| Realisation (net ÷ gross) | 58.6% | 55.7% |

Realisation by payer class (billing, before denials): Medicare (420,000 − 252,000) ÷ 420,000 = **40.0%**; Commercial 366,000 ÷ 610,000 = **60.0%**; Self-pay 100% before charity care, 86.2% after. Gross charges are never revenue; the 1,160,000 is a list price. One month only, so no trend: please upload prior months.

**5. Bad debt.** If the 18,000 is inside the 26,000, true bad debt is **8,000**; if it is in addition, bad debt is 26,000 and the total charge 44,000. Whether bad debt here should be an implicit price concession (a reduction of revenue) depends on whether collectability was assessed at the outset; that is your call.

**6. Receivables ageing (payer and patient separated by class).**

| Payer class | 0–30 | 31–90 | Over 90 | Total | Over 90 % |
|---|---:|---:|---:|---:|---:|
| Medicare | 40,000 | 12,000 | 3,000 | 55,000 | 5.5% |
| Commercial | 95,000 | 41,000 | 22,000 | 158,000 | 13.9% |
| Self-pay | 22,000 | 30,000 | 44,000 | 96,000 | **45.8%** |
| **Total** | 157,000 | 83,000 | 69,000 | 309,000 | 22.3% |

Self-pay carries 31% of the balance but 64% of the over-90 tail (44,000 of 69,000). Net of the contractual allowance of 62,000, receivables are 247,000. The bad debt reserve against the 44,000 of self-pay over 90 days was not supplied.

**7. Unapplied cash rose from 6,000 (August) to 14,000 (September)**, up 8,000 or 133%. Remittances are not being matched to claims; receivables are overstated by up to that amount until applied. Its age was not supplied.

**8. Denials.** 30,000 in September: Medicare 9,000 (2.1% of gross), Commercial 21,000 (3.4%). No reason codes, so the drivers and a denials reserve cannot be assessed.

**9. Proposed entries — PROPOSALS, NOT POSTED** (generic account names; no chart supplied).
- Reclassify charity care: Dr charity care (deduction from revenue) 18,000 / Cr bad debt expense 18,000.
- Contractual difference, only once the 16,000 is explained and the billing figure is confirmed: Dr contractual allowances 16,000 / Cr allowance for contractual adjustments 16,000.

## (d) What was not done, and why

- **Realisation trend, reserve back-test, AR days trend, payer mix shift** — one month only.
- **Cash to bank deposits** — no bank data. **Unapplied cash ageing** — no detail.
- **Cutoff, write-off concentration** — no ledger detail with dates and users.
- **Contractual reserve against contract rates, denials reserve** — no contracts, no reason codes.
- **Excel workpaper** (`Healthcare_Revenue_Cycle_2025-09_Lakeside Clinic.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts.

## Coverage (manual run)

| Section | Content |
|---|---|
| Environment | Lakeside Clinic, September 2025, USD — user-asserted. Source: upload. Billing summary accepted with a limit (unnamed in content); ledger totals accepted with a limit (totals, not detail); `_final.csv` rejected (staff roster). Aggregate level only |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done; 2 done with a limit (one month); 3 done with a limit (AR ties, cash not tied); 4 done with a limit (no back-test); 5 done with a limit (adjustment rate and unapplied cash only); 6 tables in chat; 7 not offered |
| Not done | Ledger-detail tests, bank tie, prior-period comparisons: need ledger detail, bank statement and prior months |

**Data sources:** user-uploaded `billing_summary_by_payer_2025-09.csv` and `clinic_gl_summary_2025-09.md`; intake answers (clinic, period, currency). No ledger read.
