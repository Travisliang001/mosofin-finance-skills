<!-- restructuring-and-severance-asc420 · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`) — **all entities in scope**, since restructurings cross entity lines
- Framework: ASC 420 or IAS 37
- Plan reference, approval date, communication date, expected completion date
- Date and time of the reads; period covered
- **Fixture flag** — any `mock: true`? In bold: **every test in Step 3b looks for a lingering or misdirected balance, and fixture balances do neither.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see immediately that Steps 1 and 2 were human and Step 3 was not.**

**Section D — What was not done, and why**
- **The plan, and evidence of approval** — a board document
- **The communication and its date** — **the recognition trigger, and not in any ledger**
- **The impacted population and individual entitlements** — **HR data**
- **Contract termination penalties** — in the contracts
- **The future-service determination** — turns on the terms of the arrangement
- **The discount rate**, where discounting applies
- **Legal and HR support for the amounts**
- **Posting.** The gateway is read-only

**Section E — Unknowns carried forward**
Reserve balances flagged as stale and not yet explained. Releases credited to unexpected accounts. Suspected severance double-counts. Additions after the expected completion date. Groups whose future-service basis is undocumented.

**Section F — Parameters used**
Plan(s) in scope and their accounts. Recognition basis per group. Discount rate if any. Expected completion date used for Test D. Periods swept. Anyone re-running next quarter needs these for the challenge tests to be comparable.
