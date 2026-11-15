# Business combination — Northbrook Trading Ltd acquires Harlow Fabrication Ltd

This run is manual: no Mosofin connection is present. Everything below comes from the file you uploaded. Nothing has been posted, sent or changed.

## (a) Read-back

Accounting for the purchase of **100% of Harlow Fabrication Ltd** by **Northbrook Trading Ltd** on **1 July 2025** (the acquisition date, used for every measurement below), under **US GAAP (ASC 805)**, for **cash plus a cash-settled earnout**, in **USD**, reporting as at **30 September 2025**, from the terms and valuation summary you uploaded. The company name is as you stated it; it is not confirmed against a connection.

Intake answers taken from the file, not from you: the date, the framework, the consideration, 100% purchased, and the earnout classification (liability). Not answered anywhere: whether Northbrook held an interest in Harlow before 1 July 2025. **Assumed: no prior interest** (the skill's default; please correct me if wrong).

What I received:
- `acquisition_terms_and_valuation.md` — deal terms (acquirer, date, 100%, cash 1,400,000, earnout up to 300,000 at fair value 180,000, deal costs 46,000) and a seven-line table of Harlow's book values and fair values citing a valuation report dated 20 August 2025.
- `acquisition_terms_and_valuation_final.csv` — three rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `acquisition_terms_and_valuation.md` | A one-page summary of deal terms with a book-value and fair-value table | Yes: Northbrook Trading Ltd acquiring Harlow Fabrication Ltd, 1 July 2025. Currency not stated (USD from intake) | Yes. Columns identifiable; book net assets foot to 470,000 and fair-value net assets to 832,000. One line does not tie (deferred tax, see findings) | Steps 1–7 | **Accepted with a limit**: it is a summary, not the purchase agreement, the valuation report or Harlow's balance sheet. Fair values are taken as quoted from the report; I cannot check them to the report, name the valuer, or see useful lives |
| `acquisition_terms_and_valuation_final.csv` | A four-week staff shift roster for employees E08–E10 | No company, date or amount in it | Not for this skill | No step uses it | **Rejected**. The name suggests a final version of the deal terms; the content is a rota. Set aside. If a final valuation exists, please upload that |

**Still missing:** the valuation report itself (required), the purchase agreement (required; a summary is allowed and was received), Harlow's balance sheet at 1 July 2025 as a separate document (required; only five summary lines received), deal cost invoices (recommended).

What the output will not cover as a result: confirmation of the fair values to the report, the valuer's name, intangible lives, the earnout terms and targets, and where the 46,000 of deal costs was actually posted. I would stop here and wait for your answer.

*You replied: go ahead with the accepted file.*

## (c) Findings

**Step 1 — acquirer and date.** Northbrook Trading Ltd obtains 100% of the shares on 1 July 2025. On the facts given, the legal acquirer is the party gaining control; nothing suggests a reverse acquisition. Common control was not addressed in the file; please confirm the two companies had no common owner.

**Step 2 — business or group of assets (your decision; the test set out).** Gross identifiable assets at fair value are 1,160,000. The largest single asset class is fixed assets at 410,000 (35.3%); customer relationships 260,000 (22.4%). Fair value is not concentrated in one asset or group of similar assets, so the screen does not point to an asset purchase. The next question, whether Harlow came with inputs and a substantive process, is for you to confirm. The rest assumes a business.

**Step 3 — consideration transferred**

| Component | Amount | Source |
|---|---:|---|
| Cash | 1,400,000 | Deal summary |
| Earnout, at acquisition-date fair value (maximum 300,000) | 180,000 | Deal summary; valuer not named |
| **Total consideration** | **1,580,000** | |

The earnout goes in at its fair value of 180,000, not its 300,000 maximum.

**Deal costs of 46,000 are not part of the price.** Legal and advisory costs are expensed as incurred. If they were added, consideration and goodwill would both be overstated by 46,000 (goodwill 794,000 instead of 748,000). I could not test where they were posted: no ledger was supplied.

**Step 4 — identifiable net assets at fair value** (fair values from the valuation report dated 20 August 2025, as quoted)

| Item | Book value | Fair value | Uplift | Fair value equals book by |
|---|---:|---:|---:|---|
| Receivables | 210,000 | 205,000 | (5,000) | — |
| Inventory | 180,000 | 195,000 | 15,000 | — |
| Fixed assets | 320,000 | 410,000 | 90,000 | — |
| Customer relationships | — | 260,000 | 260,000 | — |
| Trade name | — | 90,000 | 90,000 | — |
| Payables and accruals | (240,000) | (240,000) | 0 | Not stated whether a conclusion or a default; please confirm |
| Deferred tax on uplifts | — | (88,000) | (88,000) | — |
| **Net identifiable assets** | **470,000** | **832,000** | **362,000** | |

**The deferred tax line does not tie to the table.** Total uplift before tax is 450,000 (−5,000 + 15,000 + 90,000 + 260,000 + 90,000); at 20% that is 90,000, not 88,000. The 88,000 equals 20% of 440,000, which is fixed assets plus the two intangibles only, leaving out inventory (+15,000) and receivables (−5,000). I have used 88,000 as supplied. If 90,000 is right, net assets are 830,000 and goodwill 750,000. This needs the valuer or the tax preparer to confirm, along with the tax bases.

Not in the valuation summary, to ask the valuer: order backlog, non-compete agreements, licences, contingent liabilities. Assembled workforce is correctly absent; it stays inside goodwill.

**Step 5 — goodwill**

| | Amount |
|---|---:|
| Consideration transferred | 1,580,000 |
| Non-controlling interest (100% bought) | 0 |
| Previously held interest (assumed none) | 0 |
| Less fair value of identifiable net assets | (832,000) |
| **Goodwill (provisional)** | **748,000** |

Positive, so no bargain purchase. Goodwill is 47% of the consideration.

**Step 6 — proposed acquisition entry, 1 July 2025. PROPOSAL — NOT POSTED.** Account names are generic; Northbrook's chart was not supplied.

| Account | Debit | Credit |
|---|---:|---:|
| Receivables | 205,000 | |
| Inventory | 195,000 | |
| Fixed assets | 410,000 | |
| Customer relationships | 260,000 | |
| Trade name | 90,000 | |
| Goodwill | 748,000 | |
| Payables and accruals | | 240,000 |
| Deferred tax liability | | 88,000 |
| Cash | | 1,400,000 |
| Contingent consideration liability | | 180,000 |
| **Total** | **1,908,000** | **1,908,000** |

Separately, also a proposal: debit acquisition-related costs (expense) 46,000, credit cash or payables 46,000.

**Step 7 — measurement period.** All amounts are **provisional**. The period runs for up to one year from 1 July 2025, so it closes no later than **1 July 2026**. Only facts that existed at 1 July 2025 qualify; I have not finalised anything. The valuation report is dated 20 August 2025, inside the period.

**Step 8 — after the acquisition, due at 30 September 2025 (not computed; inputs missing).**
- Earnout liability: remeasure to fair value at 30 September 2025 and each reporting date; the change goes through profit and loss, not goodwill. Needs the valuer.
- Customer relationships and trade name: amortisation from 1 July 2025 needs useful lives, which were not supplied.
- Inventory step-up of 15,000 passes through cost of sales as that inventory is sold.
- Fixed asset step-up of 90,000 increases depreciation; lives not supplied.
- Goodwill 748,000: not amortised; annual impairment test (goodwill-and-impairment-testing).

**Step 9 — disclosure data available now:** acquiree name, date, 100%, consideration by class (cash 1,400,000; contingent 180,000, range 0 to 300,000), the asset and liability classes above, goodwill 748,000, deal costs 46,000 expensed.

## (d) What was not done, and why

- **No fair value was computed or checked.** They come from the valuation report as quoted in the summary; the report itself was not uploaded and the valuer is not named. Owner: valuation specialist.
- **Deferred tax 88,000 versus 90,000** — flagged, not corrected. Owner: tax preparer.
- **Deal cost posting test** — no ledger or invoices. Owner: Northbrook finance.
- **Harlow's full balance sheet at 1 July 2025** — only five summary lines; cash, debt and other balances, if any, are not shown.
- **Business-versus-asset conclusion, common control, prior interest** — yours to confirm.
- **Earnout remeasurement at 30 September 2025, amortisation and depreciation of the step-ups** — fair value update and useful lives not supplied.
- **Harlow's revenue and earnings since 1 July 2025; reasons for the acquisition; qualitative goodwill factors** — not supplied.
- **Excel workpaper** (`Business_Combination_Harlow Fabrication_2025-09-30.xlsx`) — not created; say if you want it.
- **Posting** — this skill never posts. The entry is a proposal for a person to review and post.

**Data sources:** user-uploaded `acquisition_terms_and_valuation.md` only (all figures); intake answers (company, period, currency). No ledger read.
