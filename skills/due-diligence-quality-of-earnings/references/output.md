<!-- due-diligence-quality-of-earnings · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Adjusted EBITDA bridge with each adjustment rationalized, quantified, and tested for true
  non-recurrence**
- **Symmetric treatment of one-time items** (income and expense)
- **Owner / related-party normalizations explicit** (private companies)
- **Stock-based comp treatment clear and defensible**
- **Revenue quality assessed across customer / product / recurring / recognition dimensions**
- **Working capital analysis with a defensible normalized target and methodology**
- **Net debt with itemized debt-like and cash-like items defined for the deal**
- **Maintenance vs. growth capex split documented**
- Forecast assessed for plausibility (if relevant)
- **Risks and quality observations itemized**
- Specialist needs (tax, legal, IT DD) flagged
- File naming consistent
- **No hypothetical synergies in historical adjusted EBITDA**

**Mosofin additions:**

- The workspace was confirmed **by name**, and **whether the target is a connected company file is stated
  explicitly** on every output
- **On buy-side, no acquirer data is presented as target data**
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**; the
  **deal perimeter** is stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The recurring "one-time" test was run against the prior three years** for every add-back, with the
  result shown per adjustment
- **One-time income items are listed alongside expense add-backs**, and total adjustments are expressed as
  a percentage of reported EBITDA
- **The earliest period the data supports is stated**, and no trend is presented beyond it
- **Reported figures were reconciled to the ledger**, with any difference reported as a data-quality
  observation
- **The working capital target is shown under more than one methodology**, with the spread quantified
- **The balance-sheet sweep for debt-like items was run**, and the net debt definition **matches the one
  used in `business-valuation`**
- **Capex is compared against depreciation** over the period, and sustained under-investment flagged
- Carve-out figures, where applicable, are labelled **constructed rather than reported**, with every
  allocation basis shown
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the source, and the periods it drew
  on, in the coverage sheet
- `mock` status is reported wherever it applies, and **no adjusted EBITDA or deal figure rests on mock
  data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No adjusted EBITDA, working capital target, net debt, customer revenue, owner compensation or deal
  term is persisted** into a skill bundle; every persisted preference states the datasource and
  `display_name` it covers
- Nothing was written back to any system — the QofE is analysis for a human to negotiate with
