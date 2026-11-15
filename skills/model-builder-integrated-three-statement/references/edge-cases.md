<!-- model-builder-integrated-three-statement · edge-cases.md · read for: Stage 4, and whenever something looks unusual. Edit here, not in SKILL.md. -->

## Edge Cases

**The original has no Edge Cases section. Everything below is a Mosofin addition** — from the domain and
from the workspace model.

**Historicals do not tie** — *the gate*. **Return the source issue list and stop.** A forecast built on
unreconciled history compounds the problem for every period it projects.

**An unmapped account** — *Mosofin-specific, and the commonest silent break*. The model foots, the trial
balance foots, and they are different numbers. **Test the mapped total against the trial balance total.**

**Annual historicals used for a monthly model** — *Mosofin-specific*. **Dividing by twelve destroys
seasonality**, which is exactly what a monthly model exists to capture. **Pull at the model's cadence.**

**The opening balance sheet is an open period** — *Mosofin-specific*. It will move. **Use the last closed
period**, and say which.

**Assumptions presented without their history** — *Mosofin-specific missed opportunity*. **Three periods of
history beside each input costs nothing** and makes every assumption arguable.

**The tool fills in the assumptions** — *Mosofin-specific, and prohibited*. **History is `[auto]`; the
forecast is the user's.** A model whose assumptions came from the builder is an extrapolation.

**A forecast driver with no historical equivalent** — a new product line, a new geography. **Legitimate, and
it should be labelled as unanchored** rather than presented alongside driver-based lines as if it had the
same support.

**Retained earnings does not roll forward in history** — *Mosofin-specific*, and it **frequently fails**:
distributions, prior-period adjustments, reclassifications. **Resolve before forecasting**, because the
model's equity roll depends on it.

**The platform's cash flow statement misclassifies** — *Mosofin-specific*. See
`cash-flow-statement-indirect-method`; platform reports classify by their own rules. **Rebuild rather than
import.**

**Checks run only over forecast periods** — *Mosofin-specific*. **Run them across history too**, so a break
is attributable to the source or the model immediately.

**A model built on summed entity figures** — *Mosofin-specific*. Intercompany is not eliminated. **Revenue,
cost and every driver are overstated.**

**Group drivers computed as averages of entity drivers** — *Mosofin-specific*. **Group DSO is group
receivables over group revenue**, not a mean.

**No FX assumption for forecast periods** in a multi-currency group — *Mosofin-specific*. Easy to forget,
and material.

**The books' history differs from the published statements** — *Mosofin-specific*. For a model shown to
investors, **the history should agree with what was filed.** Ask; see `financial-statement-builder`.

**A result comes back with `mock: true`** — *Mosofin-specific*. **The model will be used to raise money, set
a budget or price a transaction.** Stop.

**The model is delivered flattened** — the original's own instruction: **preserve formulas** unless asked
otherwise. A flattened model cannot be used for what it was built for.

**A stored mapping applied to another entity** — *Mosofin-specific*. Chart-specific. The historicals will
look right and be wrong.

**A stored preference names an entity that is no longer connected** — *Mosofin-specific*. Flag it; never
build against the wrong company file.

**A tool is `permission`-gated mid-run** — *Mosofin-specific*. Ask in chat, re-invoke with
`approved=true` (**reads only — never for a write**) after an explicit yes, and record the task as `[gated]` in the coverage sheet.
