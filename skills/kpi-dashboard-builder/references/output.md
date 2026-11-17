<!-- kpi-dashboard-builder · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **KPIs selected for decision-usefulness, matched to industry and audience**
- **Every KPI precisely defined** — formula, source, basis, inclusions / exclusions
- **Calculations consistent across periods** — no definition drift
- **Trends shown, not just point values**
- **Targets / benchmarks only where user-provided** — none invented
- **Status indicators meaningful and rule-based**
- **Layout prioritizes the most important metrics; no clutter**
- **Tie-outs to source data**
- **Live formulas (Excel) or in-memory data (HTML)**
- **File naming consistent**
- **No vanity metrics presented as health indicators**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**; the
  dashboard states whether it is **per entity or consolidated**
- The capability map was discovered **this run** via Gate 2, **before metric selection**, so **no tile was
  promised without a data source**
- **Every metric carries its verdict**, and **metrics declined for lack of a source are listed with the
  system that would supply them**
- **No operational metric is approximated from financial data** — **ARR, churn and customer counts are left
  blank rather than derived from revenue**
- **Each `[auto]` metric's definition records the tool, the parameters and the accounts**, so recomputation
  cannot drift
- **The financial tie-out is reported** — dashboard revenue equals the profit and loss for every period
  shown
- **Every tile carries its as-at date and period status**, and open-period figures are labelled as partial
- **Supplied metrics carry their source and date**, distinguishable from computed ones
- **The status rule is stated in words**, not only as a colour
- **Available history was checked before designing a trend**, and trends are not fabricated beyond it
- **Movements are described; drivers are attributed only with evidence**
- In a multi-entity run, **group ratios are computed from group components**, intercompany is eliminated
  before group metrics, currencies are translated with the rate basis stated, and **coverage is reported per
  entity**
- Every metric carries its verdict, source and as-at date in the coverage sheet
- `mock` status is reported **on the face of the dashboard**, not in a note
- Every computed metric traces to a tool result in this conversation; the answer ends with a single **Data
  sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No metric values, trends or targets are persisted** into a skill bundle — **the recipe is stored; the
  numbers never are**; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system
