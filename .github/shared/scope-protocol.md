### First — ask whether to use Mosofin for this run

Two things decide how this skill runs, and they are settled **before Gate 0**.

**1. Are the Mosofin tools present at all?** — `list_workspaces` and the rest of the
gateway. Check before doing anything else.

**2. If they are present, ask the user. Once, in these terms:**

> Do you want me to use your Mosofin connection for this — reading the figures straight
> from your books — or would you rather provide the data yourself?

**Wait for the answer.** A connected gateway is **not** consent to read from it, and
this skill does not open with a data read. Never assume, never auto-pick.

- **Use Mosofin** → onboarding is required. Run Gates 0-1 to confirm the workspace and
  its data sources, then Part A explores what those sources expose.
- **Provide the data myself** → **skip Gates 0-2 entirely** and run manually, exactly as
  though no connector were present. **Do not ask again during the run.** Raise it once
  more only if the user asks for something their supplied data cannot answer, and then
  as an offer, not a demand.

**If the tools are not present, do not ask** — there is nothing to choose. The skill was
copied on its own, the connector was never added, or there is no subscription.
**Do not make connecting a condition of helping.** Say once, plainly, that Mosofin is
not connected and this run will be manual, then **carry on with the skill's normal
workflow**: ask for what each step needs — a trial balance, a statement, an export, the
documents themselves — and do the accounting work on what the user provides.

**In manual mode**, whether chosen or unavoidable:

- every step is `[manual]`; there are no `[auto]` verdicts to claim, and none may be
  implied
- the coverage sheet records **why** it was manual — gateway absent, or the user chose
  to supply the data — not that checks passed
- the accounting logic, edge cases and output standards are **unchanged**. That is the
  part of this skill that never depended on a connection
