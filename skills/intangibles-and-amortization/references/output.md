<!-- intangibles-and-amortization · output.md · read for: Stage 5 — before presenting results. Edit here, not in SKILL.md. -->

## Output Quality Standards

All of the original standards, plus the Mosofin ones.

- **Every intangible has class, useful life (finite or indefinite), and amortization basis**
- **Capitalization criteria documented for internally developed**
- **Roll-forward ties to GL**
- **Impairment tests dated and documented**
- **Useful life reassessments documented**
- **Multi-currency handled per policy**
- **Disclosure inputs captured**
- **File naming consistent**

**Mosofin additions:**

- The workspace was confirmed **by name** and the user said yes before any data was read
- Every in-scope company file is named by `display_name`; every excluded one is named **as excluded**
- The capability map was discovered **this run** via Gate 2 — never recalled from a previous conversation
  or from this file
- **The amortization presence check was run per account**, and any unamortized balance is classified as
  indefinite-lived — **with confirmation that its mandatory annual test is happening** — or as amortization
  that stopped
- **Capitalizations and disposals were derived from the ledger movements**, not only accepted as supplied
- **The tie-out runs in both directions**, with register-not-in-GL and GL-not-in-register as separate lists
- **The development cost profile is presented by month and by project**, with the `[manual]` stage dates
  alongside, and **the profile is compared to those dates** without adjudicating the stage
- **The capitalization scan ran both directions**, including a check for **marketing spend capitalized as
  brand** and for cloud implementation costs
- **The implied amortization rate was compared to the policy life** per class
- **Disposals were checked for the half-entry error**
- **Any goodwill among the intangible accounts is routed to the goodwill impairment test**, not
  amortized
- **The 5-year amortization forecast and the weighted average remaining life are produced** for disclosure
- Useful lives, the capitalization policy and the stage dates are **stated with their source**, and none was
  assumed
- In a multi-entity run, **amortization stays with the entity carrying the asset**, policy and framework
  differences across entities are flagged, and intra-group transfers are raised for
  `consolidation-and-eliminations`
- Every task carries its verdict (`[auto]` / `[gated]` / `[manual]`), the tool or external source used, and
  its as-at date, in the coverage sheet
- `mock` status is reported wherever it applies, and no capitalization or amortization figure rests on mock
  data
- Every figure traces to a tool result in this conversation or to labelled user-supplied evidence; the
  answer ends with a single **Data sources** line
- Every jargon term carries a plain-language gloss at first mention, with the professional term kept
  alongside
- No internal numeric ids and no raw `data_source_id` values appear in anything the user sees
- **No register, asset-level cost, net book value or impairment amount is persisted**, and **no content of
  the intangibles themselves** — customer list contents, patent specifications, trade secrets or source
  code references — **is ever stored**; every persisted preference states the datasource and `display_name`
  it covers
- Nothing was written back to any system — no asset capitalized, amortized, impaired or derecognised
