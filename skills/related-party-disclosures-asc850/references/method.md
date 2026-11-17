<!-- related-party-disclosures-asc850 · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Inputs
- Workflow
- Step 1 — Define the related-party universe
- Step 2 — Completeness procedures
- Step 3 — Compile transactions and balances
- Step 4 — Prepare disclosures
- Step 5 — Controls
- Outputs
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. Mosofin drafts a disclosure; it does not disclose anything, and it does not decide that a party is related.

---

## Inputs

| Input | Format | Required | Mosofin source | Verdict |
|---|---|---|---|---|
| **Org chart and cap table** | Entities, owners, control relationships | **Required** | **Not in the books.** No cap table exists on this surface. **Partial exception**: the connected company files are themselves candidate entities under common control — see Gate 1. | `[manual]`, `[auto]` in part |
| **Key personnel list** | Officers, directors, significant shareholders | **Required** | **Not in the books.** There is no director field in a general ledger. | `[manual]` |
| **GL detail and intercompany** | Transactions and balances | **Required** | **Live read**, in full, across every connected file | `[auto]` |
| Contracts | Management fees, leases, services, loans | Recommended | The *payments* are readable; **the agreements are not.** Terms, and whether they are arm's length, live in the contract. | `[auto]` in part |
| Prior disclosures | Prior year footnotes | Recommended | Not in the books; **but the prior year's transactions with the same parties are** — a useful cross-check on last year's note | `[manual]`, `[auto]` in part |

---

## Workflow

### Step 1 — Define the related-party universe

`[manual]` in substance. All four categories preserved.

| Category | Mosofin contribution | Verdict |
|---|---|---|
| **Entities under common control** | **Partly automatic**: the other connected company files are candidates by construction. Everything not connected is invisible. | `[auto]` in part, `[manual]` to complete |
| **Significant shareholders and their entities** | **Nothing.** No cap table on this surface. | `[manual]` |
| **Key management personnel and close family** (per framework) | **Nothing.** And note the frameworks differ on how wide "close family" reaches — establish which applies. | `[manual]` |
| **Board members and their entities** | **Nothing.** A board is a legal fact recorded in statutory registers, not an accounting one. | `[manual]` |

**Three of the four categories are entirely off this surface**, and the fourth is only partly on it. That is the honest position and it should be stated in the output rather than left for a reader to infer from an empty column.

**What the workspace does contribute here is a starting list rather than an answer** `[auto]`:

- the connected entities themselves
- any account named for an individual — **a director's loan account, an officer's current account, a shareholder loan.** These are named accounts in the chart and finding them is one read. **An account called "Loan — J Okonkwo" is a related-party balance announcing itself**, and it is remarkable how often such an account exists while the disclosure note does not mention it.
- **round-sum recurring charges from a single entity with no other trading relationship** — the classic management-company signature, named in this skill's own description.

Present these as **candidates for the universe**, feeding the interview. They are not the universe.

---

### Step 2 — Completeness procedures

**The step where a connected workspace changes the work.** All four preserved, and the verdicts split cleanly two and two.

| Procedure | Verdict | What actually happens |
|---|---|---|
| **Management representation of related parties** | `[manual]` | A person states, in writing, who the related parties are. Not a query, and not replaceable by one. |
| **Compare vendor/customer masters to the related-party list** | **`[auto]`** | **Full population, both masters, every name.** See below. |
| **Scan the GL for keywords and known names** | **`[auto]`** | **Full population, every transaction, every memo and description field the surface exposes.** Not a scan — a complete read. |
| **Review legal contracts and board minutes** | `[manual]` | Neither is on this surface. Board minutes in particular are where undisclosed relationships are most often first recorded. |

#### What the two automatic procedures actually deliver

`[auto]`, and it is worth being precise about the gain, because it is real but bounded.

The original says "compare" and "scan," which in manual practice means: take the list of names, look through the vendor master for the obvious ones, grep the ledger for a few keywords, and stop when it feels sufficient. A connected ledger removes the "feels sufficient" part:

- **Every** vendor record is matched, not the ones someone remembers to check
- **Every** customer record likewise
- **Every** transaction description and memo, across the full period, in one pass
- **Every** connected company file, in the same run
- and the match can be **fuzzy** — surname alone, initials, common abbreviations, a company name with and without its suffix — which a human scan is bad at and a machine is good at

That is a genuine and material improvement in the strength of two of the four procedures.

**And it remains bounded exactly as the near-substitute section says.** It finds transactions with the names you supplied. Where the input list is incomplete, the output is confidently incomplete, and it does not look incomplete.

#### Three additional `[auto]` detections the original does not name

These do not depend on the input list, which is what makes them worth having — they can surface a party nobody named.

**1. The same name in both the vendor and the customer master.** An entity that both buys from the client and sells to it is not necessarily related — there are perfectly ordinary reasons — but it is a cheap, high-yield flag, and it is the shape of an undisclosed management company or a founder's other business almost every time it is not innocent. One read of two lists.

