# Valuation package — Northbrook Trading Ltd, as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. **This is valuation analysis, not an opinion of value**; a qualified valuation professional signs before anyone relies on a figure. Nothing was written anywhere, and no market data was supplied by me.

## Read-back

Building a valuation package for **Northbrook Trading Ltd** at **30 September 2025**, for **management planning** (fair market value), in **USD**, on **your 12-month P&L forecast**, with the WACC inputs, **five trading comps and three precedent multiples** from `market_data_supplied.md`. Bridge items from **your 30 Sep 2025 trial balance**; net debt on **your definition: term loan plus card balance less cash**; **1,080,000 diluted shares** (your figure; no cap table). Company, period and currency are user-asserted. Purpose, standard, terminal growth, net-debt definition and share count arrived inside the market-data file; used as confirmed in this read-back. Fiscal year end not stated: the TB's P&L accounts hold 9 months (rent 81,000 = 9 × 9,000; depreciation 37,800 = 9 × 4,200), so I read them as January–September 2025 year to date.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts, balance sheet plus YTD P&L | No company or currency named; dated 30 Sep 2025 (= valuation date) | Yes: debits 6,546,018 = credits 6,546,018 | Yes: bridge (Step 6b), measured history (Steps 2c, 3) | **Accepted with a limit**: company/currency user-asserted; P&L is 9 months only, so no LTM figure |
| `forecast_2025-10_to_2026-09.csv` | 12-month P&L forecast by line, to interest | Oct 2025–Sep 2026; no company named | P&L only: **no capex, working capital, tax or balance sheet**; one year, not five | Yes: DCF (Step 2), comps metric (Step 5) | **Accepted with a limit**: DCF is indicative only; capex/WC tie-backs cannot run |
| `market_data_supplied.md` | Typed summary of market inputs, not the source data | Dated 30 Sep 2025 | Yes as a summary. Sourced and dated: risk-free rate, trading comps. **No source or date**: ERP, beta, size premium, cost of debt, tax rate ("sample"), debt weight, precedents, terminal growth. No peer or deal names; multiple basis (LTM/NTM) not stated | Yes: Steps 3–6 | **Accepted with a limit**: every figure user-supplied, not evidenced |
| `forecast_2025-10_to_2026-09_final.csv` | **Not a forecast.** A staff shift rota: employees E08–E10, week_1–week_4, nights/days/off | No company, no dates, no amounts | No | No step uses it | **Rejected** on content. If a final forecast exists, please upload it; otherwise I use `forecast_2025-10_to_2026-09.csv` |

Still missing: forecast capex, working capital and tax (and years 2–5); sources and dates for the unsourced inputs; peer and deal names and the multiple basis; cap table; lease agreements (rent is 9,000/month but the TB has no lease liability); restricted-cash status; tax status (the TB has no income-tax expense or payable).

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. Anchor.** Valuation date 30 Sep 2025; balance sheet read at the same date (no gap). EV basis, then bridge to equity. Labels used below: **[mgmt]** your forecast, **[market]** sourced market data, **[user, unsourced]**, **[analyst]** my selection, **[measured]** from the TB.

**2. The forecast is the same months of 2025 × 1.10, line by line, one-offs included.** Jan–Sep 2026 against the TB's Jan–Sep 2025: revenue 4,442,460 / 4,038,600 = 1.100; COGS, payroll, marketing, professional fees, bank fees and interest all 1.100. So it repeats the June professional-fee spike (18,150 vs 2,750 run-rate), the September marketing spike (32,061 = 6.4% of revenue vs 4.0%) and the Jul–Sep COGS step to 60% (vs 58%). Depreciation also rises 10% (4,620/month) with no capex. Forecast NTM: revenue 5,649,930; **EBITDA 867,074 (15.3%)**; EBIT 811,634. Candidate normalisations, not applied: June fees +15,400, September marketing +12,023 → 894,497.

**3. Measured history beside the assumptions [measured, Jan–Sep 2025].** Revenue 4,038,600; gross margin 41.3%; EBITDA 642,515 (15.9%); no income tax booked. Net operating working capital 1,197,196: DSO 53, DIO 79, DPO 29 days. Fixed assets 420,000 cost, net 108,800 — about 26 months of depreciation left with no capex in the model.

**4. WACC — visible build.** Cost of equity 4.2% [market] + 1.1 [user, unsourced] × 5.5% [user, unsourced] + size 2.0% [judgment, unsourced] = **12.25%**. After-tax cost of debt 5.7% × (1 − 20%) = 4.56%. **WACC = 80% × 12.25% + 20% × 4.56% = 10.71%.** Reality checks: actual interest 10,474 for 9 months annualises to 13,965 = **6.3% on the 220,000 loan**, and your own forecast interest (1,463 in October) runs at **8.0%** — both above the 5.7% used. Actual debt (227,300 incl. card) is about 3% of the EVs below, not the 20% target: the target is a recapitalisation claim. Beta is one figure, not unlevered/relevered from peers.

**5. DCF (unlevered: EBIT, not net income; interest excluded).** NOPAT 811,634 × 0.8 = 649,307; + D&A 55,440.

