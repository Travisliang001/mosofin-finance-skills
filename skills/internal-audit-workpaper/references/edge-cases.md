<!-- internal-audit-workpaper · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Objectivity and independence**: **internal audit must be objective; auditors shouldn't audit areas they
recently operated. Flag independence threats.** *Mosofin note*: **the workspace is read-only and did not
operate the process**, which supports objectivity — **but it is not the auditor**, and the independence
question is about the people.

**Scope limitations**: **if access to evidence or people is restricted, document the limitation and its
effect on conclusions — don't conclude beyond the evidence.** *Mosofin note*: **a disconnected entity and a
`disabled` tool are both scope limitations** in exactly this sense.

**Root cause vs. symptom**: **a finding that stops at the symptom — "reconciliations weren't done" — without
the cause — "no one was assigned and the system doesn't prompt" — yields weak recommendations. Always reach
the cause.** *Mosofin note*: **data gives you the symptom.** The cause comes from asking.

**Quantifying consequence**: **where possible, quantify the impact — dollars at risk, error rate, exposure.
It drives the risk rating and management's attention. Where not quantifiable, describe the risk
concretely.** *Mosofin note*: **quantification is frequently `[auto]`**, and it is one of the most useful
things the workspace contributes.

**Management disagreement**: **document both the finding and management's position objectively; escalate
unresolved high-risk items to the audit committee or governance rather than softening the finding.**

**Sampling limitations**: **a sample finding may indicate a broader issue; consider whether to expand
testing or characterize the finding as indicative. Be clear about what the sample supports.** *Mosofin
note*: **where the population is readable, expanding to 100% is often trivial** — do that rather than
characterising.

**Repeat findings**: **a finding that recurs from a prior audit indicates remediation failed — rate higher
and escalate; the control / governance issue is more serious.** *Mosofin note*: **re-running the stored test
makes recurrence a fact rather than a recollection.**

**Operational vs. compliance focus**: **operational audits assess efficiency and effectiveness
(judgment-based); compliance audits assess adherence to specific rules (more binary). Match procedures and
reporting to the type.** *Mosofin note*: **compliance testing suits `[auto]` procedures far better than
operational auditing does** — efficiency and effectiveness are rarely answerable from a ledger.

**Consulting vs. assurance**: **internal audit sometimes advises (consulting) vs. provides assurance. Keep
the role clear; advising on a process then auditing it creates an independence issue.**

**Report tone**: **findings must be factual and constructive. Avoid accusatory language; focus on the
condition and improvement, supported by evidence.**

**A full-population test read as full assurance** — *Mosofin-specific, and the most important limit here*.
**The ledger records what was recorded.** Completeness needs an external reference point.

**Sampling when the population was readable** — *Mosofin-specific*. Weaker than it needed to be. **Test
everything and say so.**

**A program made entirely of `[auto]` procedures** — *Mosofin-specific*. Check the objectives: **effectiveness
and authorisation are rarely answerable from data.** Some fieldwork is missing.

**"Reviewed the ledger" recorded as work performed** — *Mosofin-specific*. **Not re-performable.** Record
the tool, the parameters, the entity and the as-at date.

**An analytical result presented as a conclusion** — *Mosofin-specific*. The query found a pattern; **the
auditor concludes.**

**No exceptions found, read as the control operating** — *Mosofin-specific*. An absence of anomalies is not
evidence that a control was performed. See `sox-controls-design-and-testing`.

**A `disabled` tool worked around instead of documented** — *Mosofin-specific*. It is a scope limitation.
Record it and state its effect.

**Exception rates aggregated across entities** — *Mosofin-specific*. A group rate hides the entity where the
process actually broke.

**A result comes back with `mock: true`** — *Mosofin-specific*. **An audit conclusion from fixture data
misleads governance.** Stop.

**Findings carried forward outside a formal tracker** — *Mosofin-specific, and prohibited*. They concern
identifiable people and must be closed through the tracker, not remembered.

**A stored program applied to a different entity** — *Mosofin-specific*. Programs are built around specific
systems and accounts. Key them by entity.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the procedure as `[gated]` in the coverage sheet.
