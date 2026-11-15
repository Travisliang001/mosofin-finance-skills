<!-- inventory-costing-fifo-lifo-wavg · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Method eligibility (LIFO not under IFRS) and consistency confirmed**
- **Cost basis includes appropriate components, excludes selling / admin**
- **Cost flow correctly applied per method and system** (periodic vs. perpetual)
- **Layer detail or average computation shown clearly**
- **NRV (or LCM where applicable) applied with correct write-down treatment and framework-appropriate
  reversal handling**
- **Period-end entries match the computation**
- **Method-comparison (if requested) shows P&L and tax impact**
- **Units and cost reconcile; ties to GL**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The method the platform applies and the method the entity reports are both stated**, and **where any
  difference is recorded is identified** — or reported as unrecorded
- **Periodic versus perpetual was established from the data**, not assumed
- **Layer detail states whether it was read or reconstructed**, and from which transaction population;
  where line-level detail was unavailable, **reconstruction is reported as not possible**
- **The validation is run and reported in units and in cost separately**
- **Computed ending inventory is compared to the ledger balance**, and any difference identified as reserve,
  adjustment, or unexplained
- **NRV is anchored in this entity's realised selling prices**, with the window and dates stated, and
  **costs to complete and sell are `[manual]` with their source**
- **Replacement cost approximated from recent purchases is labelled as an approximation**
- **Freight-in treatment is checked** in both directions, as is selling or admin cost in inventory
- **The observed price direction is stated** in any method comparison, rather than reciting the
  rising-price rule
- **Items with no sales activity are identified** and routed to `inventory-obsolescence-and-reserve`
- In a multi-entity run, **group cost is the originating entity's cost**, intercompany mark-up in stock is
  identified for elimination, method differences across entities are flagged, and **NRV is not carried
  across entities**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no inventory or COGS figure rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No quantities, unit costs, layer stacks, inventory values or NRV figures are persisted** into a skill
  bundle, and **no item-level cost or supplier pricing is stored**; every persisted preference states the
  datasource and `display_name` it covers
- Nothing was written back to any system — no costing adjustment, write-down or COGS entry posted
