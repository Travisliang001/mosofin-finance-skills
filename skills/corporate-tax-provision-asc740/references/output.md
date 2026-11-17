<!-- corporate-tax-provision-asc740 · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Current and deferred tax computed and summing to the total provision**
- **Permanent vs. temporary differences correctly classified**
- **Deferred tax at the enacted future rate, remeasured for any rate change**
- **Valuation allowance assessed with documented evidence** (or the IFRS recognition threshold applied)
- Uncertain tax positions assessed and reserved per the framework
- **ETR reconciliation arrives exactly at the total provision and effective rate**
- **Deferred tax rollforward ties** (opening + movements = closing)
- **Intraperiod allocation applied** (continuing ops vs. OCI / equity / discontinued)
- **No hardcoded tax rates — all confirmed for the entity's jurisdiction and year**
- Disclosure-ready figures provided
- File naming consistent
- **Specialist flags raised for Pillar Two, outside basis, and other complex areas**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its tax jurisdiction**; every excluded
  one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Every rate carries its source and the year it applies to**, or appears on the open-items sheet.
  **None is supplied from memory**
- **The temporary-difference schedule marks each row's book side as read and its tax side as supplied** —
  no book balance is presented as a temporary difference
- **The valuation-allowance assessment includes the measured cumulative pre-tax result** for the last
  three years, with the periods stated
- **Deferred tax movements posted to OCI or equity are identified from the ledger** and excluded from the
  P&L charge, with the computed allocation reconciled to the actual postings
- Permanent-difference candidates surfaced from the chart of accounts are presented as **prompts, not
  determinations**
- The ETR "Other" line is within a stated threshold, or broken out
- Every input carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used,
  and the periods it drew on, in the coverage sheet
- In a multi-entity run, **the provision is computed per entity and jurisdiction before any group
  aggregation**, and losses are not netted across entities without confirmed grouping rules
- `mock` status is reported wherever it applies, and no published provision rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No tax rates, taxable income, deferred balances, NOL amounts or UTP assessments are persisted** into a
  skill bundle; every persisted preference states the datasource, `display_name` and jurisdiction it
  covers
- Nothing was written back to any system — the provision is a proposal for the tax function to review
