<!-- gaap-vs-ifrs-conversion · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Conversion scoped to applicable, material differences**
- **Each difference documented** (source vs. target treatment) **and classified**
  (recognition / measurement / presentation / timing)
- **Adjustments quantified with computations and the deferred tax effect of each**
- **Net income and equity reconciliations bridge source to target, line by line**
- **First-time adoption (if applicable) applies IFRS 1 exemptions and produces required reconciliations**
- **Restated statements and rewritten policies under the target framework**
- **Direction of conversion applied correctly**
- **"Converged" standards not assumed identical**
- **Complex / judgmental areas flagged for technical accounting and audit**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its current framework**; every excluded one
  is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The conversion was scoped from the connected chart of accounts**, and **all ten difference areas appear
  in Sheet 8** — including those ruled out, with the evidence that ruled them out
- **No policy was inferred from a balance**; every accounting policy is recorded as `[manual]` with its
  source
- **Account evidence contradicting the stated source framework was raised before converting**
- **The reconciliation's source net income and equity are tied to the connected books**, with the tool call
  and as-at date
- **Presentation-only differences are tracked separately** and not lost among quantified adjustments
- **The deferred tax effect is computed for every adjustment**, with the rate and its source stated
- Where scoping revealed a structural gap — material rent with no lease liability, for instance — **it is
  reported as a finding rather than absorbed**
- In a multi-entity run, **each entity is scoped separately**, conversion precedes translation and
  consolidation, and the reconciliation is presented per entity as well as in total
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no bridge intended for a lender, listing or group
  parent rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No balances, adjustment amounts, restated figures or reconciliation totals are persisted** into a skill
  bundle; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — no restatement, adjustment or policy change posted
