<!-- xbrl-tagging-checklist · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Registrant `display_name` (never the `data_source_id`), **and every file read**
- **Consolidated or component-level basis**
- Taxonomy version in use
- Period and comparative period, **and whether the comparative was restated**
- Date the reference schedule was produced, **and the date it was last re-run**
- **Fixture flag** — any `mock: true`? In bold: **a reference schedule is designed to be trusted without question; a fixture one must not be.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Steps 1, 2, 3 and 5 were human and only Step 4's reference side was not.**

**Section D — What was not done, and why**
- **Reading the filing document** — **Mosofin cannot read it**
- **Reading the taxonomy** — an external published artefact
- **Element selection** — requires both of the above
- **Extension decisions, anchoring and naming**
- **Tagging itself**
- **Share classes, share counts and EPS** — **no cap table on this surface**
- **Pre-validation and EDGAR validation** — a tool Mosofin does not have
- **Warning assessment and reviewer sign-off**
- **Filing.** The gateway is read-only

**Section E — Unknowns carried forward**
Figures whose reference could not be produced. Dimensions not native to the ledger. Warnings assessed but unresolved. Extensions carried forward without re-justification. Comparatives whose restatement status is unconfirmed.

**Section F — Parameters used**
Accounts mapped to each statement line. Periods read. Dimension sources. Consolidation basis. **A reference schedule is IPE and must be re-performable**, per `sox-controls-design-and-testing`.
