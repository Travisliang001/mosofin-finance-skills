<!-- cost-accounting-process-costing · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Quality checks

- **Units tie-out (no unexplained gains / losses)** — **[manual]** to perform, since the units are
  supplied; but **insist on it**. An unexplained difference is spoilage, evaporation or a miscount, and
  each has a different accounting consequence. Distinguish **normal** loss (a cost of production,
  absorbed into good units) from **abnormal** loss (a period expense)
- **% completion assumptions documented** — **[manual]**, with the source and date recorded per the
  coverage sheet
- **Material addition points consistent** — **[manual]** across periods; **[auto]** to detect
  inconsistency in the *result*, since a changed addition point produces a step-change in material cost
  per unit with no change in prices
- **Costs classified correctly between DM and conversion** — **[gated]**: the accounts feeding each pool
  are readable, so the classification can be listed for review rather than assumed

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The model is reconciled to the ledger**, not only to itself — opening WIP, costs added, transfers and
  closing WIP each agreed to the accounts, with every difference reported and unforced
- **Equivalent units are never derived from money.** No unit count is inferred from a WIP balance or a
  standard cost
- **The method (weighted-average or FIFO) is stated on the output**, and a method change is flagged
  rather than presented as a movement
- **Cost per equivalent unit is shown with both its numerator and its denominator**
- **Every unit count and completion percentage names its source and the date of the count**
- Normal and abnormal loss are distinguished where a units difference arises
- The department sequence used is compared against the transfers actually posted
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool used, and that tool's
  policy, in the coverage sheet
- `mock` status is reported wherever it applies, and no unit cost feeding inventory valuation or pricing
  rests on mock data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No unit costs, WIP balances, unit counts or production volumes are persisted** into a skill bundle;
  every persisted preference states the datasource and `display_name` it covers
- Nothing was written back to any system — every entry is a proposal for a human to post
