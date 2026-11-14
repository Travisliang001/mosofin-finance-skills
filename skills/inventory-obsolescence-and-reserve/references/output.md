<!-- inventory-obsolescence-and-reserve · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original's four Quality checks, kept as stated, plus the rest of its workflow requirements and the
Mosofin additions.**

**The original's Quality checks:**

- **Tie inventory listing to GL**
- **Ensure consistent cost basis**
- **Separate damaged / expired from slow-moving**
- **Review large write-downs with operations and sales**

**From the original workflow and outputs:**

- **A reserve policy is defined**: aging buckets, reserve percentages by bucket based on history, and
  special handling for seasonal, end-of-life and customer-specific items
- **Slow-moving and excess are identified per SKU**: days on hand, months of supply, comparison to forecast
  demand, and no-move flags
- **The LCNRV / NRV test is performed**, including the finished-goods consideration for raw materials
- **The reserve is quantified** by an appropriate method — aging-based, specific identification, or
  forecast-based excess
- **The entries are booked and tracked**, distinguishing the reserve entry from the write-off entry
- **A roll-forward is provided**: beginning reserve, additions, write-offs and usage, ending reserve
- The deliverables include the **reserve calculation tables, the SKU exception list with rationale, the
  recommended journal entries, and the roll-forward with a disclosure-ready summary**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The aging basis is stated** — lot-tracked dates or last-purchase proxy — and never presented as the
  other
- **Reserve rates are derived from this entity's own history** and presented alongside the rates in use,
  with the derivation window stated
- **The existing reserve is back-tested** against actual write-offs and below-cost sales over prior periods
- **The no-move list is filtered through the special-handling categories** before presentation, and **no-move
  is never reported as obsolete**
- **Every exception carries its carrying value**, not just its quantity, plus last sale date and units sold
- **The usage window for days-on-hand and months-of-supply is stated**
- **Where no forecast exists, the comparison is labelled as historical demand**, not forecast
- **Items already selling below cost are identified from realised prices**, with counts and average
  shortfall
- **LCNRV and the obsolescence reserve do not overlap**, and one method is applied per population
- **The roll-forward ties to the reserve account**, with the difference reported including zero
- **Write-offs posted to expense while a reserve exists are flagged**
- **Physical condition is recorded as `[manual]` and not assessed here**, with a named owner
- In a multi-entity run, **months of supply is measured against group demand**, demand elsewhere in the group
  is checked before reserving, **reserves are computed on group cost**, and transfer-reset aging is checked
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no reserve rests on mock movement data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No SKU quantities, carrying values, reserve amounts, item costs or exception lists are persisted** into
  a skill bundle; every persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no reserve, write-down or write-off posted
