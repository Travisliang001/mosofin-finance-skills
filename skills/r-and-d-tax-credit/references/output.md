<!-- r-and-d-tax-credit · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`), and **which entity is claiming**, if different
- Date and time of the reads, **and the date the schedules were assembled**
- Tax year and jurisdiction
- **Fixture flag** — any `mock: true`? In bold. A claim quantum on fixture data means nothing.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict. Note any divergence from this file's defaults.

**Section C — Steps by verdict**
Every step, with the verdict as it actually applied. **The reader should be able to see immediately that Step 2 was entirely human.**

**Section D — What was not done, and why**
For this skill, typically:

- **The qualifying-activity assessment** — the advance, the uncertainty, the systematic process. **Not in any accounting system. Made by people who did the work.**
- **The boundary determination** within each project — a technical judgment
- **Staff time apportionment** — **the ledger holds cost, not time**
- **Current rates, definitions and qualifying-cost rules** — current-sourced, never carried forward
- **Entity size determination** where group aggregation applies — **the group is not in the company file**
- **Entitlement in a group or subcontracting arrangement** — jurisdictional rules, specialist judgment
- **Claim notification and deadline compliance**
- **Specialist review** — and whether it has been obtained
- **Filing.** The gateway is read-only

**Section E — Unknowns carried forward**
Projects surfaced by the ledger but not yet assessed. Costs in the population not yet included or excluded. Grants identified but not yet matched to projects. Rules not yet confirmed. Records flagged as thin.

**Section F — Parameters used**
Accounts and dimensions included in the cost sweep. Vendor filters applied. Apportionment bases used and who supplied them. Rates applied and when confirmed. Anyone re-running next year needs these — and next year's claim will be substantially cheaper for having them.
