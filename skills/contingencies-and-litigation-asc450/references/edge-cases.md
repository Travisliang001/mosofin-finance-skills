<!-- contingencies-and-litigation-asc450 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards implicit
in the steps above.*

**IFRS thresholds differ from US GAAP** — and the skill's own title spans both. Under **IAS 37** a
provision is recognised when an outflow is **more likely than not** (broadly, greater than 50%), which
is a **lower bar** than US GAAP's "probable" as applied in practice. **And where a range exists with no
better point within it, IAS 37 points to the mid-point, whereas US GAAP points to the minimum.** Confirm
the framework at Gate 3 and apply its own rule — the two frameworks can produce different accruals from
identical facts.

**Probable but not estimable** — disclose and explain why no estimate is possible. **Do not accrue a
placeholder**; a made-up number is worse than an honest absence.

**A matter is generating fees but is not on the list** — the completeness sweep's whole purpose. Raise
it as a **question** for management and counsel. Never assert that a matter exists or characterise it.

**Legal spend inferred as a probability** — *the central Mosofin-specific hazard*. Fee levels correlate
with activity, not with outcome. A vigorously defended case the entity expects to win generates more
fees than one it expects to settle. **Never infer likelihood from spend.**

**Gain contingencies** — a claim the entity expects to *receive* is generally not recognised until
realised, precisely because optimism is easy. Note them; do not accrue them.

**Netting an insurance recovery against the loss** — assess separately, recognise the recovery only when
realisation is assured, and **show the gross exposure**. A netted disclosure hides the size of the
claim.

**Re-accruing a matter already provided for** — *Mosofin-specific and directly avoidable*. Compare the
assessed amount against the balance already carried and propose only the movement.

**A settlement was paid but the accrual was never released** — *Mosofin-specific and detectable*. Both
the payment and the accrual balance are readable; a settled matter still carrying a provision overstates
liabilities.

**A stale assessment** — a probability from two periods ago is not a current assessment. Track the
assessment date per matter and flag anything overdue for refresh.

**Privileged or restricted matters in a shared workpaper** — ask before naming a matter, a counterparty
or counsel. Use a matter reference where confidentiality applies, and **never persist the narrative**.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say that
its completeness sweep was not run. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data cannot support an accrual or
a disclosure about real litigation.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's matter register to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
