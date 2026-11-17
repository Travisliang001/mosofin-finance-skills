<!-- statement-of-equity-changes · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- **Standalone or consolidated**, and whether NCI arises
- Entity type and framework, **and whether the chart is consistent with the stated entity type**
- Periods presented
- **Fixture flag** — any `mock: true`? In bold: **the source test is the only test here that can fail, and fixture data passes it.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Step 4 was entirely unavailable and Step 0 was entirely automatic.**

**Section D — What was not done, and why**
- **All share counts, all classes, all movements** — **no cap table on this surface**
- **The par / APIC split** on issuances and exercises
- **Non-controlling interest**, where consolidation is performed outside
- **Tie-out 7** — share counts to disclosure
- **Per-share amounts** and any two-class EPS allocation
- **Property dividend fair values**
- **Forfeiture events** and the grant data behind stock compensation
- **The treasury stock method** and the conversion method for convertible instruments
- **Posting.** The gateway is read-only

**Section E — Unknowns carried forward**
Direct retained earnings postings unexplained. Opening-balance breaks with no adjustment line. Movements landing in "Other." Partner capital accounts turned negative. Stock compensation charges that have not varied.

**Section F — Parameters used**
Accounts mapped to each component. Periods read. Treasury method. Framework and entity type. **Comparability across periods is the point of this statement**, and it depends on the same mapping being used each time.
