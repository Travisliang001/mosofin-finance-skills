# Related party disclosures (ASC 850) — Northbrook Trading Ltd, period to 30 September 2025

Mosofin is not connected, so this run is manual: every step is `[manual]`, from your uploads. (Connecting Mosofin would run the name match across every master and transaction — docs.mosofin.com.) **DRAFT — FOR REVIEW. Nothing has been posted or disclosed; no relationship is asserted beyond those you listed.**

## 1. Read-back

Preparing related party disclosures for **Northbrook Trading Ltd** (user-asserted), **USD**, period to **30 September 2025**, against the **four parties you listed**. Found in `related_parties.md`, to confirm here: framework **ASC 850**; output **for the CFO only**; **J. Marsh joined the board in June 2025**.

| Intake | Treatment |
|---|---|
| B — period | Intake says September 2025 / as at 30 Sep; your uploads cover Oct 2024–Sep 2025 (bills) and Jul–Sep 2025 (intercompany). **Please confirm the reporting period** (year to 31 Dec 2025?) — figures below are shown by the period each file covers |
| D — changes | Marsh joining in June given; **no leavers stated — assumed none, and I say so** |
| E — guarantees, nil-value transactions | Not answered → **listed as not confirmed**; please tell me (e.g. a personal guarantee by A. Reyes, free use of premises) |
| F — audience | CFO only. I compile only what the standard requires about individuals |

## 2. Validation of the upload — shown before any work

| File | What it actually is | Company / period | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `related_parties.md` | Related-party list: 80% subsidiary, CEO/director and his company, a new director, a 20% shareholder; framework; audience | No dates for when Reyes or Investor A became related; Investor A unnamed | Yes, as a client-supplied list | Yes — Step 1 universe | **Accepted with a limit**: user-supplied; "Investor A" cannot be name-matched |
| `vendor_master.csv` | Vendor master: 12 vendors, terms, tax form, entity type, bank-change date, paid_2025 | No company; "paid_2025" | Yes | Yes — Step 2 master-to-list comparison | **Accepted with a limit: company user-asserted.** No customer master or employee list, so those comparisons cannot run |
| `bill_payment_history_12m.csv` | 92 vendor bills for 8 vendors, Oct 2024 – Sep 2025, with due and paid dates | Oct 2024–Sep 2025 (not a calendar year) | Yes; 4 vendors in the master have no bills | Yes — Step 3 transactions; arm's-length payment behaviour | **Accepted with a limit**: vendor side only; 12-month window |
| `intercompany_ledger_northbrook_trading.csv` | Intercompany entries with Northbrook UK: 3 items, Jul–Sep 2025, total (38,000) | Q3 2025 only; no balance; sign convention not stated | Partly | Yes — Step 3 for the subsidiary | **Accepted with a limit**: Q3 only, no closing balance |
| `related_parties_final.csv` | **Not a related-party list.** A staff shift rota: E08–E10, week_1…week_4, "nights / days / off" | No company, parties or amounts | No | No step uses it | **Rejected** on content despite its name. Not used |

