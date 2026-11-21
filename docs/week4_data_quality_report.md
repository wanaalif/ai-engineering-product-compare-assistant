# Week 4 Data Quality and Bias Report: Product Compare Assistant

**Student:** Alif | **Audit date:** 18 November 2026 | **Audited stage:** Topic 3 Part B prepared files

Labels used: **Observed** = checked in a file, log, or script output. **Inferred risk** = plausible but not proven. **N.V.** = Not Verified. Evidence codes are explained in Appendix A.

## 1. Project and Data Overview

The Product Compare Assistant helps online shoppers compare headphones. The later AI task is retrieval-augmented generation: find evidence in product text, customer reviews, and reference papers, then write a comparison that cites its sources.

| Item | Record |
|---|---|
| Two Topic 2 requirements | **FR1:** compare named headphones (features, specifications, review-based strengths and weaknesses). It needs product text (S01) and review text (S02), linked by `parent_asin`. **FR4:** give a source reference for every claim. It needs a stable ID on every record (`record_id`, `parent_asin`; DOI and page for papers). I chose them because FR1 is the comparison that solves the problem statement, and FR4 is the grounding that objectives O1 and O2 promise. |
| Pathways audited | D (JSON records: S01 products, S02 reviews) and A (PDF text: S03, S04, S05) |
| Audited outputs (Part B) | `data/processed/prepared_meta.jsonl` (56,043 records, SHA-256 `dc0e5179…`), `data/processed/prepared_reviews.jsonl` (39,033 records, `597ff358…`), `data/processed/prepared_text.jsonl` (147 chunks, `f4e08cf3…`) |
| Matching manifest | `data/week3_manifest.json` [E1] |
| Where the files are | `prepared_text.jsonl` is in the repository. The full prepared S01 and S02 files are restricted (no stated licence) and stay in the working storage of the Week 3 Colab run. Only 20-record samples are committed in `data/samples/`. |
| Source and access status | S01, S02: Amazon Reviews 2023, Hugging Face revision `2b6d039e…`, **licence not stated (N.V.)**. S03: CC BY 4.0 per the article page footer (checked 4/11/2026). S04, S05: CC BY, **version N.V.** |
| Population, unit, and sample | **Text chunk:** 147 of 147 inspected (all). **Product record:** 20, the first 20 records of the prepared file (`data/samples/prepared_meta_sample.jsonl`), a convenience sample. **Review record:** 20, chosen the same way. Full-file numbers for S01 and S02 come from the Week 3 pipeline log and inspection [E3] and were not recomputed here. |
| Limits | The two JSON samples are not representative. The raw S01 and S02 files and the PDFs were not reopened, so accuracy against the source is N.V. beyond the 10 spot checks in section 2. |

**Checkpoint A1.** If a product has no review in S02, FR1 cannot give review-based strengths or weaknesses for it. If a record has no ID, DOI, or page, FR4 cannot cite it.

## 2. Five-Dimension Quality Scorecard

| Dimension | Finding and evidence | Impact on the task | Decision |
|---|---|---|---|
| **Completeness** | **Observed:** 11,528 of 56,043 prepared products (20.6%) have neither features nor description [E3]; 4 of 20 in the sample [E4]. Price exists for only 22.2% of source products [E3]. **Observed (derived):** at least 17,010 products (30.4%) have no review in S02, because 39,033 reviews cannot cover 56,043 products. **Observed:** the reference text has 0 chunks that mention impedance or drivers, and 1 that mentions noise cancelling [E4]. | FR1 comparisons for these products rest on title and details only. Explanations of common terms would be missing. | Warning |
| **Consistency** | **Observed:** 78 of 147 chunks (53%) contain ligature characters (ﬁ, ﬂ; 194 in total; S04 49 of 65, S05 29 of 34). "filter" appears in 1 chunk and its ligature spelling in 27 [E4]. **Observed:** 7,529 of 39,046 raw reviews (19.3%) had HTML tags; none remain in the 20-review sample [E3, E4]. **Observed:** all 147 chunks are labelled "CC BY 4.0", but the S04 and S05 version is unconfirmed [E1]. | Keyword search (the BM25 half of the hybrid retrieval) would miss many chunks. The licence label may claim more than is verified. | Warning |
| **Accuracy** | **Observed:** 10 spot checks agree with the source: 2 products and 2 reviews against the raw records printed in notebook Cell 9, and 6 PDF page starts (S03, S04, S05, pages 1 and 2; S05 page 1 starts at Section 1 by design). The review date conversion was checked (1676601581238 gives 2023-02-17). **Observed:** 5 of 20 sample products are not headphones although labelled "Headphones & Earbuds" (see V2). **Observed:** 4 chunks are figure or table text with at least 40% non-letter characters, for example S04-p005-01 (axis labels) [E4]. **N.V.:** accuracy beyond these checks. | FR1 could compare a lantern with headphones. Noisy chunks reduce retrieval precision. | Review |
| **Timeliness** | **Observed:** S01 and S02 are a 2023 snapshot (reviews run to Sep 2023, about 3 years old at audit). Sample review dates run from 2010-12-22 to 2023-02-17, and 19 of 20 sample products show a first-available date from 2004-09-01 to 2023-02-27 [E4]. S04 and S05 were published in 2016 and S03 in 2025. The only freshness requirement is FR5 (no current price or stock). | Newer models are absent. Price and stock questions must be refused (FR5). | Warning (acceptable for coursework scope) |
| **Uniqueness** | **Observed:** 0 duplicate record IDs and 0 duplicate chunk texts among the 147 chunks; 20 of 20 distinct IDs in each sample; S01 had 56,048 distinct `parent_asin` values [E3]. **Observed:** 8 of 20 sample reviews have an `asin` that differs from `parent_asin` (product variants), so joins must use `parent_asin`. **N.V.:** duplicate reviews in the full S02 file. | Duplicate evidence would count one opinion several times. | Pass (observed items); N.V. for full files |

