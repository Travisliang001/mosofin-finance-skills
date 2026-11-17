<!-- benefits-and-401k-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Defined benefit complexity**: DB and OPEB accounting is among the most complex in GAAP / IFRS
and depends entirely on actuarial valuation. **Never estimate the obligation without an actuary.**
The skill structures and records; the actuary provides the numbers.

**US GAAP vs. IFRS for DB**: significant differences in how actuarial gains and losses are treated
(US GAAP deferral / amortization options versus IAS 19 remeasurements to OCI) and in cost
components. **Apply the correct framework** — and confirm it at Gate 3 rather than inferring it.

**PTO payout vs. use-it-or-lose-it**: accrue if PTO vests / carries over and is paid out; a strict
use-it-or-lose-it policy with no payout may not require an accrual. **Confirm the policy** — this
single answer decides whether Step 3 applies at all.

**PTO at current vs. future rates**: accrue at current pay rates; if a payout would be at a future
(higher) rate, consider the effect. Reassess as rates change.

**Self-insured health plans**: require an accrual for **IBNR** claims — an estimate, sometimes
actuarial. **Don't just expense premiums**, because under self-insurance there aren't any.

**Contribution remittance deadlines**: employee retirement contributions withheld **must be
remitted to the plan within regulatory deadlines**; late remittance is a compliance issue, not
just a cash-flow one. Flag unremitted balances. *Mosofin note*: this is `[auto]` and should be run
every period — it is the single most valuable automated check in this skill.

**Vesting of employer match**: unvested match forfeited when employees leave reduces cost or
offsets future contributions. Track vesting.

**Multiemployer plans**: special accounting and disclosure apply where an employer participates in
a plan shared with unrelated employers — the employer generally expenses its required
contributions rather than recognising a share of the obligation, with specific disclosures. Flag
it; do not treat it as an ordinary DB plan.

**Plan amendments / curtailments / settlements** (DB): these trigger special recognition (prior
service cost, curtailment gains and losses, settlement accounting) — actuarial and complex. Flag.

**Multi-jurisdiction benefits**: benefit types and statutory requirements vary by country; **map
per jurisdiction.** A statutory pension in one country may be a voluntary plan in another.

**Employee contributions sitting in the employer's expense account** — *Mosofin-specific and
directly testable*. If withheld money has been coded as employer cost, expense is overstated and
the liability understated. Test for it every run.

**A benefit exists but has no account and no vendor** — *Mosofin-specific*. Absence of an account
is not absence of an obligation; it is the strongest indicator of an unaccrued benefit. Ask rather
than concluding.

**A PTO liability that never moves** — *Mosofin-specific*. Either nobody is taking holiday, or the
accrual is not being reassessed. The second is far more likely.

**No actuarial report is available** — *Mosofin-specific handling of a domain constraint*. Produce
the DB structure with cells marked "awaiting actuarial valuation" and list them in Sheet 8. **Do
not fill them.** An empty schedule that names what it needs is a useful deliverable.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say
whose benefit costs are therefore unmeasured. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Fixture data cannot support a
booked accrual, a disclosure figure, or an assertion that contributions were remitted on time.

**A stored plan term is out of date** — *Mosofin-specific*. Match rates and vesting schedules
change at renewal. Re-confirm stored plan terms whenever the computed cost diverges from the
posted cost.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it.
Never apply it to a different entity; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
