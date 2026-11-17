<!-- personal-tax-return-prep · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Income organized by type with source documents**
- **Residency / filing status established and its effect applied**
- **Deductions and reliefs applied per jurisdiction** — standard vs. itemized compared where allowed
- **Income correctly bucketed for differential rates** — ordinary / dividend / capital gains
- **Tax computed on current-year brackets and rates** — confirmed, not assumed
- **Credits and payments applied; balance due or refund computed**
- **Document checklist maps every figure to evidence; missing items flagged**
- **No hardcoded rates, brackets, allowances, or thresholds**
- **Cross-border, equity-comp, and HNW situations flagged for specialist**
- **Clear recommendation for qualified professional review before filing**
- **File naming consistent**

**Mosofin additions:**

- **The taxpayer and their relationship to any connected entity were confirmed at Gate 0**, and **no
  owner-specific figure was read without establishing entitlement**
- **The scope boundary is stated**: personal income, personal deductions, rates and allowances are all
  external; **the workspace contributes only where the taxpayer has an interest in a connected business**
- **Where no business is connected, that is reported as a complete outcome**, not a limitation
- Every in-scope entity is named by `display_name`; **entities the taxpayer has no interest in were not
  read**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Every business-sourced figure appears on Sheet 8** with its entity, tool call, as-at date **and the tax
  adjustment still required**, so accounting profit is never presented as taxable profit
- **A share is applied** where ownership is shared, and **no whole-entity figure is reported as the
  taxpayer's income**
- **The basis-period question is raised** where the business year end and tax year differ
- **Drawings and the owner's loan account are quantified and their treatment marked `[manual]`**, with an
  overdrawn balance flagged for its own consequences
- **Every rate, band, allowance, threshold and deadline appears on Sheet 9** with source and year, and
  **none was supplied from memory**
- **Professional review before filing is recommended in the output itself**
- Every figure carries its verdict and source in the coverage sheet
- `mock` status is reported wherever it applies, and **no figure on a signed return rests on mock data**
- Every business figure traces to a tool result, every personal figure to a document the taxpayer holds, and
  every statutory value to Sheet 9; the answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **Nothing about the taxpayer is persisted** — no income, deductions, credits, balances, household details,
  residency conclusions, prior-year figures, rates or allowances
- Nothing was written back to any system — **and nothing was filed**
