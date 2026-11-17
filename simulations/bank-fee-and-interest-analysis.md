# Bank fees and interest — Northbrook Trading Ltd, 13 months to 30 September 2025 (upload path)

Mosofin is not connected, so this run is manual: every figure comes from the files you uploaded. Connecting Mosofin would count wires, payments and deposits from the books automatically ([docs.mosofin.com](https://docs.mosofin.com)). Nothing was recoded or posted, and no bank was contacted.

**Bank statement supplied: September 2025 only.** Fees for September were tied both ways. For the other twelve months, **only fees posted in the books were examined**, so the 13-month total understates the true bank cost. It is not "total bank fees".

## Read-back

Bank fees and interest for **Northbrook Trading Ltd** (user-asserted), **September 2024 – September 2025**, in **USD**. Products, as you told me: **one operating account, wires, merchant services**. **No fee schedule** (question E), so rates paid are reported but not compared with a contract. **No earnings credit rate** (question F), as you confirmed.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Used by | Verdict |
|---|---|---|---|---|---|
| `bank_fee_and_interest_ledger_13m.csv` | A **monthly summary** of posted fees and interest: month, type, count, amount. 52 rows = 13 months × 4 types (monthly service fee, wire fee, merchant fees, interest expense) | Sep 2024 – Sep 2025. No company, account names or currency | Yes, at summary level. Counts are given for wires (40) but **0 for merchant fees**, so merchant unit rates cannot be computed. It is not line-level ledger detail, so descriptors and miscodings cannot be checked | Steps 1, 2, 4, 5 | **Accepted with a limit**: company user-asserted; summary, not ledger detail |
| `bank_statement_2025-09.csv` | Bank statement, 15 transactions; running balance recomputed and foots, 1,246,642 → **1,219,776** | September 2025 only; no account number or company | Yes | Step 3 (two-sided tie, September) | **Accepted with a limit**: one month of thirteen |
| `bank_fee_and_interest_ledger_13m_final.csv` | **Not a ledger.** A staff shift rota: employee E08–E10, week_1…week_4, "nights / days / off" | No company, dates or amounts | No | No step | **Rejected** on content. The name suggests a final fee ledger. Upload that if it exists; otherwise the ledger above is used. |

**Still missing:** bank statements (or the bank's account analysis statement) for **Sep 2024 – Aug 2025**, needed to find fees missing from the books; the **merchant processor statements** (Stripe), since merchant fees are charged by the processor, not the bank; line-level ledger detail for the fee and interest accounts; the term-loan schedule; the bank's fee schedule.

*Here I would stop and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## Findings

### 1. Categorised fees, last 12 months (Oct 2024 – Sep 2025), posted fees only

| Bucket | Driver | Count | Amount (USD) | Unit rate | Share of fees |
|---|---|---:|---:|---|---:|
| Account maintenance: monthly service fee | Fixed | 12 | 600 | 50 / month | 2.9% |
| Transaction: wire fees | Volume | 36 wires | 1,260 | **35 per wire** (every month: 140/4, 105/3, 70/2) | 6.1% |
| Merchant services | Volume | not given | 18,686 | **cannot compute**: no transaction count or sales volume | **90.9%** |
| **Bank and merchant fees** | | | **20,546** | | |
| Lending: interest expense | Fixed | 12 | 22,800 | 1,900 / month | (separate) |
| Interest earned | — | — | **0** | — | — |

Categories were read from the "type" label, not from bank descriptors. Treasury, cash-handling, FX and lending-fee buckets carry no posted fees. None of those is on your product list, so none is flagged. ACH is in use (the September statement shows ACH debits and credits) but no ACH fee is posted, and none appears on the September statement. That is consistent, not a gap.

### 2. September tie-out, statement against books (the only two-sided month)

| Fee | Statement | Ledger | Difference |
|---|---:|---:|---|
| Monthly service fee (30 Sep) | 50 | 50 | Tied |
| Wire fees | **1 wire, 35** (15 Sep, Kestrel Supplies) | **4 wires, 140** | **Books 105 higher: 3 wire fees not on the statement** |

With one operating account, three of the four wire fees booked in September have no matching wire or fee on the statement. Either they were posted in error (so bank fees are overstated by 105), or a second account exists that you have not mentioned. **Investigating**: please confirm before any correction. The 6,900 term-loan payment is consistent with 1,900 interest plus 5,000 principal. No missing postings were found for September. **For the other twelve months the missing-postings check was not performed**, so this is not a finding of nothing.

### 3. Trend

- Bank and merchant fees, September YoY: 1,579 → 1,822, **+15.4%**, driven by merchant fees 1,389 → 1,632 (**+17.5%**).
- Merchant fees rose every month from 1,250 (Dec 2024) to a peak of **1,844 (Jul 2025)**, then eased to 1,632. Without card volumes I cannot tell whether that is more sales or a higher effective rate.
- Wire fees swing 70–140 on a 2/3/4 wire cycle. The service fee is flat. No one-time items were identified.
- **Interest expense is a flat 1,900 every month** while the loan payment includes principal. On an amortising loan, interest should fall as principal falls. Check this against the loan schedule: a fixed accrual that is never trued up misstates interest.

### 4. Cost reduction options (each sized on its stated assumption)

| Option | Annual saving | Rests on | Assumption |
|---|---:|---|---|
| Review the merchant pricing model (interchange-plus vs flat vs tiered) | **not sizable yet**: needs processor statements | 18,686 posted merchant fees, 91% of the cost | Processor statements and card volumes supplied |
| Move wires to ACH where the payee accepts it | **up to 1,260** | 36 wires × 35 | ACH costs nothing, as the September statement suggests; the true ACH price needs the fee schedule |
| Idle cash earning nothing | **about 12,579 per 1 percentage point** of yield | September average daily balance **1,257,906**; no interest income posted in 13 months | Rate is the bank's to quote, not mine. No ECR, as you confirmed, so moving or sweeping the balance does not lose a hidden credit |
| Coding rule for the recurring 50 fee and 35 wire fee | time, not cash | 13 + 40 recurring same-amount charges | — |

### 5. Proposed entries

**None proposed yet.** The 105 September wire-fee difference is still being investigated. If the three fees prove to be posting errors: DR operating bank account 105 / CR bank fees 105. Use your own account names, since no chart of accounts was supplied. Stripe deposits arrive net of fees, so the netting check (grossing receipts up and recognising fees separately) needs the processor statement and was not run.

## Not done, and why

- Missing postings, Sep 2024 – Aug 2025: no statements for those months.
- Netted-fee check on Stripe transfers (18,842 and 21,307 in September): no processor statement or gross receipts.
- Merchant unit rate, and contracted-vs-paid comparison: no counts, no fee schedule.
- Miscoding scan: no line-level ledger.
- Excel workpaper `Bank_Fee_Analysis_2025-09.xlsx`: not created. Would you like it?

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, Sep 2024 – Sep 2025, USD, all user-asserted. Data source: upload, because the Mosofin gateway is absent. Fee ledger accepted with a limit (summary only); September statement accepted with a limit (one month); rota rejected.
**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Task | Status | Gap |
|---|---|---|
| 1 Fee taxonomy | Done with a limit | Categories from summary labels |
| 2 Classify lines | Done with a limit | No descriptors or line detail |
| 3 Tie to GL | Done for September only | 105 wire-fee difference investigating |
| 3 **Identify missing postings** | **Not done for 12 of 13 months** | **Bank statement not supplied** for Sep 2024 – Aug 2025 |
| 3 Miscodings / netting | **Not done** | Ledger detail; processor statements |
| 4 Trend and unit rates | Done with a limit | No merchant counts |
| 5 Playbook | Done, sized where possible | Fee schedule, processor pricing |
| 6 Entries | None proposed | Pending investigation |

**Data sources:** upload — bank_fee_and_interest_ledger_13m.csv, bank_statement_2025-09.csv.
