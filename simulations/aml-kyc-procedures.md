# AML / KYC working paper — for the responsible officer only

**Restricted: for P. Whitcombe (MLRO) only. Not for any customer, and nothing here is a reason to contact one.**

This run is manual: no Mosofin connection is present. Everything below comes from the file you uploaded. It is support for a compliance function, not legal or compliance advice. I have screened no one, decided nothing about suspicion, drafted no filing and changed nothing in any system.

## (a) Read-back

Documenting the AML programme for **Northbrook Payments**, regulated under **"Sampleland AML Regulations 2020"** as you stated it, offering **payment services**, with customer activity from **the file you uploaded** for **Q3 2025 (July to September)**. Responsible officer: **P. Whitcombe, compliance lead (MLRO)**. Screening on **the company's own subscription service** (not named). Output to **the officer only**.

Two points where the file and your intake answers differ. I need you to confirm both:
- **Entity.** You gave the company as **Northbrook Trading Ltd**. The file is for **Northbrook Payments**, which it calls a separate entity. The regime, products, officer and customers below belong to Northbrook Payments, and I label everything that way. Nothing here describes Northbrook Trading Ltd.
- **Period.** You gave September 2025 (as at 30 September 2025). The activity is quoted for Q3 as a whole and cannot be split by month.

Intake questions the file does not answer, and the default applied:
- **Existing AML policy: none written.** Default: I give a framework outline only, not a finished procedure document.
- **Screening tool name and lists covered:** not stated. Screening is recorded as supplied, and as not evidenced where no result was given.
- **Jurisdiction, thresholds, timeframes, retention period under the regime:** not stated. None is assumed.

What I received:
- `aml_customer_and_activity.md` — entity, regime, officer, screening tool, policy status, and a table of 3 customers with risk attributes, screening status and Q3 activity.
- `aml_customer_and_activity_final.csv` — 3 rows, columns employee / week_1..week_4, values nights / days / off.

## (b) Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `aml_customer_and_activity.md` | A combined intake note, customer list with risk attributes, screening status and activity summary | **Entity differs from intake** (Northbrook Payments, not Northbrook Trading Ltd). Period Q3 2025, wider than September. No currency stated | Readable. 3 customers. Activity is a one-line summary per customer, not a transaction listing: no dates, directions, counterparties or countries | Steps 1–7 | **Accepted with a limit**, subject to your confirming the entity. Monitoring can only restate the summaries; no pattern test can be run on the underlying payments. Screening results are as reported, with no report from the tool |
| `aml_customer_and_activity_final.csv` | A four-week staff shift roster (E08–E10) | No entity, period, customer or amount | Not for this skill | No step uses it | **Rejected**. The name suggests a final customer and activity file; the content is a rota. Set aside. If a final activity export exists, please upload it |

**Still missing:** the transaction listing for the period (required for monitoring); screening output from your tool for each customer (required to record screening); identity and ownership evidence for each customer; a written AML policy (none exists). I would stop here and wait for your answer, in particular on the entity.

*You replied: go ahead with the accepted file.* I proceed for Northbrook Payments.

## (c) Findings

**Step 1 — context.** Regime as you stated: Sampleland AML Regulations 2020. A payment services business is the kind of firm such regimes normally cover; whether Northbrook Payments is an obliged entity, and its exact duties, are for the officer and legal counsel to confirm. P. Whitcombe owns every determination and any filing.

**Step 2–4 — customer risk rating** (all inputs supplied by hand in the file; none measured from books)

| Customer | Type | Risk factors supplied | Indicative rating | Due diligence level |
|---|---|---|---|---|
| C-01 | Limited company | Domestic, retail | Lower | Standard |
| C-02 | Limited company | Held through an offshore holding; **beneficial owner not identified** | **High** | Enhanced, and see item 1 |
| C-03 | Individual | Politically exposed person (declared) | **High** | Enhanced, with senior management approval |

The rating scale is indicative; there is no written policy defining one.

**Step 5 — screening log** (results as supplied; this skill screens no one and does not say any name is clear)

