<!-- vendor-onboarding-and-w9-tin · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`)
- Payer jurisdiction
- **Whether vendor bank details were readable, and under what policy**
- **Whether master-data change history was readable** — and if not, **that Step 0c did not run**
- Vendor count and period of payment history read
- **Fixture flag** — any `mock: true`? In bold: **"no duplicates" and "no bank changes" are this skill's headline outputs, and fixture data guarantees both.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict, including the two Gate 2 answers.

**Section C — Steps by verdict**
Every step. **A reader should see that all screening was human and Step 0 was not.**

**Section D — What was not done, and why**
- **Sanctions, OFAC and PEP screening** — **Mosofin has no list access and clears nobody**
- **TIN / VAT number matching** — a lookup service
- **Form extraction and validation** — **documents are not in the accounting system**
- **Bank account name verification** — from a bank letter
- **Bank-change detection**, where change history was unreadable
- **The onboarding decision, and any hard stop**
- **Vendor creation or amendment.** The gateway is read-only

**Section E — Unknowns carried forward**
Duplicate candidates unresolved. Bank changes unverified. Actively-paid vendors without forms. Expiring forms. Format-invalid tax IDs. Unclassified LLCs. One-time payees now recurring.

**Section F — Parameters used**
Match keys and fuzzy-match thresholds. Payment period. Required-document policy applied. Format rules by jurisdiction. **A duplicate report that cannot be reproduced cannot be re-checked next quarter.**
