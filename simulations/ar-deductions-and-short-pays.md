# Open deductions: Northbrook Trading Ltd, as at 30 September 2025

Manual run: the Mosofin tools are not present, so everything below comes from your uploads. Nothing was posted, issued or sent.

## Read-back

> Working **Northbrook Trading Ltd**'s open deductions **as at 30 September 2025**, in **USD**, from **the deduction log you uploaded** (`open_deductions_2025-09-30.csv`; there is no separate deduction account), with **`deduction_backup.md`** and **`cash_application_policy.md`** (short-pay write-off up to 50, approved by the credit manager). Dispute window: **90 days**. Shall I go ahead?

Company, date and currency are **user-asserted**: none of the files names the company or the currency.

## Validation of the upload (shown before any work)

| File | What it actually is | Company / period | Usable | Needed by | Verdict |
|---|---|---|---|---|---|
| `open_deductions_2025-09-30.csv` | Deduction log: 7 rows (ref, customer, customer ref, payment date, invoice, amount deducted, reason, status), total 6,028.50, payment dates 20 Jun to 24 Sep 2025 | No company or currency named; dates consistent with 30 Sep 2025 | All needed columns present; no invoice amount or amount paid columns | Steps 1-5 | **Accepted with a limit**: company and currency user-asserted; invoice amount and amount paid not supplied, so those log columns stay blank |
| `open_deductions_2025-09-30_final.csv` | **Not a deduction log.** A staff shift roster: columns employee, week_1..week_4, rows E08-E10 with "days / nights / off". No customer, invoice or amount | None | Nothing this skill can use | No step | **Rejected**: the name suggests a final deduction log, the content is a rota. If a later version of the log exists, please upload it in its place; until then I work from the 7-row log above |
| `deduction_backup.md` | Backup register: one row per deduction naming the document and what it shows (carrier exception report, promotion agreement, signed delivery note, contract clause; "none" for two items) | Dates in 2025, consistent | Usable | Step 4 | **Accepted with a limit**: these are summaries of the documents, not the documents themselves; decisions below cite them as user-supplied |
| `cash_application_policy.md` | Policy: write-off up to 50 approved by the credit manager; unapplied cash sits in 1100 Accounts Receivable | No company or date named | Usable | Steps 4-5 (write-off limit, approver) | **Accepted with a limit**: company user-asserted |
| `customer_list.csv` | Customer master: 12 customers, terms 30 days, credit limits, AP contact emails | No company named | Usable | Step 5 (who each draft goes to) | **Accepted with a limit**: company user-asserted |

**Still missing (recommended, not required):** remittance advices for the short payments (needed to place DED-0083); an open receivables listing or aged receivables as at 30 Sep 2025 (needed to tie the log); a chart of accounts (needed for real account names in the entries). I would wait for your answer here; proceeding on "go ahead with the accepted files".

## The deduction log (aged from payment date)

| Ref | Customer | Invoice | Paid | Age (days) | Band | Amount | Reason as given | Mapped | Evidence | Decision | Proposal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DED-0071 | Castleton Foods | INV-19402 | 2025-06-20 | 102 | over 90 | 1,240.00 | shortage 40 cases | shortage | Delivery note for INV-19402 signed 22 May 2025 by R. Hale: 240 cases received in good condition; invoice bills 240 | **Invalid** | Dispute. **At risk**: past the 90-day window |
| DED-0083 | Brecon Outdoor | INV-19560 | 2025-07-30 | 62 | 61-90 | 2,900.00 | (blank) | unexplained | None; no remittance received | **Needs backup** | Ask the customer for the reason and the remittance. Not yet a confirmed deduction: may be a payment-run error |
| DED-0094 | Pennine Retail Group | INV-19688 | 2025-08-14 | 47 | 31-60 | 368.00 | Q3 promotion 2% | promotion | Promotion agreement PRM-Q3 signed 20 Jun 2025: 2% on orders shipped 1 Jul-30 Sep 2025, once per invoice; INV-19688 (18,400.00) shipped 28 Jul 2025. 2% x 18,400.00 = 368.00 | **Valid** | Credit memo 368.00 against INV-19688 |
| DED-0098 | Tideswell Hotels | INV-19715 | 2025-09-05 | 25 | 0-30 | 42.50 | price difference | pricing | None | **Needs backup** (agreed price list or quote) | Within the 50 limit: write-off proposal, approver the credit manager, as the cheaper route than chasing |
| DED-0100 | Ashby Engineering | INV-19759 | 2025-09-18 | 12 | 0-30 | 610.00 | freight not agreed | freight | Supply contract clause 4: FOB origin, freight charged to customer at cost as a separate line; INV-19759 carries freight 610.00 | **Invalid** | Dispute |
| DED-0101 | Ridgeway Logistics | INV-20611 | 2025-09-24 | 6 | 0-30 | 500.00 | damaged pallet | damage | Fastline Haulage exception report FX-55210, 15 Sep 2025, signed by driver and customer: 1 pallet crushed, goods value 500.00 refused | **Valid** | Credit memo 500.00 against INV-20611 |
| DED-0102 | Pennine Retail Group | INV-19688 | 2025-09-12 | 18 | 0-30 | 368.00 | Q3 promotion 2% | promotion | Same invoice, same reason, same amount and customer ref PRM-Q3-0087 as DED-0094; agreement allows the deduction **once per invoice** | **Invalid: duplicate** | Dispute, citing DED-0094 |

