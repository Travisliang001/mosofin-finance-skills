# Stripe reconciliation — Northbrook Trading Ltd, September 2025 (upload path)

The Mosofin tools are not present, so this run is manual, from your uploads only. Nothing was posted, no payout initiated and no dispute actioned; every entry below is a proposal.

## (a) Read-back

Reconciling **Stripe** to **Northbrook Trading Ltd** for **1–30 September 2025**, in **USD**. Sales are recorded **one entry per payout** (aggregate approach), as you told me. **No reserve** is held, as you told me. The numbers come from **the files you uploaded**.

Not answered at intake, and what I did:

| Input | Treatment |
|---|---|
| Clearing account name | Not typed; the GL file shows **1050 Stripe Clearing**. I use it — please confirm |
| Country / tax jurisdiction | Not given → output-tax and input-tax-on-fees points are raised as questions, not computed |
| Opening Stripe clearing balance (1 Sep) | Not given; the GL detail shows no opening line → **taken as zero and flagged** |
| Stripe balance definition | Stripe "available" vs "pending" not in the export; the 3 Oct payout is treated as **pending at 30 Sep** |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `stripe_payouts_2025-09.csv` | Stripe payout report: payout date, gross, fees, refunds, chargebacks, net. 3 payouts, net 46,569 | Payouts 5 Sep, 19 Sep and **3 Oct 2025** (the last covers 29 Sep activity). No account or entity name; no payout IDs | Yes; each row foots (gross − fees − refunds − chargebacks = net) | Yes — Steps 2, 4, 5 | **Accepted with a limit**: no processor reference to quote in the tie-out |
| `stripe_balance_transactions_2025-09.csv` | Stripe balance transactions: date, type, amount, fee, net. 8 rows (5 charges, 2 refunds, 1 dispute), net 46,569 | 2–29 Sep 2025 | Yes; no transaction IDs or currency column | Yes — Steps 1–3, fee-rate check | **Accepted with a limit**: no IDs, so refunds and the dispute cannot be traced to an original charge |
| `stripe_gl_detail_2025-09.csv` | GL detail for the Stripe-related accounts: 1000 Operating Bank, 4000 Sales Revenue, 1050 Stripe Clearing. 6 lines, debits = credits = 46,569 | Sep 2025 | Yes; no opening balance for 1050 | Yes — book side, Steps 2, 4, 7 | **Accepted with a limit**: clearing opening balance unknown |
| `bank_statement_2025-09.csv` | Bank statement for the operating account, 1–30 Sep 2025: opening 1,246,642, closing 1,219,776; running balance foots | Sep 2025; account not named | Yes | Yes — Step 5 (proof the payouts arrived) | **Accepted** — only the two STRIPE TRANSFER lines are used |
| `stripe_payouts_2025-09_final.csv` | **Not a payout report.** A staff shift rota: employee, week_1…week_4, "nights/days/off" for E08–E10 | No company, dates or amounts | No | No step uses it | **Rejected** on content despite the name. If a later payout export exists, upload that. Not used. |

Still missing: the clearing account name and country typed in chat (required by the checklist; inferred from the GL, please confirm); the 1050 opening balance; Stripe's fee invoice / pricing (for the rate check and any input tax).

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

Processor supplied by export; posting approach declared by you: **one entry per payout**. Payouts tied **to the bank statement** (strongest assurance), not just to recorded deposits. No mock data.

### Gross-to-net decomposition, September (USD)

| Component | Stripe transactions | Stripe payouts (5 Sep + 19 Sep + 3 Oct) | Books |
|---|---:|---:|---:|
| Gross charges (5) | 48,680 | 48,680 | **not recorded** |
| Refunds (2) | (480) | (480) | not recorded |
| Chargebacks / disputes (1) | (200) | (200) | not recorded |
| Processor fees | (1,431) | (1,431) | **not recorded** |
| **Net** | **46,569** | **46,569** | Sales Revenue credited **46,569** |

The Stripe side ties internally to the cent: transactions → payouts (19,720 / 578 fees on 5 Sep; 22,340 / 653 on 19 Sep; 6,620 / 200 on 3 Oct).

### Finding 1 — revenue is recorded net of fees (presentation finding)

Sales Revenue (4000) was credited with **the net payouts, 46,569**, not gross charges of 48,680. Every signal in the net-revenue test is present: revenue equals net payouts to the cent; no merchant-fee account is used (none exists in the posting); refunds and the chargeback are netted inside revenue rather than shown as contra-revenue.

**Estimated gross-up: 2,111** = fees 1,431 + refunds 480 + chargeback 200. Revenue should read 48,680 gross, with 1,431 fee expense and 680 contra-revenue (refunds and chargebacks). **Profit is unaffected**; revenue, expense and margins are not. Tax point: output tax (sales tax / VAT) is normally due on the gross sale, so if sales tax is declared from the revenue account it may be **under-declared**. I cannot size that without your jurisdiction and whether these sales are taxable.

