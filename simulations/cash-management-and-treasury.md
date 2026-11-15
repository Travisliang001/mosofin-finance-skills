# Treasury review — Northbrook Trading Ltd (and Northbrook UK Ltd), as at 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual and uses only your uploads (connecting Mosofin would read every cash account's 12-month activity: docs.mosofin.com). **This designs; your team and your bank act.** No money was moved, no account opened or closed, nothing changed in any system.

## (a) Read-back

Reviewing treasury for **Northbrook Trading Ltd** (USD) as at **30 September 2025**, from **your uploads**: **three cash accounts** totalling **1,237,236 USD**, all mapped by you to a bank and purpose. Your treasury inputs also name **Northbrook UK Ltd** holding **84,200 GBP** and say cash **can** move between the two, so I include it **as a second entity, subject to your confirmation**; your intake named Northbrook Trading only. No cash is restricted. Limit: **no more than 1,000,000 with one bank**. **No existing treasury policy.** Liquidity must cover **loan payments of 6,900 a month** and **2026 capex of 80,000**.

| Intake question | Status | Treatment |
|---|---|---|
| B — entities, currencies | Intake: Northbrook Trading (USD). Treasury inputs add Northbrook UK (GBP) | UK included on confirmation; if out of scope, its trial balance is set aside |
| C — bank, purpose, signatories | Given for the three USD accounts; UK account: "a UK bank", no purpose or signatories | UK columns listed as missing |
| D — trapped cash, movement | None restricted; cash can move (your inputs) | Used |
| E — risk appetite | Single-bank cap 1,000,000; no investment or FX limits | Investment and FX limits drafted with figures left open |
| F — policies, facilities, coverage | No policy; loan 6,900/month; capex 80,000 | Designed from scratch; no revolver supplied |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts, balances; cash accounts 1000, 1010, 1050 = 1,237,236 | 30 Sep 2025 (file name); no company or currency in the file | Yes | Yes — Step 1 balances, Step 7 drawn debt, Step 8 KPIs | **Accepted with a limit**: company/currency user-asserted |
| `cash_account_ledger_2025-09.csv` | Movements on one cash account: opening 1,246,642 + 15 lines = **1,230,316**, agreeing to account 1000 | Sep 2025 only | Yes, but **one month, one account** (checklist asks 12 months for every account) | Yes — Step 1 activity, Step 5 payment mix | **Accepted with a limit**: dormancy and volatility cannot be measured |
| `treasury_inputs.md` | Your account-to-bank map, signatories, risk appetite, coverage needs | Undated; user-supplied | Yes | Yes — Steps 1–3, 7 | **Accepted**: every figure in it labelled user-supplied |
| `trial_balance_northbrook_uk_2025-09-30.csv` | Trial balance of **Northbrook UK Ltd**: bank 84,200, intercompany receivable from Northbrook Trading 33,220; debits = credits 603,520 | 30 Sep 2025; currency not stated (GBP per your inputs) | Yes | Yes — group map, intercompany, FX (Steps 1, 2, 6) | **Accepted with a limit**: a second entity, outside the intake's named company; used only on your confirmation |
| `treasury_inputs_final.csv` | **Not treasury inputs.** A staff shift rota: E08–E10, week_1–week_4, "nights/days/off" | No company, dates or amounts | No | No | **Rejected** on content; I use `treasury_inputs.md` |

Still missing: 12 months of movements for every account (both entities); UK bank name, purpose and signatories; a GBP/USD rate at 30 Sep 2025 with its source; any facility terms beyond the term loan; current payment approval practice.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files", UK included.*

## (c) Findings

### 1. Bank account map (balance and currency from the books; bank, purpose, signatories from you)

| Entity | Account | Currency | Bank | Purpose | Balance 30 Sep | Signatories | Activity in Sep |
|---|---|---|---|---|---:|---|---|
| Northbrook Trading | 1000 Operating Bank Account | USD | Calder Bank | Operations | 1,230,316 | A. Reyes, S. Patel | 15 movements |
| Northbrook Trading | 1010 Petty Cash | USD | — | Float | 500 | Office manager | not supplied |
| Northbrook Trading | 1050 Stripe Clearing | USD | Stripe | Card receipts | 6,420 | none | not supplied (yet two Stripe transfers, 18,842 and 21,307, reached 1000 in Sep) |
| Northbrook UK | 1000 Bank | GBP | "a UK bank" *(missing)* | *(missing)* | 84,200 GBP | *(missing)* | not supplied |

