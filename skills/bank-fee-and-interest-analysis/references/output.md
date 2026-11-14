<!-- bank-fee-and-interest-analysis · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

*The original did not carry a Quality Standards section; these are Mosofin additions, plus the
standards implied by the workflow.*

- Every fee is categorized into one of the eight buckets, with its driver marked fixed or volume
- **Every unit rate states its numerator, its denominator count, and the period**
- One-time items are separated from the trend
- Every recommendation is **sized**, with the count and assumption it rests on
- Miscodings name the account they are in and the account they belong in
- Detected netting is quantified and carries a gross-up entry, not a simple fee entry
- **The output states plainly whether a bank statement was available**, and that a GL-only
  analysis understates total bank cost
- **"Missing postings" is reported as not performed when no statement was supplied** — never as
  finding nothing
- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as
  excluded**, with the consequence stated
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous
  conversation or from this file
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that
  tool's policy, in the coverage sheet
- Categories inferred rather than read from a descriptor are labelled as inferred
- Account names in every proposed JE are the **real names from the connected chart of accounts**
- `mock` status is reported wherever it applies
- Every figure traces to a tool result in this conversation or to labelled user-supplied
  evidence; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term
  kept alongside
- No internal numeric ids, no raw `data_source_id` values, and **no bank account numbers** appear
  in anything the user sees or in any persisted preference
- Nothing was written back to any system — every entry and recommendation is a proposal for a
  human
