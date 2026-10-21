# Evaluation Criteria — Product Compare Assistant

Flow: Objective / Requirement → Evaluation Criterion → Measurement Method → Metric → Threshold → User / Business Outcome

Objectives (from `docs/week1_project_scope.md`):
- **O1:** Design a document-grounded product comparison assistant for the headphones subcategory.
- **O2:** Develop it with hybrid retrieval, citation, and refusal guardrails.
- **O3:** Evaluate it on retrieval quality, faithfulness and citation accuracy, refusal correctness, and latency, against BM25-only and dense-only baselines.

## Evaluation Sets (to be built in later weeks)

| Set | Contents | Minimum size |
|---|---|---|
| ES1: Supported queries | Questions with reference answers and marked source passages: 20 name-based comparisons, 20 needs-based requests, 20 spec or term questions | 60 |
| ES2: Scope and safety | Price, stock, availability, hearing-health, and out-of-scope queries | 30 |
| ES3: Multi-turn dialogues | Two- or three-turn conversations with follow-up references | 20 |
| ES4: Mixed-review products | Products with both positive and negative reviews | 20 products |
| ES5: Stratified set | ES1 queries tagged by brand size and review volume | Subset of ES1 |

## Evaluation Criteria Table

| Objective / Requirement ID | Evaluation Criterion | Capability Bucket | Measurement Method | Metric | Threshold | User / Business Outcome |
|---|---|---|---|---|---|---|
| O3 / NFR2 | Answer correctness | Domain-specific capability | Score ES1 responses against reference answers using a defined rubric. | Correct response rate | ≥ 80% | Shoppers receive sufficiently reliable product information for routine comparisons. |
| O2 / NFR3 | Retrieval relevance | Domain-specific capability | Run labelled queries from ES1 and compare hybrid retrieval with BM25-only and dense-only baselines. | Recall@5; MRR | Recall@5 ≥ 0.80; MRR higher than both baselines | The right products and reviews reach the answer, and the hybrid design is justified by evidence. |
| O2 / FR4 / RAI1 | Source citation and support | Instruction-following capability | Inspect ES1 responses for citation presence and check whether each cited source supports the claim. | Citation presence rate; citation-source match rate | 100% presence; ≥ 95% match | Shoppers can verify every claim against the original listing or review. |
| O2 / RAI1 | Claim faithfulness | Generation capability | Break ES1 responses into claims and check each against retrieved evidence. | Supported-claim rate | ≥ 90% | Reduces wrong purchases caused by invented or misstated specifications. |
| O2 / FR5 / RAI4 | Refusal of unsupported and out-of-scope queries | Instruction-following capability | Run ES2 and record whether each query is refused and redirected. | Refusal-and-redirect success rate | ≥ 95% | Shoppers are not misled about current price or stock, and receive no hearing-health advice. |
| O2 / RAI2 | Review attribution and balance | Generation capability | Inspect ES4 responses for attribution to reviews, review counts, and both sides of conflicting opinions. | Attribution-and-balance rate | ≥ 90% | Shoppers see how much opinion supports each claim rather than a single biased verdict. |
| O1 / FR6 | Follow-up handling | Instruction-following capability | Run ES3 dialogues and check that follow-up questions are resolved to the correct earlier product or answer. | Context-resolution success rate | ≥ 85% | Shoppers can refine a comparison naturally without repeating themselves. |
| O3 / RAI3 | Coverage fairness | Domain-specific capability | Compare correctness on ES5 across brand and review-volume groups. | Absolute correctness-rate gap | ≤ 10 percentage points | Shoppers get similar answer quality for popular and less popular products. |
| O3 / NFR1 | Response latency | Cost and latency | Measure end-to-end response time across a defined workload of at least 50 queries. | p90 latency | < 8 s | Shoppers receive a sufficiently responsive interaction. |

