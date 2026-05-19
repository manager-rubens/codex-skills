---
name: product-rice-matrix
description: Create a Product Management RICE prioritization matrix for a set of previously scoped tasks. Use when the user asks to classify, rank, prioritize, score, or compare roadmap/Kanban/backlog tasks using RICE, especially when task titles, status, summaries, scope, acceptance criteria, Notion cards, issues, tickets, or PRD tasks are already available. Always base scoring on the provided task scope and evidence; do not invent missing scope.
---

# Product RICE Matrix

## Goal

Produce a pragmatic RICE ranking from tasks whose scope has already been made available through Notion, tickets, a PRD, pasted task lists, or local documents. Treat the task scope, summary, status, acceptance criteria, and implementation notes as the evidence base.

## Workflow

1. Gather tasks from the provided source.
   - If the source is Notion, fetch the database/page schema first, then fetch each relevant card.
   - Include only tasks that are in scope for the user's request. For "a fazer", include non-final statuses such as Backlog, ToDO, In Progress, Testing, or equivalent.
   - Exclude completed/finalized tasks unless the user explicitly asks for all tasks.

2. Extract evidence per task.
   - Title.
   - Status.
   - Priority, if present.
   - Product area/phase, if present.
   - Summary/objective.
   - Scope.
   - Acceptance criteria.
   - Known blockers, validation notes, dependencies, or owner confirmations.

3. Refuse to score from title alone when scope is missing.
   - Ask for the missing task scope if most tasks have only titles.
   - If only a few tasks lack detail, score them with low confidence and mark the reason.

4. Use a clear RICE scale.
   - Reach: 1 to 5. Estimate how much of the relevant user base or workflow the task affects.
   - Impact: 0.5, 1, 1.5, 2, or 3. Estimate the magnitude of benefit or risk reduction for affected users.
   - Confidence: 50% to 100%. Reflect evidence quality, clarity of scope, and validation certainty.
   - Effort: 0.5 to 5. Estimate implementation/testing effort in relative product/engineering units.
   - Score: `(Reach * Impact * Confidence) / Effort`, where Confidence is decimal form.

5. Calibrate scoring as a PM, not as a spreadsheet clerk.
   - Security, privacy, broken core flows, release blockers, and data integrity can receive high Impact even with modest Reach.
   - Tasks already in Testing can have low Effort if the remaining work is validation/configuration.
   - Dependencies should lower Confidence or raise Effort.
   - Duplicate or overlapping tasks should be called out and optionally recommended for merge.
   - Current roadmap priority may inform scoring but must not override the RICE result by itself.

6. Present the output.
   - State the source and inclusion rule.
   - State the scoring scale.
   - Provide a sorted table with Rank, Task, Status, R, I, C, E, RICE, and PM rationale.
   - Add a concise recommended execution sequence.
   - Add notes for overlaps, dependencies, missing data, or tasks needing re-scoping.

## Scoring Heuristics

Use these defaults when exact metrics are unavailable:

- Reach 5: affects the whole product, all users, or a launch gate.
- Reach 4: affects most active users or a primary workflow.
- Reach 3: affects a meaningful subset or operational maintenance.
- Reach 2: affects a narrow workflow or future scale.
- Reach 1: affects an edge case or internal-only detail.

- Impact 3: prevents launch, protects security/privacy, fixes trust-breaking behavior, or unlocks core value.
- Impact 2: materially improves a primary workflow or removes visible user friction.
- Impact 1.5: improves usability, maintainability, or operational confidence.
- Impact 1: useful polish or moderate internal leverage.
- Impact 0.5: minor polish or speculative upside.

- Confidence 90-100%: scope and acceptance criteria are clear, evidence is current, and validation path is obvious.
- Confidence 75-85%: scope is clear but effort or user impact is partly estimated.
- Confidence 60-70%: task is understandable but dependencies or missing details matter.
- Confidence 50-55%: scope is thin; mark as "needs clarification".

- Effort 0.5-1: validation, configuration, copy, or narrow UI fix.
- Effort 1.5-2: contained implementation or multi-surface test.
- Effort 2.5-3: moderate implementation with data/assets/testing.
- Effort 4-5: broad feature, migration, multiple dependencies, or uncertain implementation.

## Output Tone

Be decisive but transparent. Make the ranking useful for sequencing work, not merely mathematically neat. Prefer short rationales tied to scope and acceptance criteria.
