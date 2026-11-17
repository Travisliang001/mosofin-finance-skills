// One spec per workflow. build.js turns each into workflows/<name>/ and self-tests it.
// compute() runs inside the Compute node with: S (settings), R (Mosofin reads), V (file validation),
// src(readKey, fileRole, columnMap) and the lib.js helpers. It returns the envelope body.
// Nothing configurable may be written inside compute(): it all comes from S.

const BASE = { company: '', currency: 'USD', datasource: 'quickbooks', data_source_id: '' };
const CO = 'Northbrook Trading Ltd';
const csv = (rows) => rows.map((r) => r.map((c) => (/[",\n]/.test(String(c)) ? `"${String(c).replace(/"/g, '""')}"` : c)).join(',')).join('\n');
const WRONG_BANK = { name: 'statement-export.csv', role: '', content: csv([['Date', 'Description', 'Amount'], ['2025-09-02', 'CARD 4411 FUEL', '-82.10'], ['2025-09-03', 'TRANSFER IN', '5000.00']]) };
const wrong = (role, name) => ({ ...WRONG_BANK, role, name: name || WRONG_BANK.name });

module.exports = [
// ───────────────────────────────────────────── 05 AR collections (built first: highest value)
{
  id: '05', name: 'ar-collections', title: 'AR collections sequencer',
  description: 'Weekly: reads open receivables, nets unapplied credits, and drafts one collection email per overdue customer, toned by how late the oldest item is. Flags customers over their credit limit.',
  trigger: 'schedule+webhook', schedule: '0 7 * * 1',
  settings: { ...BASE, as_at: '', buckets: [30, 60, 90], min_balance: 50, exclude_customers: [], credit_limits: {},
    tones: { '1-30': 'friendly reminder', '31-60': 'firm reminder', '61-90': 'final notice', '90+': 'escalation: account on hold pending payment', default: 'reminder' },
    sender_name: 'Accounts Receivable',
    subject_template: '{{company}}: {{currency}} {{net}} overdue ({{tone}})',
    body_template: 'Hello {{customer}},\n\nOur records show the following invoices are past due:\n\n{{lines}}\n\nAfter credits of {{currency}} {{credit}}, {{currency}} {{net}} is outstanding. Please arrange payment or let us know if anything is in dispute.\n\nThank you,\n{{sender}}' },
  settingNotes: { buckets: 'Aging bucket upper bounds in days; the oldest overdue item picks the bucket', min_balance: 'No draft when the net overdue balance is below this', exclude_customers: 'Customer names never chased (e.g. in dispute, legal)', credit_limits: '{ "Customer": limit } — flagged when the open balance exceeds it', tones: 'Tone per bucket label; used in the subject and body', subject_template: 'Email subject; {{placeholders}} filled per customer', body_template: 'Email body; {{lines}} lists the overdue invoices', sender_name: 'Signature on the draft' },
  reads: [{ key: 'invoices', tool: 'search_invoices', params: { status: 'Open' } }, { key: 'credits', tool: 'search_payments', params: { unapplied: true } }],
  optionalReads: ['credits'],
  fileSpec: {
    ar_open: { required: false, what: 'open A/R invoice list', columns: [['customer', 'customer_name'], ['invoice', 'invoice_no', 'doc_number'], ['balance', 'open_balance', 'amount_due'], ['due_date', 'due']] },
    credits: { required: false, what: 'unapplied credits / payments list', columns: [['customer', 'customer_name'], ['amount', 'unapplied']] },
  },
  compute() {
    const asAt = S.as_at || S.run_at.slice(0, 10);
    const inv = src('invoices', 'ar_open', { customer: ['customer', 'customer_name', 'CustomerRef'], no: ['invoice', 'invoice_no', 'doc_number', 'DocNumber'], bal: ['balance', 'open_balance', 'amount_due', 'Balance'], due: ['due_date', 'due', 'DueDate'], email: ['email', 'bill_email', 'BillEmail'] }).rows;
    const cr = src('credits', 'credits', { customer: ['customer', 'customer_name', 'CustomerRef'], amt: ['amount', 'unapplied', 'UnappliedAmt'] }).rows;
    if (!inv.length) return { status: 'error', blocked: true, summary: 'No open receivables from Mosofin or a file; nothing to chase.' };
    const b = S.buckets;
    const bucket = (d) => { for (let i = 0; i < b.length; i++) if (d <= b[i]) return (i ? b[i - 1] + 1 : 1) + '-' + b[i]; return b[b.length - 1] + '+'; };
    const excluded = S.exclude_customers.map(normName);
    const by = {};
    for (const r of inv) (by[normName(r.customer)] = by[normName(r.customer)] || { customer: r.customer, email: r.email || null, items: [] }).items.push({ no: r.no, bal: num(r.bal), due: r.due, days: daysBetween(r.due, asAt) });
    const findings = [], actions = [];
    for (const [k, c] of Object.entries(by)) {
      const gross = sum(c.items, (x) => x.bal);
      const credit = sum(cr.filter((x) => normName(x.customer) === k), (x) => x.amt);
      const net = r2(gross - credit);
      const lim = Object.entries(S.credit_limits).find(([n]) => normName(n) === k);
      if (lim && gross > num(lim[1])) findings.push({ type: 'over_credit_limit', customer: c.customer, open_balance: gross, credit_limit: num(lim[1]), excess: r2(gross - num(lim[1])) });
      if (excluded.includes(k)) { findings.push({ type: 'excluded_customer', customer: c.customer, open_balance: gross }); continue; }
      const overdue = c.items.filter((x) => x.days > 0);
      if (!overdue.length) continue;
      const overdueAmt = sum(overdue, (x) => x.bal), due = r2(Math.min(net, overdueAmt));
      if (credit) findings.push({ type: 'unapplied_credit_netted', customer: c.customer, credit, overdue: overdueAmt, net_due: due });
      if (due < S.min_balance) { findings.push({ type: 'below_min_balance', customer: c.customer, net_due: due, min_balance: S.min_balance }); continue; }
      const worst = Math.max(...overdue.map((x) => x.days)), bk = bucket(worst), tone = S.tones[bk] || S.tones.default;
      const lines = overdue.map((x) => `  ${x.no}  due ${x.due}  ${S.currency} ${x.bal.toFixed(2)}  (${x.days} days overdue)`).join('\n');
      const v = { customer: c.customer, company: S.company, currency: S.currency, net: due.toFixed(2), credit: credit.toFixed(2), lines, tone, days: worst, sender: S.sender_name };
      actions.push({ type: 'email_draft', channel: 'email', customer: c.customer, to: c.email, bucket: bk, oldest_days_overdue: worst, amount_due: due, invoices: overdue.map((x) => x.no), subject: fill(S.subject_template, v), body: fill(S.body_template, v) });
      if (!c.email) findings.push({ type: 'no_email_on_file', customer: c.customer });
    }
    const open = sum(inv, (x) => x.bal);
    return { period: asAt, summary: `${actions.length} collection draft(s) across ${Object.keys(by).length} customer(s); ${S.currency} ${open.toFixed(2)} open, ${S.currency} ${sum(actions, (a) => a.amount_due).toFixed(2)} being chased.`,
      findings, proposed_actions: actions, totals: { open_balance: open, customers: Object.keys(by).length, drafts: actions.length, amount_chased: sum(actions, (a) => a.amount_due) } };
  },
  logic: ['Groups open invoices by customer; ages each against `as_at`.', 'Nets unapplied credits off the overdue amount; skips customers whose net is below `min_balance` and anyone on `exclude_customers`.', 'One draft per customer listing every overdue invoice; the oldest item picks the bucket and the tone.', 'Flags any customer whose open balance exceeds their `credit_limits` entry.'],
  outputNotes: ['`proposed_actions[]`: `email_draft` with `to`, `subject`, `body`, `amount_due`, `invoices[]` — ready for an email connector after approval.', '`findings[]`: `over_credit_limit`, `unapplied_credit_netted`, `below_min_balance`, `excluded_customer`, `no_email_on_file`.'],
  sampleInput: { settings: { company: CO, as_at: '2025-09-30', credit_limits: { 'Harlow Retail': 40000 }, exclude_customers: ['Corran Ltd'] }, files: [
    { name: 'open-invoices-2025-09-30.csv', role: 'ar_open', company: CO, content: csv([['customer', 'invoice_no', 'invoice_date', 'due_date', 'balance', 'email'],
      ['Harlow Retail', 'INV-1031', '2025-06-10', '2025-07-10', '18400.00', 'ap@harlowretail.example'], ['Harlow Retail', 'INV-1058', '2025-08-05', '2025-09-04', '24650.00', 'ap@harlowretail.example'],
      ['Bexley Foods', 'INV-1062', '2025-08-12', '2025-09-11', '1200.00', 'accounts@bexley.example'], ['Corran Ltd', 'INV-0977', '2025-04-02', '2025-05-02', '6300.00', ''],
      ['Dunmore Hotels', 'INV-1080', '2025-09-15', '2025-10-15', '9100.00', 'pay@dunmore.example'], ['Ellis & Co', 'INV-1012', '2025-06-15', '2025-07-17', '3875.50', '']]) },
    wrong('credits'),
    { name: 'unapplied-credits.csv', role: 'credits', company: CO, content: csv([['customer', 'amount', 'date'], ['Bexley Foods', '1180.00', '2025-09-20']]) }] },
  expect: { status: 'partial', find: ['over_credit_limit', 'unapplied_credit_netted', 'below_min_balance', 'excluded_customer'], actions: ['email_draft'], rejected: ['statement-export.csv'],
    check: (e) => (e.proposed_actions.length === 2 ? null : `expected 2 drafts (Harlow, Ellis), got ${e.proposed_actions.length}`) },
},
// ───────────────────────────────────────────── 02 Bank reconciliation
{
  id: '02', name: 'bank-reconciliation', title: 'Bank reconciliation',
  description: 'Matches a bank statement against the cash account in the books. Exact-amount matches within a date window are paired; everything else is an exception on one side. Bank-only fees and interest come back as proposed journal entries.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, cash_account: '1000 Operating Cash', period_start: '', period_end: '', date_window_days: 5,
    bank_charge_keywords: ['fee', 'charge', 'interest', 'service'], bank_fee_account: '6900 Bank Charges', interest_income_account: '4900 Interest Income', statement_closing_balance: null, book_closing_balance: null },
  settingNotes: { cash_account: 'GL cash account to reconcile (name or number as Mosofin returns it)', date_window_days: 'Max days between bank and book dates for an exact-amount match', bank_charge_keywords: 'Bank-only lines whose description contains one of these get a proposed journal entry', bank_fee_account: 'Debit account for proposed fee entries', interest_income_account: 'Credit account for proposed interest entries', statement_closing_balance: 'Optional; with book_closing_balance, proves the reconciliation ties', book_closing_balance: 'Optional; GL cash balance at period end' },
  reads: [{ key: 'gl', tool: 'get_general_ledger', params: { account: '$cash_account', start_date: '$period_start', end_date: '$period_end' } }],
  fileSpec: {
    bank_statement: { required: true, what: 'bank statement', columns: [['date', 'posted_date', 'transaction_date'], ['amount'], ['description', 'memo', 'payee', 'details']] },
    gl_cash: { required: false, what: 'cash account ledger', columns: [['date', 'txn_date'], ['amount', 'net'], ['description', 'memo', 'name'], ['ref', 'num', 'doc_number', 'type']] },
  },
  compute() {
    const bank = src(null, 'bank_statement', { date: ['date', 'posted_date', 'transaction_date'], amt: ['amount'], desc: ['description', 'memo', 'payee', 'details'] }).rows.map((r, i) => ({ id: 'B' + (i + 1), date: r.date, amt: num(r.amt), desc: r.desc }));
    const gl = src('gl', 'gl_cash', { date: ['date', 'txn_date', 'TxnDate'], amt: ['amount', 'net', 'Amount'], desc: ['description', 'memo', 'name', 'Memo'], ref: ['ref', 'num', 'doc_number', 'DocNumber'] }).rows.map((r, i) => ({ id: 'G' + (i + 1), date: r.date, amt: num(r.amt), desc: r.desc, ref: r.ref || null }));
    if (!bank.length) return { status: 'error', blocked: true, summary: 'No usable bank statement; the reconciliation cannot run without one.' };
    if (!gl.length) return { status: 'error', blocked: true, summary: 'No cash ledger from Mosofin or a file; nothing to reconcile against.' };
    const used = new Set(), pairs = [];
    for (const b of bank) {
      const g = gl.filter((g) => !used.has(g.id) && Math.abs(g.amt - b.amt) < 0.005 && Math.abs(daysBetween(g.date, b.date)) <= S.date_window_days)
        .sort((x, y) => Math.abs(daysBetween(x.date, b.date)) - Math.abs(daysBetween(y.date, b.date)))[0];
      if (g) { used.add(g.id); b.m = g.id; pairs.push({ bank: b.id, book: g.id, amount: b.amt, days_apart: Math.abs(daysBetween(g.date, b.date)) }); }
    }
    const feeRe = new RegExp(S.bank_charge_keywords.join('|'), 'i');
    const findings = [], actions = [];
    for (const b of bank.filter((b) => !b.m)) {
      const near = gl.filter((g) => !used.has(g.id) && Math.abs(g.amt - b.amt) < 0.005).map((g) => ({ book: g.id, date: g.date, days_apart: Math.abs(daysBetween(g.date, b.date)) }));
      const isFee = feeRe.test(b.desc || '');
      findings.push({ type: isFee ? 'bank_charge_not_in_books' : 'in_bank_not_in_books', date: b.date, amount: b.amt, description: b.desc, candidates_outside_window: near });
      if (isFee) actions.push({ type: 'journal_entry', date: b.date, memo: `Bank ${b.amt < 0 ? 'charge' : 'interest'}: ${b.desc}`, lines: b.amt < 0
        ? [{ account: S.bank_fee_account, debit: -b.amt, credit: 0 }, { account: S.cash_account, debit: 0, credit: -b.amt }]
        : [{ account: S.cash_account, debit: b.amt, credit: 0 }, { account: S.interest_income_account, debit: 0, credit: b.amt }] });
    }
    for (const g of gl.filter((g) => !used.has(g.id))) findings.push({ type: g.amt < 0 ? 'outstanding_payment' : 'deposit_in_transit', date: g.date, amount: g.amt, description: g.desc, ref: g.ref });
    const t = { bank_lines: bank.length, book_lines: gl.length, matched: pairs.length, bank_only_total: sum(bank.filter((b) => !b.m), (b) => b.amt), book_only_total: sum(gl.filter((g) => !used.has(g.id)), (g) => g.amt), matched_pairs: pairs };
    const not_done = [];
    if (S.statement_closing_balance != null && S.book_closing_balance != null) {
      const diff = r2(num(S.statement_closing_balance) + t.book_only_total - (num(S.book_closing_balance) + t.bank_only_total));
      t.unexplained_difference = diff;
      if (Math.abs(diff) >= 0.01) findings.push({ type: 'reconciliation_does_not_tie', statement_balance: num(S.statement_closing_balance), book_balance: num(S.book_closing_balance), unexplained: diff });
    } else not_done.push('Closing balances not supplied (statement_closing_balance, book_closing_balance): the tie-out proof was not run.');
    return { period: `${S.period_start} to ${S.period_end}`, summary: `${pairs.length} matched; ${bank.length - pairs.length} bank-only and ${gl.length - used.size} book-only item(s); ${actions.length} proposed fee/interest entr${actions.length === 1 ? 'y' : 'ies'}.`, findings, proposed_actions: actions, totals: t, not_done };
  },
  logic: ['Validates the statement first; without a usable statement the run stops with `status: "error"`.', 'Pairs bank and book lines with the exact same amount within `date_window_days`, closest date first.', 'Unmatched bank lines: fees/interest (by `bank_charge_keywords`) get a proposed journal entry; the rest are listed with any same-amount candidates outside the window.', 'Unmatched book lines become outstanding payments or deposits in transit.', 'With both closing balances set, proves the reconciliation ties and reports any unexplained difference.'],
  outputNotes: ['`proposed_actions[]`: `journal_entry` (balanced lines) for bank-only fees and interest only.', '`findings[]`: `bank_charge_not_in_books`, `in_bank_not_in_books`, `outstanding_payment`, `deposit_in_transit`, `reconciliation_does_not_tie`.', '`totals.matched_pairs` lists every pairing.'],
  sampleInput: { settings: { company: CO, period_start: '2025-09-01', period_end: '2025-09-30', statement_closing_balance: 151885.0, book_closing_balance: 147545.0 }, files: [
    { name: 'operating-account-sept-2025.csv', role: 'bank_statement', company: CO, content: csv([['date', 'description', 'amount'],
      ['2025-09-02', 'HARLOW RETAIL PAYMENT', '18400.00'], ['2025-09-05', 'PAYROLL NET PAY', '-42350.00'], ['2025-09-09', 'KESTREL SUPPLY CO', '-6210.00'],
      ['2025-09-15', 'ACH BEXLEY FOODS', '2350.00'], ['2025-09-30', 'MONTHLY SERVICE FEE', '-45.00'], ['2025-09-30', 'WIRE FEE', '-15.00']]) }] },
  sampleReads: { gl: [
    { date: '2025-09-01', amount: 18400.0, memo: 'Harlow Retail receipt', doc_number: 'RCPT-311' }, { date: '2025-09-04', amount: -42350.0, memo: 'September payroll', doc_number: 'PR-09' },
    { date: '2025-09-08', amount: -6210.0, memo: 'Kestrel Supply bill pay', doc_number: 'CHK-2207' }, { date: '2025-09-14', amount: 2350.0, memo: 'Bexley Foods receipt', doc_number: 'RCPT-318' },
    { date: '2025-09-26', amount: -4400.0, memo: 'Orchard Lane Properties rent', doc_number: 'CHK-2214' }] },
  expect: { status: 'ok', find: ['bank_charge_not_in_books', 'outstanding_payment'], actions: ['journal_entry'], check: (e) => (e.totals.unexplained_difference === 0 ? null : `does not tie: ${e.totals.unexplained_difference}`) },
},
// ───────────────────────────────────────────── 03 Three-way match
{
  id: '03', name: 'three-way-match', title: 'Three-way match',
  description: 'Checks each bill line against its purchase order and goods-received record. Price and quantity variances over tolerance, bills with no PO line, and billing beyond what was received come back as exceptions with a proposed hold.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, price_tolerance_pct: 2, qty_tolerance: 0 },
  settingNotes: { price_tolerance_pct: 'Allowed unit-price difference vs the PO, in percent', qty_tolerance: 'Units a bill may exceed the received (or ordered) quantity by' },
  reads: [{ key: 'bills', tool: 'search_bills', params: { status: 'Open' } }],
  fileSpec: {
    purchase_orders: { required: true, what: 'purchase order lines', columns: [['po', 'po_number'], ['item', 'sku'], ['qty', 'quantity'], ['unit_price', 'price']] },
    receipts: { required: false, what: 'goods received lines', columns: [['po', 'po_number'], ['item', 'sku'], ['qty_received', 'qty', 'quantity']] },
    bills: { required: false, what: 'bill lines', columns: [['bill', 'bill_no', 'invoice'], ['po', 'po_number'], ['item', 'sku'], ['qty', 'quantity'], ['unit_price', 'price']] },
  },
  compute() {
    const M = { po: ['po', 'po_number', 'PONumber'], item: ['item', 'sku'], qty: ['qty', 'quantity', 'qty_received'], price: ['unit_price', 'price', 'rate'], bill: ['bill', 'bill_no', 'invoice', 'DocNumber'], vendor: ['vendor', 'vendor_name'] };
    const po = src(null, 'purchase_orders', M).rows, rc = src(null, 'receipts', M).rows, bl = src('bills', 'bills', M).rows.filter((b) => b.item);
    if (!po.length) return { status: 'error', blocked: true, summary: 'No purchase orders supplied; nothing to match against.' };
    if (!bl.length) return { status: 'error', blocked: true, summary: 'No bill lines from Mosofin or a file.' };
    const k = (r) => normNo(r.po) + '|' + normName(r.item), threeWay = rc.length > 0;
    const findings = [], holds = {};
    if (!threeWay) findings.push({ type: 'two_way_only', detail: 'No goods-received records supplied: quantities were checked against the PO, not against what was received. This is not a three-way match.' });
    let clean = 0;
    for (const b of bl) {
      const p = po.find((x) => k(x) === k(b)), base = { bill: b.bill, vendor: b.vendor || null, po: b.po, item: b.item };
      if (!p) { findings.push({ type: 'no_matching_po_line', ...base, billed_value: r2(num(b.qty) * num(b.price)) }); holds[b.bill] = 'no_matching_po_line'; continue; }
      let ok = true;
      const pv = num(p.price) ? ((num(b.price) - num(p.price)) / num(p.price)) * 100 : 0;
      if (Math.abs(pv) > S.price_tolerance_pct) { ok = false; holds[b.bill] = 'price_variance'; findings.push({ type: 'price_variance', ...base, po_price: num(p.price), bill_price: num(b.price), variance_pct: r2(pv), value: r2((num(b.price) - num(p.price)) * num(b.qty)) }); }
      const against = threeWay ? sum(rc.filter((x) => k(x) === k(b)), (x) => x.qty) : num(p.qty);
      if (num(b.qty) - against > S.qty_tolerance) { ok = false; holds[b.bill] = holds[b.bill] || 'quantity'; findings.push({ type: threeWay ? 'billed_more_than_received' : 'billed_more_than_ordered', ...base, billed_qty: num(b.qty), [threeWay ? 'received_qty' : 'ordered_qty']: against, value: r2((num(b.qty) - against) * num(b.price)) }); }
      if (ok) clean++;
    }
    const ex = findings.filter((f) => f.bill).length;
    return { summary: `${clean} of ${bl.length} bill line(s) match (${threeWay ? 'three-way' : 'two-way only'}); ${ex} exception(s) on ${Object.keys(holds).length} bill(s).`, findings,
      proposed_actions: Object.entries(holds).map(([bill, reason]) => ({ type: 'hold_bill', bill, reason })), totals: { bill_lines: bl.length, clean_lines: clean, exceptions: ex, value_at_issue: sum(findings, (f) => f.value || f.billed_value || 0) } };
  },
  logic: ['Purchase orders are required; bill lines come from Mosofin, or a file if Mosofin has none.', 'Each bill line is matched to its PO line by PO number + item.', 'Price: flags a unit-price difference over `price_tolerance_pct`.', 'Quantity: billed vs received (three-way). With no receipts file it checks billed vs ordered and says plainly that it is two-way only.'],
  outputNotes: ['`proposed_actions[]`: `hold_bill` per bill with an exception.', '`findings[]`: `price_variance`, `billed_more_than_received` / `billed_more_than_ordered`, `no_matching_po_line`, `two_way_only`.'],
  sampleInput: { settings: { company: CO }, files: [
    { name: 'po-lines.csv', role: 'purchase_orders', company: CO, content: csv([['po_number', 'vendor', 'item', 'qty', 'unit_price'], ['PO-5521', 'Kestrel Supply Co', 'Pallet wrap', '200', '12.50'], ['PO-5521', 'Kestrel Supply Co', 'Corner boards', '500', '1.10'], ['PO-5530', 'Ashby Metals', 'Steel shelving', '20', '310.00']]) },
    { name: 'goods-received.csv', role: 'receipts', company: CO, content: csv([['po_number', 'item', 'qty_received', 'date'], ['PO-5521', 'Pallet wrap', '200', '2025-09-10'], ['PO-5521', 'Corner boards', '450', '2025-09-10'], ['PO-5530', 'Steel shelving', '20', '2025-09-18']]) },
    { name: 'bill-lines.csv', role: 'bills', company: CO, content: csv([['bill_no', 'vendor', 'po_number', 'item', 'qty', 'unit_price'], ['KS-8812', 'Kestrel Supply Co', 'PO-5521', 'Pallet wrap', '200', '12.50'], ['KS-8812', 'Kestrel Supply Co', 'PO-5521', 'Corner boards', '500', '1.10'], ['AM-2290', 'Ashby Metals', 'PO-5530', 'Steel shelving', '20', '328.00'], ['AM-2291', 'Ashby Metals', 'PO-5544', 'Bolts', '1000', '0.20']]) }] },
  expect: { status: 'ok', find: ['price_variance', 'billed_more_than_received', 'no_matching_po_line'], actions: ['hold_bill'] },
},
// ───────────────────────────────────────────── 04 Duplicate invoice detection
{
  id: '04', name: 'duplicate-invoice-detection', title: 'Duplicate invoice detection',
  description: 'Scans bills (open and paid) for likely duplicates: the same vendor with the same invoice number once punctuation and prefixes are stripped, or the same vendor and amount within a few days. Each pair comes back with a proposed hold on the later bill.',
  trigger: 'schedule+webhook', schedule: '0 6 * * *',
  settings: { ...BASE, as_at: '', lookback_days: 365, near_days: 7, amount_tolerance: 0.01 },
  settingNotes: { lookback_days: 'Only bills dated within this many days of as_at are compared', near_days: 'Same vendor + same amount within this many days counts as a possible duplicate', amount_tolerance: 'Amounts this close count as equal' },
  reads: [{ key: 'bills', tool: 'search_bills', params: {} }],
  fileSpec: { bills: { required: false, what: 'bill register', columns: [['vendor', 'vendor_name'], ['bill_no', 'invoice', 'doc_number', 'bill'], ['amount', 'total'], ['date', 'bill_date']] } },
  compute() {
    const asAt = S.as_at || S.run_at.slice(0, 10);
    const all = src('bills', 'bills', { vendor: ['vendor', 'vendor_name', 'VendorRef'], no: ['bill_no', 'invoice', 'doc_number', 'bill', 'DocNumber'], amt: ['amount', 'total', 'TotalAmt'], date: ['date', 'bill_date', 'TxnDate'], status: ['status'] }).rows;
    if (!all.length) return { status: 'error', blocked: true, summary: 'No bills from Mosofin or a file.' };
    const rows = all.filter((r) => { const d = daysBetween(r.date, asAt); return d == null || (d >= 0 && d <= S.lookback_days); });
    const f = [];
    for (let i = 0; i < rows.length; i++) for (let j = i + 1; j < rows.length; j++) {
      const a = rows[i], b = rows[j];
      if (normName(a.vendor) !== normName(b.vendor)) continue;
      const sameNo = !!normNo(a.no) && normNo(a.no) === normNo(b.no), sameAmt = Math.abs(num(a.amt) - num(b.amt)) <= S.amount_tolerance;
      const gap = Math.abs(daysBetween(a.date, b.date) ?? 9999);
      if (!(sameNo || (sameAmt && gap <= S.near_days))) continue;
      const [x, y] = day(a.date) <= day(b.date) ? [a, b] : [b, a];
      const side = (r) => ({ bill_no: r.no, date: r.date, amount: num(r.amt), status: r.status || null });
      f.push({ type: sameNo ? 'same_invoice_number' : 'same_amount_near_date', confidence: sameNo && sameAmt ? 'high' : 'medium', vendor: a.vendor, first: side(x), second: side(y), days_apart: gap, amount_at_risk: num(y.amt) });
    }
    return { period: asAt, summary: `${f.length} possible duplicate pair(s) among ${rows.length} bill(s) from the last ${S.lookback_days} days.`, findings: f,
      proposed_actions: f.map((x) => ({ type: 'hold_bill', vendor: x.vendor, bill: x.second.bill_no, reason: `${x.type} with ${x.first.bill_no}`, note: x.second.status && /paid/i.test(x.second.status) ? 'already paid: request a credit or refund instead of a hold' : null })),
      totals: { bills_checked: rows.length, pairs: f.length, amount_at_risk: sum(f, (x) => x.amount_at_risk) } };
  },
  logic: ['Takes bills from Mosofin (file fallback) within `lookback_days`, open and paid alike.', 'A pair is flagged when the vendor matches and either the invoice numbers match after normalising (`INV-4471` = `INV4471` = `4471`), or the amounts match within `near_days`.', 'Confidence is high when both number and amount match.'],
  outputNotes: ['`findings[]`: `same_invoice_number` / `same_amount_near_date` with both bills side by side.', '`proposed_actions[]`: `hold_bill` on the later bill (or a refund note if it is already paid).'],
  sampleInput: { settings: { company: CO, as_at: '2025-09-30' } },
  sampleReads: { bills: [
    { vendor: 'Kestrel Supply Co', doc_number: 'INV-4471', date: '2025-09-03', amount: 6210.0, status: 'Paid' }, { vendor: 'Kestrel Supply Co.', doc_number: 'INV4471', date: '2025-09-17', amount: 6210.0, status: 'Open' },
    { vendor: 'Ashby Metals', doc_number: 'AM-2290', date: '2025-09-18', amount: 6560.0, status: 'Open' }, { vendor: 'Ashby Metals', doc_number: 'AM-2301', date: '2025-09-22', amount: 6560.0, status: 'Open' },
    { vendor: 'Orchard Lane Properties', doc_number: 'RENT-0925', date: '2025-09-01', amount: 4400.0, status: 'Paid' }, { vendor: 'Orchard Lane Properties', doc_number: 'RENT-0825', date: '2025-08-01', amount: 4400.0, status: 'Paid' }] },
  expect: { status: 'ok', find: ['same_invoice_number', 'same_amount_near_date'], actions: ['hold_bill'], check: (e) => (e.findings.length === 2 ? null : `expected 2 pairs (rent a month apart is not one), got ${e.findings.length}`) },
},
// ───────────────────────────────────────────── 09 Cash application
{
  id: '09', name: 'cash-application', title: 'Cash application matcher',
  description: 'Proposes which open invoices each customer payment pays: invoice numbers in the remittance first, then an exact single-invoice amount, then a combination of up to three of that customer\'s invoices. Anything ambiguous is left for a person with the candidates listed.',
  trigger: 'webhook', blockOnMissing: false,
  settings: { ...BASE, amount_tolerance: 0.01, max_combination: 3 },
  settingNotes: { amount_tolerance: 'Amounts this close count as equal', max_combination: 'Largest number of invoices one payment may be split across (2 or 3)' },
  reads: [{ key: 'invoices', tool: 'search_invoices', params: { status: 'Open' } }, { key: 'payments', tool: 'search_payments', params: { unapplied: true } }],
  fileSpec: {
    payments: { required: false, what: 'customer receipts / remittance list', columns: [['payer', 'customer', 'customer_name'], ['amount'], ['date']] },
    invoices: { required: false, what: 'open A/R invoice list', columns: [['customer', 'customer_name'], ['invoice', 'invoice_no', 'doc_number'], ['balance', 'open_balance', 'amount_due']] },
  },
  compute() {
    const inv = src('invoices', 'invoices', { customer: ['customer', 'customer_name', 'CustomerRef'], no: ['invoice', 'invoice_no', 'doc_number', 'DocNumber'], bal: ['balance', 'open_balance', 'amount_due', 'Balance'] }).rows.map((r) => ({ customer: r.customer, no: r.no, bal: num(r.bal) }));
    const pay = src('payments', 'payments', { payer: ['payer', 'customer', 'customer_name', 'CustomerRef'], amt: ['amount', 'TotalAmt'], date: ['date', 'TxnDate'], memo: ['memo', 'reference', 'remittance', 'description', 'PrivateNote'] }).rows.map((r) => ({ payer: r.payer, amount: num(r.amt), date: r.date, memo: r.memo || '' }));
    if (!pay.length) return { status: 'error', blocked: true, summary: 'No customer payments from Mosofin or a file; nothing to apply.' };
    if (!inv.length) return { status: 'error', blocked: true, summary: 'No open invoices from Mosofin or a file; nothing to apply against.' };
    const eq = (a, b) => Math.abs(a - b) <= S.amount_tolerance, used = new Set(), actions = [], findings = [];
    const combos = (c, amt) => { const n = c.length, m = S.max_combination;
      for (let a = 0; a < n; a++) for (let b = a + 1; b < n; b++) { if (m >= 2 && eq(c[a].bal + c[b].bal, amt)) return [c[a], c[b]]; if (m >= 3) for (let d = b + 1; d < n; d++) if (eq(c[a].bal + c[b].bal + c[d].bal, amt)) return [c[a], c[b], c[d]]; } return null; };
    for (const p of pay) {
      const open = inv.filter((i) => !used.has(i.no)), mine = open.filter((i) => normName(i.customer) === normName(p.payer));
      const tokens = p.memo.toUpperCase().split(/[^A-Z0-9-]+/).map(normNo).filter(Boolean);
      const memoHits = open.filter((i) => normNo(i.no) && tokens.includes(normNo(i.no)));
      let pickd = null, basis = null;
      if (memoHits.length && eq(sum(memoHits, (x) => x.bal), p.amount)) { pickd = memoHits; basis = 'invoice numbers in the remittance'; }
      else {
        const sameAmt = mine.filter((i) => eq(i.bal, p.amount));
        if (sameAmt.length === 1) { pickd = sameAmt; basis = 'exact amount, same customer'; }
        else if (sameAmt.length > 1) { findings.push({ type: 'ambiguous_match', payment: p, candidates: sameAmt.map((i) => ({ invoice: i.no, balance: i.bal })), note: 'several invoices of this customer have exactly this amount' }); continue; }
        else { const c = combos(mine, p.amount); if (c) { pickd = c; basis = 'sum of this customer\'s invoices'; } }
      }
      if (pickd) { pickd.forEach((i) => used.add(i.no)); actions.push({ type: 'apply_payment', payer: p.payer, date: p.date, amount: p.amount, invoices: pickd.map((i) => ({ invoice: i.no, amount: i.bal })), basis }); }
      else findings.push({ type: 'unapplied_payment', payment: p, customer_open_invoices: mine.map((i) => ({ invoice: i.no, balance: i.bal })), note: mine.length ? 'amount matches no invoice or combination: short-pay, overpay or deduction?' : 'payer not found among customers with open invoices' });
    }
    const rec = sum(pay, (x) => x.amount), app = sum(actions, (x) => x.amount);
    return { summary: `${actions.length} of ${pay.length} payment(s) matched (${S.currency} ${app.toFixed(2)}); ${findings.length} need a person (${S.currency} ${r2(rec - app).toFixed(2)}).`, findings, proposed_actions: actions,
      totals: { payments: pay.length, received: rec, applied: app, unapplied: r2(rec - app) } };
  },
  logic: ['Payments and open invoices come from Mosofin, or from files.', 'Order of evidence: invoice numbers quoted in the remittance (must sum to the payment); one invoice of that customer with exactly the amount; a combination of up to `max_combination` of that customer\'s invoices.', 'Never picks between equal candidates: several same-amount invoices is an `ambiguous_match` for a person.'],
  outputNotes: ['`proposed_actions[]`: `apply_payment` with the invoices and the basis for each match.', '`findings[]`: `ambiguous_match`, `unapplied_payment` (with the customer\'s open invoices to choose from).'],
  sampleInput: { settings: { company: CO }, files: [
    { name: 'receipts-sept.csv', role: 'payments', company: CO, content: csv([['date', 'customer', 'amount', 'reference'], ['2025-09-22', 'Harlow Retail', '18400.00', 'REMIT INV-1031'], ['2025-09-23', 'Ellis & Co', '5075.50', 'payment'], ['2025-09-24', 'Bexley Foods', '600.00', ''], ['2025-09-25', 'Dunmore Hotels', '4000.00', 'part payment']]) },
    { name: 'open-invoices.csv', role: 'invoices', company: CO, content: csv([['customer', 'invoice_no', 'balance'], ['Harlow Retail', 'INV-1031', '18400.00'], ['Harlow Retail', 'INV-1058', '24650.00'], ['Ellis & Co', 'INV-1012', '3875.50'], ['Ellis & Co', 'INV-1044', '1200.00'], ['Bexley Foods', 'INV-1062', '600.00'], ['Bexley Foods', 'INV-1071', '600.00'], ['Dunmore Hotels', 'INV-1080', '9100.00']]) }] },
  expect: { status: 'ok', find: ['ambiguous_match', 'unapplied_payment'], actions: ['apply_payment'], check: (e) => (e.proposed_actions.length === 2 ? null : `expected Harlow (memo) and Ellis (combination) applied, got ${e.proposed_actions.length}`) },
},
// ───────────────────────────────────────────── 01 Invoice ingestion
{
  id: '01', name: 'invoice-ingestion', title: 'Invoice ingestion and coding',
  description: 'Turns supplier invoice lines into bill drafts: matches the vendor to the vendor list, codes each line to a GL account by keyword rules, and flags unknown vendors and lines no rule covers. Proposes the bills; enters nothing.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, default_expense_account: '6999 Uncategorised: review',
    coding_rules: [{ keyword: 'software|subscription|licen', account: '6150 Software' }, { keyword: 'freight|shipping|courier', account: '5200 Freight In' }, { keyword: 'rent|lease', account: '6100 Rent' }, { keyword: 'repair|maintenance', account: '6170 Repairs and Maintenance' }, { keyword: 'pallet|wrap|packag|corner board', account: '5100 Packaging' }] },
  settingNotes: { coding_rules: 'Ordered list of { keyword (regex), account }; first match codes the line', default_expense_account: 'Account used when no rule matches; such lines are flagged' },
  reads: [{ key: 'vendors', tool: 'search_vendors', params: {} }],
  optionalReads: ['vendors'],
  fileSpec: {
    invoice_lines: { required: true, what: 'supplier invoice lines', columns: [['vendor', 'supplier'], ['invoice_no', 'invoice', 'number'], ['description', 'item'], ['amount', 'line_amount', 'total']] },
    vendors: { required: false, what: 'vendor list', columns: [['name', 'vendor', 'display_name']] },
  },
  compute() {
    const lines = src(null, 'invoice_lines', { vendor: ['vendor', 'supplier'], no: ['invoice_no', 'invoice', 'number'], date: ['date', 'invoice_date'], due: ['due_date', 'due'], desc: ['description', 'item'], amt: ['amount', 'line_amount', 'total'] }).rows;
    if (!lines.length) return { status: 'error', blocked: true, summary: 'No readable invoice lines.' };
    const vs = src('vendors', 'vendors', { name: ['name', 'vendor', 'display_name', 'DisplayName'] });
    const findings = [], actions = [], not_done = [], groups = {};
    if (!vs.have) not_done.push('Vendor list unavailable: vendors were not checked against the books.');
    for (const l of lines) (groups[normName(l.vendor) + '|' + normNo(l.no)] = groups[normName(l.vendor) + '|' + normNo(l.no)] || { vendor: l.vendor, no: l.no, date: l.date || null, due: l.due || null, lines: [] }).lines.push(l);
    for (const g of Object.values(groups)) {
      const v = vs.have ? vs.rows.find((x) => normName(x.name) === normName(g.vendor)) : null;
      if (vs.have && !v) { findings.push({ type: 'unknown_vendor', vendor: g.vendor, invoice: g.no }); actions.push({ type: 'create_vendor', name: g.vendor, reason: `on invoice ${g.no}, not in the vendor list` }); }
      const coded = g.lines.map((l) => { const rule = S.coding_rules.find((r) => new RegExp(r.keyword, 'i').test(l.desc || ''));
        if (!rule) findings.push({ type: 'uncoded_line', vendor: g.vendor, invoice: g.no, description: l.desc, amount: num(l.amt), coded_to: S.default_expense_account });
        return { description: l.desc, amount: num(l.amt), account: rule ? rule.account : S.default_expense_account, basis: rule ? `rule "${rule.keyword}"` : 'no rule matched: review' }; });
      actions.push({ type: 'bill_draft', vendor: v ? v.name : g.vendor, vendor_on_file: vs.have ? !!v : null, bill_no: g.no, date: g.date, due_date: g.due, total: sum(coded, (x) => x.amount), lines: coded });
    }
    return { summary: `${Object.keys(groups).length} invoice(s), ${lines.length} line(s) read; ${findings.length} item(s) to review before entry.`, findings, proposed_actions: actions, not_done,
      totals: { invoices: Object.keys(groups).length, lines: lines.length, amount: sum(lines, (x) => x.amt) } };
  },
  logic: ['Input is invoice lines as CSV/rows. Scanned PDFs or images need an extraction step first (for example an LLM node before the webhook) that produces these columns.', 'Groups lines into invoices by vendor + invoice number.', 'Vendor checked against Mosofin vendors (file fallback); an unknown vendor gets a proposed `create_vendor`.', 'Each line coded by the first matching `coding_rules` keyword; unmatched lines go to `default_expense_account` and are flagged.'],
  outputNotes: ['`proposed_actions[]`: `bill_draft` per invoice (coded lines, basis per line), `create_vendor` for unknown vendors.', '`findings[]`: `unknown_vendor`, `uncoded_line`.'],
  sampleInput: { settings: { company: CO }, files: [
    { name: 'extracted-invoice-lines.csv', role: 'invoice_lines', company: CO, content: csv([['vendor', 'invoice_no', 'invoice_date', 'due_date', 'description', 'amount'],
      ['Kestrel Supply Co', 'INV-4502', '2025-09-26', '2025-10-26', 'Pallet wrap 200 rolls', '2500.00'], ['Kestrel Supply Co', 'INV-4502', '2025-09-26', '2025-10-26', 'Freight', '180.00'],
      ['Brightline Analytics', 'BA-0091', '2025-09-28', '2025-10-28', 'Annual software subscription', '4800.00'], ['Brightline Analytics', 'BA-0091', '2025-09-28', '2025-10-28', 'Onboarding workshop', '950.00']]) }] },
  sampleReads: { vendors: [{ DisplayName: 'Kestrel Supply Co' }, { DisplayName: 'Ashby Metals' }, { DisplayName: 'Orchard Lane Properties' }] },
  expect: { status: 'ok', find: ['unknown_vendor', 'uncoded_line'], actions: ['bill_draft', 'create_vendor'] },
},
// ───────────────────────────────────────────── 06 Expense receipts
{
  id: '06', name: 'expense-receipts', title: 'Expense receipt checker',
  description: 'Checks a batch of employee expense lines against policy: per-category limits, a receipt over a set amount, weekend spend and duplicates within the batch. Returns the clean lines per employee for approval and the exceptions for a person.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, category_limits: { meals: 75, hotel: 250, taxi: 60, mileage: 200, other: 500 }, receipt_required_over: 25, flag_weekends: true, duplicate_window_days: 0 },
  settingNotes: { category_limits: 'Per-line limit by category; a category not listed uses `other`', receipt_required_over: 'Lines above this need a receipt', flag_weekends: 'Flag spend dated Saturday or Sunday', duplicate_window_days: 'Same employee, merchant and amount within this many days is a duplicate (0 = same day)' },
  reads: [],
  fileSpec: { expenses: { required: true, what: 'expense report lines', columns: [['employee', 'name'], ['date'], ['merchant', 'vendor'], ['category'], ['amount']] } },
  compute() {
    const rows = src(null, 'expenses', { emp: ['employee', 'name'], date: ['date'], merchant: ['merchant', 'vendor'], cat: ['category'], amt: ['amount'], receipt: ['receipt', 'receipt_attached', 'has_receipt'] }).rows.map((r, i) => ({ line: i + 1, emp: r.emp, date: r.date, merchant: r.merchant, cat: String(r.cat || 'other').toLowerCase(), amt: num(r.amt), receipt: /^(y|yes|true|1)$/i.test(String(r.receipt || '')) }));
    if (!rows.length) return { status: 'error', blocked: true, summary: 'No readable expense lines.' };
    const findings = [], bad = new Set();
    const flag = (r, type, extra) => { bad.add(r.line); findings.push({ type, line: r.line, employee: r.emp, date: r.date, merchant: r.merchant, category: r.cat, amount: r.amt, ...extra }); };
    for (const r of rows) {
      const lim = S.category_limits[r.cat] ?? S.category_limits.other;
      if (lim != null && r.amt > lim) flag(r, 'over_policy_limit', { limit: lim, excess: r2(r.amt - lim) });
      if (r.amt > S.receipt_required_over && !r.receipt) flag(r, 'missing_receipt', { threshold: S.receipt_required_over });
      const d = day(r.date); if (S.flag_weekends && d && [0, 6].includes(d.getUTCDay())) flag(r, 'weekend_expense', {});
    }
    for (let i = 0; i < rows.length; i++) for (let j = i + 1; j < rows.length; j++) { const a = rows[i], b = rows[j];
      if (normName(a.emp) === normName(b.emp) && normName(a.merchant) === normName(b.merchant) && Math.abs(a.amt - b.amt) < 0.005 && Math.abs(daysBetween(a.date, b.date)) <= S.duplicate_window_days) flag(b, 'duplicate_in_batch', { duplicate_of_line: a.line }); }
    const byEmp = {};
    for (const r of rows) { const e = (byEmp[r.emp] = byEmp[r.emp] || { employee: r.emp, clean: [], held: 0 }); if (bad.has(r.line)) e.held = r2(e.held + r.amt); else e.clean.push(r); }
    const actions = Object.values(byEmp).filter((e) => e.clean.length).map((e) => ({ type: 'approve_reimbursement', employee: e.employee, amount: sum(e.clean, (x) => x.amt), lines: e.clean.map((x) => x.line), held_amount: e.held }));
    return { summary: `${rows.length} line(s) from ${Object.keys(byEmp).length} employee(s); ${rows.length - bad.size} clean, ${bad.size} held with ${findings.length} exception(s).`, findings, proposed_actions: actions,
      totals: { lines: rows.length, total: sum(rows, (x) => x.amt), clean: sum(rows.filter((r) => !bad.has(r.line)), (x) => x.amt), held: sum(rows.filter((r) => bad.has(r.line)), (x) => x.amt) } };
  },
  logic: ['File-driven: one CSV of expense lines (a `receipt` yes/no column is read if present).', 'Per line: category limit, receipt over `receipt_required_over`, weekend date.', 'Across the batch: same employee + merchant + amount within `duplicate_window_days`.', 'Clean lines are proposed for reimbursement per employee; a line with any exception is held.'],
  outputNotes: ['`proposed_actions[]`: `approve_reimbursement` per employee (clean lines only, held amount shown).', '`findings[]`: `over_policy_limit`, `missing_receipt`, `weekend_expense`, `duplicate_in_batch`.'],
  sampleInput: { settings: { company: CO }, files: [
    { name: 'expenses-sept.csv', role: 'expenses', company: CO, content: csv([['employee', 'date', 'merchant', 'category', 'amount', 'receipt'],
      ['Priya Shah', '2025-09-09', 'Rail Europe', 'taxi', '42.00', 'yes'], ['Priya Shah', '2025-09-09', 'Harbour Grill', 'meals', '118.40', 'yes'], ['Priya Shah', '2025-09-10', 'Quayside Hotel', 'hotel', '214.00', 'yes'],
      ['Tom Reed', '2025-09-13', 'City Cabs', 'taxi', '38.50', 'no'], ['Tom Reed', '2025-09-16', 'Office Depot', 'other', '64.99', 'yes'], ['Tom Reed', '2025-09-16', 'Office Depot', 'other', '64.99', 'yes']]) }] },
  expect: { status: 'ok', find: ['over_policy_limit', 'missing_receipt', 'weekend_expense', 'duplicate_in_batch'], actions: ['approve_reimbursement'] },
},
// ───────────────────────────────────────────── 14 Vendor statement reconciliation
{
  id: '14', name: 'vendor-statement-reconciliation', title: 'Vendor statement reconciliation',
  description: 'Reconciles a supplier\'s statement to the bills and payments in the books for that vendor: items on the statement but not in the books, items in the books not on the statement, and amount differences on the same reference.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, vendor: '', as_at: '', amount_tolerance: 0.01 },
  settingNotes: { vendor: 'Vendor whose statement this is (as named in the books)', amount_tolerance: 'Differences at or below this are ignored' },
  reads: [{ key: 'ledger', tool: 'search_bills', params: { vendor: '$vendor' } }],
  fileSpec: {
    statement: { required: true, what: 'supplier statement', columns: [['date'], ['reference', 'invoice', 'invoice_no', 'doc'], ['amount', 'debit']] },
    ap_ledger: { required: false, what: 'A/P ledger for the vendor', columns: [['reference', 'bill_no', 'invoice', 'doc_number'], ['amount', 'total']] },
  },
  compute() {
    const asAt = S.as_at || S.run_at.slice(0, 10);
    const st = src(null, 'statement', { date: ['date'], ref: ['reference', 'invoice', 'invoice_no', 'doc'], amt: ['amount', 'debit'], type: ['type'] }).rows.map((r) => ({ date: r.date, ref: r.ref, amt: num(r.amt), type: r.type || null }));
    const bk = src('ledger', 'ap_ledger', { date: ['date', 'TxnDate'], ref: ['reference', 'bill_no', 'invoice', 'doc_number', 'DocNumber'], amt: ['amount', 'total', 'TotalAmt'], vendor: ['vendor', 'vendor_name', 'VendorRef'], type: ['type'] }).rows
      .filter((r) => !S.vendor || !r.vendor || normName(r.vendor) === normName(S.vendor)).map((r) => ({ date: r.date, ref: r.ref, amt: num(r.amt), type: r.type || null }));
    if (!st.length) return { status: 'error', blocked: true, summary: 'No usable supplier statement.' };
    if (!bk.length) return { status: 'error', blocked: true, summary: `No A/P records for ${S.vendor || 'the vendor'} from Mosofin or a file.` };
    const findings = [], seen = new Set();
    for (const s of st) {
      const b = bk.find((x) => !seen.has(x) && normNo(x.ref) && normNo(x.ref) === normNo(s.ref));
      if (!b) { findings.push({ type: 'on_statement_not_in_books', date: s.date, reference: s.ref, amount: s.amt, likely: s.amt < 0 ? 'payment or credit not recorded' : 'bill not entered (or entered under another number)' }); continue; }
      seen.add(b);
      if (Math.abs(b.amt - s.amt) > S.amount_tolerance) findings.push({ type: 'amount_differs', reference: s.ref, statement: s.amt, books: b.amt, difference: r2(s.amt - b.amt) });
    }
    for (const b of bk.filter((x) => !seen.has(x))) findings.push({ type: 'in_books_not_on_statement', date: b.date, reference: b.ref, amount: b.amt, likely: day(b.date) > day(asAt) ? 'after the statement date' : 'vendor has not recorded it, or it is posted to the wrong vendor' });
    const stTot = sum(st, (x) => x.amt), bkTot = sum(bk, (x) => x.amt);
    const explained = r2(sum(findings.filter((f) => f.type === 'on_statement_not_in_books'), (f) => f.amount) - sum(findings.filter((f) => f.type === 'in_books_not_on_statement'), (f) => f.amount) + sum(findings.filter((f) => f.type === 'amount_differs'), (f) => f.difference));
    const actions = findings.filter((f) => f.type !== 'in_books_not_on_statement').map((f) => ({ type: 'vendor_query', vendor: S.vendor, reference: f.reference, question: f.type === 'amount_differs' ? `Statement shows ${f.statement}, our books ${f.books}: please send the invoice or credit note.` : `Please send a copy of ${f.reference} (${f.amount}).` }));
    return { period: asAt, summary: `Statement ${S.currency} ${stTot.toFixed(2)} vs books ${S.currency} ${bkTot.toFixed(2)}: difference ${r2(stTot - bkTot).toFixed(2)}, ${Math.abs(r2(stTot - bkTot - explained)) < 0.01 ? 'fully explained' : 'NOT fully explained'} by ${findings.length} item(s).`,
      findings, proposed_actions: actions, totals: { statement_balance: stTot, book_balance: bkTot, difference: r2(stTot - bkTot), explained, unexplained: r2(stTot - bkTot - explained) } };
  },
  logic: ['The statement is required; the vendor\'s bills come from Mosofin (A/P ledger file as fallback).', 'Statement lines matched to book records by normalised reference.', 'Lists statement-only items, book-only items and same-reference amount differences, then proves those explain the total difference.'],
  outputNotes: ['`proposed_actions[]`: `vendor_query` per item that needs the vendor (missing documents, amount differences).', '`findings[]`: `on_statement_not_in_books`, `in_books_not_on_statement`, `amount_differs`.', '`totals.unexplained` must be 0 for the reconciliation to be complete.'],
  sampleInput: { settings: { company: CO, vendor: 'Kestrel Supply Co', as_at: '2025-09-30' }, files: [
    { name: 'kestrel-statement-sept.csv', role: 'statement', company: CO, content: csv([['date', 'reference', 'amount'], ['2025-09-03', 'INV-4471', '6210.00'], ['2025-09-12', 'INV-4488', '1940.00'], ['2025-09-24', 'INV-4499', '3305.00'], ['2025-09-15', 'PMT 0915', '-6210.00']]) },
    { name: 'ap-ledger-kestrel.csv', role: 'ap_ledger', company: CO, content: csv([['date', 'bill_no', 'amount'], ['2025-09-03', 'INV4471', '6210.00'], ['2025-09-12', 'INV-4488', '1490.00'], ['2025-09-15', 'PMT 0915', '-6210.00'], ['2025-09-29', 'INV-4502', '2680.00']]) }] },
  expect: { status: 'ok', find: ['on_statement_not_in_books', 'amount_differs', 'in_books_not_on_statement'], actions: ['vendor_query'], check: (e) => (e.totals.unexplained === 0 ? null : `unexplained ${e.totals.unexplained}`) },
},
// ───────────────────────────────────────────── 13 GL flux monitor
{
  id: '13', name: 'gl-flux-monitor', title: 'GL flux monitor',
  description: 'Compares each P&L account this period with the prior period and flags movements over both a percentage and an absolute threshold, plus accounts that went to zero or appeared from nothing. Asks the account owner for an explanation.',
  trigger: 'schedule+webhook', schedule: '0 8 3 * *',
  settings: { ...BASE, period_start: '', period_end: '', prior_start: '', prior_end: '', flux_pct: 15, flux_abs: 2500, account_owners: {}, default_owner: 'Controller' },
  settingNotes: { prior_start: 'First day of the comparison period', prior_end: 'Last day of the comparison period', flux_pct: 'Percent change that trips a flag (both thresholds must trip)', flux_abs: 'Absolute change that trips a flag', account_owners: '{ "account": "owner" } for explanation requests', default_owner: 'Owner when an account has none' },
  reads: [{ key: 'current', tool: 'get_profit_and_loss', params: { start_date: '$period_start', end_date: '$period_end' } }, { key: 'prior', tool: 'get_profit_and_loss', params: { start_date: '$prior_start', end_date: '$prior_end' } }],
  fileSpec: {
    current: { required: false, what: 'P&L by account (current period)', columns: [['account'], ['amount', 'total', 'balance']] },
    prior: { required: false, what: 'P&L by account (prior period)', columns: [['account'], ['amount', 'total', 'balance']] },
  },
  compute() {
    const M = { account: ['account', 'name', 'Account'], amt: ['amount', 'total', 'balance', 'Amount'] };
    const cur = src('current', 'current', M), pri = src('prior', 'prior', M);
    if (!cur.have || !pri.have) return { status: 'error', blocked: true, summary: 'Both periods are needed: current and prior P&L by account, from Mosofin or files.' };
    const a = {}, put = (rows, k) => rows.forEach((r) => { if (!r.account) return; (a[r.account] = a[r.account] || { account: r.account, current: 0, prior: 0 })[k] = r2(a[r.account][k] + num(r.amt)); });
    put(cur.rows, 'current'); put(pri.rows, 'prior');
    const findings = [];
    for (const x of Object.values(a)) {
      const d = r2(x.current - x.prior), pct = x.prior ? r2((d / Math.abs(x.prior)) * 100) : null;
      let type = null;
      if (x.prior && !x.current && Math.abs(x.prior) >= S.flux_abs) type = 'went_to_zero';
      else if (!x.prior && x.current && Math.abs(x.current) >= S.flux_abs) type = 'new_activity';
      else if (Math.abs(d) >= S.flux_abs && pct != null && Math.abs(pct) >= S.flux_pct) type = d > 0 ? 'increase' : 'decrease';
      if (type) findings.push({ type, account: x.account, current: x.current, prior: x.prior, change: d, change_pct: pct, owner: S.account_owners[x.account] || S.default_owner });
    }
    findings.sort((p, q) => Math.abs(q.change) - Math.abs(p.change));
    const byOwner = {};
    findings.forEach((f) => (byOwner[f.owner] = byOwner[f.owner] || []).push(f));
    const actions = Object.entries(byOwner).map(([owner, fs]) => ({ type: 'explanation_request', owner, period: `${S.period_start} to ${S.period_end}`, accounts: fs.map((f) => ({ account: f.account, current: f.current, prior: f.prior, change: f.change, change_pct: f.change_pct, flag: f.type })),
      message: `Please explain these movements versus ${S.prior_start} to ${S.prior_end}:\n` + fs.map((f) => `- ${f.account}: ${f.prior} -> ${f.current} (${f.change >= 0 ? '+' : ''}${f.change}${f.change_pct != null ? ', ' + f.change_pct + '%' : ''})`).join('\n') }));
    return { period: `${S.period_start} to ${S.period_end}`, summary: `${findings.length} of ${Object.keys(a).length} account(s) moved more than ${S.flux_pct}% and ${S.currency} ${S.flux_abs}.`, findings, proposed_actions: actions, totals: { accounts: Object.keys(a).length, flagged: findings.length } };
  },
  logic: ['Reads the P&L by account for the period and the comparison period (files as fallback).', 'Flags an account when the change passes BOTH `flux_pct` and `flux_abs`; also `went_to_zero` and `new_activity` above `flux_abs`.', 'Groups flagged accounts by owner into one explanation request each.'],
  outputNotes: ['`findings[]`: `increase`, `decrease`, `went_to_zero`, `new_activity` with both figures and the change.', '`proposed_actions[]`: `explanation_request` per owner, with a ready message.'],
  sampleInput: { settings: { company: CO, period_start: '2025-09-01', period_end: '2025-09-30', prior_start: '2025-08-01', prior_end: '2025-08-31', account_owners: { '6150 Software': 'IT lead' } } },
  sampleReads: {
    current: [{ account: '4000 Sales', amount: 412300 }, { account: '5000 Cost of Goods Sold', amount: 247900 }, { account: '6000 Salaries', amount: 61200 }, { account: '6100 Rent', amount: 4400 }, { account: '6150 Software', amount: 0 }, { account: '6200 Marketing', amount: 15800 }, { account: '6170 Repairs and Maintenance', amount: 1350 }],
    prior: [{ account: '4000 Sales', amount: 398750 }, { account: '5000 Cost of Goods Sold', amount: 238100 }, { account: '6000 Salaries', amount: 60800 }, { account: '6100 Rent', amount: 4400 }, { account: '6150 Software', amount: 7300 }, { account: '6200 Marketing', amount: 9400 }, { account: '6170 Repairs and Maintenance', amount: 980 }] },
  expect: { status: 'ok', find: ['went_to_zero', 'increase'], actions: ['explanation_request'] },
},
// ───────────────────────────────────────────── 07 Month-end close orchestrator
{
  id: '07', name: 'month-end-close-orchestrator', title: 'Month-end close status',
  description: 'Checks the close from evidence, not from ticks: the trial balance balances, suspense and clearing accounts are empty, and each checklist task has a status. Lists what blocks the close and nudges each owner.',
  trigger: 'schedule+webhook', schedule: '0 8 1-7 * *',
  settings: { ...BASE, period_end: '', tolerance: 0.01, suspense_accounts: ['suspense', 'ask my accountant', 'uncategorized', 'clearing'],
    checklist: [{ task: 'Bank reconciliations', owner: 'AP lead', check: 'status' }, { task: 'Accruals posted', owner: 'GL accountant', check: 'status' }, { task: 'Payroll reconciled', owner: 'Payroll', check: 'status' }, { task: 'Depreciation posted', owner: 'GL accountant', check: 'status' }, { task: 'Trial balance balances', owner: 'Controller', check: 'tb_balances' }, { task: 'Suspense accounts cleared', owner: 'Controller', check: 'suspense_zero' }] },
  settingNotes: { tolerance: 'Rounding tolerance for the trial-balance check', suspense_accounts: 'Account-name fragments treated as suspense/clearing; must be zero', checklist: 'Close tasks: { task, owner, check } where check is `status` (from the task_status file), `tb_balances` or `suspense_zero`' },
  reads: [{ key: 'tb', tool: 'get_trial_balance', params: { end_date: '$period_end' } }],
  fileSpec: {
    trial_balance: { required: false, what: 'trial balance', columns: [['account'], ['debit', 'balance', 'amount']] },
    task_status: { required: false, what: 'close task status list', columns: [['task'], ['status']] },
  },
  compute() {
    const tb = src('tb', 'trial_balance', { account: ['account', 'name', 'Account'], debit: ['debit', 'Debit'], credit: ['credit', 'Credit'], bal: ['balance', 'amount'] }).rows.map((r) => ({ account: r.account, net: r.debit !== undefined || r.credit !== undefined ? r2(num(r.debit) - num(r.credit)) : num(r.bal) }));
    const st = src(null, 'task_status', { task: ['task'], status: ['status'], note: ['note', 'notes'] }).rows;
    const items = [], findings = [];
    for (const c of S.checklist) {
      let status = 'not evidenced', detail = null;
      if (c.check === 'tb_balances') { if (tb.length) { const d = sum(tb, (x) => x.net); status = Math.abs(d) <= S.tolerance ? 'done' : 'blocked'; detail = `debits minus credits = ${d}`; } }
      else if (c.check === 'suspense_zero') { if (tb.length) { const re = new RegExp(S.suspense_accounts.join('|'), 'i'); const open = tb.filter((x) => re.test(x.account) && Math.abs(x.net) > S.tolerance); status = open.length ? 'blocked' : 'done'; detail = open.length ? open.map((x) => `${x.account}: ${x.net}`).join('; ') : 'all zero'; open.forEach((x) => findings.push({ type: 'suspense_not_cleared', account: x.account, balance: x.net, owner: c.owner })); } }
      else { const s = st.find((x) => normName(x.task) === normName(c.task)); if (s) { status = /done|complete|closed|yes/i.test(s.status) ? 'done' : 'open'; detail = s.note || s.status; } }
      items.push({ task: c.task, owner: c.owner, status, detail });
      if (c.check === 'tb_balances' && status === 'blocked') findings.push({ type: 'trial_balance_out_of_balance', difference: sum(tb, (x) => x.net), owner: c.owner });
      if (status !== 'done') findings.push({ type: status === 'not evidenced' ? 'task_not_evidenced' : status === 'open' ? 'task_open' : 'task_blocked', task: c.task, owner: c.owner, detail });
    }
    const byOwner = {};
    items.filter((i) => i.status !== 'done').forEach((i) => (byOwner[i.owner] = byOwner[i.owner] || []).push(i));
    const done = items.filter((i) => i.status === 'done').length;
    return { period: S.period_end, summary: `Close for ${S.period_end}: ${done} of ${items.length} task(s) done; ${items.length - done} outstanding across ${Object.keys(byOwner).length} owner(s).`, findings,
      proposed_actions: Object.entries(byOwner).map(([owner, its]) => ({ type: 'owner_nudge', owner, tasks: its.map((i) => ({ task: i.task, status: i.status, detail: i.detail })), message: `Close ${S.period_end} still needs from you: ` + its.map((i) => `${i.task} (${i.status})`).join(', ') })),
      totals: { tasks: items.length, done, outstanding: items.length - done, checklist: items }, not_done: tb.length ? [] : ['No trial balance from Mosofin or a file: the balance and suspense checks were not run.'] };
  },
  logic: ['`checklist` is fully configurable: each task has an owner and a check type.', '`tb_balances`: trial balance debits = credits within `tolerance`.', '`suspense_zero`: every account whose name contains a `suspense_accounts` fragment is zero.', '`status`: read from an uploaded task-status list; a task with no status is "not evidenced", never assumed done.'],
  outputNotes: ['`totals.checklist[]`: every task with status `done` / `open` / `blocked` / `not evidenced`.', '`proposed_actions[]`: `owner_nudge` per owner with their outstanding tasks.', '`findings[]`: `trial_balance_out_of_balance`, `suspense_not_cleared`, `task_open`, `task_blocked`, `task_not_evidenced`.'],
  sampleInput: { settings: { company: CO, period_end: '2025-09-30' }, files: [
    { name: 'close-tracker.csv', role: 'task_status', company: CO, content: csv([['task', 'status', 'note'], ['Bank reconciliations', 'done', 'all 3 accounts'], ['Accruals posted', 'in progress', 'awaiting utilities'], ['Payroll reconciled', 'done', '']]) }] },
  sampleReads: { tb: [{ account: '1000 Operating Cash', debit: 147545, credit: 0 }, { account: '1100 Accounts Receivable', debit: 63525.5, credit: 0 }, { account: '1999 Suspense', debit: 1250, credit: 0 }, { account: '2000 Accounts Payable', debit: 0, credit: 58200 }, { account: '3000 Retained Earnings', debit: 0, credit: 154120.5 }] },
  expect: { status: 'ok', find: ['suspense_not_cleared', 'task_open', 'task_not_evidenced'], actions: ['owner_nudge'] },
},
// ───────────────────────────────────────────── 08 Recurring journal automator
{
  id: '08', name: 'recurring-journal-automator', title: 'Recurring journal check',
  description: 'Checks that each recurring entry (rent, depreciation, subscriptions, amortisation) was posted this period at its usual amount. Missing ones come back as proposed journal entries; amounts that drifted are flagged.',
  trigger: 'schedule+webhook', schedule: '0 8 28 * *',
  settings: { ...BASE, period_start: '', period_end: '', drift_pct: 5,
    recurring_rules: [{ name: 'Office rent', debit_account: '6100 Rent', credit_account: '2000 Accounts Payable', amount: 4400 }, { name: 'Monthly depreciation', debit_account: '6800 Depreciation', credit_account: '1590 Accumulated Depreciation', amount: 3125 }, { name: 'Software subscriptions', debit_account: '6150 Software', credit_account: '2100 Accrued Liabilities', amount: 7300 }] },
  settingNotes: { recurring_rules: 'The recurring entries: { name, debit_account, credit_account, amount }', drift_pct: 'Posted amount differing from the rule by more than this percent is flagged' },
  reads: [{ key: 'gl', tool: 'get_general_ledger', params: { start_date: '$period_start', end_date: '$period_end' } }],
  fileSpec: { gl: { required: false, what: 'general ledger detail', columns: [['account'], ['amount', 'debit']] } },
  compute() {
    const gl = src('gl', 'gl', { account: ['account', 'Account'], amt: ['amount', 'debit', 'Amount'], date: ['date', 'TxnDate'], memo: ['memo', 'description'] }).rows;
    if (!gl.length) return { status: 'error', blocked: true, summary: 'No general ledger for the period from Mosofin or a file.' };
    const findings = [], actions = [];
    let ok = 0;
    for (const r of S.recurring_rules) {
      const posted = sum(gl.filter((g) => normName(g.account) === normName(r.debit_account)), (g) => g.amt);
      if (!posted) {
        findings.push({ type: 'recurring_entry_missing', name: r.name, account: r.debit_account, expected: r.amount });
        actions.push({ type: 'journal_entry', date: S.period_end, memo: `${r.name}: ${S.period_end}`, lines: [{ account: r.debit_account, debit: r.amount, credit: 0 }, { account: r.credit_account, debit: 0, credit: r.amount }] });
      } else if (Math.abs(posted - r.amount) / r.amount * 100 > S.drift_pct) findings.push({ type: 'amount_drift', name: r.name, account: r.debit_account, expected: r.amount, posted, difference: r2(posted - r.amount) });
      else ok++;
    }
    return { period: `${S.period_start} to ${S.period_end}`, summary: `${ok} of ${S.recurring_rules.length} recurring entr${S.recurring_rules.length === 1 ? 'y' : 'ies'} posted as expected; ${actions.length} missing, ${findings.length - actions.length} drifted.`, findings, proposed_actions: actions,
      totals: { rules: S.recurring_rules.length, as_expected: ok, missing: actions.length, missing_amount: sum(actions, (a) => a.lines[0].debit) } };
  },
  logic: ['`recurring_rules` holds every recurring entry; edit it, nothing is hardcoded.', 'For each rule, sums what was posted to its debit account in the period.', 'Nothing posted: proposes the entry. Posted but more than `drift_pct` off: flags the drift.'],
  outputNotes: ['`proposed_actions[]`: `journal_entry` (balanced) for each missing recurring entry.', '`findings[]`: `recurring_entry_missing`, `amount_drift`.'],
  sampleInput: { settings: { company: CO, period_start: '2025-09-01', period_end: '2025-09-30' } },
  sampleReads: { gl: [{ account: '6100 Rent', amount: 4400, date: '2025-09-01' }, { account: '6800 Depreciation', amount: 3480, date: '2025-09-30' }, { account: '6000 Salaries', amount: 61200, date: '2025-09-30' }] },
  expect: { status: 'ok', find: ['recurring_entry_missing', 'amount_drift'], actions: ['journal_entry'] },
},
// ───────────────────────────────────────────── 10 PBC chase-up
{
  id: '10', name: 'pbc-chase-up', title: 'Audit PBC chase-up',
  description: 'Tracks a prepared-by-client (PBC) request list: what is received, overdue or due soon. Drafts one reminder per owner listing only their open items.',
  trigger: 'schedule+webhook', schedule: '0 9 * * 1-5',
  settings: { ...BASE, as_at: '', due_soon_days: 3, engagement: 'year-end audit', sender_name: 'Finance',
    subject_template: '{{engagement}}: {{count}} open request(s) for you', body_template: 'Hi {{owner}},\n\nFor the {{engagement}}, these requests are still open:\n\n{{lines}}\n\nPlease upload them or let me know what is holding them up.\n\nThanks,\n{{sender}}' },
  settingNotes: { due_soon_days: 'Items due within this many days are included as due soon', engagement: 'Engagement name used in drafts', subject_template: 'Reminder subject', body_template: 'Reminder body; {{lines}} lists the items', sender_name: 'Signature' },
  reads: [],
  fileSpec: {
    pbc_list: { required: true, what: 'PBC request list', columns: [['item', 'request', 'description'], ['owner'], ['due', 'due_date']] },
    received: { required: false, what: 'list of documents received', columns: [['item', 'request']] },
  },
  compute() {
    const asAt = S.as_at || S.run_at.slice(0, 10);
    const list = src(null, 'pbc_list', { id: ['id', 'ref', 'no'], item: ['item', 'request', 'description'], owner: ['owner'], due: ['due', 'due_date'], status: ['status'] }).rows;
    const got = src(null, 'received', { item: ['item', 'request'] }).rows.map((r) => normName(r.item));
    if (!list.length) return { status: 'error', blocked: true, summary: 'No readable PBC list.' };
    const findings = [], byOwner = {};
    let received = 0;
    for (const r of list) {
      if (/received|done|complete|closed/i.test(r.status || '') || got.includes(normName(r.item))) { received++; continue; }
      const d = daysBetween(asAt, r.due), state = d == null ? 'no_due_date' : d < 0 ? 'overdue' : d <= S.due_soon_days ? 'due_soon' : null;
      if (!state) continue;
      const f = { type: state, ref: r.id || null, item: r.item, owner: r.owner, due: r.due, days_overdue: d != null && d < 0 ? -d : 0 };
      findings.push(f); (byOwner[r.owner] = byOwner[r.owner] || []).push(f);
    }
    const actions = Object.entries(byOwner).map(([owner, fs]) => { const lines = fs.map((f) => `- ${f.ref ? f.ref + ' ' : ''}${f.item} (due ${f.due}${f.days_overdue ? ', ' + f.days_overdue + ' days overdue' : ''})`).join('\n');
      const v = { owner, engagement: S.engagement, count: fs.length, lines, sender: S.sender_name };
      return { type: 'email_draft', channel: 'email', owner, items: fs.map((f) => f.item), subject: fill(S.subject_template, v), body: fill(S.body_template, v) }; });
    return { period: asAt, summary: `${received} of ${list.length} request(s) received; ${findings.filter((f) => f.type === 'overdue').length} overdue, ${findings.filter((f) => f.type === 'due_soon').length} due within ${S.due_soon_days} day(s).`, findings, proposed_actions: actions,
      totals: { requests: list.length, received, open: list.length - received, overdue: findings.filter((f) => f.type === 'overdue').length } };
  },
  logic: ['File-driven: the PBC list (with optional `status`) plus an optional received-documents list.', 'An item is received if its status says so or it appears on the received list.', 'Open items are overdue, due within `due_soon_days`, or missing a due date; later items are left alone.', 'One reminder per owner with only their items.'],
  outputNotes: ['`proposed_actions[]`: `email_draft` per owner.', '`findings[]`: `overdue`, `due_soon`, `no_due_date`.'],
  sampleInput: { settings: { company: CO, as_at: '2025-10-01', engagement: 'FY2025 audit' }, files: [
    { name: 'pbc-list.csv', role: 'pbc_list', company: CO, content: csv([['id', 'item', 'owner', 'due_date', 'status'], ['PBC-01', 'Bank confirmations', 'Treasury', '2025-09-25', 'received'], ['PBC-02', 'Fixed asset additions support', 'GL accountant', '2025-09-26', 'open'], ['PBC-03', 'Inventory count sheets', 'Operations', '2025-10-03', 'open'], ['PBC-04', 'Payroll reconciliation Q3', 'Payroll', '2025-10-20', 'open'], ['PBC-05', 'Legal letters', 'GL accountant', '2025-09-29', 'open']]) },
    { name: 'received-docs.csv', role: 'received', company: CO, content: csv([['item', 'received_on'], ['Legal letters', '2025-09-30']]) }] },
  expect: { status: 'ok', find: ['overdue', 'due_soon'], actions: ['email_draft'] },
},
// ───────────────────────────────────────────── 11 Vendor onboarding
{
  id: '11', name: 'vendor-onboarding', title: 'Vendor onboarding check',
  description: 'Checks new-vendor details before setup: required fields present, TIN in a valid format, and no existing vendor with the same name or TIN. Clean vendors are proposed for creation; the rest get a request for the missing information.',
  trigger: 'webhook', blockOnMissing: true,
  settings: { ...BASE, required_fields: ['legal_name', 'tin', 'address', 'email', 'payment_terms', 'tax_classification'], tin_digits: 9 },
  settingNotes: { required_fields: 'Columns that must be filled for a vendor to be set up', tin_digits: 'Digits a TIN must have (US EIN/SSN: 9)' },
  reads: [{ key: 'vendors', tool: 'search_vendors', params: {} }],
  optionalReads: ['vendors'],
  fileSpec: {
    new_vendors: { required: true, what: 'new vendor form / W-9 data', columns: [['legal_name', 'name'], ['tin', 'ein', 'tax_id']] },
    vendors: { required: false, what: 'existing vendor list', columns: [['name', 'vendor', 'display_name']] },
  },
  compute() {
    const nv = src(null, 'new_vendors', null).rows;
    const ex = src('vendors', 'vendors', { name: ['name', 'vendor', 'display_name', 'DisplayName'], tin: ['tin', 'TaxIdentifier', 'ein'] });
    if (!nv.length) return { status: 'error', blocked: true, summary: 'No readable vendor form.' };
    const findings = [], actions = [], not_done = ex.have ? [] : ['Existing vendor list unavailable: the duplicate check was not run.'];
    const val = (r, k) => { const key = Object.keys(r).find((x) => x.toLowerCase() === k.toLowerCase()); return key ? String(r[key]).trim() : ''; };
    for (const r of nv) {
      const name = val(r, 'legal_name') || val(r, 'name'), tin = (val(r, 'tin') || val(r, 'ein') || val(r, 'tax_id')).replace(/[^0-9]/g, ''), issues = [];
      const missing = S.required_fields.filter((f) => !val(r, f));
      if (missing.length) issues.push({ type: 'missing_fields', fields: missing });
      if (tin && (tin.length !== S.tin_digits || /^(\d)\1+$/.test(tin))) issues.push({ type: 'tin_invalid_format', tin_digits_found: tin.length, detail: /^(\d)\1+$/.test(tin) ? 'all one digit' : `expected ${S.tin_digits} digits` });
      if (ex.have) { const dup = ex.rows.find((x) => (normName(x.name) && normName(x.name) === normName(name)) || (tin && String(x.tin || '').replace(/[^0-9]/g, '') === tin));
        if (dup) issues.push({ type: 'possible_duplicate_vendor', existing: dup.name, matched_on: normName(dup.name) === normName(name) ? 'name' : 'tin' }); }
      issues.forEach((i) => findings.push({ vendor: name, ...i }));
      if (!issues.length) actions.push({ type: 'create_vendor', name, tin_last4: tin.slice(-4), payment_terms: val(r, 'payment_terms'), email: val(r, 'email') });
      else if (issues.some((i) => i.type !== 'possible_duplicate_vendor')) actions.push({ type: 'information_request', vendor: name, to: val(r, 'email') || null, ask: issues.filter((i) => i.type !== 'possible_duplicate_vendor').map((i) => (i.type === 'missing_fields' ? `missing: ${i.fields.join(', ')}` : `TIN ${i.detail}: please send a corrected W-9`)) });
    }
    return { summary: `${nv.length} vendor(s) checked: ${actions.filter((a) => a.type === 'create_vendor').length} ready to set up, ${nv.length - actions.filter((a) => a.type === 'create_vendor').length} need attention.`, findings, proposed_actions: actions, not_done, totals: { vendors: nv.length, ready: actions.filter((a) => a.type === 'create_vendor').length } };
  },
  logic: ['One row per new vendor; columns named as in `required_fields`.', 'Checks completeness, TIN format (digit count, not all one digit), and duplicates against existing vendors by name or TIN.', 'Only the last four TIN digits appear in the output.'],
  outputNotes: ['`proposed_actions[]`: `create_vendor` when clean; `information_request` when fields are missing or the TIN is malformed.', '`findings[]`: `missing_fields`, `tin_invalid_format`, `possible_duplicate_vendor`.'],
  sampleInput: { settings: { company: CO }, files: [
    { name: 'new-vendor-forms.csv', role: 'new_vendors', company: CO, content: csv([['legal_name', 'tin', 'address', 'email', 'payment_terms', 'tax_classification'], ['Marlow Logistics LLC', '84-1234567', '12 Dock Rd, Newark NJ', 'ar@marlow.example', 'Net 30', 'LLC-C'], ['Fenwick Print', '12-345678', '4 Mill St, Albany NY', '', 'Net 15', 'Sole proprietor'], ['Kestrel Supply Company Inc', '61-7654321', '9 Quarry Ln, Erie PA', 'billing@kestrel.example', 'Net 30', 'C corporation']]) }] },
  sampleReads: { vendors: [{ DisplayName: 'Kestrel Supply Co', TaxIdentifier: '61-7654321' }, { DisplayName: 'Ashby Metals' }] },
  expect: { status: 'ok', find: ['missing_fields', 'tin_invalid_format', 'possible_duplicate_vendor'], actions: ['create_vendor', 'information_request'] },
},
// ───────────────────────────────────────────── 12 Scheduled financial pack
{
  id: '12', name: 'scheduled-financial-pack', title: 'Scheduled financial pack',
  description: 'Each month, assembles the P&L and balance sheet with prior-period comparatives and highlights, as structured data for a downstream renderer, dashboard or email step. Checks the balance sheet balances before anything goes out.',
  trigger: 'schedule+webhook', schedule: '0 9 5 * *',
  settings: { ...BASE, period_start: '', period_end: '', prior_start: '', prior_end: '', highlight_pct: 10, highlight_abs: 5000, recipients: [] },
  settingNotes: { prior_start: 'Comparison period start', prior_end: 'Comparison period end', highlight_pct: 'Line movements over this percent AND highlight_abs are highlighted', highlight_abs: 'Absolute movement threshold for highlights', recipients: 'Who the downstream step should send the pack to (passed through, never sent from here)' },
  reads: [{ key: 'pl', tool: 'get_profit_and_loss', params: { start_date: '$period_start', end_date: '$period_end' } }, { key: 'pl_prior', tool: 'get_profit_and_loss', params: { start_date: '$prior_start', end_date: '$prior_end' } }, { key: 'bs', tool: 'get_balance_sheet', params: { as_of_date: '$period_end' } }],
  optionalReads: ['pl_prior'],
  fileSpec: {
    pl: { required: false, what: 'P&L by account', columns: [['account'], ['amount', 'total']] },
    pl_prior: { required: false, what: 'prior-period P&L by account', columns: [['account'], ['amount', 'total']] },
    bs: { required: false, what: 'balance sheet by account', columns: [['account'], ['amount', 'balance', 'total']] },
  },
  compute() {
    const M = { account: ['account', 'name', 'Account'], amt: ['amount', 'total', 'balance', 'Amount'], type: ['type', 'account_type', 'section', 'AccountType'] };
    const pl = src('pl', 'pl', M).rows, pp = src('pl_prior', 'pl_prior', M).rows, bs = src('bs', 'bs', M).rows;
    if (!pl.length) return { status: 'error', blocked: true, summary: 'No P&L for the period from Mosofin or a file.' };
    const cls = (r) => { const t = String(r.type || '').toLowerCase(), n = String(r.account || '').trim()[0];
      if (/income|revenue|sales/.test(t) && !/other expense/.test(t)) return 'revenue'; if (/cost of/.test(t)) return 'cogs'; if (/expense/.test(t)) return 'expense';
      if (/asset/.test(t)) return 'asset'; if (/liabilit/.test(t)) return 'liability'; if (/equity/.test(t)) return 'equity';
      return { 1: 'asset', 2: 'liability', 3: 'equity', 4: 'revenue', 5: 'cogs' }[n] || 'expense'; };
    const prior = {}; pp.forEach((r) => (prior[r.account] = r2((prior[r.account] || 0) + num(r.amt))));
    const lines = pl.map((r) => { const c = num(r.amt), p = pp.length ? prior[r.account] || 0 : null, d = p == null ? null : r2(c - p);
      return { account: r.account, class: cls(r), current: c, prior: p, change: d, change_pct: p ? r2((d / Math.abs(p)) * 100) : null }; });
    const tot = (k, rows, f) => sum(rows.filter((x) => cls(x) === k), f);
    const rev = tot('revenue', pl, (x) => x.amt), cogs = tot('cogs', pl, (x) => x.amt), exp = tot('expense', pl, (x) => x.amt);
    const t = { revenue: rev, cogs, gross_profit: r2(rev - cogs), gross_margin_pct: rev ? r2(((rev - cogs) / rev) * 100) : null, expenses: exp, net_income: r2(rev - cogs - exp) };
    if (pp.length) { const pr = tot('revenue', pp, (x) => x.amt), pc = tot('cogs', pp, (x) => x.amt), pe = tot('expense', pp, (x) => x.amt); t.prior_net_income = r2(pr - pc - pe); t.prior_revenue = pr; }
    const findings = lines.filter((l) => l.change != null && Math.abs(l.change) >= S.highlight_abs && (l.change_pct == null || Math.abs(l.change_pct) >= S.highlight_pct)).map((l) => ({ type: 'highlight', account: l.account, current: l.current, prior: l.prior, change: l.change, change_pct: l.change_pct }));
    let bsTables = null; const not_done = [];
    if (bs.length) { const A = tot('asset', bs, (x) => x.amt), L = tot('liability', bs, (x) => x.amt), E = tot('equity', bs, (x) => x.amt);
      bsTables = { assets: A, liabilities: L, equity: E, lines: bs.map((r) => ({ account: r.account, class: cls(r), amount: num(r.amt) })) };
      t.balance_sheet_difference = r2(A - L - E);
      if (Math.abs(t.balance_sheet_difference) >= 0.01) findings.push({ type: 'balance_sheet_does_not_balance', assets: A, liabilities: L, equity: E, difference: t.balance_sheet_difference }); }
    else not_done.push('No balance sheet: the pack has the P&L only.');
    if (!pp.length) not_done.push('No prior period: comparatives and highlights were skipped.');
    const blocked = findings.some((f) => f.type === 'balance_sheet_does_not_balance');
    return { period: `${S.period_start} to ${S.period_end}`, summary: `Pack for ${S.period_start} to ${S.period_end}: revenue ${S.currency} ${rev}, net income ${S.currency} ${t.net_income}; ${findings.filter((f) => f.type === 'highlight').length} highlight(s).${blocked ? ' Balance sheet does not balance: hold the pack.' : ''}`,
      findings, totals: t, not_done,
      proposed_actions: blocked ? [] : [{ type: 'deliver_report', report: 'monthly financial pack', recipients: S.recipients, payload: { profit_and_loss: { lines, totals: t }, balance_sheet: bsTables, highlights: findings.filter((f) => f.type === 'highlight') } }] };
  },
  logic: ['Reads the P&L for the period and the comparison period, and the balance sheet at period end (files as fallback).', 'Classifies accounts by type (or by account-number range when no type is given) and totals revenue, COGS, gross profit and margin, expenses, net income.', 'Highlights lines whose movement passes both `highlight_pct` and `highlight_abs`.', 'If the balance sheet does not balance, no delivery is proposed.'],
  outputNotes: ['`proposed_actions[]`: one `deliver_report` whose `payload` has the P&L lines with comparatives, totals, balance sheet and highlights, plus the configured `recipients`.', '`findings[]`: `highlight`, `balance_sheet_does_not_balance`.'],
  sampleInput: { settings: { company: CO, period_start: '2025-09-01', period_end: '2025-09-30', prior_start: '2025-08-01', prior_end: '2025-08-31', recipients: ['board pack distribution list'] } },
  sampleReads: {
    pl: [{ account: '4000 Sales', amount: 412300, type: 'Income' }, { account: '5000 Cost of Goods Sold', amount: 247900, type: 'Cost of Goods Sold' }, { account: '6000 Salaries', amount: 61200, type: 'Expense' }, { account: '6100 Rent', amount: 4400, type: 'Expense' }, { account: '6200 Marketing', amount: 15800, type: 'Expense' }],
    pl_prior: [{ account: '4000 Sales', amount: 398750, type: 'Income' }, { account: '5000 Cost of Goods Sold', amount: 238100, type: 'Cost of Goods Sold' }, { account: '6000 Salaries', amount: 60800, type: 'Expense' }, { account: '6100 Rent', amount: 4400, type: 'Expense' }, { account: '6200 Marketing', amount: 9400, type: 'Expense' }],
    bs: [{ account: '1000 Operating Cash', amount: 147545, type: 'Asset' }, { account: '1100 Accounts Receivable', amount: 63525.5, type: 'Asset' }, { account: '2000 Accounts Payable', amount: 58200, type: 'Liability' }, { account: '3000 Equity', amount: 152870.5, type: 'Equity' }] },
  expect: { status: 'ok', find: ['highlight'], actions: ['deliver_report'] },
},
// ───────────────────────────────────────────── 15 Fixed asset rollforward
{
  id: '15', name: 'fixed-asset-rollforward', title: 'Fixed asset rollforward',
  description: 'Rolls the fixed asset register forward for the period (opening cost, additions, disposals, closing) and checks straight-line depreciation posted per asset against what the register says it should be. Missing depreciation comes back as a proposed entry.',
  trigger: 'schedule+webhook', schedule: '0 8 28 * *', blockOnMissing: true,
  settings: { ...BASE, period_start: '', period_end: '', depreciation_account: '6800 Depreciation', accumulated_account: '1590 Accumulated Depreciation', materiality: 1 },
  settingNotes: { depreciation_account: 'Expense account depreciation is posted to (read from the GL)', accumulated_account: 'Credit side of proposed depreciation entries', materiality: 'Differences below this per asset are ignored' },
  reads: [{ key: 'depn', tool: 'get_general_ledger', params: { account: '$depreciation_account', start_date: '$period_start', end_date: '$period_end' } }],
  fileSpec: {
    register: { required: true, what: 'fixed asset register', columns: [['asset_id', 'asset'], ['cost'], ['in_service_date', 'in_service', 'acquired'], ['life_months', 'useful_life_months']] },
    depreciation_gl: { required: false, what: 'depreciation postings', columns: [['amount', 'debit'], ['memo', 'description', 'asset_id']] },
  },
  compute() {
    const reg = src(null, 'register', { id: ['asset_id', 'asset'], desc: ['description', 'name'], cost: ['cost'], salvage: ['salvage', 'residual'], start: ['in_service_date', 'in_service', 'acquired'], life: ['life_months', 'useful_life_months'], disposed: ['disposed_date', 'disposal_date'] }).rows;
    const gl = src('depn', 'depreciation_gl', { amt: ['amount', 'debit', 'Amount'], memo: ['memo', 'description', 'asset_id', 'Memo'] });
    if (!reg.length) return { status: 'error', blocked: true, summary: 'No readable fixed asset register.' };
    const ps = day(S.period_start), pe = day(S.period_end);
    const mIdx = (d) => d.getUTCFullYear() * 12 + d.getUTCMonth();
    const roll = { opening_cost: 0, additions: 0, disposals: 0, closing_cost: 0 }, findings = [], actions = [], not_done = [];
    let expectedTotal = 0, postedTotal = 0;
    for (const a of reg) {
      const st = day(a.start), dis = a.disposed ? day(a.disposed) : null, cost = num(a.cost), life = num(a.life);
      if (st < ps && (!dis || dis >= ps)) roll.opening_cost += cost;
      if (st >= ps && st <= pe) roll.additions += cost;
      if (dis && dis >= ps && dis <= pe) roll.disposals += cost;
      const monthly = life ? (cost - num(a.salvage)) / life : 0;
      let exp = 0;
      for (let m = mIdx(ps); m <= mIdx(pe); m++) { const age = m - mIdx(st); if (age >= 0 && age < life && (!dis || m < mIdx(dis))) exp += monthly; }
      exp = r2(exp); expectedTotal += exp;
      if (!gl.have) continue;
      const posted = sum(gl.rows.filter((g) => String(g.memo || '').toUpperCase().includes(String(a.id).toUpperCase())), (g) => g.amt); postedTotal += posted;
      if (exp && !posted) { findings.push({ type: 'depreciation_not_posted', asset: a.id, description: a.desc || null, expected: exp });
        actions.push({ type: 'journal_entry', date: S.period_end, memo: `Depreciation ${a.id} ${S.period_start} to ${S.period_end}`, lines: [{ account: S.depreciation_account, debit: exp, credit: 0 }, { account: S.accumulated_account, debit: 0, credit: exp }] }); }
      else if (Math.abs(posted - exp) >= S.materiality) findings.push({ type: 'depreciation_variance', asset: a.id, expected: exp, posted, difference: r2(posted - exp) });
    }
    Object.keys(roll).forEach((k) => (roll[k] = r2(roll[k])));
    roll.closing_cost = r2(roll.opening_cost + roll.additions - roll.disposals);
    if (gl.have) { const unattributed = r2(sum(gl.rows, (g) => g.amt) - postedTotal); if (Math.abs(unattributed) >= S.materiality) findings.push({ type: 'unattributed_depreciation', amount: unattributed, note: 'posted to the depreciation account without an asset id in the memo' }); }
    else not_done.push('No depreciation postings from Mosofin or a file: expected depreciation was computed but not compared.');
    return { period: `${S.period_start} to ${S.period_end}`, summary: `Cost rolls ${roll.opening_cost} + ${roll.additions} - ${roll.disposals} = ${roll.closing_cost}; depreciation expected ${r2(expectedTotal)}${gl.have ? `, posted ${r2(sum(gl.rows, (g) => g.amt))}` : ''}; ${findings.length} finding(s).`,
      findings, proposed_actions: actions, not_done, totals: { ...roll, depreciation_expected: r2(expectedTotal), depreciation_posted: gl.have ? sum(gl.rows, (g) => g.amt) : null } };
  },
  logic: ['The register is required (asset id, cost, in-service date, life in months; salvage and disposal date optional).', 'Cost rollforward: opening + additions - disposals = closing for the period.', 'Expected depreciation: straight line, full month from the in-service month, stops at end of life or the disposal month.', 'Posted depreciation is attributed to an asset when its memo contains the asset id; differences over `materiality` are flagged.'],
  outputNotes: ['`totals`: the cost rollforward and expected vs posted depreciation.', '`proposed_actions[]`: `journal_entry` for each asset with no depreciation posted.', '`findings[]`: `depreciation_not_posted`, `depreciation_variance`, `unattributed_depreciation`.'],
  sampleInput: { settings: { company: CO, period_start: '2025-09-01', period_end: '2025-09-30' }, files: [
    { name: 'fa-register.csv', role: 'register', company: CO, content: csv([['asset_id', 'description', 'cost', 'salvage', 'in_service_date', 'life_months', 'disposed_date'],
      ['FA-001', 'Warehouse racking', '84000', '0', '2023-01-15', '120', ''], ['FA-002', 'Forklift', '36000', '6000', '2024-03-01', '60', ''], ['FA-003', 'Delivery van', '42000', '4200', '2025-09-10', '72', ''], ['FA-004', 'Old server', '12000', '0', '2021-06-01', '48', '2025-09-20']]) }] },
  sampleReads: { depn: [{ amount: 700, memo: 'Depreciation FA-001 Sep 2025' }, { amount: 500, memo: 'Depreciation FA-002 Sep 2025' }] },
  expect: { status: 'ok', find: ['depreciation_not_posted'], actions: ['journal_entry'], check: (e) => (e.totals.closing_cost === 162000 ? null : `closing cost ${e.totals.closing_cost}, expected 162000`) },
},
// ───────────────────────────────────────────── 16 Inventory obsolescence reserve
{
  id: '16', name: 'inventory-obsolescence-reserve', title: 'Inventory obsolescence reserve',
  description: 'Ages each item by days since its last sale, applies a tiered reserve percentage, and compares the required reserve with the one on the books. Proposes the adjusting entry.',
  trigger: 'schedule+webhook', schedule: '0 8 25 3,6,9,12 *', blockOnMissing: true,
  settings: { ...BASE, as_at: '', aging_tiers: [{ days: 180, reserve_pct: 25 }, { days: 365, reserve_pct: 50 }, { days: 540, reserve_pct: 100 }], never_sold_pct: 100, existing_reserve: 0, reserve_account: '1390 Inventory Reserve', expense_account: '5050 Inventory Obsolescence' },
  settingNotes: { aging_tiers: 'Days since last sale -> reserve percent; the highest tier reached applies', never_sold_pct: 'Reserve percent for items with no sale date', existing_reserve: 'Reserve balance on the books now', reserve_account: 'Contra-inventory account', expense_account: 'P&L account for the adjustment' },
  reads: [],
  fileSpec: { items: { required: true, what: 'inventory listing with last-sale dates', columns: [['sku', 'item'], ['qty', 'on_hand', 'quantity'], ['unit_cost', 'cost'], ['last_sale', 'last_sale_date', 'last_sold']] } },
  compute() {
    const asAt = S.as_at || S.run_at.slice(0, 10);
    const items = src(null, 'items', { sku: ['sku', 'item'], desc: ['description', 'name'], qty: ['qty', 'on_hand', 'quantity'], cost: ['unit_cost', 'cost'], last: ['last_sale', 'last_sale_date', 'last_sold'] }).rows;
    if (!items.length) return { status: 'error', blocked: true, summary: 'No readable inventory listing.' };
    const tiers = [...S.aging_tiers].sort((a, b) => a.days - b.days), findings = [];
    let required = 0, value = 0;
    for (const it of items) {
      const v = r2(num(it.qty) * num(it.cost)); value += v;
      const age = it.last ? daysBetween(it.last, asAt) : null;
      const pct = age == null ? S.never_sold_pct : (tiers.filter((t) => age >= t.days).pop() || { reserve_pct: 0 }).reserve_pct;
      if (!pct) continue;
      const res = r2((v * pct) / 100); required += res;
      findings.push({ type: age == null ? 'never_sold' : 'slow_moving', sku: it.sku, description: it.desc || null, value: v, days_since_sale: age, reserve_pct: pct, reserve: res });
    }
    required = r2(required); const adj = r2(required - num(S.existing_reserve));
    const actions = Math.abs(adj) >= 0.01 ? [{ type: 'journal_entry', date: asAt, memo: `Inventory obsolescence reserve to ${required}`, lines: adj > 0 ? [{ account: S.expense_account, debit: adj, credit: 0 }, { account: S.reserve_account, debit: 0, credit: adj }] : [{ account: S.reserve_account, debit: -adj, credit: 0 }, { account: S.expense_account, debit: 0, credit: -adj }] }] : [];
    return { period: asAt, summary: `${findings.length} of ${items.length} item(s) need a reserve; required ${S.currency} ${required} vs ${S.existing_reserve} booked: adjustment ${adj}.`, findings: findings.sort((a, b) => b.reserve - a.reserve), proposed_actions: actions,
      totals: { items: items.length, inventory_value: r2(value), required_reserve: required, existing_reserve: num(S.existing_reserve), adjustment: adj } };
  },
  logic: ['File-driven: an inventory listing with quantity, unit cost and last-sale date.', 'Days since last sale picks the highest `aging_tiers` tier reached; no sale date uses `never_sold_pct`.', 'Required reserve minus `existing_reserve` is the proposed adjustment (either direction).'],
  outputNotes: ['`findings[]`: `slow_moving` / `never_sold` per item with value, age, percent and reserve, largest first.', '`proposed_actions[]`: one balanced `journal_entry` for the adjustment.'],
  sampleInput: { settings: { company: CO, as_at: '2025-09-30', existing_reserve: 4000 }, files: [
    { name: 'inventory-listing.csv', role: 'items', company: CO, content: csv([['sku', 'description', 'on_hand', 'unit_cost', 'last_sale_date'], ['PW-200', 'Pallet wrap', '850', '9.40', '2025-09-28'], ['CB-110', 'Corner boards', '4000', '0.62', '2025-02-11'], ['SS-310', 'Steel shelving kit', '14', '298.00', '2024-07-30'], ['LB-001', 'Legacy label printer', '6', '410.00', '2023-11-02'], ['TP-050', 'Tape gun (discontinued)', '120', '7.50', '']]) }] },
  expect: { status: 'ok', find: ['slow_moving', 'never_sold'], actions: ['journal_entry'] },
},
// ───────────────────────────────────────────── 17 Sales tax nexus monitor
{
  id: '17', name: 'sales-tax-compliance-monitor', title: 'Sales tax nexus monitor',
  description: 'Totals sales and transaction counts by ship-to state over a trailing window and compares them with each state\'s economic-nexus thresholds. Flags states crossed where the company is not registered, and states approaching the line.',
  trigger: 'schedule+webhook', schedule: '0 8 2 * *',
  settings: { ...BASE, window_start: '', as_at: '', warn_pct: 80, registered_states: [],
    thresholds: { default: { amount: 100000, transactions: 200 }, CA: { amount: 500000, transactions: null }, TX: { amount: 500000, transactions: null }, NY: { amount: 500000, transactions: 100 } } },
  settingNotes: { window_start: 'Start of the measurement window (e.g. 12 months back)', warn_pct: 'Flag a state once sales or transactions reach this percent of its threshold', registered_states: 'States where the company already collects and files', thresholds: 'Per-state { amount, transactions } (null = no count test); `default` for states not listed. Confirm against current state rules before relying on them.' },
  reads: [{ key: 'invoices', tool: 'search_invoices', params: { start_date: '$window_start', end_date: '$as_at' } }],
  fileSpec: { sales: { required: false, what: 'sales by invoice with ship-to state', columns: [['state', 'ship_to_state', 'shipping_state'], ['amount', 'total']] } },
  compute() {
    const rows = src('invoices', 'sales', { state: ['state', 'ship_to_state', 'shipping_state', 'ShipAddrState'], amt: ['amount', 'total', 'TotalAmt'] }).rows;
    if (!rows.length) return { status: 'error', blocked: true, summary: 'No sales for the window from Mosofin or a file.' };
    const by = {}, noState = [];
    for (const r of rows) { const s = String(r.state || '').trim().toUpperCase(); if (!s) { noState.push(num(r.amt)); continue; } const x = (by[s] = by[s] || { state: s, sales: 0, transactions: 0 }); x.sales = r2(x.sales + num(r.amt)); x.transactions++; }
    const reg = S.registered_states.map((s) => s.toUpperCase()), findings = [];
    for (const x of Object.values(by)) {
      const t = S.thresholds[x.state] || S.thresholds.default, pa = (x.sales / t.amount) * 100, pt = t.transactions ? (x.transactions / t.transactions) * 100 : 0, pct = r2(Math.max(pa, pt));
      const base = { state: x.state, sales: x.sales, transactions: x.transactions, threshold_amount: t.amount, threshold_transactions: t.transactions, pct_of_threshold: pct, test: pa >= pt ? 'sales' : 'transactions' };
      if (pct >= 100) findings.push({ type: reg.includes(x.state) ? 'nexus_registered' : 'nexus_crossed_not_registered', ...base });
      else if (pct >= S.warn_pct && !reg.includes(x.state)) findings.push({ type: 'approaching_nexus', ...base });
    }
    if (noState.length) findings.push({ type: 'sales_without_state', count: noState.length, amount: sum(noState) });
    const crossed = findings.filter((f) => f.type === 'nexus_crossed_not_registered');
    return { period: `${S.window_start} to ${S.as_at}`, summary: `${Object.keys(by).length} state(s) with sales; ${crossed.length} crossed nexus without registration, ${findings.filter((f) => f.type === 'approaching_nexus').length} approaching.`,
      findings, proposed_actions: crossed.map((f) => ({ type: 'registration_review', state: f.state, reason: `${f.test} at ${f.pct_of_threshold}% of the threshold`, note: 'Confirm the threshold and measurement period with the state before registering.' })),
      totals: { states: Object.keys(by).length, sales: sum(Object.values(by), (x) => x.sales), by_state: Object.values(by).sort((a, b) => b.sales - a.sales) } };
  },
  logic: ['Sales by ship-to state over `window_start`..`as_at` from Mosofin invoices (file fallback).', 'Each state is tested on sales and, where the state has one, transaction count; the higher percentage counts.', 'Crossed and not in `registered_states` → registration review; at or above `warn_pct` → approaching.', 'Thresholds are settings, not law: the README and every action say to confirm them.'],
  outputNotes: ['`findings[]`: `nexus_crossed_not_registered`, `approaching_nexus`, `nexus_registered`, `sales_without_state`.', '`proposed_actions[]`: `registration_review` per crossed state.', '`totals.by_state[]`: sales and counts per state.'],
  sampleInput: { settings: { company: CO, window_start: '2024-10-01', as_at: '2025-09-30', registered_states: ['NY'] } },
  sampleReads: { invoices: [].concat(
    Array.from({ length: 30 }, (_, i) => ({ ShipAddrState: 'NJ', TotalAmt: 3500 + i * 10 })),
    Array.from({ length: 12 }, () => ({ ShipAddrState: 'PA', TotalAmt: 7200 })),
    Array.from({ length: 40 }, () => ({ ShipAddrState: 'NY', TotalAmt: 13000 })),
    [{ ShipAddrState: 'CA', TotalAmt: 22000 }, { ShipAddrState: '', TotalAmt: 950 }]) },
  expect: { status: 'ok', find: ['nexus_crossed_not_registered', 'approaching_nexus'], actions: ['registration_review'] },
},
// ───────────────────────────────────────────── 18 Intercompany netting
{
  id: '18', name: 'intercompany-netting-settlement', title: 'Intercompany reconciliation and netting',
  description: 'Checks that each pair of group entities agrees on what they owe each other, lists the mismatches, and proposes the fewest settlement payments that clear the agreed balances.',
  trigger: 'schedule+webhook', schedule: '0 8 26 * *', blockOnMissing: true,
  settings: { ...BASE, as_at: '', tolerance: 1, entities: [] },
  settingNotes: { tolerance: 'Pair differences at or below this are treated as agreed', entities: 'Limit to these entities; empty = every entity in the file' },
  reads: [],
  fileSpec: { balances: { required: true, what: 'intercompany balances by entity and counterparty', columns: [['entity'], ['counterparty'], ['balance', 'amount']] } },
  compute() {
    let rows = src(null, 'balances', { entity: ['entity'], cp: ['counterparty'], bal: ['balance', 'amount'] }).rows.map((r) => ({ e: String(r.entity).trim(), c: String(r.cp).trim(), b: num(r.bal) }));
    if (S.entities.length) rows = rows.filter((r) => S.entities.includes(r.e) && S.entities.includes(r.c));
    if (!rows.length) return { status: 'error', blocked: true, summary: 'No intercompany balances to check.' };
    const get = (a, b) => sum(rows.filter((r) => r.e === a && r.c === b), (r) => r.b), seen = new Set(), findings = [], net = {};
    for (const r of rows) {
      const key = [r.e, r.c].sort().join('|'); if (seen.has(key)) continue; seen.add(key);
      const ab = get(r.e, r.c), ba = get(r.c, r.e), diff = r2(ab + ba);
      if (Math.abs(diff) > S.tolerance) { findings.push({ type: 'pair_does_not_agree', entity: r.e, counterparty: r.c, entity_says: ab, counterparty_says: ba, difference: diff }); continue; }
      net[r.e] = r2((net[r.e] || 0) + ab); net[r.c] = r2((net[r.c] || 0) - ab);
    }
    const cred = Object.entries(net).filter(([, v]) => v > 0.005).map(([e, v]) => ({ e, v })).sort((a, b) => b.v - a.v);
    const debt = Object.entries(net).filter(([, v]) => v < -0.005).map(([e, v]) => ({ e, v: -v })).sort((a, b) => b.v - a.v);
    const actions = [];
    while (cred.length && debt.length) { const c = cred[0], d = debt[0], amt = r2(Math.min(c.v, d.v));
      actions.push({ type: 'settlement_payment', from: d.e, to: c.e, amount: amt, currency: S.currency }); c.v = r2(c.v - amt); d.v = r2(d.v - amt); if (c.v < 0.005) cred.shift(); if (d.v < 0.005) debt.shift(); }
    const gross = sum(rows.filter((r) => r.b > 0), (r) => r.b);
    return { period: S.as_at || S.run_at.slice(0, 10), summary: `${seen.size} entity pair(s): ${findings.length} do not agree. Agreed balances settle with ${actions.length} payment(s) of ${S.currency} ${sum(actions, (a) => a.amount)} (gross receivables ${gross}).`,
      findings, proposed_actions: actions, totals: { pairs: seen.size, mismatched: findings.length, net_positions: net, settlement_total: sum(actions, (a) => a.amount) },
      not_done: findings.length ? ['Pairs that do not agree were left out of netting until they are reconciled.'] : [] };
  },
  logic: ['File-driven: one row per entity per counterparty; positive = receivable from the counterparty, negative = payable.', 'Each pair must mirror (A says +x, B says -x) within `tolerance`; mismatched pairs are listed and left out of netting.', 'Agreed balances become net positions per entity, settled greedily largest-first: the fewest payments for this set.'],
  outputNotes: ['`findings[]`: `pair_does_not_agree` with both sides and the difference.', '`proposed_actions[]`: `settlement_payment` from, to, amount.', '`totals.net_positions`: each entity\'s net receivable (+) or payable (-).'],
  sampleInput: { settings: { company: 'Northbrook Group', as_at: '2025-09-30' }, files: [
    { name: 'ic-balances-sept.csv', role: 'balances', company: 'Northbrook Group', content: csv([['entity', 'counterparty', 'balance'],
      ['Northbrook Trading Ltd', 'Northbrook UK', '104800'], ['Northbrook UK', 'Northbrook Trading Ltd', '-104800'], ['Northbrook Trading Ltd', 'Northbrook Logistics', '-22500'], ['Northbrook Logistics', 'Northbrook Trading Ltd', '22500'],
      ['Northbrook UK', 'Northbrook Logistics', '18000'], ['Northbrook Logistics', 'Northbrook UK', '-15600']]) }] },
  expect: { status: 'partial', find: ['pair_does_not_agree'], actions: ['settlement_payment'] },
},
];
