# IPO readiness roadmap — Northbrook Trading Ltd, baseline at September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would let the skill measure close speed from posting dates itself — docs.mosofin.com. Not raised again.) **This is a finance roadmap, not legal, securities or listing advice**; every filing requirement below is to be confirmed with counsel and the auditors.

## (a) Read-back

- **Company:** Northbrook Trading Ltd (user-asserted). **Period:** baseline as at 30 September 2025. **Currency:** USD. **Data source:** upload only.
- **From `ipo_readiness_inputs.md` (please confirm):** target **listing in 18 months** (about March 2027); **registrant: the current parent**; **no reorganisation planned** — the current structure is assessed on that basis. **Audits:** 2023 and 2024 audited; **2022 not audited**; audit standard (private-company vs PCAOB) not stated. **Equity:** cap table uploaded, one 2025 grant with an independent valuation. **Systems:** one accounting system, **spreadsheets for revenue schedules**. **No control assessment has been done.**
- Files received: `close_calendar.csv` (6 monthly closes, April–September 2025), `cap_table.csv` (3 holders/classes, 2025 movement), `ipo_readiness_inputs.md` (facts above), `close_calendar_final.csv` (see validation).

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `close_calendar.csv` | Close log: 6 months, close date, working days to close, manual vs total journals, reopened flag | No entity named; Apr–Sep 2025 | Yes; close dates, journal counts and flags all present | Steps 0b, 1, 2, 5 (close speed, manual-entry profile, period integrity) | **Accepted with a limit:** company user-asserted; a summary log, not posting-date detail, so the 50/80/100% posting distribution and the last adjusting entry cannot be measured |
| `cap_table.csv` | Cap table: Founders 800,000 and Investor A 200,000 common; option pool 60,000 → 80,000 | No entity named; 2025 movement | Yes | Step 4 (equity and EPS) | **Accepted with a limit:** company user-asserted; the 60,000 opening options have no grant history (dates, strikes, vesting, fair values) |
| `ipo_readiness_inputs.md` | Intake facts: timeline, registrant, reorganisation, audits, equity, systems | No entity named; current | Yes | Stage 1 B–F; Steps 1, 4, 5 | **Accepted with a limit:** user-supplied summary; every fact from it is labelled user-supplied, not evidenced |
| `close_calendar_final.csv` | **An employee shift roster** (E08–E10, weeks 1–4, nights/days/off) — not a close calendar despite the name | No company, no period | Not a finance document | No step uses it | **Rejected:** it holds no close dates or journals. If a later close calendar exists, upload that instead |

**Still missing (required):** **financial statements for the years to be presented** — the checklist marks them required; without them the comparable-data check, the memo-library scoping from the accounts, reconciliation hygiene and the complex-instrument scan cannot run. **Recommended and missing:** control assessment (you say none exists) and a systems list; grant history for the 60,000 opening options; the auditors' standard for 2023–2024.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Measured baseline (from your close log — method: close date vs month end, six months)

| Month | Closed on | Working days | Manual / total journals | Manual share | Reopened |
|---|---|---|---|---|---|
| Apr 2025 | 14 May | 10 | 41 / 58 | 70.7% | no |
| May 2025 | 13 Jun | 10 | 39 / 55 | 70.9% | no |
| **Jun 2025 (Q2 end)** | 16 Jul | **12** | 47 / 61 | **77.0%** | **yes** |
| Jul 2025 | 13 Aug | 9 | 40 / 57 | 70.2% | no |
| **Aug 2025** | 12 Sep | 9 | 38 / 54 | 70.4% | **yes** |
| **Sep 2025 (Q3 end)** | 14 Oct | 10 | 42 / 60 | 70.0% | no |
| **Six months** | | **avg 10.0 (9–12)** | **247 / 345** | **71.6%** | **2 of 6** |