### Finding 2 — the 6,420 at 30 September is in transit, booked to revenue via clearing

The 29 Sep charge of 6,620 (fee 200, net 6,420) was **paid out on 3 October**, after period end. It is correctly absent from the September bank statement. The books recorded it on 30 Sep as DR 1050 Stripe Clearing 6,420 / CR Sales Revenue 6,420 — again **net**, so the gross charge and its 200 fee are missing.

### Clearing account roll-forward — 1050 Stripe Clearing

| | As it should be (gross) | As booked |
|---|---:|---:|
| Opening 1 Sep (not supplied, taken as 0) | 0 | 0 |
| + Gross charges | 48,680 | — |
| − Refunds | (480) | — |
| − Chargebacks | (200) | — |
| − Fees | (1,431) | — |
| + Net in transit booked 30 Sep | — | 6,420 |
| − Payouts received in bank | (40,149) | — (payouts debited bank against revenue, bypassing clearing) |
| **Closing 30 Sep** | **6,420** | **6,420** |
| Stripe balance at 30 Sep (pending, paid 3 Oct) | 6,420 | 6,420 |
| **Difference** | **0.00** | **0.00** |

The closing balance agrees with Stripe's pending balance, but only because both sides are net; the clearing account is used for one line a month, not as a true clearing account. Ageing: the 6,420 is 1 day old at period end and was paid out 4 days after the charge. Normal.

### Payout tie-out

| Payout date | Stripe net | Bank date | Bank amount | Variance | Tied to |
|---|---:|---|---:|---:|---|
| 5 Sep | 18,842 | 5 Sep, STRIPE TRANSFER | 18,842 | 0 | bank statement |
| 19 Sep | 21,307 | 19 Sep, STRIPE TRANSFER | 21,307 | 0 | bank statement |
| 3 Oct | 6,420 | — (after period end) | — | in transit | October statement needed |

No unexplained Stripe deposits on the statement.

### Other checks

| # | Item | Detail | Action |
|---|---|---|---|
| 3 | Effective fee rate | 1,431 / 48,680 = **2.94%**. Per charge 2.92–2.93%, except **29 Sep: 200 / 6,620 = 3.02%** | Check against your Stripe pricing; one charge is out of line |
| 4 | Dispute of 200 on 18 Sep | No dispute fee charged and no link to the original charge (no IDs) | Confirm status (open or lost) and whether Stripe will charge a dispute fee |
| 5 | Refunds 300 (4 Sep) and 180 (17 Sep) | Cannot be traced to original charges without IDs | Export with charge IDs |
| 6 | Charge-to-payout lag | 2–3 days for the first payout charges; 3–7 days for the second; 4 days for the third. Stable | None |

### Proposed correcting entry — proposal only, nothing posted (aggregate approach, September)

Reclassify revenue to gross. Account names from your files where they exist; **no fee, refunds or chargeback account appears in the GL detail**, so those three are placeholders until you confirm the accounts:

| Account | DR | CR |
|---|---:|---:|
| Merchant processing fees (placeholder) | 1,431 | |
| Sales returns / refunds (placeholder) | 480 | |
| Chargebacks (placeholder) | 200 | |
| 4000 Sales Revenue | | 2,111 |

Memo: Stripe September — gross up revenue for fees, refunds and chargebacks netted in payouts; evidenced by Stripe payout report rows 5 Sep, 19 Sep, 3 Oct and balance transactions 2–29 Sep. After this, Sales Revenue from Stripe = 48,680; clearing and bank are unchanged. Going forward, booking each payout as DR Bank (net) + DR Fees + DR Refunds + DR Chargebacks / CR Revenue (gross) via 1050 would keep the clearing account meaningful.

## (d) What was not done, and why

| Task | Status | Gap |
|---|---|---|
| Output tax on gross sales; input tax on fees | Not computed | Country / jurisdiction and taxability |
| Clearing opening balance | Assumed zero | 31 Aug balance of 1050 |
| Stripe "available" vs "pending" definition | Inferred from payout date | Stripe balance report at 30 Sep |
| 3 Oct payout reaching the bank | Not verifiable | October bank statement |
| Refund and dispute traced to original charges | Not run | Transaction IDs |
| Fee rate against contract | Effective rate only | Stripe pricing agreement |
| Multi-currency | Not applicable on the files (single currency assumed; no currency column) | Confirm all charges were USD |
| Posting the reclassification | Not done — read-only | A person posts it |

Would you like the workpaper as `Processor_Recon_Stripe_2025-09.xlsx`? Only on your yes.

**Data sources:** user uploads only — `stripe_payouts_2025-09.csv`, `stripe_balance_transactions_2025-09.csv`, `stripe_gl_detail_2025-09.csv`, `bank_statement_2025-09.csv`. No Mosofin connection used.
