<!-- model-auditor-financial-model-review · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**The model's history is stale, not wrong** — *Mosofin-specific, and the most common tie-out finding*. Built
from an older export; the books have since been adjusted, reopened or reclassified. **Report as STALE, not
FAIL** — the cause and the fix are different.

**The books changed after the model was reviewed** — the mirror case. **A review is a point-in-time
statement**; record the source as-at date so the memo remains interpretable later.

**A model line aggregates several accounts** — *Mosofin-specific*. **Confirm the mapping before recording a
FAIL.** A false FAIL costs more credibility than a missed difference.

**A consolidated model tied to a single entity** — *Mosofin-specific*. **Everything fails.** Establish what
the model represents at Gate 1.

**Intercompany not eliminated in the source** — *Mosofin-specific*. Every revenue and cost line differs by
the intercompany amount, and the reviewer reports a model error that is a source error.

**No materiality threshold supplied** — every difference becomes a FAIL. **Ask for one**; the review is
uninterpretable without it.

**A hardcode that makes a historical tie** — *Mosofin-specific cross-check*. **The tie-out finds the number;
the formula review finds how it got there.** A hardcoded historical that ties is a different problem from a
formula-driven one that does not.

**Openings correct internally but wrong at source** — *Mosofin-specific*. **A perfect roll-forward from a
wrong opening is wrong throughout**, and Step 4's internal checks will not catch it.

**The cap table cannot be tied** — *Mosofin-specific*. Share count and equity items are `[manual]`, always.
**OPEN with its reason**, and for an equity-sensitive model that may itself justify a HOLD.

**Scenarios outside anything in the entity's history** — *Mosofin-specific*. Not a formula error; **a
credibility comment**, and the reviewer is the last person able to raise it.

**A debt schedule that cannot be tied** — the balance is readable, the amortisation schedule is not. **OPEN
on the schedule, TIED on the balance** — state both.

**Currency mismatch between model and books** — *Mosofin-specific*. Check at Gate 3 before tying out.

**A year-end mismatch between model and entity** — *Mosofin-specific*. Period structures that do not align
make every period comparison meaningless.

**A result comes back with `mock: true`** — *Mosofin-specific*. **A clean tie-out against fixtures**, on a
model going to a lender or a board.

**The tie-out is complete and read as a complete review** — *Mosofin-specific, and the risk this skill must
manage*. **Five of six steps are still spreadsheet work.** The coverage sheet exists to prevent that
reading.

**A stored mapping applied to a different model or entity** — *Mosofin-specific*. Mappings are specific to
both. False FAILs across the board.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never tie
out against the wrong company file.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the tie-out as `[gated]` in the coverage sheet.