1. **Close speed: ~10 working days, slowest at the June quarter end (12).** Weekday counts tie to your stated days except: August is 10 weekdays (you show 9, consistent with Labor Day 1 Sep excluded), and June's 12 counts 4 July as a working day. Holiday basis is inconsistent by one day; it does not change the conclusion. The target close day is yours and the auditors' to set; the gap is "close completes on working day 10–12 against the target you set".
2. **The close is carried by manual journals: 247 of 345 (71.6%) by count**, steady at 70–77% every month (value split not supplied). Each recurring manual journal becomes an ICFR control with a preparer, reviewer and evidence — **about 40 a month is the approximate size of the SOX workstream**, before revenue spreadsheets.
3. **Closed periods were reopened twice in six months (June and August).** An audit-readiness signal: a company that adjusts reported history is not ready to file it. The reopening entries, who approved them and why are needed.
4. **Audit status is the likely binding constraint.** 2023 and 2024 are audited, **2022 is not**, and **2025 and 2026 are not yet audited**. With a listing around March 2027, which years must be presented depends on filer status (for example whether emerging-growth relief applies) — **not settled here; confirm with counsel.** If the filing needs only the latest two years, 2022 does not matter but 2025 (and possibly 2026) audits are on the critical path; if three years, 2024 may be included. **If 2023–2024 were private-company (AICPA) audits, they may need re-auditing under PCAOB standards** — critical path, `[manual]` to establish.
5. **Equity and EPS — start this workstream first (the most common cause of IPO delay).**
   - Shares: **1,000,000 common** (Founders 800,000; Investor A 200,000), unchanged in 2025. Options **80,000** (60,000 opening + 20,000 granted 1 Apr 2025) = **8.0% of common, 7.4% fully diluted** (80,000 / 1,080,000).
   - **2025 grant stock compensation (user-supplied figures):** 20,000 × 1.10 = **22,000 total fair value**, 4-year monthly vesting = **458.33 a month**; **6 months to 30 Sep 2025 = 2,750 expense** (straight line, before forfeitures). Whether it is booked cannot be checked: no financial statements.
   - The 60,000 opening options have **no grant history**: their expense, vesting and any cheap-stock exposure are not assessable. The 2025 grant was priced at a strike of 2.50 against a valuation dated 15 Mar 2025; the valuation's common-share value is not given, so whether the strike was at or above fair value is unverified. Grants close to an IPO are routinely examined — 409A support is `[manual]`.
   - **Diluted EPS model:** weighted shares 1,000,000; the 80,000 options are dilutive only above strike under the treasury-stock method, which needs an average share price — not supplied. Preferred stock, convertibles or warrants: none in the cap table; the balance sheet could not be scanned to confirm.
6. **Controls: no control assessment exists; revenue runs on spreadsheets.** The ICFR programme starts from zero: key processes, narratives, walkthroughs. Revenue spreadsheets need end-user-computing controls. Segregation of duties cannot be observed from uploads.
7. **Memo library — scoped only partly.** **Live from the uploads:** revenue recognition (spreadsheet schedules) and stock compensation (2025 grant). **Leases, business combinations, income taxes, debt and derivatives: not scoped** — needs the financial statements; none is ruled out.

### Close acceleration plan (sequenced by what holds the close open)

The log cannot show the last adjusting entry, so the account holding the close open is unknown; **June's 12 days and both reopenings point at quarter-end and adjusting work first.** (1) Investigate the June and August reopenings; (2) catalogue the ~40 monthly manual journals and automate the recurring ones only if they sit on the critical path; (3) reconciliation standard and cut-off test — needs the ledger; (4) bring revenue schedules under control; (5) **close calendar and RACI** — the primary deliverable, owner: Controller.

### Roadmap (from September 2025, listing ~March 2027 — proposed, owners by role)

| Workstream | Gap (size and basis) | First deliverable | Owner |
|---|---|---|---|
| Equity and EPS | 60,000 options with no history; no EPS model | Validated cap table + grant register; 409A file | CFO + counsel |
| Audit / PCAOB | 2025–2026 unaudited; 2023–24 standard unknown; 2022 unaudited | Years-required memo; auditor engagement | CFO + auditors |
| Close speed | 10.0 days avg, 12 at Q2; 2 reopenings | Close calendar + RACI | Controller |
| ICFR / SOX | No assessment; ~41 manual JEs/month (71.6%) | Process inventory, risk assessment | Controller / SOX lead |
| Memos | Revenue, stock comp live; four areas unscoped | Revenue and stock-comp memos | Technical accounting |
| Reporting | No disclosure checklist or certification flow | Disclosure checklist; review workflow (officer certification is personal) | CFO |

## (d) What was not done, and why

- **Posting-date distribution (50/80/100%) and last adjusting entry:** the close log has no journal-level dates. Upload a journal listing with posting dates.
- **Comparable-data depth, period-integrity tie of comparatives, suspense balances, complex-instrument scan, memo scoping for four areas:** no financial statements. Upload statements for 2022–2025.
- **Manual-entry share by value:** counts only.
- **`close_calendar_final.csv`:** rejected (a shift roster); not used.
- **Excel workpaper** `IPO_Readiness_2025-09_Northbrook Trading Ltd.xlsx`: not created — say yes if you want it.
- **Nothing was posted, filed, changed or remediated.** Nothing is saved; an IPO plan is material non-public information.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, baseline 30 Sep 2025, USD — user-asserted. Source: upload (no Mosofin connection). 3 files accepted with a limit; `close_calendar_final.csv` rejected (shift roster) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 0 done with a limit (uploads; no statements); 0b done with a limit (close days, manual count, reopenings — no posting distribution, depth or hygiene); 1 done with a limit; 2 done with a limit; 3 partly (2 of 6 areas scoped); 4 done with a limit (2025 grant only); 5 done (sized; no assessment exists); 6 listed; 7 tables in chat; 8 not offered until results approved |
| Not done | Comparable-data depth, comparatives tie, suspense ages, instrument scan (financial statements); posting-date distribution (journal listing); 409A support and opening-option history (grant register) |

**Data sources:** user uploads — `close_calendar.csv`, `cap_table.csv`, `ipo_readiness_inputs.md` (all user-supplied, not evidenced).
