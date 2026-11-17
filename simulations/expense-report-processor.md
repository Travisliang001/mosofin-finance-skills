# Expense report review — employee E04, Northbrook Trading Ltd, September 2025 (upload path)

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would automate the ledger checks — docs.mosofin.com.) Nothing was approved, rejected, paid or posted; everything below is a proposal for a person.

## (a) Read-back

Reviewing the **September 2025 expense report of employee E04** (the identifier comes from the file name only; the report itself names no employee) for **Northbrook Trading Ltd** (user-asserted), in **USD**, against the expense policy and chart of accounts you uploaded.

Not answered at intake, and what the skill does about each:

| Input | Treatment |
|---|---|
| **Mileage rate** | **Never defaulted and never supplied from memory.** The policy says "ask finance". The mileage line cannot be validated until finance confirms the rate. |
| Payment method per line (own money vs corporate card) | Not in the report. **Not assumed.** Figures below are shown as "if out-of-pocket"; please confirm. |
| Receipts (images) | Not supplied; the receipt column is taken "per the report", not verified |
| Tax jurisdiction, deductibility split, input tax | Not supplied → no deductible / non-deductible split, no tax decomposition |
| Per-diem table, FX source | Not needed — no per-diem claims; single currency assumed (no currency column) |
| Employee name and department | Not supplied; E04 not matched to an employee record |

