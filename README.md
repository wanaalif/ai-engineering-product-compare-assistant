# Product Compare Assistant

> A RAG-based assistant that helps online shoppers compare similar headphones by retrieving evidence from product descriptions, customer reviews, and technical reference documents and generating explainable, source-cited comparisons.

## Problem Statement
The growth of e-commerce has given consumers many alternatives, but product specifications, descriptions, and reviews are spread across separate pages and formats, so shoppers must manually collect and synthesise information to find meaningful differences between similar products such as headphones. Search and filtering tools narrow the choices but cannot answer natural-language comparison questions with contextual explanations. This project applies AI engineering, specifically retrieval-augmented generation with citation and refusal guardrails, to retrieve evidence from product documents, generate explainable comparisons, and ground every answer in retrieved sources to improve transparency and reliability.

## Evidence of the Problem
- Online shoppers rely heavily on product information when making decisions. Amsl, S., Watson, I., Teller, C., & Wood, S. (2023). Presenting products on websites – the importance of information quality criteria for online shoppers. *International Journal of Retail & Distribution Management, 51*(9/10). https://doi.org/10.1108/ijrdm-04-2023-0266
- Explaining the differences between similar products is a recognised challenge in online shopping that motivates research on automatically generated comparisons. Vedula, N., Collins, M. D., Agichtein, E., & Rokhlenko, O. (2023). Generating explainable product comparisons for online shopping. https://doi.org/10.1145/3539597.3570489

## Initial Related Work / Existing Approaches
- **Alexa for Shopping (Amazon).** Amazon Staff. (2026, May 13). Alexa for Shopping: Amazon's AI assistant for personalized shopping. *About Amazon*. https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant. Key limitation: proprietary and closed; the system cannot be independently reproduced or objectively evaluated by researchers.
- **Product question answering survey.** Deng, Y., Zhang, W., Yu, Q., & Lam, W. (2023). Product question answering in e-commerce: A survey. *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 11951–11964. https://doi.org/10.18653/v1/2023.acl-long.667. Key limitation: existing product QA methods struggle with answer reliability and trustworthiness, and generation-based methods suffer from hallucination.
- **Meaningful answer generation for e-commerce QA.** Gao, S., Chen, X., Ren, Z., Zhao, D., & Yan, R. (2021). Meaningful answer generation of e-commerce question-answering. *ACM Transactions on Information Systems, 39*(2), 1–26. https://doi.org/10.1145/3432689. Key limitation: focuses on single-product QA rather than product comparison, with no explicit evidence attribution or citations.

## Project Objectives
- O1: To design a document-grounded AI product comparison assistant for the headphones subcategory of consumer electronics, based on public product metadata, customer reviews, and supporting technical reference documents.
- O2: To develop the assistant with hybrid retrieval (keyword plus dense), citation of source products and documents, and guardrails that refuse questions the data cannot support (e.g., current price or stock).
- O3: To evaluate the assistant on retrieval quality, answer faithfulness and citation accuracy, refusal correctness, and latency, against BM25-only and dense-only baselines.

## Target Users
Online shoppers comparing similar headphones, particularly those who are not technical experts and want plain-language differences backed by evidence.

## Data Sources
- Source 1: Amazon Reviews 2023, product metadata (descriptions, features, details) for the headphones subcategory. URL: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Source 2: Amazon Reviews 2023, user reviews (ratings, text, helpfulness votes) for the same subcategory. URL: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Source 3: Olive, S. E. (2021). The perception and measurement of headphone sound quality: What do listeners prefer? *Acoustics Today, 18*(1), 58. URL: https://doi.org/10.1121/at.2022.18.1.58
- Source 4: Cotton, D. (2021). Headphone essentials 3: Basics of headphone types and tech (Version 1.31). Daystar Visions. URL: http://daystarvisions.com/Music/HE3-Basics_of_Headphone_Types_and_Tech.pdf

## Weekly Progress
| Week | Focus | Deliverable | Status |
|------|-------|-------------|--------|
| W1 | System map + project scope | README + docs | ✅ |
