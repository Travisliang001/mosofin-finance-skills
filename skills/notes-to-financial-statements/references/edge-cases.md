<!-- notes-to-financial-statements · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Private company with reduced disclosures**: **private entities have fewer requirements — e.g. US GAAP
private company alternatives, IFRS for SMEs. Apply the right reduced-disclosure framework.**

**First-time adoption of a framework** — e.g. first IFRS statements: **extensive transition disclosures
required (IFRS 1).**

**Going-concern doubt**: **requires specific disclosure of the conditions, management's plans, and whether
the plans alleviate the doubt. Significant wording care; flag for legal and audit.**

**Litigation with uncertain outcome**: **balance disclosure — informing users — against prejudicing the
entity's legal position. Legal counsel must review. Never state a probable loss amount that could be used
against the entity in litigation without legal sign-off.** **A hard rule here.**

**Subsequent event that's a material acquisition**: **may require pro-forma disclosures.**

**Related party transactions not at arm's length**: **disclose the non-arm's-length nature; tax and
regulatory implications** (the transfer pricing documentation if cross-border).

**Recently issued standards not yet adopted**: **disclose the expected impact, or state it's being
assessed.**

**Concentration risks**: **customer, supplier, geographic, or product concentrations require disclosure if
significant.** *Mosofin note*: **all four are measurable**, and this is one disclosure that is more often
asserted than computed.

**Fair value Level 3 measurements**: **require extensive disclosure of valuation techniques, inputs, and
sensitivity.** **[manual]**; no fair values here.

**Comparative period restated**: **disclose the restatement, the nature of the error or reclassification,
and the effect on each affected line**.

**Segment note**: **coordinate with `segment-reporting` for the segment disclosures.**

**A policy note that contradicts the data** — *Mosofin-specific, and rarely tested*. A stated FIFO policy
against a platform running weighted average; a stated life against a different implied one. **Cheap to
detect here.**

**A policy inferred from the data and asserted as the policy** — *Mosofin-specific*. **The data shows
results.** Infer, then ask.

**A note comparative that does not match last year's published note** — *Mosofin-specific*. Usually unposted
audit adjustments. **A visible inconsistency in a published document.**

**Subsequent events drafted from memory** — *Mosofin-specific opportunity*. **The post-period population is
readable**, and this is the note most likely to miss something.

**A subsequent event with no ledger trace** — *Mosofin-specific limit*. A lawsuit filed, a contract lost, a
key person leaving. **Invisible here.** Ask explicitly.

**A name match treated as a related party** — *Mosofin-specific*. **A match to investigate**, and the real
relationships — a director's other company, a family connection — **will not match at all.**

**Group-versus-entity related party confusion** — *Mosofin-specific*. **Intercompany transactions eliminate
in consolidated notes but are disclosable related party transactions in each entity's own statutory
accounts.** Ask which statements these notes accompany.

**A note total that does not tie to the statement face** — *Mosofin-specific*. Now provable rather than
transcribed. **Report the difference.**

**A disconnected group member** — *Mosofin-specific*. Consolidated disclosures are incomplete. Say so before
drafting.

**A result comes back with `mock: true`** — *Mosofin-specific*. **Notes are published and audited.**

**A prior year's note text reused unchanged** — *Mosofin-specific*. **Policy wording may legitimately
persist; figures never do**, and a rolled-forward note with stale numbers is a common and embarrassing
error.

**A stored contingency description is reused** — *Mosofin-specific, and prohibited*. Litigation wording is
legally reviewed for a specific moment.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's checklist to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the note as `[gated]` in the coverage sheet.
