<!-- model-auditor-financial-model-review · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Model Auditor — Financial Model Review (Mosofin)

Performs **the last pass before a financial model is sent** to a client, board, lender, investor, or deal
team. The review **ties figures back to source**, flags **broken links, balance breaks, circular
references, inconsistent formulas, and hardcodes sitting inside formulas**, then gives a **pass / hold
call**.

**In plain words:** somebody built a spreadsheet that a decision now depends on. Before it leaves the
building, someone should check that the history in it matches reality, that the arithmetic actually works
in every period, and that nothing is quietly typed over a formula.

## One step of six is the workspace's — and it is the one people skip

**Be clear about this up front, because overclaiming here would be easy and wrong.**

| Step | Where the work happens | Verdict |
|---|---|---|
| **1. Freeze the review scope** | the model and the engagement | **[manual]** |
| **2. Source tie-out** | **the books** | **[auto]** — **this is the workspace's step** |
| **3. Formula integrity review** | the spreadsheet | **[manual]** |
| **4. Statement and schedule checks** | inside the model | **[manual]** |
| **5. Scenario and sensitivity review** | inside the model | **[manual]** |
| **6. Issue log and pass / hold call** | judgment | **[gated]** |

**The model is not in the workspace.** Mosofin holds no spreadsheets, reads no formulas and cannot see a
circular reference. **Steps 3, 4 and 5 are inspection of a file the user supplies**, and nothing here
changes that.

**But Step 2 is different, and it matters more than its position suggests:**

> **The source tie-out is the step that most often gets skipped or sampled**, because pulling historical
> financials, trial balances, debt balances and opening positions is slow — so reviewers spot-check three
> figures and move on to the formulas, which are more entertaining.
>
> **Here the source is one read.** **Every historical P&L line, every opening balance sheet figure, the cash
> position, the debt balances** — all `[auto]`, all at once. **So the tie-out can be complete rather than
> sampled**, and **the "OPEN — source missing" flag largely disappears** for anything the books hold.
>
> **That changes the pass / hold call**, because unresolved OPEN items are one of the commonest reasons a
> review ends inconclusive.

**And there is one finding this step surfaces that a spot-check would not:**

> **The model's "actuals" are a snapshot, and the books have moved since.** A model built from a February
> export and reviewed in May contains **February's version of the past** — before the audit adjustments,
> before the reopened month, before the reclassification. **A full tie-out against live books finds this
> immediately**, and it is a genuine Critical issue: **a model whose history does not match the accounts
> will be challenged by the first person who checks.**

**Independence note**: **Mosofin is read-only.** The reviewer reads the books and changes nothing —
appropriate for a review whose whole value is being an independent check.
