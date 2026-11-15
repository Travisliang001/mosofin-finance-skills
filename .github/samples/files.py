"""Every sample file, by key: (file name, what it is, content). Built from base.py."""
import base as B

def csv(header, rows):
    q = lambda v: '"%s"' % v if isinstance(v, str) and ("," in v) else str(v)
    return "\n".join([",".join(header)] + [",".join(q(v) for v in r) for r in rows]) + "\n"

def doc(title, body):
    return f"# {title}\n\n*Sample document for testing. Fictitious company and figures.*\n\n{body.strip()}\n"

F = {}
def add(key, name, what, content): F[key] = (name, what, content)

I, co = B.I, B.CO
def tbcsv(i): return csv(["account", "name", "debit", "credit"], B.tb(i))

# ---- ledgers and statements ----------------------------------------------------------
add("coa", "chart_of_accounts.csv", "Chart of accounts", csv(["account", "name", "type"], B.COA))
add("tb", "trial_balance_2025-09-30.csv", f"Trial balance of {co} at 30 September 2025", tbcsv(I))
add("tb_aug", "trial_balance_2025-08-31.csv", f"Trial balance of {co} at 31 August 2025", tbcsv(I - 1))
add("tb_py", "trial_balance_2024-12-31.csv", f"Trial balance of {co} at 31 December 2024", tbcsv(26))
add("pnl36", "monthly_profit_and_loss_36m.csv", "Monthly profit and loss by line, October 2022 to September 2025",
    csv(["month"] + B.PL_LINES + ["net_income"], [[p["month"]] + [p[k] for k in B.PL_LINES] + [p["net_income"]] for p in B.PNL]))
_bsk = ["cash", "ar", "inventory", "prepaid", "fixed_assets_net", "ap", "accrued", "debt", "share_capital", "retained_earnings"]
add("bs36", "monthly_balance_sheet_36m.csv", "Balance sheet at each month end, October 2022 to September 2025",
    csv(["month"] + _bsk, [[b["month"]] + [b[k] for k in _bsk] for b in B.BS]))
add("pnl_ytd", "profit_and_loss_2025_ytd.csv", "Profit and loss by month, January to September 2025",
    csv(["month"] + B.PL_LINES + ["net_income"], [[p["month"]] + [p[k] for k in B.PL_LINES] + [p["net_income"]] for p in B.PNL[27:]]))
add("budget", "budget_2025.csv", "Approved 2025 budget by month and line",
    csv(["month"] + B.PL_LINES, [[p["month"]] + [round(p[k] * (1.03 if k == "revenue" else 0.98 if k == "cogs" else 1)) if k != "marketing"
                                                 else round(p["revenue"] * 0.04) for k in B.PL_LINES] for p in B.PNL[27:]]))
add("je", "journal_entries_2025-09.csv", "Journal entries for September 2025, with user and posting date",
    csv(["je_no", "date", "posted_on", "user", "account", "debit", "credit", "memo"], B.JE))
add("gl", "general_ledger_2025-09.csv", "General ledger detail for September 2025: cash postings and journals",
    csv(["date", "source", "account", "name", "debit", "credit", "memo"],
        [(d, "bank", "1000", "Operating Bank Account", max(a, 0), max(-a, 0), t) for d, t, a in B.CASH_LEDGER] +
        [(d, j, a, B.NAME[a], dr, cr, m) for j, d, _, _, a, dr, cr, m in B.JE]))
add("forecast", "forecast_2025-10_to_2026-09.csv", "Management forecast for the next twelve months, by line",
    csv(["month"] + B.PL_LINES, [[f"{2025 + (9 + k) // 12}-{(9 + k) % 12 + 1:02d}"] + [round(B.PNL[24 + k][x] * 1.1) for x in B.PL_LINES] for k in range(12)]))

# ---- receivables -----------------------------------------------------------------------
add("ar_aging", "ar_aging_detail_2025-09-30.csv", "Open receivables by invoice at 30 September 2025",
    csv(["customer", "invoice", "invoice_date", "due_date", "amount", "days_overdue"], B.AR_OPEN))
add("ar_hist", "customer_payment_history_12m.csv", "Paid invoices with payment dates, last twelve months",
    csv(["customer", "invoice", "invoice_date", "paid_date", "amount", "days_to_pay"], B.AR_HIST))
add("customers", "customer_list.csv", "Customer list with terms and contact",
    csv(["customer", "terms_days", "credit_limit", "contact_email"], [(c, 30, [200000, 150000, 120000, 90000][k % 4], f"ap@{c.split()[0].lower()}.example") for k, c in enumerate(B.CUSTOMERS)]))
add("qb_summary", "AR_Aging_Summary_QuickBooks.csv", "QuickBooks A/R Aging Summary at 30 September 2025",
    csv(["Customer", "Current", "1 - 30", "31 - 60", "61 - 90", "91 and over", "Total"],
        [(c, *[sum(r[4] for r in B.AR_OPEN if r[0] == c and lo <= r[5] <= hi and (r[5] > 0 or lo == 0)) for lo, hi in ((0, 0), (1, 30), (31, 60), (61, 90), (91, 999))],
          sum(r[4] for r in B.AR_OPEN if r[0] == c)) for c in B.CUSTOMERS]))
add("lockbox", "lockbox_2025-09-22_to_26.csv", "Bank lockbox file: receipts 22 to 26 September 2025",
    csv(["date", "payer_name", "reference", "amount"], [("2025-09-22", "PENNINE RETAIL GRP", "INV-20537", 112071), ("2025-09-23", "CASTLETON FOODS LTD", "", 88056),
        ("2025-09-24", "RIDGEWAY LOG", "INV-20611", 71546), ("2025-09-25", "ASHBY ENG", "INV20685", 56036), ("2025-09-26", "UNKNOWN PAYER 4471", "", 4003)]))
add("remit", "remittance_advice.txt", "Remittance advice received with the lockbox payments",
    "Ridgeway Logistics remittance 24 Sep 2025: paying INV-20611 less 500.00 deduction for damaged pallet (their ref DM-118).\nCastleton Foods remittance 23 Sep 2025: paying INV-20574 in full.\n")

# ---- payables, purchasing -----------------------------------------------------------------
add("ap_open", "open_bills_2025-09-30.csv", "Open payables by bill at 30 September 2025",
    csv(["vendor", "bill_no", "bill_date", "due_date", "amount", "po", "status"], B.BILLS))
add("ap_paid", "bill_payment_history_12m.csv", "Bills paid, with due and paid dates, last twelve months",
    csv(["vendor", "bill_no", "bill_date", "due_date", "paid_date", "amount"], B.AP_PAID))
add("po", "purchase_orders.csv", "Purchase orders with lines and approval",
    csv(["po", "vendor", "item", "qty", "unit_price", "approved_by", "approved_on"], B.PO))
add("grn", "goods_receipts.csv", "Goods receipt notes", csv(["grn", "po", "received_on", "qty_received", "condition"], B.GRN))
add("vendors", "vendor_master.csv", "Vendor master with terms, tax form status and bank change date",
    csv(["vendor", "terms_days", "tax_form_on_file", "entity_type", "bank_details_changed_on", "paid_2025", "tax_id_masked"],
        [(*v, f"**-***{1000 + 37 * k}") for k, v in enumerate(B.VENDORS)]))
add("pay_2025", "payments_by_vendor_2025.csv", "Total paid to each vendor in 2025, by payment method",
    csv(["vendor", "entity_type", "method", "paid_2025"], [(v[0], v[3], "card" if v[0].startswith("Pinecrest") else "ach", v[5]) for v in B.VENDORS]))
_kb = next(b for b in B.BILLS if b[5] == "PO-1040")
add("vendor_stmt", "kestrel_supplies_statement_2025-09.txt", "Statement from the vendor Kestrel Supplies at 30 September 2025",
    f"KESTREL SUPPLIES — STATEMENT OF ACCOUNT\nCustomer: {co}\nAs at 30 September 2025\n\nInvoice    Date        Amount\n4502       2025-09-03  {_kb[4]:,}.00\nINV-4471   2025-09-05  6,480.00\n4388       2025-08-14  3,920.00\n\nBalance due: {_kb[4] + 6480 + 3920:,}.00\n")
