# Architecture Decisions — Product Compare Assistant (V1)

V1 is a conceptual architecture. Components are labelled by function; specific technologies will be selected in later topics.

## 1. Simplest Architecture and Gaps

Simplest flow: User Query → AI Application → Language Model Service → Response

This cannot satisfy the requirements alone. The model has no access to the 2023 product data, cannot cite sources, and has no control over scope or unsupported questions. The next section shows what is needed.

## 2. Architecture Needs from Requirements

| Requirement ID | What does the requirement need? | Architecture Response |
|---|---|---|
| FR1 / FR2 / NFR2 / NFR3 | Answers must come from product descriptions, reviews, and reference text, and candidates must be found for needs-based requests. | Knowledge Source and Knowledge Access (hybrid retrieval) |
| FR4 / RAI1 | Every claim must carry a verifiable source reference and be supported by evidence. | Source tracking and Grounding and Citation Check |
| FR5 / FR8 / RAI4 | Unsupported (price, stock) and out-of-scope (other categories, hearing health) queries must be refused and redirected. | Scope and Intent Control |
| FR6 | Follow-up questions must resolve to earlier products and answers. | Session Context |
| RAI2 | Opinions must show review counts and conflicting views. | Review evidence retrieved with its metadata (rating, count) |
| RAI3 | Correctness must be comparable across brand and review-volume groups. | Evaluation Points with stratified logging |
| NFR1 | Responses must meet the latency target. | Limited number of processing steps between components |

## 3. Architecture Decision Records

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| ADR1: Include knowledge access with hybrid retrieval | FR1, FR2, FR4, NFR2, NFR3, RAI1: answers must be grounded in the product data | Base model only; keyword search only; dense retrieval only; hybrid retrieval | Knowledge Access component using hybrid retrieval over a Knowledge Source | More complexity and tuning, but better grounding and a design that can be compared with baselines (O3). |
| ADR2: Include explicit scope and intent control | FR2, FR5, FR8, RAI4: out-of-scope and unsupported queries must be refused, and the two request modes must be recognised | Instruction in the prompt only; explicit control component | Explicit Scope and Intent Control before retrieval and generation | Possible false refusals and additional processing time. |
| ADR3: Include grounding and citation check before the response | FR4, RAI1: claims must be supported and cited | Prompt-based citation only; check after generation | Grounding and Citation Check on the generated answer | Extra latency and cost (NFR1, NFR4), but fewer unsupported claims. |
| ADR4: Include session-scoped conversation context | FR6: follow-up questions must work | Stateless queries; session-scoped context | Session Context kept only for the current conversation | More context handling and risk of carrying wrong context, but natural follow-ups; nothing persists after the session. |

## 4. Initial Requirements Traceability Matrix

| Objective | Requirement | Evaluation Criterion | Architecture Element | Later Evidence |
|---|---|---|---|---|
| O1 | FR1, FR2, FR3 / NFR2 | Answer correctness | Language Model Service; Knowledge Access | Planned: rubric scores on ES1 |
| O1 | FR6 | Follow-up handling | Session Context | Planned: multi-turn results on ES3 |
| O2 | NFR3 | Retrieval relevance | Knowledge Access; Knowledge Source | Planned: Recall@5 and MRR versus BM25 and dense baselines |
| O2 | FR4 / RAI1 | Source citation and support; claim faithfulness | Grounding and Citation Check | Planned: citation and faithfulness results on ES1 |
| O2 | FR5 / RAI4 | Refusal of unsupported and out-of-scope queries | Scope and Intent Control | Planned: refusal results on ES2 |
| O2 | RAI2 | Review attribution and balance | Knowledge Access (review metadata); Grounding and Citation Check | Planned: attribution results on ES4 |
| O3 | RAI3 | Coverage fairness | Evaluation Points | Planned: stratified correctness gap on ES5 |
| O3 | NFR1 | Response latency | End-to-end interaction path; Evaluation Points | Planned: p90 latency over the defined workload |

## 5. Final Review Checklist

- **Does each component support a requirement or evaluation need?** Yes. Section 2 maps each component to requirement IDs.
- **Is any important data source, safety control, or evaluation point missing?** The three data stores (metadata, reviews, reference documents), scope control, citation check, and evaluation points are all included. Monitoring and deployment controls are deferred to later topics.
- **Have I added any technology or component that is not yet justified?** No specific technologies are named, and each component traces to an ADR.
- **Is there a simpler architecture that could still satisfy the requirements?** Removing the scope control or the citation check would leave RAI4 and RAI1 without an enforcement point, so the current design is the simplest that meets them.