**2. A vendor or customer whose name matches a connected company file's `display_name`**, or nearly does. This finds intercompany trading that has been recorded as ordinary third-party trading, which is both an elimination problem and a disclosure problem. See `consolidation-and-eliminations`.

**3. Accounts named for people.** As in Step 1: director's loan accounts, officer current accounts, shareholder loans. Read the chart, not the transactions. **This is the single cheapest related-party detection available and it requires no input list at all.**

Each of these produces **candidates for enquiry**, and each must be presented that way. A vendor appearing in both masters is a question to ask, not a relationship to assert.

---

### Step 3 — Compile transactions and balances

`[auto]` for four of the five fields. All five preserved.

| Field | Mosofin source | Verdict |
|---|---|---|
| **Nature of the relationship** | Not in the books | `[manual]` |
| **Description of the transaction** | Readable — account, memo, document reference | `[auto]` |
| **Amounts recognised** | Readable, exactly, by party and by period | `[auto]` |
| **Outstanding balances and terms** | **Balances readable; terms are not.** | `[auto]` / `[manual]` |
| **Whether the terms are arm's length** | **Partly testable** — see below | `[manual]` to conclude, `[auto]` in part to evidence |

**On balances and terms.** The balance owed to or from a related party is a live read and is exact. The **terms** — interest rate, repayment date, security, whether it is repayable on demand — are in the loan agreement, and frequently there is no agreement at all, which is itself the disclosure. `[auto]` for one closely related fact that matters in several jurisdictions: **whether any interest has actually been charged on the balance.** A material director's loan carrying no interest is a disclosure item and often a tax item too.

#### On arm's length, which is the interesting field

`[manual]` to conclude. But `[auto]` to *evidence*, and the evidence is better than it first appears.

Arm's length means: on the terms that would apply between unrelated parties. In many cases **the client transacts the same thing with unrelated parties**, and those transactions are in the same ledger. So:

- **The same product or service sold to a related party and to third parties** — compare price, discount and payment terms. `[auto]`, and it is a real benchmark, not a proxy.
- **A related-party lease against the client's other leases**, or against market rents where other properties are in the books.
- **A management fee with no comparable at all** — which is itself informative. A charge with no benchmark available is the case where an external opinion is needed most.
- **Payment behaviour**: a related party that pays at 180 days while third parties pay at 30 is not on third-party terms, whatever the invoice says. Terms as written and terms as operated are different things, and the ledger knows the second one. See the receivables ageing for the days-to-pay derivation.

**Where no comparable exists, say so** rather than reaching for a weaker one. And where the amount is material, this is the transfer pricing documentation territory and, across borders, a tax-authority matter rather than only a disclosure one.

---

### Step 4 — Prepare disclosures

`[auto]` to assemble the figures. **`[manual]` to draft and to approve** — the note is a statement in a set of financial statements and it carries legal weight.

All four common elements preserved:

| Element | Verdict |
|---|---|
| **Relationship description** | `[manual]` — it describes people and structures, not transactions |
| **Transactions during the period** | `[auto]` — amounts by party and by type, exact |
| **Balances at period end** | `[auto]` |
| **Commitments and contingencies with related parties** | **`[manual]`** — a commitment is a contract not yet transacted, and the ledger records transactions. A guarantee given for a related party's borrowing is the classic case and it appears nowhere in the accounts until it is called. |

Feed into `notes-to-financial-statements`.

**The commitments line deserves emphasis** because it is the item most often missed and it is the one a live ledger is *least* able to help with. A parent guaranteeing a subsidiary's bank facility, a director personally guaranteeing the company's lease, a commitment to fund a related entity — none of these are transactions. They are promises, and they are disclosable. Ask.

---

### Step 5 — Controls

Both preserved.

- **Quarterly refresh of the related-party list.** `[manual]` to refresh the *list*; **`[auto]` to re-run the match against it.** This is the natural rhythm: the client updates the names when something changes, and the completeness match re-runs every quarter at the cost of one query. See `quarter-end-close`, where this belongs as a quarterly task.
- **Review and sign-off by legal or the CFO.** `[manual]`. A person takes responsibility.

**Why the refresh matters more than it sounds.** A related-party list goes stale in a specific and dangerous way: **people leave.** A director who resigned in March is a related party for the part of the year they served, and transactions with them in that window are disclosable — but they will have dropped off the current list by the time the disclosure is prepared. **Ask for joiners and leavers with dates, not just a current list**, and match transactions against the period each person was actually related.

`[auto]` supporting the refresh: **a diff.** Compare this quarter's vendor and customer masters against the previous run's, and report the new counterparties. A new related party usually arrives as a new supplier, so the list of names that did not exist last quarter is a short and well-targeted place to look.

---

## Outputs

All four of the original's outputs preserved, plus two Mosofin additions. Delivered as an `.xlsx` workpaper.

**Sheet 1: Related-Party Register**
| Party | Type (entity / individual) | Relationship | Period related from / to | Source | Verdict |

