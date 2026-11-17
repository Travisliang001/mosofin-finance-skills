# Audit preparation and PBC list — Northbrook Trading Ltd, readiness at 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, on the files you uploaded. (Connecting Mosofin would let the skill produce the ledger schedules itself — docs.mosofin.com. Not raised again.)

## (a) Read-back

- **Entity:** Northbrook Trading Ltd (user-asserted). **Currency:** USD. **Data source:** upload only.
- **From your `audit_inputs.md` (please confirm):** **full audit** of the year to **31 December 2025**, US GAAP. **Fieldwork starts 9 February 2026.** Figures still moving. **No materiality communicated** — areas are ranked by balance size only; no figure is supplied. Owners: **S. Patel (controller)** for all areas, **warehouse manager** for inventory.
- **This run** is a readiness check as at **30 September 2025** (your intake period), on the interim trial balance, with 31 Dec 2024 as the comparative. Year-end schedules will need re-running on the final TB.
- **The auditor's request list (8 items, A1-A8) governs.** It is mapped below in their wording; nothing is renamed. Items beyond it are listed separately as likely follow-ups.

## (b) Validation of the uploaded files (before any work)

| File | What it actually is | Right company / period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2025-09-30.csv` | Trial balance, 29 accounts | No entity in file; date only in file name | Foots: 6,589,681 = 6,589,681 | Steps 1, 3, 4 (scoping, tie-outs) | **Accepted with a limit:** company and period user-asserted; interim, not year-end |
| `trial_balance_2024-12-31.csv` | Trial balance, same 29-account chart | No entity in file | Foots: 6,459,050 = 6,459,050 | Steps 3, 7 (roll-forwards, prior-year comparison) | **Accepted with a limit:** company user-asserted |
| `auditor_request_list.csv` | Auditor's PBC requests A1-A8 by area | No entity or date in file | Yes | Step 2 (governs the list) | **Accepted with a limit:** 8 high-level requests; follow-ups expected |
| `audit_inputs.md` | Engagement facts, owners, 2025 events, prior-year point | Names year to 31 Dec 2025 | Yes | Intake B-F, Steps 5-7 | **Accepted with a limit:** a summary, user-supplied; used once you confirm the read-back |
| `trial_balance_2025-09-30_v2.csv` | Trial balance of **a different company**: 4 accounts, bank account named "**Bank — Harlow Fabrication Ltd**", foots 306,000 | **Names Harlow Fabrication Ltd, not Northbrook Trading** | — | Not for this entity's list | **Rejected:** it is Harlow's TB, not a second version of Northbrook's. If this is a **group audit** including Harlow (acquired 1 July), tell me and I will scope Harlow as a separate component |

**Still missing:** prior-year PBC list, audit adjustments and the management letter (only one point given); A/R and A/P agings; customer sales listing (to identify the ten largest customers for A8); whether the audit is of Northbrook alone or the group with Harlow; a reviewer other than S. Patel.

I would stop here and wait for your answer. *(Assumed answer: "go ahead with the accepted files".)*

## (c) Findings

### Issues to resolve before fieldwork (self-identified likely adjustments)

1. **The March dividend of 60,000 is not in the books.** Retained earnings at 30 Sep 2025 = 1,422,317 = 789,221 (31 Dec 2024) + 633,096 (2024 profit). If the dividend were recorded it would be 1,362,317. No dividends or distribution account exists. Either it was not booked, or booked somewhere unexpected. Board approval (A7) and the payment are needed.
2. **The Harlow Fabrication acquisition (1 July 2025) is not visible in Northbrook's trial balance.** No investment, goodwill, consideration payable or new debt; fixed-asset cost is unchanged at 420,000. Purchase agreement, consideration paid and an ASC 805 business-combination analysis will be requested even though A1-A8 do not mention it. Professional fees YTD 36,500 already exceed all of 2024 (30,000): check for deal costs.
3. **Restructuring approved in October 2025**: a post-30-Sep event; any liability and its timing need a memo for year-end (contingencies / subsequent events).
4. **Nine balances have not moved since 31 Dec 2024**: petty cash 500, Stripe clearing 6,420, allowance 9,000, prepaids 18,000, corporate card 7,300, payroll clearing 1,200, payroll tax 5,400, sales tax 2,600, intercompany payable to Northbrook UK 38,000. Identical balances nine months on suggest these accounts are not being reconciled — together with the prior-year point (bank reconciliations not reviewed monthly), a close weakness to fix now.
5. **Allowance for doubtful accounts is 9,000, unchanged, while A/R grew 602,143 → 798,360 (+196,217, +32.6%).** The allowance memo will be challenged.

### PBC tracker — auditor's list (governs)

| Ref | Auditor's request | Owner | Source | Readiness now | Tie / roll-forward from the TBs | Gap |
|---|---|---|---|---|---|---|
| A1 | Bank statements and reconciliations for all accounts at year end | S. Patel | manual | Not started | 1000 = 1,230,316 at 30 Sep; Stripe clearing and petty cash static | Statements; monthly reviewed recs (PY point) |
| A2 | Ageing by customer and subsequent receipts | S. Patel | manual | Not started | Control 1100 = 798,360 | Aging not uploaded; subsequent receipts are Jan 2026 |
| A3 | Count sheets and costing support | Warehouse manager | manual | Not started | 1200 = 683,100 (+187,946 YTD) | Year-end count to be planned; costing method |
| A4 | Register, additions and disposals with invoices | S. Patel | manual | Partly ready | Cost 420,000 → 420,000 (no additions/disposals); acc. dep. 273,400 + 37,800 = 311,200 **ties** | Asset register; confirm truly nil additions given Harlow |
| A5 | Ageing and unrecorded liabilities search | S. Patel | manual | Not started | Control 2000 = 255,264 | Aging; post-year-end bills (Jan-Feb 2026) |
| A6 | Loan agreement and covenant compliance certificates | S. Patel | manual | Partly ready | 265,000 − 9 x 5,000 = 220,000 **ties**; interest 17,100 YTD | Agreement; Q3 lender certificate |
| A7 | Board minutes and dividend approvals | S. Patel | manual | **Gap** | Share capital 250,000 unchanged; RE roll-forward excludes the 60,000 dividend | Minutes; dividend booking (finding 1) |
| A8 | Contracts for the ten largest customers | S. Patel | manual | Not started | Revenue 4,038,600 YTD | Customer sales listing to pick the ten |

### Likely follow-ups beyond the auditor's list

Business combination (Harlow) — purchase agreement, ASC 805 analysis; related parties — Northbrook UK intercompany 38,000 and a related-party listing (not a vendor list); accrued liabilities 28,800 support; prepaids 18,000 schedule; payroll liabilities; tax provision, corporate return and information returns; restructuring memo; allowance and inventory-obsolescence memos.

### Areas ranked by balance (no materiality given)

Revenue 4,038,600 · Cash 1,230,316 · Receivables 798,360 · Inventory 683,100 · Payables 255,264 · Debt 220,000 · Fixed assets (net) 108,800. Low-balance, high-attention: **Harlow acquisition, dividend, related parties, restructuring**.

### Timeline (working back from fieldwork 9 Feb 2026 — proposed dates)

Plan year-end count by 15 Dec 2025 → final TB and bank reconciliations 16 Jan 2026 → agings, tie-outs, roll-forwards 23 Jan → documents (minutes, loan agreement, contracts, Harlow agreement) 30 Jan → independent review 2-5 Feb → deliver 6 Feb.

**Readiness:** 0 of 8 auditor items ready; 2 partly ready (A4, A6 roll-forwards tie). All 8 need a human document; none can be produced unaided from the uploads.

## (d) What was not done, and why

- **Subledger-to-GL tie-outs** (A2, A5): no agings uploaded.
- **Prior-year adjustments and management letter** follow-up: only one point supplied.
- **Group scoping for Harlow**: its TB was rejected as a different company pending your answer.
- **Review step**: S. Patel owns every non-inventory item, so no independent reviewer exists — please name one.
- **Excel tracker** `Audit_Prep_PBC_2025_Northbrook Trading Ltd.xlsx`: not created — say yes if you want it.
- **Nothing was posted, sent to the auditor or changed.** Every schedule and adjustment above is for your review.

## (e) Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, FY2025 audit, readiness at 30 Sep 2025, USD — user-asserted. Source: upload. 4 files accepted with a limit; `trial_balance_2025-09-30_v2.csv` rejected (Harlow Fabrication's TB) |
| Capability map | Not applicable: no connection. Every item is `[manual]` |
| Steps | 0 done (uploads); 1 done (balance-size ranking only); 2 done (auditor list governs + follow-ups); 3 done with a limit (two roll-forwards tie; no agings); 4 done; 5 done (proposed dates); 6 listed; 7 done with a limit (5 issues; PY letter incomplete); 8 tables in chat |
| Not done | A/R and A/P subledger ties (agings); PY adjustments (PY letter and adjustment list); Harlow component (group decision) |

**Data sources:** user uploads — `trial_balance_2025-09-30.csv`, `trial_balance_2024-12-31.csv`, `auditor_request_list.csv`, `audit_inputs.md`.
