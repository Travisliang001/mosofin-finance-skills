<!-- multicurrency-fx-revaluation · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Functional currency determined per entity with rationale**
- **Transaction FX (P&L) and translation (OCI) handled distinctly — not conflated**
- **Monetary vs. non-monetary correctly classified for remeasurement**
- **Current-rate method applied for functional ≠ presentation translation; temporal method for special
  cases**
- **CTA accumulated in OCI; remeasurement gain / loss in P&L per framework**
- **Hedge accounting only applied where designated and documented**
- **Realized vs. unrealized FX distinguished**
- **Goodwill and intercompany FX handled per the rules**
- **Disposal CTA release tracked**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its home currency**; every excluded one is
  named **as excluded**; the presentation currency is stated
- The capability map was discovered **this run** via Gate 2, **per entity** — never recalled from a previous
  conversation or from this file
- **Whether balances are currency-tagged is established and stated**, and where they are not, **revaluation
  is reported as not performable from the ledger** rather than approximated
- **Whether the platform revalues automatically is established**, and **no duplicate entry is proposed**
- **Each entity's home currency was compared to its concluded functional currency**, and any disagreement
  raised before revaluation or translation
- **Realized and unrealized FX are reported separately**, derived from settled versus open balances
- **The computed FX is compared to what was actually posted**, with differences attributed to rate,
  population or classification
- **Every rate carries its source, type and date**, and none was supplied from memory
- **Every account is explicitly classified** monetary or non-monetary, with **deferred revenue and
  prepayments identified as non-monetary**
- **The CTA roll-forward ties to the CTA account**, and **CTA is tracked per operation** so a disposal
  release is identifiable
- **The average-rate basis is stated**, and seasonality was tested before relying on a simple average
- **Hedge accounting is applied only where designation and documentation exist**, and their absence is
  stated
- In a multi-entity run, **every entity is read in one batch**, translation precedes consolidation, every
  figure carries its currency, and **intercompany translation differences are carried rather than forced**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet, **per entity**
- `mock` status is reported **per entity**, and no revaluation or translation rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No exchange rates, balances, FX amounts or CTA figures are persisted** into a skill bundle; every
  persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — no revaluation or translation entry posted
