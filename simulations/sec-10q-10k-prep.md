# 10-Q preparation — Northbrook Trading Ltd, Q3 2025 (quarter ended 30 September 2025)

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been filed, submitted, signed, posted or sent. Every schedule is a proposal for your
team; I give no legal view on any disclosure.

## Read-back

Preparing the **Form 10-Q** for **Northbrook Trading Ltd** for **Q3 2025** (quarter and nine months
ended 30 September 2025), in **USD**, an **accelerated filer**, **filing on 7 November 2025**,
earnings release **5 November 2025**, from **the trial balances and P&L you uploaded**. Prior filing:
**the Q2 2025 10-Q, as two quoted figures only**. Non-GAAP: **Adjusted EBITDA** as defined in your
file. Reviewers: controller, FP&A lead, outside counsel; XBRL applies (independent review by the
reporting manager). **Significant events in the quarter: not answered.** Company, period and
currency are as you stated; the form, status, dates, measure and reviewers come from
`filing_inputs.md` and count as answered once you confirm.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `filing_inputs.md` | Form, filer status, dates, two figures quoted from the Q2 10-Q, XBRL facts, Adjusted EBITDA definition, reviewers | Q3 2025; company not named (user-asserted) | Yes | Steps 1, 2, 2b, 4 | **Accepted with a limit**: the prior filing is quoted, not supplied; figures from it are user-supplied, not evidenced |
| `trial_balance_2025-09-30.csv` | Trial balance, 33 accounts; YTD revenue 4,038,600 | No entity or date inside (user-asserted) | Yes. Debits = credits = 6,546,018; every P&L line agrees to the YTD P&L | Step 2 (tie-out reference) | **Accepted with a limit**: company user-asserted; **parent-company ledger, not consolidated** (see finding 1) |
| `profit_and_loss_2025_ytd.csv` | Monthly P&L, Jan to Sep 2025, 12 lines plus net income | 2025, user-asserted company | Yes; YTD net income 594,241 agrees to the TB | Steps 1, 2, 2b (H1 vs filed; Q3 = Jul–Sep) | **Accepted with a limit**: company user-asserted |
| `trial_balance_2025-08-31.csv` | Trial balance at 31 Aug 2025; YTD revenue 3,583,200 = Jan–Aug in the P&L | Yes | Yes; foots at 6,106,903 | Step 1 (preliminary analytics, September movement) | **Accepted with a limit**: not a filing comparative; a 10-Q needs 30 June and 31 December TBs, not 31 August |
| `trial_balance_september.csv` | A trial balance, but **not September 2025**: YTD revenue 3,499,900, retained earnings 763,715, dividends nil, term loan 280,000 (60,000 above 30 Sep 2025, i.e. twelve 5,000 repayments earlier). It is **September 2024** | Wrong period for the one confirmed at intake | Foots (5,363,915) | Could serve only the nine-months-2024 income comparative, which needs your confirmation | **Rejected**: the name suggests the current September TB; the content is a year earlier. Set aside. If it is meant as the 9M 2024 comparative, confirm, and also send 30 June 2024 and 31 December 2024 TBs |

**Still missing:** the Q2 2025 10-Q and the 2024 10-K themselves (required for the comparative check),
the current draft 10-Q (required for the tie-out), TBs at 30 June 2025, 31 December 2024 and for the
comparative 2024 periods, the consolidated figures including Northbrook UK Ltd, the cap table, and the
significant events of the quarter. I would stop here and wait for your answer.

*You replied: go ahead with the accepted files.*

## Findings

**1. The ledger is the parent's, not the group's.** The TB carries *Investment in Northbrook UK Ltd*
104,800 and *Intercompany Payable – Northbrook UK* 38,000. A 10-Q presents consolidated statements,
so every tie-out reference below is **component-level**. A tie-out against these figures would agree
perfectly and still be wrong. Please supply the consolidated TB or the consolidation workpaper.

