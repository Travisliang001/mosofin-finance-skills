<!-- vendor-onboarding-and-w9-tin · method.md · read for: Stages 3–6 — the work itself. Edit here, not in SKILL.md. -->

## Contents

- How to read the verdicts
- Step 0 — Audit the vendor master *(Mosofin addition, promoted from the original's closing note)*
- Step 0a — Completeness
- Step 0b — Completeness weighted by payment activity
- Step 0c — Bank-detail change detection
- Step 0d — Duplicate vendors
- Step 0e — Related parties and vendor/customer overlap
- Inputs
- Workflow
- Step 1 — Identify the form type
- Step 2 — Extract fields
- Step 3 — Validate
- Step 4 — Screening
- Step 5 — Bank-detail verification
- Step 6 — Payment terms and currency
- Step 7 — Set up classification
- Step 8 — Output
- Output Quality Standards
- Seed to evolved: what happens on the first real run
- Anti-patterns


## How to read the verdicts

- **`[auto]`** — Mosofin can do this from live reads, unattended.
- **`[gated]`** — the gateway asks first. Explain, get consent, re-invoke with `approved=true` (**reads only — never for a write**) and the `data_source_id`.
- **`[manual]`** — not on this surface, or not a machine's judgment. **The step stays. The user performs it.**

**Everything here is a proposal.** The gateway is read-only. **Mosofin creates no vendor, changes no bank detail, screens nobody and clears nobody.**

---

## Step 0 — Audit the vendor master *(Mosofin addition, promoted from the original's closing note)*

**`[auto]`. One batched read across the whole master, and it should run before any individual onboarding, because it establishes whether the vendor already exists.**

### Step 0a — Completeness

Read every vendor record and test for the fields Step 2 requires: legal name, entity type, address, tax identifier, country of tax residence, bank details, payment terms, contact.

**Report by field and by vendor.** `[auto]`.

**But do not stop here** — an unranked completeness list is the audit nobody reads.

### Step 0b — Completeness weighted by payment activity

**`[auto]`, and this is the reframing that makes the audit useful.**

**Join the master to payment history.** For every vendor with a missing or invalid field, show **what was paid to them this year and last.**

| Situation | Priority |
|---|---|
| **Incomplete record, no payments in two years** | Housekeeping. Consider deactivating. |
| **Incomplete record, modest payments** | Remediate in the normal cycle. |
| **Incomplete record, material payments** | **The finding.** Missing tax form on an actively-paid vendor is a reporting exposure and, in the US, potentially a backup withholding one. |
| **No record of a tax form, payments approaching the reporting threshold** | **Preventive** — fix it before the year end rather than during the reporting scramble. |

**Rank by amount paid.** A list of twelve vendors ordered by money is acted on; a list of four hundred ordered by vendor code is not.

### Step 0c — Bank-detail change detection

**`[auto]` where the surface exposes master-data change history. The highest-value detection in this skill.**

**Read every change to vendor banking data**: what changed, when, and — where recorded — by whom.

Then test for the pattern:

| Signal | Why it matters |
|---|---|
| **A bank detail change followed by a payment within a short window** | **The payment-redirection fraud signature.** The purpose of the change was the payment. |
| **A change to a long-dormant vendor** shortly before activity resumes | Same shape, slower. |
| **A change made by the same person who then approved or released the payment** | A segregation-of-duties failure on the highest-risk master field. See `sox-controls-design-and-testing`. |
| **A change to a bank account in a different country from the vendor** | Step 5's consistency check, applied retrospectively across the whole master. |
| **Several vendors' details changed to the same account** | Unambiguous, and worth surfacing immediately. |

**How to report it.** With dates, vendors, amounts and — where the pattern warrants — urgency. **Never as an accusation.** The overwhelming majority of bank-detail changes are legitimate: a supplier genuinely changed banks, a factoring arrangement started, an account was consolidated. **The point is not that a change is suspicious; it is that a change followed immediately by a payment is the one shape that should always have been verified**, and Step 5 already says how.

**Where the surface does not expose change history, say so explicitly.** This test not running must never look like this test passing.

### Step 0d — Duplicate vendors

**`[auto]`, full population, and it is the check the original places in Step 4 as one line.**

> **Duplicate vendor check** — match by **name, tax ID, bank account, address**; flag potential duplicates in the master.

All four match keys, run across every pair in the master:

| Key | Note |
|---|---|
| **Tax ID** | **The strongest.** Two records, one tax ID, is a duplicate almost without exception. |
| **Bank account** | **Equally strong, and it also catches deliberate duplication** — two vendor names paying to one account. Match on a masked identifier where possible. |
| **Name** | **Fuzzy**, and it needs to be: "Acme Ltd", "Acme Limited", "ACME LTD." and "Acme" are one supplier and four records. |
| **Address** | Useful corroboration, and it catches name changes. |

**Why duplicates matter beyond tidiness:**

- **Duplicate payments.** The same invoice entered against two vendor records defeats duplicate detection that keys on vendor. See `duplicate-invoice-detection` and `three-way-match` exception 9.
- **Split history.** Spend analysis, `vendor-statement-reconciliation` and any negotiation based on volume all break when one supplier's activity sits under two records.
- **Incomplete compliance.** One record has the W-9, the other does not — and payments made under the second are unreported.
- **They multiply.** A near-miss name creates a second record, which is exactly the failure `quickbooks-ar-aging-collections` warns about from the customer side.

**Report as candidates with their evidence**, ranked by combined payment volume. **Merging records is `[manual]`** — and irreversible in many systems, so it needs care and it is not Mosofin's to do.

### Step 0e — Related parties and vendor/customer overlap

`[auto]`. Match the vendor master against **the customer list** and against **other connected entities' `display_name`s.**

- **A name in both the vendor and customer masters** — could be an ordinary reciprocal trading relationship, could be a related party. **Ask.** See `related-party-disclosures-asc850`.
- **A vendor matching a connected entity** — intercompany trading recorded as third-party, which is an elimination problem as well as a disclosure one. See `consolidation-and-eliminations`.
- **A vendor sharing an address or bank account with an employee**, where employee data is available — **this is a fraud test and a sensitive one.** Flag the coincidence factually; conclude nothing. See `fraud-detection-and-forensics`.

---

## Inputs

All seven preserved.

| Input | Format | Required | Mosofin source | Verdict |
|-------|--------|----------|----------------|---------|
| **Vendor's submitted form / document** | PDF, image, or pasted data | **Required for validation** | **Not in the books.** A document. | `[manual]` |
| **Entity's jurisdiction (the payer's country)** | Country | **Required** | Not in the books | `[manual]` |
| **Vendor's claimed country** | Country | **Required** | **`[auto]` where recorded on the master** | Split |
| **Vendor's legal name and entity type** | Text | **Required** | **`[auto]` for what is recorded — which is not necessarily the legal name** | Split |
| **Vendor's address** | Text | **Required** | `[auto]` where recorded | `[auto]` |
| Vendor's bank details | Text | Required for payment setup | **`[auto]` where exposed — commonly `[gated]`** | Conditional |
| **Existing vendor master** | CSV / XLSX | **Required for audit mode** | **`[auto]`, in full — this is Step 0** | **`[auto]`** |

