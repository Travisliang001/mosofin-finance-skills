# Segment reporting under ASC 280 — Northbrook Trading Ltd, nine months to 30 September 2025

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been posted, sent or changed. The disclosure text is a draft.

## Read-back

Preparing segment disclosures for **Northbrook Trading Ltd** for the **nine months to 30 September
2025** under **ASC 280**, in **USD**, from **the segment results, P&L and trial balance you
uploaded**. The decision maker is **the CEO**, who reviews **three divisions: Fixings, Packaging and
Services**. Profit measure: **operating profit before central costs**. The CEO also sees **assets by
division** (they are in the segment file; please confirm they are reviewed). Not answered:
**intersegment pricing** (shown as recorded, basis not supplied) and **which other items** the CEO
reviews (only revenue, the profit measure and assets are disclosed). Company and currency are as you
stated; no file names them.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `segment_results_2025.csv` | Revenue, operating profit before central costs and assets for three divisions | No company or dates; revenue totals 4,038,600, equal to Jan–Sep 2025 in the P&L, so nine months to 30 Sep 2025 | Yes. No intersegment column, no depreciation, capex or interest by segment | Steps 1–6 | **Accepted with a limit**: period inferred from the totals; summary figures, not the CEO's reports; intersegment revenue cannot be shown |
| `profit_and_loss_2025_ytd.csv` | Monthly P&L, Jan to Sep 2025 | 2025; company user-asserted | Yes; net income 594,241 | Step 6 (revenue and profit reconciliation) | **Accepted with a limit**: company user-asserted |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 33 accounts | User-asserted | Yes; debits = credits = 6,546,018; revenue 4,038,600 agrees to the P&L | Step 6 (asset reconciliation) | **Accepted with a limit**: holds an investment in Northbrook UK Ltd (104,800), so it is the parent's ledger, not a consolidated one |
| `segment_results_2025_final.csv` | A four-week shift rota for employees E08 to E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**: the name suggests final segment results; the content is a staff rota. Set aside. If final segment figures exist, please upload them |

**Still missing:** the reports the CEO actually reviews (recommended), the prior-year segment note
(recommended, for comparatives), customer-level revenue (for the major-customer test), revenue by
country and long-lived assets by location (entity-wide disclosures), and a breakdown of central
costs. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## Findings

**1. Operating segments.** Three, as the CEO reviews them: Fixings, Packaging, Services. The TB has
no division dimension, so the segment figures come from outside the books and **the reconciliation
does not tie by construction**: it is a real test. No aggregation proposed. For reference, margins on
the profit measure are 23.4%, 20.7% and 18.6%.

**2. Reportable segment tests** (intersegment revenue assumed nil: none recorded)

| Segment | Revenue | % of combined | Profit measure | % of profitable total | Assets | % of combined | Reportable? |
|---|---:|---:|---:|---:|---:|---:|---|
| Fixings | 2,221,230 | 55.0% | 520,000 | 58.4% | 1,400,000 | 56.0% | **Yes** (all three) |
| Packaging | 1,494,282 | 37.0% | 310,000 | 34.8% | 900,000 | 36.0% | **Yes** (all three) |
| Services | 323,088 | **8.0%** | 60,000 | **6.7%** | 200,000 | **8.0%** | **No**: below 10% on every test |
| **Total** | **4,038,600** | | **890,000** | | **2,500,000** | | |

Profit test denominator: all three are profitable, so it is the profitable total, 890,000; there is
no loss side. **75% coverage test** (denominator: external consolidated revenue, 4,038,600): Fixings
+ Packaging = 3,715,512, **92.0%**, so no further segment is needed. **Services goes into "All
Other"**, unless you choose to report it voluntarily.

**3. Reconciliations**

| Revenue | |
|---|---:|
| Fixings + Packaging (reportable) | 3,715,512 |
| All Other (Services) | 323,088 |
| Intersegment eliminations | 0 (none recorded; pricing basis not supplied) |
| **Consolidated revenue (P&L and TB)** | **4,038,600** — agrees |

| Profit | |
|---|---:|
| Segment operating profit before central costs, all segments | 890,000 |
| Central costs not allocated to divisions | **(285,285)** |
| Interest expense | (10,474) |
| **Income before tax (P&L; no tax line in the books)** | **594,241** |

**Central costs of 285,285 are a derived figure, not an explained one.** They are what is left between
the segment total and consolidated operating profit (604,715 = 594,241 + 10,474). ASC 280 needs the
reconciling items itemised; please supply what makes up central costs (HQ payroll, rent, professional
fees and so on). Until then it is one balancing figure and should not be published as such.

| Assets | |
|---|---:|
| Segment assets | 2,500,000 |
| Not allocated to divisions | **213,959** |
| **Total assets per TB (net of allowance and depreciation)** | **2,713,959** |

The unallocated 213,959 needs naming too (likely cash held centrally, the investment in Northbrook UK
Ltd of 104,800, prepaids). And if the 10-Q presents consolidated figures, the asset total will differ.

**4. Entity-wide disclosures** (required even though segments exist)
- **Products and services**: the three divisions give a split (Fixings 2,221,230; Packaging
  1,494,282; Services 323,088) if they are product groupings; please confirm.
- **Geography**: not supplied. Need revenue by country and the attribution basis, and long-lived
  assets by location.
- **Major customers (≥10% of 4,038,600, i.e. ≥ 403,860)**: **not tested**; no customer-level revenue.

**5. Draft note (DRAFT).** "The Company has three operating segments, Fixings, Packaging and Services,
reviewed by the Chief Executive Officer. Fixings and Packaging are reportable; Services is included in
All Other. Segment performance is measured as operating profit before central costs." Figures as in
the tables above, once central costs are itemised.

## What was not done, and why

- **Comparatives (Step 8)**: no prior-year segment figures.
- **Intersegment revenue**: none recorded; basis not supplied.
- **Major customers, geography**: no data.
- **Items beyond revenue, profit measure and assets**: not shown; the CEO's review of them is unconfirmed.
- **Excel workbook**: not created. Do you want `Segment_Reporting_2025_Northbrook Trading Ltd.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, nine months to 30 Sep 2025, USD, ASC 280, user-asserted; source upload; three files accepted with limits, rota rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (CEO's structure); 2 no aggregation; 3 done; 4 your measure; 5 done for three items; 6 done, central costs and unallocated assets **unexplained**; 7 products only, geography and major customers **not done**; 8 **not done** |
| Unknowns | Central costs 285,285; unallocated assets 213,959; intersegment basis; major customers |
| Parameters | 10% thresholds on combined segment figures; 75% on external revenue 4,038,600; intersegment nil |
