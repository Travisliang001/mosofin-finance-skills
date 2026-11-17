<!-- healthcare-revenue-cycle-accounting · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**Gross charges reported as revenue** — **the classic healthcare misstatement.** The chargemaster rate is a
list price. Net revenue is the only meaningful figure.

**Charity care recorded as bad debt** — **different things.** Charity care was never going to be pursued;
bad debt was expected and failed. The misclassification overstates expense, understates community benefit,
and is scrutinised.

**Bad debt treated as expense where it is really a price concession** — under the current revenue model,
amounts never realistically collectible **reduce revenue** rather than creating an expense. **Which applies
depends on whether collectability was assessed at the outset.**

**Payer AR and patient AR aged together** — they behave completely differently. Payer AR ages against
adjudication cycles; patient AR against household finances. **Separate them or the aging means nothing.**

**Realization assumed rather than computed** — *Mosofin-specific opportunity*. **Where gross charges are
recorded, the history is a direct read.** Compare the assumption to it.

**Gross charges are not recorded in the GL** — *Mosofin-specific limit*. Realization **cannot** be computed
from the ledger. Say so; do not derive it from net figures.

**A reserve has never been back-tested** — *Mosofin-specific*. Compare each prior reserve to what actually
happened. **A reserve consistently released or topped up is mis-set**, and the pattern is readable.

**Unapplied cash rising** — *Mosofin-specific*. Remittances are not being matched. AR is overstated and the
revenue cycle has a real operational problem.

**A step change in the adjustment rate** — *Mosofin-specific*. A contract changed, a payer changed
behaviour, or something is posting wrongly. Investigate before adjusting the estimate.

**Write-offs concentrated by period, payer or user** — *Mosofin-specific*. **Report as a pattern, never as
an allegation.**

**Denials trend without reason codes** — *Mosofin-specific limit*. The amounts are readable; **the causes
are in the billing system**, and only the causes are actionable.

**The GL and the billing system do not agree** — **that is the finding, not an obstacle.** Quantify the
difference and list the reconciling items.

**Patient-level detail is requested or reproduced** — *Mosofin-specific, and prohibited*. **Work at
aggregate level.** If patient detail is genuinely required, it belongs in the source system under its own
access controls.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
revenue and AR are therefore unexamined.

**A result comes back with `mock: true`** — *Mosofin-specific*. Net revenue and the reserves are the largest
estimates in a healthcare income statement, and a fixture realization rate would drive both.

**A stored realization rate or reserve balance is reused** — *Mosofin-specific*. Both are state, and
realization drifts with payer mix. **Persist the basis; recompute the rate.**

**One entity's realization applied to another** — *Mosofin-specific*. Specialty, site and payer mix all
differ. Never carry a rate across company files.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one practice's account map to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
