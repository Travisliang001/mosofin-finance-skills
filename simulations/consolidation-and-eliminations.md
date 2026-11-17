# Consolidation — Northbrook Trading Ltd group — 30 September 2025 (nine months)

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read each entity's trial balance at the same date and both sides of every intercompany balance ([docs.mosofin.com](https://docs.mosofin.com)).

## Read-back

Consolidating **Northbrook Trading Ltd (parent, USD)** and **Northbrook UK Ltd (80% owned since 1 March 2019, functional currency GBP)** at **30 September 2025**, nine months year to date, under **US GAAP**, presentation currency **USD**, from **your uploads**. Rates from **`fx_rates.csv` (bank rate sheet)**. Group structure, ownership and functional currency come from `group_structure.md` — facts that arrived inside a file; used once you confirm them here.

Unanswered, and how this run treats them:
- **Acquisitions, fair value adjustments, goodwill, equity-method investments (E)**: the structure note says no acquisitions or disposals in 2025; nothing on the 2019 acquisition. **Assumed none — no goodwill, no fair value adjustments, no associates.** This is an assumption, not evidence.
- **Prior-period consolidated balances (F)**: not supplied. **The NCI and CTA roll-forwards start from this period**, and the UK's opening retained earnings cannot be split from CTA (below).

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Account-level TB, 29 accounts, USD-sized; carries **2300 Intercompany Payable – Northbrook UK** → the **parent's** TB. Debits = credits **6,589,681** | No entity or currency named; date in file name only | Yes | Steps 2, 4, 5, 6, 9 (parent column) | **Accepted with a limit**: company and date user-asserted. **No investment-in-subsidiary account** (Finding 2) |
| `trial_balance_northbrook_uk_2025-09-30.csv` | Northbrook UK TB, 10 accounts, GBP. Debits = credits **603,520** | Entity in file name; currency and date user-asserted | Yes | Steps 3, 4, 5, 6 (UK column) | **Accepted with a limit**: currency GBP per the structure note |
| `group_structure.md` | Group structure note: parent, 80% sub, functional currencies, presentation USD | Group; "no acquisitions or disposals in 2025" | A summary, not the shareholder register or acquisition agreement | Step 1 (scope), Step 6 (NCI %) | **Accepted with a limit**: ownership and functional currency **user-supplied, not evidenced** |
| `fx_rates.csv` | GBP/USD closing 1.27 (30 Sep 2025), average 1.255 (Jan–Sep 2025), historical 1.31 (1 Mar 2019), four transaction-date rates; source "bank rate sheet" | Matches the date and period | Yes | Step 3 (translation), Step 5 (IC matching) | **Accepted** |
| `intercompany_ledger_northbrook_trading.csv` | Parent's IC ledger: 3 items, USD, total **−38,000** | Jul–Sep 2025 | Yes; no account coding | Step 5 (A and B) | **Accepted with a limit**: does not say which parent P&L or inventory accounts hold the charges |
| `intercompany_ledger_northbrook_uk.csv` | UK's IC ledger: 4 items, GBP, total **33,220** | Jul–Sep 2025 | Yes | Step 5 (A and B) | **Accepted** |
| `trial_balance_2025-09-30_v2.csv` | A 4-line TB whose bank account is **"Bank — Harlow Fabrication Ltd"**; equity 66,000. Foots (306,000) but is **another company's books** — Harlow is not a group member, and the lines match neither group entity | Names a **different company** | n/a | No step: not in the group | **Rejected** — wrong company. If a revised parent TB was meant, upload it in its place |

**Still missing:** (1) **where the parent carries its investment in Northbrook UK** (account and balance); (2) UK **retained earnings at acquisition (1 Mar 2019)** and any goodwill; (3) **prior-period consolidated balances** (opening NCI, opening CTA); (4) the parent accounts that hold the IC charges, and how much of the UK goods is **still in parent inventory**. I would wait here; proceeding on the accepted files as instructed.

## Findings

**1. Intercompany balance does not agree — 4,189.40 difference, not eliminated.**

| Item | UK (GBP) | UK at transaction rate (USD) | Parent (USD) | Difference |
|---|---:|---:|---:|---:|
| IC-071 mgmt fee, 10 Jul | 9,450 | 11,999.61 | 12,000 | 0.39 |
| IC-082 goods, 12 Aug | 14,570 | 18,503.90 | 18,500 | −3.90 |
| IC-093 goods, 18 Sep | 5,900 | 7,493.00 | 7,500 | 7.00 |
| **IC-097 goods, 29 Sep** | **3,300** | **4,191.00** | **not recorded** | **−4,191.00** |
| Balance at closing 1.27 | 33,220 → **42,189.40** | | **38,000** | **4,189.40** |

Cause: **IC-097, shipped by the UK on 29 September, is not in the parent's books** — goods in transit / cut-off. The remaining **1.60** (37,998.40 vs 38,000) is rate rounding. **Proposed elimination A (matched part only):** DR 2300 IC Payable – Northbrook UK 37,998.40 / CR UK 1300 IC Receivable 37,998.40. **Not eliminated:** IC-097 4,191.00 (left on the UK receivable) and the 1.60 rounding (left on the parent payable), both shown in the tie-outs. If you confirm IC-097 was in transit, the parent's own books need it recorded (a proposal for your team: DR inventory in transit 4,191 / CR 2300) — then eliminate it too.

