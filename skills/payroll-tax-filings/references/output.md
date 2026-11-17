<!-- payroll-tax-filings · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **All filing obligations mapped with frequency, form, and deadline**
- **Deposit / remittance schedule determined per current rules**
- **Amounts computed on correct taxable bases with caps applied, at current rates**
- **Deposits reconciled to liabilities with timeliness flagged**
- **Periodic returns tie to registers and GL**
- **Year-end three-way tie** (wage statements ↔ returns ↔ GL) **achieved before issuance**
- **No hardcoded rates, bases, schedules, forms, or deadlines — all current-sourced**
- **Multi-jurisdiction, classification, and provider-remittance risks flagged**
- **Professional review recommended for filing**
- **File naming consistent**

**Mosofin additions:**

- **Every statutory value used appears on Sheet 8 with its source, jurisdiction and year**, and **nothing
  appears in a computation that is not on that sheet**
- **No rate, ceiling, threshold, frequency, form or deadline was supplied from memory**, as a default or as
  an illustration
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **as employer of record**; every excluded one is
  named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Both sides of the deposit reconciliation were read** — the liability from the GL and the deposits from
  the payment records — and **the balance still due is computed rather than asserted**
- **Timeliness is stated exactly** where due dates were supplied — the payment date against the due date —
  **and reported as unassessable where they were not**
- **The evidence is stated to stop at the company's bank account**, and **proof of actual deposit is marked
  `[manual]`** wherever a provider is involved
- **Over-deposits are flagged as requiring action**, not reported as headroom
- **The computed amount due is compared to the liability balance**, and any difference reported as a
  possible accrual error
- **The liability accounts were compared to the obligation list** in both directions, with an obligation
  lacking an account raised as a possible unaccrued liability
- **The historical payment pattern was compared to the stated deposit schedule**
- **The GL leg of the three-way tie is provided immediately**, and the tie is completed before any wage
  statement is issued
- **Per-employee data appears only on the wage statement sheet**, and nowhere else
- In a multi-entity run, **filings are prepared per employer and never consolidated**, deposit
  reconciliation runs per entity, cross-entity payments are raised as intercompany with the original
  obligation still outstanding, and **registration gaps are flagged per entity**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no statutory filing figure rests on mock data**
- Every ledger figure traces to a tool result in this conversation and every statutory value to Sheet 8; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No rates, ceilings, thresholds, frequencies or deadlines are persisted**, and **no employee's wage or
  withholding data is stored**; every persisted preference states the datasource and `display_name` it
  covers
- Nothing was written back to any system — no filing submitted, no remittance made, no return amended