## 3. Validation Findings

| Rule | Condition and scope | Items tested and result | Action on failure |
|---|---|---|---|
| **V1** (FR4) | Every prepared record has a usable source reference. Chunk: non-empty `source_id`, `doi`, `title`, `licence`, `text`; integer `page` of at least 1; `source_sha256` equals the manifest value. Product and review record: non-empty `record_id`, `parent_asin`, `source_id`, and for reviews non-empty `text`. | 187 tested (147 chunks, 20 products, 20 reviews). **187 pass, 0 fail** [E4]. S01 and S02 results cover the samples only; full files are N.V. | **Hard fail.** Stop the pipeline, because a claim could not be cited. |
| **V2** (FR1; Topic 3 filter risk) | Every prepared product is a headphone or earbud product, not an accessory or unrelated item. The Week 3 filter used the category branch "Headphones & Earbuds" and trusted its labels. A keyword screen nominated 9 of 20 titles, and I judged them by hand. | 20 tested. **15 pass, 5 fail** [E4]: B00KS0K4MG (replacement cable), B00A3QQKIW (storage cart), B007XSU2XC (LED lantern), B08225X6DB (AirPods skin), B010R0X7N4 (phone wallet case). Population: **N.V.** | **Review.** Add a `product_type_suspect` flag and quarantine after manual review. Do not delete automatically: some accessories (for example a headphone cable) may be valid for accessory questions. |

**Reference integrity (every S02 review links to an S01 product):** **N.V.** The two samples are the first rows of different files and do not overlap (0 of 19 review products appear in the 20-product sample), so this is not a join test. Smallest next check: run `docs/week4_audit_checks.py --full-meta … --full-reviews …` on the full files.

## 4. Duplicate, Anomaly and Coverage Findings

**Duplicates.** None found in the observed items (section 2). Full S01 and S02 files: N.V.

**Anomalies (Observed [E4]).**
- Author contact details: S03-p001-01 and S04-p001-01 contain email addresses and phone numbers.
- Figure and table text: S03-p006-05, S03-p007-02, S04-p005-01, S04-p015-03.
- Back matter and journal footers: S03-p008-07, S04-p016-04 (conflicts of interest, abbreviations), S04-p001-05, S05-p001-02.
- 4 chunks are under 200 characters. The shortest, S03-p003-06 (71 characters), is a sentence that continues on the next page.
- Non-headphone products: see V2. Of the 4 sample products without text, 2 are not headphones (a cable and a wallet case) and 2 are genuine headphones, so missing text alone does not identify bad records.

**Coverage of two relevant cases.**

