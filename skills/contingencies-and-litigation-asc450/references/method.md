<!-- contingencies-and-litigation-asc450 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 0b — Completeness sweep (Mosofin addition)
- Step 1 — Classify each matter
- Step 2 — Determine accounting treatment
- Step 3 — Measure accrual and record
- Step 4 — Draft disclosures
- Step 5 — Controls
- Step 6 — Evolve the skill (Mosofin-specific, final step)
- Outputs
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical evidence tool
added.

**Never drop a task because no tool covers it.** In this skill most of the substance is legitimately
`[manual]` — it is legal judgment — and recording that honestly is the correct outcome, not a
shortfall.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the accrual
accounts, the legal spend and the settlement history do not depend on each other. Never serialize them.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_accounts`* — the accrued liability, legal expense, warranty and insurance recovery accounts
  — usually **[auto]**
- *`get_general_ledger`* on those accounts — **existing accruals, their movement, and settlements paid**
  — usually **[auto]**
- *`get_balance_sheet`* / *`get_trial_balance`* — the accrued contingency balance carried — usually
  **[auto]**
- *`get_vendor_expenses`* with a monthly breakdown — **legal spend by firm over time: the completeness
  signal** — usually **[auto]**
- *`search_vendors`* / *`get-vendor`* — **to identify counsel, including any newly added firm** —
  usually **[auto]**
- *`search_bills`* / *`get-bill`* — individual legal invoices and their descriptions — usually **[auto]**
- *`search_purchases`* — settlement payments made directly — usually **[auto]**
- *`search_deposits`* — **insurance recoveries received** — usually **[auto]**
- *`search_journal_entries`* — prior accrual and release entries — usually **[auto]**
- *`get_profit_and_loss`* — the legal and professional fee trend — usually **[auto]**
- *`get_company_info`* — legal name and currency — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask the user in chat, then re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert that task to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data — it cannot support an accrual or a disclosure
about real litigation.

## Step 0b — Completeness sweep (Mosofin addition)

**Run before Step 1.** The contingency list is what management knows about; this tests it against what
the money says.

**[auto]** signals, each of which may indicate an unlisted matter:

- **Legal spend by firm, by month** (*`get_vendor_expenses`*, *`search_bills`*) — a firm being paid
  steadily, or a step-change in fees
- **A law firm newly added as a vendor** (*`search_vendors`*) since the last review
- **Settlement-shaped payments** — a single large payment to a non-trade counterparty
  (*`search_purchases`*, *`get_general_ledger`*)
- **Insurance recoveries received** (*`search_deposits`*) — money arriving from an insurer implies a
  claim
- **Movement on the accrued liability account** not explained by a listed matter
- **A rise in warranty or rework cost**, which may indicate an emerging product issue

**Report each signal against the contingency list**, and flag anything unmatched as a **completeness
question for management and counsel** — phrased as a question, never as an assertion that a matter
exists. Where the sweep finds nothing unmatched, **say that it was run and found nothing**; that is a
positive result and it is what makes the log's completeness defensible.

If the vendor or ledger tools are unavailable, **record the sweep as not performed** rather than
reporting no exceptions.

## Step 1 — Classify each matter

For each matter capture — **[manual]** for all four, with the ledger contributing supporting evidence:

- **Nature of matter**
- **Current status and key dates**
- **Expected outcomes**
- **Insurance / recovery considerations**

**[auto]** to attach to each matter: the legal fees incurred on it to date (where the invoices identify
the matter), any settlement already paid, and any recovery already received. That gives each row a
factual spine even though the assessment itself is supplied.

## Step 2 — Determine accounting treatment

**US GAAP framing** — the classification is **[manual]** (it comes from the assessment); the accounting
consequence is **[auto]** once given:

- **Probable and reasonably estimable: accrue.**
- **Reasonably possible: disclose.**
- **Remote: generally no accrual / disclosure** (with exceptions).

The two tests are separate and both must hold for an accrual: a matter can be **probable but not
estimable**, in which case you disclose and say why you cannot estimate — you do not accrue a guess.

**If a range of loss exists:**

- **Accrue the best estimate; if no best estimate, accrue the minimum of the range** (per applicable
  guidance) **and disclose the range if reasonably possible.**

Accruing the minimum is a rule, not a judgment call — so once the range is supplied, this step is
**[auto]**. Record which was used: best estimate, or minimum-of-range because no point in the range was
better than any other.

## Step 3 — Measure accrual and record

Accrual entry (typical) — `DR` is a debit, `CR` a credit. **Mosofin does not post** — this is a
proposal:

```
DR Legal Expense / Warranty Expense   XXX
    CR Accrued Liability                  XXX
