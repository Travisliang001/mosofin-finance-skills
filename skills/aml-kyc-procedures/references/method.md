<!-- aml-kyc-procedures · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

# PART B — The domain work

## Contents

- Step 0 — Fetch the evidence (grounding)
- Step 1 — Frame the regulatory context
- Step 2 — Risk-based approach foundation
- Step 3 — Customer Due Diligence (CDD)
- Step 4 — Enhanced Due Diligence (EDD)
- Step 5 — Screening
- Step 6 — Ongoing monitoring and transaction monitoring
- Step 7 — Suspicious activity escalation
- Step 8 — Recordkeeping and program governance
- Step 9 — Output
- Step 10 — Evolve the skill (Mosofin-specific, final step)
- Both entity scenarios


Every step below is the original procedure, unchanged in count, order, or substance, with
plain-language wording, an `[auto]` / `[gated]` / `[manual]` verdict, and the typical
evidence tool added.

**Never drop a task because no tool covers it.** In this skill a large share of the work is
legitimately `[manual]` — that is the honest shape of AML in an accounting workspace, and
recording it that way is the point. A silently omitted screening step would imply a check
that never happened, which in this domain is the exact failure regulators sanction.

Tool names in *italics* are typical. Resolve real names and policies from your Gate 2 catalog.

## Step 0 — Fetch the evidence (grounding)

Pull the `[auto]` / `[gated]` reads. **Batch independent reads into one message** — the
customer list, the invoice history, and the deposit history do not depend on each other.
Never serialize.

The server is **stateless**: pass `data_source_id` on **every** call, including retries.

Typical opening batch, per in-scope entity:

- *`search_customers`* — the customer population as the books know it — usually **[auto]**
- *`get_customer`* — a customer's full record: address, terms, contact — usually **[auto]**
- *`search_vendors`* — the payment-out side; vendors need screening too — usually **[auto]**
- *`search_invoices`*, *`search_payments`*, *`search_deposits`*, *`search_sales_receipts`* —
  money in — usually **[auto]**
- *`search_purchases`*, *`search_bill_payments`*, *`search_transfers`* — money out and
  between accounts — usually **[auto]**
- *`get_general_ledger`* — full transaction detail for pattern work — usually **[auto]**
- *`get_customer_sales`*, *`get_customer_balance`* — activity and exposure by customer —
  usually **[auto]**
- *`get_company_info`* — the entity's own profile — usually **[auto]**

Handle the envelopes:

- `approval_required` → ask in chat, re-invoke the same tool with `approved=true` (**reads only — never for a write**).
- `entity_required` → ask by `display_name`, then pass that `data_source_id`.
- `tool_policy_disabled` → convert to **[manual]** and record the gap.
- `UNKNOWN_TOOL` → read the valid names from the error; do not guess.
- Dead connection → surface the `reconnect_url`.

Check the **`mock` flag**. `mock: true` is fixture data. It can illustrate a monitoring rule
but **cannot support a risk rating, an alert disposition, or an escalation**. An escalation
built on mock data would be a fabricated allegation about a real person — never do it.

## Step 1 — Frame the regulatory context

Establish whose rules apply and who is accountable, before anything else. **[manual]** —
this is legal and regulatory ground, not ledger ground. The profile tool
(*`get_company_info`*, **[auto]**) contributes the entity's own legal name, address and
industry as inputs only.

Confirm:

- The **jurisdiction(s)** and applicable **AML/CFT** regime (CFT = countering the financing of
  terrorism, which travels with AML in almost every regime)
- Whether the entity is a regulated **obliged entity** — a business the law specifically
  requires to run AML controls — and its specific obligations
- The responsible compliance function — the **MLRO** (money laundering reporting officer) or
  **BSA officer** (under the US Bank Secrecy Act). **Emphasise that they own determinations
  and filings**, not this skill and not the person running it
- That specific thresholds, timeframes, and forms **must be confirmed against current local
  regulation** — do not assume, and do not carry a figure over from a previous engagement

## Step 2 — Risk-based approach foundation

AML follows a **risk-based approach**: put the effort where the risk is, rather than treating
every customer identically. Establish the risk factors:

- **Customer risk** — type (individual / entity / trust), **PEP** status, ownership
  complexity, industry, reputation. **[auto]** for type and industry where the books record
  them (*`get_customer`*, *`search_customers`*); **[manual]** for PEP status, ownership
  complexity and reputation.