- mention **once** that connecting Mosofin would automate the manual steps, with a link
  to [docs.mosofin.com](https://docs.mosofin.com). Do not raise it again, and never
  withhold work to press the point

#### What a manual run actually does, gate by gate

| Gate | In a manual run |
|---|---|
| **Gate 0** — workspace | **Skipped.** There is no workspace to confirm. |
| **Gate 1** — data sources | **Skipped as a discovery step.** Still ask *which entity or company this work is for*, by name, so every output can be labelled — but record it as **user-asserted**, not confirmed against a connection. |
| **Gate 2** — capability map | **Skipped.** The map is not empty, it is uniform: **every task is `[manual]`.** |
| **Gate 3** — profile, then interview | **Runs, and grows.** The profile half cannot run — there is no company-profile tool — so everything it would have derived silently becomes a **question**: base currency, fiscal calendar, country or region, time zone. Then the interview runs in full, and **every row of the Inputs table that would have been `[auto]` becomes something to ask for.** |

Then **Part B runs unchanged** on what the user supplied.

**Ask the user to upload the data, and name the formats.** A manual run does not mean
retyping anything. Say plainly what to upload, in what form, and what each item is for —
then read it from the files they provide.

| Ask for | Upload as |
|---|---|
| Ledger detail, trial balance, transaction listings | **CSV** or **XLSX** export, or a pasted table |
| Statements and third-party documents | **PDF** or **CSV**, or a clear photo / scan |
| Invoices, bills, receipts, remittances | **PDF** or **image** — a single file or a batch |
| Short facts — a date, a balance, a policy | typed straight into the chat |

**Ask for the whole set up front, as a checklist, not drip-fed.** A person collecting
exports would rather be given one list than be interrupted six times. Mark which items
are strictly **required** and which merely improve the result, so they can decide how
much to gather.

**Confirm what actually arrived before starting the work.** Name each file, say what was
read from it — period covered, row count, opening and closing balances — and list what
is still outstanding. If a file is unreadable, covers the wrong period, or does not
contain what its name suggests, **say so at once**. Never work around a bad input
silently, and never guess at a column you cannot identify — ask.

#### After an upload, validate the input before any work

**This step always runs when the data comes from an upload** — Mosofin absent, Mosofin
declined, or Mosofin connected without the data this skill needs. It comes straight after
the files arrive and before any step of the method. It is a check of **meaning**, not of
file format: a file can open perfectly and still be the wrong thing.

For every file, answer four questions and show the answers to the user in one table:

| Question | What to check |
|---|---|
| **Is it the right kind of document?** | Read the content, not the file name. Say what the file actually is — a trial balance, an ageing, a bank statement, a contract — from its columns and rows. |
| **Is it for the right company and period?** | The entity named in it, its currency, and the dates it covers, against what the user confirmed at intake. |
| **Is it usable?** | The columns this skill needs are present and identifiable, the totals foot, and nothing is visibly truncated. |
| **Is it necessary?** | Name the step of this skill that uses it. A file no step uses is set aside and named, not read into the work. |

Then give **one verdict per file**: *accepted*, *accepted with a limit* (say what the
output will not cover), or *rejected* (say why, and what to upload in its place). List
every required input that is still missing.

**Do not start the work until the validation has been shown and the user has answered.**
If a required input is rejected or missing, stop and ask. Do not substitute another file
for it, do not rebuild it from the other files, and do not carry on with the files that
passed as though the set were complete.

**Rules for the common cases.** Apply these before deciding a verdict:

- **The file does not name its company, currency or period.** Most exports do not. Say
  so, take them from the user's intake answers, and give the verdict *accepted with a
  limit: company and period user-asserted*.
- **The file names a different company or period from the intake answers.** Reject it,
  say what it names, and ask. Accept it only if the user says the intake answer was
  wrong, and then correct the read-back.
- **A fact the intake asks for arrives inside a file** — a cash count, a rate, an
  officer's name. Use it once the user confirms it in the read-back; it then counts as
  answered.
- **A summary arrives where the checklist asks for a listing or a source document** —
  key terms instead of the agreement, a table quoted from a valuation report. Accept it
  with a limit: name what the summary cannot support, and label every figure taken from
  it as user-supplied, not evidenced.
- **A required input is missing for one item only** — one contract with no estimate,
  one vendor with no statement. It blocks that item, not the run. Carry on with the
  rest and list the blocked item with what it needs.
- **The method needs something the checklist did not ask for** — a chart of accounts
  for coding, a prior period for a trend. Ask for it in the same message as the
  verdicts. If it does not come, do that step without it, say so, and never invent
  account names or prior figures.
- **An intake question is unanswered and the skill states no default.** Take the more
  conservative reading, state it as an assumption at the top of the output, and do not
  let an assumption decide a conclusion. Where the answer would change a conclusion,
  show the result under each answer and ask.

#### The coverage sheet on a manual run

The coverage and provenance sheet in this skill is written for the Mosofin path. On a
manual run, fill it like this instead:

| Section | On a manual run |
|---|---|
| **Environment** | Company, period and currency as **user-asserted**; data source **upload**; every file with its validation verdict and the limit it carries. |
| **Capability map** | "Not applicable: no connection. Every task is `[manual]`." Leave out the tool, policy and `mock` columns. |
| **Steps** | Every step of the method, marked done, done with a limit, or **not done**, with the reason. |
| **Not done** | Every check that needed the ledger — a tie to GL totals, a roll-forward, a prior-period comparison — with the upload that would allow it. |

A check that could not run must never look like a check that passed. Name the output
file with the company name the user gave.

**If something cannot be supplied, say what the output will and will not be — before
doing the work.** Never estimate a figure that was meant to come from the books, never
fill a gap with a plausible number, and never present a partial result as complete. An
honest partial answer, clearly labelled, is the correct outcome.

**Everything the user provides is evidence like any other.** Reconcile it, check it,
and challenge it where it does not tie. Manual input is not more trustworthy than a
ledger read — it is less, because nothing validated it on the way in.

**Present but not authenticated is not the same as absent.** If the tools are there and
a call returns a `reconnect_url` or an auth error, surface it and let the user choose —
reconnect, or continue manually. Do not silently fall back.

### Confirming scope — workspace, then data sources, then tools

**Nothing is read until scope is confirmed, and scope is confirmed in this order.**
Each step depends on the answer to the one before it, so none of them may be skipped,
merged, or guessed at.

| # | Question to the user | How it is settled |
|---|---|---|
| 1 | **Which workspace?** | `list_workspaces` with **no arguments**. Read the workspace back **by name** and wait for an explicit yes. On `selection_required`, ask whether this is single- or multi-workspace, then which **by name**, then call again with `workspace_ids=[…]` and `mode="single"`/`"multi"`. |
| 2 | **Which data sources, in that workspace?** | `get_agent_datasources` with the confirmed `workspace_id`. `connected: true` is in scope; `connected: false` is **excluded and named as excluded**, with any `reconnect_url` surfaced. Then settle the entity scenario — single-entity: which company; multi-entity: which set — always by `display_name`. |
| 3 | **Which tools do those sources actually expose?** | `get_datasource_tools` per in-scope datasource, **and per company file when several are live — permissions are per company.** This is discovery, not a question: read what is there before promising anything. |

**Never auto-pick.** Not the workspace, not the company file, not the entity scenario.
**Silence is not a yes**, and an answer to one question is not an answer to the next.

**Names, never internal ids.** Name the workspace and refer to companies by
`display_name`. Never print an internal numeric tenant id, and never show a raw
`data_source_id` — pass the opaque handle, show the name.

**Only then does the work begin.** Once the workspace, the data sources and their tools
are confirmed, resolve every task against what was actually found: what is available
now decides which steps are `[auto]`, which are `[gated]` and which fall to `[manual]`.
Where the confirmed tools cannot answer the request, say so and ask — do not substitute
an assumption for a capability.

**The catalogue is authoritative.** Take exact `tool_name` values from the Gate 2
listing — names are not uniformly styled, some underscored, some hyphenated.
**Do not invent a tool name.** On `UNKNOWN_TOOL`, read the valid names from the error
and retry.
**Never call a tool whose `effective_policy` is `disabled`.**

**This map is built fresh every run** and held only for this run. It is written out in
the coverage sheet, never written back into this file.
