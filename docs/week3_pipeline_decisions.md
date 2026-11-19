# Week 3 Pipeline Decisions: Product Compare Assistant

Version: 1.0 (Topic 3, Step C3)

Artefacts this file explains:
- Notebook: `notebooks/week3_pipeline.ipynb`
- Diagram: `docs/week3_pipeline_diagram.png`
- Inventory: `docs/week3_data_inventory.md`
- Part B output and manifest: `data/processed/`, `data/week3_manifest.json`
- Part C output and manifests: `data/pipeline_v1/json/`, `data/pipeline_v1/documents/`

## 1. Requirements and Sources Selected

| Requirement | What it needs from the data | Source |
| --- | --- | --- |
| FR1, FR2 (compare named headphones, find candidates for needs) | Product titles, features, descriptions, details | S01 |
| FR3, FR4 (suggestion with evidence, source references) | Stable IDs that can be cited (`parent_asin`, review `record_id`, paper DOI and page) | S01, S02, S03 |
| FR5 (decline price and stock questions) | Price is a 2023 snapshot and exists for few products, so it is stored as `price_2023_snapshot` and never presented as current | S01 |
| FR7 (explain technical terms) | Reference text that defines terms, with page numbers for citation | S04, S05 |
| RAI1 (grounding) | Every chunk carries its source, DOI, licence, and page | S03 to S05 |
| RAI2 (review bias) | Rating, helpful votes, verified purchase, and review counts | S02, S01 |
| RAI3 (coverage across brands and review volume) | Store (brand) and `rating_number` kept for every product | S01 |
| NFR3 (retrieval quality, later) | Clean text with known source IDs | S01 to S05 |
| NFR5 (maintainability) | A rerunnable pipeline that rebuilds outputs from raw sources | All |

The Topic 2 architecture element served is the **Knowledge Source** (three stores: product metadata, customer reviews, technical reference documents). Embedding and indexing happen in later topics.

## 2. Part B Comparison and Evidence

Each comparison uses the same input for both configurations. The numbers are in `docs/week3_run_evidence.md`.

### S01 product metadata (JSON pathway)

|                      | Config A                                                     | Config B                                                              |
| -------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| Rule                 | Required keys (`parent_asin`, `title`) present and not blank | Config A, and at least one non-blank `features` or `description` text |
| Records kept         | 56043                                                        | 44515                                                                 |
| Distinct stores kept | 10936                                                        | 8648                                                                  |

**Selected: Config A.** Config B would remove the products with the least descriptive text. Those products tend to come from smaller sellers, so removing them could make the assistant's coverage unfair across brands (RAI3), and we could no longer measure that gap. Config A keeps them and adds `has_features`, `has_description`, and `has_price` flags, so later steps can filter or report on them.
**Benefit:** coverage by brand stays measurable.
**Accepted limitation:** some prepared records have little text, so retrieval quality for them may be poor.

### S02 customer reviews (JSON pathway)

|                               | Config A                | Config B                                                                  |
| ----------------------------- | ----------------------- | ------------------------------------------------------------------------- |
| Rule                          | Text kept as downloaded | HTML tags removed and entities decoded; text must not be empty afterwards |
| Records kept                  | 39033                   | 39033                                                                     |
| Reviews with HTML tags        | 7529                    | 0 after cleaning                                                          |
| Average characters per review | 368.4                   | 361.4                                                                     |

**Selected: Config B.** Review text contains tags such as `<br />`, which would appear inside retrieved passages and answers.
**Benefit:** clean text for retrieval and citation.
**Accepted limitation:** the tag-removal rule may remove text that only looks like a tag, and a few reviews that contain only markup are dropped.

### S03 to S05 research papers (PDF pathway)

|                                               | Config A (lab baseline)                         | Config B                                                                                       |
| --------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Method                                        | Fixed 500-character chunks over the joined text | Whole sentences packed into chunks of about 800 characters (maximum 1,000), never across pages |
| Page numbers kept                             | No                                              | Yes                                                                                            |
| Average chunks that end at a sentence end     | 3.43%                                           | 87.67 %                                                                                        |
| Average chunks that start at a sentence start | 8.8%                                            | 90.37 %                                                                                        |

