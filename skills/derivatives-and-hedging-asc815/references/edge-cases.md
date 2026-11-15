<!-- derivatives-and-hedging-asc815 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards implicit
in the steps above.*

**Documentation dated after inception** — **hedge accounting is not available for the gap.** Every fair
value movement in that window belongs in profit and loss. This is the harshest and most expensive rule in
the area, and Step 0b's third check exists to find it.

**Amounts stranded in OCI** — the hedged transaction has occurred but the reclassification never happened.
**Both OCI and earnings are misstated** until it does. Directly detectable.

**A forecast transaction that is no longer expected to occur** — the amounts in OCI must be released to
earnings immediately, not held. A hedge of something that will not happen is not a hedge.

**A settlement with no recorded instrument** — cash moved to a counterparty bank with nothing on the
balance sheet. Either an unrecorded derivative or a misposted payment; both are worth knowing.

**A recorded balance treated as a current valuation** — *the central Mosofin-specific hazard*. The carrying
value is last period's mark. Fair value at this date must come from the counterparty or a model.

**The counterparty's mark is the only valuation** — it is not independent; they are on the other side of
the trade. Validating it at least approximately is a control, not a nicety.

**An embedded derivative nobody looked for** — the accounts show nothing because nothing has been
identified. **Absence of evidence is not evidence of absence** here; only contract review finds them.

**Hedge accounting assumed when it was never elected** — many entities hold derivatives and take
everything to profit and loss, which is simpler and entirely valid. Establish which regime applies before
doing any of the work.

**Effectiveness failed and dedesignation not processed** — hedge accounting must stop prospectively, and
the OCI balance follows specific rules rather than simply reversing.

**Only the effective portion booked** — the ineffective portion goes to earnings immediately. A single
hedge can produce entries in both OCI and profit in the same period.

**An internal derivative treated as a hedging instrument** — a swap between group entities nets to zero on
consolidation and generally cannot hedge for group reporting. Only the external leg qualifies.

**The instrument and the hedged item are in different entities** — the designation cannot hold in either
entity's standalone accounts. Common where a group treasury transacts centrally.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
positions are therefore unexamined. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data cannot support a designation,
an effectiveness conclusion or a disclosure.

**A stored valuation is reused** — *Mosofin-specific*. Marks are stale within a day. Persist the valuation
*source*, never the value.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's designation to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