**`[manual]`** for the relationships. **Add the "period related from / to" columns** — they are what makes a leaver's transactions get disclosed correctly. **Add a Source column**: `client-supplied`, `connected entity`, or `ledger candidate — unconfirmed`.

**Sheet 2: Completeness Evidence**
Each of the four procedures, what was done, by whom, over what population.

At the head of this sheet, in bold: **which procedures were run over the full population and which were not**, and the statement that **a name match cannot establish completeness.** That sentence belongs on the sheet, not only in this file — the sheet is what gets filed and reviewed.

**Sheet 3: Transactions and Balances**
| Party | Transaction type | Description | Amount | Period | Closing balance | Terms | Arm's length? | Evidence |

`[auto]` for amounts, descriptions and balances. `[manual]` for terms and the arm's-length conclusion, with the `[auto]` comparables in the Evidence column where they exist.

**Sheet 4: Disclosure Tables**
Disclosure-ready, formatted for the note. Marked **DRAFT — FOR REVIEW**.

**Sheet 5: Management Representation Draft**
`[manual]` to sign. Mosofin drafts the wording; a person makes the representation, and the representation is the point.

**Sheet 6: Ledger Candidates** *(Mosofin addition)*
Everything the books surfaced without being asked:

| Candidate | How surfaced | Evidence | Amount | Status (confirmed / not related / open) |
|---|---|---|---|---|

Names in both masters. Vendors matching a connected entity. Accounts named for individuals. Round-sum recurring management charges. New counterparties since the last refresh.

**Every row starts "open."** Nothing on this sheet is a finding until a person confirms it, and the sheet is a list of questions rather than a list of related parties.

**Sheet 7: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet.

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `RelatedParty_[YYYY]_[EntityName].xlsx`

Entity `display_name` in the file name and on every sheet. If any read returned `mock: true`, say so in the file name and at the head of Sheet 2, where the negative finding lives.

---

## Output Quality Standards

*(A Mosofin addition — the original has no Output Quality Standards section.)*

- **The related-party universe is client-supplied and documented as such.** Mosofin proposes candidates; it does not determine relationships.
- **All four completeness procedures appear in the evidence**, including the two Mosofin cannot perform. **A procedure not performed is listed with its owner, never omitted.**
- **The population covered by each procedure is stated** — full population, or not.
- **The limits of the name match are stated on the completeness sheet**, not only in this file.
- **Every party carries the period over which it was related**, so part-year relationships are handled correctly.
- **Transactions and balances are exact and traceable** to the underlying records.
- **Arm's-length conclusions carry their evidence**, or state that no comparable was available.
- **Nil-value and off-balance-sheet items are actively asked for**, since they cannot be read.
- **Ledger candidates are questions, not findings.** Nothing is asserted as a relationship without confirmation.
- **The disclosure is a draft** until a person reviews and signs it.
- **Only what the disclosure requires is compiled** about any individual.
- **File naming consistent.**

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — and, obviously, **any client's related-party list.** That list is the most sensitive artefact this skill touches and it must never travel with the seed to another engagement.

**What is worth persisting into the workspace-scoped skill:**

1. **The related-party register**, with periods and sources. Expensive to build, stable between quarters, and the entire basis of the recurring match.
2. **Name variants** — married names, trading names, abbreviations — which is what makes the fuzzy match actually work on the second run.
3. **Candidates confirmed as *not* related, with the reasoning.** Without this, Sheet 6 re-raises the same eight names every quarter and the client stops reading it.
4. **Which accounts are related-party accounts** — the director's loan account, the intercompany accounts — so they are read directly rather than rediscovered.
5. **Arm's-length comparables already identified**, and the conclusions reached.
6. **The framework**, and any client-specific interpretation agreed with the auditor.
7. **The last refresh date and the counterparty snapshot**, so the next run's diff has a baseline.

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and here that is not a tidiness rule but a confidentiality one.

**The evolved version asks "what has changed?" rather than "who are your related parties?"** — and answers, itself, with the counterparty diff.

---

## Anti-patterns

- **Reporting a clean match as completeness.** It means nothing matched the names you were given.
- **Treating the connected company files as the whole universe.** They are a floor. The founder's other business is not connected.
- **Asserting a relationship from a name collision.** Sheet 6 holds questions.
- **Using the current director list for a full-year disclosure.** People resign, and their transactions while serving are still disclosable.
- **Filtering by materiality without saying so.** The fact of a relationship can matter regardless of size.
- **Forgetting nil-value transactions.** Free premises and unpaid services leave no trace at all — ask.
- **Forgetting guarantees.** Off-balance-sheet, disclosable, invisible.
- **Blending ASC 850 and IAS 24.** They differ on scope; pick one.
- **Presenting a written interest rate as evidence of arm's length** when the payment behaviour says otherwise. Terms as operated beat terms as drafted.
- **Compiling more about an individual than the disclosure requires.**
- **Carrying names between workspaces.**
- **Re-raising a candidate the client already explained.** Persist the "not related" conclusions.
- **Saying "disclosed".** Mosofin drafts; the financial statements disclose.
