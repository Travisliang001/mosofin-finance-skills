<!-- pensions-and-postretirement-asc715 · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**A defined contribution plan treated as defined benefit** — **the most basic scoping error.** **A defined
contribution plan needs only the contribution expensed**; there is no obligation, no actuary and no OCI.
**Confirm the plan type before anything else.**

**A multi-employer plan** — where several unrelated employers participate and **assets and obligations
cannot be attributed** — **may be accounted for as defined contribution** by the participants despite being
a defined benefit plan overall. **`[manual]`, from the plan documentation**, and a common misstatement.

**No pension entry posted at all** — *Mosofin-specific, and the simplest serious finding*. **A sponsor with a
defined benefit plan and no journal has not accounted for it.** One query.

**The recorded liability does not equal the funded status** — *Mosofin-specific*. **An entry never posted, a
prior-year error carried forward, or a report nobody acted on.** All three are common.

**Everything through profit, nothing through OCI** — *Mosofin-specific*, or the reverse. **The entry does not
follow the framework**, and it is visible without the report.

**Contributions differ from the report's figure** — *Mosofin-specific*. **A payment near the measurement
date the actuary did not know about**, or something recorded as a contribution that was not. **Either way
the funded status changes.**

**The contribution entry proposed when it is already posted** — *Mosofin-specific*. **Contributions are cash
and are usually recorded when paid.** Proposing it again doubles the liability reduction.

**The measurement date does not match the reporting date** — the funded status is as at the wrong day.
**Confirm at Gate 3.**

**A discount rate reused from the prior year** — *Mosofin-specific, and the failure this area is most prone
to*. **Rates move materially year to year and the obligation scales off them.** **Never persist an
assumption.**

**A plan in surplus with no asset ceiling test** — **a surplus you cannot access is not worth its face
value.** Easy to miss the first year a plan moves into surplus.

**A single "pension expense" account** — *Mosofin-specific*. **The components disclosure cannot be produced
from the ledger**, and the presentation requirement separating service cost from the other components cannot
be met. Worth knowing before year-end.

**Expected return and net interest confused** — **the ASC 715 / IAS 19 difference.** Same facts, different
expense. See `gaap-vs-ifrs-conversion`.

**A plan amendment omitted** — **prior service cost arises from amendments**, and an amendment that never
reached the actuary produces an obligation that is simply wrong.

**Settlements and curtailments treated as ordinary movements** — **both trigger immediate recognition**, and
a large one-off payment out of the plan may be a settlement rather than benefits paid.

**A group plan's sponsor misidentified** — *Mosofin-specific*. **The obligation lands in the wrong entity's
balance sheet**, and both sets of accounts are wrong.

**Contributions paid by one entity for several** — *Mosofin-specific*. Unallocated, they create an
intercompany balance.

**A result comes back with `mock: true`** — *Mosofin-specific*. **The net pension liability is frequently
among the largest figures on a sponsor's balance sheet.**

**A stored actuarial figure is reused** — *Mosofin-specific*. **All of it is state.** Persist the plan
details and the account map; re-obtain everything else from the current report.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's plan details to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
