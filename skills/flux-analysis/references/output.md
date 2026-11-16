<!-- flux-analysis · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output quality standards

- The **thresholds** (percentage and amount, for each statement) are stated at the top, with
  whether they were the user's or the default
- A movement is flagged only when it passes **both** thresholds, apart from the always-flag cases
  (nil, appears from nil, sign change, gross margin)
- The largest movement **below** the line is named, so the reader sees where the line sits
- Expense movements are shown against revenue as well as in amount and percent
- Every flagged movement has **one driver** and an explanation that cites its evidence, or is
  marked **"unexplained: asked"** with the question drafted
- An account that **drops to nil** is never called a saving without evidence
- The **cash proof** ties to nil, or the difference is reported, or the step is marked not run
- Proposed entries balance, use the **real account names**, and are marked as proposals
- Owner questions are drafts, grouped by owner; nothing was sent
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
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- Nothing was written back to any system