**2. Comparatives do not match the Q2 filing.** The Q2 10-Q reported six-month revenue of
**2,598,300**. The ledger now shows **2,615,200** for January to June: **16,900 higher (0.65%)**.
Something has been posted into a reported period since it was filed. I have not chosen a figure:
route to `restatement-and-prior-period-adjustment` for the materiality and correction analysis.
Total assets of 2,741,000 at 30 June 2025 could not be compared: no June TB.

**3. Deadline.** Accelerated filer: 10-Q due 40 days after quarter end, 9 November 2025, a Sunday,
so **Monday 10 November 2025**. Your 7 November filing (Friday) leaves one business day of slack;
earnings on Wednesday 5 November. Please confirm filer status was re-tested on public float.

**4. Tie-out schedule (ledger reference computed; component-level; a person performs the tie-out)**

| Line | Q3 2025 (Jul–Sep) | 9M 2025 | Document figure | Agreed / by / date |
|---|---:|---:|---|---|
| Revenue | 1,423,400 | 4,038,600 | Draft not supplied | Open |
| Cost of goods sold | 854,040 | 2,370,856 | | Open |
| Operating expenses (payroll to repairs) | 363,960 | 1,063,029 | | Open |
| Interest expense | 3,277 | 10,474 | | Open |
| Net income | 202,123 | 594,241 | | Open |
| Total assets at 30 Sep 2025 | | 2,713,959 | | Open |
| Shares and EPS | Not verifiable from the ledger: cap table required | | | Open |

**5. Adjusted EBITDA (Regulation G starting point).** Net income + interest + depreciation:
**Q3 218,000; 9M 642,515.** "One-time professional fees" must trace to a ledger amount: the only
candidate is **June 2025, 16,500 against a 2,500 monthly run-rate (14,000 above)**, giving 9M
Adjusted EBITDA of 656,515 if 14,000 is the add-back; Q3 has none. Please name the amount and its
support. With one prior quarter only, I cannot test consistency or recurrence of the add-back.

**6. No income tax line.** The TB has no income tax expense or payable, and the Adjusted EBITDA
definition adds back no tax. For a filer this is a question for the controller: is the provision
booked elsewhere, or not yet booked?

**7. September movement (preliminary analytics).** Marketing 29,146 in September against 19,000 to
20,000 in prior months; cash +98,169, receivables −33,070, inventory −28,461, term loan −5,000.

## Calendar (owners to be named by you; runs back from 7 November)

| Milestone | Owner | Due |
|---|---|---|
| Close complete, comparatives resolved (finding 2) | Controller | Open |
| Draft financials and footnotes | Controller | Open |
| FP&A review of MD&A metrics | FP&A lead | Open |
| Auditor review (mandatory) | External auditor | Before 5 Nov |
| Earnings release | Open | 5 Nov 2025 |
| Legal review | Outside counsel | Open |
| XBRL tagging and independent review (142 tags, 6 extensions last quarter) | Reporting manager | Open |
| Final tie-out and certifications | Open | 6 Nov 2025 |
| File | Open | 7 Nov 2025 (deadline 10 Nov) |

## What was not done, and why

- **Tie-out to the document**: no draft. **Lock test (Step 4b)**: no lock date or posting detail.
- **Comparative columns for 2024** and the 31 December 2024 balance sheet: no TBs or 10-K.
- **Disclosure checklist completeness**: significant events not answered; commitments, contingencies,
  subsequent events and related parties are yours to populate. Segments: no dimension in the TB.
- **DCP certifications, SOX evidence, final read-through**: human acts.
- **Excel workbook**: not created. Do you want `SEC_Filing_Prep_2025-Q3_Northbrook Trading Ltd.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Q3 2025, USD, user-asserted; source upload; **component-level, not consolidated**; four files accepted with limits, September 2024 TB rejected |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1 done (dates from you, owners open); 2 ledger side done, document side **not done**; 2b done for H1 revenue, total assets **not done**; 3 skeleton only; 4b **not done**; 5 human |
| Unknowns | 16,900 H1 revenue difference; consolidation; tax; Adjusted EBITDA add-back; events |
| Parameters | Accelerated filer, 40 days; Q3 = Jul–Sep from monthly P&L; EBITDA per your definition |