---

## Workflow

### Step 1 — Identify the form type

**`[manual]`.** All twelve rows of the reference table preserved.

| Form | Used by | Purpose |
|------|---------|---------|
| **W-9** | US payers, US payees (individuals or entities) | Capture name, TIN/SSN/EIN, entity type for 1099 reporting |
| **W-8BEN** | US payers paying non-US individuals | Treaty claim, beneficial owner, no withholding or reduced rate |
| **W-8BEN-E** | US payers paying non-US entities | Entity classification, treaty claim |
| **W-8ECI** | US payers paying non-US persons with US-effectively-connected income | Different withholding rules |
| **TD1 / TD1ON etc.** | Canada — employee tax credits | **Payroll, not vendor onboarding** |
| **NR4 / Form NR301** | Canada paying non-residents | Treaty exemption claim |
| **VAT registration certificate** | EU / UK / many jurisdictions | Confirms VAT registration for reverse-charge / B2B treatment |
| **GST / HST registration** | Canada | Confirms registration; allows input tax credit |
| **CR / TRN / National ID** | UAE / Saudi / GCC | Trade licence / tax registration |
| **PAN + GSTIN** | India | Permanent Account Number + GST identifier |
| **ABN registration** | Australia | Australian Business Number |
| **TIN (generic)** | Most jurisdictions | Taxpayer identifier |

