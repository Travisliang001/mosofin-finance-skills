# Intercompany reconciliation — Northbrook group, September 2025

Mosofin is not connected, so this run is manual, from the ledgers you uploaded for each company.

## (a) Read-back

> Reconciling intercompany balances as at **30 September 2025** between **Northbrook Trading Ltd (USD)** and **Northbrook UK Ltd (GBP)**, from **your uploaded files**. Reporting currency **USD**, rates from **the table you supplied (bank rate sheet)**. No group member is missing: the structure note lists two companies, one pair. Shall I go ahead?

Not answered at intake, with the default applied:

- **Intercompany accounts and naming (D):** neither ledger names its account. Proposed: the Trading file is Northbrook Trading's intercompany **payable to Northbrook UK** (all amounts negative); the UK file is Northbrook UK's intercompany **receivable from Northbrook Trading** ("US"). References `IC-nnn` are shared by both sides and are the join. **This needs your yes.**
- **Intercompany agreement (F):** not supplied. Causes that depend on it — mark-up, gross vs net, which rate each side should use, payment terms, settlement currency — are **not assessed**.
- **Date window / amount tolerance:** none agreed. Matching is on reference only; no window was needed. No tolerance applied: every difference is shown.
- **Year-ends:** not stated; the same calendar date (30 Sep 2025) is used for both.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `intercompany_ledger_northbrook_trading.csv` | Intercompany ledger, 3 lines, date / reference / description / amount_usd | Company only in the file name; USD; lines 10 Jul - 18 Sep 2025, descriptions refer to "UK" | Yes. Total (38,000) USD. No account, no opening balance, no counterparty column. | Yes — Steps 1-3 | **Accepted with a limit**: taken as the complete open balance at 30 Sep; account not named |
| `intercompany_ledger_northbrook_uk.csv` | Intercompany ledger, 4 lines, same columns in GBP | Company only in the file name; GBP; lines 10 Jul - 29 Sep 2025, descriptions refer to "US" | Yes. Total 33,220 GBP. Same gaps. | Yes — Steps 1-3 | **Accepted with a limit**: as above |
| `fx_rates.csv` | FX rate table GBP/USD, 5 rates with type, date and source (bank rate sheet) | Closing 30 Sep 2025 = 1.27; average Jan-Sep 1.255; transaction rates for 10 Jul and 12 Aug only | Yes for the balance. **No transaction rate for 18 Sep or 29 Sep.** | Yes — Steps 3 and 5 | **Accepted with a limit**: translation at transaction-date rates is not possible for IC-093 and IC-097; I will not supply a rate |
| `group_structure.md` | Group structure note: parent Northbrook Trading Ltd (USD), Northbrook UK Ltd (GBP, 80% owned since 1 Mar 2019), presentation currency USD | Names both companies; no period, "no acquisitions or disposals in 2025" | Yes | Yes — Step 1 (which pairs exist) and the reporting currency | **Accepted** |
| `intercompany_ledger_northbrook_trading_final.csv` | **Not a ledger.** Columns employee, week_1..week_4 with nights / days / off — a staff shift rota | No company, dates or amounts | No | No step uses it | **Rejected** on content. Set aside; the Trading ledger above is used. If a later ledger exists, upload it. |

**Still missing:** your confirmation of the intercompany accounts (required); transaction rates for 18 and 29 September (only if you want line-level translation at transaction rates); the intercompany agreement (recommended); October postings for Northbrook Trading (to confirm cut-off).

I would wait here for your answer. *(Assumed answer: "yes to the accounts as proposed; go ahead with the accepted files".)*

## (c) Findings

### Pair matrix (2 companies, 1 pair)

| Pair | Both sides supplied? | Cross-currency? | Reconcilable? |
|---|---|---|---|
| Northbrook Trading Ltd (USD) ↔ Northbrook UK Ltd (GBP) | Yes | Yes | **Yes** — from uploads, user-asserted |

### Balance for the pair (translate, then compare; closing rate 1.27, bank rate sheet, 30 Sep 2025)

| | Local | USD |
|---|---:|---:|
| Northbrook UK — receivable from Trading | GBP 33,220 | 42,189.40 |
| Northbrook Trading — payable to UK | USD (38,000) | (38,000.00) |
| **Difference — UK shows more than Trading** | | **4,189.40** |

Split of the difference:

| Component | USD |
|---|---:|
| Timing / unrecorded on one side: IC-097, on UK's books only | 4,191.00 |
| FX (rate differences on the three matched lines) | (1.60) |
| True mismatch (amount disagreement not explained by rate) | 0.00 |
| **Total** | **4,189.40** |

### Transaction-level matching