**Totals: 7 deductions, 6,028.50.**

| By reason | Count | Amount | | By age band | Count | Amount |
|---|---|---|---|---|---|---|
| Promotion | 2 | 736.00 | | 0-30 | 4 | 1,520.50 |
| Unexplained | 1 | 2,900.00 | | 31-60 | 1 | 368.00 |
| Shortage | 1 | 1,240.00 | | 61-90 | 1 | 2,900.00 |
| Freight | 1 | 610.00 | | over 90 | 1 | 1,240.00 |
| Damage | 1 | 500.00 | | | | |
| Pricing | 1 | 42.50 | | | | |

| By decision | Count | Amount |
|---|---|---|
| Valid (credit) | 2 | 868.00 |
| Invalid (dispute), incl. 1 duplicate | 3 | 2,218.00 |
| Needs backup | 2 | 2,942.50 (of which 42.50 proposed for write-off) |

## Duplicates and repeats (checked before deciding)

- **INV-19688 deducted twice by Pennine Retail Group**: DED-0094 (14 Aug, 368.00) and DED-0102 (12 Sep, 368.00), same reason, same customer ref PRM-Q3-0087. The promotion is valid once; the second deduction is a second recovery of the same 368.00.
- No credit memos were supplied, so "deduction already credited" could not be checked (see Not done).
- No other repeat claimants in this log.

## Proposals (for approval; nothing issued or sent)

**Credit memos:** INV-19688 Pennine 368.00 (promotion); INV-20611 Ridgeway 500.00 (damage). Total 868.00.

**Write-off:** DED-0098 Tideswell 42.50, within the 50 limit, **approver: credit manager**. No other item is within the limit.

**Dispute drafts** (to the AP contacts in the customer list):
- Castleton Foods (ap@castleton.example): INV-19402, 1,240.00. The delivery note signed 22 May 2025 by R. Hale confirms 240 cases received in good condition, the invoiced quantity. Please pay the balance. Note: taken 102 days ago, past the 90-day window; recovery may need goodwill.
- Ashby Engineering (ap@ashby.example): INV-19759, 610.00. Clause 4 of the supply contract sets delivery FOB origin with freight charged at cost; please pay the freight line.
- Pennine Retail Group (ap@pennine.example): INV-19688, 368.00 deducted on 12 Sep (DED-0102). The Q3 promotion was already taken on this invoice on 14 Aug (DED-0094); the agreement allows it once per invoice. Please pay the 368.00.

**Backup request:** Brecon Outdoor (ap@brecon.example): payment of 30 Jul 2025 is 2,900.00 short against INV-19560 with no reason and no remittance. Please send the remittance and the reason. Above the write-off limit; it ages into the at-risk band on 28 Oct 2025.

## Proposed entries (proposals; account names other than 1100 to be confirmed from your chart of accounts)

```
Promotion credit, Pennine INV-19688
DR Promotional allowances (reduction of revenue)   368.00
    CR 1100 Accounts Receivable                        368.00
Damage credit, Ridgeway INV-20611
DR Sales returns and allowances                    500.00
    CR 1100 Accounts Receivable                        500.00
Write-off, Tideswell INV-19715
DR Deductions written off                           42.50
    CR 1100 Accounts Receivable                         42.50
```
Each balances. Promotion is treated as a revenue reduction, not an expense.

## Not done, and why

- **Tie of the log to receivables**: not done. No deduction account exists and no receivables listing or ledger was uploaded. Upload the aged receivables as at 30 Sep 2025 to tie 6,028.50.
- **Already-credited check**: not done. No credit memo listing uploaded.
- **Invoice amount / amount paid per deduction**: not available from the log.
- **Real account names** other than 1100: no chart of accounts uploaded; the names above are placeholders.
- `open_deductions_2025-09-30_final.csv` was rejected (a staff roster) and not used.

## Coverage sheet (manual run)

**Environment:** Northbrook Trading Ltd, as at 30 Sep 2025, USD, all user-asserted. Data source: upload. Files: deduction log (accepted, limit: company/currency asserted, no invoice amounts); backup register (accepted, limit: summaries, not source documents); cash application policy (accepted, limit: company asserted); customer list (accepted, limit: company asserted); `_final.csv` (rejected: shift roster).

**Capability map:** Not applicable: no connection. Every task is `[manual]`.

| Step | Status |
|---|---|
| 0 Fetch evidence | Done with a limit: uploads only; no invoices, payments, credit memos, receivables |
| 1 Build log | Done with a limit: invoice amount and amount paid unavailable |
| 2 Age and size | Ageing done; **tie to receivables not done** (no ledger) |
| 3 Duplicates and repeats | Duplicate found; already-credited check **not done** (no credit memos) |
| 4 Decide against evidence | Done, `[manual]`, using the backup register (summaries) |
| 5 Propose resolutions | Done; drafts only, nothing sent |
| 6 Entries | Done with a limit: placeholder account names except 1100 |
| 7 Save | Not offered until you have reviewed the results |

Would you like the log as `AR_Deductions_Northbrook_Trading_2025-09-30.xlsx`? I will create it only on a yes.

**Data sources:** upload only: `open_deductions_2025-09-30.csv`, `deduction_backup.md`, `cash_application_policy.md`, `customer_list.csv`.
