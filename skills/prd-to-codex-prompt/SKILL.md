---
name: prd-to-codex-prompt
description: Create a clear, complete initial prompt for OpenAI Codex from a Product Requirements Document (PRD). Use when the user wants to turn a PRD, product spec, feature brief, ticket, or requirements document into a Codex-ready prompt for implementation, refactoring, debugging, review, testing, or planning. The skill must require the user to provide or attach a PRD before drafting the prompt.
---

# PRD to Codex Prompt

## Overview

Generate an initial OpenAI Codex prompt that is understandable, complete, actionable, and faithful to the user's PRD. Do not produce the Codex prompt until a PRD has been provided in the conversation or as an attached/local file.

## Required PRD Gate

Before drafting any prompt, verify that a PRD is available.

- If no PRD is present, ask the user to paste or attach the PRD. Stop there.
- If the user gives only a vague idea, roadmap item, or one-line feature request, ask for a PRD or a PRD-like brief with goals, scope, requirements, constraints, and acceptance criteria. Stop there.
- If a PRD is attached or pasted, treat it as supplied and continue.
- If the PRD is incomplete, continue only when enough implementation direction exists. Capture missing information as questions or assumptions inside the generated prompt.

Suggested request when the PRD is missing:

```text
Para gerar um prompt inicial completo para o Codex, preciso primeiro do PRD. Cole aqui o PRD ou anexe o arquivo, incluindo objetivo, escopo, requisitos, criterios de aceite, restricoes e contexto tecnico quando houver.
```

## Workflow

1. Read the PRD fully before drafting.
2. Extract the product goal, user problem, target users, required behavior, non-goals, dependencies, constraints, edge cases, acceptance criteria, and rollout or testing expectations.
3. Infer the likely Codex task type: build, modify, debug, refactor, test, review, document, or investigate.
4. Ask at most three clarifying questions only when the PRD leaves a decision that would materially change the implementation. If the prompt can proceed with reasonable assumptions, include those assumptions in the prompt instead.
5. Generate a single initial prompt for a new Codex thread. The prompt should be self-contained and written so another Codex instance can begin useful work without rereading the full conversation.

## Prompt Quality Bar

The generated Codex prompt must:

- State the desired outcome plainly.
- Include relevant PRD context without dumping unnecessary prose.
- Separate must-haves from nice-to-haves.
- Preserve named requirements, acceptance criteria, metrics, personas, platforms, APIs, data shapes, and constraints from the PRD.
- Tell Codex what to inspect first when a repo is involved.
- Define expected deliverables, verification steps, and any files or areas that should be avoided.
- Include open questions and assumptions when the PRD is ambiguous.
- Avoid inventing requirements that are not in the PRD.
- Use the same language as the user unless they request another language.

## Output Format

When the PRD is available, respond with:

```markdown
Aqui esta um prompt inicial para usar com o Codex:

[prompt in a fenced text block]

Pontos que talvez voce queira confirmar:
- [only include if there are meaningful uncertainties]
```

Inside the fenced prompt, use this structure unless the PRD calls for a different shape:

```text
You are OpenAI Codex working in this repository.

Goal
[One concise paragraph describing the outcome.]

Context From The PRD
- [Condensed product/user/business context.]

Scope
- Must do: [...]
- Out of scope: [...]

Functional Requirements
- [...]

Non-Functional Requirements And Constraints
- [...]

Acceptance Criteria
- [...]

Implementation Guidance
- Start by inspecting [...]
- Follow existing project patterns.
- Keep changes scoped to [...]
- Do not [...]

Verification
- Run or add [...]
- Manually check [...]

Deliverables
- [...]

Open Questions Or Assumptions
- [...]
```

## Handling Weak PRDs

If the PRD lacks implementation detail but still defines the product outcome, generate a prompt that instructs Codex to inspect the repo and ask for clarification before making high-risk decisions. If the PRD lacks the actual product outcome, ask the user for a fuller PRD instead of generating the prompt.
