# Data Inventory: Product Compare Assistant

Version: 1.1 (Week 3, Step A4)

Evidence in section 4 comes from the Colab notebook `ai_engineering_product_compare_assistant_notebook.ipynb`.

## 1. Source Table

| Source ID | Filename / URL                                                                                                                                                                                                                                                                                                                                                 | Type and purpose                                                                                                                                                                                                | Version / date / owner                                                                                                                                                                                                                                    | Access / rights                                                                                                                                                                          | Inspection evidence |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| S01       | Hugging Face config `raw_meta_Electronics`. Listed on https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023                                                                                                                                                                                                                                          | JSON Lines, semi-structured. Item metadata: title, features, description, details, average rating, price. We keep only headphones. Needed for FR1, FR2, FR4, FR5, NFR2, NFR3.                                   | Amazon Reviews 2023. Collected in 2023 (reviews run to Sep 2023). Owner: McAuley Lab, UC San Diego. Hub revision `2b6d039ed471f2ba5fd2acb718bf33b0a7e5598e`, last modified on the Hub 8 Dec 2024. Downloaded: 18/10/2026. Checked in notebook: 3/11/2026. | Public, no login. No licence is stated on the dataset card (checked 2/11/2026). Cite Hou et al. (2024), arXiv:2403.03952. Used for coursework only. Raw file is not committed to GitHub. | See Evidence S01    |
| S02       | Hugging Face config `raw_review_Electronics`, same dataset page as S01. Streamed, not downloaded in full.                                                                                                                                                                                                                                                      | JSON Lines, semi-structured. Customer reviews: rating, title, text, helpful votes, verified purchase, product ID, timestamp. We keep reviews of headphones only. Needed for FR1, FR3, FR4, RAI2, RAI3.          | Same release, owner, and revision as S01. First 500,000 rows streamed on 3/11/2026.                                                                                                                                                                       | Same rights as S01. Review text was written by Amazon customers. `user_id` is a pseudonymous ID and is dropped from prepared data.                                                       | See Evidence S02    |
| S03       | Lee, E. M., Subramaniam, C., & Park, S. (2025). Perceived risk and fashion on the intention to adopt wireless earbuds in the United States using a partial least squares-structural equation modeling approach: Empirical study. _JMIR Formative Research, 9_, e56887. https://doi.org/10.2196/56887. Local copy: `data/raw/s03_lee_2025_wireless_earbuds.pdf` | PDF journal article. Survey of 205 US respondents on what influences earbud purchase (comfort, fashionability, perceived health risk). Needed for FR2 and FR3.                                                  | Published 19 Jun 2025. Owner: the authors; publisher JMIR Publications. Downloaded: 3/11/2026                                                                                                                                                             | Open access. Creative Commons Attribution (CC BY 4.0), per the article page footer (checked 4/11/2026). Reuse with credit. Raw PDF not committed.                                        | See Evidence S03    |
| S04       | Gutierrez-Parera, P., & Lopez, J. J. (2016). Influence of the quality of consumer headphones in the perception of spatial audio. _Applied Sciences, 6_(4), 117. https://doi.org/10.3390/app6040117. Local copy: `data/raw/s04_gutierrez_parera_2016_headphone_quality.pdf`                                                                                     | PDF journal article. Listening tests on how frequency response, distortion, and left-right sensitivity differences affect perceived quality. Needed for FR7 (terms) and FR3 (why headphones differ in quality). | Published 22 Apr 2016. Owner: the authors; publisher MDPI. Downloaded: 4/11/2026                                                                                                                                                                          | Open access. Creative Commons Attribution (CC BY 4.0), per the article page footer (checked 4/11/2026). Reuse with credit. Raw PDF not committed.                                        | See Evidence S04    |
| S05       | Välimäki, V., & Reiss, J. D. (2016). All about audio equalization: Solutions and frontiers. _Applied Sciences, 6_(5), 129. https://doi.org/10.3390/app6050129. Local copy: `data/raw/s05_valimaki_reiss_2016_equalization.pdf`                                                                                                                                 | PDF review article (46 pages, mostly signal processing). We use only the sections on tone controls, headphone equalization, and noise. Needed for FR7.                                                          | Published 6 May 2016. Owner: the authors; publisher MDPI. Downloaded: 4/11/2026                                                                                                                                                                           | Open access. Creative Commons Attribution (CC BY 4.0), per the article page footer (checked 4/11/2026).  Reuse with credit. Raw PDF not committed.                                       | See Evidence S05    |

## 2. Raw and Prepared Storage

