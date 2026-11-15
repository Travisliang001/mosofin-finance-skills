# Bad debt and allowance — Northbrook Trading Ltd, 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded. Connecting Mosofin would let the loss rates be derived from your past ageings automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was posted and no balance was written off.

## Read-back

Assessing receivables for **Northbrook Trading Ltd** (user-asserted) at **30 September 2025**, in **USD**, under **US GAAP** with the **aged-percentage method** your policy names ("Receivables: allowance based on ageing"). Assumptions taken because the intake did not answer them:

| Question | Status | What this run does |
|---|---|---|
| C — framework | US GAAP, aged-percentage | Under US GAAP, trade receivables fall under **CECL** (current expected credit loss, ASC 326). An ageing matrix is an accepted way to apply CECL, but CECL also needs current conditions and a forecast. I treat the ageing method as a CECL provision matrix. That makes write-off history **required**, not just recommended. |
| D — insolvency, disputes, credit changes | Not answered | Candidates are flagged by age and payment history only. **No customer was confirmed** insolvent or in dispute. |
| E — write-off approval | No approval matrix supplied | **No write-off is proposed.** Specific balances are listed as candidates for review only. |
| F — forecast and tax jurisdiction | Not answered | No forward-looking adjustment and no tax-recovery entry. |

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `ar_aging_detail_2025-09-30.csv` | Invoice-level receivables ageing: customer, invoice, dates, amount, days overdue. 14 lines, 12 customers, incl. one credit memo | No company or currency in the file; dated by name and due dates to 30 Sep 2025. Days overdue recomputed against 30 Sep: all agree | Yes. Totals **798,360**, which agrees to TB account 1100 Accounts Receivable (798,360) | Steps 2–3 | **Accepted with a limit**: company and currency user-asserted |
| `ar_aging_detail_2025-09-30_final.csv` | **Not an ageing.** A staff shift rota: employee E08–E10, week_1…week_4, "nights / days / off" | No company, dates or amounts | No | No step | **Rejected** on its content. If a later "final" ageing exists, upload it; otherwise the ageing above is used. Not read into the work. |
| `customer_payment_history_12m.csv` | 60 **paid** invoices, Oct 2024–Sep 2025, with days to pay (recomputed: all agree). 2,801,789 in total | Same 12 customers as the ageing; no company name | Yes, for payment behaviour. It holds **no write-offs and no past ageings**, so it cannot give loss rates | Step 2 and Step 3 (current-condition signals) | **Accepted with a limit**: not a write-off history |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 29 accounts; debits = credits = 6,589,681 | No company name in the file | Yes. Gives the existing allowance, 1150 Allowance for Doubtful Accounts, **9,000 credit** at 30 Sep | Step 4 | **Accepted with a limit**: a balance only, not the allowance account detail, so no roll-forward |
| `accounting_policies.md` | Accounting policy summary | US GAAP, private company; accounts to be issued 20 March 2026 | Yes | Step 1 (framework and method) | **Accepted**: confirms framework and "allowance based on ageing", but **gives no loss rates** |

**Still missing:**
1. **Loss rates, or the history to derive them** (required): three to five years of write-offs and recoveries by ageing bucket, plus past ageings at the same dates, or rates you state as your own.
2. **Allowance account detail** for the period (required for the roll-forward): opening balance, charges, write-offs, recoveries.
3. The **write-off approval matrix** (who approves, up to what amount).
4. Any known insolvency, dispute or credit change (question D), and a forecast view under CECL (question F).

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

### 1. The required allowance cannot be computed from these files

The skill never assumes a loss rate, and none was supplied or is derivable. The paid-invoice history shows no losses, but it only lists invoices that **were** paid, so it says nothing about what share of each bucket was later lost. Your ageing, ready for the rates:

| Ageing bucket (days past due) | AR balance (USD) | Loss rate | Provision |
|---|---:|---|---|
| Current (not yet due) — invoices | 428,103 | not supplied | — |
| Current — unapplied credit CM-0312 | (2,150) | — | — |
| 1–30 | 200,127 | not supplied | — |
| 31–60 | 72,046 | not supplied | — |
| 61–90 | 48,031 | not supplied | — |
| 91–120 | 48,200 | not supplied | — |
| Over 120 | 4,003 | not supplied | — |
| **Total (= TB 1100)** | **798,360** | | **not computed** |

