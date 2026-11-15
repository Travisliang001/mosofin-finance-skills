<!-- construction-percentage-of-completion · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

All of the original edge cases, plus the ones Mosofin's workspace model introduces.

**Inefficient / wasted costs**: **don't include in the numerator of cost-to-cost — they aren't
progress. Inflates % complete artificially. A common error and audit area.** *Mosofin note*: the ledger
records the cost but not that it was rework — this is `[manual]` and must be asked, not inferred.

**Uninstalled materials (ASC 606)**: **typically excluded from cost-to-cost progress until installed;
revenue may be recognized only for the cost (no margin) on those materials**, depending on
circumstances. *Mosofin note*: materials purchases are visible, installation is not.

**Variable consideration constraint**: **estimated variations and claims should only be included to the
extent highly probable not to reverse. Aggressive inclusion overstates revenue and risks reversal.**

**Claims and disputes**: **not recognized until enforceable and reliably measurable; often well after
the work is done. Don't bake in optimistic claim outcomes.**

**Loss contracts**: **full loss recognition immediately — including the remaining-period loss accrued,
not spread. A frequent restatement area.** *Mosofin note*: identifying them is `[auto]` once estimates
exist. Run the test on every contract, every period.

**Multiple performance obligations bundled** (e.g. design + build + maintain): **identify and allocate
separately if distinct. If integrated and not distinct, treat as one performance obligation.**

**Modifications / claims pending approval**: **be careful about recognizing modifications that haven't
been approved — only when enforceable.**

**Contract assets vs. receivables**: **a receivable is an unconditional right to consideration** (billed
or billable based on time elapsed); **a contract asset is conditional on more than just time. Don't
conflate.** *Mosofin note*: the aging report shows receivables only — contract assets are computed, not
read, so never take the aging as the WIP position.

**Backlog (remaining performance obligations) disclosure**: **includes only enforceable amounts; can be
a significant disclosure for construction entities.**

**Cost-plus contracts**: different — **revenue typically based on costs + agreed margin / fee**; the
transaction price has different mechanics; **still over-time recognition usually applies.** *Mosofin
note*: cost-plus is the one variant where the ledger nearly supplies revenue directly, since revenue
follows measured cost — flag these separately, as their `[auto]` coverage is genuinely higher.

**Joint ventures and joint operations**: construction often involves JV / JO structures **with specific
accounting per the relationship.**

**Costs are not tagged by job at all** — *Mosofin-specific, and the first thing to check*. Without a job
dimension on cost transactions, per-contract costs are `[manual]` in full and the books cannot support
contract-level accounting. Say so, and recommend the tagging change; it converts every future period.

**Company-wide cost allocated across contracts** — *Mosofin-specific*. A percentage complete derived
from an allocation is arithmetic, not evidence, and it drives revenue. Never do it; mark the contract
`[manual]` instead.

**Billings mistaken for revenue** — *Mosofin-specific*. Invoice history is readable and tempting.
Under over-time recognition, revenue follows progress; the gap between them **is** the WIP balance.

**The estimate at completion is stale** — *Mosofin-specific and the highest-impact risk here*. Check it
against costs already incurred **plus committed purchase orders**: an estimate below that floor is
demonstrably out of date. Show the estimate's date and owner on every contract.

**A company file is connected but not active** — *Mosofin-specific*. Name it as excluded and say which
contracts are therefore unmeasured. Surface any `reconnect_url`.

**A result comes back with `mock: true`** — *Mosofin-specific*. Recognised revenue and loss provisions
on real contracts cannot rest on fixture data.

**A stored estimate is reused instead of re-confirmed** — *Mosofin-specific*. Estimates are state, not
decisions. Persist the revision history; re-confirm the current figure every period.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it. Never
apply one entity's job-tagging convention to another; never drop it silently.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