add("invoice_pdf", "invoice_kestrel_INV-4471.txt", "A supplier invoice as received (text of the PDF)",
    f"KESTREL SUPPLIES\nINVOICE INV-4471        Date: 5 September 2025     Terms: Net 30\nBill to: {co}\n\nQty  Item                 Unit     Amount\n300  Steel bracket SB-20  20.00   6,000.00\n\nSubtotal 6,000.00\nSales tax 8% 480.00\nTOTAL DUE 6,480.00 USD\nRemit to: account ending 4471\n")
add("uncoded", "uncoded_transactions.csv", "Bank and card transactions not yet coded to an account",
    csv(["date", "description", "amount"], [("2025-09-04", "ADOBE *CREATIVE CLOUD", -89.99), ("2025-09-09", "DELTA AIR 0062341", -612.40), ("2025-09-11", "NORTHGATE UTILITIES", -1840.00),
        ("2025-09-18", "AMZN MKTP US*2K4", -214.75), ("2025-09-24", "ACH DEBIT UNKNOWN ORIG 88213", -1240.00), ("2025-09-27", "GREYFRIARS LEGAL RETAINER", -5000.00)]))

# ---- bank, cards, processors ---------------------------------------------------------------
_run, _rows = B.BANK_OPEN, []
for d, t, a in B.BANK:
    _run += a; _rows.append((d, t, a, _run))
add("bank", "bank_statement_2025-09.csv", f"Bank statement, operating account, September 2025 (opening {B.BANK_OPEN:,}, closing {B.BANK_CLOSE:,})",
    csv(["date", "description", "amount", "balance"], [("2025-09-01", "OPENING BALANCE", 0, B.BANK_OPEN)] + _rows))
add("cash_ledger", "cash_account_ledger_2025-09.csv", f"Ledger for account 1000 Operating Bank Account, September 2025 (closing {B.CASH_GL:,})",
    csv(["date", "description", "amount"], [("2025-09-01", "Opening balance", B.CASH_LEDGER_OPEN)] + B.CASH_LEDGER))
_card = [("2025-09-03", "DELTA AIR 0062341", 612.40), ("2025-09-05", "HILTON GARDEN INN", 438.00), ("2025-09-05", "HILTON GARDEN INN", 438.00), ("2025-09-09", "ADOBE *CREATIVE CLOUD", 89.99),
         ("2025-09-12", "STAPLES 00412", 156.20), ("2025-09-16", "THE CAPITAL GRILLE", 486.50), ("2025-09-21", "UBER *TRIP", 38.75), ("2025-09-25", "AMZN MKTP US*2K4", 214.75), ("2025-09-28", "LATE FEE", 39.00)]
add("card", "corporate_card_statement_2025-09.csv", "Corporate card statement, September 2025", csv(["date", "merchant", "amount"], _card))
add("card_ledger", "card_account_ledger_2025-09.csv", "Ledger for account 2050 Corporate Card Payable, September 2025",
    csv(["date", "description", "amount", "receipt"], [(d, m, a, "yes" if k % 3 else "no") for k, (d, m, a) in enumerate(_card) if m != "LATE FEE" and k != 2]))
add("expense", "expense_report_E04_2025-09.csv", "Expense report submitted by employee E04 for September 2025",
    csv(["date", "category", "merchant", "amount", "receipt", "business_purpose"], [("2025-09-03", "Airfare", "Delta", 612.40, "yes", "Client visit Castleton"),
        ("2025-09-05", "Hotel", "Hilton Garden Inn", 438.00, "yes", "Client visit Castleton"), ("2025-09-05", "Hotel", "Hilton Garden Inn", 438.00, "yes", "Client visit Castleton"),
        ("2025-09-16", "Meals", "The Capital Grille", 486.50, "yes", "Dinner, 2 people"), ("2025-09-21", "Ground transport", "Uber", 38.75, "no", ""), ("2025-09-22", "Mileage", "", 142.00, "no", "220 miles")]))
add("expense_policy", "expense_policy.md", "Expense policy", doc("Expense policy", "- Receipts required for any item over 25.\n- Meals: up to 75 per person.\n- Hotel: up to 250 per night.\n- Mileage: at the rate finance publishes each year (ask finance).\n- Claims need a business purpose."))
add("stripe_payouts", "stripe_payouts_2025-09.csv", "Stripe payout report, September 2025",
    csv(["payout_date", "gross", "fees", "refunds", "chargebacks", "net_payout"], [("2025-09-05", 19720, -578, -300, 0, 18842), ("2025-09-19", 22340, -653, -180, -200, 21307), ("2025-10-03", 6620, -200, 0, 0, 6420)]))
add("stripe_tx", "stripe_balance_transactions_2025-09.csv", "Stripe balance transactions, September 2025",
    csv(["date", "type", "amount", "fee", "net"], [("2025-09-02", "charge", 9800, -287, 9513), ("2025-09-03", "charge", 9920, -291, 9629), ("2025-09-04", "refund", -300, 0, -300),
        ("2025-09-12", "charge", 11200, -327, 10873), ("2025-09-16", "charge", 11140, -326, 10814), ("2025-09-17", "refund", -180, 0, -180), ("2025-09-18", "dispute", -200, 0, -200),
        ("2025-09-29", "charge", 6620, -200, 6420)]))
add("stripe_gl", "stripe_gl_detail_2025-09.csv", "Ledger detail for Stripe clearing, revenue and fee accounts, September 2025",
    csv(["date", "account", "name", "debit", "credit", "memo"], [("2025-09-05", "1000", "Operating Bank Account", 18842, 0, "Stripe payout"), ("2025-09-05", "4000", "Sales Revenue", 0, 18842, "Stripe payout"),
        ("2025-09-19", "1000", "Operating Bank Account", 21307, 0, "Stripe payout"), ("2025-09-19", "4000", "Sales Revenue", 0, 21307, "Stripe payout"),
        ("2025-09-30", "1050", "Stripe Clearing", 6420, 0, "Balance held at Stripe"), ("2025-09-30", "4000", "Sales Revenue", 0, 6420, "Balance held at Stripe")]))
add("fee_ledger", "bank_fee_and_interest_ledger_13m.csv", "Ledger for bank fees and interest, September 2024 to September 2025",
    csv(["month", "type", "count", "amount"], [r for k in range(23, 36) for r in ((B.ym(k), "Monthly service fee", 1, 50), (B.ym(k), "Wire fee", 2 + k % 3, 35 * (2 + k % 3)),
        (B.ym(k), "Merchant fees", 0, round(B.PNL[k]["revenue"] * 0.004) - 50 - 35 * (2 + k % 3)), (B.ym(k), "Interest expense", 1, 1900))]))
add("petty", "petty_cash_count_and_vouchers.md", "Petty cash count and voucher list, head office float",
    doc("Petty cash — count at 30 September 2025", "Authorised float: 500.00\nCash counted by the office manager on 30 September 2025: 182.40\n\n| Voucher | Date | Paid to | Amount | Receipt |\n|---|---|---|---:|---|\n| 101 | 2025-09-03 | Post office | 42.60 | yes |\n| 102 | 2025-09-09 | Taxi | 31.00 | no |\n| 103 | 2025-09-12 | Cleaning supplies | 88.50 | yes |\n| 104 | 2025-09-18 | Staff lunch | 96.00 | yes |\n| 105 | 2025-10-02 | Stationery | 24.50 | yes |\n| IOU | 2025-09-25 | E08 advance | 30.00 | — |"))

# ---- payroll, inventory, assets, schedules -----------------------------------------------------
add("payroll", "payroll_register_2025-09.csv", "Payroll register for September 2025",
    csv(["employee", "department", "gross", "income_tax_withheld", "social_security_withheld", "retirement_401k", "net_pay"], [(e, d, g, t, s, k, g - t - s - k) for e, d, g, t, s, k in B.PAYROLL]))
