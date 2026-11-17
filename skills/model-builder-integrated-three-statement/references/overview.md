<!-- model-builder-integrated-three-statement · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Model Builder — Integrated Three-Statement Model (Mosofin)

Builds a **working financial model** from **historicals plus user assumptions**. The output is a **live,
formula-driven model**: **P&L, balance sheet, and cash flow fully linked, driver-based, and protected by
checks**. **Do not deliver only a static export unless the user explicitly asks for one.**

**In plain words:** take what the business has actually done, work out the handful of rates and ratios that
describe how it operates, let the user say how those change, and let the arithmetic carry the consequences
through all three statements — so that changing one assumption moves everything it should.

It is **workspace-scoped on the foundation**: the historical statements, the mapping and the historical
value of every driver come from tool calls against a company file connected to your Mosofin workspace in
this conversation. **The forecast assumptions are the user's, always.**

## Where the workspace fits: the foundation and the drivers

**Six steps. The first two-thirds of the value the workspace adds sits in Step 2, and the rest in Step 3.**

**Step 2 — validating the historicals — is entirely `[auto]`, and it is a gate, not a formality.** The
original says: *"If historicals do not tie, pause and return a source issue list before building the
forecast layer."*

> **All five validations are queries**: the P&L summing to net income, the balance sheet balancing in every
> historical period, the cash flow reconciling opening to ending cash, the retained earnings roll-forward,
> and the completeness of the account mapping. **And the source issue list the original asks for can
> actually be produced** — with the accounts, the periods and the amounts.
>
> **That matters more than it sounds.** A model built on historicals that do not tie will be discovered
> later — usually by whoever the model was built for. **Catching it before the forecast layer exists is the
> difference between an hour and a rebuild.**

**Step 3 — the drivers — is where the second contribution sits.**

> **Every one of the seven driver categories has a measurable historical value.** DSO, DIO and DPO; gross
> margin by period; opex as a percentage of revenue and by department; capex against revenue and against
> the asset base; the effective interest rate on debt; the effective tax rate.
>
> **[auto]** to compute, and it changes the conversation. **"What DSO should we assume?" is a question
> nobody answers well. "Your DSO has run 44, 47 and 51 days over the last three years — what should the
> forecast use?" is a question that gets a considered answer**, and the resulting assumption is anchored
> rather than invented.
>
> **Compute the historical value of every driver and present it beside the assumption field.** That is the
> single most useful thing this skill does with the workspace.

**And the boundary, which is absolute:**

> **The forecast is the user's. Never generate assumptions.** History is `[auto]`; **the forward view is
> `[manual]`**, and a model whose assumptions were supplied by the tool that built it is not a forecast —
> it is an extrapolation wearing a forecast's clothes. **Present history, ask for assumptions, build what
> they imply.**

**Steps 1, 4, 5 and 6 — architecture, linking, checks and delivery — are model construction**, performed in
the workbook. **Mosofin builds no spreadsheets and posts nothing**; the model is a file produced here from
readable data.

**See a financial model review** — its Step 2 source tie-out and this skill's Step 2
validation are the same operation from opposite ends. **A model built with this skill should pass that one.**
