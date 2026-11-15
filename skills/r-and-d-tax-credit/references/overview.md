<!-- r-and-d-tax-credit · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# R&D Tax Credit — Mosofin Seed

Identifies qualifying research and development activity, computes qualifying expenditure and the resulting credit or relief, and builds the documentation a claim needs. R&D incentives exist in many jurisdictions, each with its own name, rules and mechanics. They are valuable and they are scrutinised, so qualification and documentation have to be robust.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The source already got the most important thing right

Most skills in this pack had to be told not to freeze things. This one already knew.

The original states, in its own opening: **it does not hardcode credit rates, qualifying-cost rules, or definitions**, because they vary significantly by jurisdiction and they change. Its last edge case says it again — *"R&D regimes are frequently reformed… Always confirm current rules — never hardcode."* Its quality standards say it a third time.

That is exactly the discipline a seed skill needs, correctly identified and correctly applied to the domain. The conversion below does not introduce it. It **extends the same instinct one layer outward**:

> The original understood that **tax rules** change and must be read fresh each time.
> A Mosofin seed must understand that **capabilities** change and must be read fresh each time too.

Same failure mode, different subject. A rate baked into a document is wrong the year it changes and gives no sign of it. A capability map baked into a document is wrong the day a policy changes and gives no sign of it either. Gate 2 is the capability version of "confirm current rules — never hardcode," and the author of this file would have recognised the argument immediately.

---

## What this skill can and cannot see

Be blunt about this at the outset, because R&D claims are an area where an eager tool can do real damage.

**An R&D claim has two halves.** They are not equally visible to an accounting system, and they are not equally important.

**The technical half — which is the half that decides the claim.** Was a scientific or technological advance sought? Was there genuine uncertainty that a competent professional could not readily resolve? Was there a systematic process of investigation?

**None of this is in the ledger. Not a trace.** The uncertainty lived in engineers' heads. The evidence of it lives in design documents, test results, failed branches in version control, and meeting notes. A general ledger records what a project *cost*. It has no idea what the project *was*, whether anybody was uncertain about anything, or whether the work advanced the state of the art or reimplemented something bought off a shelf in 2019.

**The cost half — which is the half that sizes the claim.** What was spent, on what, by whom, when. Substantial parts of this *are* readable, and that is where the workspace earns its place.

So the division of labour is unusually clean, and unusually lopsided in importance: **the workspace can help build a complete and accurate cost population. It cannot contribute one sentence to the question of whether the work qualifies.** A tool that blurs that line produces a large, well-formatted, confidently wrong claim — and R&D claims carry penalty exposure, which makes confidently wrong the expensive kind.

### The hazard that comes with being fast

There is a specific danger in connecting this particular skill to live data, and it deserves naming before the workflow rather than after.

The original says, correctly: **contemporaneous documentation is far stronger than reconstructed.** Tax authorities know the difference and ask about it.

A live ledger makes reconstruction *effortless*. A cost analysis by project, by category, by month, formatted and totalled, can be produced two years after the fact in about ninety seconds — and it will look exactly as polished as one maintained throughout. **Polish is not provenance.** A schedule assembled in 2026 from 2024's ledger is a reconstruction, however good it looks, and presenting it with the visual authority of contemporaneous records overstates what it is.

So: **every cost schedule this skill produces is stamped with when it was assembled and from what.** Where records were maintained at the time, say so. Where they were rebuilt from the ledger afterwards, say that instead. The claim is stronger for the honesty and materially weaker without it, because the one thing worse than thin documentation is documentation that implies a rigour it did not have.

This is the same shape as the caution in `fraud-detection-and-forensics`: the ease of querying makes the discipline around the query *more* important, not less.

---

## Related skills

| Skill | Relationship |
|---|---|
| `tax-return-prep-corporate` | The parent return this claim feeds. Step 5's interaction lands there. |
| `corporate-tax-provision-asc740` | The accounting consequence of a credit recognised in the accounts. |
| `grant-accounting-nonprofit-restricted-funds` | The accounting for the grants that Step 4 sweeps for, and which can disqualify a project. |
| `intangibles-and-amortization` | Capitalised development costs — a population an expenditure claim must consider and which is not in the P&L. |
| `intercompany-reconciliation` | Reading both sides of a group R&D recharge where both entities are connected. |
| `job-costing-and-wip` | Where project-dimension cost tracking is set up properly in the first place. |
| `payroll-journal-entry-builder` / `payroll-reconciliation` | Why the payroll pool may or may not be readable by employee. |
| `tax-planning-and-projections` | Where the cash benefit of a payable credit belongs in the forecast. |
| `fraud-detection-and-forensics` | The same caution about ease of querying raising, not lowering, the standard of discipline. |
