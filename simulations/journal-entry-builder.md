# Journal entry builder — Northbrook Trading Ltd, September 2025 accruals

Mosofin is not connected, so this run is manual: every validation is `[manual]`, on the files you uploaded. (Connecting Mosofin would read the chart, the accrual account and open bills directly — docs.mosofin.com. Not raised again.)

**PROPOSED ENTRY — NOT POSTED.** Nothing here has been recorded anywhere; a person reviews and posts it.

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Period:** September 2025, posting date **2025-09-30**. **Currency:** USD (user-asserted; no file states it).
- **Request:** one accrual entry for the three September items in `accrual_candidates_2025-09.csv`.
- **Unanswered at intake, defaults applied:** accounting system not named → **generic import columns**; tax jurisdiction not given → **no tax lines** (the skill adds tax only when a jurisdiction is supplied); **materiality threshold not given → not assumed**, so the large-entry flag cannot run; accounting basis not stated → **accrual basis assumed** (accruals are wrong on a pure cash basis — please confirm).

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `accrual_candidates_2025-09.csv` | List of 3 services received but not invoiced: vendor, description, date received, estimated amount, evidence | No entity named; dates 26–30 Sep 2025 | Yes; amounts total **11,850** | Steps 1, 3, 4 (the event to record) | **Accepted with a limit:** company user-asserted; estimates, not invoices — every amount is user-supplied, not evidenced |
| `chart_of_accounts.csv` | Chart of accounts: 41 accounts with number, name, type; no duplicates | No entity named | Yes; number, name and type present | Steps 2, 3, 6 (accounts exist, sign vs type) | **Accepted with a limit:** company user-asserted; not in numeric order (e.g. 1510 after 1600, 2400 among expenses), which does not affect use |
| `accrual_candidates_2025-09_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4, nights/days/off) — not accrual candidates despite the name | No company, no period | No amounts, vendors or accounts | No step uses it | **Rejected:** a staff rota. If a revised accrual list exists, upload that instead |

**Still missing (not in your upload, needed for full validation):** (1) **the Accrued Liabilities (2100) ledger detail or open-bills list for September/October** — the Pitfall 1 double-count check needs it; (2) **materiality threshold** for the review flag; (3) **your accounting system** if you want a system-specific import file; (4) whether the period is still open and not yet reported.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) The proposed entry

```
PROPOSED ENTRY — NOT POSTED
Entity: Northbrook Trading Ltd (user-asserted)
Date: 2025-09-30            Entry #: to be assigned by preparer
Type: Accrual (reversing 2025-10-01)
Reference: Summit Freight delivery log; Greyfriars Legal LLP engagement letter; Northgate Utilities 3-month average
Memo: Accrue September services received, not yet invoiced — invoices expected October 2025
Source: journal-entry-builder, from accrual_candidates_2025-09.csv (user-supplied estimates)
```

| Account No. | Account Name | Debit | Credit | Line memo |
|---|---|---|---|---|
| 6900 | Postage and Delivery | 5,800.00 | | Summit Freight — freight, last week of Sep 2025 (delivery log) — **confirm outbound; see note 1** |
| 6400 | Professional Fees | 4,200.00 | | Greyfriars Legal LLP — contract review, Sep 2025 (engagement letter rate) |
| 6170 | Utilities | 1,850.00 | | Northgate Utilities — electricity, Sep 2025 (estimate: prior three months' average) |
| 2100 | Accrued Liabilities | | 11,850.00 | Accrual of the three September items above; reverse 2025-10-01 |
| **Total** | | **11,850.00** | **11,850.00** | **Balanced** |

**Reversing entry (also a proposal):** dated **2025-10-01** (first day of the next period), DR 2100 Accrued Liabilities 11,850.00 / CR 6900 5,800.00, 6400 4,200.00, 6170 1,850.00; memo "Reverse September accrual dated 2025-09-30"; entry # to reference the original once assigned.

**Notes for the reviewer**

1. **Freight coding needs your decision.** Your chart has no freight account. 6900 Postage and Delivery fits **outbound** freight. If this is **inbound** freight on inventory purchases, it belongs in inventory cost (1200 Inventory, or 5000 Cost of Goods Sold if the goods were sold) — I have not defaulted that judgement.
2. **Utilities 1,850 is an average, not a reading** — the weakest of the three estimates; true up when the bill arrives.
3. **Legal 4,200** is at the engagement-letter rate; confirm hours with Greyfriars before posting if the bill is due soon.
4. No line touches a control account (cash, AR, AP or revenue): the credit goes to 2100, a liability accrual account, not 2000 Accounts Payable.

### Validation results (check by check)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Debits = credits to the penny | **Pass** | 5,800 + 4,200 + 1,850 = 11,850 = 11,850 |
| 2 | All accounts exist in the chart | **Pass** | 6900, 6400, 6170, 2100 all in `chart_of_accounts.csv` |
| 3 | Date within an open period | **Not run** | No period status supplied |
| 4 | Memo explains business purpose | Pass | Header and every line |
| 5 | Source documents referenced | Pass with a limit | Evidence named per line; documents not uploaded |
| 6 | Reversing flag correct | Pass | Accrual, reverses 2025-10-01 (not 30 Sep) |
| 7 | Signs match account types | **Pass** | Debits to 3 Expense accounts; credit to Other Current Liability |
| 8 | No P&L accounts in a pure BS reclass | N/A | Not a reclass |
| 9 | Tax lines present if warranted | Not run | No jurisdiction supplied |
| 10 | No existing accrual already covers these items (Pitfall 1) | **Not run** | 2100 ledger / open bills not supplied — **the key gap** |
| 11 | No open invoice for a receipt to revenue | N/A | No receipt |
| 12 | Loan payment split | N/A | No loan payment |
| 13 | Target is not a control account | **Pass** | 2100 is an accrual account |
| 14 | Materiality review flag | Not run | No threshold given; none assumed |
| 15 | Clearing / suspense balances | N/A | None touched |

**Validated: 7 checks passed (one with a limit), 4 not run, 4 not applicable.**

## (d) What was not done, and why

- **Pitfall 1 double-count check:** no Accrued Liabilities detail or bills list. If any of these vendors' September invoices is already entered, that line must come out.
- **Period-open and already-reported check, materiality flag, tax lines:** inputs not supplied.
- **System-specific import file:** platform not named; generic columns used. Excel workpaper `Northbrook Trading Ltd_JE_September accruals_2025-09-30.xlsx` not created — say yes if you want it.
- **`accrual_candidates_2025-09_final.csv`:** rejected (shift roster); not used.
- **Nothing was posted, sent, paid or changed.** Both entries above are proposals.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, posting date 2025-09-30, USD — user-asserted. Source: upload (no Mosofin connection). 2 files accepted with a limit; `accrual_candidates_2025-09_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done with a limit (uploads); 1 done (accrual, reversing); 2 done (signs vs uploaded types); 3 done; 4 done (accrual + reversal pattern); 5 not done (no jurisdiction); 6 done with a limit (7 pass, 4 not run); 7 done (generic columns, in chat); 8 not offered until results approved |
| Not done | Pitfall 1 accrual check (2100 GL detail / open bills); period status (close status); materiality (threshold); tax (jurisdiction) |

**Data sources:** user uploads — `accrual_candidates_2025-09.csv`, `chart_of_accounts.csv`.
