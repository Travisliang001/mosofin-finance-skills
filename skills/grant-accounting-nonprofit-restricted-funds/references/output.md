<!-- grant-accounting-nonprofit-restricted-funds · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original has no Output Quality Standards section. Everything below is a Mosofin addition**, drawn
from the original's own workflow and outputs and from the workspace model.

**From the original workflow and outputs:**

- **Each funding source is classified** — exchange vs. contribution, conditional vs. unconditional,
  restricted vs. unrestricted
- **A fund / grant tracking structure is defined**, with grant IDs, reporting categories and coding rules
- **Revenue and restrictions are recognised** per the terms, with contribution receivable recorded where
  unconditional
- **Release from restriction is recorded when purpose or time restrictions are met**
- **Spend is tracked against budget by grant category**, with unallowable costs flagged
- **Supporting documentation is maintained for audits**
- The deliverables include the **grant register, spend vs. budget reporting, the restricted net assets
  roll-forward, JE templates and coding rules, and the audit-ready evidence checklist**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The grant-to-dimension mapping is stated**, including where it is many-to-many, and no class total is
  presented as a grant total without it
- **Every classification names the agreement clause relied on**, and none was inferred from the ledger
- **Release from restriction is computed from qualifying expenditure with its transaction support**, not
  carried forward
- **Cumulative release is proved not to exceed the award**, and **restricted net assets are reconciled to
  awards less releases**
- **The four compliance checks were run** — overspend by grant and by category, spend outside the grant
  period, untagged spend in grant-funded programs, and dormant grants — with exceptions listed
- **Unallowable-cost rules, once supplied, were tested against the ledger**
- **The dimension coverage rate is reported** where tagging is inconsistent
- Where restricted and unrestricted net assets are not separated in the chart, **the structural gap is
  reported** rather than worked around
- **Account names in proposed entries match the chart**, and the direction of the release entry was
  confirmed against this entity's presentation
- In a multi-entity run, **restrictions are never released by transfer**, fiscal sponsorship is classified
  from the agreement, and release is computed on total qualifying spend across files
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no funder report rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No grant balances, spend figures, release amounts or net asset totals are persisted** into a skill
  bundle, and **no individual donor name, amount or contact detail is ever stored**; every persisted
  preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no contribution, release or reclassification posted
