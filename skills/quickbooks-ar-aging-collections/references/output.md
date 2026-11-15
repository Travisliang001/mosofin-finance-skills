<!-- quickbooks-ar-aging-collections · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

Absorbs and extends the original's "Run context and provenance."

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- As-of date, and whether it was supplied or defaulted to today
- Accounting basis, **and how it was determined** — parameter observed, or absent
- Extraction timestamp
- **Fixture flag** — did any response carry `mock: true`? In bold, with the warning that the customer names are not real.

**Section B — Capability map as observed today**
Each tool called: its name **as returned by `get_datasource_tools`**, its `effective_policy`, and the resulting verdict. Note every case where the observed policy differed from this file's default — including whether a basis parameter existed, since that is the assertion the original froze.

**Section C — Field provenance**
The original's four-way distinction, made into a table: every field in the output marked `workspace-read`, `calculated`, `user-supplied` or `unavailable`. Calculated fields name the source fields they were derived from, satisfying the "reproducible from visible source fields" check.

**Section D — What was not done, and why**
The `[manual]` list. For this skill it will typically include:

- **Dispute status, credit holds, strategic tier** — not accounting fields; not on any accounting surface
- **The customer's own confirmation of the balance** — an audit confirmation, obtained from the customer
- **Cash-basis aging**, if requested and unavailable
- **Exact credit sales**, if the connector could not separate them from cash sales
- **Escalation and late-fee policy**, if not supplied
- **Sending anything.** The gateway is read-only and this skill has no send path

**Section E — Unknowns carried forward**
The reconciliation variance, if unexplained. Invoices with missing due dates. Customers with unapplied credits still unresolved. Suspected duplicate invoices not yet confirmed. These are the opening work list for the next run.

**Section F — Parameters used**
Bucket definitions. Tolerance. DSO denominator and whether it was exact or a proxy. Ranking factors actually applied, and which were omitted for want of input. Anyone re-running next month needs these for the two agings to be comparable — and month-on-month comparability is most of what a collections report is for.
