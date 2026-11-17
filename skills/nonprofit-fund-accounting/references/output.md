<!-- nonprofit-fund-accounting · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Net assets classified into without / with donor restrictions per current standards**
- **Conditional vs. unconditional and contribution vs. exchange distinctions applied rigorously**
- **Restrictions tracked and released correctly when satisfied**
- **Endowment corpus, earnings, spending, and underwater status handled**
- **In-kind contributions only recognized when criteria met; disclosure under ASU 2020-07**
- **Functional expense allocation by documented, consistent methodology** — no over-allocation to program
- **Liquidity, net asset composition, endowment, and contribution disclosures complete**
- **NFP-specific statement structure** — financial position, activities, functional expenses, cash flows —
  **followed**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **Both structural questions are answered in the header** — whether the chart separates net asset classes,
  and whether function is tracked as a dimension **and is genuinely function rather than programs**
- **Where the functional matrix cannot be built from a dimension, that is stated** rather than approximated
  from program classes
- **The proportion of expense directly identified versus allocated is reported**, and **the program
  percentage is trended against prior periods**
- **Qualifying spend with no corresponding release entry is identified**, with the amounts that should have
  released
- **The release line is verified to net to zero**, and **the net asset roll-forward ties to the balance
  sheet by class**
- **Board-designated amounts are recorded as `[manual]`** from board authority, never inferred from an
  account name
- **Every classification names the agreement clause relied on**, and **no conditionality is inferred from
  the ledger**
- **Underwater endowment status is marked `[manual]`**, with the valuation source named
- **The liquidity disclosure uses the computed available-resources figure**, with donor-restricted amounts
  excluded, rather than boilerplate
- In a multi-entity run, **restrictions are never released by transfer**, a trading subsidiary is not given
  net asset classes, net asset classes survive consolidation, and **the group program percentage is computed
  with intercompany eliminated**
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and **no published NFP statement rests on mock data**
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No individual donor name, gift amount, contact detail or giving history is ever persisted**, and no net
  asset balance, release amount or expense figure is stored; every persisted preference states the
  datasource and `display_name` it covers
- Nothing was written back to any system — no contribution, release or allocation posted
