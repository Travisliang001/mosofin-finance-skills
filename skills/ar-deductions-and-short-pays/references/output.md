<!-- ar-deductions-and-short-pays · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output quality standards

- Every deduction is aged from the **payment date**, with its reason as given and as mapped
- The log's total **ties** to the deduction account or the deducted part of receivables, or the
  difference is reported
- Duplicates (same invoice, same reason, twice) and deductions already credited are found
  **before** any decision
- Every decision — **valid**, **invalid**, **needs backup** — cites its evidence document, or
  names the document that would decide it
- No deduction is called valid or invalid on the customer's reason code alone
- Write-offs are proposed **only within the policy limit**, each naming its approver; without a
  policy none are proposed and that is said
- Every credit memo, write-off, dispute and backup request is a **proposal**; nothing was issued
  or sent
- Proposed entries balance and use the **real account names**
- Items past the dispute window are marked at risk
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**
- The capability map was discovered **this run** via Gate 2
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used and its
  policy, in the coverage sheet
- `mock` status is reported wherever it applies
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention
- No internal numeric ids, no raw `data_source_id` values and no customer bank details appear in
  anything the user sees
- Nothing was written back to any system
