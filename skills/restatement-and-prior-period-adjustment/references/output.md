<!-- restatement-and-prior-period-adjustment · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`)
- **Entity or group level** — which issued statements are in scope
- Framework: ASC 250 or IAS 8. Public or private.
- Date and time of the reads; periods covered
- **Source of the issued figures** — which document, dated when. **Not "the ledger."**
- **Fixture flag** — any `mock: true`? In bold: **the prior-period sweep returns clean on fixture data by construction, and the restated statements will balance regardless.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see immediately that Step 1's determination, Step 3's conclusion and all of Step 7 were human.**

**Section D — What was not done, and why**
- **The error-versus-estimate determination** — **turns on what was known at the time, which is not in any ledger**
- **The materiality conclusion** — **assigned by the framework to management, auditors and governance**
- **The correction-method determination**
- **Per-share effects** — **no share counts on this surface**
- **Covenant definitions** — **in the credit agreement**
- **Compensation and clawback assessment** — **plans are not ledger data**
- **The fraud question**
- **Root cause** — established by talking to people
- **The control deficiency and material weakness assessment**
- **Non-reliance determination, amended filings, regulatory disclosure**
- **Auditor involvement — mandatory, and not substitutable**
- **Posting, restating, and filing.** The gateway is read-only

**Section E — Unknowns carried forward**
Prior-period postings found but not yet assessed. Periods where the ledger and the issued statements differ and the difference is unexplained. Errors quantified but not yet concluded on. Share counts outstanding. Covenant recomputations awaiting definitions.

**Section F — Parameters used**
Benchmarks and thresholds applied. Periods swept and the lock dates observed. Which statements were used as the issued baseline, and their date. Both materiality methods, shown. **A materiality analysis that cannot be reproduced is not evidence**, and this one will be re-performed by an auditor.
