# XBRL tagging checklist — Northbrook Trading Ltd, Q3 2025 Form 10-Q (upload path)

Mosofin is not connected, so this run is manual and works only from the files you uploaded. **Nothing was tagged, validated or filed**, and no element was chosen from memory. What follows is a checklist, a reference schedule from your trial balance and the expected calculation relationships — inputs for your tagger and reviewer, not a tag review.

## Read-back

Preparing the XBRL checklist for the **Q3 2025 Form 10-Q** of **Northbrook Trading Ltd** (accelerated filer; filing 7 Nov 2025, earnings release 5 Nov), on the taxonomy you named, **'US GAAP 2025'**, in **USD**, as at **30 September 2025**. Independent XBRL review by **your reporting manager**; accounting review by the controller, FP&A lead and outside counsel. These facts arrived in `filing_inputs.md` and are used once you confirm them here. **No filing draft was uploaded (question D)**, so per the skill's default this is **the checklist only, with no tag review**. **No validation output (E)**: the validation review is listed as not done. The company is not named in any file; it is user-asserted.

## Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `filing_inputs.md` | Typed summary of the filing facts: form, filer status, dates, prior-filing figures, taxonomy version, prior tag-map **summary** (142 items, 6 extensions), a non-GAAP definition, reviewers | Q3 2025; company not named | Yes as a summary. It is **not** the prior tag map itself and not the draft | Yes: scope, taxonomy (Step 1), comparatives (Step 4), reviewers (Step 5) | **Accepted with a limit**: prior figures and tag-map counts are user-supplied, not evidenced; tag-by-tag consistency cannot be checked |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts: balance sheet at 30 Sep 2025 and YTD P&L (9 months) | Dated 30 Sep 2025; no company or currency | Yes: debits 6,546,018 = credits 6,546,018 | Yes: reference schedule and Step 4b | **Accepted with a limit**: company user-asserted; **single-entity ledger** (holds an investment in and payable to Northbrook UK Ltd), so it is a component-level reference unless the 10-Q is unconsolidated |
| `filing_inputs_final.csv` | **Not filing inputs.** A staff shift rota: employees E08–E10, week_1–week_4, nights/days/off | No company, dates or amounts | No | No step uses it | **Rejected** on content; I use `filing_inputs.md` |

**Still missing (required):** the **filing draft** (statements, notes, MD&A), the **prior tag map** itself (XLSX). Recommended: validation tool output; Northbrook UK Ltd's ledger or the consolidation if the 10-Q is consolidated; the comparative-period ledger; share counts for EPS.

*I would stop here and wait. Assumed answer: "go ahead with the accepted files".*

## Findings

**1. The reference basis does not match a consolidated 10-Q.** The TB carries **Investment in Northbrook UK Ltd 104,800** and **Intercompany payable to Northbrook UK 38,000**. A consolidated filing eliminates both, so every figure from this TB would disagree with the draft and look like a tagging error. Please confirm whether the 10-Q is consolidated; if so, the reference schedule needs the consolidated figures.

**2. Reference schedule — component level, from your TB (ledger values; comparatives not available)**

| Statement line | Value 30 Sep 2025 | Natural balance | Period type | Source accounts |
|---|---:|---|---|---|
| Cash and equivalents | 1,009,899 | Debit | Instant | 1000, 1010, 1050 (Stripe clearing — confirm classification) |
| Accounts receivable, net | 789,360 | Debit | Instant | 1100 less 1150 (allowance 9,000) |
| Inventory | 683,100 | Debit | Instant | 1200 |
| Prepaid expenses | 18,000 | Debit | Instant | 1300 |
| Property and equipment, net | 108,800 | Debit | Instant | 1500 less 1510 |
| Investment in subsidiary | 104,800 | Debit | Instant | 1600 (eliminated if consolidated) |
| **Total assets** | **2,713,959** | | Instant | |
| Current liabilities excl. debt | 338,564 | Credit | Instant | 2000–2300 (incl. 38,000 intercompany) |
| Term loan | 220,000 | Credit | Instant | 2500 |
| Share capital | 250,000 | Credit | Instant | 3000 |
| Retained earnings | 1,905,395 | Credit | Instant | 3100 + YTD net income − 3200 |
| Revenue, 9 months | 4,038,600 | Credit | Duration | 4000 |
| Cost of goods sold, 9 months | 2,370,856 | Debit | Duration | 5000 |
| Operating expenses, 9 months | 1,062,829 | Debit | Duration | 6000–6600 |
| Interest expense, 9 months | 10,474 | Debit | Duration | 7000 |
| **Net income, 9 months** | **594,241** | Credit | Duration | |

