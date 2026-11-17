<!-- insurance-accounting-overview · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

**The original has no Output Quality Standards section. Everything below is a Mosofin addition**, drawn
from the original's own workflow map, close deliverables and outputs, and from the workspace model.

**From the original workflow and deliverables:**

- **The business model is established** — carrier, MGA or broker — and the close map is tailored to it
- **Premium is covered**: gross written premium, the unearned premium reserve, premium receivables and cash
- **Claims and loss reserves are covered**: case reserves, IBNR, and loss adjustment expenses
- **Reinsurance is covered**: ceded premium and reinsurance payable, recoverables and credit risk
- **Acquisition costs are covered**: commissions payable and DAC where applicable
- **Investment income is covered** where the entity is a carrier: interest and dividends, realized and
  unrealized gains
- The deliverables include the **premium roll-forward and UPR schedule, the loss reserve roll-forward with
  development analysis, the reinsurance recoverable schedules, the commission and DAC schedules, and the key
  reconciliations to GL**
- The outputs include **a tailored close checklist, required data sources and owners, schedule templates
  with a tie-out approach, and a risk list covering data completeness, reserve adequacy and reinsurance
  credit risk**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name` **with its business model**; every excluded one is
  named **as excluded**; **regulated entities are identified**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The account signature was read and compared to the stated business model**, and any contradiction raised
  before proceeding
- **The capability profile is stated** — which parts of the close the workspace can evidence for this model,
  and which it cannot
- **Every close-map task carries a data source, an owner and a verdict**, and the actuarial and
  policy-system rows name their owners rather than being omitted
- **IBNR, reserve adequacy and development triangles are marked `[manual]`** and never estimated
- **UPR is not recomputed from the ledger**; any ratio presented is labelled a reasonableness indicator
- **Losses are presented gross and ceded**, not net only
- **Reinsurance recoverables are aged**, and credit risk is flagged as `[manual]`
- **For a regulated broker or MGA, the client money reconciliation is performed per entity**, with its
  components and date, **unallocated receipts aged**, and **no netting across entities**
- **Trust and own-funds bank accounts are explicitly identified** in the account map
- **Each GL reconciliation reports its difference, including zero**, with reconciling items listed
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no client money conclusion rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No reserve balances, IBNR figures, client money positions, recoverables or premium amounts are
  persisted**, and **no policyholder or claimant name, policy number or claim detail is ever stored**; every
  persisted preference states the datasource and `display_name` it covers
- File naming consistent
- Nothing was written back to any system — no reserve, premium entry or cession posted
