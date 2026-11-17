<!-- revenue-recognition-asc606 · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- Framework: ASC 606 or IFRS 15
- Practical expedients elected and applied
- Date and time of the reads; contract and periods covered
- **Fixture flag** — any `mock: true`? In bold: **generated deferred revenue unwinds perfectly, so every Step 0 test passes by construction.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see immediately that Steps 1 to 4 were human and Steps 5 to 11 largely were not.**

**Section D — What was not done, and why**
- **The contract** — **not in the accounting system, and it is the primary input**
- **The distinct test and the PO identification** — contract analysis
- **Estimated SSP** where no observable standalone sales exist
- **The variable consideration estimate and the constraint conclusion**
- **The over-time versus point-in-time determination**
- **Control transfer indicators**: title, risk and acceptance — contractual
- **Modification assessments**
- **Remaining performance obligations** — **includes unbilled commitments, which are not in the ledger**
- **The principal versus agent conclusion**
- **Discount rates** for a significant financing component
- **Posting.** The gateway is read-only

**Section E — Unknowns carried forward**
Step 0 findings not yet explained. Contracts where recognised and should-have-been-recognised differ. SSPs supported by thin observable populations. Customers appearing in both the customer and vendor lists. Suspected modifications from billing changes. Commission treatment unconfirmed.

**Section F — Parameters used**
Framework. Expedients elected. SSP sources and observation counts. Measure of progress per PO. Constraint applied. Dimensions used for disaggregation. Periods read. **Next period's schedule must be reproducible from these, or the roll-forward will not tie.**