No income-tax expense or payable exists in the TB: a 10-Q income statement normally carries a tax line, so confirm whether tax sits outside this ledger.

**3. Comparatives from your prior filing (user-supplied).** Six-month revenue 2,598,300 implies **Q3 revenue 4,038,600 − 2,598,300 = 1,440,300**, the figure the three-month column must carry. Total assets moved from 2,741,000 (30 Jun) to 2,713,959 (−27,041). I cannot test either against the ledger without the Q2 TB, and cannot say whether Q2 was restated; the comparative tagged must be the restated figure if it was.

**4. Expected calculation relationships (Step 4b), for the tagger.**
- Total assets 2,713,959 = liabilities 558,564 + equity 2,155,395. **Holds.**
- Revenue 4,038,600 − COGS 2,370,856 − operating expenses 1,062,829 − interest 10,474 = net income 594,241. **Holds.**
- Retained earnings roll: opening 1,378,654 + net income 594,241 − dividends 67,500 = **1,905,395**. A statement of equity needs these three as separate duration facts.
- Allowance and fixed-asset roll-forwards: openings and movements not in the TB, so not specified.
- These are the ledger's relationships; where the taxonomy's calculation linkbase differs, the taxonomy governs.

**5. Checklist items with nothing to check yet.**
- **Extensions:** prior filing had 6 of 142 items (4.2%). Each must be re-justified against 'US GAAP 2025' and anchored; compare the count once the new tag map exists.
- **Taxonomy:** confirm 'US GAAP 2025' is the version accepted for a November 2025 filing and review the carried tag map for deprecated elements.
- **EPS and share counts:** **requires the cap table**; not derivable here — marked, not blank.
- **Non-GAAP Adjusted EBITDA** (net income + interest + depreciation + one-time professional fees): on the TB, 594,241 + 10,474 + 37,800 = 642,515 before the one-time fees; the one-time amount is not identified in the ledger (YTD fees 36,500). If it appears in the 10-Q, it needs consistent treatment across sections.
- **Sign conventions:** natural balances are in the schedule; expenses are debits and must not be tagged negative.

## What was not done, and why

- Tag review, element selection, dimension tagging and cross-section consistency: no filing draft or tag map.
- Pre-validation, EDGAR error and warning review: no validation output.
- Reviewer sign-off: named (reporting manager), not performed.
- No Excel file created; I would ask before making `XBRL_Tagging_2025-Q3_Northbrook-Trading-Ltd.xlsx`.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, USD — user-asserted; source: upload. Basis: **component-level** (single-entity TB); 10-Q basis unconfirmed. Taxonomy 'US GAAP 2025' (user-stated). Period 30 Sep 2025; comparatives user-supplied, restatement unknown. Reference schedule produced today; re-run before filing. Two files accepted with limits, rota rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 tag map: **not done** (no draft). 2 extensions: **not done**, prior count noted. 3 dimensions: **not done**. 4 checks: reference side done; EPS needs cap table. 4b relationships: done for statement totals and retained earnings; roll-forwards not. 5 validation: **not done** |
| Not done | Comparative tie to the ledger (needs the Q2 and prior-year TBs); consolidation (needs Northbrook UK Ltd figures) |
| Unknowns carried forward | Consolidation basis; income tax; one-time professional fees amount; Stripe clearing classification; restatement status |
| Parameters | Account-to-line mapping as in the schedule; periods: 30 Sep 2025 instant, 9 months YTD duration |
