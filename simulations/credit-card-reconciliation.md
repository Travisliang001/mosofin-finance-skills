# Corporate card reconciliation — Northbrook Trading Ltd — September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]` and every figure comes from your uploads. Connecting Mosofin would let the posted card charges and the card liability balance be read from the books ([docs.mosofin.com](https://docs.mosofin.com)).

**What this is:** a statement supplied, so this is a **reconciliation of the statement's charge listing to the card ledger listing** — not a full tie of closing balances, because neither file carries an opening or closing balance (see limits).

## Read-back

Reconciling the corporate card for **Northbrook Trading Ltd** (user-asserted) for **September 2025**, statement and accounting period both 1–30 Sep 2025 (assumed to coincide), currency **USD** (user-asserted; no file states a currency), from your uploads. **Receipt threshold: 25** — taken from `expense_policy.md` (a fact that arrived inside a file; used once you confirm it here), with meals capped at 75 per person and hotels at 250 per night. Not answered, so not applied: **cardholder** (unknown), **capitalisation threshold** (never defaulted — capital test not run), **tax jurisdiction** (tax recovery not assessed), **chart of accounts** (no account names invented), cardholder transaction limit. Go-ahead assumed.

## Upload validation (shown before any work)

| File | What it actually is | Company / period | Usable? | Needed for | Verdict |
|---|---|---|---|---|---|
| `corporate_card_statement_2025-09.csv` | Card issuer transaction listing: 9 lines, 3–28 Sep 2025, date / merchant / amount; total 2,513.59 | No entity, currency or cardholder | Yes, but **no opening balance, payments or closing balance**, no posting date, no card or cardholder | Steps 1–2, 6 | **Accepted with a limit**: company user-asserted; balance tie-out (Step 2) cannot be done, only a listing-to-listing match |
| `card_account_ledger_2025-09.csv` | Book-side card charges: 7 lines, 3–25 Sep 2025, with a yes/no receipt flag; total 2,036.59 | No entity, currency or account | Yes; **no GL account coding**, no liability balance, no payments | Steps 1–4, 6 | **Accepted with a limit**: company user-asserted; the receipt flag shows a receipt was recorded as captured, not that it was matched and verified; coding review impossible |
| `expense_policy.md` | Expense policy: receipts over 25, meals 75/person, hotel 250/night, business purpose required | No entity | Yes | Steps 3, 6 (thresholds) | **Accepted with a limit**: company user-asserted; no capitalisation threshold or card limit in it |
| `corporate_card_statement_2025-09_final.csv` | **An employee shift rota** (E08–E10, weeks 1–4: days / nights / off). Not a card statement despite its name | None | n/a | No step uses it | **Rejected.** If a final statement exists (with balances), please upload it in its place |

**Still missing:** statement balances (opening, payments, closing) and the **GL card liability balance at 30 Sep** — both required for the Step 2 tie-out; the **receipts themselves**; cardholder name; chart of accounts; capitalisation threshold; tax jurisdiction; business purpose per charge.

*I would wait here for your answer; proceeding with the accepted files as instructed.*

## Findings

**1. Statement to ledger: 477.00 on the statement is not in the books (Steps 1–2).**

| | Amount |
|---|---:|
| Statement charges, 9 lines | 2,513.59 |
| Ledger charges, 7 lines | 2,036.59 |
| **Difference** | **477.00** |
| (a) Second HILTON GARDEN INN 438.00 on 5 Sep — on statement, not in ledger | 438.00 |
| (b) LATE FEE 28 Sep — on statement, not in ledger | 39.00 |
| Unexplained | **0.00** |

The other 7 lines agree one-for-one on date, merchant and amount.

**2. Possible duplicate charge: HILTON GARDEN INN 438.00 twice on 5 Sep (Step 6, duplicate test).** Same merchant, same amount, same day. The ledger has it once. Either the issuer double-charged (dispute it; do not book the credit until the issuer resolves it) or there were two genuine stays/rooms (then the second is unposted). Ask the cardholder for the folio. Not posted pending that answer.

