<!-- insurance-accounting-overview · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**The business model is assumed rather than confirmed** — *the central risk here*. Carrier and broker
accounting share vocabulary and almost nothing else. **Read the account signature and confirm.**

**IBNR estimated from the ledger** — **impossible by definition.** It concerns events nobody has reported.
**Actuarial, always.**

**A reserve balance treated as evidence of adequacy** — the balance is what was posted. **Adequacy is a
separate actuarial question**, and the two are routinely conflated.

**Loss development triangles attempted without claims data** — they need claims by accident year, which is
claims-system data. **Cannot be built here.**

**UPR recomputed from the ledger** — **it cannot be.** Earning depends on policy inception and expiry dates.
The reasonableness ratio is an indicator, not a recomputation.

**Losses shown net of reinsurance only** — **reinsurance does not discharge the obligation.** Show gross and
ceded; the policyholder is still owed in full.

**A reinsurance recoverable treated as cash** — it is a credit exposure, sometimes running for years.
**Age it.**

**Commission recognised in full on cancellable business** — clawback experience is readable through credit
notes and reversals. **Check it before assuming the revenue is earned.**

**Client money reconciled across a group** — *Mosofin-specific, and wrong*. It is **per regulated entity**,
against that entity's own trust accounts. **A surplus in one does not cure a shortfall in another.**

**Own funds left in the trust account** — commission earned but not withdrawn commingles the firm's money
with clients'. **A breach in many regimes even though nobody is short.**

**Unallocated receipts ageing in the trust account** — *Mosofin-specific*. The commonest cause of a
shortfall, and readable with its age.

**A trust account misidentified in the account map** — *Mosofin-specific, and safety-critical*. Classifying
own funds as client money, or the reverse, corrupts the one regulatory control available here. **Confirm the
mapping explicitly and store it per entity.**

**The account signature contradicts the stated model** — *Mosofin-specific*. Reserve accounts in a broker's
chart, or none in a carrier's. Raise it before proceeding.

**Unrealized investment gains without market values** — **[manual]**. There are no market prices here.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say whose
close, or whose client money, is therefore unexamined.

**A result comes back with `mock: true`** — *Mosofin-specific*. **A client money reconciliation on fixture
balances is worse than none** — a false clean result on a reportable regulatory obligation.

**A stored client money position or reserve is reused** — *Mosofin-specific*. Both are state, and the client
money position is a point-in-time regulatory figure. **Recompute it.**

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
apply one entity's trust account map or business model to another.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
