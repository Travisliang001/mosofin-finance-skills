# Share-based compensation (ASC 718) — Northbrook Trading Ltd — to 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would read the expense and equity accounts directly ([docs.mosofin.com](https://docs.mosofin.com)). **Every entry below is a proposal for a person to post; nothing has been posted.** Fair values are yours; none was computed here.

## Read-back

Share-based pay at **Northbrook Trading Ltd** (issuer and employer, user-asserted) for the period to **30 September 2025** (2025 year to date, September month shown separately), **USD**, under **ASC 718**. Awards **equity-settled**, **service vesting**, forfeitures **as they occur** (your answers). From the cap table (facts that arrived inside a file; used once you confirm them here): **20,000 options granted 1 April 2025, strike 2.50, vesting monthly over 4 years, grant-date fair value 1.10 per option from an independent valuation dated 15 March 2025.** Modifications, cancellations and exercises: none reported, **assumed none** (the skill's default for question F). **Attribution method not stated** — see below. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `cap_table.csv` | Cap table summary, 3 rows: Founders 800,000 common, Investor A 200,000 common, option pool 60,000 → 80,000 (+20,000 granted 2025), with the 2025 grant's terms and fair value in a note | No entity or currency named; 2025 movement | Yes for the 2025 grant. **The 60,000 opening options have no grant dates, strikes, vesting terms or fair values** | Steps 1–8 | **Accepted with a limit**: company user-asserted; a summary, not a grant-level award register; **opening 60,000 options cannot be scheduled** |
| `trial_balance_2025-09-30.csv` | Trial balance at 30 Sep 2025, 29 accounts, debits = credits = 6,589,681 | No entity or currency named | Yes. **No stock-compensation expense account and no additional paid-in capital (APIC) account**; Share Capital 250,000 | Step 0b (recorded vs schedule), Step 6 accounts | **Accepted with a limit**: company user-asserted; TB only, no ledger detail |
| `cap_table_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4). Not a cap table, despite its name | None | n/a | No step uses it | **Rejected.** If a later cap table or award register exists, upload it instead |

**Still missing:** a **grant-level award register** for the **60,000 options outstanding at 1 January 2025** (grant date, strike, vesting, fair value with source and date) — **blocking for those awards** (question D); the **attribution method** you elect (straight-line or graded); the **recipients and their departments** for the functional split; the **ledger** for any SBC posted elsewhere. Would wait here; proceeding on the 2025 grant.

## Classification and vesting (Steps 1–5)

| Award | Settlement | Condition | Fair value | Source / date | Total cost |
|---|---|---|---:|---|---:|
| 2025 grant, 20,000 options, strike 2.50 | Equity-settled (your answer) — TB shows no SBC liability, consistent | Service, monthly over 48 months from 1 Apr 2025 | 1.10 | Independent valuation, 15 Mar 2025 — 17 days before grant, **not stale** | **22,000** |
| Opening pool, 60,000 options | Not known | Not known | **Not supplied** | — | **Not computed** |

Forfeitures as they occur: none reported, so no reversal. No performance or market condition.

## Expense schedule — 2025 grant

Monthly vesting is **graded vesting** (48 tranches). US GAAP lets you elect **straight-line** for a service-only award, or attribute **each tranche over its own period** (accelerated). You have not said which, and it changes every period's charge, so both are shown:

| | Straight-line | Graded (accelerated) |
|---|---:|---:|
| September 2025 | 458.33 | 997.09 |
| Q3 (Jul – Sep 2025) | 1,375.00 | 3,289.18 |
| **Cumulative 1 Apr – 30 Sep 2025** | **2,750.00** | **8,274.19** |
| Unrecognised at 30 Sep 2025 | 19,250.00 | 13,725.81 |
| Remaining period | 42 months (3.5 years) | 42 months, weighted to the near term |

Straight-line: 22,000 ÷ 48 = 458.33 a month × 6 months. Graded: each tranche of 416.67 options (458.33 of cost) expensed over its own 1 – 48 months.

## Recorded vs schedule (Step 0b)

| Check | Per schedule | Per books | Difference |
|---|---:|---:|---|
| SBC expense, 2025 to date | 2,750.00 (SL) / 8,274.19 (graded) | **0 — no SBC account on the TB** | **Unrecorded: 2,750.00 or 8,274.19** |
| Cumulative expense vs APIC movement | same | **No APIC account** | Equity credit never booked |
| Exercise cash vs exercises | 0 exercises | Not testable (no ledger) | Not performed |

**No share-based compensation has been recorded for 2025**, and nothing for the 60,000 earlier options appears either (no APIC at all), so prior-period expense may also be missing — not quantifiable without their terms.

## Proposed entry (proposal — Mosofin does not post)

```
DR  [Stock-based compensation expense — account not in your TB]   2,750.00  (graded: 8,274.19)
    CR  [Additional paid-in capital — account not in your TB]          2,750.00  (graded: 8,274.19)
Memo: ASC 718 — options granted 1 Apr 2025 — expense 1 Apr – 30 Sep 2025
```

Your chart has no SBC expense or APIC account; I have not invented names — please name them. Functional allocation (COGS / S&M / G&A) needs the recipients' departments.

## Award roll-forward and disclosures (Step 8)

| Options | Number | Weighted-avg exercise price |
|---|---:|---:|
| Outstanding 1 Jan 2025 | 60,000 | **not supplied** |
| Granted | 20,000 | 2.50 |
| Exercised / forfeited / expired | 0 / 0 / 0 (none reported) | — |
| **Outstanding 30 Sep 2025** | **80,000** | not computable |
| of which vested, 2025 grant | 2,500 (6/48 × 20,000) | 2.50 |

Disclosure inputs still needed: valuation assumptions (volatility, expected term, risk-free rate, dividend yield), terms of the opening 60,000, remaining contractual terms. Hand-offs: the APIC movement to `statement-of-equity-changes`; the non-cash add-back to the cash flow statement; the book-tax difference to the tax provision. **SBC is not an add-back in a quality-of-earnings bridge.**

## Coverage sheet (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, to 30 Sep 2025, USD — **user-asserted**; ASC 718. Data source: **upload**. Cap table and TB accepted with limits; `cap_table_final.csv` **rejected** (shift rota) |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Step 0b | Done with a limit: expense and APIC compared to TB (nil); exercise cash not performed |
| Steps 1–5 | Done for the 2025 grant; **not done** for the opening 60,000 (no terms or values) |
| Step 6 | Done under both attribution methods; accounts and functional split open |
| Step 7 | Not applicable: no exercises or modifications reported |
| Step 8 | Done with a limit: weighted averages incomplete |
| Not done | Opening awards, prior-period expense, ledger tie, department split |

Nothing was posted. **Data sources:** upload — `cap_table.csv`, `trial_balance_2025-09-30.csv`.
