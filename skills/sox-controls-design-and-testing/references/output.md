<!-- sox-controls-design-and-testing · output.md · read for: Stage 5 — the coverage and provenance sheet; check before presenting. Edit here, not in SKILL.md. -->

## Coverage and Provenance sheet (mandatory)

**Section A — Environment**
- Workspace name (never the numeric id)
- Company file `display_name`(s) (never the `data_source_id`) — **each in-scope location separately**
- Framework: COSO / SOX
- Period tested, and whether coverage is full-period
- **Whether the surface exposes user attribution**, and whether shared logins are in use
- **The ITGC conclusion, and its effect on reliance on automated testing**
- **Fixture flag** — any `mock: true`? In bold: **fixture data produces "no exceptions noted" on every test, and those conclusions must never be capable of supporting an ICFR assertion.**

**Section B — Capability map as observed today**
Each tool used: name as returned by `get_datasource_tools`, `effective_policy`, resulting verdict.

**Section C — Steps by verdict**
Every step, and **every control**, marked full-population `[auto]` or sampled `[manual]`. **A reader should see exactly which conclusions rest on complete data and which rest on a sample.**

**Section D — What was not done, and why**
- **Walkthroughs** — a process is people and systems
- **Design assessment** — reasoning about a hypothetical
- **ITGCs** — **not in the accounting data, and foundational to everything that is**
- **Entity-level controls** — tone at the top is not a posting
- **Management review controls** — **the review itself; only the follow-up was testable**
- **Controls evidenced outside the accounting system** — email approvals, workflow tools, physical controls, observation
- **Inquiry and observation** as methods
- **Root cause** — established by talking to people
- **Severity rating and the material weakness conclusion** — **assigned by the framework to management and the auditors**
- **Service organisation controls** — outside the workspace
- **SoD testing**, where attribution was unavailable or logins are shared
- **Certification.** The gateway is read-only

**Section E — Unknowns carried forward**
Exceptions not yet evaluated as isolated or systemic. SoD conflicts without identified compensating controls. Deficiencies quantified but not rated. Controls whose ledger-evidenced status is undetermined. Uncorrected exceptions indicating failed follow-up.

**Section F — Parameters used**
Populations, periods, thresholds, conflict definitions, sampling method where sampled. **A control test that cannot be re-performed is not evidence** — and an auditor will re-perform this one.