- **Geographic risk** — the countries involved, higher for sanctioned or high-risk
  jurisdictions per official lists. **[auto]** to extract the country from customer and
  vendor addresses (*`get_customer`*, *`get-vendor`*) and from where payments go;
  **[manual]** to classify a country as high-risk, because that classification comes from an
  official list this workspace cannot see.
- **Product / service risk** — cash-intensive, cross-border, or anonymity-enabling products
  are higher risk. **[auto]** in part: the books show cash accounts, foreign-currency
  activity, and the product/service list (*`search_items`*, *`search_accounts`*,
  *`get_general_ledger`*).
- **Channel risk** — face-to-face versus remote / non-face-to-face onboarding. **[manual]**;
  the ledger does not record how a customer was met.
- **Transaction risk** — size, frequency, patterns. **[auto]**; this is the strongest
  automated signal available and feeds Step 6 directly.

Build a **customer risk-rating model** combining these into low / medium / high (or a scored
model). **The rating drives the level of due diligence.** State clearly, per factor, whether
the input was measured from the books or supplied by hand — a rating that mixes the two
without saying so cannot be defended in an inspection.

## Step 3 — Customer Due Diligence (CDD)

**CDD** is the baseline "who is this, really?" check, done at onboarding and kept current.

Standard CDD for onboarding and ongoing:

- **Identify and verify the customer** — name, date of birth / incorporation, address,
  identifiers — verified against reliable, independent documents or data. **[manual]**: the
  books hold a *stated* name and address (*`get_customer`*, **[auto]**), which is a starting
  point, **not** verification. Never present a customer record as verified identity.
- **For entities**: legal form, registration, directors, governing documents. **[manual]** —
  a corporate registry is not a connected datasource.
- **Identify beneficial owners** — the natural persons who ultimately own or control the
  customer, typically those above an ownership/control threshold (**confirm the local
  threshold**) — and verify their identity. **[manual]**, always. The books show who you
  invoiced, never who owns them.
- **Understand the purpose and intended nature** of the relationship. **[gated]**: the
  transaction history evidences what the relationship has *actually* been
  (*`get_customer_sales`*, *`search_invoices`*), which is a genuine and useful cross-check
  against what the customer *said* it would be.
- **Determine the source of funds / wealth** appropriate to risk — where this money came
  from, and where the customer's wealth came from generally. **[manual]** for the assertion;
  **[auto]** to observe which accounts and instruments the money actually arrived through
  (*`search_deposits`*, *`search_payments`*).

Document the CDD performed and the evidence obtained — including, for each element, whether
it was verified or merely recorded.

## Step 4 — Enhanced Due Diligence (EDD)

**EDD** is the heavier version, for the relationships that warrant it.

For high-risk customers / relationships (high-risk rating, PEPs, high-risk jurisdictions,
complex ownership), apply EDD — **[manual]** throughout, with the transaction record as
supporting evidence only:

- Additional identity and ownership verification
- **Source of funds / wealth scrutiny with corroboration** — not just an assertion, but
  evidence for it
- **Senior management approval** for the relationship — a named person signing off
- **Enhanced ongoing monitoring** — tighter thresholds and shorter review cycles in Step 6
- For **PEPs**: specific PEP procedures. A politically exposed person holds or held a
  prominent public function, so is more exposed to bribery and corruption risk

Document the enhanced measures and the rationale for applying them.

## Step 5 — Screening

> **`[manual]` — in every workspace, always. Mosofin has no screening tool.**

Screen customers and beneficial owners, at onboarding and on an ongoing basis, against:

- **Sanctions lists** — the relevant official sanctions regimes. Screening for sanctioned
  parties is **mandatory and a strict obligation**
- **PEP lists** — politically exposed persons
- **Adverse media** — negative news indicating financial crime risk
- **Watchlists**

What this skill does here, and what it does not:

- **It does** produce the **screening population**: every customer, every vendor, and every
  beneficial owner supplied by the user, with the exact legal names, trading names,
  addresses and countries held in the connected books (*`search_customers`*,
  *`search_vendors`*, *`get_customer`*, *`get-vendor`* — **[auto]**). Name variants matter
  in screening, so give every spelling the books hold.
- **It does** maintain the **screening log** (Sheet 4) and the false-positive review record.
- **It does not** screen. It cannot check a name against any list, and must never state or
  imply that a name is clear.

**A positive sanctions match has immediate, serious consequences** — potential asset freeze,
prohibition on dealing, mandatory reporting. **Escalate to the compliance function
immediately; do not proceed.** Manage **false positives** — innocent name collisions —
through a documented review, so that clearing them stays consistent and auditable.

## Step 6 — Ongoing monitoring and transaction monitoring

This is the step the connected books genuinely support, and where the automated work lives.

