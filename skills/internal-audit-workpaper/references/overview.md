<!-- internal-audit-workpaper · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Internal Audit Workpaper (Mosofin)

Plans and documents an internal audit — **scoping**, building the **audit program**, executing **fieldwork
with proper workpapers**, developing **findings with risk ratings and recommendations**, and structuring
the **report**. Supports **operational, financial, and compliance** internal audits.

**In plain words:** internal audit is the organisation checking itself. Someone independent looks at how a
process actually runs, compares it to how it is supposed to run, works out why the gap exists, and gets
agreement on fixing it — then comes back later to see whether it was fixed.

This skill is **standards-aware** — it aligns with the **IIA's International Professional Practices
Framework** in structure — and **process-agnostic**.

It is **workspace-scoped**: transaction populations, balances and the analytical evidence come from tool
calls against a company file connected to your Mosofin workspace in this conversation, or from something
you supplied by hand and that is labelled as such.

## What the workspace changes: two and a half procedure types, and the end of sampling

**Step 3 names six procedure types. The workspace covers about two and a half of them, and the split is
worth stating before any program is written:**

| Procedure | What it means | Verdict |
|---|---|---|
| **Analyze** | Examine data for patterns, trends, exceptions | **[auto]** — the strongest fit; populations, trends and outliers are all readable |
| **Re-perform** | Redo the calculation or process step yourself | **[gated]** — anything computed *from ledger data* can be re-performed; anything computed outside it cannot |
| **Inspect** | Examine a document or record | **[gated]** — records held in the system are readable; **paper, contracts, signed approvals and images are not** |
| **Observe** | Watch the process being performed | **[manual]** — a physical act |
| **Inquire** | Ask the people who do the work | **[manual]** — and the least reliable evidence on its own |
| **Confirm** | Get independent verification from a third party | **[manual]** — **there is no confirmation capability on this surface** |

**Write this mapping into the audit program itself.** A program whose procedures are all "analyze" is
narrow; one that pretends "observe" and "confirm" are covered is wrong. **The value here is knowing which
half of the fieldwork a person still has to do.**

### Sampling — and why you may not need it

**This is the most consequential thing the workspace changes about audit method.**

Sampling exists because testing every item was impractical. **When the population is readable, it often is
practical.**

> **Where the whole population can be read, test the whole population.** **Sampling risk falls to zero**,
> the conclusion is stronger, and the exception rate is a fact rather than an estimate. "All 4,812
> transactions were tested; 7 exceptions were found" is a better sentence than any sample can produce.

Where a full test is not possible — the field is not exposed, the volume is impractical, the evidence is
outside the system — **sample properly**: define the population, state the method, state the size and the
basis. **And say which you did.**

**But hold the counterweight firmly, because it is the limit of everything above:**

> **A full-population test of the ledger is not a full-population test of the process.** The ledger records
> what was *recorded*. **A transaction that should have existed and does not is invisible to every query you
> can run.** **Completeness is the assertion the ledger cannot test on its own** — it needs an external
> reference point: a bank statement, a third-party confirmation, a physical count, an independent record.
> **Say so explicitly wherever completeness is in scope**, and route it to the `[manual]` fieldwork.

### The workpaper standard fits unusually well

Step 4 asks that **a reviewer be able to re-perform from the workpaper and reach the same conclusion.**

**A Mosofin procedure satisfies that standard better than most manual ones**, provided you document it
properly: **record the exact tool called, the parameters passed, the entity, and the as-at date.** Anyone
with the same access can re-run it and get the same answer. **That is re-performability in the strict
sense**, and it should be the documented form of every `[auto]` procedure.

**One caveat**: **a tool result is evidence in a workpaper; it is not a preserved record.** If a matter
becomes an investigation, see `fraud-detection-and-forensics` — chain of custody is a separate discipline.

**Independence note**: **Mosofin is read-only and did not operate the process.** It cannot have made the
entries it is testing, which supports objectivity — but **it also cannot be the auditor.** The judgments,
the findings and the conclusions are the auditor's.
