<!-- cash-flow-statement-indirect-method · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Statement ties exactly to the change in cash (Step 6 proven)**
- Working-capital changes exclude non-cash movements (acquisitions, FX, reclasses)
- Gains / losses on disposals reversed out of operating
- **Capex separated from disposals and depreciation**
- Interest / dividend classification consistent with framework and policy
- FX effect isolated on its own line
- Supplemental disclosures (interest paid, taxes paid, non-cash items) present
- Comparative period included
- File naming consistent
- **No plug figure to force the tie-out — every line is sourced**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- **The accounts counted as cash are named on the face of the statement**, with restricted cash
  identified
- **Investing and financing are built from ledger movements, not from net balance changes**; gross
  draws and repayments are shown separately
- **The rebuild is compared against the platform's own cash flow report**, and every material
  difference is explained rather than adopted
- **Transfers between the entity's own accounts are identified and excluded** from cash flows
- Every material non-cash adjustment names the journal or event behind it
- The FX line is shown as nil rather than omitted where the entity holds no foreign currency
- Every line carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet
- `mock` status is reported wherever it applies, and **no published statement rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence;
  the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- No statements, balances or figures are persisted into a skill bundle; every persisted preference
  states the datasource and `display_name` it covers
- Nothing was written back to any system — the statement is a deliverable for a human to review and
  publish