**3. Late fee 39.00 not booked (Step 7).** A fee from the issuer is a real cost and a sign a payment was late. Proposal only:

```
DR  Bank fees / card fees (account per your chart)      39.00
    CR  Credit card liability                               39.00
Memo: Card late fee, statement Sep 2025
```

**4. Missing receipts above the 25 threshold (Step 3).** Three charges, **741.14** in total, flagged "no" in the ledger: DELTA AIR 612.40 (3 Sep), ADOBE *CREATIVE CLOUD 89.99 (9 Sep), UBER *TRIP 38.75 (21 Sep). All 🔴 exceptions. The four flagged "yes" are **receipt captured, not verified** — no receipt images were uploaded, so none is 🟢 matched.

**5. Policy checks the data cannot clear (Step 6).**
- **THE CAPITAL GRILLE 486.50 (meal):** within the 75-per-person cap only if 7 or more people attended (486.50 / 75 = 6.49). Attendee list and business purpose needed.
- **HILTON GARDEN INN 438.00 per charge:** 188.00 over the 250-per-night cap if one night; within it if two or more. Folio needed — and see finding 2.
- **Business purpose:** recorded for none of the 9 charges; the policy requires it for every claim.

**6. Recurring subscription candidate (Step 6).** ADOBE *CREATIVE CLOUD 89.99 — **1,079.88 a year** if monthly. Only one month was supplied, so recurrence is not proven; prior months would confirm. Also missing its receipt.

**7. Tests that could not run.** Capitalisation-threshold breach: **not run** (no threshold; never defaulted) — the largest charge is 612.40. Suspense / uncategorised coding: **not run** (no coding in the ledger). Tax recovery: **not assessed** (no jurisdiction). Charges with no merchant identification: **nil**. Cash advances: **nil** on merchant names. Sanctions screening: not possible from these files.

**8. Posting option.** The ledger posts charges individually, which indicates **Option A** (each charge to expense when incurred); this step therefore **proposes** only the two missing items above and reviews nothing else, since no coding is visible.

## Proposed coding (no chart supplied — categories, not account names)

Travel: DELTA AIR 612.40, HILTON 438.00, UBER 38.75 · Meals: CAPITAL GRILLE 486.50 · Software subscription: ADOBE 89.99 · Office supplies: STAPLES 156.20 · Amazon 214.75: **unclear** (marketplace; needs the receipt).

## What was not done, and why

- **Closing-balance tie-out (Step 2)** — no statement balances and no GL liability balance; upload the full issuer statement and the trial balance at 30 Sep.
- **Receipt matching** — no receipts uploaded; only the ledger's yes/no flag.
- **Coding review, capital test, tax recovery** — no chart of accounts, capitalisation threshold or jurisdiction.
- **Excel workpaper** — not created; I would ask first (`CC_Recon_[Cardholder]_2025-09.xlsx`, cardholder unknown).

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, September 2025, USD — user-asserted. Data source: upload (gateway absent). Statement and card ledger accepted with limits (no balances; no coding; company user-asserted); policy accepted with a limit; `corporate_card_statement_2025-09_final.csv` rejected (shift rota).

**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status | Note |
|---|---|---|
| 0 Evidence | Done with a limit | Listings only; no balances |
| 1 Parse statement | Done with a limit | No posting dates, balances, cardholder |
| 2 Tie to GL | **Not done** as a balance tie; listing difference 477.00 fully explained | Needs statement balances + GL balance |
| 3 Receipts | Done with a limit | Flag only; 3 missing above 25 |
| 4 Coding | Done with a limit | Categories proposed; no COA |
| 5 Tax | Not done | No jurisdiction |
| 6 Exceptions | Done with a limit | Duplicate, missing receipts, policy caps, subscription; capital test not run |
| 7 JE | Proposed, not posted | Late fee 39.00; Hilton pending |
| 8 Output | Tables in chat | xlsx only on a yes |
| 9 Save preferences | Not done | Offered only after results are approved |

**Data sources:** user uploads — `corporate_card_statement_2025-09.csv`, `card_account_ledger_2025-09.csv`, `expense_policy.md`. Nothing was posted, disputed, sent or paid.