| Case | Expected evidence | Observed evidence and gap | Possible effect |
|---|---|---|---|
| Headphone types (FR1, needs-based requests) | Enough products of each type with text | S01 extract of 56,048 products [E3]: earbud 37,403 (66.7%), over-ear 8,951 (16.0%), on-ear 3,804 (6.8%), open-ear 227 (0.4%), no subtype 5,663 (10.1%). Sample of 20: 14 earbud, 4 over-ear, 1 on-ear, 1 none. | Open-ear and on-ear requests have few candidates, 10.1% of products cannot be filtered by type, and results lean towards earbuds. |
| Products with review evidence (FR1, review-based strengths and weaknesses) | At least one review per product | **Observed (derived):** at least 17,010 of 56,043 products (30.4%) have no review in S02. Exact coverage: **N.V.** The 20 sample reviews cover 19 products. | No review-based comparison for at least 30.4% of products. The assistant must say "no review evidence". |

Limit: product-type counts come from the extract before preparation (5 records were later excluded), and review coverage is a lower bound on the gap.

## 5. Bias Assessment

**Main risk (Inferred risk): pipeline-induced representation bias in the review subset.**

| Step | Statement |
|---|---|
| Source or preparation decision | S02 scans only the first 500,000 rows of the Electronics review file, then keeps reviews of headphone products. |
| Data gap or skew | 39,033 reviews for 56,043 products. At least 30.4% of products have no review. Which products have reviews depends on file order (N.V.). |
| Potential effect on the application | Retrieval finds rich review evidence for some brands and none for others, so some comparisons look better evidenced only because of file order. |
| Proposed control | Compute review counts per product by store and by `rating_number` group (the stratified test in RAI3). Scan the full file using the product ID list, or sample across the file. Show the evidence level in each answer and refuse review-based claims when there are no reviews. |

**Second risk (Inferred risk): measurement bias in ratings.** 15 of 20 sample reviews are 5-star. The assistant should show rating counts and should not present an average rating as proof of quality.

**A trade-off I accepted.** Config B in Part B would have removed 11,528 products and 2,288 of 10,936 stores (20.9%), so I kept all products (Config A) to protect brand coverage. The sample shows that some text-less products are not headphones, so V2 now adds the product-type flag instead.

This section does not claim anything about system accuracy or fairness. That needs the later evaluation.

## 6. Privacy, Rights and Governance

| Question | Finding |
|---|---|
| Provenance and version | **Observed:** `prepared_text.jsonl` has SHA-256 `f4e08cf3…`, which matches the manifest. Part B and Part C outputs have identical hashes for all five prepared outputs, and source hashes match across the manifests [E1, E2]. The Week 3 repeatability check passed (Cell 18). Dataset revision `2b6d039e…` (last modified on the Hub on 8 Dec 2024). |
| Rights and permissions | S01 and S02: no licence stated, so permission for sharing is **N.V.** (use is limited to private coursework). S03: CC BY 4.0 per the article page footer. S04 and S05: CC BY, version **N.V.**, yet the records say "CC BY 4.0". |
| Privacy and sensitive data | **Observed:** `user_id` is absent in 20 of 20 sample reviews (full file N.V.). **Observed:** two text chunks contain author email addresses and phone numbers (S03-p001-01, S04-p001-01); they are public in the papers but not needed. **N.V.:** names, emails, or phone numbers inside review text. |
| Consent or collection basis | Reviews are public posts collected by the dataset authors. Consent for this secondary use is **N.V.**. The papers are open access publications. |
| Ongoing maintenance | The project owner (me) reviews and corrects the data. Questions about rights go to the lecturer. Revalidate when the dataset revision changes, a licence is clarified, the preparation settings change, or a rule fails on the full files. |

**Required actions.** (1) Redact author emails and phone numbers before indexing. (2) Set the S04 and S05 licence label to "CC BY (version to confirm)" until I read the version in each PDF. (3) Decide whether the two sample files in `data/samples/` may stay in a public repository, because they contain Amazon customer text with no stated licence. If not, remove the review text from the sample or make the repository private.

## 7. Mitigation and Impact on Requirements

| Priority | Improvement | Owner and timing | Requirements affected | Risk that remains |
|---|---|---|---|---|
| 1 | Run the full-file checks (`week4_audit_checks.py --full-…`): reference integrity, review coverage by store and rating group, duplicate reviews, contact details in reviews. Add `product_type_suspect` and `review_count` flags, and review the flagged products by hand. | Me, before building the evaluation sets in Topic 5 | FR1, FR4, RAI2, RAI3, NFR3 | The keyword screen cannot catch every non-headphone product. The licence of S01 and S02 stays unknown. |
| 2 | Clean the text corpus before indexing: Unicode normalisation (fixes ligatures), redact emails and phones, drop back matter and figure or table chunks (or flag them), and fix the licence label. | Me, before embeddings and indexing in Topic 5 | FR4, NFR3, RAI1 (and FR7) | Sentences split at page breaks. Accuracy beyond the spot checks stays N.V. |