## (b) Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `expense_report_E04_2025-09.csv` | An expense report: date, category, merchant, amount, receipt flag, business purpose. 6 lines, total 2,155.65 | Dates 3–22 Sep 2025. No company, employee, or currency in the content | Partly. Missing: employee name, currency, payment method, line ID, hotel nights, attendees, mileage start/end | Yes — Steps 1–5 | **Accepted with a limit**: employee identity rests on the file name; card-paid vs out-of-pocket cannot be separated; per-night and per-person tests rest on stated assumptions |
| `expense_policy.md` | A T&E policy with five rules (receipts over 25; meals 75 per person; hotel 250 per night; mileage at finance's published rate; business purpose required). Marked "sample… fictitious company" | No company name or effective date | Yes, but thin: silent on airfare class, alcohol, ground transport, late submission; mileage rate not stated | Yes — Step 2 | **Accepted with a limit**: only these five rules are tested |
| `chart_of_accounts.csv` | Chart of accounts: 29 accounts with number, name, type | No company name | Yes — but it has **no travel, meals, lodging or mileage expense account and no employee reimbursement payable** | Yes — Step 3 | **Accepted with a limit**: coding cannot be completed to real accounts |
| `expense_report_E04_2025-09_final.csv` | **Not an expense report.** A staff shift rota: employee, week_1…week_4, "nights/days/off" for E08–E10 (E04 is not even in it) | No dates, merchants or amounts | No | No step uses it | **Rejected** on content despite the name. If a later version of the report exists, upload that. Not used. |

Still missing: **the mileage rate from finance** (required — a mileage claim is present); the payment method per line; receipts; hotel folio (nights); meal attendees; a card statement or ledger extract for the duplicate check against charges the company already paid.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## (c) Findings

**Policy supplied: yes (five rules).** Total claimed **2,155.65** across 6 lines. Not mock data.

### Line detail

| # | Date | Category | Merchant | Amount | Receipt (per report) | Policy check | Proposed |
|---|---|---|---|---:|---|---|---|
| 1 | Wed 3 Sep | Airfare | Delta | 612.40 | yes | Purpose given. Policy has no class rule | 🟢 Approve 612.40 |
| 2 | Fri 5 Sep | Hotel | Hilton Garden Inn | 438.00 | yes | **Over the 250-per-night cap if one night (188.00 over); within it if two nights (219.00 a night).** Nights not stated | 🟡 Review — need folio. 250.00 supportable now |
| 3 | Fri 5 Sep | Hotel | Hilton Garden Inn | 438.00 | yes | **Exact duplicate of line 2**: same date, merchant, amount, purpose | 🔴 Reject 438.00 unless the folio shows a second, separate charge |
| 4 | Tue 16 Sep | Meals | The Capital Grille | 486.50 | yes | "Dinner, 2 people" = **243.25 per person against a 75 cap**. Allowed 2 × 75 = 150.00; **excess 336.50**. No attendee names and no business purpose beyond "dinner"; not on the Castleton trip dates | 🔴 Disallow 336.50; 🟡 the 150.00 needs attendees and purpose |
| 5 | Sun 21 Sep | Ground transport | Uber | 38.75 | **no** | **Receipt required over 25 — missing. Business purpose blank.** Weekend ride with no stated purpose: possible personal | 🟡 Review — hold 38.75 until receipt and purpose supplied |
| 6 | Mon 22 Sep | Mileage | (none) | 142.00 | no | 220 miles claimed; 142.00 ÷ 220 = **0.6455 per mile implied**. **Policy rate not supplied** — cannot confirm. "220 miles" sits in the purpose field: no purpose, no start/end points | 🟡 Review — hold 142.00 pending finance's rate and a trip log |

### Exceptions

| Line | Issue | Severity | Recommended action |
|---|---|---|---|
| 3 | Duplicate hotel claim, 438.00 | 🔴 Reject | Remove one line; ask the claimant for the folio |
| 4 | Meal over per-person cap by 336.50 (243.25 vs 75 a head) | 🔴 Reject the excess | Pay at most 150.00; manager decides any exception |
| 4 | Attendees and business purpose not stated | 🟡 Review | Obtain names and client |
| 2 | Hotel 438.00 vs 250 a night — nights unknown | 🟡 Review | Folio. If one night, disallow 188.00 |
| 5 | No receipt (38.75 > 25) and no purpose; Sunday | 🟡 Review | Receipt and purpose, or treat as personal |
| 6 | Mileage rate unconfirmed; no route or purpose | 🟡 Review | Finance's published rate; recompute 220 × rate |
| 2–3 | Hotel dated 5 Sep, flight 3 Sep, same purpose | 🟢 Note | Probably the checkout date; folio will confirm |
| all | Payment method not stated | 🟡 Review | Any line paid on the corporate card is not reimbursable to the employee |

### Reimbursement — proposal, if every line was paid out of pocket

| Component | USD |
|---|---:|
| Total claimed | 2,155.65 |
| Less duplicate hotel (line 3) | (438.00) |
| Less meal excess over cap (line 4) | (336.50) |
| **Maximum supportable if every open query is resolved in the claimant's favour** | **1,381.15** |
| Less held pending evidence: hotel over one-night cap 188.00; Uber 38.75; mileage 142.00; meal allowance pending attendees 150.00 | (518.75) |
| **Supportable today without further evidence** (airfare 612.40 + hotel 250.00) | **862.40** |

Disallowed outright: **774.50**. If the hotel was a single night the maximum falls to 1,193.15. The mileage figure will change if finance's rate is not 0.6455.

### GL coding and posting inputs

**The uploaded chart of accounts has no account for travel, lodging, meals, ground transport or mileage, and no employee reimbursement payable.** I do not invent account numbers. Conceptual coding, **PLACEHOLDER — REMAP REQUIRED**:

| Lines | Conceptual account | Amount at maximum supportable |
|---|---|---:|
| 1 | Travel — Airfare | 612.40 |
| 2 | Travel — Lodging | 438.00 |
| 4 | Meals | 150.00 |
| 5, 6 | Travel — Local Transport | 180.75 |
| Credit | Employee reimbursement payable (nearest real accounts: 2000 Accounts Payable or 2100 Accrued Liabilities; card-paid lines would go to 2050 Corporate Card Payable) | 1,381.15 |

Suggestion: add travel and meals expense accounts, and (once you give the jurisdiction's rule) a non-deductible meals account or class. The balanced entry itself would be built by the journal-entry skill from these inputs; nothing is posted.

## (d) What was not done, and why

| Task | Status | What is needed |
|---|---|---|
| Mileage validation | **Not performed** | Finance's published rate (never supplied from memory) |
| Duplicate check against charges already paid on the corporate card | **Not run — not "clean"** | Card statement or ledger extract; payment method per line |
| Receipt verification | Per the report only | Receipt images |
| Per-night and per-person tests | Run on stated assumptions (nights unknown; 2 diners as stated) | Folio; attendee list |
| Airfare class, alcohol, late submission | Not tested | Policy is silent |
| Deductibility split, input tax | Not performed | Jurisdiction and rules |
| Coding to real accounts; historical coding support | Placeholder only | A chart with T&E accounts; ledger history |
| Employee match; reimbursement-payable and card-clearing checks | Not run | Employee list; ledger balances |
| Approving, rejecting, paying or posting | Not done — read-only | A manager and AP |

Policy assumptions for you to confirm: the 75 meal cap applies per person per meal; the 250 hotel cap is per night including taxes; "over 25" means strictly above 25.

Would you like the workpaper as `E04_ExpenseReport_2025-09.xlsx`? Only on your yes.

**Data sources:** user uploads only — `expense_report_E04_2025-09.csv`, `expense_policy.md`, `chart_of_accounts.csv`. No Mosofin connection used.