The relationship is monitored on a risk-sensitive basis:

- **Periodic CDD refresh** — more frequent for higher risk. **[gated]**: the books can flag
  which customers have transacted since their last review date and are therefore due
  (*`get_customer_sales`*, *`search_invoices`*), but the review date itself is a stored
  preference or user input.
- **Transaction monitoring** — detect activity **inconsistent with the customer's known
  profile**. **[auto]** over the connected ledger (*`get_general_ledger`*,
  *`search_deposits`*, *`search_payments`*, *`search_invoices`*, *`search_purchases`*,
  *`search_transfers`*, *`get_customer_sales`*). Look for:
  - **Unusual size** — transactions far outside the customer's own history
  - **Unusual frequency** — a dormant account suddenly busy, or vice versa
  - **Unusual patterns** — round-number amounts, repeated identical values, weekend or
    out-of-hours clustering
  - **Unusual geographies** — money moving to or from places the relationship never involved
  - **Structuring** — deliberately breaking a large amount into several smaller ones to stay
    under a reporting threshold. Detect the *pattern*, not the single transaction
  - **Rapid movement** — money in and straight back out ("pass-through"), leaving little
    behind
- **Establish monitoring rules / scenarios** tuned to the entity's risk, with thresholds the
  user confirms. State every rule's logic explicitly so it can be reviewed and re-run.
- **Investigate alerts; clear or escalate.** Every alert gets a disposition and a reason.

Two honesty requirements specific to running this from a workspace:

- **Coverage.** State which accounts and which date range the monitoring actually covered.
  Monitoring that ran over one connected company file while another sat disconnected covered
  less than it appears to.
- **Cash.** Ledger data shows recorded transactions. Unrecorded cash is, by definition,
  invisible here — and cash intensity is a primary money-laundering risk factor. Name this
  limit rather than implying full coverage.

## Step 7 — Suspicious activity escalation

When activity is potentially suspicious — **[gated]** to route and document, **never [auto]**
to decide:

- The framework routes it to the compliance function (**MLRO / BSA officer**)
- **The responsible officer determines** whether to file a suspicious activity / transaction
  report (a **SAR** or **STR**) with the authorities. This is a regulated determination with
  strict rules and timeframes, and **must not be made casually**
- **Tipping off** — telling the customer they are under suspicion or that a report was filed
  — is typically **prohibited**, and often a criminal offence. Strict confidentiality applies
- **Document the internal escalation and decision objectively** — facts and observed
  patterns, not conclusions or characterisations of a person

**This skill structures the escalation process; it does not make the filing determination —
that is the officer's regulated responsibility.** Mosofin, being read-only, could not file
anything even if asked to, and must never draft language asserting that a named person
committed a crime.

A workspace-specific caution: a suspicious-activity escalation names a real, identifiable
person or business. Everything in it must trace to a tool result in this conversation, with
the `mock` flag confirmed false. Never let a fixture-backed figure reach an escalation record.

## Step 8 — Recordkeeping and program governance

- **Recordkeeping**: retain CDD, screening, monitoring, and escalation records for the
  regulatory **retention period** (**confirm the local period**; do not assume one).
  **[manual]** — Mosofin stores nothing on the user's behalf, and a workspace connection is
  not a record-retention system. Say where the records will actually live.
- **Program elements** — the pillars of an AML program: documented **policies**, a
  **designated compliance officer**, **training**, **independent testing / audit**, and a
  **risk assessment**. **[manual]**, but each one gets a row in Sheet 7 with its status.
- **Periodic enterprise-wide AML risk assessment** — the whole-business view of where the
  entity's money-laundering exposure sits, refreshed on a cycle.

## Step 9 — Output

Deliver framework and procedure documentation plus a workpaper.

**Document: AML/KYC Procedures**

The risk-based procedures: CDD/EDD steps, risk model, screening, monitoring, escalation,
recordkeeping.

**Workpaper (.xlsx):**

**Sheet 1: Risk Assessment Model**

Risk factors and the customer risk-rating logic. Mark each factor as measured-from-books or
supplied-by-hand.

**Sheet 2: CDD/EDD Checklist**

By risk level: required identification, verification, beneficial ownership, source of funds.

**Sheet 3: Customer Risk Rating** (if rating customers)

Per customer: factors, score, rating, DD level required. Add the entity `display_name` column
in a multi-entity run.

**Sheet 4: Screening Log**

Customers / owners screened, lists, results, false-positive resolution. **Every row states
which external screening tool produced the result** — this sheet is never populated from
Mosofin data, only from what the compliance function supplies.