| Ref | UK line (GBP) | UK in USD at 1.27 | Trading line (USD) | Difference | Match basis | Status |
|---|---:|---:|---:|---:|---|---|
| IC-071, 10 Jul, management fee | 9,450 | 12,001.50 | (12,000) | 1.50 | Reference, same date | Matched pair with a rate difference |
| IC-082, 12 Aug, goods | 14,570 | 18,503.90 | (18,500) | 3.90 | Reference, same date | Matched pair with a rate difference |
| IC-093, 18 Sep, goods | 5,900 | 7,493.00 | (7,500) | (7.00) | Reference, same date | Matched pair with a rate difference |
| IC-097, 29 Sep, goods | 3,300 | 4,191.00 | — | 4,191.00 | — | **Unmatched — on UK only** |

At the transaction-date rates supplied: IC-071 at 1.2698 = 11,999.61 (0.39 under Trading's 12,000); IC-082 at 1.27 = 18,503.90 (3.90 over). Trading's figure for IC-093 implies a rate of about 1.2712; no rate for that date was supplied, so it cannot be tested.

### Mismatches

| # | Item | Amount | Probable cause | Recommended action | Age at 30 Sep |
|---|---|---:|---|---|---|
| 1 | **IC-097**, goods shipped to US, dated 29 Sep 2025 — on Northbrook UK's ledger, **not on Northbrook Trading's** | GBP 3,300 = USD 4,191.00 at closing | Probable **cut-off timing**: shipped by UK one day before period end and not yet booked by Trading. It could instead be a missed posting; Trading's October ledger was not supplied, so which is not shown. | Confirm shipping terms and receipt date. If Trading owned the goods at 30 Sep, Trading books the purchase and payable in September (proposal below); if not, UK's sale is early. Do not adjust UK's figure to force agreement. | 1 day |
| 2 | Rate differences on IC-071, IC-082, IC-093 | net (1.60) | Each side recorded in its own currency at a slightly different rate. | No entry in either company's books; carried as a translation difference at consolidation. | — |

No journal posted direct to an intercompany account without a document can be identified: the files carry no source or document type.

### Ageing of the open balance (Trading's payable)

IC-071 (12,000) is 82 days old; IC-082 (18,500) 49 days; IC-093 (7,500) 12 days. Nothing has been settled since July; payment terms are not known, so "overdue" is not assessed.

### Settlement proposal (agreed items only; IC-097 excluded until resolved)

| Pair | Net amount | Paying | Receiving | Currency | Date |
|---|---|---|---|---|---|
| Trading ↔ UK | USD 38,000 on Trading's books = GBP 29,920 on UK's books | Northbrook Trading Ltd | Northbrook UK Ltd | Not stated — needs the agreement | Yours to set |

### Elimination entries — PROPOSALS for the consolidation ledger, NOT POSTED

| # | Entry | Dr | Cr |
|---|---|---:|---:|
| 1 | Eliminate the agreed balance: Dr Intercompany payable (Trading) / Cr Intercompany receivable (UK) | 38,000.00 | 38,000.00 |
| 2 | Residual on UK's translated receivable, carried explicitly, not buried: 42,189.40 − 38,000.00 = 4,189.40, being IC-097 4,191.00 (goods in transit / unrecorded payable, pending item 1) less 1.60 FX to the translation reserve (CTA — the equity line that holds currency translation differences) | — | — |
| 3 | If you confirm Trading owned the goods at 30 Sep — proposal for **Trading's own books**: Dr Inventory (goods in transit) / Cr Intercompany payable — Northbrook UK. USD amount needs the 29 Sep transaction rate, which was not supplied; 4,191.00 at the closing rate is indicative only. | 4,191.00 | 4,191.00 |

Intercompany revenue against expense (management fee and goods) also eliminates at consolidation, in full despite the 80% holding; the amounts need each side's P&L accounts and transaction-date rates, which were not supplied. **Unrealised profit in inventory** on goods UK sold to Trading and Trading still holds is not assessed: it needs Trading's closing holdings and UK's mark-up.

## (d) What was not done, and why

- **Intercompany accounts** were proposed, not confirmed against a chart of accounts or trial balance; neither ledger was tied to a book balance.
- **Transaction-rate translation** for IC-093 and IC-097: no rate supplied; none invented.
- **Cut-off proof for IC-097:** no October ledger for Trading and no shipping documents.
- **Agreement-dependent causes** (mark-up, gross/net, rate convention, withholding tax, payment terms, settlement currency): not assessed — no agreement.
- **Revenue/expense and unrealised-profit eliminations:** not quantified — data not supplied.
- **Excel workpaper** (`IC_Reconciliation_2025-09.xlsx`): not created — say yes if you want it.
- **Nothing was posted, sent, settled or changed** in either company's books. Every entry is a proposal.

**Data sources:** uploaded intercompany ledgers for Northbrook Trading Ltd and Northbrook UK Ltd; uploaded FX table (bank rate sheet); uploaded group structure note; company, period and currency as typed at intake.
