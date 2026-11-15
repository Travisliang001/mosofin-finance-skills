<!-- ipo-readiness-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**Close speed asserted rather than measured** — *Mosofin-specific, and the central opportunity*. **Posting
dates are readable.** Measure it; the roadmap is different when you do.

**A fast close optimised at the expense of control** — **speed and ICFR are different requirements.**
Closing quickly by having one person post everything without review is worse, not better.

**A close carried by manual journals** — *Mosofin-specific*. **It will not scale to a public cadence and
each entry becomes a control.** The count sizes the ICFR workstream.

**Comparable years exist in the system but not on a consistent basis** — *Mosofin-specific*. A chart
restructure or an entity change mid-history **breaks comparability**, and it is usually discovered when the
comparatives are drafted, far too late.

**Closed periods reopened** — *Mosofin-specific, and an audit-readiness signal*. A company that routinely
adjusts history is not ready to file it.

**Prior-year comparatives no longer match what was presented** — *Mosofin-specific*. The same check as in
`financial-statement-builder`. It signals unposted audit adjustments or reopened periods.

**Private-company audit mistaken for a PCAOB audit** — **a different standard**, and prior years frequently
need re-auditing. **`[manual]` to establish, and it belongs on the critical path.**

**The equity workstream started late** — **the most common cause of IPO delay in this list**, and the one the
workspace helps with least. Start it first.

**Complex instruments discovered late** — *Mosofin-specific*. **Their existence is often visible on the
balance sheet** even when their terms are not. Flagging them early is cheap.

**Segregation of duties assessed from user fields** — *Mosofin-specific*. **Shared logins and delegated
access break the link.** Surface patterns; do not conclude.

**A Mosofin read treated as retained evidence** — *Mosofin-specific*. It is repeatable and documentable —
see `internal-audit-workpaper` — **but retention is a systems and policy matter.**

**Assessing a structure that is about to change** — *Mosofin-specific*. **Ask about reorganisation before
measuring anything.**

**The group close measured only at the parent** — *Mosofin-specific*. **The group close is only as fast as
its slowest subsidiary**, and consolidation is itself a workstream.

**Intercompany mismatches tolerated at private-company pace** — *Mosofin-specific*. They cannot survive a
40-day deadline. See `intercompany-reconciliation`.

**A result comes back with `mock: true`** — *Mosofin-specific*. **A readiness assessment on fixtures
measures a fictional company**, and it will be relied on for a timetable and a budget.

**The roadmap or its timing is persisted** — *Mosofin-specific, and prohibited*. **An IPO plan is material
non-public information.** Persist method and structure, never the confidential specifics.

**A stored measurement is reused instead of re-taken** — *Mosofin-specific*. **The measurements are the
progress indicator.** Re-take them every time.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
assess the wrong registrant.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