**Sheet 5: Transaction Monitoring**

Rules / scenarios, alerts, dispositions. Add the date range and the accounts actually
covered, and note anything outside coverage.

**Sheet 6: Escalation Register**

Internal escalations to the compliance officer — objective facts; decisions are the
officer's.

**Sheet 7: Regulatory Confirmations Needed**

Thresholds, timeframes, forms, retention periods to confirm locally; MLRO / legal items.
Also carry here any missing program pillar found in Step 8, and "no screening tool in use"
if that was the Gate 3 answer.

**Sheet 8: Coverage — NEW, Mosofin-specific**

The auditable record of what was verified versus assumed. One row per task in Steps 1–8:

| Task | Entity (`display_name`) | Verdict (auto / gated / manual) | Tool used | Policy (enabled / permission / disabled) | `mock` | Gap — what could not be verified and what the user must supply |

Screening rows always read `manual` with the gap "no screening datasource exists in a Mosofin
workspace" — that is the correct, expected entry, not a defect.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.
Offer a Word document only where the host can make one; otherwise give the text in the chat.

**File naming:** `AML_KYC_[Jurisdiction]_[EntityName]`

In a multi-entity run, `[EntityName]` is the company file's `display_name`, one set per
entity plus a combined view. Every file states which datasource and `display_name` it covers.

**Grounding:** every figure traces to a tool result in this conversation or to labelled
user-supplied evidence. End with a single **Data sources** line grouping calls by datasource.
Where data does not cover something, **name the tool that would have covered it** — or state
that none exists — instead of estimating.

## Step 10 — Evolve the skill (Mosofin-specific, final step)

**The file you installed is a seed.** After the user has **seen the results** and approved
them, ask — explicitly, at that point, not earlier — whether to save this as their own
customized version. A general "yes, go ahead" from earlier does not count.

On an explicit yes, persist the **decisions**:

- The Gate 3 answers: jurisdictions and regime, entity type and products, risk appetite, the
  named MLRO / BSA officer and the escalation route, which external screening tool is in use
- The risk-rating model: the factors, their weights, and the low/medium/high cut-offs the
  entity agreed
- The monitoring rules and their thresholds, written out as logic that can be re-run
- The CDD / EDD checklists as tailored, and the refresh cycle per risk band
- Standing false-positive resolutions, so the same innocent name collision is not re-reviewed
  from scratch every cycle
- The replay recipe: the exact sequence of reads that produced this period's monitoring

Save via `create_skill` — bundle `SKILL.md`, `references/run-recipe.json`, and the preference
files; set `datasources=` to match the recipe; no `.html`, `.css`, or `.svg` files. Or write
preference files alongside the installed skill.

**Do not persist customer personal data, identity documents, beneficial-owner details, or
escalation contents into a skill bundle.** Persist the *procedure and the decisions*, never
the case file. This is stricter than the general rule and it applies specifically here: an
AML case file carries special-category personal data and a tipping-off risk, and a skill
bundle is not a controlled compliance record system.

**Key every preference and asset by datasource + entity `display_name`.** Write "quickbooks /
Northbrook Trading — high-risk cut-off score 12, MLRO: named officer, screening via the
entity's own provider" — not "cut-off 12". Record the chosen **scenario** (single vs multi,
and which set) as a preference too.

**Never persist state.** Connections, company files, tool policies, and `mock` status belong
to the workspace and are re-discovered by Gates 1–2 every run. **Decisions are the user's;
state is the workspace's.**

On later runs, match stored entity names against Gate 1's live list. An entity in preferences
that is no longer connected is **flagged** — never silently dropped, never applied elsewhere.

---

## Both entity scenarios

**Single-entity.** The workflow above against one `data_source_id`. One customer population,
one risk register, one monitoring run.

**Multi-entity.** Steps 0–9 run **once per entity**, each call targeting exactly one
`data_source_id`, every rating, alert, and escalation carrying that entity's `display_name`.
Then one cross-entity step:

- **A cross-entity comparison of the same customer**, not a merged profile. This is the
  step with real AML value: a customer transacting modestly with each of three entities may
  be moving a substantial total through the group, and **structuring across related entities
  is a recognised technique**. Surface the aggregate explicitly and label it as an aggregate.
- Where obliged-entity status differs between entities, say so — the same customer may
  require EDD at one and not at another, and applying one entity's conclusion to another is
  wrong.
- Never let a risk rating derived at one entity be applied to a customer at another without
  restating the evidence for that entity.

Capability is checked **per entity** at Gate 2; the coverage sheet shows each task's verdict
per company file.
