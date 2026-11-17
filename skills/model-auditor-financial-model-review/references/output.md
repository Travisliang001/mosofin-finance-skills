<!-- model-auditor-financial-model-review · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Quality Bar

**The original's Quality Bar, kept as stated, plus the Mosofin additions.**

**The model review is not complete until:**

- **Key figures have source tie-out status**
- **Formula integrity exceptions are logged**
- **Balance and cash checks are tested across all forecast periods**
- **Circular references and broken links are explicitly addressed**
- **Hardcodes inside formulas are flagged or justified**
- **The final pass / hold recommendation is clear and defensible**

**Mosofin additions:**

- The workspace was confirmed **by name** and **the entity or group the model represents was established
  before any tie-out ran**
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**, and
  **an incomplete group means affected tie-outs are OPEN rather than TIED**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The source tie-out is complete across every historical period, not sampled**, since the cost is one
  batch of reads
- **Every TIED figure records the tool, the parameters and the as-at date**, so the tie-out is reproducible
- **STALE is reported separately from FAIL**, and the model's source vintage is recorded
- **Mapping was confirmed before any FAIL was recorded**, so aggregation differences are not reported as
  mismatches
- **OPEN items name their reason** — read unavailable, or genuinely external such as the cap table, a debt
  schedule or an assumption memo
- **Opening balances were tied to source separately from the internal roll-forward checks**
- **The materiality threshold is stated**, and IMMATERIAL DIFF is applied against it rather than to taste
- **Scenario assumptions were compared to historical ranges**, with credibility comments where they diverge
- **The coverage sheet makes clear that Steps 3, 4 and 5 are `[manual]`**, so a complete tie-out is never
  read as a complete model review
- In a consolidated review, **the source is consolidated with intercompany eliminated**, the currency and
  rate basis are confirmed, and equity items dependent on the cap table are OPEN
- `mock` status is reported wherever it applies, and **no pass / hold call rests on a tie-out against mock
  data**
- Every source figure traces to a tool result in this conversation; every model figure to its cell
  reference; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No model contents, figures, tie-out results, issue logs or pass / hold calls are persisted** into a
  skill bundle — **a model under review is frequently confidential**; every persisted preference states the
  datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — **the reviewer changed nothing**, in the books or the model
