<!-- subsequent-events-asc855 · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Subsequent Events (ASC 855 / IAS 10) — Mosofin Seed

Performs a structured subsequent events review: identifying events after the balance sheet date but before the financial statements are issued, or available to be issued, and determining recognition versus disclosure.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## The asymmetry at the centre of this skill

Three other skills in this pack run a subsequent-events sweep and defer here for the detail — `quarter-end-close`, `sec-10q-10k-prep` and the restructuring accounting. All three carry the same caution, and this is where it gets explained.

> **A ledger sweep is strong evidence for recognised (Type 1) events and structurally weak for non-recognised (Type 2) ones.**
>
> **That asymmetry is not a limitation of the connector. It follows from the definitions.**

Here is why.

**A recognised event provides evidence of a condition that existed at the balance sheet date.** The condition was already there; something afterwards revealed it. And the revealing thing is very often **a transaction** — a customer paying, a customer failing, stock selling below cost, a credit note being issued, a claim settling. **Those are exactly the things a general ledger records.**

**A non-recognised event arises from a condition that came into existence after the balance sheet date.** A fire. A lawsuit filed. A major customer lost. A financing signed. A regulatory action. An acquisition agreed. A director resigning.

**Almost none of those are transactions**, and several generate no accounting entry at all for months — a lawsuit filed produces no posting until it is provided for or settled. **A condition that arose after the period end has, by definition, generated no pre-period accounting, and frequently has generated no post-period accounting yet either.**

So the honest position, which must appear in every output:

| | Ledger sweep |
|---|---|
| **Type 1 — recognised** | **Genuinely strong.** Full population, exact, and the transactions found are the classic textbook cases. |
| **Type 2 — non-recognised** | **Structurally weak.** Found by asking people, reading board minutes, and legal enquiry. |

**A completed ledger sweep is not a completed subsequent events review**, and a log containing only ledger-derived events is a log that has done half the job. Record the source of every entry — see Step 5.

### And one practical gain worth more than it sounds

**The window keeps moving until the statements are issued.**

In practice, a subsequent events review is performed once — a few weeks before issuance, because it takes effort — and it is **stale by the time the accounts go out.** The last two or three weeks before issuance are typically covered by an enquiry of management and nothing more.

**A ledger sweep costs one query, so it can be re-run the day before issuance.** That closes the gap entirely for the transactional half, and it is a genuine process improvement rather than a faster version of the same thing. Run it at the start of the review, and **run it again immediately before issuance.**

### Two near-substitutes

**1. The posting date is not the event date.** An entry **posted** in January and **dated** December is a period-end transaction recorded late; it is not a subsequent event. An entry dated January for a January event is. And the reverse trap: an event occurring in January may not be posted until March, so a sweep run in February by posting date will miss it.

**Read by both dates and keep them distinct.** The transaction date locates the event; the posting date tells you when the business found out — which is itself informative.

**2. A post-period transaction is not automatically a subsequent event.** The overwhelming majority of transactions after the balance sheet date are ordinary business, and a review that lists them all has produced a general ledger extract, not a log. **The sweep is a filter, and Step 2b sets out what it filters for.**

---

## Related skills

| Skill | Relationship |
|---|---|
| `quarter-end-close` | Runs a subsequent events sweep as a quarterly task and defers here for the detail. |
| `year-end-close` | The same, annually, with the longest window. |
| `sec-10q-10k-prep` | Subsequent events as a filing disclosure, and the window running to the filing date. |
| `restatement-and-prior-period-adjustment` | The error-versus-estimate distinction with the same structure — and where an event discovered after issuance goes. |
| `bad-debt-and-write-offs` | The receivable allowance that post-period collections and failures bear on. |
| `inventory-obsolescence-and-reserve` | Net realisable value evidence from post-period sales. |
| `revenue-recognition-asc606` | Post-period credit notes against pre-period invoices. |
| `revenue-cutoff-testing` | Transactions dated before the period end and posted after — not subsequent events. |
| `statement-of-equity-changes` | Dividends declared after the balance sheet date. |
| `notes-to-financial-statements` | The destination for the disclosure draft. |
| `journal-entry-builder` | Formats the proposed adjusting entries. |
