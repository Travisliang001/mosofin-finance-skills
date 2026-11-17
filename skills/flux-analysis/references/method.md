<!-- flux-analysis · method.md · read for: Stages 3–6 — the analysis itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Line the accounts up side by side
- Step 2 — Apply both thresholds
- Step 3 — Drill into each flagged account
- Step 4 — Assign the driver and draft the explanation
- Step 5 — Prove the cash movement
- Step 6 — Proposed entries and owner questions
- Step 7 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios

Each step carries an `[auto]` / `[gated]` / `[manual]` verdict and the typical evidence tool.
**Never drop a task because no tool covers it.** A `[manual]` task is a task with a *named gap*.
Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull every period in **one batch**: the reads do not depend on each other. The server is
**stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`get_profit_and_loss`* for the period and each comparison period, on the **same accounting
  method** — usually **[auto]**. A monthly trend (`summarize_column_by` month) over 13 months or
  more also gives the account's normal range.
- *`get_balance_sheet`* at the end of the period and each comparison date — usually **[auto]**
- *`get_general_ledger`* for the period — **[auto]** if enabled; read it after Step 2 for the
  flagged accounts only, if the tool takes an account filter
- *`search_journal_entries`* for the period — the manual entries that most often explain a
  movement

On the upload path the same evidence comes from the files accepted at validation.

## Step 1 — Line the accounts up side by side

One row per account: current, each comparison period, the change in amount and in percent. Keep
the statement grouping (revenue, cost of sales, operating expenses, other; assets, liabilities,
equity) so subtotals flux too.

- Match accounts by **number and name**. An account present in one period only is a row of its
  own, not dropped: it is either new, closed, or renamed (see edge cases).
- Express expense accounts as **a share of revenue** as well. "Marketing up 53% while revenue is
  down 5%" is a finding; "marketing up 53%" alone is not.
- Show gross margin and net margin for each period.

## Step 2 — Apply both thresholds

Flag a movement when it passes **both** the percentage and the amount threshold, separately for
the income statement and the balance sheet. A movement **at or above** a threshold passes it;
compare unrounded figures. One threshold alone floods the list with small
accounts (percentage) or ignores mix changes in big ones (amount).

Always flag, whatever the thresholds:

- an account that goes **to nil** from a recurring balance, or appears from nil, when the
  amount that stopped or started is at least half the amount threshold
- a **sign change** (an asset with a credit balance, an expense with a credit)
- **gross margin** moving by a percentage point or more

State the thresholds on the face of the output, and list one line under them for the largest
movement that did **not** trip, so the reader can see where the line was drawn.

## Step 3 — Drill into each flagged account

For each flagged account, read the postings behind the movement **[auto]** with
*`get_general_ledger`* or the uploaded detail:

- the largest postings in the period, and anything in the comparison period that did not recur
- manual journals, and who posted them, and when (an entry posted after the comparison period
  closed is a timing driver)
- the account's monthly history: is this month out of its normal range, or is the comparison
  month the odd one?

Without ledger detail the movement can be flagged but not explained: mark it **"unexplained:
asked"** and say which read would have explained it.

## Step 4 — Assign the driver and draft the explanation

Every flagged movement gets exactly one primary driver:

| Driver | What it means | Typical evidence |
|---|---|---|
| **Volume** | More or fewer units, at the same rate | Revenue moved the same way; unit counts |
| **Price / rate** | Same volume, different rate | Contract, price list, rate change |
| **Mix** | A different blend of products, customers or costs | Margin moves while volume does not |
| **Timing** | Recorded in a different period from the activity | Late or early posting, missing accrual, a month with no entry |
| **One-time** | A single event that will not recur | One large posting with a clear memo |
| **Error** | Posted to the wrong account, period, or amount | Mis-coding, duplicate, reversal missing |

Write each explanation in one or two sentences: **what moved, by how much, the driver, and the
evidence**. If the user listed known events (Stage 1, F), use them, citing the user. Never
invent a reason; where the evidence runs out, write "unexplained: asked" and draft the question.

**An account that drops to nil from a recurring amount is a timing or error driver until proven
otherwise.** A subscription, rent or depreciation line does not stop by itself.

## Step 5 — Prove the cash movement

With balance sheets for both dates, prove the change in cash:

```
change in cash = net income + non-cash charges (depreciation, amortisation)
                 − increase in receivables − increase in inventory − increase in prepaids
                 + increase in payables and accruals
                 − debt repaid + debt drawn − dividends + equity raised
                 ± other balance sheet movements
```

The difference must be **nil**. A difference means a balance sheet line is missing from the
bridge or the balance sheet does not balance: report it. Without a balance sheet, mark this step
**not run** and say so.

## Step 6 — Proposed entries and owner questions

For a **timing** or **error** driver with enough evidence, propose the correcting entry. `DR` is a
debit, `CR` a credit; every entry balances. **Mosofin does not post** — these are proposals.

```
Missing recurring charge (e.g. a subscription not posted this month)
DR <expense account>              XXX
    CR Accrued liabilities             XXX
```

Use the **real account names** from the chart of accounts (*`search_accounts`*, **[auto]**).

For every movement marked "unexplained: asked", draft one question to its owner (Stage 1, E),
grouped by owner: the account, both figures, the change, and what evidence would explain it.
The questions are drafts; the skill sends nothing.

## Step 7 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them,
ask — explicitly, at that point, not earlier — whether to save this as their own customised
version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- the thresholds for each statement
- the account owners
- account groupings and any accounts always reviewed whatever their movement
- recurring accounts expected every month (so a nil is caught next run)
- known one-offs, so they are excluded from future comparisons
- the replay recipe: the reads that produced this analysis

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Key every preference by datasource + entity `display_name`.** Thresholds suited to one company
are wrong for another. **Never persist state**: connections, company files, tool policies and
`mock` status are re-discovered by Gates 1–2 every run. An entity in preferences that is no
longer connected is **flagged**, never silently dropped.

---

## Outputs

- **Flux schedule.** Every account with current, comparison periods, change and percent, and the
  share of revenue for expense lines; flagged rows marked, thresholds stated at the top.
- **Explanations.** One per flagged movement: driver, evidence, and the source (ledger, journal,
  user) — or "unexplained: asked".
- **Cash proof.** The bridge from opening to closing cash, with any difference, or "not run".
- **Proposed entries**, marked as proposals.
- **Owner questions**, grouped by owner, as drafts.

**Coverage sheet — Mosofin-specific.** One row per task in Steps 1–6:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be verified and what the user must supply |

Ask whether the user wants the workpaper as an Excel (`.xlsx`) file, and create it only on a
yes: `Flux_Analysis_[YYYY-MM].xlsx`, and in a multi-entity run
`Flux_Analysis_[YYYY-MM]_[EntityDisplayName].xlsx`. If they decline, give the same sheets as
tables in the chat.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`.

**Multi-entity.** Steps 0–6 run **once per entity**, each call targeting exactly one
`data_source_id`, every movement carrying that entity's `display_name`. A group view is a
separate step: intercompany accounts must net to nil in the group, so their movements are shown
per entity and eliminated in the group flux. Never add entities' movements together without the
label. Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's
verdict per company file.
