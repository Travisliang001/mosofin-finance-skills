<!-- debt-and-covenant-tracking · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Complete facility inventory with all key terms**
- **Amortization schedules per facility through maturity**
- **Every covenant catalogued verbatim with key definitions**
- **Covenant computations built per the agreement's precise definitions (not book equivalents)**
- **Headroom shown and quantified for each ratio**
- **Forward projection of covenants with sensitivity**
- **Maturity profile and refinancing horizon**
- **Compliance certificate and deliverable calendar**
- **Breach / waiver history maintained**
- **Breaches escalated to management / counsel; accounting effects (current / long-term classification)
  flagged**
- File naming consistent

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**;
  **the covenant testing perimeter is stated on every output**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **No covenant ratio is computed or reported without the agreement's definitions.** Where they are
  missing, the book components appear **labelled as book components**, with the covenant explicitly marked
  not computed
- **Every covenant build shows the bridge**: book component → each definitional adjustment → covenant
  component → ratio
- **The debt-like item sweep was run and its result stated**, including when nil
- **Historic amortization lines are built from ledger movements, not net balance changes**, and actual is
  compared against scheduled
- **The effective rate borne is shown alongside the stated rate**
- **Headroom is expressed as the EBITDA fall that would breach**, not only as a ratio cushion
- Where a breach is confirmed, **the long-term / current classification of the debt was checked**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet
- `mock` status is reported wherever it applies, and **no compliance conclusion rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No covenant ratios, headroom figures, balances or breach positions are persisted** into a skill bundle;
  every persisted preference states the datasource, `display_name` and **facility** it covers
- Nothing was written back to any system — no drawdown, no repayment, no certification