- **Existing allowance:** 1150 Allowance for Doubtful Accounts, **9,000** credit at 30 Sep 2025 (trial balance). That is 1.13% of total AR, and 17.2% of the 52,203 more than 90 days past due.
- **Adjustment:** not computed. Required allowance minus 9,000 will be the bad-debt charge or release once rates are given. **No allowance entry is proposed.**

### 2. Signals for the allowance and for any specific reserve (not write-offs)

- **Harlow Fabrication Ltd: concentration and a skipped invoice.** 248,157 open, **31.1% of all receivables**. Its days to pay rose every invoice: 76, 82, 88, 94, 100. INV-20418 (48,200, dated 28 May, 95 days overdue) is still open, yet a **later** invoice (INV-18004, dated 10 June) was paid on 18 Sep. Paying around an older invoice usually means a dispute or a short payment. Ask the account owner before reserving.
- **Foxhall Garden Centres: the oldest balance.** INV-20907, 4,003, **130 days overdue**, the only balance over 120 days. Invoices dated before and after it (March, May, July) were paid, so this one was also skipped. Days to pay 69 → 81.
- **Portfolio-wide slowing.** Every one of the 12 customers took 3 days longer on each successive invoice through the year (e.g. Pennine 38 → 50, Tideswell 56 → 68). Under CECL this is a current-conditions signal that the historical rates may understate losses. It needs your judgement (question F).
- **Tideswell Hotels.** 48,031 at 67 days overdue, consistent with its own history (56–68 days to pay). Slow, not yet abnormal.

### 3. Write-off candidates

**None proposed.** No customer has a qualifying reason (insolvency, dissolution, limitation period, legal advice, a lost dispute). Age alone is never a reason, and no approval matrix was supplied. Harlow INV-20418 and Foxhall INV-20907 are **candidates for review only**.

### 4. Credit memo and other checks

- **Calder Print CM-0312, (2,150), dated 2 Sep, unapplied.** Calder also has INV-20796, 32,020, 20 days overdue. Apply the credit before any reserve. The net balance is 29,870. This is a billing or cash-application item, not a bad debt.
- **Intercompany.** No Northbrook UK receivable is in the ageing (the TB shows only 2300 Intercompany Payable). Nothing to exclude.
- **Low-risk customers.** Elmfield Schools (12,008, current) may be a public-sector body. If so, give it a lower rate when the matrix is set.
- **Subsequent receipts.** Accounts are issued 20 March 2026. Cash received after 30 Sep on any overdue invoice is evidence for or against a reserve. Please send the post-period receipts.

## What was not done, and why

- Required allowance, adjustment, bad-debt entry: **no loss rates** (history or your own stated rates).
- Roll-forward (opening + charge − write-offs + recoveries = closing): **no allowance account detail**. Only the 9,000 closing balance is known.
- Specific write-offs and entries: no qualifying reason and no approval authority.
- Forward-looking CECL adjustment, tax recovery: questions F not answered.
- Excel workpaper `BadDebt_Allowance_2025-09.xlsx`: not created. Would you like it once the rates are in?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, 30 Sep 2025, USD, all user-asserted. Data source: upload, because the Mosofin gateway is absent. Files: ageing (accepted with a limit), payment history (accepted with a limit: not a write-off history), trial balance (accepted with a limit: balance only), policies (accepted), shift rota (rejected).
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 0 Fetch evidence | Done with a limit: no write-off history, past ageings or allowance detail |
| 1 Methodology | Done: US GAAP, ageing matrix treated as CECL provision matrix; no forecast |
| 2 Write-off candidates | Done with a limit: none proposed; 2 for review; credit memo found |
| 3 Allowance | **Not done**: no loss rates |
| 4 Adjustment | **Not done**: depends on Step 3; existing 9,000 identified |
| 5 Entries | **Not done**: nothing to propose |
| 6 Output | Tables in chat; xlsx on request |
| 7 Save preferences | Not offered: results incomplete |

**Not done:** roll-forward (needs allowance account detail), loss-rate derivation (needs past ageings and write-off history), prior-period comparison (needs prior allowance).

**Data sources:** upload — ar_aging_detail_2025-09-30.csv, customer_payment_history_12m.csv, trial_balance_2025-09-30.csv, accounting_policies.md.