| Source ID | Raw location (not committed)                                     | Prepared output                                                                                                                                                                                                                                      | Preparation method                                                                                                            |
| --------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| S01       | `data/raw/meta_Electronics.jsonl.gz` (or the Hugging Face cache) | `data/processed/prepared_meta.jsonl`: one record per headphone product with `parent_asin`, title, features, description, details, average rating, rating count, store, and the subtype (the fourth category level). Images and videos are dropped. | JSON/API export pathway. Filter with `categories[2] == "Headphones & Earbuds"`, keep text fields, and record the product IDs. |
| S02       | Streamed from Hugging Face; no raw copy.                         | `data/processed/prepared_reviews.jsonl`: `parent_asin`, rating, title, text, helpful votes, verified purchase, timestamp. `user_id` and images are dropped. HTML tags such as `<br />` are removed from text.                                      | JSON/API export pathway. Stream the file and keep reviews whose `parent_asin` is in the S01 headphone list.                   |
| S03       | `data/raw/s03_lee_2025_wireless_earbuds.pdf`                     | `data/processed/s03_pages.jsonl`: one record per page with page number, DOI, licence, and text. The reference list is dropped.                                                                                                                       | PDF/TXT pathway. Extract text page by page and keep page numbers so answers can cite them.                                    |
| S04       | `data/raw/s04_gutierrez_parera_2016_headphone_quality.pdf`       | `data/processed/s04_pages.jsonl`: same format as S03.                                                                                                                                                                                                | PDF/TXT pathway. Same as S03.                                                                                                 |
| S05       | `data/raw/s05_valimaki_reiss_2016_equalization.pdf`              | `data/processed/s05_pages.jsonl`: same format, but only the pages for the sections listed in the open issues.                                                                                                                                        | PDF/TXT pathway. Extract text, then keep the selected sections only.                                                          |


## 3. Checkpoint A: Which Requirement Needs Which Source

|Requirement|What it needs from the data|Source|
|---|---|---|
|FR1, FR2 (compare named headphones, find candidates for needs)|Product titles, features, descriptions, details|S01|
|FR2, FR3 (needs-based matching, suggestion with trade-offs)|Evidence on what buyers care about (comfort, fashion, perceived risk)|S02, S03|
|FR3, FR4 (suggestion with evidence, source references)|Product IDs and review IDs that can be cited|S01, S02|
|FR5 (decline price and stock questions)|The data is a 2023 snapshot; price exists for only about 22% of products|S01|
|FR7 (explain technical terms)|Reference text that defines terms (frequency response, distortion, open and closed designs, equalization, bass and treble, noise isolation)|S04, S05|
|RAI2 (review bias, conflicting views)|Ratings, helpful votes, review counts|S02|
|RAI3 (coverage across brands and review volume)|Brand (store) and review counts per product|S01, S02|
|NFR3 (retrieval quality)|Text to retrieve over, with known source IDs|S01 to S05|

## 4. Inspection Evidence

### Evidence S01

- Method: `datasets` 3.6.0, `load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_Electronics", trust_remote_code=True)`.
- Hub revision: `2b6d039ed471f2ba5fd2acb718bf33b0a7e5598e`. Last modified on the Hub: 2024-12-08 22:21 UTC. Checked: 2026-11-03 21:29 UTC.
- Rows: 1,610,012.
- Columns: `main_category`, `title`, `average_rating`, `rating_number`, `features`, `description`, `price`, `images`, `videos`, `store`, `categories`, `details`, `parent_asin`, `bought_together`, `subtitle`, `author`.
- Filter rules compared:

|Rule|Products|
|---|---|
|Title contains "headphone"|69,543|
|Any category contains "headphone"|102,057|
|Both rules|51,272|
|Title only|18,271|
|Category only|50,785|

- The title-only matches are mostly accessories (cables, adapters, amplifiers, record players), so the title rule is not used.
- The broad category rule also includes accessories (adapters 5,146; ear pads 4,940; cases 2,840; extension cords 1,556), so it is not used either. 7,348 title matches have an empty category path.
- **Category rule chosen:** `categories[2] == "Headphones & Earbuds"`.
- Result: 56,048 products, all with a distinct `parent_asin`.

|Subtype (fourth category level)|Products|
|---|---|
|Earbud Headphones|37,403|
|Over-Ear Headphones|8,951|
|(no subtype)|5,663|
|On-Ear Headphones|3,804|
|Open-Ear Headphones|227|

- Compared with the title rule: 35,273 title matches are inside the branch, 34,270 are outside, and 20,775 branch products have no "headphone" in the title.
- Field coverage on the 56,048 products: title, average rating, rating count, categories, details, and `parent_asin` 100%; store 99.6%; main category 93.8%; features 75.3%; description 56.8%; price 22.2%; subtitle 0.2%; `bought_together` and `author` 0%. `images` and `videos` show 100% only because empty containers count as filled, so ignore them.
- Sample record (shortened):

```json
{
  "main_category": "All Electronics",
  "title": "MXditect EB166 Headphones with Mic Stereo Earphones for iOS Android Windows System, Black",
  "average_rating": 3.3,
  "rating_number": 69,
  "features": ["Equipped with two high quality drivers, create dynamic stereo sound and strong deep bass", "Tangle-free audio cord, helps you get rid of messy tangle effectively", "..."],
  "description": ["Parameters: Package Size: 3.35 x 3.35 x 0.98 inches. Net Weight: 0.58 ounces. ... Frequency Range: 20Hz-20 kHz. ...[cut]"],
  "price": "None",
  "store": "MXditect",
  "categories": ["Electronics", "Headphones, Earbuds & Accessories", "Headphones & Earbuds", "Earbud Headphones"],
  "details": "{\"Product Dimensions\": \"3.35 x 3.35 x 0.98 inches\", \"Item Weight\": \"0.04 Pounds\", \"Item model number\": \"EB166\", ...[cut]}",
  "parent_asin": "B06XJHRP5G"
}
```