**Still missing (required):** **period-end receivable and payable balances by party** (including the intercompany balance); **customer transaction detail** and customer master; GL detail or chart (to find accounts named for individuals, e.g. director's loan accounts); employee list. Recommended: prior-year disclosure; the Halden lease; a full-period intercompany ledger.

*I would stop here and wait for your answer. Assumed answer: "go ahead with the accepted files".*

## 3. Findings

### Completeness evidence (Step 2) — **a name match cannot establish completeness**

| Procedure | Done? | Population | Result |
|---|---|---|---|
| Management representation | **No — yours to give** | — | Draft wording available |
| Vendor master vs list | Yes | All 12 vendors | **Halden Property Management matches** (A. Reyes's company). No vendor matches Marsh, Reyes personally or Northbrook UK. Investor A cannot be matched (unnamed) |
| Customer master vs list | **Not done** | — | No customer data uploaded |
| GL keyword / named-account scan | **Not done** | — | No GL uploaded |
| Contracts and board minutes | **No — yours** | — | — |

### Transactions and balances (Step 3)

| Party | Relationship (as you told me) | Transactions | Amount | Closing balance | Terms / evidence |
|---|---|---|---|---:|---|
| **Halden Property Management** | Owned by A. Reyes, CEO and director; landlord of the warehouse | Rent, 12 bills of **6,750** monthly, Oct 2024–Sep 2025 | **81,000** (12 months); **60,750** billed and paid Jan–Sep 2025 | Not supplied (Sep bill paid 6 Sep) | Terms **0 days**; every bill **paid 1 day** after billing, vs **15–30 days** for every third-party vendor. Arm's length **not concluded**; no comparable lease uploaded |
| **Northbrook UK Ltd** | 80% subsidiary | IC-071 management fee 12,000 (10 Jul); goods shipped by UK 18,500 (12 Aug) and 7,500 (18 Sep) | **38,000** in Jul–Sep 2025 (goods 26,000; fee 12,000) | **Not supplied** | Direction of the management fee unclear ("from UK", sign negative) — confirm who charged whom. Eliminated on consolidation; disclosable in Northbrook's standalone statements if presented |
| A. Reyes | CEO and director | None found with him personally in the vendor data | — | — | Compensation and any loans not in the uploads |
| J. Marsh | Director **from June 2025** (part-year) | None found | — | — | Related only from June: match transactions from that date |
| Investor A | 20% shareholder | Cannot be tested | — | — | Name needed |

Note: the vendor master's `paid_2025` for Halden (81,000) equals the 12-month Oct 2024–Sep 2025 total, not calendar 2025 (60,750); the same holds for the other monthly vendors. Treat that column as 12-month, not year-to-date.

### Ledger candidates — questions, not findings (all **open**)

| Candidate | How surfaced | Status |
|---|---|---|
| M. Okafor Consulting | Vendor named for an individual, sole proprietor, no tax form; 16,962 billed in 11 months | Open — is Okafor connected to any director or shareholder? |
| Kestrel Supplies / Kestrel Supplies Inc. | Two vendor records, near-identical names | Open — likely a duplicate vendor, not a related party; raise with AP |

### Draft disclosure (DRAFT — FOR REVIEW, figures pending the period and balances)

> *The Company leases its warehouse from Halden Property Management, an entity owned by the Company's Chief Executive Officer and director. Rent of $[60,750 / full-year] was incurred in [period]; amounts payable at [date] were $[—]. The Company has an 80% owned subsidiary, Northbrook UK Ltd, from which it purchased goods of $[26,000 Q3] and [paid / received] management fees of $[12,000 Q3]; balances at [date] were $[—]. [Guarantees: none / to be confirmed.]*

## 4. What was not done, and why

| Item | Status | Needed |
|---|---|---|
| Period-end balances; intercompany balance | **Not done** | Balances by party at period end |
| Customer-side and GL named-account procedures | **Not done** | Customer master and transactions; GL / chart |
| Arm's-length conclusion on Halden rent | Evidence only (payment terms) | Lease; market or other-lease comparable |
| Guarantees, nil-value transactions, commitments | Not confirmed | Your answer |
| Investor A; Reyes compensation and loans | Not tested | Name; payroll / loan records |
| Management representation, sign-off, disclosure | **Not done — read-only; a person signs** | — |

## 5. Coverage and provenance (manual run)

- **A — Environment:** Northbrook Trading Ltd, USD, ASC 850, period to 30 Sep 2025 (to confirm) — user-asserted; source **upload**. Files: list, vendor master, bill history, intercompany ledger *accepted with a limit*; `related_parties_final.csv` *rejected (shift rota)*.
- **B — Capability map:** not applicable — no connection; every task is `[manual]`.
- **C — Steps:** Step 1 universe — **entirely client-supplied**; Step 2 — one of four procedures run (vendor master), on names only; Step 3 — vendor and Q3 intercompany transactions compiled, balances not; Step 4 — draft only; Step 5 controls — quarterly refresh and CFO sign-off recommended.
- **E — Unknowns:** period; balances; fee direction; Okafor; guarantees; Investor A.
- **F — Parameters:** list dated as supplied; match exact and surname/company-name, vendor master only; Marsh related from June 2025.

Would you like `RelatedParty_2025_Northbrook_Trading_Ltd.xlsx`? Only on your yes.
