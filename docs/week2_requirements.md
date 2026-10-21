# Requirements Specification — Product Compare Assistant
Version: 1.0

> Thresholds are initial targets based on intended use. They are illustrative where marked and will be revised after baseline testing. "Defined evaluation set" refers to the sets described in `docs/week2_evaluation_criteria.md`.

## Section 1: Functional Requirements

| # | Requirement — The system SHALL | Scope Boundary — SHALL NOT (where relevant) |
|---|---|---|
| FR1 | Compare two or more headphones named by the user, covering their features, specifications, and review-based strengths and weaknesses. | Compare or describe products that are not in the source documents as if they were supported, or invent specifications. |
| FR2 | Accept a description of the user's needs (e.g., use case, preferred features) and identify candidate headphones from the source documents that match, then compare them. | Present candidates that cannot be traced to the source documents. |
| FR3 | Provide a suggestion for the user's stated needs, accompanied by the supporting evidence and the trade-offs between the options. | Give a suggestion without supporting evidence, or present it as definitive when the evidence is conflicting or insufficient. |
| FR4 | Provide a source reference (product identifier, review, or reference document) for each factual claim in a comparison or suggestion. | Present unsupported information as if it came from a source. |
| FR5 | State when the available evidence is insufficient or conflicting, and decline to guess. | State current price, stock, or availability, or provide purchase links, based on the 2023 data snapshot. |
| FR6 | Support follow-up questions that refer to products or answers earlier in the same conversation (e.g., "what about its battery life?"). | Use or retain conversation content from other users or after the session ends. |
| FR7 | Present comparisons in plain language and explain technical terms (e.g., noise cancelling, codecs, impedance) when they matter to the comparison. | Assume the user has technical expertise. |
| FR8 | Decline queries outside headphone product comparison (e.g., other product categories, general chat) and redirect the user to the supported scope. | Provide medical or hearing-health advice (e.g., treating hearing loss or tinnitus). |

## Section 2: Non-Functional Requirements

| # | Quality Attribute | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| NFR1 | Performance | The system shall return a complete response within the agreed latency target. | Measure end-to-end latency on a defined workload of at least 50 queries covering both comparison modes and follow-ups. | p90 latency | < 8,000 ms |
| NFR2 | Correctness | Answers shall be factually consistent with the source documents. | Score a curated evaluation set of supported queries using a defined rubric. | Correct response rate (%) | ≥ 80% |
| NFR3 | Correctness (retrieval) | The system shall retrieve the relevant evidence for a query. | Run labelled retrieval queries and compare against BM25-only and dense-only baselines. | Recall@5; MRR | Recall@5 ≥ 0.80; MRR higher than both baselines |
| NFR4 | Cost | Inference cost shall remain within the project budget. | Record model/API usage over the evaluation workload. | Cost per 100 queries | < US$1.00 per 100 queries (illustrative) |
| NFR5 | Maintainability | New product records and reference documents shall be incorporated without rebuilding unrelated components. | Run a controlled update test adding a batch of 100 new product records. | Update time | < 15 min |
| NFR6 | Reliability | The system shall return a complete response or a defined refusal for every query without unhandled errors. | Run the full evaluation workload and log failures. | Successful response rate (%) | ≥ 99% |

## Section 3: Responsible AI Requirements

| # | Responsible AI Risk | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| RAI1 | Hallucination / Grounding | Every factual claim shall be supported by a retrieved source, with a verifiable reference, and unsupported claims shall not be presented as fact. | Check responses to the defined evaluation set for citation presence, whether each cited source supports the claim, and claim-level support. | Citation presence rate; citation-source match rate; supported-claim rate | 100% presence; ≥ 95% match; ≥ 90% supported claims |
| RAI2 | Review bias and manipulation | Opinions drawn from reviews shall be attributed to reviews with the number of reviews, and conflicting views shall be shown rather than a single verdict. | Run a test set of at least 20 products with mixed reviews and inspect responses for attribution, review counts, and both positive and negative points where present. | Attribution-and-balance rate | ≥ 90% |
| RAI3 | Fairness / Unequal coverage | Correctness shall not differ beyond the agreed tolerance across brand and review-volume groups. | Evaluate a stratified test set (high-volume vs low-volume products, major vs minor brands) and compare correctness rates. | Absolute correctness-rate gap between groups | ≤ 10 percentage points |
| RAI4 | Stale data / Safety and scope | The system shall refuse price, stock, availability, hearing-health, and other out-of-scope queries and redirect the user appropriately. | Run a safety/scope test set containing at least 30 such queries. | Refusal-and-redirect success rate | ≥ 95% |
