# SOX controls: operating effectiveness, Northbrook Trading Ltd, September 2025

This run is manual: no Mosofin connection. Everything below comes from the files you uploaded.
Nothing has been posted, paid, sent or changed. Severity is left blank for management and the
auditors; I quantify exposures in amounts only.

## Read-back

Testing **operating effectiveness** of **six controls** in **purchase-to-pay (C1–C3)** and **period
close (C4–C6)** at **Northbrook Trading Ltd** for **September 2025**, in **USD**, from **the control
list and transaction files you uploaded**. Per your list, **four leave a trace in the books (C1, C2,
C4, C6)** and **two need evidence you supply (C3 call-back log, C5 signed bank reconciliation)**.
**No materiality**: exposures are stated in amounts only and no severity is suggested. Walkthroughs
and system descriptions (E) and open prior deficiencies: not answered, so walkthroughs are listed as
not done. Company, period and currency are as you stated; no file names them.

## Validation of the upload (before any work)

| File | What it actually is | Right company and period? | Usable? | Necessary? | Verdict |
|---|---|---|---|---|---|
| `control_list.csv` | Control list: 6 controls, process, description, trace in books (yes/no), evidence location | No company named (user-asserted) | Yes; no owners, frequency, risks or assertions | Steps 4, 6b (routes each control) | **Accepted with a limit**: a control list, not process descriptions; the RACM risk and owner columns stay open |
| `purchase_orders.csv` | 5 purchase orders (PO-1040 to PO-1045; PO-1044 absent), approver and approval date | Aug–Sep 2025 | Yes; no order date and no creator field | C1, C2 | **Accepted with a limit**: "approved before ordering" can only be tested against receipt and bill dates; PO creator-vs-approver SoD cannot run |
| `goods_receipts.csv` | 3 goods receipts against PO-1040, 1041, 1043 | Sep 2025 | Yes | C2 | **Accepted** (company user-asserted) |
| `open_bills_2025-09-30.csv` | 12 open supplier bills at 30 Sep 2025, 255,264 in total | Sep 2025 | Yes; no entered-by or approved-by field; open bills only, no payments | C2, duplicate check | **Accepted with a limit**: "before payment" tested as "would fail at payment"; no paid bills |
| `journal_entries_2025-09.csv` | 7 journals (16 lines), entry date, posting date, user, memo; all balance; 80,468 total debits | Sep 2025 (one dated Aug) | Yes; **one user field only, no reviewer or approver field** | C4, C6 | **Accepted with a limit**: C4 (second-person review) cannot be tested from this file |
| `control_list_final.csv` | A four-week shift rota for employees E08 to E10 | No company, date or amount | Not for this skill | No step uses it | **Rejected**: the name suggests a final control list; the content is a staff rota. Set aside |

**Still missing:** process descriptions (required); evidence for C3 (AP call-back log) and C5 (signed
bank reconciliation PDF) (required for controls outside the books); a journal reviewer/approver field
or review evidence for C4; the August close date (for C6); vendor master change log (C3); payment
records (C2). Materiality: not supplied, and I will not set one. I would stop here and wait.

*You replied: go ahead with the accepted files.*

## Findings (full population; no sampling, so no sample size was set)

| Control | Population | Exceptions | Rate | Result |
|---|---:|---:|---|---|
| C1 PO approved before ordering | 5 POs | 2 | 2 of 5 | Exceptions |
| C2 Three-way match before payment | 12 bills | 11 | 11 of 12 | Exceptions |
| C3 Vendor bank change call-back | — | — | — | **Not tested**: paper log not supplied |
| C4 Journals reviewed by a second person | 7 JEs | — | — | **Not tested**: no reviewer field. **Not effective until evidenced** |
| C5 Bank reconciliation reviewed and signed | — | — | — | **Not tested**: signed PDF not supplied |
| C6 No posting to closed periods | 7 JEs | 1 | 1 of 7 | Exception |

**C1.** **PO-1042 (Summit Freight, 23,449) has no approver and no approval date**, and its bill
INV-4644 is open. **PO-1043 (Brightline IT, 6 laptops, 13,027) was approved on 12 September, after the
bill (9 September) and the goods (10 September)**: retrospective approval. PO-1044 is missing from
the sequence; please confirm it was cancelled.