USD cash 1,237,236; group total **cannot be stated in USD** without a GBP rate. No dormant or redundant account can be identified from one month of one account.

### 2. Counterparty concentration — over your limit

Calder Bank holds **1,230,316**, **230,316 above** your 1,000,000 single-bank cap (123% of it). Stripe 6,420 is a payment processor balance, not a bank deposit. Proposal: move at least 230,316, and the surplus in item 3, to a second counterparty that meets the policy criteria below; the choice of bank is yours.

### 3. Liquidity policy — proposed levels for approval

Daily operating outflow, from the 2025 P&L: cash costs 3,395,185 over 273 days = **12,437/day**.

| Level | Basis | USD |
|---|---|---:|
| Minimum cash | 30 days of operating outflow (373,097) + 12 months loan service 82,800 + 2026 capex 80,000 | **535,897** |
| Operating buffer | 15 days of outflow (volatility could not be measured: one month of data) | 186,549 |
| Surplus threshold | Minimum + buffer | 722,446 |
| Surplus above threshold today | 1,237,236 − 722,446 | **514,790** |

Days of cash on hand: **99 days** on the P&L basis; 189 days on September's bank outflows (196,305), which are lighter than the cost run-rate because payables rose. The UK's 84,200 GBP is excluded until translated; it is movable per your inputs.

### 4. Short-term investment policy (criteria only; no product or bank named)

Order of priorities: safety, then liquidity, then yield. Eligible: government securities, insured or rated time deposits and government money market funds; maximum maturity 6 months, weighted-average maturity 90 days; no more than 1,000,000 per counterparty (your cap); USD and GBP only; each placement approved by two authorised people. Limits beyond your 1,000,000 cap are proposals.

### 5. Payment controls — **designed, not tested**

Dual approval for payments above a threshold you set, matching the two operating-account signatories; callback verification for new or changed payee details; positive pay for cheques (cheques 2287 and 2291 were issued in September); wires (64,200 to Kestrel Supplies, plus a 35 fee) only where ACH will not do; quarterly review of online banking access; Stripe payout destination changes under dual control. None of this was observed operating.

### 6. FX and intercompany

Translation exposure: Northbrook UK net assets **187,420 GBP** (share capital 100,000 + retained earnings 52,420 + 2025 profit 35,000). **Intercompany does not agree**: Northbrook Trading owes UK **38,000** (2300); UK shows a receivable of **33,220** (1300). Difference 4,780, or an implied rate of 1.1439 if one side is in GBP; reconcile before any pooling. Pooling or sweeping between the two entities creates intercompany loans: **tax and legal review required first**.

### 7. Facilities

Term loan drawn 220,000; 6,900 a month in debt service. No revolver or undrawn facility was supplied, so none is counted as liquidity.

### 8. KPIs

Cash balance [manual, from TB]; concentration by bank [manual, mapped above]; days cash on hand [manual, computed]; idle cash % and yield [not measurable: no interest income in the TB]; bank fees 16,155 YTD [manual, from TB]; forecast accuracy [needs the 13-week forecast].

## (d) What was not done, and why

| Step | Status | Gap |
|---|---|---|
| 1 Map | done with a limit | UK bank details missing; dormancy needs 12 months of movements |
| 2 Structure | proposed | Second counterparty; pooling only after tax/legal review |
| 3 Liquidity | proposed | Buffer not sized from observed volatility |
| 4–5 Investment, payments | designed | Not tested; approval thresholds are yours to set |
| 6 FX | partial | No GBP rate; intercompany unreconciled |
| 7 Facilities | done | No revolver terms |
| 10 Workbook and policy | not created | Would you like `Treasury_2025_Northbrook Trading Ltd.xlsx` and the policy document? Only on a yes |
| 11 Save preferences | not offered yet | Account map and limits only; no balances or signatories saved |

**Coverage (manual run).** Environment: Northbrook Trading Ltd (USD) and Northbrook UK Ltd (GBP), user-asserted; data source upload; verdicts as in (b). Capability map: not applicable, no connection; every task `[manual]`. Not done: dormancy scan, payment-run pattern, new-payee-before-large-payment test — each needs 12 months of ledger and vendor history.

**Data sources:** user uploads only — `trial_balance_2025-09-30.csv`, `cash_account_ledger_2025-09.csv`, `treasury_inputs.md`, `trial_balance_northbrook_uk_2025-09-30.csv`.