```

**Consider recoveries (insurance) carefully; do not net unless permitted and realizable.** A probable
loss and a probable recovery are assessed separately, and the recovery is generally recognised only
when realisation is assured — netting them prematurely understates both the liability and the asset,
and hides the gross exposure a reader needs to see.

Use the **real account names from the connected chart of accounts** (*`search_accounts`*, **[auto]**).
**[auto]** to compute the movement required: compare the accrual indicated by the assessment against
the balance already carried, and propose only the difference — a common error is re-accruing a matter
in full when part is already provided.

## Step 4 — Draft disclosures

Disclosures should include — **[gated]**: the amounts are **[auto]**, the narrative is **[manual]**:

- **Nature of the contingency**
- **Status**
- **Amount accrued (if disclosed) and / or the range of reasonably possible loss, if estimable**
- **A statement if the loss cannot be reasonably estimated**

Two cautions specific to drafting this from a workspace:

- **Never write a probability or an outcome the assessment did not give you.** Disclosure language about
  live litigation is read by opposing parties; an inference drawn from the fee pattern has no business
  in it.
- **Do not name a matter, a counterparty, or counsel** in a shared workpaper unless the user has
  confirmed it is not restricted. Use a matter reference where privilege or confidentiality applies.

## Step 5 — Controls

- **Legal letter process and completeness** — **[manual]** for the letters; **[auto]** for the
  completeness sweep at Step 0b, which is direct evidence supporting this control
- **Periodic refresh of probability and estimates** — **[gated]**: whether a refresh is *due* is
  trackable from the assessment dates stored at Step 6; the refresh itself is **[manual]**
- **Review by CFO / legal** — **[manual]**, and named: a contingency accrual signed off by nobody is not
  controlled

## Step 6 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved them, ask —
explicitly, at that point, not earlier — whether to save this as their own customized version. A
general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- **The counsel vendor list** — which vendors are law firms, so the completeness sweep runs
  automatically next period and a *new* firm stands out
- **The matter register**: matter references, types, and the entity each attaches to. **References, not
  narratives**
- **The account map**: accrued contingency liability, legal expense, warranty, insurance recovery
- **The framework** and, if IFRS, the provision-recognition threshold applied
- **The assessment cadence** — how often probabilities are refreshed, and who owns each matter
- **The reviewers** — who signs off accruals and disclosures
- The replay recipe: the exact sequence of reads that produced the completeness sweep

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference files; set
`datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write preference files
alongside the installed skill.

**Never persist matter narratives, counterparty names, counsel advice, probability assessments,
estimates, or ranges.** This is the strictest persistence rule in the pack, and for good reason:
litigation assessments may be **privileged**, they are commercially damaging if disclosed, and a stored
probability that later proves wrong is a document nobody wants to explain. **Persist references and
process; never the assessment.**

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — counsel vendors: [list]; accrual account: Provisions; reviewed by CFO and General
Counsel" — not "counsel vendors: [list]". Contingencies attach to specific legal entities, and an
unlabelled matter register applied to the wrong company file accrues a liability in the wrong balance
sheet. Record the chosen **scenario** (single vs multi, and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong to the
workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's; state is the
workspace's** — and **a probability assessment is state**, re-confirmed every period.

On later runs, match stored entity names against Gate 1's live list. An entity in preferences that is no
longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Outputs

- **Contingency log with classification and treatment.** Each matter: reference, entity
  (`display_name`), type, status, probability **as assessed by management / counsel with the date and
  the source**, estimate or range, treatment (accrue / disclose / neither), and the amount.
- **Accrual calculation support.** Including the balance already carried, so the proposed entry is the
  movement rather than the gross.
- **JE package.** Marked clearly as **proposals**.
- **Draft disclosure language and checklist.** With any restricted matter referenced rather than named.

**Completeness sweep report — NEW, Mosofin-specific.**

| Signal | Entity (`display_name`) | Evidence (vendor, amount, period) | Matched to a listed matter? | Question for management / counsel |

**Coverage sheet — NEW, Mosofin-specific.**

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy | `mock` | Gap — what could not be evidenced and who owns it |

Every probability and every estimate reads `manual` with its source named. That is the correct,
expected result — **an `[auto]` probability would be a defect, not an achievement.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming — Mosofin addition** (the original left it unstated, and multi-entity output needs it):
`Contingencies_[YYYY-MM]_[EntityName].xlsx`, where `[EntityName]` is the company file's `display_name`.
Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled user-supplied
evidence. End with a single **Data sources** line grouping calls by datasource. Where the data does not
cover something — every probability, every estimate — **name the person who supplied it** instead of
estimating.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One log, one sweep.

**Multi-entity.** Steps 0–5 run **once per entity**, each call targeting exactly one `data_source_id`,
every matter carrying the entity that bears it. Then:

- **A contingency attaches to a legal entity.** Separate legal entities exist partly to ring-fence
  liabilities, so **which entity is the defendant is a substantive fact, not a presentational one.**
  Never aggregate a group exposure without the per-entity breakdown beneath it.
- **A parent guarantee changes the picture.** Where a parent has guaranteed a subsidiary's obligations,
  the exposure reaches the parent too — but that is a `[manual]` legal fact the books do not hold. Ask.
- **Legal spend may sit at one entity for a matter affecting another.** A group legal function billing
  centrally is common, so the completeness sweep at the parent may surface a matter belonging to a
  subsidiary. Report the signal against the group, then attribute it with the user.
- **Group disclosure aggregates; group accrual does not.** The note may describe the group's exposure,
  but each accrual sits in the entity that bears it.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict per company
file.
