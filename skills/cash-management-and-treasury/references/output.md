<!-- cash-management-and-treasury · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Complete bank account map with redundancies and trapped cash identified**
- Recommended structure rationalized to operational and risk needs
- Liquidity policy with explicit minimum, buffer, surplus, and reserve levels
- Investment policy with eligible instruments, limits, and approval matrix
- **Payment controls including fraud prevention measures**
- FX policy aligned with exposures and accounting (hedge designation if applied)
- **Counterparty concentration assessed and limited**
- Treasury KPIs defined and monitored
- Policy documented and governance authority matrix specified
- **Pooling / multi-entity structures flagged for tax / legal review**
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**; **entities with no connected file are named as gaps in the map**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **The account map marks each column's source** — balance and currency measured, bank and
  signatories supplied
- **Dormant and redundant accounts were detected from actual movement**, and closure candidates
  ranked by balance
- **Counterparty concentration is reported only once accounts are mapped to banks**, or declared
  outstanding
- **Payment controls are labelled designed, not tested**, and every control Mosofin cannot verify is
  recorded as a gap with a named owner
- Each treasury KPI is marked auto / gated / manual on the dashboard
- Facility limits are never presented as liquidity without confirmed terms
- In a multi-entity run, **group cash is reported alongside the movable subset**, and pooling is
  proposed only where cash can actually move
- `mock` status is reported wherever it applies, and no policy or account-closure decision rests on
  mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence;
  the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No bank account numbers, banking credentials, signatory names with authority levels, or cash
  balances are persisted** into a skill bundle; every persisted preference states the datasource and
  `display_name` it covers
- Nothing was written back to any system — no account was opened or closed, no cash moved, no
  permission changed