_g = sum(p[2] for p in B.PAYROLL); _net = sum(p[2] - p[3] - p[4] - p[5] for p in B.PAYROLL)
add("payroll_gl", "payroll_gl_detail_2025-09.csv", "Ledger detail for payroll accounts, September 2025",
    csv(["date", "account", "name", "debit", "credit", "memo"], [("2025-09-30", "6000", "Payroll Expense", B.PNL[I]["payroll"], 0, "September payroll incl. employer tax"),
        ("2025-09-30", "2150", "Payroll Clearing", 0, _net + 1200, "Net pay"), ("2025-09-12", "2150", "Payroll Clearing", _net // 2, 0, "Payroll run 1"),
        ("2025-09-26", "2150", "Payroll Clearing", _net - _net // 2, 0, "Payroll run 2"), ("2025-09-30", "2160", "Payroll Tax Payable", 0, 5400, "Taxes withheld and employer share, unpaid")]))
add("plan_terms", "benefit_plan_terms.md", "Summary of the retirement plan and paid-time-off policy",
    doc("Benefit plan terms", "**401(k):** employees contribute 4% of gross; employer matches 100% of the first 4%. Match vests over three years (33% a year).\n**Remittance:** employee contributions are due to the plan within 7 business days of each pay date.\n**Paid time off:** 15 days a year, accrued monthly, carried forward up to 5 days, paid out on leaving.\n\n| Employee | PTO hours accrued and unused at 30 Sep 2025 | Hourly rate |\n|---|---:|---:|\n| E01 | 64 | 45.00 |\n| E04 | 88 | 39.80 |\n| E06 | 40 | 42.70 |\n| E12 | 120 | 92.30 |"))
add("items", "inventory_listing_2025-09-30.csv", "Inventory by item at 30 September 2025, with last sale date",
    csv(["sku", "description", "qty_on_hand", "unit_cost", "value", "last_sale_date"], [(s, d, round(v / (20 + 3 * k)), 20 + 3 * k, v, ls) for k, ((s, d, _, ls), v) in enumerate(zip(B.ITEMS, B._iv))]))
add("moves", "inventory_movement_12m.csv", "Units sold by item by month, last twelve months",
    csv(["month", "sku", "units_sold"], [(B.ym(k), s, 0 if ls < f"{B.ym(k)}-01" else 40 + 7 * j + k % 5) for k in range(24, 36) for j, (s, _, _, ls) in enumerate(B.ITEMS)]))
add("prices", "selling_prices.csv", "Recent selling price by item", csv(["sku", "recent_selling_price"], [(s, round((20 + 3 * k) * (0.6 if s in ("LK-09", "PN-55") else 1.45), 2)) for k, (s, _, _, _) in enumerate(B.ITEMS)]))
add("purchases", "inventory_purchases_2025-09.csv", "Inventory purchases by item, September 2025",
    csv(["date", "sku", "qty", "unit_cost"], [("2025-09-04", "SB-20", 4000, 22.15), ("2025-09-07", "C-12", 90, 26.00), ("2025-09-15", "SB-20", 1500, 23.40), ("2025-09-21", "FX-01", 600, 35.00)]))
add("fa", "fixed_asset_register.csv", "Fixed asset register", csv(["asset", "description", "in_service", "cost", "useful_life_years"], B.FA))
add("prepaid", "prepaid_schedule.csv", "Prepaid expenses schedule at 30 September 2025",
    csv(["item", "vendor", "paid_on", "amount", "covers_from", "covers_to"], [("Insurance", "Calder Mutual", "2025-01-02", 18000, "2025-01-01", "2025-12-31"),
        ("Software licence", "Pinecrest Software", "2025-07-01", 12000, "2025-07-01", "2026-06-30"), ("Trade show deposit", "ExpoWest", "2025-08-15", 4500, "2025-11-10", "2025-11-12"),
        ("Maintenance contract", "Orchard Packaging", "2024-10-01", 6000, "2024-10-01", "2025-09-30")]))
add("recurring", "recurring_entries.csv", "Recurring entries that should post each month, with what posted in September 2025",
    csv(["entry", "amount", "day", "posted_2025-07", "posted_2025-08", "posted_2025-09"], [("Rent", 9000, 1, "yes", "yes", "yes"), ("Depreciation", 4200, 30, "yes", "yes", "yes"),
        ("Insurance release", 1500, 30, "yes", "yes", "yes"), ("Loan interest", 1900, 30, "yes", "yes", "yes"), ("Software subscription", 3500, 5, "yes", "yes", "no")]))
add("accrual_inputs", "accrual_candidates_2025-09.csv", "Goods and services received by 30 September 2025 and not yet billed",
    csv(["vendor", "description", "received_on", "estimated_amount", "evidence"], [("Summit Freight", "Freight, last week of September", "2025-09-30", 5800, "delivery log"),
        ("Greyfriars Legal LLP", "Contract review, September", "2025-09-26", 4200, "engagement letter rate"), ("Northgate Utilities", "Electricity, September", "2025-09-30", 1850, "prior three months average")]))

# ---- group, currency -----------------------------------------------------------------------------
add("ic_us", "intercompany_ledger_northbrook_trading.csv", f"Intercompany ledger in the books of {co}: balance with Northbrook UK Ltd (USD)",
    csv(["date", "reference", "description", "amount_usd"], [("2025-07-10", "IC-071", "Management fee from UK", -12000), ("2025-08-12", "IC-082", "Goods shipped by UK", -18500),
        ("2025-09-18", "IC-093", "Goods shipped by UK", -7500)]))
add("ic_uk", "intercompany_ledger_northbrook_uk.csv", "Intercompany ledger in the books of Northbrook UK Ltd: balance with Northbrook Trading Ltd (GBP)",
    csv(["date", "reference", "description", "amount_gbp"], [("2025-07-10", "IC-071", "Management fee to US", 9450), ("2025-08-12", "IC-082", "Goods shipped to US", 14570),
        ("2025-09-18", "IC-093", "Goods shipped to US", 5900), ("2025-09-29", "IC-097", "Goods shipped to US", 3300)]))
add("tb_uk", "trial_balance_northbrook_uk_2025-09-30.csv", "Trial balance of Northbrook UK Ltd at 30 September 2025 (GBP)",
    csv(["account", "name", "debit", "credit"], [("1000", "Bank", 84200, 0), ("1100", "Accounts Receivable", 61300, 0), ("1300", "Intercompany Receivable - Northbrook Trading", 33220, 0),
        ("1200", "Inventory", 47800, 0), ("2000", "Accounts Payable", 0, 39100), ("3000", "Share Capital", 0, 100000), ("3100", "Retained Earnings", 0, 52420),
        ("4000", "Sales Revenue", 0, 412000), ("5000", "Cost of Goods Sold", 251000, 0), ("6000", "Operating Expenses", 126000, 0)]))
add("rates", "fx_rates.csv", "Exchange rates supplied by the user (source: the company's bank)",
    csv(["pair", "rate_type", "date", "rate", "source"], [("GBP/USD", "closing", "2025-09-30", 1.2700, "bank rate sheet"), ("GBP/USD", "average", "2025-01-01 to 2025-09-30", 1.2550, "bank rate sheet"),
        ("GBP/USD", "historical (equity)", "2019-03-01", 1.3100, "bank rate sheet"), ("GBP/USD", "transaction", "2025-08-12", 1.2700, "bank rate sheet"), ("GBP/USD", "transaction", "2025-07-10", 1.2698, "bank rate sheet")]))
add("fx_bal", "foreign_currency_balances_2025-09-30.csv", "Foreign-currency balances at 30 September 2025",
    csv(["account", "counterparty", "currency", "foreign_amount", "booked_usd", "booked_rate"], [("2300", "Northbrook UK Ltd", "GBP", -29920, -38000, 1.2701), ("1100", "Tideswell Hotels (GBP invoice)", "GBP", 18000, 22500, 1.2500)]))
add("group", "group_structure.md", "Group structure", doc("Group structure", "- **Northbrook Trading Ltd** (USA, USD): parent.\n- **Northbrook UK Ltd** (England, GBP): 80% owned since 1 March 2019. Functional currency GBP.\n- Presentation currency: USD.\n- No acquisitions or disposals in 2025."))

# ---- debt, equity, leases, contracts ---------------------------------------------------------------
add("loan", "term_loan_agreement_summary.md", "Summary of the term loan agreement, with covenant definitions",
    doc("Term loan — summary of terms", "Lender: Calder Bank. Original principal 580,000. Repayment 5,000 a month plus interest. Rate: fixed 5.7%. Matures 31 December 2029.\n\n**Covenants, tested quarterly on the trailing twelve months:**\n1. *Leverage*: Total Debt / Covenant EBITDA not above 2.50x.\n2. *Interest cover*: Covenant EBITDA / Interest Expense not below 4.0x.\n\n**Definitions.** *Covenant EBITDA* = net income + interest + depreciation, **plus** one-time professional fees up to 15,000 a year, **less** any gain on asset sales. *Total Debt* = term loan + corporate card balance + any lease liabilities.\nCompliance certificate due 45 days after each quarter end."))
add("debt_ledger", "term_loan_ledger_2025.csv", "Ledger for account 2500 Term Loan, 2025",
    csv(["date", "description", "amount"], [(B.eom(k), d, a) for k in range(27, 36) for d, a in (("Principal repayment", 5000), ("Interest charged", -1900), ("Interest paid", 1900))]))
add("equity_ledger", "equity_accounts_ledger_2025.csv", "Ledger for the equity accounts, January to September 2025",
    csv(["date", "account", "description", "amount"], [("2025-01-01", "3100", "Opening retained earnings", -B.BS[26]["retained_earnings"]), ("2025-03-31", "3100", "Dividend declared and paid", 60000),
        ("2025-06-30", "3100", "Adjustment", 7500), ("2025-01-01", "3000", "Opening share capital", -250000)]))
add("cap_table", "cap_table.csv", "Cap table with 2025 movements and option grants",
    csv(["holder", "class", "shares_opening", "movement_2025", "shares_closing", "note"], [("Founders", "Common", 800000, 0, 800000, ""), ("Investor A", "Common", 200000, 0, 200000, ""),
        ("Option pool", "Options", 60000, 20000, 80000, "20,000 granted 1 Apr 2025, strike 2.50, 4-year monthly vesting, grant-date fair value 1.10 per option (independent valuation, 15 Mar 2025)")]))
add("lease", "lease_terms.md", "Key terms of two property leases",
    doc("Lease terms", "| Lease | Start | Term | Payment | Escalation | Option |\n|---|---|---|---|---|---|\n| Warehouse, Unit 4 | 2024-01-01 | 5 years | 9,000 a month, in advance | 3% each January | One 3-year renewal at market rent |\n| Office printer | 2025-03-01 | 12 months | 180 a month | none | none |\n\nDiscount rate supplied by the company: 6.0% (incremental borrowing rate, from the lender's indicative quote dated 12 December 2023).\nNo initial direct costs. No incentives."))
add("contract", "contract_harlow_fabrication.md", "Customer contract with Harlow Fabrication Ltd",
    doc("Supply and services agreement — Harlow Fabrication Ltd", "Signed 1 July 2025. Term 36 months from 1 July 2025.\n\n| Deliverable | Price |\n|---|---:|\n| Software licence (hosted, access for the term) | 108,000 |\n| Implementation (completed 31 August 2025) | 24,000 |\n| Support, 36 months | 18,000 |\n| **Total** | **150,000** |\n\nBilling: 60,000 on signing, then 2,500 a month from August 2025. No right of return. No variable amounts.\nStandalone selling prices from the company's price list: licence 120,000; implementation 30,000; support 30,000."))

# ---- costing ------------------------------------------------------------------------------------------
add("jobs", "job_costs_2025-09.csv", "Costs by job, September 2025 (jobs tagged as projects)",
    csv(["job", "customer", "status", "cost_type", "amount", "labour_hours"], [("J-301", "Ashby Engineering", "open", "materials", 18400, 0), ("J-301", "Ashby Engineering", "open", "labour", 0, 210),
        ("J-302", "Tideswell Hotels", "open", "materials", 9200, 0), ("J-302", "Tideswell Hotels", "open", "labour", 0, 96), ("J-298", "Brecon Outdoor", "closed", "materials", 3100, 0),
        ("(untagged)", "", "", "materials", 2640, 0), ("(untagged)", "", "", "subcontractor", 1900, 0)]))
add("jobs_policy", "job_costing_policy.md", "Job costing policy", doc("Job costing policy", "- Jobs are tagged in the books as projects.\n- Overhead pool: rent, depreciation and software.\n- Overhead is applied on direct labour hours at a predetermined rate of 28.00 an hour (set January 2025 from the budget).\n- Labour rate for costing: 46.00 an hour.\n- J-301 contract price 60,000; J-302 contract price 31,000; J-298 was invoiced 9,800 and closed in August."))
add("contracts_wip", "construction_contracts_2025-09.csv", "Contracts in progress: price, costs, billings and estimate at completion",
    csv(["contract", "customer", "contract_price", "costs_to_date", "estimated_total_cost", "estimate_updated_on", "billed_to_date"], [("C-11", "Elmfield Schools", 900000, 310000, 720000, "2025-09-25", 380000),
        ("C-12", "Tideswell Hotels", 450000, 400000, 480000, "2025-09-25", 390000), ("C-13", "Dunmore Medical", 260000, 52000, "", "", 40000)]))
add("production", "production_report_2025-09.csv", "Production report by department, September 2025",
    csv(["department", "units_opening_wip", "opening_pct_complete", "units_started", "units_completed", "units_closing_wip", "closing_pct_complete", "materials_added", "conversion_added", "opening_wip_cost"],
        [("Mixing", 2000, 50, 18000, 17000, 3000, 40, 126000, 68000, 14500), ("Filling", 1000, 60, 17000, 16500, 1500, 30, 33000, 52800, 9900)]))
add("standards", "standard_costs.csv", "Standard costs with effective dates, and September 2025 actuals",
    csv(["item", "standard", "standard_set_on", "actual_2025-09", "unit"], [("Steel bracket SB-20 purchase price", 20.00, "2023-08-01", 22.50, "per unit"), ("Material usage per finished unit", 2.0, "2023-08-01", 2.1, "units"),
        ("Labour rate", 44.00, "2024-01-01", 46.00, "per hour"), ("Labour hours per finished unit", 0.50, "2024-01-01", 0.48, "hours"), ("Units produced", "", "", 5200, "units"), ("Units purchased", "", "", 11000, "units")]))
add("var_hist", "variance_account_history.csv", "Monthly balance posted to the purchase price variance account, last twelve months",
    csv(["month", "purchase_price_variance"], [(B.ym(k), 9000 + 900 * (k - 24)) for k in range(24, 36)]))

# ---- tax (all rates fictitious, for testing only) ------------------------------------------------------
_T = "**SAMPLE RATES FOR TESTING ONLY — fictitious, not real tax law.** Source to quote back: 'sample rate card v1, tax year 2025'.\n\n"
add("tax_rules", "tax_rates_and_rules_SAMPLE.md", "Tax rates and rules supplied by the user for the test (fictitious)",
    doc("Tax rates and rules (sample)", _T + "- Jurisdiction: 'Sampleland'. Tax year: calendar 2025.\n- Corporate income tax: 20% flat.\n- Disallowed: fines 100%; client entertainment 50%; donations above 10,000.\n- Tax depreciation: 25% straight line on cost, in place of book depreciation.\n- Losses: carried forward without limit. Brought forward at 1 Jan 2025: nil.\n- Estimated payments: four equal instalments; safe harbour is 100% of prior-year tax (prior-year tax: 61,000).\n- Enacted future rate for deferred tax: 20%."))
add("prior_return", "prior_year_tax_computation_summary.md", "Summary of the 2024 tax computation", doc("2024 tax computation — summary", "Taxable profit 305,000. Tax at 20%: 61,000. No losses carried forward. Tax written-down value of fixed assets at 31 Dec 2024: 150,000 (cost 420,000). Deferred tax liability at 31 Dec 2024: 9,000."))
add("personal", "personal_tax_documents_SAMPLE.md", "Personal income documents for the owner (fictitious)",
    doc("Personal tax documents (sample)", _T + "Taxpayer: the owner (employee E12). Resident in Sampleland. Filing jointly. Tax year 2025.\n- Salary from Northbrook Trading Ltd: per payroll.\n- Dividend from Northbrook Trading Ltd, 31 March 2025: 48,000 (80% of 60,000).\n- Bank interest: 1,240.\n- Rental income 18,000, rental costs 6,500.\n- Personal allowance 12,000; rate 15% to 50,000 of taxable income, 30% above.\n- Tax already withheld on salary: per payroll. Estimated payments made: 8,000."))
add("rd", "rd_projects_and_time.md", "R&D project descriptions and time allocation",
    doc("R&D projects (sample)", _T + "- Regime: 'Sampleland R&D credit', 12% of qualifying cost, SME scheme.\n- **P1 Self-aligning bracket**: new joint geometry; outcome uncertain at the start; three failed prototypes. Staff: E01 40%, E02 60% of the year.\n- **P2 Warehouse layout review**: re-arranging racking using known methods. Staff: E08 20%.\n- **P3 ERP configuration**: standard configuration of bought software. Staff: E06 15%.\n- Materials for prototypes (P1): 14,200. Subcontractor testing lab (P1): 8,000.\n- No grants received. Company is an SME and profitable."))
add("tp", "transfer_pricing_inputs.md", "Functional analysis and intercompany agreements",
    doc("Transfer pricing inputs (sample)", "- Northbrook UK Ltd manufactures brackets to Northbrook Trading's specification, holds little inventory, bears no market risk. Northbrook Trading owns the designs and sells to customers.\n- Intercompany goods: priced at UK cost plus 8% (agreement dated 1 January 2022).\n- Management fee: 12,000 a quarter charged by the UK to the US. **No written agreement.**\n- Comparable set supplied by the user: five contract manufacturers, interquartile range of mark-up on total cost 5.5% to 9.5% (source: user's database extract, 2024 data).\n- Documentation requirement: local file needed where intercompany transactions exceed 250,000 a year (sample rule)."))
add("payroll_rules", "payroll_tax_rules_SAMPLE.md", "Payroll tax rates and deposit schedule supplied for the test (fictitious)",
    doc("Payroll tax rules (sample)", _T + "- Employee income tax withheld: 12% of gross. Employee social security: 7.65%. Employer social security: 7.65%.\n- Deposit schedule assigned for 2025: **monthly**, due by the 15th of the following month.\n- Returns: quarterly. Filed by the company (no payroll provider).\n- Deposits made in 2025 Q3: July 31,900 on 14 Aug; August 31,900 on 15 Sep; September not yet paid."))
add("info_rules", "information_return_rules_SAMPLE.md", "Information return thresholds and form rules supplied for the test (fictitious)",
    doc("Information return rules (sample)", _T + "- Regime: US-style 1099. Reporting year 1 January to 31 December 2025.\n- Form 1099-NEC: services paid to non-corporate payees, threshold 600 for the year.\n- Corporations are not reported, except legal services.\n- Payments by card are reported by the card network, not the payer.\n- Foreign payees with a W-8 are not reported on a 1099."))
add("state_sales", "sales_by_state_2025.csv", "Sales by ship-to state, 2025 year to date, with tax collected",
    csv(["state", "sales", "transactions", "tax_collected", "registered", "registered_since"], [("Texas", 1840000, 2210, 115000, "yes", "2019-02-01"), ("California", 1120000, 1480, 81200, "yes", "2020-06-01"),
        ("Ohio", 310000, 402, 0, "no", ""), ("Georgia", 142000, 260, 0, "no", ""), ("Oregon", 96000, 118, 0, "no", "")]))
add("nexus", "sales_tax_thresholds_SAMPLE.md", "Economic nexus thresholds supplied for the test (fictitious)", doc("Sales tax thresholds (sample)", _T + "- Ohio: 100,000 of sales or 200 transactions in the year.\n- Georgia: 100,000 of sales or 200 transactions.\n- Oregon: no state sales tax.\n- Rates are applied by the company's tax engine; none are supplied here.\n- Physical presence: Texas (warehouse) and California (two employees) only."))
add("vat_tx", "vat_transactions_2025-Q3.csv", "Sales and purchases with VAT codes, Northbrook UK Ltd, July to September 2025 (GBP)",
    csv(["date", "type", "counterparty", "net", "vat_code", "vat"], [("2025-07-14", "sale", "UK customer A", 60000, "standard", 12000), ("2025-08-02", "sale", "Northbrook Trading Ltd (export)", 14570, "zero", 0),
        ("2025-08-20", "sale", "UK customer B", 38000, "standard", 7600), ("2025-07-22", "purchase", "UK supplier", 41000, "standard", 8200), ("2025-09-05", "purchase", "EU software vendor", 6000, "reverse charge", 1200),
        ("2025-09-05", "purchase", "EU software vendor (reverse charge output)", 0, "reverse charge", -1200), ("2025-09-19", "purchase", "Staff entertainment", 900, "blocked", 180)]))
add("vat_rules", "vat_rules_SAMPLE.md", "VAT rates and rules supplied for the test (fictitious)", doc("VAT rules (sample)", _T + "- Registered in one country since 2019. Standard rate 20%. Exports of goods are zero-rated.\n- Input VAT on staff entertainment is not recoverable.\n- No partial exemption. No special schemes. Quarterly returns.\n- VAT control account balance in the books at 30 September 2025: 11,580 payable."))

# ---- reporting, audit, controls ---------------------------------------------------------------------------
add("policies", "accounting_policies.md", "Accounting policies in use", doc("Accounting policies", "- Framework: US GAAP. Private company.\n- Revenue: recognised when goods are delivered.\n- Inventory: weighted average cost, lower of cost and net realisable value.\n- Fixed assets: straight line, 3 to 10 years.\n- Receivables: allowance based on ageing.\n- Accounts will be issued on 20 March 2026.\n- Legal review of contingencies: Greyfriars Legal LLP."))
add("notes_prior", "prior_year_notes_extract.md", "Extract from last year's notes", doc("Notes to the 2024 accounts — extract", "Note 1 Accounting policies (as above). Note 4 Fixed assets: cost 420,000, accumulated depreciation 197,800. Note 7 Term loan: 445,000, fixed 5.7%, matures 2029. Note 9 Related parties: management fee from Northbrook UK Ltd 48,000. Note 11 Commitments: warehouse lease to 2028."))
add("pbc", "auditor_request_list.csv", "Auditor's request list for the 2025 audit",
    csv(["ref", "area", "request"], [("A1", "Cash", "Bank statements and reconciliations for all accounts at year end"), ("A2", "Receivables", "Ageing by customer and subsequent receipts"), ("A3", "Inventory", "Count sheets and costing support"),
        ("A4", "Fixed assets", "Register, additions and disposals with invoices"), ("A5", "Payables", "Ageing and unrecorded liabilities search"), ("A6", "Debt", "Loan agreement and covenant compliance certificates"),
        ("A7", "Equity", "Board minutes and dividend approvals"), ("A8", "Revenue", "Contracts for the ten largest customers")]))
add("controls", "control_list.csv", "Existing controls for purchase-to-pay and period close",
    csv(["control", "process", "description", "leaves_trace_in_books", "evidence_location"], [("C1", "Purchase-to-pay", "Purchase orders approved before goods are ordered", "yes", "PO approval fields"),
        ("C2", "Purchase-to-pay", "Invoice matched to PO and receipt before payment", "yes", "bill, PO and receipt records"), ("C3", "Purchase-to-pay", "Vendor bank detail changes verified by call-back", "no", "AP call-back log (paper)"),
        ("C4", "Close", "Journals reviewed by a second person", "yes", "user and posting fields"), ("C5", "Close", "Bank reconciliation reviewed and signed monthly", "no", "signed PDF in the close folder"), ("C6", "Close", "No posting to closed periods", "yes", "posting dates")]))
add("criteria", "purchasing_policy.md", "Purchasing policy: the criteria for an internal audit", doc("Purchasing policy", "1. Every purchase over 1,000 needs a purchase order approved **before** the order is placed.\n2. Approval limits: managers up to 10,000; finance director up to 50,000; CEO above.\n3. Goods must be receipted before the invoice is paid.\n4. A change to vendor bank details must be verified by telephone on a known number.\n5. One person may not both create a vendor and approve its payment.\n\nAudit performed by internal audit, who did not operate this area. Completeness is out of scope."))
add("segments", "segment_results_2025.csv", "Results by division as reviewed by the CEO, 2025 year to date",
    csv(["division", "revenue", "operating_profit_before_central_costs", "assets"], [("Fixings", round(sum(p["revenue"] for p in B.PNL[27:]) * 0.55), 520000, 1400000),
        ("Packaging", round(sum(p["revenue"] for p in B.PNL[27:]) * 0.37), 310000, 900000), ("Services", sum(p["revenue"] for p in B.PNL[27:]) - round(sum(p["revenue"] for p in B.PNL[27:]) * 0.55) - round(sum(p["revenue"] for p in B.PNL[27:]) * 0.37), 60000, 200000)]))
add("matters", "legal_matters.md", "Open legal matters with management's assessment",
    doc("Legal matters at 30 September 2025", "| Matter | Type | Counsel | Management's view | Estimate | Given by |\n|---|---|---|---|---|---|\n| Customer claim, defective brackets | Litigation | Greyfriars Legal LLP | Probable | 40,000 to 70,000 | General counsel, 28 Sep 2025 |\n| Former employee claim | Employment | Greyfriars Legal LLP | Reasonably possible | up to 25,000 | General counsel, 28 Sep 2025 |\n| Supplier counterclaim | Litigation | Greyfriars Legal LLP | Remote | — | General counsel |\n\nFramework: US GAAP. No matter is privileged. Insurance: product liability policy with a 10,000 deductible."))
add("related", "related_parties.md", "List of related parties", doc("Related parties", "- Northbrook UK Ltd — 80% subsidiary.\n- A. Reyes — CEO and director. Owns Halden Property Management (landlord of the warehouse).\n- J. Marsh — director since June 2025.\n- Investor A — 20% shareholder.\nFramework: ASC 850. Output for the CFO only."))
add("issued", "issued_statements_2024_extract.md", "Extract of the issued 2024 financial statements", doc("Issued 2024 statements — extract", "Revenue 2024: 4,731,300. Net income 2024: 331,596. The 2024 accounts were issued on 18 March 2025.\n\n**Error found in the Q3 2025 close:** shipments of 86,000 dispatched on 2 January 2025 were invoiced and recognised as revenue on 30 December 2024 (cost of goods 49,900). Framework ASC 250. Private company. Materiality used by the auditors: 5% of pre-tax income."))
add("filing", "filing_inputs.md", "Filing inputs: filer status, calendar, prior filing figures",
    doc("Filing inputs (sample)", "Form 10-Q for Q3 2025. Filer status: accelerated. Filing date 7 November 2025; earnings release 5 November.\nPrior filing (Q2 2025 10-Q) reported: revenue for the six months 2,598,300; total assets 2,741,000.\nTaxonomy version stated by the user: 'US GAAP 2025'. Prior tag map: 142 tagged items, 6 custom extensions.\nNon-GAAP measure used: Adjusted EBITDA = net income + interest + depreciation + one-time professional fees.\nReviewers: controller (accounting), FP&A lead, outside counsel. Independent XBRL review: reporting manager."))
add("mda", "mda_drivers.md", "Management's explanation of results", doc("Drivers supplied by management", "- Revenue grew on volume in Fixings; prices were unchanged.\n- Gross margin fell because steel prices rose and were not passed on until October.\n- Marketing rose for a trade show in September.\n- One-time legal fee in June for a contract dispute.\n- Liquidity: term loan 220,000; no revolver. Capex plan 2026: 80,000 for a second packing line.\n- Known trends: **for management to write.**\nReport type: 10-K. Sign-off: CFO and counsel."))
add("subseq", "post_period_ledger_2025-10.csv", "Ledger activity from 1 October 2025 to the date of the review",
    csv(["date", "account", "description", "amount"], [("2025-10-06", "1100", "Receipt from Pennine Retail Group", -112071), ("2025-10-09", "1150", "Write-off: Foxhall Garden Centres (administration)", 4003),
        ("2025-10-14", "6400", "Settlement of customer claim, defective brackets", 52000), ("2025-10-20", "1200", "Credit note issued: returned PN-55 panels", -8200)]))
add("close_cal", "close_calendar.csv", "Month-end close calendar with completion dates, last six months",
    csv(["month", "books_closed_on", "working_days_to_close", "manual_journals", "total_journals", "period_reopened"], [("2025-04", "2025-05-14", 10, 41, 58, "no"), ("2025-05", "2025-06-13", 10, 39, 55, "no"),
        ("2025-06", "2025-07-16", 12, 47, 61, "yes"), ("2025-07", "2025-08-13", 9, 40, 57, "no"), ("2025-08", "2025-09-12", 9, 38, 54, "yes"), ("2025-09", "2025-10-14", 10, 42, 60, "no")]))

# ---- valuation, deals -----------------------------------------------------------------------------------------
add("market", "market_data_supplied.md", "Market data supplied by the user for a valuation",
    doc("Market data (supplied by the user)", "Valuation date 30 September 2025. Purpose: management planning. Standard: fair market value.\n- Risk-free rate 4.2% (user: government bond yield, 30 Sep 2025). Equity risk premium 5.5%. Beta 1.1. Size premium 2.0%. Pre-tax cost of debt 5.7%. Tax rate 20% (sample). Target debt weight 20%.\n- Comparable companies, EV / EBITDA (user's data provider, 30 Sep 2025): 6.8x, 7.4x, 8.1x, 8.9x, 9.6x.\n- Precedent transactions, EV / EBITDA: 7.0x, 8.5x, 10.2x.\n- Terminal growth 2.5%.\n- Net debt definition: term loan plus card balance less cash. Diluted shares: 1,080,000."))
add("deal", "acquisition_terms_and_valuation.md", "Acquisition terms and the valuer's fair values",
    doc("Acquisition of Harlow Fabrication Ltd (sample)", "Acquirer: Northbrook Trading Ltd. Acquisition date 1 July 2025. 100% of the shares. Framework US GAAP.\nConsideration: cash 1,400,000 plus an earnout of up to 300,000 (fair value 180,000, payable in cash, classified as a liability).\nDeal costs (legal and advisory): 46,000.\n\n| Item | Book value | Fair value (valuation report, 20 Aug 2025) |\n|---|---:|---:|\n| Receivables | 210,000 | 205,000 |\n| Inventory | 180,000 | 195,000 |\n| Fixed assets | 320,000 | 410,000 |\n| Customer relationships | — | 260,000 |\n| Trade name | — | 90,000 |\n| Payables and accruals | (240,000) | (240,000) |\n| Deferred tax on fair value uplifts (20%, sample) | — | (88,000) |"))
add("impair", "impairment_inputs.md", "Carrying amounts, goodwill allocation, projections and discount rate",
    doc("Impairment test inputs (sample)", "Test date 30 September 2025. Framework US GAAP. Goodwill 748,000, all allocated to one reporting unit, 'Harlow'.\nCarrying amount of the Harlow unit including goodwill: 1,620,000.\nProjections supplied by management (free cash flow): 2026 150,000; 2027 165,000; 2028 180,000; 2029 190,000; 2030 200,000. Terminal growth 2.5%.\nDiscount rate supplied: 10.5% post-tax (derivation: the user's cost of capital memo, 30 Sep 2025).\nTrigger noted by management: loss of a major customer in August 2025."))
add("model", "model_summary_for_review.csv", "Summary tab of the lender model to be reviewed (actuals extracted 5 October 2025)",
    csv(["line", "2025-07", "2025-08", "2025-09", "note"], [("Revenue", B.PNL[33]["revenue"], B.PNL[34]["revenue"], B.PNL[35]["revenue"] + 50000, "model"),
        ("Cost of goods sold", B.PNL[33]["cogs"], B.PNL[34]["cogs"], B.PNL[35]["cogs"], "model"), ("Cash", B.BS[33]["cash"], B.BS[34]["cash"], B.BS[35]["cash"], "model"),
        ("Total assets", "", "", sum(B.BS[35][k] for k in ("cash", "ar", "inventory", "prepaid", "fixed_assets_net")), "model"), ("Total liabilities and equity", "", "", sum(B.BS[35][k] for k in ("ap", "accrued", "debt", "share_capital", "retained_earnings")) - 12000, "model")]))
add("qoe", "management_adjusted_ebitda_bridge.csv", "Management's proposed adjustments to EBITDA, twelve months to September 2025",
    csv(["adjustment", "amount", "management_reason"], [("One-time legal fee, June 2025", 14000, "Non-recurring dispute"), ("Owner salary above market", 60000, "Owner paid 192,000; market 132,000"),
        ("Trade show marketing", 7300, "One-time"), ("Rent to related party below market", -24000, "Landlord is the CEO's company; market rent is higher")]))
add("restructure", "restructuring_plan.md", "Approved restructuring plan", doc("2025 restructuring plan (sample)", "Approved by the board on 3 October 2025. Communicated to affected staff on 14 October 2025 (all-hands meeting; minutes on file).\n\n| Group | Roles | Severance terms | Total |\n|---|---:|---|---:|\n| Warehouse, night shift | 3 | 8 weeks' pay each | 26,000 |\n| Admin | 1 | 12 weeks' pay | 11,700 |\n\nNo future service is required. Lease on the overflow unit to be exited: penalty 15,000. Expected completion 31 December 2025.\nFramework ASC 420. Output for the CFO only. No names are to be recorded."))
add("ipo", "ipo_readiness_inputs.md", "IPO readiness inputs", doc("IPO readiness inputs (sample)", "Target: listing in 18 months. Registrant: the current parent. No reorganisation planned.\nAudits: 2023 and 2024 audited; 2022 not audited.\nEquity: see cap table; one grant in 2025 with an independent valuation.\nSystems: one accounting system, spreadsheets for revenue schedules. No control assessment has been done."))

# ---- sectors ------------------------------------------------------------------------------------------------------
add("npo", "nonprofit_trial_balance_and_gifts.md", "Trial balance and gift schedule of a charity (separate fictitious entity)",
    doc("Riverside Community Trust — year to 30 June 2025 (sample)", "Framework ASC 958. Three programmes tracked as classes: Youth, Seniors, Food bank.\n\n| Account | Amount |\n|---|---:|\n| Cash | 412,000 |\n| Net assets without donor restrictions (opening) | 180,000 |\n| Net assets with donor restrictions (opening) | 95,000 |\n| Contributions received | 640,000 |\n| Programme expenses — Youth | 210,000 |\n| Programme expenses — Seniors | 150,000 |\n| Programme expenses — Food bank | 120,000 |\n| Salaries (shared) | 90,000 |\n| Rent (shared) | 24,000 |\n| Fundraising event costs | 31,000 |\n\n| Gift | Amount | Restriction | Conditional? | Spent on purpose by 30 June |\n|---|---:|---|---|---:|\n| Harlow Foundation | 200,000 | Youth programme only | No | 160,000 |\n| City grant | 150,000 | Food bank, year to June 2025 | Yes — must serve 5,000 meals; 5,400 served | 120,000 |\n| General donations | 290,000 | None | No | — |\n\nShared costs split on staff time: Youth 40%, Seniors 25%, Food bank 15%, Management 15%, Fundraising 5%. No endowment. No gifts in kind."))
add("grants", "grant_awards_and_spending.md", "Grant award terms with spending by grant", doc("Grant awards (sample)", "| Grant | Award | Period | Conditional? | Restriction | Budget: staff / supplies / indirect | Spent: staff / supplies | Report due |\n|---|---:|---|---|---|---|---|---|\n| G1 City food grant | 150,000 | Jul 2024–Jun 2025 | Yes: 5,000 meals (5,400 served) | Food bank | 90,000 / 45,000 / 15,000 | 88,000 / 32,000 | 31 Aug 2025 |\n| G2 Harlow Foundation | 200,000 | Jan 2024–Dec 2025 | No | Youth programme | 140,000 / 40,000 / 20,000 | 121,000 / 39,000 | 31 Jan 2026 |\n| G3 State seniors grant | 60,000 | Jul 2024–Jun 2025 | No | Seniors | 50,000 / 10,000 / 0 | 49,000 / 14,500 (of which 3,200 dated July 2025) | 30 Sep 2025 |\n\nIndirect cost rate: 10% of direct costs where the award allows. Grants are tagged in the books as classes."))
add("gov", "township_trial_balance_by_fund.csv", "Trial balance by fund of a township (separate fictitious entity), year to 30 June 2025",
    csv(["fund", "fund_type", "account", "amount"], [("General", "governmental", "Cash", 820000), ("General", "governmental", "Property tax receivable", 140000), ("General", "governmental", "Accounts payable", -95000),
        ("General", "governmental", "Fund balance", -865000), ("Road", "special revenue", "Cash", 310000), ("Road", "special revenue", "Fund balance", -310000), ("Water", "enterprise", "Cash", 190000),
        ("Water", "enterprise", "Capital assets net", 2400000), ("Water", "enterprise", "Revenue bonds", -1500000), ("Water", "enterprise", "Net position", -1090000)]))
add("gov_notes", "township_notes.md", "Basis of accounting and fund balance constraints", doc("Millbrook Township — notes (sample)", "Framework GASB. Books kept on modified accrual for governmental funds, full accrual for the water fund. Funds tagged as classes.\nConstraints: Road fund restricted by state law to road maintenance. General fund: 200,000 committed by board resolution for a new fire truck; 50,000 assigned to next year's budget.\nCapital assets of governmental activities (register): 3,100,000 net. General obligation debt: 900,000. Pension actuarial report: net pension liability 640,000 (report dated 15 August 2025)."))
add("health", "billing_summary_by_payer_2025-09.csv", "Billing system totals by payer class, September 2025 (totals only, no patient detail)",
    csv(["payer_class", "gross_charges", "contractual_adjustments", "payments", "denials", "charity_care", "ar_0_30", "ar_31_90", "ar_over_90"], [("Medicare", 420000, -252000, 150000, 9000, 0, 40000, 12000, 3000),
        ("Commercial", 610000, -244000, 318000, 21000, 0, 95000, 41000, 22000), ("Self-pay", 130000, 0, 31000, 0, 18000, 22000, 30000, 44000)]))
add("health_gl", "clinic_gl_summary_2025-09.md", "Ledger totals for the clinic, September 2025", doc("Lakeside Clinic — ledger totals, September 2025 (sample)", "Gross patient revenue 1,160,000. Contractual allowances (contra-revenue) (480,000). Bad debt expense 26,000. Charity care recorded as bad debt: 18,000.\nPatient receivables 309,000. Allowance for contractual adjustments (62,000). Unapplied cash 14,000 (August: 6,000).\nCharity care policy: free care below 200% of the poverty guideline; presented as a deduction from revenue, not as bad debt."))
add("insure", "insurer_close_schedules_2025-09.md", "Close schedules of an insurance carrier (separate fictitious entity)", doc("Harbour Mutual — close schedules, September 2025 (sample)", "Business model: carrier. Regulated. One 30% quota share treaty.\n- Written premium, September: 900,000. Unearned premium reserve: opening 2,100,000; closing per policy system 2,250,000; ledger 2,180,000.\n- Paid claims 410,000. Case reserves 1,300,000. IBNR per the actuary's quarterly report (30 Sep 2025): 760,000; ledger 700,000.\n- Reinsurance recoverable on paid claims 123,000, of which 48,000 is over 90 days.\n- Commissions paid 135,000; deferred acquisition costs opening 310,000."))
add("property", "property_schedule.md", "Property schedule with use, cost and lease terms", doc("Property schedule (sample)", "Framework US GAAP. Period: 2025.\n\n| Property | Use | Cost | Land / building | In service | 2025 rent billed | 2025 costs |\n|---|---|---:|---|---|---:|---:|\n| Unit 7, Dock Road | Rented to a tenant | 1,200,000 | 300,000 / 900,000 | 2021-04-01 | 108,000 | 21,000 |\n| Mill House | Occupied by the company | 800,000 | 200,000 / 600,000 | 2018-01-01 | — | 34,000 |\n| Plot 12 | Under development | 450,000 to date | all land so far | — | — | interest capitalised 18,000, including 6,000 after work paused in June |\n\nUnit 7 lease: 5 years from 1 Jan 2024, 8,000 a month in year 1, rising 500 a month each year, first two months rent-free. Buildings depreciated over 40 years."))
add("swap", "interest_rate_swap.md", "Interest rate swap confirmation and bank valuation", doc("Interest rate swap (sample)", "Counterparty: Calder Bank. Trade date 1 January 2025. Notional 200,000. Company pays fixed 5.2%, receives floating. Matures 31 December 2029.\nBank valuation at 30 September 2025: liability of 3,400 (bank mark-to-market statement dated 1 October 2025; method: discounted cash flow on the bank's curve).\nHedge documentation: designation memo for a cash flow hedge of the term loan, **dated 14 February 2025**.\nLedger: derivative liability recorded 2,900; other comprehensive income debit 2,900.\nFramework ASC 815. Note: the term loan is fixed rate (see the loan summary)."))
add("crypto", "exchange_export_2025.csv", "Exchange account export: digital asset holdings and transactions, 2025",
    csv(["date", "asset", "type", "quantity", "usd_amount", "price_source"], [("2025-02-10", "BTC", "buy", 1.5, 63000, "exchange"), ("2025-05-20", "BTC", "buy", 0.5, 26000, "exchange"), ("2025-08-04", "BTC", "sell", -0.4, 22800, "exchange"),
        ("2025-06-01", "USDC", "buy", 50000, 50000, "exchange"), ("2025-09-30", "BTC", "closing price per unit", 1, 58000, "exchange closing price 30 Sep 2025"), ("2025-09-30", "USDC", "closing price per unit", 1, 1.00, "exchange closing price 30 Sep 2025")]))
add("esg", "esg_activity_data_2025.csv", "Activity data for ESG reporting, January to September 2025",
    csv(["site", "metric", "quantity", "unit", "source", "owner"], [("Texas warehouse", "Electricity", 412000, "kWh", "utility bills", "Facilities manager"), ("California office", "Electricity", 38000, "kWh", "landlord statement", "Office manager"),
        ("Texas warehouse", "Diesel (forklifts, van)", 9600, "litres", "fuel card", "Facilities manager"), ("All", "Headcount", 12, "employees", "payroll", "HR"), ("All", "Business flights", "", "km", "not collected — spend only", "")]))
add("esg_notes", "esg_scope_and_factors.md", "ESG scope and emission factor source", doc("ESG scope (sample)", "Purpose: customer requests. Boundary: operational control, two sites. Framework: none yet.\nEmission factors supplied by the user (**sample factors, fictitious**): electricity 0.40 kg CO2e per kWh; diesel 2.70 kg CO2e per litre. Source to quote: 'sample factor set 2025'.\nNo assurance planned this year. Nothing published before."))
add("actuarial", "actuarial_report_summary.md", "Summary of the actuary's report on the staff pension plan", doc("Actuarial valuation — staff pension plan (sample)", "Defined benefit plan. Measurement date 30 September 2025. Report dated 20 October 2025 by Marlow Actuaries. Framework ASC 715.\n\n| | Opening | Closing |\n|---|---:|---:|\n| Projected benefit obligation | 1,180,000 | 1,265,000 |\n| Fair value of plan assets | 960,000 | 1,010,000 |\n\nService cost 62,000. Interest cost 59,000. Expected return on assets 57,600. Actual return 41,000. Contributions 45,000. Benefits paid 36,000. Actuarial loss on the obligation: nil. Discount rate 5.0%.\nLedger: pension liability 220,000; no pension entry posted in the nine months."))
add("aml", "aml_customer_and_activity.md", "AML inputs: regime, officer, customers and activity", doc("AML inputs (sample)", "Entity: Northbrook Payments (separate fictitious entity), offering payment services. Regime as stated by the user: 'Sampleland AML Regulations 2020'. Responsible officer: the compliance lead, P. Whitcombe (MLRO). Screening tool: the company's own subscription service.\nExisting policy: none written.\n\n| Customer ref | Type | Risk attributes | Screening (company's tool) | Q3 activity |\n|---|---|---|---|---|\n| C-01 | Limited company | Domestic, retail | Clear, 2 Sep 2025 | 42 payments, average 1,100 |\n| C-02 | Limited company | Owned through an offshore holding; owner not identified | Not run | 9 payments of 9,900 each within 6 days |\n| C-03 | Individual | Politically exposed person (declared) | Match reviewed, 1 Aug 2025 | 3 payments, average 4,000 |\n\nOutput for the officer only."))
add("credit_policy", "credit_request_and_policy.md", "Credit request, customer financials and credit policy", doc("Credit request (sample)", "Customer: Harlow Fabrication Ltd (legal entity as named). Requested: net 45, about 40,000 a month, USD. Current limit 200,000.\nCustomer's latest accounts (year to Dec 2024, supplied by the customer): revenue 6.2m; net income 110,000; current assets 1.9m; current liabilities 1.7m; total debt 1.4m; equity 600,000.\nNo credit bureau report. No trade references. No credit insurance.\nCredit policy: tier ceilings 50,000 / 150,000 / 300,000; no customer above 25% of receivables; limits above 150,000 approved by the finance director."))
add("approvals", "approval_matrix_and_tolerances.md", "Approval matrix and matching tolerances", doc("Approval matrix and tolerances", "Purchase order approval: managers (J. Marsh) up to 10,000; finance director (A. Reyes) up to 50,000; CEO above.\nMatching tolerance: price 2%, quantity exact, total 25.\nServices orders (freight, consulting) need a signed service confirmation in place of a goods receipt.\nNo foreign-currency orders. Exceptions are resolved by the AP manager.\nShort-pay write-off: up to 50, approved by the credit manager. Unapplied cash account: 2100 is **not** used; unapplied cash sits in 1100 as credits."))
add("wco", "working_capital_terms.md", "Agreed terms, guardrails and cost of capital", doc("Working capital inputs", "Customer terms agreed: 30 days (Harlow Fabrication 45 days). Supplier terms: as recorded.\nGuardrails: Kestrel Supplies is strategic — do not propose stretching it. Service level: 98% order fill.\nCost of capital: 9%. No industry benchmarks supplied."))
add("kpi", "kpi_request.md", "KPI dashboard request", doc("KPI request", "Audience: the board. Business model: distribution with some services. Period: 36 months to September 2025, refreshed monthly.\nOperational systems: none connected; orders are in a separate order system. No targets set. Current KPI in use: 'gross margin', defined informally."))
add("chart_req", "chart_of_accounts_request.md", "Chart of accounts restructure request", doc("Chart of accounts request", "Restructure of the existing chart. Target system: the same accounting system. Framework US GAAP. Industry: distribution. Reporting by department. The chart must serve the lender's covenant reporting (needs one-time professional fees shown separately)."))
add("treasury", "treasury_inputs.md", "Bank accounts, signatories and policy inputs", doc("Treasury inputs", "| Account | Bank | Purpose | Signatories |\n|---|---|---|---|\n| 1000 Operating Bank Account | Calder Bank | Operations | A. Reyes, S. Patel |\n| 1010 Petty Cash | — | Float | Office manager |\n| 1050 Stripe Clearing | Stripe | Card receipts | — |\n\nNorthbrook UK Ltd holds 84,200 GBP at a UK bank; cash can move between the two entities. No cash is restricted. Risk appetite: no more than 1,000,000 with one bank. No existing treasury policy. Liquidity must cover loan payments of 6,900 a month and 2026 capex of 80,000."))
add("budget_req", "budget_inputs_2026.md", "Budget inputs for 2026", doc("2026 budget inputs", "Fiscal year 2026, monthly. Method: driver-based revenue, incremental overheads. No budget exists for 2026.\nRevenue drivers: volume +8%; price +3% from 1 January; one new customer worth 240,000 a year from April.\nHeadcount: two warehouse hires in March at 52,000 a year each; one sales hire in July at 82,000.\nTarget: operating margin 12%. Rent rises to 9,500 a month from July. No inflation assumption supplied for other costs."))
add("scenario", "scenario_request.md", "Scenario and sensitivity request", doc("Scenario request", "Decision: whether to take a second packing line in 2026. Model: the twelve-month forecast (uploaded). Output metric: cash at 30 September 2026 and minimum cash in the year.\nDrivers to vary: revenue growth, gross margin, DSO, payroll. Ranges: propose from history.\nScenarios: 'Base'; 'Steel shock' (margin down 3 points for six months); 'Lost customer' (Harlow leaves in January).\nThreshold: minimum cash 250,000. No probability weights."))
add("model_req", "model_assumptions.md", "Model assumptions", doc("Model assumptions", "Purpose: internal planning. Horizon: three years, monthly. Revenue growth 8% a year; gross margin 41%; operating costs grow 4% a year.\nCapex 80,000 in 2026, then equal to depreciation. Term loan on its agreed schedule (5,000 a month, 5.7%). No new equity.\nTax: single effective rate of 20% (sample). Circularity: use prior-period balances for interest."))
add("audit_scope", "audit_inputs.md", "Audit type, timeline and events", doc("Audit and year-end inputs", "Engagement: full audit of the year to 31 December 2025, US GAAP. Fieldwork starts 9 February 2026. Figures still moving. No materiality communicated.\nOwners: controller (S. Patel) for all areas except inventory (warehouse manager).\nStatutory filings in scope: corporate tax return; information returns.\nEvents in 2025: dividend of 60,000 in March; acquisition of Harlow Fabrication on 1 July; restructuring approved in October.\nPrior year auditor's point: bank reconciliations not reviewed monthly.\nQ3 obligations: board pack and lender compliance certificate. No interim review."))
add("wrong_rota", "staff_rota_september.csv", "A staff rota (not an accounting document)", csv(["employee", "week_1", "week_2", "week_3", "week_4"], [("E08", "nights", "nights", "days", "days"), ("E09", "days", "days", "nights", "nights"), ("E10", "off", "days", "days", "nights")]))
add("wrong_period", "trial_balance_september.csv", f"Trial balance of {co} at 30 September **2024** (the wrong year)", tbcsv(23))
add("wrong_company", "trial_balance_2025-09-30_v2.csv", "Trial balance of a different company, Harlow Fabrication Ltd, at 30 September 2025",
    csv(["account", "name", "debit", "credit"], [("1000", "Bank — Harlow Fabrication Ltd", 96000, 0), ("1100", "Accounts Receivable", 210000, 0), ("2000", "Accounts Payable", 0, 240000), ("3000", "Equity", 0, 66000)]))
