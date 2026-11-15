# FX revaluation — Northbrook Trading Ltd, 30 September 2025 (upload path)

Mosofin is not used for this run (you chose upload only), so every step is `[manual]` and works from your files. **Nothing was posted: the entry below is a proposal.** Every rate used is yours, from `fx_rates.csv` ("bank rate sheet"); none was supplied by me.

## Read-back

Revaluing foreign-currency balances for **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, from **your uploads**, at the **closing rate you supplied (GBP/USD 1.27, bank rate sheet, dated 30 Sep 2025)**. Functional currency **USD** (your answer); presentation currency **USD**; **US GAAP**; **no hedges** (your answer).

| Not answered at intake | What I applied |
|---|---|
| E. Does your system revalue automatically, and has it run? | Not answered. Checked the books: **no FX gain/loss account exists in the trial balance**, so no revaluation has been posted for this period. I would **ask you again before treating the entry as final** |
| F. Which accounts are monetary? | Proposed below; **waiting for your yes** |
| Is Northbrook UK Ltd translated/consolidated by you? | Not asked by you; translation is out of scope until its trial balance is supplied |

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `foreign_currency_balances_2025-09-30.csv` | Foreign-currency balance listing: 2 GBP items with foreign amount, booked USD and booked rate | No company named; as-at from file name | Yes; both booked USD amounts tie to the TB lines they sit in (2300 = 38,000 exactly; 1100 includes 22,500) | Yes — Steps 3 and 7 | **Accepted with a limit: company and period user-asserted** |
| `fx_rates.csv` | Rate table, GBP/USD: closing 30 Sep 2025 1.27, average 1 Jan–30 Sep 2025 1.255, closing 31 Dec 2024 1.253, historical 1 Mar 2019 1.31, four transaction-date rates; source "bank rate sheet" on every row | GBP/USD only; dated | Yes | Yes — Steps 3, 4, 7 | **Accepted** (user-supplied evidence) |
| `trial_balance_2025-09-30.csv` | Northbrook trial balance, 33 accounts, USD | No company/date in file | Foots: DR = CR = 6,546,018 | Yes — population check; FX account check (Step 0b) | **Accepted with a limit: company and period user-asserted** |
| `foreign_currency_balances_2025-09-30_final.csv` | **Not a balance listing.** A staff shift rota: employees E08–E10 by week, "days / nights / off" | No company, no period, no amounts | No financial content | No step | **Rejected** on content despite its name. If a revised balance listing exists, upload it |

Still missing: **FX gain/loss account detail for the period** (required to check for entries already posted — the TB has no such account, so I take it that none were); **trial balance of Northbrook UK Ltd** (required only if you want translation); **the transaction date of the Tideswell invoice** (see Finding 2); your yes on the monetary classification.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Ground rules (Step 0b, Steps 1–2)

- **Currency-tagged?** Only through your listing; the TB itself carries no currency. Population = the 2 listed items.
- **System revalues?** No evidence of it: no FX gain/loss or CTA account in the TB or the chart.
- **Functional currency USD** (your answer). The investment in Northbrook UK Ltd (1600) and the intercompany payable (2300) show a UK operation; its own functional currency is not stated.
- **Transaction FX vs translation:** this run is **transaction FX only** (Northbrook Ltd's GBP balances, to P&L). Translation of the UK sub (to OCI/CTA) is a separate exercise, not done.

## Monetary classification (proposed — please confirm)

| Account | Item | Proposed | Reason |
|---|---|---|---|
| 1100 | Tideswell Hotels GBP invoice | **Monetary** — remeasure | Receivable settles in cash |
| 2300 | Intercompany payable to Northbrook UK | **Monetary** — remeasure to P&L | Current payable; no sign it is long-term-investment in nature (if it were, the FX would go to OCI instead) |
| 1600 | Investment in Northbrook UK Ltd 104,800 | **Non-monetary** — not remeasured | Equity investment at historical cost; 104,800 / 1.31 (2019 rate) = GBP 80,000 |

## Remeasurement at the closing rate 1.27 (Step 3)

| Account | Counterparty | GBP | Booked USD | Booked rate | USD at 1.27 | Unrealized FX |
|---|---|---:|---:|---:|---:|---:|
| 1100 | Tideswell Hotels | 18,000 | 22,500 | 1.25 | 22,860.00 | **gain 360.00** |
| 2300 | Northbrook UK Ltd | (29,920) | (38,000) | 1.2701 | (37,998.40) | **gain 1.60** |
| **Total** | | | | | | **gain 361.60** |

Realized FX: **not computed** — no settlements during the period were supplied. The 361.60 is all **unrealized** and reverses if the rate moves back.

## Proposed entry (Step 7) — proposal only, not posted

| Account | DR | CR |
|---|---:|---:|
| 1100 Accounts Receivable (Tideswell) | 360.00 | |
| 2300 Intercompany Payable – Northbrook UK | 1.60 | |
| Unrealized FX gain — **no such account in your chart; tell me which to use** | | 361.60 |

Posted vs proposed: nothing posted (no FX account in the TB), so the proposal stands — **subject to your answer to E**, because if your system revalues automatically this entry would double count.

## Findings

1. **Net unrealized FX gain of 361.60** on two GBP balances at the closing rate 1.27 — immaterial against September revenue, but a proposal nonetheless.
2. **Tideswell invoice booked at 1.25**, a rate that matches **none** of your transaction-date rates (1.2698–1.27) and is close to the 31 Dec 2024 closing 1.253 / YTD average 1.255. Either the invoice is older than any listed date or it was booked at the wrong rate. If its true transaction rate was 1.27, the 360 is a booking error, not FX.
3. **Intercompany booked rate 1.2701 does not reproduce the booked USD**: 29,920 × 1.2701 = 38,001.39, not 38,000 (implied rate 1.27005). Rounding only, 1.39.
4. **No FX gain/loss account exists** in the chart or TB, despite GBP balances — either the system has never revalued, or FX has been absorbed elsewhere. Worth confirming.
5. **Northbrook UK Ltd translation not performed**: no UK trial balance. The 2019 historical rate 1.31 and the opening rate 1.253 are on file for when it is.

## Not done, and why

Realized FX (no settlements); translation / CTA (no UK TB); disclosures beyond the figures above; final classification (awaiting your yes); hedge accounting (none, per you). No `.xlsx` created — I would ask whether you want `FX_Revaluation_2025-09_Northbrook Trading Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, 30 Sep 2025, functional/presentation USD — user-asserted. Source: upload. Balances and TB accepted with limits; rates accepted; `_final` listing rejected (shift rota). |
| Capability map | Not applicable: no connection. Every task is `[manual]`; every rate row is `manual`, source "bank rate sheet". |
| Steps | 0b done with limit · 1 functional currency per your answer · 2 done · 3 done (unrealized only) · 4 **not done** (no UK TB) · 5–6 not applicable · 7 proposal done · 8 partial · 9 tables in chat · 10 not offered. |
| Not done | Check against posted FX (needs FX account detail); realized FX (settlement data); translation and CTA roll (UK TB, CTA account). |

**Data sources:** user uploads — `foreign_currency_balances_2025-09-30.csv`, `fx_rates.csv`, `trial_balance_2025-09-30.csv`.
