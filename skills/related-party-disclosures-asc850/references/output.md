<!-- related-party-disclosures-asc850 · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`) — **all files read**, since several may be in scope
- Framework applied: ASC 850 or IAS 24
- Date and time of the reads; period covered
- **Fixture flag** — any `mock: true`? In bold, with the specific warning: **this skill's headline output is a negative finding, and on fixture data a negative finding is guaranteed and worthless.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see immediately that Step 1 was almost entirely human** and that two of Step 2's four procedures were not run by Mosofin at all.

**Section D — What was not done, and why**
- **The org chart and cap table** — **no cap table on this surface**
- **Key personnel, directors, close family** — **no such fields exist in a general ledger**
- **Management representation** — a person represents
- **Contracts and board minutes** — not on this surface, and board minutes are where undisclosed relationships surface first
- **Terms of related-party balances** — in the agreements, where agreements exist
- **Arm's-length conclusions** where no comparable was available
- **Commitments, guarantees and nil-value transactions** — **not transactions, therefore not in the ledger**
- **Sign-off**, and **the disclosure itself.** The gateway is read-only

**Section E — Unknowns carried forward**
Open candidates from Sheet 6. Parties whose related period is undetermined. Balances whose terms are unknown. Transactions with no available comparable. New counterparties since the last refresh, unreviewed.

**Section F — Parameters used**
The related-party list applied, with its date. Match method — exact, fuzzy, which variants. Fields searched. Company files included. Period. **A completeness procedure that cannot be reproduced is not evidence**, and next quarter's refresh needs to run the same match against a changed list.
