# Subsequent events review: Northbrook Trading Ltd, balance sheet date 30 September 2025

Mosofin is not connected, so this run is manual and works only from your uploads. (Connecting
Mosofin would let the sweep re-run itself up to issue: [docs.mosofin.com](https://docs.mosofin.com).)
Nothing is posted. Every entry is **PROPOSED — NOT POSTED**, and every classification is yours.

## Read-back (please confirm)

> Reviewing subsequent events for **Northbrook Trading Ltd** from **30 September 2025** to an
> issue date of **20 March 2026**, under **US GAAP (ASC 855)**, from **your uploads**, in USD.
> Testing **every reserve and accrual found** (allowance for doubtful accounts, accrued liabilities,
> inventory, and the legal matters listed at 30 September). **Management's events since the period
> end: not yet given.** Shall I go ahead?

Not answered, with the default applied: **which definition sets the window end** (issued, or
available to be issued) — please confirm, it goes in the disclosure; **estimates that matter most** —
I test every reserve and accrual found; **management's events by category** and **board minutes** —
listed below as not answered / not reviewed. US GAAP is taken from `legal_matters.md`.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Step | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts | No company named; 30 Sep 2025 | Foots: 6,546,018 each side | Period-end balances of the estimates | **Accepted with a limit**: company user-asserted |
| `ar_aging_detail_2025-09-30.csv` | AR ageing by invoice, 14 lines | No company named; at 30 Sep 2025 | Totals 798,360 = TB 1100 exactly | Period-end position per customer (Step 2b) | **Accepted with a limit**: company user-asserted |
| `post_period_ledger_2025-10.csv` | Post-period ledger lines, 6–20 Oct 2025 | No company named | Readable; **only 4 lines for a month** | The sweep (Steps 2, 2b) | **Accepted with a limit**: covers 6–20 Oct only, and 4 entries cannot be the full population for a company billing ~450,000 a month. Window 21 Oct 2025 – 20 Mar 2026 unswept |
| `legal_matters.md` | Management's legal matters list at 30 Sep 2025 | Northbrook context; GC views 28 Sep 2025 | Text | Contingency estimates at the period end | **Accepted with a limit**: management's summary, not counsel's letters; figures user-supplied |
| `post_period_ledger_2025-10_final.csv` | **A staff shift rota** (employee, week_1..week_4) | None | No financial content | None | **Rejected**: despite the name it is not ledger detail. Upload the full post-period ledger instead |

**Still missing (required):** the complete ledger detail from 1 October 2025 to today, and again
just before 20 March 2026; **management's list of known events** (by category, below).
**Recommended:** board minutes since 30 Sep; counsel's updated legal letters. I would wait for your
answer; the sweep below runs on the accepted files only.

## Completeness statement

The transactional sweep covered **4 post-period entries dated 6–20 October 2025**, which is not
the full population. Non-transactional events are covered only by the enquiries recorded below,
and **none has been answered yet**. **The window stays open to 20 March 2026**; re-run the sweep
on the full ledger at the end of each month and the day before issue.

## Ledger sweep detail (Sheet 5): candidates, not conclusions

| # | Pattern | Counterparty | Position at 30 Sep | Post-period item | Date (days after) | Amount | Candidate type |
|---|---|---|---|---|---|---|---|
| 1 | Claim predating period end settled | Customer claim, defective brackets | Probable, estimate 40,000–70,000; total accrued liabilities only 28,800 | Settlement expensed to 6400 | 14 Oct (14) | 52,000 | Recognised candidate |
| 2 | Pre-period receivable written off | Foxhall Garden Centres (administration) | INV-20907, 4,003, 130 days overdue | Write-off against allowance 1150 | 9 Oct (9) | 4,003 | Recognised candidate |
| 3 | Goods returned after period end | PN-55 panels, customer not named | Sale presumably pre-period; invoice not identified | Taken back into stock at cost, credit note issued | 20 Oct (20) | 8,200 at cost | Recognised candidate (revenue and NRV) |
| 4 | Provided-against receivable paid / favourable | Pennine Retail Group | INV-20537, 112,071, 12 days overdue | Paid in full | 6 Oct (6) | 112,071 | Favourable evidence: collectible at 30 Sep |
| 5 | Material balance, no activity since | Harlow Fabrication Ltd | 248,157 (31% of AR): INV-20418 48,200 at 95 days; INV-20977 199,957 due 12 Oct | No receipt by 20 Oct; INV-20977 now past due | — | 248,157 | Collectibility indicator (weaker) |

Also open with no post-period receipt: Tideswell Hotels 48,031 (67 days), Ridgeway Logistics
72,046 (41 days). Calder Print has an unapplied pre-period credit memo CM-0312 (−2,150).

## What each candidate needs (Step 3 is yours)

**1. Defective-brackets claim (52,000).** The claim existed at 30 September and management judged it
probable at 40,000–70,000, so the settlement is evidence of the amount of an existing liability.
Accrued liabilities in total are only 28,800, below even the low end (40,000), and the settlement
was expensed in October rather than charged against an accrual, so the claim appears **not accrued**.
Proposed (if you classify it recognised): **Dr Claims/legal expense 52,000 / Cr Accrued liabilities
52,000 at 30 Sep 2025**, with October's 52,000 then recorded against the accrual. The product
liability policy (10,000 deductible) may give a recovery of up to 42,000: a separate asset only if
recovery is probable, never netted. Confirm with the insurer.

**2. Foxhall write-off (4,003).** Nine days after the period end, on an invoice already 130 days
overdue: proximity suggests the condition existed at 30 Sep (evidence, not proof). It is within the
allowance, but the allowance falls from 9,000 to **4,997** against Harlow's 48,200 at 95 days
and Tideswell's 48,031 at 67 days. When did Foxhall enter administration?

**3. PN-55 returns (8,200 at cost).** Which customer, which invoice, at what selling price, and why
returned? If the goods were faulty or the sale not complete at 30 Sep, reverse the revenue and
margin at 30 Sep and test the returned stock for write-down to NRV. Credit note amount needed.

**4. Pennine receipt (112,071).** Favourable: confirms the receivable at 30 Sep. No adjustment.

**5. Harlow (248,157).** The largest exposure, partly 95 days overdue, nothing received since.
Ask for Harlow's status and any correspondence; this drives the allowance.

**Legal, not swept:** former employee claim (reasonably possible, up to 25,000) — disclosure
candidate at 30 Sep, not an accrual; supplier counterclaim (remote) — nothing. I do not draft the
disclosure of a legal matter: counsel and management do.

## Management enquiry, by category (not yet answered)

Litigation · customers (insolvencies, losses, disputes — **Harlow in particular**) · financing ·
ownership · assets (fire, flood, theft, impairment) · acquisitions or disposals · regulatory ·
directors and key people · significant commitments and guarantees · **dividends declared after 30 Sep**.

## Subsequent events log (Sheet 1)

| Event | Event date | Posting date | Source | Category | Impact | Disclosure |
|---|---|---|---|---|---|---|
| Claim settled | 14 Oct 2025 | not given | ledger sweep | *(preparer)* | 52,000, less any amount already accrued (not identifiable) | *(preparer)* |
| Foxhall in administration, write-off | 9 Oct 2025 (admin date unknown) | not given | ledger sweep | *(preparer)* | 4,003 | *(preparer)* |
| PN-55 return | 20 Oct 2025 | not given | ledger sweep | *(preparer)* | 8,200 cost; revenue unknown | *(preparer)* |
| Pennine paid | 6 Oct 2025 | not given | ledger sweep | *(preparer)* | none | *(preparer)* |
| Harlow silent | — | — | ledger sweep | *(preparer)* | up to 248,157 exposure | *(preparer)* |

The ledger file has one date per line, so event and posting dates cannot be separated.

## Not done, and why

- Sweep of 21 Oct 2025 – 20 Mar 2026: no ledger; the window is open.
- Board minutes, legal letter updates, management enquiry: not supplied.
- Classification, materiality, disclosure wording, posting: yours.
- Inventory NRV beyond the PN-55 return: no post-period sales data.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD, US GAAP: **user-asserted**. Data source **upload** (Mosofin not used). Window 30 Sep 2025 – 20 Mar 2026; definition **not confirmed**. Sweep run once, on 6–20 Oct 2025 only; **final run not done**. Files: 4 accepted with limits, 1 rejected (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done with a limit (definition open); 2: transactions done with a limit (partial ledger), receipts/payments done with a limit, minutes **not done**, legal updates **not done**, enquiry **not answered**; 2b done; 3 left to you; 4 proposed entry drafted; 5 log drafted |
| Unknowns | 5 candidates unclassified; 21 Oct – 20 Mar unswept; all ten enquiry categories open; Harlow's status |
| Parameters | Patterns: settlement, write-off, return, receipt against period-end AR, silent balance; accounts 1100, 1150, 1200, 2100, 6400 |

Would you like this as `Subsequent_Events_2025-09-30_Northbrook Trading Ltd.xlsx`?
