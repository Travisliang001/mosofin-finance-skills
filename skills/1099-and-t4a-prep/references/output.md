<!-- 1099-and-t4a-prep · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- Every reportable vendor has a complete record — or an explicit flag naming what is missing
- Each payment is allocated to the correct form and box
- Amounts reconcile to GL totals
- No vendor flagged as reportable without supporting payments
- No payment to a non-reportable entity type included
- Thresholds and rules applied are the **user-supplied** values, sourced and dated in the
  output — never remembered or assumed
- File naming consistent
- Filing due dates noted, but only as supplied by the user

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task in Steps 1–6 carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool
  used, and that tool's policy, in the coverage sheet
- Every `[manual]` task names the tool that would have covered it and what the user must
  supply — no task is silently dropped
- `mock` status is reported wherever it applies, and no filing assertion rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at its first mention, with the
  professional term kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user
  sees — workspaces and company files are referred to by name
- Every persisted preference and generated asset states the datasource and `display_name`
  it covers
- Nothing was written back to any system — every output is a proposal for a human to file
