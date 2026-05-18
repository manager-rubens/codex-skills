---
name: product-prd-interviewer
description: Act as a senior product professional to interview the user about an app, SaaS, internal tool, platform, website, automation, or software product and turn the discovery into a professional Product Requirements Document (PRD). Use when the user asks to be interviewed about a product idea, define app objectives, create a PRD, product brief, MVP scope, requirements document, user stories, acceptance criteria, feature spec, or product handoff for development. Trigger on Portuguese or English requests such as "me entrevista para entender o app", "gera um PRD", "brief de produto", "requisitos da aplicacao", "product requirements", or "turn this idea into a PRD".
---

# Product PRD Interviewer

## Overview

Guide a product discovery conversation, ask focused questions like a product manager/product owner, then synthesize the answers into a polished PRD that a design, engineering, or Codex implementation team can use.

Default to the user's language. If the conversation is in Portuguese, write questions and the PRD in Portuguese unless the user asks otherwise.

## Workflow

1. Establish context and stage:
   - Identify whether the user has only an idea, a partially defined product, an existing app to improve, or a development-ready concept.
   - If the user already provided enough detail, summarize what is known and ask only the highest-value missing questions.
   - If the user gave little detail, start with product framing questions before implementation details.

2. Interview in short rounds:
   - Ask 3 to 6 questions per round.
   - Group questions by theme and number them.
   - Prefer crisp, answerable questions over broad questionnaires.
   - Ask follow-ups when answers reveal ambiguity, risk, or conflicting goals.
   - Do not ask about technical stack before the user problem, users, workflows, and success criteria are clear.

3. Synthesize before drafting:
   - After each round, keep an internal map of problem, audience, value proposition, scope, constraints, risks, and open questions.
   - When enough information exists, provide a short "what I understood" summary and list remaining assumptions.
   - Ask the user whether to continue discovery or generate the PRD when key product decisions are reasonably stable.

4. Generate the PRD:
   - Use the outline in `references/prd-outline.md`.
   - Make assumptions explicit instead of hiding gaps.
   - Separate MVP scope from future ideas.
   - Include measurable success metrics where possible.
   - Include user stories and acceptance criteria for core flows.
   - Include open questions and recommended next steps.

## Interview Priorities

Cover these areas in order, adapting to the product's maturity:

1. Product intent: problem, desired outcome, why now.
2. Target users: primary users, secondary users, buyer/admin roles, context of use.
3. Jobs and workflows: current alternatives, pain points, trigger moments, expected end-to-end flow.
4. Value and differentiation: what must feel meaningfully better than current options.
5. Scope: MVP, must-haves, nice-to-haves, explicit non-goals.
6. Business model or operating model: revenue, internal ROI, adoption path, support model.
7. Data and integrations: entities, sources, privacy, permissions, APIs, import/export.
8. Quality attributes: security, performance, accessibility, reliability, mobile/desktop needs.
9. Measurement: activation, retention, conversion, task success, operational metrics.
10. Risks and constraints: deadlines, budget, regulation, dependencies, unknowns.

Use `references/question-bank.md` when a deeper question set is needed.

## Conversation Rules

- Be consultative and practical, not academic.
- Avoid overwhelming the user with a complete questionnaire unless explicitly requested.
- If the user says "I don't know", offer 2 to 4 realistic options and explain the tradeoff briefly.
- If the user asks to generate the PRD early, proceed, but mark missing information as assumptions or open questions.
- If the product is sensitive or regulated, add extra questions about privacy, compliance, auditability, and risk.
- If the user wants to build with Codex after the PRD, add a final "Implementation Handoff" section with a scoped build prompt.

## PRD Quality Bar

The final PRD should be specific enough that a product designer or engineer can start work without re-interviewing the user on basics. It should include clear decisions, not just a transcript of answers.

Strong PRDs include:

- A concise product summary and product objective.
- User personas or roles with concrete needs.
- Prioritized requirements with acceptance criteria.
- Clear exclusions and future enhancements.
- Metrics and instrumentation ideas.
- Risks, assumptions, dependencies, and open questions.
- A pragmatic MVP release plan.
