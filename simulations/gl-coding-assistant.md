# GL coding suggestions — Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected for this run (you chose upload only), so every step is `[manual]` and works from your files. Connecting Mosofin would automate the reads — docs.mosofin.com. **Nothing was coded, recoded or posted**: every account below is a **suggestion** for a person to apply in your own system.

## (a) Read-back

Suggesting GL accounts for **6 uncoded transactions** of **Northbrook Trading Ltd** (user-asserted; no file names it), **September 2025**, **USD**, single entity, coding **only to accounts in your uploaded chart** (no placeholders needed — the chart was supplied).

| Not answered at intake | What I did |
|---|---|
| Tax jurisdiction and tax code list | Not given → **"Tax code: TBD — confirm with tax setup"** on every line. No tax rule assumed. |
| Capitalization threshold | **Not defaulted.** No line looks like equipment; flagged where relevant as "threshold unknown — please confirm". |
| House coding policy | None → history and the chart only. |
| Source account (bank or card) of the six items | Not in the file. None of the six appears among the September bank lines in your GL extract, so they may be card spend (2050 Corporate Card Payable) — please confirm. |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `uncoded_transactions.csv` | Bank/card-feed style list: date, raw description, signed amount. 6 outflows, total **−8,997.14** | 4–27 Sep 2025; no company or source account | Yes; descriptions readable | Yes — the batch to code (Steps 1–2) | **Accepted with a limit: company user-asserted; source account unknown** |
| `chart_of_accounts.csv` | Chart of accounts: 36 accounts, number, name, type | No company | Yes. No uncategorized/suspense account; **no Utilities, Airfare or Legal-specific account** | Yes — every suggestion must come from it (Step 2) | **Accepted** |
| `general_ledger_2025-09.csv` | September GL extract: 15 one-sided bank lines on 1000 and 7 journals (14 lines; DR = CR = 79,799) | 31 Aug–30 Sep 2025; no company | Usable as **coding history only to a limited extent**: one month, bank lines carry no offset account, so no vendor-to-account history can be read. One relevant precedent: JE-0905 "Legal fee missed in August" → 6400 Professional Fees | Yes — Tier 1 history (Step 2) | **Accepted with a limit**: one month, no vendor-level history |
| `uncoded_transactions_final.csv` | **Not a transaction list.** A staff shift rota: employee E08–E10, week_1…week_4, "nights/days/off" | No company, dates or amounts | No | No step | **Rejected** on content despite the name. Not used. |

Still missing (would raise confidence): **prior months' coded ledger** (vendor history for Tier 1), the **source account** of the six items, the **tax jurisdiction and configured tax codes**, the **capitalization threshold**, and any house coding rules.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Suggested coding

| Date | Vendor (cleaned) | Description | Amount | Suggested GL account | Tax code | Confidence | Evidence / tier | Reasoning | Flags |
|---|---|---|---:|---|---|---|---|---|---|
| 2025-09-04 | Adobe | ADOBE *CREATIVE CLOUD | −89.99 | **6300 Software** | TBD | 🟢 High | Tier 2 — SaaS tool; no history | Creative Cloud is a software subscription and 6300 is the chart's software account. | Likely recurring monthly; confirm |
| 2025-09-09 | Delta Air Lines | DELTA AIR 0062341 | −612.40 | **6800 Travel and Meals** | TBD | 🟢 High | Tier 2 — airline; no history | Airfare; the chart has no separate airfare account, so the combined travel account is the match. | Traveller and business purpose not in the file |
| 2025-09-11 | Northgate Utilities | NORTHGATE UTILITIES | −1,840.00 | **No Utilities account exists in this chart.** Nearest: 6100 Rent (occupancy) — **confirm, or add a Utilities account** | TBD | 🟡 Medium | Tier 2 — utility; chart gap | A utility bill has no exact home in this chart; I will not invent one. | ⚠️ Chart gap — your decision |
| 2025-09-18 | Amazon (Marketplace) | AMZN MKTP US*2K4 | −214.75 | **6700 Office Supplies** | TBD | 🟡 Medium | Tier 2 — general retailer; no history | Office supplies is the usual business purchase, but a marketplace order can hold anything. | ✂️ Possible split; 👤 confirm business purpose |
| 2025-09-24 | Unknown originator | ACH DEBIT UNKNOWN ORIG 88213 | −1,240.00 | **Needs Review** | TBD | 🔴 Low | Tier 5 — cannot classify | No payee name, no history and no keyword; I will not guess. | ⚠️ Identify the originator from the bank's ACH detail before coding |
| 2025-09-27 | Greyfriars Legal LLP | GREYFRIARS LEGAL RETAINER | −5,000.00 | **6400 Professional Fees** — or **1300 Prepaid Expenses** if the retainer is held against future work | TBD | 🟡 Medium | Tier 3 — keyword "legal"; one precedent (JE-0905 legal fee → 6400) | Legal fees go to 6400 in this ledger, but a retainer is often an advance, which is an asset until used. | ⚠️ Round amount; retainer terms needed; posted Saturday |

**Summary:** 6 transactions, **8,997.14** in total. Confidence: **High 2 (33%)**, **Medium 3 (50%)**, **Low 1 (17%)**. **Flagged: 4** — Northgate (chart gap), Amazon (possible split), the unknown ACH (needs review), Greyfriars (expense vs prepaid). No transfer, related-party, cross-border or capex flag applies on what the files show; the capitalization threshold is unknown, so the capex test is not run for certain.

**Data quality notes:**
- **No Tier 1 match was possible for any line**: the GL extract holds one month and no vendor-to-account postings. Every confidence above rests on vendor type or keyword, not on how this entity has coded these vendors before.
- **No uncategorized or suspense account** exists in the chart, so there is no uncoded backlog to report beyond this batch.
- The unknown ACH debit of 1,240.00 is the item to chase first: an unidentified debit should be traced to its originator and authority, not just coded.

## (d) Not done, and why

Tier 1 history (no prior coded ledger); tax codes (no jurisdiction or code list); capex threshold check (no threshold); uncoded-population sheet (no suspense account). No `.xlsx` created — I would ask whether you want `Northbrook Trading Ltd_Coded_Transactions_2025-09-30.xlsx`. Learning loop: if you recode any line, I will ask whether to keep it as a rule.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, September 2025, USD — user-asserted. Source: upload. Uncoded list and GL accepted with limits; chart accepted; `uncoded_transactions_final.csv` rejected (staff rota). COA: supplied, no fallback in use. |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 parse and normalise done (6/6) · vendor-master match **not done** (no vendor master) · 2 classify done: Tier 2 ×4, Tier 3 ×1, Tier 5 ×1; Tier 1 **not done** · 3 tax codes **not done** (TBD) · 4 special cases: split, chart gap, retainer flagged; capex **not done** (threshold); transfer and related-party checked, none · 5 tables in chat · 6 not offered. |
| Not done | Tier 1 history (prior coded GL); tax codes (jurisdiction + code list); capex check (threshold); source account (bank/card statement). |

**Data sources:** user uploads — `uncoded_transactions.csv`, `chart_of_accounts.csv`, `general_ledger_2025-09.csv`.
