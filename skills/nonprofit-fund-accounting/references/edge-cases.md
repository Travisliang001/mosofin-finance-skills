<!-- nonprofit-fund-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Conditional vs. unconditional contributions**: **misclassifying conditional as unconditional inflates
revenue, and vice versa. The barrier-and-right-of-return test is the key — apply rigorously.** *Mosofin
note*: **undetectable from the ledger** — a premature recognition looks identical to a proper one. Only the
agreement tells you.

**Exchange vs. contribution**: **a "grant" with deliverables of commensurate value to the grantor is an
exchange (revenue under 606), not a contribution. The distinction affects timing and classification.**

**Donor restrictions not met yet but funds spent for the purpose**: **when the entity incurs the expense
satisfying the purpose, that's the release point — record the release.**

**Contributions of long-lived assets** — e.g. a land donation for a program: **classification depends on
donor stipulation; if no stipulation, often implied time restriction over useful life unless the entity's
policy is to release at acquisition.**

**Pledges receivable**: **unconditional pledges = receivable + revenue at present value if multi-year.
Conditional pledges = no recognition until conditions met.** *Mosofin note*: **the receivable balance is
`[auto]`; whether the pledges behind it are conditional is not.**

**Joint costs of multi-purpose activities** — e.g. a fundraising appeal that also educates: **specific rules
on whether and how to allocate to program; misallocation is an audit and regulator focus.**

**Underwater endowments**: **don't ignore — disclose; the deficiency stays in with-donor-restrictions per
UPMIFA or applicable law.** **Requires a fair value, which is `[manual]`.**

**Functional allocation rigor**: **regulators and donors scrutinize program % — over-allocation to program
is improper and a reputational and regulatory risk.** *Mosofin note*: **the percentage is `[auto]` and
should be trended**; an unexplained movement is what draws attention.

**In-kind services**: **only recognized if they meet the specialized-skill criteria; routine volunteer time
is generally NOT recognized as revenue or expense**, though disclosed narratively.

**Liquidity disclosure**: **a required NFP disclosure introduced to improve transparency on financial
resources; design it meaningfully, not boilerplate.** *Mosofin note*: **the quantitative half is largely
computable**, which makes specificity cheap.

**Board-designated vs. donor-restricted**: **only donor-imposed restrictions create the "with donor
restrictions" class; board-designated amounts are still without donor restrictions, because the board can
undesignate.** *Mosofin note*: **the ledger cannot distinguish them** — both may sit in the same account, or
a designated account may look restricted. **`[manual]`, from the minutes.**

**A program class treated as a functional classification** — *Mosofin-specific, and the central trap*.
**Programs and function are different axes.** Establish which the dimension carries.

**The chart does not separate net asset classes** — *Mosofin-specific structural finding*. **The required
split cannot come from the ledger.** Report it before anything else.

**Qualifying spend with no release entry** — *Mosofin-specific, and detectable*. **The classic error the
original names**, and the three signals together identify it.

**The release line does not net to zero** — *Mosofin-specific*. A mechanical error that occasionally reaches
published statements.

**A functional matrix that is mostly allocated rather than directly identified** — *Mosofin-specific*.
**Report the proportion.** A matrix built 80% on judgment is a different document.

**The program percentage moves without an explained cause** — *Mosofin-specific*. Methodology change,
operational change, or misallocation. **Trend it.**

**A restricted transfer to an affiliate treated as a release** — *Mosofin-specific*. **The restriction
travels with the money.**

**A trading subsidiary given net asset classes** — *Mosofin-specific*. It is a for-profit entity; its result
consolidates into the unrestricted column.

**A result comes back with `mock: true`** — *Mosofin-specific*. **These statements go to funders, regulators
and the public.**

**A stored balance or release amount is reused** — *Mosofin-specific*. All state. **Persist the mapping and
the methodology; recompute.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one organisation's dimension mapping to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