**2. The parent's trial balance has no investment in Northbrook UK.** Nothing in 1000–1510 is an investment account. So **elimination E (investment against the UK's equity) cannot be drafted**, and the UK's share capital (GBP 100,000 → **USD 131,000** at the 1.31 historical rate) stays inside consolidated equity. Consolidated equity attributable to the parent is therefore **overstated by an unknown amount** until you tell me where the investment sits and what RE the UK had at acquisition.

**3. Translation (current-rate method; functional GBP, per your note).** Assets 226,520 × 1.27 = **287,680.40**; AP 39,100 × 1.27 = **49,657.00**; net assets **238,023.40**. Share capital 100,000 × 1.31 = **131,000**. Revenue 412,000, COGS 251,000, opex 126,000 × 1.255 → net income GBP 35,000 = **USD 43,925**. Opening RE (GBP 52,420) and CTA together = **63,098.40**; they cannot be split without prior consolidated balances (historical rates for each year's earnings). CTA goes to OCI, not profit.

**4. Intercompany revenue and expense.** UK sales to the parent in the period: GBP 33,220; matched three items GBP 29,920. **Proposed elimination B:** DR UK Sales Revenue 38,000 / CR parent expense or inventory 38,000 (parent accounts to be confirmed). At the UK's average rate those sales translate to 37,549.60; the **450.40** gap is a translation difference and belongs in CTA. IC-097 (GBP 3,300) excluded until resolved.

**5. Unrealised profit in parent inventory — not computed.** Goods shipped GBP 20,470 (IC-082, IC-093). Whether the parent still holds them is not in any file. Sensitivity only, not proposed: if all were on hand and the UK's average gross margin (39.1%) applied, the unrealised profit would be up to GBP 7,999 (≈ USD 10,159).

**6. NCI (20%), proportional share, starting this period.** Balance sheet: 20% × 238,023.40 = **47,604.68**. Income: 20% × 43,925 = **8,785**. Opening NCI and NCI dividends: not supplied.

## Consolidated (provisional — before Findings 2 and 5 are resolved)

| | Parent | UK (USD) | Eliminations | Consolidated |
|---|---:|---:|---:|---:|
| Total assets | 2,836,496.00 | 287,680.40 | (37,998.40) | **3,086,178.00** |
| Total liabilities | 558,564.00 | 49,657.00 | (37,998.40) | **570,222.60** |
| Equity incl. NCI | 2,277,932.00 | 238,023.40 | — | **2,515,955.40** (NCI 47,604.68) |
| Net income (9M) | 605,615.00 | 43,925.00 | 0 | **649,540.00** → NCI 8,785; parent 640,755 |

## Tie-outs (Step 9)

1 Eliminations balance: yes (A, B). 2 BS balances: yes, 3,086,178.00 = 570,222.60 + 2,515,955.40. 3 NI = sum − IC profit: **before** unrealised profit (Finding 5). 4 NCI = roll-forward: opening not supplied. 5 CTA: not separable (Finding 3). **6 IC balances fully eliminated: NO** — 4,191.00 receivable and 1.60 payable remain. 7 IC revenue/expense: matched part only; IC-097 open. **8 Parent equity check: not possible** — no investment account, no acquisition-date RE.

## Not done, and why

Elimination E and goodwill (Finding 2); unrealised profit (Finding 5); opening NCI and CTA roll-forward (no prior consolidation); consolidated cash flow statement (no cash flow data per entity); IC dividends (none in either TB). Excel workpaper `Consolidation_2025-09_Northbrook Trading Ltd.xlsx` offered, not created without your yes.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Group Northbrook Trading Ltd, 30 Sep 2025, USD, US GAAP — **user-asserted**. Source: **upload** (Mosofin not used, your choice). Both entity TBs **supplied, not read**; same date per file names. Rates: bank rate sheet. `trial_balance_2025-09-30_v2.csv` **rejected** (Harlow Fabrication Ltd, not a group member) |
| Capability map | Not applicable: no connection. Every task is `[manual]`, for both entities |
| Steps | 1 done (structure note, user-supplied) · 2 done with a limit (framework/policy alignment not evidenced) · 3 done, CTA not separable · 4 done · 5 A and B matched part only; C **not done**; D none; E **not done**; F none · 6 done with a limit · 7 none (assumed) · 8 BS and IS only, provisional · 9 two tie-outs fail, shown · 11 not offered |
| Not done | Investment account; acquisition-date RE; prior consolidation; parent IC account coding; buyer inventory detail |

Every elimination is a proposal; nothing was posted. **Data sources:** upload — parent: `trial_balance_2025-09-30.csv`, `intercompany_ledger_northbrook_trading.csv`; Northbrook UK: `trial_balance_northbrook_uk_2025-09-30.csv`, `intercompany_ledger_northbrook_uk.csv`; group: `group_structure.md`, `fx_rates.csv`.