| Case | FCFF yr 1 | EV, WACC 10.71%, g 2.5% | Range (WACC ±1%, g ±0.5%) | TV % of EV | Implied exit multiple |
|---|---:|---:|---:|---:|---:|
| A — forecast as supplied (capex and ΔWC absent, so 0) | 704,747 | **8,581,919** | 7,256,458 – 10,499,809 | **92.6%** | 10.2× |
| B — check [analyst]: capex = D&A; ΔWC = 10% growth × NWC 1,197,196 | 529,588 | **6,448,948** | 5,452,920 – 7,890,161 | **92.6%** | 7.6× |

With one forecast year, **terminal value is 93% of EV**: the explicit forecast is nearly decorative and the sensitivity grid is the headline. Case A's implied exit multiple (10.2×) is above every trading comp. Exit-multiple method at the comps median 8.1× × NTM EBITDA: EV 6,980,315 (Case A), implying perpetual growth of only 0.6%. Terminal growth 2.5% is within long-run growth.

**6. Trading comps** [market: your provider, 30 Sep 2025]: 6.8 / 7.4 / 8.1 / 8.9 / 9.6×; mean 8.16×, median 8.1×, IQR 7.4–8.9×. On NTM forecast EBITDA 867,074: **IQR 6,416,348 – 7,716,959**, median 7,023,299. Not screened: no names, so industry, scale, growth and margin cannot be compared; none excluded. Basis (LTM vs NTM) unknown; LTM EBITDA cannot be built (Oct–Dec 2024 not uploaded). Minority basis.

**7. Precedents** [user, unsourced]: 7.0 / 8.5 / 10.2×, median 8.5×: **6,069,518 – 8,844,155**. Control basis — kept on its own bar, not blended with comps.

**8. Football field (EV, USD m)**

| Method | Low | Base | High |
|---|---:|---:|---:|
| DCF Case A (as supplied) | 7.26 | 8.58 | 10.50 |
| DCF Case B (capex + WC check) | 5.45 | 6.45 | 7.89 |
| Trading comps, IQR (minority) | 6.42 | 7.02 | 7.72 |
| Precedents, range (control) | 6.07 | 7.37 | 8.84 |

The bars overlap at about 6.4–7.7m. DCF Case A sits above the market evidence; that gap is the main thing to resolve with the forecast owner.

**9. Bridge to equity — your definition, then the sweep [measured, TB 30 Sep 2025]**

| Item | Amount | Treatment |
|---|---:|---|
| Term loan (2500) | (220,000) | Debt |
| Corporate card payable (2050) | (7,300) | Debt (your definition) |
| Operating bank + petty cash (1000, 1010) | 1,003,479 | Cash; restricted portion unknown |
| **Net cash, your definition** | **776,179** | |
| Candidates, undecided: Stripe clearing +6,420 (cash in transit); Investment in Northbrook UK Ltd +104,800 (at cost, not fair value — is the subsidiary in scope?); Intercompany payable to Northbrook UK (38,000) | net +73,220 | Your decision |
| Lease liability | **none on TB** | Rent 9,000/month; under ASC 842/IFRS 16 a lease liability is debt. Need the lease |

Equity value at the comps IQR: **7,192,527 – 8,493,138** (indicative per share on 1,080,000: **6.66 – 7.86**); at DCF Case B base 7,225,127 (6.69); at Case A base 9,358,098 (8.66). Per-share is indicative only — no cap table, options or warrants seen.

## What was not done, and why

- Forecast tie-backs for capex, working capital and tax, and a 5-year DCF: the forecast has none of them.
- Model history tied to the accounts: the forecast has no historical columns; only the 9-month TB was available.
- Comparable screening and outlier review: no peer or deal names.
- Lease, restricted cash and tax lines in the bridge: not in the TB; leases and tax status are needed.
- No Excel file created; I would ask before making `Valuation_Northbrook-Trading-Ltd_2025-09-30.xlsx`. No opinion of value.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, valuation date 30 Sep 2025 — all user-asserted; balance sheet read at 30 Sep 2025; source: upload. Files and verdicts as in the validation table (3 accepted with limits, 1 rejected). Purpose management planning; specialist needed before reliance |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 anchor: done. 2 DCF: done with a limit (one year, no capex/WC/tax). 2b history tie: **not done**. 2c evidence: done with a limit (9-month TB). 3 WACC: done, inputs largely unsourced. 4 terminal value: done, both methods and cross-implied checks. 5 comps: done with a limit (no screen). 6 football field: done. 6b bridge: done with a limit (candidates undecided, no lease data). 7 package: in chat only |
| Not done | Tie of model history to the ledger (needs historical columns or monthly P&L); LTM EBITDA (needs Oct–Dec 2024); lease liability (needs lease agreements) |
| Unknowns carried forward | Card balance and UK investment/intercompany treatment; restricted cash; tax status; multiple basis; capex and WC assumptions; cost of debt 5.7% vs 6.3–8.0% observed |
| Parameters | WACC 10.71%; g 2.5%; exit multiple 8.1× (comps median); comps IQR 7.4–8.9×; precedents 7.0–10.2×; NTM EBITDA 867,074; net cash 776,179; 1,080,000 shares |