**Also open (not audited here):** FR7 needs explanations of terms such as impedance and drivers, which no chunk covers. I need one more reusable source or a narrower FR7. **Residual risks:** unknown rights for S01 and S02, an unverified review-coverage bias, 2016 reference papers, and small samples.

## 8. Quality-Gate Decision

**GO WITH CONDITIONS.**

**Scope:** use of the Part B prepared files for private development in this course: building retrieval experiments and evaluation sets. Not for publishing S01 or S02 content, and not for claims about system accuracy.

**Evidence.**
1. V1 passed on all 187 items, and the hash chain from source to prepared file to manifest is intact (Part B and Part C outputs match).
2. Known defects are findable and fixable: 5 of 20 sample products are not headphones (V2), at least 30.4% of products have no review, and 53% of text chunks contain ligatures.

**Why not GO:** the defects above would reduce FR1 correctness and retrieval quality if left unfixed, and licence and privacy questions are open. **Why not HOLD:** no blocking rights or privacy problem exists for private coursework use, and every problem has a clear next step.

**Conditions.**
- **C1** Complete the full-file checks and flags (priority 1) before building the evaluation sets.
- **C2** Complete the text corpus cleaning (priority 2) before indexing.
- **C3** Confirm the CC BY version for S04 and S05, and decide on the sample files in `data/samples/` before the repository becomes public.
- **C4** Resolve the N.V. items in Appendix B, or keep them marked N.V. in later reports.

**Re-review when:** conditions C1 and C2 are done (rerun V1 and V2 on the full files); the dataset revision or a licence changes; the preparation settings change; or later retrieval tests show unexplained misses on terms or products.

---

## Appendix A: Evidence Index

| Code | Evidence | Location |
|---|---|---|
| E1 | Lineage manifest and Part B record of each source and output | `data/week3_manifest.json` |
| E2 | Part C pipeline manifests (same hashes as Part B) | `data/pipeline_v1/json/pipeline_manifest.json`, `data/pipeline_v1/documents/pipeline_manifest.json` |
| E3 | Week 3 run evidence and notebook outputs (Cells 9 to 12, 18, 19) | `notebooks/week3_pipeline.ipynb`, `docs/week3_data_inventory.md` |
| E4 | Audit script output on the committed files (V1, V2 screen, ligatures, terms, samples) | `docs/week4_audit_checks.py` (run: `python docs/week4_audit_checks.py`) |

## Appendix B: Not Verified Items and the Smallest Next Check

| N.V. item | Smallest next check |
|---|---|
| Licence of S01 and S02 | Read the dataset authors' terms (dataset paper and project page) and record the answer in the inventory |
| CC BY version of S04 and S05 | Read the copyright note in each PDF |
| Reasons for the 5 excluded S01 records and 13 excluded S02 records | Print their IDs in the notebook and inspect them (they may be valid exceptions) |
| Reference integrity, review coverage, duplicates, contact details in review text (full files) | `python docs/week4_audit_checks.py --full-meta data/processed/prepared_meta.jsonl --full-reviews data/processed/prepared_reviews.jsonl` |
| Non-headphone share in the full S01 file | Take 50 random titles from the full file and judge them by hand |
| Accuracy of chunks against the PDFs | Compare 10 random chunks with the PDF pages |

## 9. Post-Audit FR7 Progress Note (21 November 2026)

This note supplements, and does not change, the 18 November audit results or its quality-gate decision. On 20 November, a separate student-authored [Headphone Technical Knowledge Base v1 (Grounded Draft)](../Headphone%20Technical%20Knowledge%20Base%20v1%20(Grounded%20Draft).md) was added to the project. Its progress record lists 80 grounded entries (Pass 1: 31; Pass 2: 49) and about 90 candidate terms still names-only, against a 150-250-entry target. The entries include impedance, driver types, ANC, distortion, and open-/closed-back designs. The draft flags EQ and other terms as unfinished and SBC/AAC primary-source specifications as not yet grounded.

This is progress on FR7 documentation, not a new result from the Week 3 ingestion pipeline. The audit finding that the existing 147 PDF chunks contain no impedance or driver coverage remains true for those chunks; the new draft is not represented in the manifests, has not been ingested, and was not audited by the checks in this report. Review the draft's source support, provenance, rights, privacy, and content before deciding whether to integrate it and rerun pipeline validation.
