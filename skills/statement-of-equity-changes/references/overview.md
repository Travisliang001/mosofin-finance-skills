<!-- statement-of-equity-changes · overview.md · read for: background — what the books supply for this work and what they cannot; read when a user asks why. Edit here, not in SKILL.md. -->

# Statement of Changes in Equity — Mosofin Seed

Builds the statement of changes in equity: a roll-forward of every equity component from opening to closing balance, showing all movements — net income, other comprehensive income, contributions, distributions and stock transactions.

**Framework-aware** (US GAAP / IFRS), and it **adapts to entity type** — corporation, partnership, LLC, sole proprietor, nonprofit.

This is a **seed skill**, written to be rewritten the first time it runs against a real workspace.

---

## Two things to understand before starting

### 1. The dollars are automatic. The shares are not.

The split in this skill is unusually clean:

| | Verdict |
|---|---|
| **Every equity account balance and every movement in it** | **`[auto]`, exact, at transaction level** |
| **Every share count — opening, issued, exercised, repurchased, by class** | **`[manual]`, entirely** |

**There is no cap table on this surface.** A general ledger records the *value* of an issuance; it does not record how many shares were issued, at what price, to whom, or of which class. This absence runs through the pack — the equity compensation accounting, `financial-statement-builder`, an IPO readiness review, `quarter-end-close`, a restatement review, the 10-Q and 10-K preparation — and here it removes **an entire step** (Step 4) and **one of the eight tie-outs.**

Say so on the sheet. A blank share roll-forward reads as unfinished work; it is a boundary.

### 2. Six of the eight tie-outs tie by construction

This matters more than it sounds, because it means the statement most likely to agree perfectly is the one that proves least.

**The statement of changes in equity is assembled from the same accounts it ties back to.** So:

| Tie-out | What it actually demonstrates |
|---|---|
| 1. Each component: opening + movements = closing | **Arithmetic.** It is the account's own activity, added up. |
| 2. Total closing equity = balance sheet equity section | **The same accounts, twice.** |
| 3. Net income = income statement net income | **Ties once the closing entries are posted** — it is the same posting. |
| 4. OCI = statement of comprehensive income | Same. |
| 5. Closing retained earnings = balance sheet RE | Same account. |
| 6. Closing AOCI = balance sheet AOCI | Same account. |
| **7. Closing share counts = shares disclosed** | **The only tie-out that reaches outside the ledger — and the only one Mosofin cannot perform.** |
| **8. Dividends declared = cash flow financing, adjusted for declared-but-unpaid** | **Genuinely has content** — see Step 5. |

**Six green ticks that were guaranteed before anyone looked.** This is the same trap as `financial-statement-builder`'s balancing balance sheet and segment reporting's reconciliation, and it is worth naming here because an equity statement with eight ticks looks thoroughly verified.

**What is worth doing instead** is the last quality standard — *no equity movement without a documented source* — which is a real test, is not guaranteed, and is `[auto]`. See Step 0.

### A near-substitute is not a substitute

**A component roll-forward is not a verification.** Opening plus movements equals closing is true of every account in every ledger, always, by double entry. It confirms the arithmetic and nothing about whether the movements belong there.

**And the equity section of the balance sheet is not independent evidence.** It is the same six or seven accounts, presented in a different order.

---

## Related skills

| Skill | Relationship |
|---|---|
| `closing-entries-and-trial-balance` | Closing entries, explicitly out of scope — and the mechanism behind tie-out 3. |
| `financial-statement-builder` | The full statement package, and the caution that a balancing balance sheet proves only arithmetic. |
| `consolidation-and-eliminations` | Non-controlling interest, and buy-outs as equity transactions. |
| `cash-flow-statement-indirect-method` | The financing section, and tie-out 8's three-way dividend reconciliation. |
| `foreign-currency-translation-asc830` | CTA within AOCI — and the warning that CTA absorbs translation errors silently. |
| `quarter-end-close` | The comparatives check and the equity roll-forward as recurring tasks. |
