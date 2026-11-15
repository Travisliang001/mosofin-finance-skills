<!-- aml-kyc-procedures · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Sanctions are strict-liability and mandatory**: a sanctions match isn't risk-rated — dealing
with a sanctioned party is prohibited regardless of intent. Immediate escalation; do not
proceed. Highest priority of anything in this skill.

**Beneficial ownership opacity**: complex structures (layered entities, nominees, trusts) can
obscure the ultimate owner — a key money-laundering technique. Treat as higher risk, apply
EDD, and **do not accept relationships where the beneficial owner cannot be identified**.

**PEPs**: politically exposed persons require EDD and senior approval; family members and
close associates are also typically in scope. PEP status isn't an accusation — it is a risk
factor requiring enhanced measures, and the documentation must read that way.

**Structuring / smurfing**: transactions deliberately kept below reporting thresholds.
Monitoring must detect **patterns**, not just single large transactions — a rule that only
fires above a threshold will never see structuring by design.

**Tipping off**: informing a customer that they are under suspicion, or that a report was
filed, is typically a criminal offence. Strict confidentiality; the escalation process must
protect it — including in how findings are phrased in any shared workpaper.

**Suspicious activity determination and filing**: a regulated decision with strict timeframes,
made by the responsible officer — not casually, and not by this skill. The skill routes and
documents; the officer decides and files.

**Jurisdiction-specific thresholds and forms**: beneficial-ownership thresholds, reporting
thresholds, retention periods, and report types vary by country and change over time. Confirm
current local requirements; **never hardcode** — and never carry a figure forward from a
stored preference without re-confirming it.

**Reliance on third parties**: relying on another party's CDD has specific rules; the obliged
entity usually retains responsibility regardless.

**Ongoing vs. one-time**: KYC isn't a one-time onboarding check — it is ongoing. Periodic
refresh and continuous monitoring are required, on a risk-based cycle.

**False positives**: screening generates many false matches; a documented, consistent review
process is needed to clear them without ignoring real hits.

**Data protection tension**: AML requires collecting and retaining personal data; balance that
with privacy law (lawful basis, retention limits). Flag for legal where they intersect — and
see the Step 10 restriction on never persisting case data into a skill bundle.

**Mosofin cannot screen** — *Mosofin-specific, and the most important one here*. No accounting
or payment datasource exposes a sanctions, PEP, adverse-media, or watchlist check. Produce the
population to be screened; never state or imply a name is clear. If the entity has no
screening tool at all, that is a finding for Sheet 7, not something to work around.

**The customer list in the books is not the regulated customer population** —
*Mosofin-specific*. The books show who was invoiced. Prospects, declined applicants,
introducers, and customers served through an unconnected platform will be missing. State the
difference before anyone treats a coverage figure as complete.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and
say which customers and which transaction period are therefore unmonitored. Monitoring gaps
are themselves a regulatory finding, so this cannot be silent. Surface any `reconnect_url`.

**The transaction-detail tool is `disabled` in this workspace** — *Mosofin-specific*. Do not
monitor from balance reports. A balance nets off exactly the offsetting movements that
layering produces, so it hides the pattern you are looking for. Mark monitoring `[manual]`,
name the tool, and request a transaction export.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data may illustrate a
rule but must never reach a risk rating, an alert disposition, or an escalation about a real
named person.

**Cash-intensive businesses** — *Mosofin-specific limit on a classic AML risk*. Ledger data
covers recorded transactions; unrecorded cash is invisible. Since cash intensity is itself a
primary risk factor, state this limit explicitly rather than letting clean monitoring output
imply clean cash handling.

**The same customer appears in several connected company files** — *Mosofin-specific*. Rate
per entity, then compare. Aggregation across entities is where cross-entity structuring shows
up, so run the comparison deliberately and label the aggregate as an aggregate.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*.
Flag it. Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