### Evidence S02

- Method: `load_dataset(..., "raw_review_Electronics", split="full", streaming=True)`, first 500,000 rows scanned.
- Reviews of the 56,048 headphone products found in the scan: 39,046 (about 7.8% of rows scanned).
- Fields: `rating`, `asin`, `parent_asin`, `user_id`, `timestamp`, `helpful_vote`, `verified_purchase`, `title`, `text` all 100%; `images` 4.3%.
- Sample reviews (shortened, `user_id` removed):

```json
[
  {"rating": 5.0, "title": "Excellent!", "text": "I love these. They even come with a carry case and several sizes of ear bud inserts. ...[cut]", "asin": "B01G8JO5F2", "parent_asin": "B01G8JO5F2", "timestamp": 1523093017534, "helpful_vote": 0, "verified_purchase": true},
  {"rating": 5.0, "title": "Best Headphones in the Fifties price range!", "text": "I've bought these headphones three times because I love them so much ...[cut]", "asin": "B013J7WUGC", "parent_asin": "B07CJYMRWM", "timestamp": 1676601581238, "helpful_vote": 0, "verified_purchase": true},
  {"rating": 5.0, "title": "solid sound for the price", "text": "Update 2-they sent a new warranty replacement. Good company.<br />Update- was 5 star until ...[cut]", "asin": "B07BHHB5RH", "parent_asin": "B07BHHB5RH", "timestamp": 1565130879386, "helpful_vote": 0, "verified_purchase": true}
]
```

- Observations: the second sample has different `asin` and `parent_asin` values; text contains `<br />` tags.

### Evidence S03

- Downloaded file name: `Perceived_Risk_and_Fashion_on_.pdf` (1,086 KB).
- SHA-256: `8d7622a8d0627d1d27fb53f9252f44259d27c6a04d686d952256105c96da309d`
- Pages: 11. Pages with extractable text: 11.
- Text sample (first 300 characters): "Original Paper Perceived Risk and Fashion on the Intention to Adopt Wireless Earbuds in the United States Using a Partial Least Squares-Structural Equation Modeling Approach: Empirical Study Edward M Lee1*, DBA; Chandrasekar Subramaniam2*, PhD; Sungjune Park2*, PhD 1Bank of America, Charlotte, NC, U"

### Evidence S04

- Downloaded file name: `applsci-06-00117-v3.pdf` (1,309 KB).
- SHA-256: `c9efada9bbd3b891a092dc306e589fba1221441b0a018b95956473dbb26a4e7c`
- Pages: 18. Pages with extractable text: 18.
- Text sample (first 300 characters): "applied sciences Article Influence of the Quality of Consumer Headphones in the Perception of Spatial Audio Pablo Gutierrez-Parera * and Jose J. Lopez Institute of Telecommunications and Multimedia Applications (ITEAM), Universitat Politècnica de València, Valencia 46022, Spain; jjlopez@dcom.upv.e"

### Evidence S05

- Downloaded file name: `applsci-06-00129.pdf` (1,883 KB).
- SHA-256: `06653abb3403cbd5a3c1bad8c69f93c72ef956b9259b6af8cde26afe9b3e9e51`
- Pages: 46. Pages with extractable text: 46.
- Text sample (first 300 characters): "applied sciences Review All About Audio Equalization: Solutions and Frontiers Vesa Välimäki 1,* and Joshua D. Reiss 2 1 Department of Signal Processing and Acoustics, Aalto University, Espoo 02150, Finland 2 Centre for Digital Music, Queen Mary University London, London E1 4NS, UK; joshua.reiss@q"

## 5. FR7 Supplementary Knowledge-Base Progress (21 November 2026)

The separately authored [Headphone Technical Knowledge Base v1 (Grounded Draft)](../Headphone%20Technical%20Knowledge%20Base%20v1%20(Grounded%20Draft).md) was prepared on 20 November to extend plain-language FR7 coverage. Its current progress record states 80 grounded entries (Pass 1: 31; Pass 2: 49) and about 90 additional candidate terms listed by name only, against a 150-250-entry target. Entries are paraphrased from the draft's cited sources; they are not extracted from the Week 3 PDFs alone.

This draft is supplementary documentation, not a new S06 source and not an input to `week3_manifest.json` or either `pipeline_v1` manifest. It has not yet been ingested, independently audited, or approved for retrieval. The Week 3 PDF-corpus finding that no chunk covers impedance or drivers remains accurate for that corpus, even though the separate draft now contains entries on those terms. Continue batch-by-batch drafting and source checking; decide on corpus hygiene, provenance/rights, stable record IDs, and validation before integrating it into a future pipeline run.
