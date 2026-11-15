<!-- grant-accounting-nonprofit-restricted-funds · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**A conditional contribution recognised as revenue early** — **the classic nonprofit misstatement**, and the
workspace cannot detect it: a premature entry looks identical to a proper one. **Only the agreement tells
you.** Ask whether a barrier and a right of return exist, per grant, and record the answer.

**Condition and restriction confused** — **a condition delays recognition; a restriction delays release.**
Getting them the wrong way round either overstates revenue or hides money that is genuinely available.

**A government grant treated as a contribution** — many are **exchange transactions** in substance, and
belong under the revenue standard instead. Test the substance, not the label on the award letter.

**Release computed from a spreadsheet nobody reconciles** — *Mosofin-specific opportunity*. **The
qualifying spend is readable**, so the release can be computed with its support attached.

**Cumulative release exceeds the award** — *Mosofin-specific check*. Earlier releases were overstated;
restricted net assets are understated.

**Restricted net assets do not equal awards less releases** — *Mosofin-specific check*. An entry was missed
or double-posted.

**Spend outside the grant period** — a pure date test, and a common, expensive audit finding.

**Overspend within budget overall but breaching a category cap** — **check both**; funders enforce category
limits independently.

**Untagged spend in a grant-funded program** — a coding error, or **cost the funder was never billed for**.
Both matter before the report goes out.

**A live grant with no spend for months** — the work stalled, or the costs are landing untagged. Surface it.

**Several grants map to one class** — *Mosofin-specific*. **A class total is not a grant total.** Establish
the mapping before treating dimension figures as grant figures.

**Restricted and unrestricted net assets are not separated in the chart** — *Mosofin-specific structural
finding*. **The roll-forward cannot be produced from the ledger.** Report it before anything else.

**A dimension is used inconsistently** — a class present on some transactions and not others is not a
tracking structure. Measure the coverage rate and say what it is.

**Restricted funds transferred to an affiliate and treated as released** — *Mosofin-specific, and
consequential*. **A restriction travels with the money.** The transfer moves a restricted balance.

**Fiscal sponsorship without variance power** — an agency transaction, not the sponsor's revenue.
`[manual]`, from the agreement.

**Indirect costs charged without a rate basis** — ask for the negotiated rate or the de minimis election;
never assume a percentage.

**A result comes back with `mock: true`** — *Mosofin-specific*. **Grant reports go to funders and are tested
in audit.** Fixture-derived spend in a funder report is a serious matter.

**A stored release amount or grant balance is reused** — *Mosofin-specific*. Both are state. **Persist the
terms and the mapping; recompute the amounts.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one organisation's grant mapping to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
