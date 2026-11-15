# Derivatives and hedging — Northbrook Trading Ltd, 30 September 2025

This run is manual: no Mosofin connection is present. Everything below comes from the files you uploaded. I have valued nothing, concluded nothing about effectiveness, and posted or changed nothing.

## (a) Read-back

Accounting for **one interest rate swap** with **Calder Bank** at **Northbrook Trading Ltd** (name as you stated it) at **30 September 2025** under **ASC 815**, in **USD**, from **the swap summary, the loan summary and the trial balance you uploaded**. Fair value from **the bank's mark-to-market statement dated 1 October 2025**: a liability of 3,400. Designated, per the file, as a **cash flow hedge of the term loan**, with a designation memo dated **14 February 2025**; the trade date is **1 January 2025**.

Intake answers taken from the files, not from you: the instrument and its terms, the valuation, the designation and its date, the framework. Not answered anywhere:
- **Whether any forecast transaction is no longer expected** — unanswered. Default: amounts in other comprehensive income are reported as **not assessed** on that point.
- **The floating rate index, reset dates and settlement frequency of the swap** — not stated.
- **How effectiveness is to be assessed, and the prior period memo** — not supplied.

What I received:
- `interest_rate_swap.md` — swap terms (notional 200,000, pay fixed 5.2%, receive floating, 1 January 2025 to 31 December 2029), bank valuation, designation memo date, the ledger balances as described, and a note that the term loan is fixed rate.
- `term_loan_agreement_summary.md` — Calder Bank term loan: original principal 580,000, 5,000 a month plus interest, **fixed 5.7%**, matures 31 December 2029, two covenants.
- `trial_balance_2025-09-30.csv` — 29 accounts, debits 6,589,681 = credits 6,589,681.
- `interest_rate_swap_final.csv` — 3 rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `interest_rate_swap.md` | Summary of swap terms, valuation, designation and recorded balances | Valuation is at 30 September 2025. The company is not named in it | Yes. It is a summary, not the confirmation, the bank statement or the memo itself; index and settlement terms absent | Steps 1–5 | **Accepted with a limit**: terms, mark and memo date are as quoted; I cannot check them to the source documents |
| `term_loan_agreement_summary.md` | Summary of the term loan terms and covenants | Lender matches the swap counterparty; no borrower named; no date | Yes for rate, repayment and maturity | Step 2 (the hedged item) and check 2 | **Accepted**. The covenant section is not used by this skill |
| `trial_balance_2025-09-30.csv` | Trial balance | Dated 30 September 2025 in the file name only; no company named | Yes, foots. It has **no derivative account and no other comprehensive income account** | Step 0b checks, Step 3 carrying value | **Accepted with a limit**: balances only, no ledger movements or cash settlements, so two of the three checks cannot be fully run |
| `interest_rate_swap_final.csv` | A four-week staff shift roster (E08–E10) | No company, date, instrument or amount | Not for this skill | No step uses it | **Rejected**. The name suggests a final swap file; the content is a rota. Set aside. If a final confirmation or valuation exists, please upload that |

**Still missing:** the swap confirmation, the bank's valuation statement and the designation memo themselves (required; only quoted in a summary); the effectiveness assessment and prior period memo (required if hedge accounting applies); ledger detail for derivative, other comprehensive income, interest and bank accounts (recommended). I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## (c) Findings

**1. The hedged item is a fixed-rate loan, so there is no variable cash flow for a cash flow hedge to hedge.**
The memo designates a cash flow hedge of the term loan. A cash flow hedge covers variability in future cash flows, for example floating-rate interest. The loan pays a **fixed 5.7%**; its interest does not vary. The swap has the company **paying fixed 5.2% and receiving floating**, which does not offset anything on a fixed-rate loan: it adds a floating receipt and a second fixed payment. On the terms supplied, the designation does not describe a relationship that cash flow hedge accounting can apply to. Hedge accounting is not assumed. Unless there is another floating-rate exposure this swap was meant for, the swap is accounted for as **not designated**, with all changes in fair value in earnings. This is for you and your auditor or technical adviser to conclude; I have not tested or concluded on effectiveness.

**2. The documentation is dated 44 days after the trade.**
Trade date 1 January 2025; designation memo 14 February 2025. Hedge accounting needs documentation at inception and cannot be applied backwards. Even if the relationship in item 1 were valid, hedge accounting is unavailable for 1 January to 14 February 2025, and the fair value movement in that window belongs in earnings. The amount at stake cannot be stated: no valuation at 14 February 2025 was supplied (source needed: Calder Bank or an independent valuer).

**3. The recorded balance is behind the valuation by 500.**

