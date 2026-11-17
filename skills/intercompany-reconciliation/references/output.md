<!-- intercompany-reconciliation · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Every entity pair reconciled to a difference of zero or a clearly explained variance**
- **Every mismatch has a probable cause and recommended action**
- **Currency conversions documented per side**
- **Settlement proposals net per pair, not gross**
- **Elimination JEs ready for consolidation**
- **File naming consistent**
- **No mismatch silently absorbed**

**Mosofin additions:**

- The workspace(s) were confirmed **by name** and the user said yes before any data was read
- **Every group member is named by `display_name` with its functional currency**; **every group member that
  is not connected is named, and every pair it belongs to is marked not reconcilable**
- **No single-sided balance is presented as a reconciliation**
- The capability map was discovered **this run** via Gate 2, **per entity, and recorded per pair**
- **All entities were read in one batch**, so every side is as at the same instant, and the reads were
  per-entity rather than per-pair
- **The pair matrix appears before the numbers**, showing what could and could not be reconciled
- **Every pair difference is reported with a number, including zero**, and **split into timing, FX and true
  mismatch**
- **Every match records its basis** — reference, or amount and date alone — and the weaker basis is flagged
- **The date window and amount tolerance used are stated**
- **No match was forced**: differing amounts are recorded as a matched pair with a difference, never as a
  match
- **Journal entries posted direct to IC accounts with no document are listed separately**
- **Open IC balances are aged**, and persistent mismatches are identified as process failures
- **Translation precedes comparison** for cross-currency pairs, and **FX differences are carried to CTA
  rather than adjusted away**
- **Elimination uses the agreed amount**, with any difference carried explicitly rather than left as a
  silent residual
- **Settlement is proposed on agreed balances only**, netted per pair
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet, **per pair**
- `mock` status is reported **per entity**, and any pair involving mock data is marked not reconciled
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No balances, mismatch amounts, transaction lists or settlement figures are persisted** into a skill
  bundle; **every persisted rule names both entities of its pair**
- Nothing was written back to any system — no entry, settlement or elimination posted
