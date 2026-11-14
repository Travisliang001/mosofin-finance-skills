<!-- customer-credit-and-collections-policy · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards implicit
in the steps above.*

**A policy designed without looking at the base** — the central hazard this skill's automated half exists
to prevent. Thirty-day terms for a book that has always paid at fifty-five, an escalation ladder for
volumes nobody has, a credit committee for twelve accounts. **Segment first, then design.**

**Segmentation on the aging instead of on behaviour** — an aging is a snapshot. A habitually slow payer
who happens to be between invoices looks current today. Segment on **measured days-to-pay**, not on who is
overdue this morning.

**A segment assignment from too few invoices** — three invoices is not a payment pattern. State the sample
size per customer and hold thin ones aside rather than banding them confidently.

**Margin used as a segmentation axis without customer-level cost** — applying one company-wide margin to
every customer makes the axis meaningless, because every customer scores identically. Say the dimension
could not be measured rather than presenting a flat figure.

**An order hold rule nobody can enforce** — if the order system cannot stop supply, the rule is an
aspiration. Ask how holds are actually implemented before writing the rule.

**A hold rule that would stop a third of the book** — technically valid, commercially impossible. Test the
proposed rule against the current base before it is agreed.

**DSO reported without its denominator** — total revenue includes cash sales that were never receivable,
so the proxy flatters the figure. State which denominator was used, and use the same one every period.

**CEI and DSO confused** — DSO moves when sales grow even if collections are unchanged. When measuring the
collections function, **CEI is the fairer metric**; when measuring working capital, DSO is the relevant
one. Say which question each answers.

**No baseline captured before launch** — the policy will be judged anecdotally. Capture the four automated
KPIs and the periods used **before** anything changes.

**Disputes invisible because they never became credits** — a dispute resolved by argument leaves no ledger
trace. The credit-memo proxy understates dispute volume; say so rather than reporting it as complete.

**Persistent credits to one customer** — a collections problem in appearance, an upstream process problem
in fact. Surface credits as a percentage of that customer's revenue.

**Governance reported as verified** — *Mosofin-specific*. Separation of duties, committee operation and
override documentation cannot be tested from an accounting datasource. Mark them **designed, not
verified**.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say that the
segmentation and baseline cover only part of the base.

**A result comes back with `mock: true`** — *Mosofin-specific*. A policy sized on fixture volumes fits no
real business, and a segment built on it labels real customers with invented behaviour.

**A stored segment assignment is reused** — *Mosofin-specific*. Assignments are state; the model is the
decision. Re-measure every review, or the policy will be treating customers according to how they behaved
two years ago.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's hold rule or terms to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
