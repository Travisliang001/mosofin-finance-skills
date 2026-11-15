<!-- cost-accounting-job-order · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Quality checks

- **Job IDs present on all direct cost postings** — **[auto]**, run at Step 0b, with the untagged total
  quantified
- **Overhead pool excludes non-overhead items** (one-time gains / losses, unrelated expenses) —
  **[gated]**, with the pool listed account by account for review
- **WIP does not include costs for closed jobs** — **[auto]**, comparing WIP by job against job status
- **Under / over applied overhead investigated for driver changes** — **[auto]** to compute and trend;
  **[manual]** to explain. A variance that grows period on period means the rate no longer reflects
  reality

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The untagged-posting test was run and its total reported** before any job margin was presented
- **The job dimension used is stated**, and where none exists the output says the books cannot support
  job costing
- **Per-job WIP reconciles to the WIP account balance**, with any difference explained
- **The overhead pool is listed account by account**, not summarised
- **Labour hours and labour rates are distinguished** — hours measured, rates supplied
- A purchase is never presented as a material issue
- No company-wide cost is allocated across jobs by a rule of thumb
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet
- `mock` status is reported wherever it applies, and no job margin driving pricing rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No job margins, customer job values, individual pay rates or the numeric overhead rate are
  persisted** into a skill bundle; every persisted preference states the datasource and `display_name`
  it covers
- Nothing was written back to any system — every entry is a proposal for a human to post