**C2.** Only Brightline 4715 matches (13,027 vs PO 13,027.02, 6 of 6 received); the exceptions:
- **Kestrel 4502: billed 88,583 against PO value 87,016.80 (4,000 × 21.7542): 1,566.20 (1.8%) over
  the PO price.** Receipt complete.
- **Orchard INV-4573: billed for 100 cartons (41,687), only 90 received: 4,168.70 billed for goods not
  received.**
- **Summit INV-4644 (23,449): unapproved PO, no receipt, due 22 September** and still open.
- **M. Okafor Consulting INV-4857 (7,816): no receipt or service confirmation.**
- **Seven bills with no PO at all: 80,702** (Greyfriars Legal 15,633; Vale Marketing 10,422;
  Northgate Utilities 13,027; Pinecrest Software 23,449; Dale Cleaning 5,211; two Kestrel bills of
  6,480). Some (utilities, legal) may be outside the PO policy; please confirm which categories are.
- **Likely duplicate: Kestrel Supplies INV-4471 (5 Sep) and "Kestrel Supplies Inc." INV4471 (6 Sep),
  both 6,480.** Same invoice number once punctuation is ignored, near-identical vendor name, one day
  apart. **6,480 duplicate-payment exposure**; also suggests a duplicate vendor record (a C3 / master
  data question).

**C4.** Six of seven journals were posted by s.patel, one by a.reyes; nothing in the file shows a
second person. Two journals stand out for review evidence:
- **JE-0904, 28 Sep, a.reyes: "Revenue adjustment", DR receivables 50,000 / CR revenue 50,000**, a
  manual revenue entry with no support. a.reyes also approves POs (A. Reyes, PO-1040 and 1041):
  **purchasing approval and revenue journals in one person** is an SoD question.
- **JE-0907, 30 Sep, s.patel: DR marketing 9,999 / CR accruals 9,999, no memo.** An amount one
  dollar under 10,000 with no description: if 10,000 is a review threshold, this sits just below it.

**C6.** **JE-0905 ("Legal fee missed in August", 3,800) is dated 31 August and was posted on 22
September**, into August after month end. If August was closed by then, this is a posting to a
closed period. September close journals dated 30 September and posted 1–3 October are normal close
entries, unless September was declared closed before them.

**Exposure, aggregated (amounts only, no severity):** unapproved or retrospectively approved POs
36,476; billed above PO or receipt 5,734.90; unmatched service bills 31,265; no-PO bills 80,702
(including the 6,480 duplicate); unreviewed manual revenue journal 50,000; unsupported accrual
9,999; closed-period posting 3,800. These overlap (Summit appears in C1 and C2) and are not additive
to a misstatement.

## What was not done, and why

- **Scoping, walkthroughs, risks (Steps 1–3)**: no process descriptions or system information.
- **Design assessment (Step 5)**: no thresholds or control owners; C4's threshold unknown.
- **C3, C4, C5 operation**: evidence not supplied. They are **not tested, not effective**.
- **SoD across the population**: only JE user and PO approver are recorded.
- **Deficiency severity (Step 8)** and **remediation (Step 9)**: yours and the auditors'.
- **Excel workbook**: not created. Do you want `SOX_ICFR_2025_Northbrook Trading Ltd.xlsx`?

## Coverage and provenance (manual run)

| Section | Content |
|---|---|
| Environment | Northbrook Trading Ltd, Sep 2025, USD, user-asserted; source upload; five files accepted (four with limits), rota rejected; no materiality |
| Capability map | Not applicable: no connection. Every task is `[manual]` |
| Steps | 1–3 **not done**; 4 RACM from your list, risks open; 4b partial; 5 **not done**; 6–7 done for C1, C2, C6 at full population; C3–C5 **not tested**; 8 amounts only; 9 open |
| Unknowns | Duplicate Kestrel bill; JE-0904 support; JE-0907; August close date; PO-1044; no-PO policy |
| Parameters | Full population: 5 POs, 3 receipts, 12 bills, 7 journals; no sample size; no threshold |
