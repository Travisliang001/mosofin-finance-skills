<!-- income-tax-deferred-tax-rollforward · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original's four Quality checks, kept as stated, plus the rest of its workflow requirements and the
Mosofin additions.**

**The original's Quality checks:**

- **Rates used are enacted as of the reporting date**
- **Temporary differences mapped to the correct jurisdiction**
- **Reversal patterns are plausible and consistent with forecasts**
- **DTAs do not double-count items captured elsewhere**

**From the original workflow and outputs:**

- **A temporary difference inventory is built**, capturing book basis, tax basis, the difference, the
  reversal pattern, and jurisdiction and rate for each item
- **DTAs and DTLs are calculated** as difference × enacted rate, classified correctly as deductible or
  taxable
- **A rollforward is produced by category**, covering beginning balance, current period expense or benefit,
  FX or rate changes, acquisitions and disposals, utilization and reversal, to the ending balance
- **The valuation allowance is assessed** against positive and negative evidence — cumulative recent losses,
  forecast taxable income, reversal of existing DTLs, and tax planning strategies — **with the conclusion
  documented and quantified**
- **The result ties to the total tax provision and the rate reconciliation**
- **Disclosures are prepared**: components of deferred taxes, valuation allowance roll-forward, expiration
  of NOLs and credits, rate reconciliation support
- The deliverables include the **inventory and rollforward schedules, the valuation allowance memo, the
  tie-out to provision and effective tax rate, the JE package, and the disclosure tables**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its taxpayer and jurisdiction**; every
  excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Every book basis is `[auto]` with the account named**; **every tax basis is `[manual]` with its source
  named**; neither side was inferred from the other
- **Every rate carries its jurisdiction and enactment date**, and none was supplied from memory
- **The inventory mapping was checked in all three directions** — double counts, items with no account, and
  **material accounts with no item**
- **The rollforward ties to the balance sheet at both ends and to the P&L deferred expense**, each
  difference quantified including zero
- **Rate changes appear on their own rollforward line**
- **The cumulative-loss computation is shown, with years and amounts**, whichever way the conclusion goes
- **DTL support for DTAs is tested for matching timing and jurisdiction**
- **NOL and credit expirations are reported by year**, not only as amounts
- Deferred movements relating to OCI or equity items **follow the item**, not the P&L
- In a multi-entity run, **the valuation allowance and the cumulative-loss test run per taxpayer**, rates
  are keyed by jurisdiction, **no offset is presented without a right of offset**, and consolidation-level
  differences are computed at group level
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no deferred balance or provision figure rests on mock
  data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No tax rates, tax bases, deferred balances, NOL amounts or valuation allowance figures are persisted**
  into a skill bundle; every persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no deferred entry, allowance or true-up posted
