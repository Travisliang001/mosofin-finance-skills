# Year-end close plan: Northbrook Trading Ltd, year ending 31 December 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and works from your
uploads. (Connecting Mosofin would automate the ledger reads: [docs.mosofin.com](https://docs.mosofin.com).)
Nothing has been posted, locked or filed. Every entry below is a proposal.

## Read-back (please confirm)

> Planning the year-end close for **Northbrook Trading Ltd** at **31 December 2025**, under
> **US GAAP**, from **your uploads**, in USD. A **full audit**, fieldwork from **9 February 2026**.
> Events this year: **dividend of 60,000 (March)**, **acquisition of Harlow Fabrication on 1 July**,
> **restructuring approved in October**. Filings in scope: **corporate tax return; information
> returns**. Prior-year auditor point: **bank reconciliations not reviewed monthly**.
> **Materiality: none communicated, and I will not supply one.** Shall I go ahead?

Framework, audit, filings, events and the prior-year point came from `audit_inputs.md`, not from you
in chat; they count as answered once you confirm this read-back. The audit firm is not named: please give it.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable? | Step that uses it | Verdict |
|---|---|---|---|---|---|
| `trial_balance_2024-12-31.csv` | Trial balance, 33 accounts, pre-closing (P&L still open) | No company named; 31 Dec 2024 per name | Foots: Dr 6,433,544 = Cr 6,433,544 | Prior-year TB; Step 5c opening check; restatement comparison | **Accepted with a limit**: company user-asserted; no issued 2024 statements to compare against |
| `journal_entries_2025-09.csv` | Journal listing, 7 entries, 16 lines, Sep 2025 (one dated 31 Aug) | No company named | Each entry balances | Step 1b (month closed, post-close posting) | **Accepted with a limit**: one month of twelve; Steps 1b and 5b cannot cover the year |
| `fixed_asset_register.csv` | Fixed asset register, 8 assets, cost 420,000 | No company named | No accumulated depreciation or disposal columns | Fixed assets year-end block | **Accepted with a limit**: cost ties, NBV cannot be reconciled |
| `audit_inputs.md` | Typed summary of audit, filings, events, owners | Names the 2025 audit | Text | Intake B–F, Step 3, Step 4 | **Accepted with a limit**: user-supplied facts, not evidenced; confirm in the read-back |
| `trial_balance_2025-09-30_v2.csv` | A 4-account balance listing whose bank line is **"Bank — Harlow Fabrication Ltd"** | **Harlow Fabrication Ltd**, not Northbrook; 30 Sep 2025 | Foots (306,000 each side), but only 4 accounts and an "Equity" plug | None for Northbrook | **Rejected**: it is the acquired company's balances, not Northbrook's trial balance. Upload Northbrook's own 30 Sep 2025 TB. If Harlow is in scope as a subsidiary for consolidation, say so and I will accept it for Harlow |

**Still missing (required):** Northbrook's trial balance at 30 Sep 2025 (and at 31 Dec 2025 when it
exists); general ledger detail for Jan–Aug and Oct–Dec 2025, and for Jan 2026 to date; the opening
2025 TB (post-closing). **Recommended:** issued 2024 financial statements; Harlow acquisition
documents (SPA, opening balance sheet, PPA); count instructions; lease, equity and debt schedules;
the materiality figure from the auditor. I would wait for your answer here; this run proceeds on
the four accepted files.

## Findings

**1. Twelve months closed — cannot be verified (Step 1b).** Only September's journal is here.
Within it, **JE-0905 (3,800, legal fee) is dated 31 Aug 2025 but posted 22 Sep 2025**: an entry
posted into August after August's close. Confirm August's reported figures were re-issued or this
is accepted as a late adjustment, and run the same test on all twelve months once the GL arrives.

**2. JE-0904: 50,000 manual revenue adjustment.** Dr AR 1100 / Cr Sales 4000, round amount,
dated 28 Sep (quarter-end week), posted by **a.reyes**, the only entry not by the controller, with
no support in the memo. Revenue posted straight to AR outside invoicing near a period end is a
cutoff and override risk: obtain the invoice/contract, and include it in the auditor's JE testing.

**3. JE-0907: 9,999 with no memo.** Dr Marketing 6200 / Cr Accrued Liabilities 2100, just under a
10,000 round figure, no description. Ask for the support; an undocumented accrual is a JE-testing selection.

**4. Depreciation is run at last year's flat rate.** September's charge (JE-0901) is 4,200 =
50,400 / 12, the 2024 annual charge. On the register, FA-005 Servers (fully depreciated Jan 2025)
and FA-007 Laptops (Aug 2025) have stopped depreciating and FA-008 was sold, so straight-line
monthly depreciation on the remaining five assets is **3,813.69**. Proposed: review the recurring
entry; the overcharge is about **386 a month**. Confirm conventions (salvage, part-month) first.

**5. The register still holds an asset sold in July.** FA-008 "Delivery van (sold Jul 2025)",
cost 12,000, is on the register; register cost 420,000 equals GL cost at 31 Dec 2024, so either
the disposal has not been booked or the register has not been updated. Proposed entry (draft):
Dr Accumulated depreciation 12,000 / Cr Fixed assets cost 12,000, plus proceeds to gain/loss
once the sale amount is known. Also: the register has no accumulated depreciation, so the GL's
273,400 at 31 Dec 2024 cannot be tied (my straight-line recompute gives 211,741; ask for the schedule).

**6. Retained earnings roll (Step 5c target).** The 2024 TB is pre-closing: net income 2024 =
**614,939** (revenue 4,597,600 less expenses 3,982,661). The 2025 opening RE should therefore be
763,715 + 614,939 − 0 = **1,378,654**, and every P&L account should open 2025 at zero. Untested:
the 2025 opening TB was not supplied. At 31 Dec 2025 the roll must also take the **60,000 March dividend** (account 3200).

**7. Event-driven work this year.**
- **Harlow acquisition (1 July):** Harlow's results included from 1 July; opening balance sheet at
  fair value; PPA final by 30 June 2026; any goodwill needs its **annual impairment test** with a
  valuation that has a lead time — book it now. Consolidation basis to decide (entity vs consolidated).
- **Restructuring approved October:** restructuring reserve and its roll-forward at year end.
- **Dividend 60,000:** equity roll-forward and the disclosure.
- **Northbrook UK:** investment 104,800 and intercompany payable 38,000 at 31 Dec 2024; intercompany
  confirmation and the consolidation question apply.

**8. Prior-year point carried forward.** Bank reconciliations not reviewed monthly: have all twelve
2025 reconciliations evidenced as reviewed (signed and dated) before fieldwork; the auditor will test it.

**9. Filings tracker (Sheet 8).** In scope: corporate income tax return (owner S. Patel);
information returns 1099 (S. Patel, due 31 Jan 2026). **Questions:** W-2/W-3 (payroll 842,400 in
2024 suggests they apply), sales tax annual reconciliation (2200 Sales Tax Payable is live),
property tax, any UK filings for Northbrook UK. Due dates and the federal/state split to be confirmed.

**10. Going-concern facts (31 Dec 2024 only).** Cash 803,866; current assets 1,917,083 vs current
liabilities 274,829 (ratio 6.98); term loan 265,000 (maturity not in the books). Facts only; the
assessment is management's. Q3 lender compliance certificate: ask for it and the covenant terms.

## Year-end calendar (outline, owners from your file)

| Task | Owner | By |
|---|---|---|
| Upload remaining 2025 GL and Sep TB; verify months 1–9 closed | S. Patel | Nov 2025 |
| Book goodwill valuation / PPA support for Harlow | S. Patel | Nov 2025 |
| Physical inventory count, 31 Dec | Warehouse manager | 31 Dec 2025 |
| Fixed asset count and disposal clean-up (FA-008) | S. Patel | Dec 2025 |
| 1099s issued | S. Patel | 31 Jan 2026 |
| Ledger-derived PBC assembled | S. Patel | before 9 Feb 2026 |

## Not done, and why

- Twelve-month close check, post-lock check (5b), new-year opening check (5c): needs the full 2025 GL, the 2025 opening TB and Jan 2026 GL.
- Lead-schedule completeness and any materiality-based test: **no materiality given; I will not supply one.**
- Tax provision / ETR true-up: no 2025 TB. Deferred tax attributes are not ledger balances.
- Confirmations, counts, valuations, actuarial items, the cap table, attorney letters, the
  going-concern conclusion, the representation letter, the audit and every filing: a person's.
- Restatement comparison of 2024: needs the issued 2024 statements.
- Harlow: rejected file; nothing about Harlow's balances is used.

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, FY 31 Dec 2025, USD, US GAAP, full audit (firm not named): **user-asserted**. Data source: **upload** (Mosofin not used, by your choice). Files: 4 accepted with limits, 1 rejected (Harlow TB). Months verified closed: **none**. Lock date: none yet. Materiality: **not supplied**. Fixture flag: n/a |
| Capability map | Not applicable: no connection. Every task is `[manual]`. |
| Steps | 1 not done (no TB/GL); 1b done with a limit (Sep only); 2 planned, 15 blocks listed, FA and equity blocks partly done; 3 done (tracker drafted, questions open); 4 planned; 5 drafted (RE target only); 5b not done; 5c not done (target computed); 6 done (carry-forward below); 7 tables in chat (Excel on request) |
| Not done | Tie to 2025 GL totals, roll-forwards, prior-year comparison: need the 2025 TB/GL and the issued 2024 statements |
| Carry-forward | Bank rec review evidence; JE-0904/0905/0907 support; depreciation run-rate; FA-008 disposal; Harlow PPA and impairment; materiality from auditor |

Would you like this as `YearEndClose_2025-12-31_Northbrook Trading Ltd.xlsx`?