| Customer | Tool | Date | Result supplied | Gap |
|---|---|---|---|---|
| C-01 | Company's subscription service | 2 Sep 2025 | Clear | Lists covered not stated; directors and owners not shown as screened |
| C-02 | — | — | **Not run** | Customer not screened. The owner cannot be screened because the owner is not identified |
| C-03 | Company's subscription service | 1 Aug 2025 | Match reviewed | Which list matched, the outcome of the review, and who reviewed it are not recorded |

**Step 6 — activity, Q3 2025** (summaries as supplied; currency not stated)

| Customer | Activity | Implied total | Observation |
|---|---|---:|---|
| C-01 | 42 payments, average 1,100 | 46,200 | Frequent, low value; in line with a domestic retail profile as described |
| C-02 | 9 payments of 9,900 each within 6 days | 89,100 | Identical amounts, each just under 10,000, clustered in 6 days (about 14,850 a day) |
| C-03 | 3 payments, average 4,000 | 12,000 | Low volume |

**Items referred to P. Whitcombe (MLRO)** — facts and patterns only; the decisions are the officer's.

1. **C-02: beneficial owner not identified.** The customer is held through an offshore holding and no natural person behind it has been identified or verified. Customer due diligence is incomplete. The skill's standard is that a relationship is not accepted where the owner cannot be identified; whether to continue, restrict or exit is for the officer and senior management.
2. **C-02: no screening on record.** Sanctions screening is a strict obligation. Neither the customer nor any owner has been screened, yet the customer transacted in Q3.
3. **C-02: repeated identical payments just below a round figure.** Nine payments of exactly 9,900 in six days, 89,100 in total. Repeated identical values close under a round amount in a short window is the pattern a structuring scenario looks for. I do not know the reporting threshold under the Sampleland regulations and do not assume one; if one sits at or near 10,000, that is relevant. Whether this is suspicious, and whether to report, is for P. Whitcombe to determine within the regime's timeframes. Needed for the review: the nine payment records (dates, counterparties, direction, source of funds). **No contact with the customer about this review.**
4. **C-03: politically exposed person.** This is a risk factor, not an accusation. It calls for enhanced due diligence: source of wealth and funds with corroboration, named senior management approval, and closer monitoring. None of these is evidenced in the file. The screening match reviewed on 1 August 2025 needs its outcome and reviewer recorded.
5. **No written AML policy.** For a payment services firm this is a gap in the first pillar of the programme. The other pillars (training, independent testing, enterprise-wide risk assessment) are not evidenced either. A designated officer exists.

**Framework outline (not a finished procedure; there is no policy to build on).** 1) Regime and obliged-entity status, confirmed by counsel. 2) Risk model: customer, geography, product, channel, transaction. 3) Standard due diligence: identify and verify the customer and its owners. 4) Enhanced due diligence triggers: high rating, politically exposed persons, opaque ownership. 5) Screening at onboarding and ongoing, on the firm's tool, with a false-positive review record. 6) Monitoring rules, including repeated-value and below-threshold patterns, thresholds confirmed by the officer. 7) Escalation to the MLRO, confidentiality, no tipping off. 8) Records and retention, period to be confirmed. 9) Training, independent testing, periodic risk assessment.

**Confirmations needed from the officer or counsel:** reporting thresholds and report type; beneficial ownership threshold; reporting timeframe; retention period; whether politically exposed status extends to family and associates under this regime.

## (d) What was not done, and why

- **Screening** — never performed by this skill. Results above are as supplied; C-02 has none.
- **Any decision on suspicion, any report or filing draft** — the officer's regulated decision.
- **Transaction-level monitoring** — only one-line summaries were supplied; no dates, counterparties, directions or countries, so size, frequency, geography and pass-through tests could not be run. Unrecorded cash is outside any file.
- **Identity, ownership, source of funds verification** — no documents supplied; nothing above is verified identity.
- **Entity confirmation** — the file is for Northbrook Payments; intake said Northbrook Trading Ltd. Unresolved.
- **September-only view** — activity is Q3 in total.
- **Full procedure document** — outline only, because no policy exists.
- **Customer population completeness** — three customers were supplied; I cannot say that is all of them.
- **Excel workpaper** (`AML_KYC_Sampleland_Northbrook Payments`) — not created; say if you want it.
- **Saving** — no identity, ownership or screening data is saved.
- **Nothing was written, sent, posted or filed.**

**Data sources:** user-uploaded `aml_customer_and_activity.md` only. No ledger read; no screening source.