> **If the form is unfamiliar, ask the user to identify it or treat it as a "Tax registration certificate" with whatever fields are present.**

**Note the TD1 row is a deliberate exclusion** and it is preserved as such — it is a payroll form and does not belong in a vendor file. Its presence in a vendor's documentation is itself worth querying.

**And the VAT/GST rows connect onwards**: a vendor's VAT registration status drives the reverse-charge treatment in the VAT and GST work, and a missing or invalid one can invalidate it.

---

### Step 2 — Extract fields

**`[manual]` from the document; `[auto]` for what the master already holds — and comparing the two is the validation.**

**Common required fields for any vendor**, all thirteen preserved: legal name (**must match the form, not the trade/DBA name**); trade name / DBA if different; entity type (individual / sole proprietor / partnership / corporation / LLC / trust / nonprofit / government / other); address (**registered office, not just mailing**); tax identifier(s); country of tax residence; country of incorporation or formation; date of incorporation or formation where relevant; bank details (account name, account number, IBAN, SWIFT/BIC, routing/sort code, intermediary bank if any); currency of payment; payment terms; designated contact.

**For W-9 specifically**, all six: legal name; business name or disregarded entity name if different; **federal tax classification** (Individual / Sole Proprietor / C-Corp / S-Corp / Partnership / Trust / LLC plus the LLC's tax classification); exempt payee code if any; **TIN (SSN, EIN, or ITIN)**; signature and date.

**For W-8BEN / W-8BEN-E**, all preserved: beneficial owner name; country of citizenship or incorporation; **permanent residence address — not a P.O. box, not "in care of"**; mailing address if different; US TIN if any, and foreign TIN; date of birth (W-8BEN only); **treaty country and article claimed**; type of income covered; capacity in which acting; signature, date, certification.

**For W-8BEN-E (entities), plus**: entity type (corporation, partnership, simple trust, complex trust, foundation, government, central bank of issue, tax-exempt organisation); **Chapter 3 status**; **Chapter 4 (FATCA) status — GIIN if applicable**; **LOB article** for the treaty claim; **substantial US owners** for passive entities.

**`[auto]` contribution: the comparison.** Where the master already holds a value — name, address, tax ID, country — **compare it to the form.** A mismatch between the record and the document is a finding, and it is one the manual process rarely makes because the record and the form are handled by different people at different times.

---

### Step 3 — Validate

`[manual]` for the form; **`[auto]` to apply format rules across the whole master.**

**Format validation** for the tax identifier — all ten rules preserved:

| Jurisdiction | Rule |
|---|---|
| **US SSN** | 9 digits, NNN-NN-NNNN |
| **US EIN** | 9 digits, NN-NNNNNNN, **valid prefix — some prefixes are not assigned** |
| **US ITIN** | Starts with 9 |
| **Canada Business Number** | 9 digits |
| **UK VAT** | GB + 9 digits, or 12 with branch |
| **EU VAT** | Country prefix + digits, **length varies** |
| **Indian PAN** | 10 characters, AAAAA9999A |
| **Indian GSTIN** | 15 characters — state code + PAN + entity number |
| **Australian ABN** | 11 digits **with checksum** |
| **UAE TRN** | 15 digits, starts with 100 |

> **If the format is wrong → fail validation, ask for resubmission.**

**`[auto]`, and run it across the entire master, not just the vendor being onboarded.** Format-invalid tax IDs sitting in a master are exactly the sort of thing that surfaces at year end when a return is rejected — and by then the vendor may be unreachable.

**Cross-check name and TIN:**

> **Some jurisdictions provide free lookup services — IRS TIN matching, HMRC VAT validator, EU VIES. If the user has access, recommend running the check. Claude can format the request but cannot run the live lookup itself.**

**Preserved exactly, and it is the honest position.** **Format validation confirms shape; matching confirms the identifier belongs to the name**, and only the lookup does that. `[auto]` prepares the queries; `[manual]` runs them.

**Completeness**, all three: all required fields populated; **form signed and dated**; **form not expired** — W-8 typically valid three years; check the user's policy.

**`[auto]` for expiry across the master** where the form date is recorded: **which W-8s are expiring in the next 90 days**, ranked by payment volume. **Preventive, and it is a genuinely useful standing report** — an expired W-8 means withholding at the full rate on the next payment.

**Consistency**, all three preserved:

- **Name on form = name on bank account** — **mismatch = fraud risk**
- **Address country = country of incorporation** — mismatch needs explanation
- **Bank country aligns with vendor country** — mismatch needs explanation

**`[auto]` for the second and third across the whole master**; `[manual]` for the first, since the name on the bank account comes from a bank letter, not from the ledger.

---

### Step 4 — Screening

**`[manual]`, and the boundary must be stated plainly every time.**

> **For each new vendor, recommend screening against:**
> - **Sanctions / OFAC** — US payers must screen; many jurisdictions require similar checks
> - **PEP (Politically Exposed Persons) lists**
> - **Internal blocked-vendor list**
> - **Duplicate vendor check** — **`[auto]`, Step 0d**
>
> **Claude doesn't run live screening but produces a screening checklist with the values to query.**

**Preserved exactly.** Three of the four require live access to lists Mosofin does not have.

> **Mosofin cannot screen. Therefore Mosofin clears nobody.**

**This must appear on the screening sheet itself**, because the failure mode is specific and serious: a screening checklist with no findings against it can be filed as though screening was performed. **An empty result means the check has not been run.** Mark every unrun check `⏸ Pending` — the original's own status code — and never blank.

**`[auto]` contributions**: the duplicate and blocked-list checks are population joins **where the blocked list is supplied**, and the search strings for the external checks are assembled automatically, including name variants and alternative spellings that improve a sanctions search's recall.

---

### Step 5 — Bank-detail verification

**The critical fraud-prevention step**, and all four points preserved.

- **Bank account name should match the vendor's legal name** — `[manual]`, from a bank letter
- **Out-of-country bank accounts for an in-country vendor need explanation** — **sometimes legitimate, often fraud.** `[auto]` across the master
- **Compare against any prior bank details on file — any change requires reverification through a known contact, not the contact who submitted the change** — **`[auto]` to detect, Step 0c; `[manual]` to verify**
- **Recommend a small test payment to confirm before first full payment** — `[manual]`

**The third point is the one that prevents the loss**, and its qualifier is the operative part: **not the contact who submitted the change.** A fraudulent change request arrives with a plausible contact attached; verifying with that contact verifies nothing. **Use a number from the file, not from the request.**

**`[auto]` makes that instruction enforceable rather than aspirational**, because Step 0c shows which changes happened and whether a payment followed — which is the evidence that the verification either happened or did not.

---

### Step 6 — Payment terms and currency

`[manual]` to confirm; `[auto]` to observe. All five preserved.

- **Confirm payment terms** — Net 30 default if not specified
- **Confirm payment currency** — vendor's preferred versus the entity's payment currency
- **Confirm payment method** — wire, ACH, SEPA, BACS, cheque, card
- **For wires**: SWIFT/BIC, intermediary bank, all banking details captured
- **For ACH/SEPA/BACS**: routing or sort code, account number, IBAN where applicable

**`[auto]` for one useful comparison**: **terms as recorded versus terms as operated.** A vendor set up on Net 30 who is consistently paid at 55 days is either being paid late or the recorded terms are wrong — and the same computation appears in `quickbooks-ar-aging-collections` from the customer side. It matters for working capital analysis and for supplier relationships. See `working-capital-optimization`.

---

### Step 7 — Set up classification

`[auto]` to flag candidates; **`[manual]` to determine.** All five preserved.

| Flag | Criteria | Verdict |
|---|---|---|
| **1099-reportable** (US) | Non-corporate individual or entity providing services in the US, US payer, above the de-minimis threshold for the year | **`[auto]` for the payment total and the entity type where recorded**; `[manual]` for the determination. See the 1099 and T4A preparation |
| **T4A-reportable** (Canada) | Similar criteria for Canadian payers | Same |
| **Reverse-charge VAT** | Entity importing services from outside its jurisdiction | **`[auto]` to identify the population** Step 4b, which is the same detection |
| **Withholding tax required** | Treaty doesn't apply, or the vendor didn't certify | `[manual]` for the rate; **`[auto]` to flag vendors with no valid certification and material payments** |
| **Related party** | Flag for elimination consideration | **`[auto]`** — Step 0e |

**The reverse-charge row is worth noting as a genuine cross-skill link**: the vendors flagged here are exactly the population the VAT and GST work sweeps for, and **setting the flag at onboarding is what prevents the omission later.** The two skills should share the list.

**And the withholding row has a preventive version**: rather than discovering at year end that a vendor never certified, **`[auto]` reports vendors approaching the threshold with no valid form**, which is Step 0b's ranking applied forward.

---

### Step 8 — Output

A vendor record as an `.xlsx` or a vendor-master-ready row. All five of the original's sheets, plus two additions.

**Sheet 1: Vendor Record**
All validated fields by section — identity, tax, banking, payment terms, classification. **Banking fields masked except where the deliverable's recipient needs them**, per the data note.

**Sheet 2: Validation Results**
| Field | Value | Validation Status | Notes |

**All four status codes preserved:**
- **✅ Valid**
- **⚠️ Warning** — e.g. bank country mismatch
- **❌ Invalid / missing** — must be fixed
- **⏸ Pending** — waiting on an external check

**`⏸ Pending` is the status that carries the screening boundary.** Everything Mosofin cannot run is Pending, never blank and never Valid.

**Sheet 3: Screening Checklist**
Sanctions, PEP, duplicate, blocked-list — **with the search strings to run.** Header states, in bold: **Mosofin does not run screening; unrun checks are Pending, not clear.** Duplicate results from Step 0d appear here populated.

**Sheet 4: Required Documents**
Tax form (received Y/N); bank verification (voided cheque, bank letter); business licence or registration; insurance certificate; signed services agreement or PO; privacy / NDA / DPA. **`[manual]`, per the entity's policy** — persist the policy so the list is consistent.

**Sheet 5: Vendor Master Import**
Format for the user's accounting system's vendor import. **`[manual]` to import — the gateway does not write.**

**Sheet 6: Master Audit** *(Mosofin addition)*
The Step 0 results, in one place:

| Finding | Vendors | Payments (12m) | Evidence | Priority | Action |
|---|---|---|---|---|---|

Incomplete records ranked by payment volume. Bank-detail changes with payment proximity. Duplicate candidates with match keys. Format-invalid tax IDs. Expiring forms. Vendor/customer overlaps. **Ranked by money throughout.**

**Sheet 7: Coverage and Provenance** *(Mosofin addition)*
The mandatory coverage sheet, **including whether bank data and change history were readable.**

Ask the user whether they want this workpaper as an Excel (`.xlsx`) file, and create it only on a yes, using the file name given for this skill. If they decline, or the host cannot make spreadsheets, give the same sheets as tables in the chat.

File naming: `Vendor_[VendorName]_Onboarding_[YYYY-MM-DD].xlsx`, and **`Vendor_Master_Audit_[YYYY-MM-DD]_[EntityName].xlsx`** for a Step 0 run.

Entity `display_name` on every sheet. If any read returned `mock: true`, say so in the file name and on Sheet 6.

---

## Output Quality Standards

All seven preserved.

- **Every required field has a value or an explicit "Missing — requested from vendor" note.** `[auto]` across the master, **ranked by payment volume.**
- **Tax ID format-validated for the stated jurisdiction.** **`[auto]`, across the whole master, not just the vendor in hand.**
- **Sanctions / PEP / duplicate screening checklist provided.** `[manual]` for the external checks — **marked Pending, never clear**; `[auto]` for duplicates.
- **Bank details verified or flagged as unverified.** `[manual]` to verify; **`[auto]` to detect changes and country mismatches.**
- **Classification flags set** — 1099, T4A, reverse-charge, withholding, related party. `[auto]` for candidates.
- **File naming consistent.** `[auto]`
- **No silent assumption about jurisdiction or entity type.** `[manual]`

**Five Mosofin additions:**

- **The master audit is ranked by money**, not by record count.
- **Bank-detail changes are tested for payment proximity**, every run.
- **Duplicates are matched on all four keys across the full population.**
- **Unrun screening is Pending, never blank** — Mosofin clears nobody.
- **Banking and identity data are read, not reproduced**, and masked where the analysis permits.

---

## Seed to evolved: what happens on the first real run

**What must never be frozen into a seed:** the capability map — Gate 2 reads it fresh — **and any jurisdiction's format rules**, which do change.

**What is worth persisting into the workspace-scoped skill:**

1. **The required-document policy** — what this entity demands before a vendor is paid. Sheet 4 is built from it.
2. **Duplicate candidates already reviewed and confirmed *not* duplicates**, with the reason — **especially legitimate remit-to children**, or the duplicate report will be dismissed wholesale next quarter.
3. **Bank changes already verified**, so a resolved change is not re-raised.
4. **The screening arrangements** — who runs them, on what service, how evidenced.
5. **Classification determinations per vendor** — 1099 status, reverse-charge flag, withholding position — **shared with the 1099 and T4A preparation and the VAT and GST work.**
6. **Form expiry dates**, so the 90-day report runs itself.
7. **Fuzzy-match thresholds tuned for this master's naming conventions.**

Persist through `create_skill`, scoped to the workspace. **Client facts belong in a client-scoped skill, never back in the seed** — and **vendor banking and identity data should not be persisted at all beyond what the classification requires.**

**The evolved version's monthly job is short**: what changed in the master, which changes preceded a payment, which forms expire soon, and which actively-paid vendors are still undocumented.

---

## Anti-patterns

- **Reporting incomplete records without ranking by payment volume.** The unranked list is the one nobody reads.
- **Letting an empty screening result look like a clear result.** Mosofin clears nobody; unrun is Pending.
- **Treating format validation as verification.** Shape is not identity.
- **Verifying a bank-detail change with the contact who requested it.**
- **Ignoring a bank change because it was months ago.** Check whether a payment followed.
- **Matching duplicates on name alone.** Tax ID and bank account are stronger.
- **Reporting legitimate remit-to children as duplicates**, which discredits the whole report.
- **Merging vendor records automatically.** Irreversible in many systems, and not Mosofin's to do.
- **Assuming an LLC's reportability.** The classification must be captured.
- **"Correcting" an SSN to an EIN.** Both are valid TINs.
- **Editing a vendor record on a name or TIN change.** It breaks the audit trail.
- **Allowing a "one-time payee" to become a recurring one** without onboarding.
- **Reproducing bank or identity details** where a masked identifier would do.
- **Onboarding into a sanctioned jurisdiction.** Hard stop — and Mosofin cannot make that determination.
- **Saying "screened", "cleared" or "created".** The gateway reads.