| | Amount |
|---|---:|
| Bank valuation at 30 September 2025 (liability) | 3,400 |
| Derivative liability recorded, per the swap summary | 2,900 |
| **Movement to record (increase in liability)** | **500** |
| Other comprehensive income, debit, as recorded | 2,900 |

The 2,900 is an earlier mark, not a current value. The 3,400 is 1.7% of the 200,000 notional.

**4. The trial balance does not show the derivative or the other comprehensive income balance.**
The swap summary says the ledger carries a derivative liability of 2,900 and an other comprehensive income debit of 2,900. The trial balance at 30 September 2025 has neither account, and it balances without them. Either they sit inside another line (for example Accrued Liabilities 28,800 and Retained Earnings), or they are not in this ledger. Please say which; the entries below depend on it.

**5. The valuation is the counterparty's own mark.**
Calder Bank is the other side of the trade and also the lender. Its statement (discounted cash flow on the bank's curve, dated 1 October 2025) is the only valuation. No independent check and no credit adjustment (the allowance for either party's risk of non-performance) is shown. Reviewing the mark at least approximately is a control you would be expected to operate.

**6. Notional and loan balance differ.** Swap notional 200,000, not stated as amortising; Term Loan per the trial balance 220,000, falling 5,000 a month (580,000 less 72 repayments). Maturities match (31 December 2029). Critical terms therefore do not match, which matters only if a hedge relationship survives item 1.

**Step 0b checks**

| Check | Run? | Result | Action |
|---|---|---|---|
| Settlement completeness | Partly; no cash ledger | Interest Expense is 17,100 for nine months. Fixed 5.7% on the loan balances implied by the repayment schedule (265,000 falling to 225,000 at each month start) is about 10,474. The other 6,626 is unexplained and no swap settlement is identified anywhere | Question: where are the swap's net settlements recorded, and what makes up interest expense? |
| Other comprehensive income reclassification | Not performed; no ledger movement | The 2,900 is not assessed for release. If item 1 stands, none of it belongs there | See proposed entries |
| Documentation timing | Yes | 44-day gap, 1 January to 14 February 2025 | Item 2 |

**Proposed entries at 30 September 2025 — PROPOSALS, NOT POSTED.** Account names are generic; the trial balance has no derivative accounts.

If the swap is treated as not designated (what the supplied terms point to):

| Debit | Credit | Amount | Why |
|---|---|---:|---|
| Loss on derivatives (earnings) | Derivative liability | 500 | Movement from 2,900 recorded to the 3,400 valuation |
| Loss on derivatives (earnings) | Other comprehensive income | 2,900 | Remove the amount held in other comprehensive income |

Effect: derivative liability 3,400; other comprehensive income nil; cumulative loss in earnings 3,400. How much of the 2,900 relates to periods already reported, and whether that is an error correction, is for you and your auditor.

If, instead, you show a valid floating-rate hedged item and hedge accounting from 14 February 2025: the 500 would go to other comprehensive income only to the extent effective, and the movement from 1 January to 14 February 2025 would still go to earnings. Not quantified; inputs missing.

**Disclosure data available:** one pay-fixed interest rate swap, notional 200,000, maturing 31 December 2029, counterparty Calder Bank, fair value liability 3,400 (bank mark).

**Embedded derivatives:** not reviewed. Only a read of the underlying contracts can find them; the loan summary shows no index-linked terms.

## (d) What was not done, and why

- **No valuation** — never computed here. The 3,400 is Calder Bank's mark, unverified.
- **No effectiveness test or conclusion** — never concluded by this skill; and no method, index or hedged-item valuation was supplied.
- **No conclusion that hedge accounting is or is not permitted** — the facts in items 1 and 2 are set out for you and your adviser.
- **Amount for the 1 January to 14 February 2025 window** — no valuation at 14 February 2025.
- **Settlement sweep and other comprehensive income movement check** — no ledger detail or bank transactions; recorded as not fully performed, not as nil exceptions.
- **Location of the 2,900 balances** — not found in the trial balance; unresolved.
- **Whether a forecast transaction is no longer expected** — unanswered; not assessed.
- **Check to source documents** — confirmation, bank statement and memo were not uploaded.
- **Covenant impact** — outside this skill.
- **Excel workpaper** (`Derivatives_Hedging_2025-09_Northbrook Trading Ltd.xlsx`) — not created; say if you want it.
- **Posting, designating, trading** — never done by this skill. Every entry is a proposal for a person to review.

**Data sources:** user-uploaded `interest_rate_swap.md`, `term_loan_agreement_summary.md`, `trial_balance_2025-09-30.csv`. Valuation: Calder Bank statement dated 1 October 2025, as quoted. No ledger read.
