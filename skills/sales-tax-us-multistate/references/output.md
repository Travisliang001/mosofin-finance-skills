<!-- sales-tax-us-multistate · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`) — **nexus is per legal entity**
- **Which address field was used** — ship-to or billing — and whether the analysis is therefore definitive or indicative
- Periods read, and the measurement bases computed (rolling and prior calendar year)
- **Thresholds and rates used, with their source and the date confirmed**
- **Fixture flag** — any `mock: true`? In bold: **fixture addresses map to no real state distribution; the nexus map is not an analysis.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Step 3 was entirely human and Step 1's economic half was not.**

**Section D — What was not done, and why**
- **Physical presence facts** — **and especially inventory location, which no ledger records**
- **Current thresholds and rates** — current-sourced, never carried forward
- **Every taxability determination**
- **Registration status and dates**
- **Filing frequencies assigned by each state**
- **Timely-filing discount rules**
- **Marketplace state-level detail**, where marketplace revenue is booked as a net deposit
- **Home-rule local detail**, where the ledger holds only a state-level tax code
- **VDA strategy**
- **Filing, registering and remitting.** The gateway is read-only

**Section E — Unknowns carried forward**
States approaching a threshold. Exposure quantified but not addressed. Certificate gaps unresolved. Untaxed purchases not yet assessed for use tax. Taxability determinations outstanding. Effective-rate anomalies unexplained.

**Section F — Parameters used**
Address field. Measurement bases. Thresholds and rates with sources and dates. States in scope. Marketplace channels identified. Periods read. **Every one of these must be re-confirmed next period** — which is the point of recording them, not of reusing them.
