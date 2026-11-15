<!-- pensions-and-postretirement-asc715 · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original has no Output Quality Standards section. Everything below is a Mosofin addition**, drawn
from the original's own workflow and outputs and from the workspace model.

**From the original workflow and outputs:**

- **The plan type and its components are identified** — service cost, interest cost, expected return or net
  interest, amortisation of prior service cost, amortisation of actuarial gains and losses, and any
  settlement or curtailment
- **The obligation and plan assets are rolled forward** from the actuarial report
- **Funded status is determined** as plan assets less the benefit obligation and **recorded on the balance
  sheet**
- **Net periodic benefit cost is split** between amounts in earnings and amounts in OCI
- **The journal entries are prepared** — cost and liability, OCI components, and employer contributions
- **Disclosure tables are produced** — assumptions, rollforwards, components of cost, expected
  contributions, benefit payment forecasts
- The deliverables include the **period-end memo, the rollforward schedules, the JE package, the disclosure
  tables, and the controls checklist**

**Mosofin additions:**

- The workspace was confirmed **by name** and **the sponsoring entity identified** before anything was
  computed
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **No actuarial figure or assumption was estimated, derived or supplied from memory**; **every one traces
  to the report by reference**, with the report's date and author recorded
- **The recorded position was compared to the actuarial report** — balance sheet against funded status,
  expense against net periodic benefit cost, AOCI against remeasurement — **and differences reported before
  the entries were built**
- **Whether a pension entry was posted at all this period is stated**
- **Employer contributions were read from the ledger and compared to the report's figure**, with any
  difference explained
- **Entries already posted are identified**, so no contribution entry is proposed twice
- **The earnings / OCI split as recorded was checked against the framework**
- **The framework is stated**, and the expected-return versus net-interest treatment identified accordingly
- **The measurement date was confirmed against the reporting date**
- **Whether the accounts separate the cost components is reported**, since the disclosure depends on it
- **Any asset ceiling is noted** where the plan is in surplus
- In a multi-entity run, **the sponsor is identified and carries the funded status**, participating
  entities' treatment is confirmed from the plan documentation, and **unallocated contributions are raised
  as intercompany**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet — **and the sheet makes clear that most of this skill is `[manual]`**
- `mock` status is reported wherever it applies, and no pension figure rests on mock data
- Every recorded figure traces to a tool result in this conversation and every actuarial figure to the
  report; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No actuarial figures, assumptions, obligations, plan asset values, funded status or participant data are
  persisted** into a skill bundle; every persisted preference states the datasource and `display_name` it
  covers
- File naming consistent
- Nothing was written back to any system — no pension entry or remeasurement posted
