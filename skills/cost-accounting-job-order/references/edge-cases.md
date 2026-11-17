<!-- cost-accounting-job-order · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

*The original did not carry an Edge Cases section; these are Mosofin additions plus the hazards implicit
in the steps above.*

**No job dimension is in use** — the books cannot support job costing. Say so plainly and recommend the
tagging change; it is the single change that would make every future period automatic.

**A material share of direct cost is untagged** — every individual job margin is understated by an
unknown, unevenly distributed amount. **Quantify it and report it before presenting margins.**

**A purchase treated as a material issue** — buying material and consuming it on a job are different
events. Charging a job when stock is bought overstates that job's cost and understates the next one's.

**Labour hours without rates** — hours are measurable, cost is not. Say which you have; an hours-based
job report is still useful and must not be presented as a cost report.

**The overhead pool contains one-off items** — a legal settlement or an asset-sale loss sitting in the
pool inflates the rate and spreads an unrelated cost across every job. List the pool account by account
so this is visible.

**Per-job WIP does not equal the WIP account balance** — untagged cost has reached the balance sheet.
The difference is the same problem as Step 0b, surfacing later and harder to fix.

**Stranded WIP on a closed job** — cost that was never relieved to cost of sales. It overstates assets
and understates the cost of the job that has already been billed and forgotten.

**The under/over-applied variance grows period on period** — the rate no longer reflects reality. This
is the fourth quality check, and the trend matters more than any single period's figure.

**A large variance closed entirely to COGS** — acceptable when immaterial, distorting when not. Compute
the variance as a percentage of total overhead before applying the policy.

**Margin reported without an estimate** — you have cost and billings, so you have margin, but **variance
against estimate needs the estimate**, which is `[manual]`. Do not present margin as variance.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which
jobs are therefore uncosted. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Job margins drive pricing and bidding;
fixture data cannot support them.

**A stored overhead rate is reused** — *Mosofin-specific*. The rate is state. Persist the method and the
base; re-derive the rate for the period.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's pool or rate to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
