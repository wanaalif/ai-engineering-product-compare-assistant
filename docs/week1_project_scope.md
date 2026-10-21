# Week 1 Project Scope: Product Compare Assistant


| Field            | Content                                        |
| ---------------- | ---------------------------------------------- |
| **Project Name** | Product Compare Assistant                      |
| **Domain**       | E-commerce / Consumer Electronics (Headphones) |

## Problem Statement

The rapid growth of e-commerce platforms has provided consumers with many product alternatives, increasing the effort required to compare products and identify meaningful differences between them (Vedula et al., 2023).
Product specifications, descriptions, and customer reviews are often distributed across separate pages and presented in different formats, requiring users to manually collect and synthesize information.
Existing search and filtering tools help user narrow product selections but do not provide contextual explanations that answer natural-language comparison questions (Vedula et al., 2023).
This project applies AI engineering, specifically retrieval-augmented generation with citation and refusal guardrails, to retrieve evidence from product documents, generate explainable comparisons, and ground every answer in retrieved sources to improve transparency and reliability.


## Evidence of the Problem

|                |                                                                                                                                                                                                                                                                            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Evidence 1** | Amsl, S., Watson, I., Teller, C., & Wood, S. (2023). Presenting products on websites – the importance of information quality criteria for online shoppers. International Journal of Retail & Distribution Management, 51(9/10). https://doi.org/10.1108/ijrdm-04-2023-0266 |
| **Evidence 2** | Vedula, Collins, M. D, Agichtein, E., & Oleg Rokhlenko. (2023). Generating explainable product comparisons for online shopping. https://doi.org/10.1145/3539597.3570489                                                                                                    |


## Initial Related Work

|                        |                                                                                                                                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Study / solution 1** | RTINGS headphone reviews and Compare tool                                                                                                                                                                                                                                          |
| Source / citation      | RTINGS.com. (n.d.). _How we test headphones_. https://www.rtings.com/headphones/learn/how-we-test                                                                                                                                                                                  |
| Key limitation         | Comparisons cover only the products RTINGS chooses to buy and test, and rely on lab measurements, scores, and graphs that shoppers must interpret themselves. The site acknowledges that one sound target does not suit every listener. No natural-language needs-based Q&A found. |
| **Study / solution 2** | Versus.com product comparison platform                                                                                                                                                                                                                                             |
| Source / citation      | Versus \| compare anything, from smartphones to cities_. (n.d.). Versus. Retrieved October 21, 2026, from https://versus.com/en                                                                                                                                                    |
| Key limitation         | Structured, specification-based comparison across many product categories, not designed to answer natural-language needs-based questions with cited review evidence.                                                                                                               |
| **Study / solution 3** | Explainable product comparison generation                                                                                                                                                                                                                                          |
| Source / citation      | Vedula, Collins, M. D, Agichtein, E., & Oleg Rokhlenko. (2023). Generating explainable product comparisons for online shopping. https://doi.org/10.1145/3539597.3570489                                                                                                            |
| Key limitation         | Non-personalized to a shopper's specific needs; Users cannot ask goal-oriented questions because the comparisons are primarily attribute-driven.                                                                                                                                   |
| **Study / solution 4** | Alexa for Shopping agentic AI assistant on Amazon                                                                                                                                                                                                                                  |
| Source / citation      | Amazon Staff. (2026, May 13). _Alexa for Shopping: Amazon's AI assistant for personalized shopping_. About Amazon. https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant                                                                                         |
| Key limitation         | Proprietary and closed; the system cannot be independently reproduced or objectively evaluated by researchers.                                                                                                                                                                     |
| **Study / solution 5** | Product question answering in e-commerce: A survey                                                                                                                                                                                                                                 |
| Source / citation      | Deng, Y., Zhang, W., Yu, Q., & Lam, W. (2023). Product question answering in e-commerce: A survey. _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, 11951–11964. https://doi.org/10.18653/v1/2023.acl-long.667   |
| Key limitation         | Existing PQA struggles with answer reliability and trustworthiness; generation-based methods suffer from hallucination.                                                                                                                                                            |

## Engineering Gap / Limitation

**Gap:** Existing headphone comparison tools rely on structured specifications, lab measurements, or editor-chosen comparisons and are not conversational, while commercial and research assistants are closed or not openly reproducible. As far as reviewed, none combine natural-language needs-based headphone comparison with cited customer-review evidence, refusal of unsupported questions, and open evaluation against baselines.

## Initial Project Objectives

- **O1:** To design a document-grounded AI product comparison assistant for the headphones subcategory of consumer electronics, based on public product metadata, customer reviews, and supporting technical reference documents.
- **O2:** To develop the assistant with hybrid retrieval (keyword plus dense), citation of source products and documents, and guardrails that refuse questions the data cannot support (e.g., current price or stock)
- **O3:** To evaluate the assistant on retrieval quality, answer faithfulness and citation accuracy, refusal correctness, and latency, against BM25-only and dense-only baselines.

## Target Users

Online shoppers comparing similar headphones, particularly those who are not technical experts and want plain-language differences backed by evidence.

## Data Sources

|              |                                                                                                                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source 1** | Amazon Reviews 2023, product metadata (descriptions, features, details; price is a 2023 snapshot field and is not used as current pricing) for the headphones subcategory. URL: [McAuley-Lab/Amazon-Reviews-2023 · Datasets at Hugging Face](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) |
| **Source 2** | Amazon Reviews 2023, user reviews (ratings, text, helpfulness votes, etc.) for the same headphones subcategory. Same URL as Source 1.                                                                                                                                                                         |
| **Source 3** | Olive, S. E. (2021). The perception and measurement of headphone sound quality: What do listeners prefer? _Acoustics Today_, _18_(1), 58. [https://doi.org/10.1121/at.2022.18.1.58](https://doi.org/10.1121/at.2022.18.1.58)                                                                                  |
| **Source 4** | Cotton, D. (2021). _Headphone essentials 3: Basics of headphone types and tech_ (Version 1.31). Daystar Visions. [http://daystarvisions.com/Music/HE3-Basics_of_Headphone_Types_and_Tech.pdf](http://daystarvisions.com/Music/HE3-Basics_of_Headphone_Types_and_Tech.pdf)                                     |


## Similar to EduAdvisor

Document-grounded Q&A using RAG; answers cite official or source passages; guardrails and refusal for out-of-scope questions; evaluation of answer quality, groundedness, latency, and safety.

## Different from EduAdvisor

- Semi-structured product data (metadata fields plus free-text reviews) instead of policy PDFs.
- Multi-item comparison: the assistant must retrieve and contrast several products, not look up one rule.
- Review text can be subjective, conflicting, or manipulated, so evidence must be weighed and attributed.
- Data is a 2023 snapshot, so the assistant must refuse current price and stock questions.
- Possible extension toward agentic behaviour (e.g., a comparison tool) in later topics.
- Domain-specific vocabulary (e.g., noise cancelling, codecs) needs technical reference documents so the assistant can explain terms in plain language.

## Responsible AI Risks

- **Risk 1: Hallucination.** The model invents or misstates a specification or compatibility claim, leading to a wrong purchase. _Control:_ answer only from retrieved passages, show source product IDs, refuse when evidence is missing.
- **Risk 2: Review bias and manipulation.** Fake, promotional, or skewed reviews distort the comparison. _Control:_ attribute opinions to reviews, report review counts, and show conflicting views rather than a single verdict.
- **Risk 3: Unfair coverage and stale data.** Some brands or subcategories have far more data than others, and 2023 data may be outdated. _Control:_ report coverage per brand, state the data date, and decline price or availability questions.
