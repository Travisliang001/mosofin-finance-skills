<!-- valuation-agent-dcf-comps-football-field · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`) — **the valuation subject**
- **Entity or consolidated basis**, and where consolidation came from
- **Valuation date, and the balance sheet date actually read**
- Purpose and audience; **whether a qualified specialist is required**
- **Fixture flag** — any `mock: true`? In bold.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step. **A reader should see that Steps 3 and 5 were entirely outside the workspace and Step 6's bridge largely was not.**

**Section D — What was not done, and why**
- **The forecast** — **an assertion about the future**
- **All WACC market inputs** — risk-free rate, ERP, beta
- **All comparables and transaction data** — **public filings and deal databases; not on this surface**
- **Options, warrants and the diluted share count** — **no cap table on this surface**
- **The terminal growth judgment**
- **Screening and outlier decisions**
- **The debt-like / cash-like classification decisions** — population surfaced, judgment reserved
- **Any opinion of value.** **Mosofin is not a licensed valuation professional**

**Section E — Unknowns carried forward**
Model history differences unexplained. Debt-like candidates undecided. Restricted cash unresolved. EBITDA basis inconsistent with net debt. Assumptions departing from measured history without comment.

**Section F — Parameters used**
Valuation date and balance sheet date. Bridge components with their classification decisions. WACC components with sources and dates. Terminal method and inputs. Comparable screen criteria. **A valuation is defended against the assumptions as documented**, so reproducibility is the point.
