<!-- bad-debt-and-write-offs · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- Methodology stated and consistent with the chosen framework
- **Loss rates sourced (not assumed)** — with the periods and derivation shown per bucket
- Roll-forward reconciles: opening + activity = closing
- Every specific write-off has a reason, an approval, and a JE reference
- Tax recovery on write-offs only when the jurisdiction permits and the procedure was followed
- File naming consistent
- Forward-looking adjustments (if CECL/ECL) disclosed and quantified

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that
  tool's policy, in the coverage sheet
- **Each loss rate states whether it was derived from the books or supplied by the user**, and a
  derived rate names the periods and accounts it came from
- **No write-off is proposed on age alone** — every one names a qualifying reason from Step 2
- Credit memos and unapplied items were checked before any balance was called a bad debt
- Intercompany balances are identified and excluded from the allowance
- The existing allowance's account name and balance date are stated with the true-up
- Account names in every proposed JE are the **real names from the connected chart of accounts**
- `mock` status is reported wherever it applies, and **no allowance or write-off rests on mock
  data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term
  kept alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- No customer balances, named risk assessments, or write-off case details are persisted into a
  skill bundle; every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — every allowance entry, write-off and tax claim is a
  proposal for a human to post
