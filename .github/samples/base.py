"""Base dataset for the sample files: one fictitious company, internally consistent.

Northbrook Trading Ltd, USD, calendar year, test period September 2025. Every table is
derived from the same monthly series so the pieces tie to each other, and a handful of
problems are seeded on purpose so a skill has something to find (see SEEDED).
Deterministic: no randomness, no dependencies.
"""
import math

CO, CCY, PERIOD, AS_AT = "Northbrook Trading Ltd", "USD", "September 2025", "2025-09-30"
MONTHS = [(2022 + (9 + i) // 12, (9 + i) % 12 + 1) for i in range(36)]          # 2022-10 .. 2025-09
EOM = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
def ym(i): y, m = MONTHS[i]; return f"{y}-{m:02d}"
def eom(i): y, m = MONTHS[i]; return f"{y}-{m:02d}-{EOM[m]}"

# ---- monthly P&L -----------------------------------------------------------------
PNL = []
for i, (y, m) in enumerate(MONTHS):
    rev = round(300000 * 1.012 ** i * (1 + 0.12 * math.sin(2 * math.pi * (m - 3) / 12)) / 100) * 100
    cogs = round(rev * (0.60 if i >= 33 else 0.58))
    r = dict(month=ym(i), revenue=rev, cogs=cogs, payroll=62000 + 400 * i, rent=9000,
             marketing=round(rev * 0.04 * (1.6 if i == 35 else 1)), software=3500,
             professional_fees=2500 + (14000 if (y, m) == (2025, 6) else 0),
             bank_fees=round(rev * 0.004), depreciation=4200, interest=1900)
    r["net_income"] = rev - sum(v for k, v in r.items() if k not in ("month", "revenue"))
    PNL.append(r)
PL_LINES = ["revenue", "cogs", "payroll", "rent", "marketing", "software", "professional_fees", "bank_fees", "depreciation", "interest"]

# ---- monthly balance sheet -------------------------------------------------------
BS, cash, re_ = [], 180000, None
for i, p in enumerate(PNL):
    ar = round(p["revenue"] * (42 + 10 * i / 35) / 30)
    inv = round(p["cogs"] * (60 + 15 * i / 35) / 30)
    ap = round(p["cogs"] * (38 - 5 * i / 35) / 30)
    accr = round(p["payroll"] * 0.5)
    b = dict(month=ym(i), ar=ar, inventory=inv, prepaid=18000, fixed_assets_net=260000 - 4200 * (i + 1),
             ap=ap, accrued=accr, debt=400000 - 5000 * (i + 1), share_capital=250000)
    if i == 0:
        re_ = cash + ar + inv + b["prepaid"] + b["fixed_assets_net"] - ap - accr - b["debt"] - 250000
    else:
        q = BS[-1]
        cash += p["net_income"] + 4200 - (ar - q["ar"]) - (inv - q["inventory"]) + (ap - q["ap"]) + (accr - q["accrued"]) - 5000
        re_ += p["net_income"]
    b["cash"], b["retained_earnings"] = cash, re_
    BS.append(b)

# ---- chart of accounts and trial balance ------------------------------------------
COA = [("1000", "Operating Bank Account", "Bank"), ("1010", "Petty Cash", "Bank"), ("1050", "Stripe Clearing", "Other Current Asset"),
       ("1100", "Accounts Receivable", "Accounts Receivable"), ("1150", "Allowance for Doubtful Accounts", "Other Current Asset"),
       ("1200", "Inventory", "Other Current Asset"), ("1300", "Prepaid Expenses", "Other Current Asset"),
       ("1500", "Fixed Assets - Cost", "Fixed Asset"), ("1510", "Accumulated Depreciation", "Fixed Asset"),
       ("2000", "Accounts Payable", "Accounts Payable"), ("2050", "Corporate Card Payable", "Credit Card"),
       ("2100", "Accrued Liabilities", "Other Current Liability"), ("2150", "Payroll Clearing", "Other Current Liability"),
       ("2160", "Payroll Tax Payable", "Other Current Liability"), ("2200", "Sales Tax Payable", "Other Current Liability"),
       ("2300", "Intercompany Payable - Northbrook UK", "Other Current Liability"), ("2500", "Term Loan", "Long Term Liability"),
       ("3000", "Share Capital", "Equity"), ("3100", "Retained Earnings", "Equity"),
       ("4000", "Sales Revenue", "Income"), ("5000", "Cost of Goods Sold", "Cost of Goods Sold"),
       ("6000", "Payroll Expense", "Expense"), ("6100", "Rent", "Expense"), ("6200", "Marketing", "Expense"),
       ("6300", "Software", "Expense"), ("6400", "Professional Fees", "Expense"), ("6500", "Bank Fees", "Expense"),
       ("6600", "Depreciation", "Expense"), ("7000", "Interest Expense", "Expense")]
PL_ACCT = dict(revenue="4000", cogs="5000", payroll="6000", rent="6100", marketing="6200", software="6300",
               professional_fees="6400", bank_fees="6500", depreciation="6600", interest="7000")
NAME = {c: n for c, n, _ in COA}

def tb(i):
    """Trial balance at month index i: balance sheet balances plus year-to-date P&L. Debits positive."""
    b, y = BS[i], MONTHS[i][0]
    ytd = [j for j in range(i + 1) if MONTHS[j][0] == y]
    prior = ytd[0] - 1
    re_open = BS[prior]["retained_earnings"] if prior >= 0 else b["retained_earnings"] - sum(PNL[j]["net_income"] for j in ytd)
    cost = 420000
    rows = {"1000": b["cash"] - 500 - 6420, "1010": 500, "1050": 6420, "1100": b["ar"] + 9000, "1150": -9000,
            "1200": b["inventory"], "1300": b["prepaid"], "1500": cost, "1510": b["fixed_assets_net"] - cost,
            "2000": -(b["ap"] - 7300 - 38000), "2050": -7300, "2100": -(b["accrued"] - 1200 - 5400 - 2600),
            "2150": -1200, "2160": -5400, "2200": -2600, "2300": -38000, "2500": -b["debt"],
            "3000": -250000, "3100": -re_open}
    for k, a in PL_ACCT.items():
        v = sum(PNL[j][k] for j in ytd)
        rows[a] = -v if k == "revenue" else v
    assert abs(sum(rows.values())) < 1, sum(rows.values())
    return [(c, NAME[c], max(v, 0), max(-v, 0)) for c, v in rows.items()]

def spread(total, weights):
    """Split an integer total by weights, exactly."""
    s = sum(weights); out = [round(total * w / s) for w in weights]; out[0] += total - sum(out); return out

I = 35                                  # September 2025
TBV = {c: d - cr for c, _, d, cr in tb(I)}
AR_TOTAL, AP_TOTAL, CASH_GL, INV_TOTAL = TBV["1100"], -TBV["2000"], TBV["1000"], TBV["1200"]

# ---- receivables -------------------------------------------------------------------
CUSTOMERS = ["Harlow Fabrication Ltd", "Pennine Retail Group", "Castleton Foods", "Ridgeway Logistics", "Marlow & Finch",
             "Ashby Engineering", "Tideswell Hotels", "Brecon Outdoor", "Calder Print", "Dunmore Medical", "Elmfield Schools", "Foxhall Garden Centres"]
_arw = [31, 14, 11, 9, 8, 7, 6, 5, 4, 3, 1.5, 0.5]
_ar = spread(AR_TOTAL + 2150, _arw)          # the +2150 is offset by a credit balance below
AR_OPEN = []                                  # customer, invoice, invoice_date, due_date, amount, days_overdue
_age = [(95, "2025-05-28", "2025-06-27"), (12, "2025-08-19", "2025-09-18"), (0, "2025-09-08", "2025-10-08"), (41, "2025-07-21", "2025-08-20"),
        (0, "2025-09-15", "2025-10-15"), (3, "2025-08-28", "2025-09-27"), (67, "2025-06-25", "2025-07-25"), (0, "2025-09-22", "2025-10-22"),
        (20, "2025-08-11", "2025-09-10"), (0, "2025-09-03", "2025-10-03"), (0, "2025-09-26", "2025-10-26"), (130, "2025-04-23", "2025-05-23")]
for k, (c, amt) in enumerate(zip(CUSTOMERS, _ar)):
    d, inv, due = _age[k]
    if k == 0:                                 # Harlow: one old invoice and one current
        AR_OPEN.append((c, "INV-20418", inv, due, 48200, 95)); AR_OPEN.append((c, "INV-20977", "2025-09-12", "2025-10-12", amt - 48200, 0))
    else:
        AR_OPEN.append((c, f"INV-{20500 + 37 * k}", inv, due, amt, d))
AR_OPEN.append(("Calder Print", "CM-0312", "2025-09-02", "", -2150, 0))      # unapplied credit
assert sum(r[4] for r in AR_OPEN) == AR_TOTAL
AR_HIST = []                                   # paid invoices, last 12 months: customer, invoice, invoice_date, paid_date, amount, days_to_pay
for k, c in enumerate(CUSTOMERS):
    base = [88, 44, 31, 47, 29, 36, 62, 28, 41, 30, 33, 75][k]
    for j in range(5):
        i = 24 + 2 * j + (k % 2); y, m = MONTHS[i]; dtp = base + (j - 2) * (3 if k else 6)
        pm, py = (m + dtp // 30 - 1) % 12 + 1, y + (m + dtp // 30 - 1) // 12
        AR_HIST.append((c, f"INV-{18000 + 100 * k + j}", f"{y}-{m:02d}-10", f"{py}-{pm:02d}-{10 + dtp % 30 if 10 + dtp % 30 <= 28 else 28:02d}",
                        round(_ar[k] * (0.5 + 0.1 * j)), dtp))

# ---- payables, purchase orders, receipts -------------------------------------------
VENDORS = [  # name, terms_days, tax_form_on_file, entity_type, bank_changed_on, paid_2025
    ("Kestrel Supplies", 30, "W-9", "Corporation", "", 412300), ("Orchard Packaging", 30, "W-9", "LLC", "", 188400),
    ("Summit Freight", 15, "W-9", "Corporation", "2025-09-16", 96200), ("Brightline IT Services", 30, "none", "Sole proprietor", "", 41800),
    ("Halden Property Management", 0, "W-9", "LLC", "", 81000), ("M. Okafor Consulting", 30, "none", "Sole proprietor", "", 18500),
    ("Kestrel Supplies Inc.", 30, "none", "Corporation", "", 6480), ("Greyfriars Legal LLP", 30, "W-9", "Partnership", "", 27400),
    ("Vale Marketing Studio", 30, "none", "LLC", "", 9200), ("Northgate Utilities", 21, "W-9", "Corporation", "", 22100),
    ("Pinecrest Software", 30, "W-8BEN-E", "Foreign corporation", "", 42000), ("Dale Cleaning Co", 30, "W-9", "Sole proprietor", "", 5400)]
_apw = [34, 16, 9, 5, 0, 3, 0, 6, 4, 5, 9, 2]
_ap = spread(AP_TOTAL - 12960, _apw)
BILLS = []                                      # vendor, bill_no, bill_date, due_date, amount, po, status
for k, (v, amt) in enumerate(zip(VENDORS, _ap)):
    if amt <= 0: continue
    bd = f"2025-09-{3 + 2 * k:02d}"
    BILLS.append((v[0], f"{'INV-' if k % 3 else ''}{4502 + 71 * k}", bd, f"2025-10-{3 + 2 * k:02d}", amt, f"PO-{1040 + k}" if k < 6 else "", "open"))
BILLS.append(("Kestrel Supplies", "INV-4471", "2025-09-05", "2025-10-05", 6480, "", "open"))
BILLS.append(("Kestrel Supplies Inc.", "INV4471", "2025-09-06", "2025-10-06", 6480, "", "open"))       # duplicate of INV-4471, other vendor record
assert sum(b[4] for b in BILLS) == AP_TOTAL
_k = next(b for b in BILLS if b[5] == "PO-1040")
PO = [  # po, vendor, item, qty, unit_price, approved_by, approved_on
    ("PO-1040", "Kestrel Supplies", "Steel bracket SB-20", 4000, round(_k[4] / 4000 / 1.018, 4), "J. Marsh", "2025-08-25"),
    ("PO-1041", "Orchard Packaging", "Carton C-12", 100, 0, "J. Marsh", "2025-08-27"),
    ("PO-1042", "Summit Freight", "Freight, September", 1, 0, "", ""),
    ("PO-1043", "Brightline IT Services", "Laptop refresh", 6, 0, "J. Marsh", "2025-09-12"),
    ("PO-1045", "M. Okafor Consulting", "Process review", 1, 0, "A. Reyes", "2025-08-30")]
_b = {b[5]: b for b in BILLS if b[5]}
PO = [(p, v, it, q, up if up else round(_b[p][4] / q, 2), ab, ao) for p, v, it, q, up, ab, ao in PO]
GRN = [("GRN-771", "PO-1040", "2025-09-04", 4000, "good"), ("GRN-772", "PO-1041", "2025-09-07", 90, "good"),      # 90 of 100 received, billed 100
       ("GRN-774", "PO-1043", "2025-09-10", 6, "good")]                                                             # received before PO approval; PO-1042/1045 none
AP_PAID = []                                    # vendor, bill_no, bill_date, due_date, paid_date, amount (12 months)
for k, v in enumerate(VENDORS[:8]):
    for j in range(4):
        i = 26 + 2 * j; y, m = MONTHS[i]; early = 12 if k in (0, 1) else 0
        AP_PAID.append((v[0], f"{3000 + 50 * k + j}", f"{y}-{m:02d}-05", f"{y}-{m:02d}-{5 + v[1] if 5 + v[1] <= 28 else 28:02d}",
                        f"{y}-{m:02d}-{max(5 + v[1] - early, 6) if 5 + v[1] - early <= 28 else 28:02d}", round(v[5] / 12)))

# ---- bank --------------------------------------------------------------------------
BANK = [  # date, description, amount (+in / -out)
    ("2025-09-02", "ACH CREDIT PENNINE RETAIL GROUP", 41200), ("2025-09-03", "CHECK 2287", -8400), ("2025-09-05", "STRIPE TRANSFER", 18842),
    ("2025-09-08", "ACH DEBIT HALDEN PROPERTY MGMT", -9000), ("2025-09-10", "ACH CREDIT CASTLETON FOODS", 36100),
    ("2025-09-12", "PAYROLL NORTHBROOK TRADING", -52310), ("2025-09-15", "WIRE OUT KESTREL SUPPLIES", -64200), ("2025-09-15", "WIRE FEE", -35),
    ("2025-09-17", "ACH CREDIT RIDGEWAY LOGISTICS", 27950), ("2025-09-19", "STRIPE TRANSFER", 21307), ("2025-09-22", "LOAN PAYMENT TERM LOAN", -6900),
    ("2025-09-24", "ACH DEBIT UNKNOWN ORIG 88213", -1240), ("2025-09-26", "PAYROLL NORTHBROOK TRADING", -52310),
    ("2025-09-29", "ACH CREDIT ASHBY ENGINEERING", 22180), ("2025-09-30", "MONTHLY SERVICE FEE", -50)]
BANK_CLOSE = CASH_GL - 10540                 # books less deposit in transit, plus outstanding check, less two items not booked
BANK_OPEN = BANK_CLOSE - sum(a for _, _, a in BANK)
# book side: everything on the statement except the fee and the unknown debit, plus two items not yet at the bank
BOOK_ONLY = [("2025-09-29", "Check 2291 to Orchard Packaging", -3150), ("2025-09-30", "Deposit - Tideswell Hotels", 12400)]
CASH_LEDGER = [(d, t, a) for d, t, a in BANK if t not in ("MONTHLY SERVICE FEE", "ACH DEBIT UNKNOWN ORIG 88213")] + BOOK_ONLY
CASH_LEDGER_OPEN = CASH_GL - sum(a for _, _, a in CASH_LEDGER)
assert CASH_LEDGER_OPEN == BANK_OPEN

# ---- payroll, inventory, fixed assets, budget, journals ----------------------------
EMP = [("E01", "Operations", 7800), ("E02", "Operations", 5200), ("E03", "Operations", 5200), ("E04", "Sales", 6900), ("E05", "Sales", 6100),
       ("E06", "Finance", 7400), ("E07", "Finance", 4800), ("E08", "Warehouse", 4300), ("E09", "Warehouse", 4300), ("E10", "Warehouse", 4100),
       ("E11", "Admin", 3900), ("E12", "Management", 16000)]
_scale = PNL[I]["payroll"] / 1.0765 / sum(e[2] for e in EMP)
PAYROLL = [(e, d, round(g * _scale), round(g * _scale * 0.12), round(g * _scale * 0.0765), round(g * _scale * 0.04)) for e, d, g in EMP]
ITEMS = [("SB-20", "Steel bracket", 9, "2025-09-27"), ("SB-35", "Steel bracket heavy", 7, "2025-09-22"), ("C-12", "Carton 12in", 3, "2025-09-29"),
         ("C-18", "Carton 18in", 3, "2025-09-18"), ("FX-01", "Fixing kit", 11, "2025-09-25"), ("FX-02", "Fixing kit pro", 14, "2025-08-30"),
         ("HG-10", "Hinge", 5, "2025-09-20"), ("HG-22", "Hinge soft-close", 8, "2025-07-14"), ("LK-05", "Lock set", 12, "2025-09-11"),
         ("LK-09", "Lock set legacy", 6, "2024-06-03"), ("PN-40", "Panel 40mm", 10, "2025-09-26"), ("PN-55", "Panel 55mm (discontinued)", 4, "2024-02-19"),
         ("TR-01", "Trim", 6, "2025-09-16"), ("TR-07", "Trim seasonal", 3, "2024-11-28"), ("WD-02", "Wedge", 2, "2025-09-08")]
_iv = spread(INV_TOTAL, [w for _, _, w, _ in ITEMS])
FA = [("FA-001", "Warehouse racking", "2021-03-01", 96000, 10), ("FA-002", "Forklift", "2021-06-15", 54000, 7), ("FA-003", "Delivery van", "2022-01-10", 62000, 5),
      ("FA-004", "Office fit-out", "2020-09-01", 88000, 10), ("FA-005", "Servers", "2020-01-20", 36000, 5), ("FA-006", "Packing line", "2023-04-01", 58000, 8),
      ("FA-007", "Laptops batch 1", "2022-08-01", 14000, 3), ("FA-008", "Delivery van (sold Jul 2025)", "2019-05-01", 12000, 5)]
assert sum(f[3] for f in FA) == 420000
JE = [  # je_no, date, posted_on, user, account, debit, credit, memo
    ("JE-0901", "2025-09-30", "2025-10-02", "s.patel", "6600", 4200, 0, "Monthly depreciation"), ("JE-0901", "2025-09-30", "2025-10-02", "s.patel", "1510", 0, 4200, "Monthly depreciation"),
    ("JE-0902", "2025-09-30", "2025-10-02", "s.patel", "6100", 1500, 0, "Prepaid insurance release"), ("JE-0902", "2025-09-30", "2025-10-02", "s.patel", "1300", 0, 1500, "Prepaid insurance release"),
    ("JE-0903", "2025-09-30", "2025-10-03", "s.patel", "6000", 12400, 0, "Accrued wages"), ("JE-0903", "2025-09-30", "2025-10-03", "s.patel", "2100", 0, 12400, "Accrued wages"),
    ("JE-0904", "2025-09-28", "2025-09-28", "a.reyes", "1100", 50000, 0, "Revenue adjustment"), ("JE-0904", "2025-09-28", "2025-09-28", "a.reyes", "4000", 0, 50000, "Revenue adjustment"),
    ("JE-0905", "2025-08-31", "2025-09-20", "s.patel", "6400", 3800, 0, "Legal fee missed in August"), ("JE-0905", "2025-08-31", "2025-09-20", "s.patel", "2100", 0, 3800, "Legal fee missed in August"),
    ("JE-0906", "2025-09-30", "2025-10-01", "s.patel", "7000", 1900, 0, "Loan interest"), ("JE-0906", "2025-09-30", "2025-10-01", "s.patel", "2500", 0, 1900, "Loan interest"),
    ("JE-0907", "2025-09-30", "2025-10-04", "s.patel", "6200", 9999, 0, ""), ("JE-0907", "2025-09-30", "2025-10-04", "s.patel", "2100", 0, 9999, "")]

SEEDED = {
    "dup_bill": "Kestrel Supplies INV-4471 for %s appears twice in open payables (second as INV4471 under 'Kestrel Supplies Inc.')" % f"{6480:,}",
    "short_ship": "PO-1041: 100 cartons ordered and billed, 90 received (GRN-772)",
    "price_creep": "PO-1040: billed price is 1.8% above the purchase order price",
    "no_po_approval": "PO-1042 has no approver; PO-1043 was received (10 Sep) before it was approved (12 Sep)",
    "old_ar": "Harlow Fabrication INV-20418 for 48,200 is 95 days overdue; Foxhall Garden Centres is 130 days overdue",
    "ar_conc": "Harlow Fabrication is about 31% of receivables",
    "ar_credit": "Calder Print has an unapplied credit memo CM-0312 of 2,150",
    "bank_items": "Bank: check 2291 (3,150) outstanding, deposit 12,400 in transit, service fees 50 and unknown debit 1,240 not in the books",
    "je_round": "JE-0904: 50,000 round-amount revenue entry posted on a Sunday by a.reyes",
    "je_late": "JE-0905: dated 31 August, posted 20 September, after the August close",
    "je_blank": "JE-0907: 9,999 with a blank memo, just under 10,000",
    "marketing_var": "Marketing in September is about 60% over its usual share of revenue",
    "margin_dip": "Gross margin falls from 42% to 40% in the last three months",
    "dso_drift": "DSO drifts from about 42 to 52 days over 36 months; DPO falls from 38 to 33 (bills paid earlier)",
    "dead_stock": "LK-09, PN-55 and TR-07 have had no sales for more than 300 days",
    "fa_disposed": "FA-008 was sold in July 2025 and is still on the register",
    "vendor_forms": "Brightline IT Services, M. Okafor Consulting and Vale Marketing Studio were paid in 2025 with no tax form on file",
    "vendor_dup": "'Kestrel Supplies' and 'Kestrel Supplies Inc.' look like the same vendor",
    "bank_change": "Summit Freight's bank details changed on 16 September 2025",
    "payroll_clearing": "Payroll clearing carries a residual 1,200",
    "legal_oneoff": "Professional fees include a one-time 14,000 in June 2025",
    "early_pay": "Kestrel Supplies and Orchard Packaging are paid about 12 days before due",
}
