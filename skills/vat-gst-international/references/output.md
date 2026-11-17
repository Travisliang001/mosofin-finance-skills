<!-- vat-gst-international · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name` (never the `data_source_id`) — **and every country registration in scope**
- **How the chart separates countries** — one VAT account pair or several
- **Whether tax codes are exposed per line**, and whether customer/supplier country is recorded
- Periods read
- **Rates and thresholds used, with source and date confirmed**
- **Fixture flag** — any `mock: true`? In bold.

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict, plus the two Gate 2 answers.

**Section C — Steps by verdict**
Every step. **A reader should see that Step 2 was entirely human and Steps 4b, 5b and 8 were not.**

**Section D — What was not done, and why**
- **All rates, thresholds and country rules** — current-sourced
- **Place of supply determinations** — **including the special rules, which turn on what a service was and where it was performed**
- **Establishment and fixed establishment facts**
- **Zero-rated versus exempt determinations**
- **The partial exemption method**
- **VAT number validation** — an external service
- **Evidence of consumer location** for B2C digital services
- **Proof of export** for zero-rated exports
- **Valid VAT invoices** supporting input recovery
- **Customs documentation**
- **E-invoicing and real-time reporting obligations**
- **Filing frequencies**
- **Filing and remittance.** The gateway is read-only

**Section E — Unknowns carried forward**
Reverse-charge population unresolved. Exempt supplies with unrestricted recovery. Blocked costs recovered. Control account not clearing. Countries approaching thresholds. Zero-rated supplies without a recorded customer VAT number. Bad debt relief unclaimed.

**Section F — Parameters used**
Countries, periods, accounts and tax codes read. Rates and thresholds with sources and dates. Partial exemption method. Schemes applied. **Every parameter must be re-confirmed next period rather than reused** — which is the point of recording them.
