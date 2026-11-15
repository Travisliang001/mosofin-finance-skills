#!/usr/bin/env python3
"""Write samples/ into every skill folder: test inputs, one deliberately wrong file, and the expected outcome.

Dependency-free and deterministic. Run from anywhere:

    .github/samples/build.py            # (re)write skills/*/samples/
    .github/samples/build.py --check    # fail if any skill has no catalogue entry or the files have drifted

The data is one fictitious company (see base.py) plus short documents (see files.py).
Each catalogue line is: files to upload, what a correct run should find, and any intake answers
beyond the standard ones.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import base as B
from files import F

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
S = B.SEEDED
ENTITY = {  # skills whose sample is a different entity or period from the base company
 "aml-kyc-procedures": ("Northbrook Payments (a separate company)", "Q3 2025 (July to September)", "USD"),
 "nonprofit-fund-accounting": ("Riverside Community Trust", "year to 30 June 2025", "USD"),
 "grant-accounting-nonprofit-restricted-funds": ("Riverside Community Trust", "year to 30 June 2025", "USD"),
 "government-fund-accounting-gasb": ("Millbrook Township", "year to 30 June 2025", "USD"),
 "healthcare-revenue-cycle-accounting": ("Lakeside Clinic", "September 2025", "USD"),
 "insurance-accounting-overview": ("Harbour Mutual", "September 2025", "USD"),
 "vat-gst-international": ("Northbrook UK Ltd", "Q3 2025 (July to September)", "GBP"),
 "sales-tax-us-multistate": (B.CO, "2025 year to date (January to September)", "USD"),
 "1099-and-t4a-prep": (B.CO, "reporting year 2025, run on 30 September 2025", "USD"),
 "closing-entries-and-trial-balance": (B.CO, "year ended 31 December 2024", "USD"),
 "year-end-close": (B.CO, "planning the close of the year ending 31 December 2025; the latest closed year is 2024", "USD"),
 "tax-return-prep-corporate": (B.CO, "tax year 2024", "USD"),
 "business-combinations-asc805": (B.CO, "acquisition on 1 July 2025", "USD"),
}
def std(skill):
    co, per, ccy = ENTITY.get(skill, (B.CO, f"{B.PERIOD} (as at {B.AS_AT})", B.CCY))
    return (f"Company: {co}. Period: {per}. Currency: {ccy}. Data source: upload only, Mosofin is not used. "
            "Where the files do not answer an intake question, say so and let the skill apply its stated default.")
TB_FIRST_COMPANY = {"financial-statement-builder", "month-end-close-checklist", "audit-prep-pbc-list", "consolidation-and-eliminations", "year-end-close"}

C = {  # skill: (files, [expected findings], extra intake answers)
 # --- everyday AP, AR and close ---
 "accruals-and-deferrals": ("tb accrual_inputs prepaid gl", ["Proposes accruals for the three received-not-billed items (5,800, 4,200, 1,850)", "Insurance prepaid release of 1,500 is already posted (JE-0902)"], ""),
 "ap-accrual-cutoff": ("ap_open po grn accrual_inputs", [S["short_ship"], "Freight for the last week of September (5,800) is received and not billed"], ""),
 "ap-aging-and-payment-runs": ("ap_open ap_paid vendors", [S["dup_bill"], S["early_pay"], S["bank_change"] + ": hold payment until verified", "Summit Freight's bill was due 22 September on its 15-day terms and is overdue"], ""),
 "ar-aging-and-collections": ("ar_aging ar_hist customers", [S["old_ar"], S["ar_conc"], S["ar_credit"], "Harlow owes 248,157 against a 200,000 credit limit: 48,157 over", "Harlow pays in 74 to 100 days and is getting slower"], ""),
 "balance-sheet-reconciliations": ("tb bank cash_ledger ar_aging ap_open items fa", [S["bank_items"], "Receivables and inventory sub-ledgers agree to the trial balance", S["fa_disposed"]], ""),
 "bank-reconciliation": ("bank cash_ledger", [S["bank_items"], f"Statement closing {B.BANK_CLOSE:,}; ledger closing {B.CASH_GL:,}; reconciles after the four items"], ""),
 "budget-vs-actual-analysis": ("pnl_ytd budget", [S["marketing_var"], S["margin_dip"], S["legal_oneoff"]], ""),
 "cash-application": ("lockbox remit ar_aging cashapp_policy", ["Ridgeway pays INV-20611 short by 500 (deduction DM-118), above the 50 write-off limit", "Ashby reference 'INV20685' needs matching to INV-20685 style numbering", "Receipt of 4,003 from an unknown payer matches Foxhall's balance by amount only: propose, do not apply"], ""),
 "cash-flow-forecast-13-week": ("ar_aging ap_open bank payroll loan", ["Receipts timed from the ageing with Harlow's 48,200 treated as doubtful", "Loan payment 6,900 a month and two payroll runs a month appear as outflows"], "Minimum cash to hold: 250,000."),
 "closing-entries-and-trial-balance": ("tb_py coa", ["Closes every income and expense account to retained earnings and produces a post-closing trial balance that balances"], ""),
 "credit-card-reconciliation": ("card card_ledger expense_policy", ["Hilton Garden Inn 438.00 is charged twice on the statement and booked once", "Late fee 39.00 is not in the books", "Several ledger lines have no receipt"], ""),
 "credit-memo-and-refund-handler": ("remit ar_aging customers", ["Proposes a credit memo of 500 to Ridgeway Logistics for the damaged pallet, pending approval", S["ar_credit"]], "Request: handle Ridgeway's 500 deduction. Approver for credit memos: the credit manager."),
 "customer-invoicing": ("contract customers coa", ["Drafts the September invoice to Harlow Fabrication for 2,500 under the contract", "States that revenue recognition under the contract is a separate question"], "Request: raise the September 2025 invoice under the Harlow contract. Sales tax: none on this contract."),
 "duplicate-invoice-detection": ("ap_open ap_paid vendors", [S["dup_bill"], S["vendor_dup"]], ""),
 "expense-report-processor": ("expense expense_policy coa", ["Hotel 438.00 on 5 September is claimed twice", "Meal 486.50 for two people is 243.25 a head, over the 75 limit", "Uber 38.75 has no receipt and is over 25", "Mileage cannot be valued: the rate was not supplied"], ""),
 "financial-statement-builder": ("tb tb_py coa", ["Balance sheet balances; income statement is nine months to 30 September 2025 with December 2024 as the comparative balance sheet"], ""),
 "fixed-asset-register-and-depreciation": ("fa tb gl", [S["fa_disposed"], "Register cost 420,000 agrees to account 1500", "Servers (FA-005, 2020, 5 years) are fully depreciated"], ""),
 "gl-coding-assistant": ("uncoded coa gl", ["Codes software, travel, utilities and legal lines to existing accounts with a confidence level", "Leaves 'ACH DEBIT UNKNOWN ORIG 88213' uncoded and asks"], ""),
 "inventory-to-gl-reconciliation": ("items tb moves", [f"Item listing totals {B.INV_TOTAL:,} and agrees to account 1200", S["dead_stock"]], ""),
 "invoice-data-extractor": ("invoice_pdf vendors", ["Extracts vendor Kestrel Supplies, INV-4471, 5 September 2025, net 6,000, tax 480, total 6,480, terms net 30", "Arithmetic checks: 300 x 20.00 = 6,000"], ""),
 "journal-entry-builder": ("accrual_inputs coa", ["Builds a balanced accrual entry for 11,850 to existing accounts, as a proposal", "Marks the utilities figure as an estimate"], "Request: build the September accrual entry for the three items."),
 "journal-entry-review": ("je coa", [S["je_round"], S["je_late"], S["je_blank"], "Routine close entries posted 1 to 3 October for 30 September are not flagged as back-dated"], "Approval threshold for journals: 10,000. The August books closed on 12 September 2025."),
 "merchant-and-payment-processor-rec": ("stripe_payouts stripe_tx stripe_gl bank", ["Revenue is recorded net of fees: gross sales 48,680 against 46,569 booked, so revenue and fees are both understated by 2,111", "Difference 2,111 is fees 1,431, refunds 480 and one dispute 200", "6,420 held at Stripe at month end was paid out on 3 October"], "Processor: Stripe. Sales are recorded one entry per payout. No reserve."),
 "month-end-close-checklist": ("tb tb_aug coa recurring bank", ["Software subscription recurring entry did not post in September", "Bank reconciliation, accruals and payroll clearing appear as open tasks, with owners left for the user to name"], ""),
 "payroll-clearing-reconciliation": ("payroll payroll_gl", [S["payroll_clearing"]], ""),
 "payroll-journal-entry-builder": ("payroll coa payroll_rules", ["Builds a balanced payroll entry: gross, withholdings, employer social security at 7.65%, net pay", f"Total payroll expense {B.PNL[B.I]['payroll']:,}"], ""),
 "payroll-reconciliation": ("payroll payroll_gl bank", ["Register net pay agrees to the two bank payroll debits within the 1,200 clearing residual", "Payroll tax payable 5,400 is unpaid at month end"], ""),
 "prepaid-amortization-schedule": ("prepaid prepaid_ledger tb", ["Schedule balance 18,000 (insurance 4,500, software 9,000, trade show 4,500) agrees to account 1300", "Maintenance contract ended 30 September and is fully amortised", "Trade show deposit has not started amortising", "Account 1300 rolls forward from 4,500 opening to 18,000 closing"], ""),
 "recurring-transaction-builder": ("recurring coa", ["Software subscription (3,500) did not post in September", "Other four entries posted in all three months"], ""),
 "three-way-match": ("ap_open po grn approvals", [S["short_ship"], S["price_creep"] + ": inside the 2% price tolerance but 1,566 over the 25 total tolerance, so an exception", S["no_po_approval"], S["dup_bill"], "PO-1042 and PO-1045 are services with no confirmation supplied: two-way by omission for those", "Seven bills (80,702) carry no PO and are listed as outside the match", "Bills carry no line detail, so the match is at header level"], ""),
 "vendor-statement-reconciliation": ("vendor_stmt ap_open ap_paid", ["Statement 98,983 against 95,063 open on the Kestrel Supplies record: difference 3,920 is invoice 4388 (14 August), not in the books and not in the payment history", "INV-4471 (6,480) is also open under a second vendor record, Kestrel Supplies Inc., as INV4471: a likely duplicate to review"], ""),
 # --- analysis from the books ---
 "working-capital-optimization": ("bs36 pnl36 ar_aging ap_paid items wco", [S["dso_drift"], S["early_pay"], S["dead_stock"], "Kestrel Supplies is excluded from supplier levers, per the guardrail"], ""),
 "kpi-dashboard-builder": ("pnl36 bs36 kpi", [S["margin_dip"], S["dso_drift"], "Lists operational metrics as not available: no order system data", "Shows no targets, and says none were supplied"], ""),
 "cash-flow-statement-indirect-method": ("tb tb_py pnl_ytd gl policies", ["Statement ties exactly to the change in cash between 31 December 2024 and 30 September 2025", "Depreciation 37,800 added back; loan repayments 45,000 in financing"], "Framework: US GAAP. Cash is accounts 1000, 1010 and 1050; none restricted. No acquisitions in the period."),
 "intercompany-reconciliation": ("ic_us ic_uk rates group", ["IC-097 (3,300 GBP, 29 September) is in the UK books and not in the US books", "Small rate differences on IC-071, IC-082 and IC-093 at their transaction rates", "UK receivable 33,220 GBP is 42,189.40 USD at 1.2700 against the US payable 38,000: difference 4,189.40, of which IC-097 is 4,191.00"], "Group: Northbrook Trading Ltd and Northbrook UK Ltd. Intercompany accounts: 2300 in the US books, 1300 in the UK books. Line matching uses each line's transaction rate; balances use the closing rate."),
 "bank-fee-and-interest-analysis": ("fee_ledger bank", ["Says on the face of the output that only posted fees were examined, apart from the September statement", "Wire fee is 35 a wire; September service fee on the statement is 50", "Merchant fees are the largest category"], "Products: one operating account, wires, merchant services. No fee schedule. No earnings credit rate."),
 "rolling-forecast": ("pnl36 forecast budget model_req", ["Locks actuals through September 2025", "Challenges the forecast, which applies 10% to every line, against the run-rate and seasonality", "Marks this as a first forecast if no prior forecast is treated as supplied"], "Horizon: 12 months, monthly. Last closed month: September 2025."),
 "cohort-and-unit-economics": ("ar_hist pnl36 customers", ["Builds cohorts from first invoice per customer", "Says channel data and cost-to-serve are not available", "CAC uses the marketing line as the only acquisition cost, and says so"], "Business model: transactional. Monthly cohorts over the last 12 months. A customer is lost after 90 days with no invoice. Sales and marketing = account 6200 only."),
 "fraud-detection-and-forensics": ("je ap_open vendors criteria", ["JE-0904: 50,000 round-amount revenue entry posted on a Sunday by a user who posts no other journal, with no support",  S["je_blank"], S["vendor_dup"], S["bank_change"], "Reports patterns with amounts and names no person as having committed fraud"], "This is a red-flag screen with no specific allegation. Approval limit 10,000. Output for the CFO only. Counsel not engaged."),
 "credit-limit-and-customer-risk": ("ar_hist ar_aging credit_policy", ["Harlow pays in about 88 days on average against 30-day terms", "Exposure about 248,000, of which 48,200 is 95 days overdue", "Harlow is about 31% of receivables, above the 25% policy limit", "Says no bureau report or references were supplied"], ""),
 "debt-and-covenant-tracking": ("loan debt_ledger pnl36 tb", ["Computes covenants on the agreement's definitions: adds back the 14,000 one-time fee and includes the card balance in debt", "Labels any book-only ratio as an input, not a compliance position", "Shows headroom on leverage (limit 2.50x) and interest cover (floor 4.0x)"], "Test date 30 September 2025, trailing twelve months. Single company is the whole borrowing group."),
 "scenario-and-sensitivity-analysis": ("forecast pnl36 bs36 scenario", ["Proposes ranges from 36 months of history and stops for the user to accept them before running sensitivities", "Runs the three named scenarios on a cash bridge against the 250,000 minimum cash threshold", "States each range's source"], ""),
 "audit-prep-pbc-list": ("tb tb_py pbc audit_scope", ["Maps to the auditor's eight requests and does not build a parallel list", "Marks bank statements, count sheets, minutes and contracts as documents a person must supply", "Builds the timeline back from 9 February 2026"], ""),
 "inventory-obsolescence-and-reserve": ("items moves prices tb", [S["dead_stock"], "LK-09 and PN-55 sell below cost: net realisable value write-down", "TR-07 is seasonal: checked before being flagged"], "Buckets 0-90, 91-180, 181-365, over 365 days. No reserve rates set: propose them. Weighted average cost. No damaged stock known. TR-07 is seasonal."),
 "customer-credit-and-collections-policy": ("ar_aging ar_hist customers credit_policy", ["Segments twelve customers by payment behaviour: Harlow, Tideswell and Foxhall are slow payers", "Tests a hold rule on the real base and reports how many customers it would stop", "Leaves governance roles as stated, not verified"], "Problem: slow payment. Orders can be held by the sales lead in the order system. Standard terms net 30."),
 "standard-costing-and-variance-analysis": ("standards var_hist purchases", ["Purchase price variance 27,500 unfavourable (11,000 units at 2.50 over standard)", "The variance is one-sided and growing for twelve months: the 2023 standard is stale", "Material usage variance 10,400 unfavourable ((2.1 - 2.0) x 5,200 x 20.00)", "Labour rate variance 4,992 unfavourable; efficiency 4,576 favourable (2,496 actual hours against 2,600 standard)"], ""),
 "bad-debt-and-write-offs": ("ar_aging ar_hist tb policies", ["Existing allowance 9,000 (account 1150)", "Foxhall (130 days) and Harlow INV-20418 (95 days) are specific candidates, not write-offs", "Says no historical write-off data was supplied, so rates are not derived"], "Framework: US GAAP, aged-percentage method as in the policy. No approval matrix supplied."),
 "cash-management-and-treasury": ("treasury tb cash_ledger tb_uk", ["Maps three cash accounts in the US and one in the UK", "Operating account balance exceeds the 1,000,000 single-bank limit", "Controls are described as designed, not tested"], ""),
 "internal-audit-workpaper": ("po grn ap_open vendors criteria", [S["no_po_approval"], S["short_ship"], S["bank_change"] + " with no call-back evidence supplied", "Findings are written against the purchasing policy"], "Compliance audit of purchase-to-pay."),
 "sox-controls-design-and-testing": ("controls po grn je ap_open", ["C1 exception: PO-1042 unapproved, PO-1043 received before approval", "C2 exception: PO-1041 billed for 100, received 90", "C6 exception: JE-0905 posted into closed August", "C3 and C5 leave no trace in the books: evidence needed from a person", "No severity rating is filled in"], "Objective: operating effectiveness. No materiality supplied."),
 "chart-of-accounts-designer": ("coa tb chart_req", ["Proposes a separate account for one-time professional fees for covenant reporting", "Maps every old account to a new one", "Does not remove an account that holds a balance without saying where it goes"], ""),
 # --- closes, models, FX ---
 "quarter-end-close": ("tb tb_aug je loan audit_scope", [S["je_late"], "Covenant test uses the agreement's definitions", "Board pack and lender certificate are the two obligations; no interim review steps"], "Quarter: Q3 2025, July to September."),
 "year-end-close": ("tb_py fa je audit_scope", ["Lists annual procedures with owners; counts, impairment and tax true-up are for people", "Uses the 2024 trial balance as the latest closed year and plans the 2025 close from the audit inputs"], ""),
 "budget-builder": ("pnl36 budget_req", ["Revenue built from volume +8%, price +3% and the new customer from April", "Three hires costed from their start months", "Lines with no assumption stay flat, and the output says so", "Reconciles to the 12% operating margin target"], ""),
 "three-statement-financial-model": ("pnl36 bs36 model_req loan", ["Balance check is zero in every period", "Shows measured history for each driver before using the assumption", "Debt follows the agreed 5,000 a month"], ""),
 "multicurrency-fx-revaluation": ("fx_bal rates tb", ["Tideswell receivable 18,000 GBP revalues from 22,500 to 22,860 at 1.2700: unrealised gain 360", "Intercompany payable revalues by about 2", "Asks whether the system already revalues before proposing an entry"], "Functional currency USD. US GAAP. No hedges."),
 # --- accounting standards ---
 "revenue-recognition-asc606": ("contract rev_invoices policies", ["Allocates 150,000 on standalone prices: licence 100,000, implementation 25,000, support 25,000", "Recognised to 30 September: 35,417 if implementation is distinct and the hosted licence is over time; billed 67,500; contract liability 32,083", "Asks whether implementation is distinct and whether the hosted licence is recognised over time, and shows the effect of each answer"], "Framework ASC 606. No expedients. No modifications."),
 "lease-accounting-asc842-ifrs16": ("lease tb pnl_ytd", ["Warehouse lease measured at the 6.0% rate supplied; printer lease is short-term", "Rent expense of 9,000 a month is in the books with no right-of-use asset recorded", "Renewal option: asks whether exercise is reasonably certain"], "Framework ASC 842. Lessee. Short-term expedient elected."),
 "intangibles-and-amortization": ("deal tb policies", ["Customer relationships 260,000 and trade name 90,000 from the acquisition are not in the trial balance", "Asks for useful lives; computes nothing without them"], "Framework US GAAP. No register exists."),
 "consolidation-and-eliminations": ("tb tb_uk rates group ic_us ic_uk", ["Translates the UK at closing 1.2700 and average 1.2550, share capital at 1.3100", "Eliminates the 104,800 investment against 80% of UK share capital at 1.3100 (no goodwill)", "Eliminates the intercompany balance and shows the unmatched IC-097 difference", "Non-controlling interest at 20%"], "Consolidation date 30 September 2025. US GAAP."),
 "foreign-currency-translation-asc830": ("tb_uk rates group", ["Translation adjustment proved independently: opening 6,077 debit plus this year's 3,116 (152,420 GBP x 0.017 + 35,000 GBP x 0.015) gives 2,961 debit, agreeing with the balancing figure", "Share capital translated at the historical rate 1.3100; profit at the average 1.2550"], "Period end 30 September 2025. Functional currency of the UK entity: GBP. No intercompany loans. No hyperinflation."),
 "statement-of-equity-changes": ("tb tb_py equity_ledger cap_table", ["Dividend 60,000 in March", "Unexplained 7,500 'Adjustment' posted direct to retained earnings on 30 June: listed and asked about", "Share roll-forward from the cap table: options 60,000 to 80,000"], "Corporation, US GAAP. Treasury stock: none."),
 "notes-to-financial-statements": ("tb tb_py policies notes_prior loan", ["Drafts policy, fixed asset and debt notes from the figures", "Flags contingencies and related parties as needing input", "Subsequent events window runs to 20 March 2026"], ""),
 "inventory-costing-fifo-lifo-wavg": ("purchases items policies", ["Applies weighted average as the policy states", "Says opening layers were not supplied"], "US GAAP. Perpetual. No standard costing."),
 "cost-accounting-job-order": ("jobs jobs_policy", ["Untagged direct cost 4,540 is shown apart, not spread", "J-301: materials 18,400 + labour 210 h at 46 + overhead 210 h at 28", "J-298 is closed and still shows cost in September"], ""),
 "cost-accounting-process-costing": ("production", ["Units reconcile in both departments (20,000 and 18,000)", "Mixing equivalent units: 20,000 materials and 18,200 conversion; cost per unit 6.94 and 3.83; 183,084 transferred to Filling"], "Weighted average. Materials added at the start. Normal spoilage: none."),
 "model-builder-integrated-three-statement": ("pnl36 bs36 coa model_req", ["Historical side ties to the statements, with the March dividend and June adjustment explaining the retained earnings movements", "Forecast uses only the assumptions supplied; none generated"], ""),
 "segment-reporting": ("segments pnl_ytd tb", ["Three divisions tested against the 10% thresholds; Services is below on profit", "Segment revenue reconciles to total revenue", "Central costs appear as a reconciling item"], "ASC 280. The decision maker is the CEO, who reviews the three divisions. Profit measure: operating profit before central costs."),
 # --- public reporting ---
 "sec-10q-10k-prep": ("tb tb_aug filing pnl_ytd", ["Builds the calendar back from 7 November", "Checks comparatives against the prior filing figures supplied", "Says the draft itself was not supplied, so the tie-out is books to books"], ""),
 "xbrl-tagging-checklist": ("filing tb", ["Says the filing draft and tagged file were not supplied: checklist only", "Notes six custom extensions to review", "Assigns no element names from memory"], ""),
 "management-discussion-and-analysis": ("pnl_ytd tb tb_py mda", ["Every variance is computed from the figures", "Trends section is left as questions for management", "Non-GAAP measure shown with its reconciliation"], ""),
 "restatement-and-prior-period-adjustment": ("issued je tb_py", ["Revenue 86,000 and cost 49,900 belong in 2025: 2024 income overstated by 36,100", "Sets out materiality factors against the 5% benchmark without concluding", S["je_late"]], ""),
 "subsequent-events-asc855": ("subseq tb ar_aging matters", ["Foxhall write-off (4,003) and the 52,000 settlement confirm conditions at 30 September: adjusting candidates", "Returned PN-55 panels bear on the inventory reserve", "Asks management by category for events the ledger cannot show"], "Issue date: 20 March 2026."),
 "related-party-disclosures-asc850": ("related vendors ap_paid ic_us", ["Halden Property Management (rent, 81,000 in 2025) is owned by the CEO", "Intercompany transactions with Northbrook UK", "J. Marsh became a director in June: related for part of the year"], ""),
 "contingencies-and-litigation-asc450": ("matters gl vendors", ["Customer claim: probable, range 40,000 to 70,000: accrue the low end where no amount is more likely, with the range disclosed", "Employment claim: disclose, no accrual", "Insurance recovery is not netted"], ""),
 # --- specialist technical ---
 "petty-cash-management": ("petty coa", ["Cash 182.40 + September vouchers 258.10 + IOU 30.00 = 470.50 against a 500.00 float: shortage 29.50", "Voucher 105 (2 October) was handed in after the count and belongs to October", "Voucher 102 (31.00) has no receipt and is over the 25 threshold", "The IOU is an employee advance (1160), not an expense"], "Receipt threshold 25. No shortage tolerance."),
 "benefits-and-401k-accounting": ("payroll plan_terms payroll_gl", ["Employer match equals the 4% employee contribution", "PTO accrual from the four balances supplied: 64x45 + 88x39.80 + 40x42.70 + 120x92.30", "Asks whether September contributions were remitted within 7 business days"], "US GAAP. No defined benefit plan."),
 "equity-compensation-accounting": ("cap_table tb", ["20,000 options at 1.10 = 22,000 over 48 months: 2,750 to 30 September on straight-line attribution, more on graded; asks which the company uses", "No stock compensation expense is in the trial balance"], "ASC 718. Equity-settled. Service vesting. Forfeitures as they occur."),
 "pensions-and-postretirement-asc715": ("actuarial tb", ["Funded status at 30 September: deficit 255,000 against 220,000 in the ledger", "Net periodic cost 63,400 (62,000 + 59,000 - 57,600)", "No pension entry was posted in the nine months"], ""),
 "derivatives-and-hedging-asc815": ("swap loan tb", ["Hedge documentation is dated 14 February, after the 1 January trade date", "The term loan is fixed rate, so a pay-fixed swap does not hedge it: asks", "Ledger shows 2,900 against the bank's 3,400"], ""),
 "gaap-vs-ifrs-conversion": ("tb policies lease", ["Lists differences area by area for this business and asks about each policy", "The warehouse lease changes from a single straight-line rent charge to depreciation plus interest under IFRS 16, with deferred tax on the adjustment", "Notes that no development costs appear in the data, and asks rather than assuming there are none"], "From US GAAP to IFRS, for group reporting, ongoing. No materiality supplied."),
 "crypto-and-digital-asset-accounting": ("crypto tb", ["Holds 1.6 BTC and 50,000 USDC at 30 September", "FIFO disposal of 0.4 BTC: cost 16,800, proceeds 22,800, gain 6,000", "Asks the user to confirm the standard in force; no digital asset account is in the trial balance"], "US GAAP. Held as an investment, in exchange custody. FIFO on disposals."),
 "esg-sustainability-reporting": ("esg esg_notes pnl_ytd", ["Electricity and diesel have quantities and owners; business flights have spend only and no quantity", "Uses only the sample factors supplied and labels them", "Does not claim assurance readiness"], ""),
 # --- sector ---
 "nonprofit-fund-accounting": ("npo", ["Releases 160,000 of the Harlow Foundation gift", "City grant condition met (5,400 meals): recognised, 120,000 spent", "Shared salaries and rent allocated on the staff-time split"], ""),
 "grant-accounting-nonprofit-restricted-funds": ("grants npo", ["G3 supplies overspent (14,500 against 10,000) and 3,200 is dated after the grant period", "G1 report was due 31 August 2025", "G1 is conditional and the condition is met"], ""),
 "government-fund-accounting-gasb": ("gov gov_notes", ["General fund balance classified: 200,000 committed, 50,000 assigned, remainder unassigned", "Road fund restricted", "Government-wide view adds capital assets 3,100,000, debt 900,000 and the net pension liability 640,000"], ""),
 "healthcare-revenue-cycle-accounting": ("health health_gl", ["Charity care 18,000 is recorded as bad debt against the policy", "Unapplied cash rose from 6,000 to 14,000", "Works on totals by payer class only"], ""),
 "insurance-accounting-overview": ("insure", ["Unearned premium: policy system 2,250,000 against ledger 2,180,000", "IBNR: actuary 760,000 against ledger 700,000; not re-estimated here", "48,000 of reinsurance recoverable is over 90 days"], ""),
 "real-estate-and-property-accounting": ("property", ["Unit 7 rent needs straight-lining over the lease, including the rent-free months", "6,000 of interest was capitalised on Plot 12 after work paused", "Land is not depreciated"], ""),
 "construction-percentage-of-completion": ("contracts_wip", ["C-11 is 43.1% complete: revenue to date 387,500 against 380,000 billed", "C-12 is a loss contract: estimated cost 480,000 against price 450,000; the full 30,000 loss is recognised now (25,000 margin reversal to date plus a 5,000 provision)", "Balances shown per contract, not netted: C-11 contract asset 7,500; C-12 contract liability 15,000", "C-13 has no estimate at completion: not computed"], "US GAAP. Cost-to-cost."),
 # --- released from review items ---
 "quickbooks-ar-aging-collections": ("qb_summary ar_aging customers", [S["old_ar"], S["ar_credit"] + ": checked before chasing", "Summary and detail totals agree"], "Whole ledger. No disputes. Drafts signed by the credit controller."),
 "vendor-onboarding-and-w9-tin": ("vendors pay_2025 ap_paid", [S["vendor_forms"], S["vendor_dup"], S["bank_change"] + ": verify by call-back", "Identifiers stay masked"], "Payer jurisdiction: US. Audit of the vendor master only. Output for the AP manager."),
 "restructuring-and-severance-asc420": ("restructure tb", ["Communication on 14 October is after 30 September: nothing recognised at 30 September", "Severance 37,700 and lease penalty 15,000 once the triggers are met", "No names recorded"], ""),
 "aml-kyc-procedures": ("aml", ["Says the activity is a per-customer summary, so transaction monitoring can only test what the summary shows", "C-02: owner not identified, not screened, nine payments of 9,900 in six days: referred to the officer", "C-03: declared politically exposed person: enhanced due diligence", "No screening is performed and no suspicion is decided"], ""),
 "ar-cash-application-lockbox": ("lockbox remit ar_aging cashapp_policy", ["Ridgeway short-pays by 500 with a deduction reference", "Castleton has no reference on the lockbox line; the remittance names INV-20574", "Unknown payer 4,003 is proposed against Foxhall by amount only"], ""),
 "ap-invoice-processing-and-3way-match": ("ap_open po grn vendors approvals coa", [S["short_ship"], S["dup_bill"], S["bank_change"], S["no_po_approval"]], "These are bills already entered. Run the batch."),
 # --- tax (sample rates only) ---
 "tax-planning-and-projections": ("pnl_ytd tax_rules forecast", ["Uses only the sample 20% rate supplied and quotes its source", "Safe harbour: 100% of prior-year tax 61,000 in four instalments", "Says it is not tax advice"], "Taxpayer: the company, in 'Sampleland', tax year 2025."),
 "tax-return-prep-corporate": ("tb_py tax_rules prior_return fa", ["Replaces book depreciation with 25% of cost (105,000)", "Lists candidate disallowables; none are added back without the user's schedule matching an account", "Says it is not tax advice"], "Jurisdiction 'Sampleland'."),
 "personal-tax-return-prep": ("personal payroll", ["Salary and withholding for E12 taken from the payroll register for one month only: says a full year is needed", "Dividend 48,000, interest 1,240, net rental 11,500", "Saves nothing and repeats no tax or account number"], ""),
 "corporate-tax-provision-asc740": ("tb tax_rules prior_return fa", ["Current tax at the sample 20% on adjusted income", "Temporary difference on fixed assets: book 146,600 against tax written-down value 101,600 at 31 December 2024", "Opening deferred tax liability 9,000"], "US GAAP. Period: nine months to 30 September 2025."),
 "income-tax-deferred-tax-rollforward": ("tb tax_rules prior_return fa", ["Rolls the 9,000 opening liability forward", "Fixed asset difference at the 20% enacted sample rate", "Asks for the tax depreciation schedule for 2025"], ""),
 "r-and-d-tax-credit": ("rd payroll", ["P1 presented as meeting the tests; P2 and P3 as routine work: the user decides", "P1 cost: staff time at 40% and 60%, materials 14,200, lab 8,000", "Benefit at the sample 12% only"], "Jurisdiction 'Sampleland', 2025."),
 "sales-tax-us-multistate": ("state_sales nexus", ["Ohio (310,000) and Georgia (142,000) exceed the sample thresholds and are not registered", "Oregon has no sales tax", "No nexus conclusion is drawn; states are named for review"], ""),
 "vat-gst-international": ("vat_tx vat_rules", ["Output VAT 19,600; recoverable input VAT 8,200; reverse charge 1,200 nets to nil", "Blocked 180 on entertainment is not recoverable", "Computed 11,400 payable against 11,580 in the control account: difference 180"], ""),
 "transfer-pricing-documentation": ("tp ic_us ic_uk group tb_uk", ["Goods at cost plus 8% sit inside the 5.5% to 9.5% range supplied", "Management fee has no written agreement", "No method is selected and no conclusion is drawn"], "Year 2025."),
 "payroll-tax-filings": ("payroll payroll_rules payroll_gl", ["September liability at the sample rates; September deposit is due 15 October and unpaid", "July and August deposits were on time", "Works on totals"], "Period: Q3 2025."),
 "1099-and-t4a-prep": ("pay_2025 vendors info_rules", [S["vendor_forms"], "Corporations excluded except legal services (Greyfriars is a partnership and reportable)", "Pinecrest is a foreign payee paid by card: excluded", "Says the list is preliminary: the payments cover the twelve months to September, not the calendar year", "LLC payees (Orchard, Halden, Vale) need their tax classification before they are included or excluded"], ""),
 # --- valuation and transactions ---
 "business-valuation": ("pnl36 bs36 forecast market", ["Three approaches with a range, not a single number", "Uses only the market data supplied, with sources", "Says it is analysis, not an opinion of value"], ""),
 "valuation-agent-dcf-comps-football-field": ("forecast market tb", ["WACC build shown input by input", "Terminal value shown as a share of enterprise value", "Bridge uses term loan plus card balance less cash"], ""),
 "model-auditor-financial-model-review": ("model pnl36 bs36", ["September revenue in the model is 50,000 above the books", "Model balance sheet is out by 12,000", "Issue log with a hold call"], "The model is for the lender. Whole model. Materiality 10,000."),
 "due-diligence-quality-of-earnings": ("pnl36 bs36 qoe related", ["Tests each management adjustment: legal fee one-time; trade show may recur", "Rent to the CEO's company is a related party item", "Says this is statement-level work without the ledger"], "Buy-side. Twelve months to 30 September 2025."),
 "business-combinations-asc805": ("deal", ["Net identifiable assets at fair value 830,000; consideration 1,580,000; goodwill 750,000", "Deal costs 46,000 are expensed", "Earnout 180,000 is a liability"], ""),
 "goodwill-and-impairment-testing": ("impair deal", ["Loss of a major customer is a triggering event", "Value from the projections at 10.5% is above the 1,620,000 carrying amount: no impairment indicated, with sensitivity shown", "Concludes nothing"], ""),
 "ipo-readiness-accounting": ("close_cal ipo cap_table", ["Close takes 9 to 12 working days", "About 70% of journals are manual", "Periods were reopened in June and August", "2022 is not audited"], ""),
}


def manifest(skill):
    keys, expect, extra = C[skill]
    keys = keys.split()
    first = keys[0]
    if first in ("tb", "tb_aug", "tb_py"):
        neg, why = ("wrong_company", "It is a trial balance for a different company (Harlow Fabrication Ltd). Reject it.") if skill in TB_FIRST_COMPANY else \
                   ("wrong_period", "It is the right kind of document for the wrong period (30 September 2024). Reject it.")
        negname = F[neg][0]
    else:
        neg = "wrong_rota"
        stem, ext = os.path.splitext(F[first][0])
        negname = f"{stem}_final.csv"
        why = f"The name suggests it is '{F[first][1]}'. The content is a staff rota. Reject it on content, not on name."
    return dict(
        skill=skill, company=ENTITY.get(skill, (B.CO,))[0], period=ENTITY.get(skill, (0, B.PERIOD))[1],
        how="Upload path only. Give the intake answers, upload every file in this folder, and check the result against 'expect'.",
        intake_answers=(std(skill) + (" " + extra if extra else "")).strip(),
        inputs=[dict(file=F[k][0], is_=F[k][1]) for k in keys],
        negative=[dict(file=negname, is_=F[neg][1], why=why)],
        expect=dict(
            validation=["Shows one validation table before any work, with a verdict per file",
                        "Accepts every file listed under inputs" + (", noting any that only partly covers a required upload" if len(keys) < 2 else ""),
                        f"Rejects {negname}: {why}", "Lists any required upload that is still missing, and waits for an answer"],
            findings=expect,
            read_only=["Posts, sends, pays and files nothing", "Presents every entry as a proposal"])), keys, neg, negname


def readme(m):
    out = [f"# Sample data — {m['skill']}", "", "Test inputs for the upload path. Fictitious company and figures. Generated by `.github/samples/build.py`; do not edit here.", "",
           "## How to test", "", "1. Start the skill with no Mosofin connection (or answer \"upload\" at intake).", f"2. Give these intake answers: {m['intake_answers']}",
           "3. Upload every file in this folder, including the wrong one.", "4. Check the validation step, then the findings, against the lists below.", "", "## Files", "", "| File | What it is |", "|---|---|"]
    out += [f"| `{i['file']}` | {i['is_']} |" for i in m["inputs"]]
    out += [f"| `{n['file']}` | **Deliberately wrong.** {n['why']} |" for n in m["negative"]]
    out += ["", "## Expected", "", "**Validation step**", ""] + [f"- {x}" for x in m["expect"]["validation"]]
    out += ["", "**Findings**", ""] + [f"- {x}" for x in m["expect"]["findings"]]
    out += ["", "**Read-only**", ""] + [f"- {x}" for x in m["expect"]["read_only"]]
    return "\n".join(out) + "\n"


def main():
    check = "--check" in sys.argv
    skills = sorted(d for d in os.listdir(os.path.join(ROOT, "skills")) if os.path.isfile(os.path.join(ROOT, "skills", d, "SKILL.md")))
    missing = [s for s in skills if s not in C]; extra = [s for s in C if s not in skills]
    if missing or extra:
        sys.exit(f"catalogue mismatch — no entry for: {missing}; unknown: {extra}")
    drift = n = 0
    for s in skills:
        m, keys, neg, negname = manifest(s)
        d = os.path.join(ROOT, "skills", s, "samples")
        want = {F[k][0]: F[k][2] for k in keys}
        want[negname] = F[neg][2]
        want["manifest.json"] = json.dumps(m, indent=1, ensure_ascii=False).replace('"is_"', '"is"') + "\n"
        want["README.md"] = readme(m)
        if check:
            for name, content in want.items():
                p = os.path.join(d, name)
                if not os.path.exists(p) or open(p).read() != content: drift += 1
            continue
        os.makedirs(d, exist_ok=True)
        for old in os.listdir(d):
            if old not in want: os.remove(os.path.join(d, old))
        for name, content in want.items():
            open(os.path.join(d, name), "w").write(content); n += 1
    if check:
        print(f"samples: {len(skills)} skills, {drift} file(s) out of date"); sys.exit(1 if drift else 0)
    print(f"samples: wrote {n} files into {len(skills)} skill folders")


if __name__ == "__main__":
    main()