**Selected: Config B.** FR4 and RAI1 need a page-level citation, and fixed chunks cut sentences in half and lose pages. The lab's paragraph-aware splitter was not used because text extracted from these PDFs rarely has blank lines between paragraphs, so it behaves like fixed chunking.
**Benefit:** each answer can cite a paper and a page, and chunks read as complete sentences.
**Accepted limitation:** a sentence that runs across a page break is split, so some chunks start or end mid-sentence.

## 3. Chosen Preparation Configuration

| Setting | Value |
| --- | --- |
| S01 | Config A; keep text, rating, store, and category fields; parse `details` JSON; drop images, videos, `bought_together`, `subtitle`, `author`; add `has_*` flags |
| S02 | Config B; strip HTML; drop `user_id` and images; add UTC review date; `record_id` is a hash of product, timestamp, and original text |
| S03 to S05 | Config B; chunk target 800, maximum 1,000 characters; running headers removed (lines repeated on at least half the pages, with a safety limit of 15% of lines); reference list cut at the last "References" heading; S05 keeps only Section 1 (Introduction) and Section 6 (Sound Reproduction Applications) |
| Invalid records | Excluded and counted (policy `exclude`); the run stops if none remain |
| Reproducibility | Hugging Face revision `2b6d039ed471f2ba5fd2acb718bf33b0a7e5598e`, first 500,000 review rows, SHA-256 of every source and output |

## 4. Engineering Decisions

| Decision | Choice | Reason |
| --- | --- | --- |
| ETL or ELT | ELT-style: load the raw extract first and keep it in `data/raw/`, then transform into `data/processed/` | The same raw data is used to compare two configurations in Part B and to rerun the pipeline in Part C. Raw files stay local and uncommitted. |
| Batch or streaming | Batch | The data is a fixed 2023 snapshot and no real-time answer is needed. The review file is read as a stream only to build a bounded batch of 500,000 rows. |
| Why JSONL and not one JSON file | JSON Lines | The sources are line-delimited records, which can be read one record at a time without loading the whole file. |
| Privacy | `user_id` is dropped before anything is stored or shared | Review user IDs are pseudonymous but not needed for any requirement. |

## 5. Stage Contracts and Failure Responses

| Stage | Contract / evidence in this project | Failure response |
| --- | --- | --- |
| Ingest | The exact source file exists (selected by name, never by extension) | Stop for a missing input |
| Inspect | JSON: required keys and valid record count are reported. PDF: a text layer exists and the section markers are found | Stop and report. A scanned PDF needs OCR; a missing heading means the PDF rule must be fixed |
| Prepare | The chosen configuration produces records; invalid records are excluded and counted | Stop if no valid record or chunk remains |
| Validate | Output exists, is not empty, record count matches the read-back count, and the SHA-256 is recorded | Stop for a missing or empty output |
| Record lineage | Each source maps to its exact output in `week3_manifest.json` and in each `pipeline_manifest.json` | Stop and report a missing mapping or missing source details |

The repeatability check (Cell 18) reruns each pipeline and compares source fingerprints, output fingerprints, and mappings. Only timestamps are expected to differ.

## 6. Output Locations

| Output | Location | Committed to GitHub? |
| --- | --- | --- |
| Part B prepared S01 and S02 | `data/processed/prepared_meta.jsonl`, `data/processed/prepared_reviews.jsonl` | No (no stated licence); a 20-record sample of each is in `data/samples/` |
| Part B prepared S03 to S05 | `data/processed/prepared_text.jsonl` | Yes (open licence, credit kept in each record) |
| Part B lineage manifest | `data/week3_manifest.json` | Yes |
| Part C JSON pipeline | `data/pipeline_v1/json/` | Manifest only |
| Part C document pipeline | `data/pipeline_v1/documents/` | Yes |
| Run evidence | `docs/week3_run_evidence.md` | Yes |

The full prepared S01 and S02 files stay in the authorised working storage and can be rebuilt from the notebook.

