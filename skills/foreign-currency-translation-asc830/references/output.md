<!-- foreign-currency-translation-asc830 · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original has no Output Quality Standards section. Everything below is a Mosofin addition**, drawn
from the original's own workflow and controls and from the workspace model.

**From the original workflow and controls:**

- **A functional currency conclusion is documented per entity**, against the four assessment factors
- **Monetary items are remeasured at the period-end spot rate**; nonmonetary items at historical rates
- **Remeasurement gains and losses are recognized in earnings**, not OCI
- **Assets and liabilities are translated at the closing rate, income at average, equity at historical**
- **CTA is recorded in OCI**
- **Intercompany balances agree after translation**, with settlement vs. net-investment classification
  considered
- **The rate source is stated and approved**
- **Entities and accounts are complete**
- **Classification is consistent** between monetary and nonmonetary
- **The translated TB ties to the consolidation**
- The deliverables include the **functional currency memo, translation worksheets and rate tables, the
  remeasurement schedule, the CTA roll-forward, and the JE package with disclosure notes**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its home currency**; every excluded one is
  named **as excluded**, and the group reporting currency is stated
- The capability map was discovered **this run** via Gate 2, **per entity** — never recalled from a previous
  conversation or from this file
- **Each file's home currency was compared to its concluded functional currency**, and any disagreement was
  raised before translation proceeded
- **CTA was proved independently** against the net-asset and rate movements, and the difference from the
  plug is reported and explained — **never absorbed**
- **The balance of the translated balance sheet is not presented as evidence of correctness**
- **Every rate carries its source, type, date and approver**, and none was supplied from memory
- **Every account is explicitly classified** monetary or nonmonetary, and unclassified accounts are flagged
  rather than defaulted
- **The average-rate method is stated**, and seasonality was tested before relying on a simple average
- **Intercompany mismatch before translation is reported separately** from the translation effect, and each
  balance's settlement or net-investment designation is documented
- **Translation precedes elimination**, and each entity is translated separately before consolidation
- Every figure carries its currency; no column mixes currencies unlabelled
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet, **per entity**
- `mock` status is reported **per entity**, and no group figure rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No exchange rates, translated balances or CTA amounts are persisted** into a skill bundle; every
  persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no remeasurement, translation or CTA entry posted
