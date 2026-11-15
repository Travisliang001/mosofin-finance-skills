<!-- esg-sustainability-reporting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**Spend read as consumption** — *the central error of this skill*. A utility invoice records what you paid.
Tariffs change. **Never present a spend-derived energy or emissions figure as metered consumption**, and
never explain a spend movement as a consumption movement without separating price.

**No emission factor is available** — the calculation cannot proceed. **Do not supply a factor from
memory.** Ask for the database, the version and the year; record all three against every figure.

**A factor version changes between years** — the series is no longer comparable. Disclose the change and
restate, or report both. Silent factor updates are a common cause of unexplained year-on-year movements.

**The ESG boundary differs from the financial boundary** — legitimate and common, but every difference must
be listed and justified. An unexplained difference is the first thing assurance will challenge.

**Intercompany spend inside a group Scope 3 figure** — double-counts. Eliminate for a group disclosure;
retain for an entity disclosure. Decide deliberately, and say which.

**A spend factor applied to a converted currency** — introduces a silent error. Factors are
currency-and-year specific. Record the currency of every spend input.

**One grid factor applied across multiple countries** — wrong, often by a large multiple. Key factors by
entity and jurisdiction.

**A metric with no named owner** — will not survive contact with assurance. Every catalog row needs a
person and a system, including the `[manual]` ones. Especially the `[manual]` ones.

**Reporting only what is easy to measure** — produces a disclosure dominated by Scope 1 and 2 while Scope 3
(usually the majority of the footprint) goes unmentioned. **State what is excluded and why**; an
acknowledged gap is credible, a silent one is not.

**A prior published figure conflicts with the current calculation** — do not quietly change it. Either the
method changed (disclose and restate) or one of them was wrong (correct it explicitly).

**Physical data supplied without a source or date** — treat exactly as you would an unsupported financial
figure. Ask for the meter read, the statement, the waste transfer note.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
activity data is therefore missing. **In ESG an excluded entity changes the total**, which is materially
different from a financial workpaper where it changes only a subtotal.

**A result comes back with `mock: true`** — *Mosofin-specific*. **An ESG disclosure is a public and often
regulated statement.** A fixture-derived figure inside one is not a footnote. Stop and say so.

**A stored metric value or factor is reused** — *Mosofin-specific*. Both are state. Persist the catalog,
the mapping and the factor *source policy*; re-obtain the data and the factors.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it, and
treat it as a **boundary change requiring disclosure**, not a housekeeping detail.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the metric as `[gated]` in the coverage sheet.
