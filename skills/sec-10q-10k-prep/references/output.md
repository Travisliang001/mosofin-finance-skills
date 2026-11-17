<!-- sec-10q-10k-prep · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Registrant `display_name`, and **every company file read** (never the `data_source_id`)
- **Consolidated or component-level**, and where the consolidation is performed
- Filer status and the resulting deadline
- Period and comparative period
- **Lock date used for the Step 4b test**
- Date and time of the reads
- **Fixture flag** — any `mock: true`? In bold: **fixture data ties out perfectly and has never been posted into after a lock. This sheet must not be capable of being mistaken for a real tie-out.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Step 5 was entirely human and that every tie-out was half automatic at most.**

**Section D — What was not done, and why**
- **Reading the draft filing.** **Mosofin cannot read the document; every tie-out is one-sided from its perspective**
- **Shares, weighted average shares and EPS** — **no cap table on this surface**
- **The consolidation**, where performed outside the books
- **Commitments and contingencies** — **not transactions**
- **Type 2 subsequent events** — found by asking, not reading
- **Disclosure completeness** — omission leaves no trace
- **Legal review, auditor review, DCP certifications, the reviewer matrix**
- **The final read-through** — the risk is between prose and figures, and prose is not on this surface
- **XBRL tagging**
- **Filing.** The gateway is read-only

**Section E — Unknowns carried forward**
Comparatives differences not yet resolved. Post-lock entries whose tie-outs have not been re-performed. Non-GAAP adjustments not traceable to the ledger. Disclosure areas without an owner. Segments not reconcilable to the consolidated total.

**Section F — Parameters used**
Lock date. Periods read. Company files included and their basis. Non-GAAP definitions applied. Comparative source filing and its date. **A tie-out that cannot be reproduced is not evidence**, and this one may be examined by an auditor or a regulator.
