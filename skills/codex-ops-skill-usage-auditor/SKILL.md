---
name: codex-ops-skill-usage-auditor
description: Audit how a Codex skill was used in a conversation or transcript, mapping invoked skills, shell/tool commands, app/browser/web calls, file edits, procedures performed, repeated steps, friction points, and concrete opportunities to improve the skill workflow. Use when the user asks to audit, review, varrer, analisar, or mapear uso de skill; list commands or procedures used by a skill; reduce repetitive work after a skill run; or turn a conversation into skill improvements.
---

# Skill Usage Auditor

## Overview

Audit the visible execution trail of a skill and convert it into a practical improvement report. Focus on how the work flowed: commands, tools, decisions, repeated procedures, validation steps, and where the skill could remove future friction.

Do not claim access to private reasoning. Base the audit on visible conversation text, tool traces, terminal output, files, transcripts, or artifacts the user provides.

## Inputs

Use the current conversation when it contains enough evidence. Also accept exported transcripts, copied chat logs, terminal logs, automation memory files, skill folders, or individual `SKILL.md` files.

If evidence is incomplete, audit the visible portion and mark gaps explicitly. Ask for more material only when the missing context prevents a useful audit.

For a deeper pass or when the user asks for a checklist-style audit, load `references/audit-checklist.md`.

## Workflow

1. Define the audit scope:
   - Identify the target skill or skills.
   - Identify the user's goal for the original task.
   - Identify the available evidence: conversation, tool traces, files, logs, web pages, generated artifacts.
   - State any important gaps.

2. Build a timeline:
   - List the main phases in order.
   - Capture skills invoked, tools used, shell commands, file reads, file edits, approvals, validations, and failures.
   - Mark each item as observed, inferred, or missing when confidence matters.

3. Map commands and tool use:
   - For shell commands, record the exact command when short and relevant; otherwise summarize the command family and purpose.
   - For tool calls, record the namespace/tool name, purpose, and important parameters.
   - For app or browser work, record the target, action, and result.
   - For file edits, record the path and why it changed.

4. Extract the procedure:
   - Group timeline items into repeatable stages.
   - Identify decision points, prerequisites, fallbacks, validation checks, and manual heuristics.
   - Separate one-off context gathering from reusable workflow steps.

5. Find repetition and friction:
   - Repeated searches, reads, curl calls, parsing steps, copy-paste transformations, file templates, validation commands, approvals, or manual comparisons.
   - Places where the agent had to rediscover stable knowledge.
   - Brittle steps caused by ambiguous triggers, missing criteria, missing examples, missing scripts, or unclear output expectations.
   - Validation gaps where the result was trusted without a concrete check.

6. Propose improvements:
   - `SKILL.md` updates for clearer triggers, scope, workflow order, decision rules, and output format.
   - `references/` files for criteria, examples, schemas, source lists, or report templates that should not bloat `SKILL.md`.
   - `scripts/` for deterministic or repeatedly rewritten operations.
   - `assets/` for reusable output templates, boilerplate, or static resources.
   - `agents/openai.yaml` updates when display text, default prompt, or implicit invocation policy is stale.
   - Automation candidates when the repeated task is recurring, while leaving creation to the user unless explicitly requested.

7. Prioritize:
   - Rank improvements by impact, implementation effort, and risk.
   - Prefer small, concrete changes that remove repeated work from the next run.
   - Call out any changes that need user approval before editing a live skill.

## Output Format

Use a concise report with these sections:

- **Scope**: target skill, original task goal, evidence used, gaps.
- **Timeline**: phases with commands, tools, files, and validations.
- **Procedure Map**: reusable stages and decision points.
- **Repetition And Friction**: where time or attention was spent repeatedly.
- **Improvement Backlog**: prioritized changes with rationale and suggested skill resource type.
- **Next Patch**: the smallest high-value edit to make first, if the user wants implementation.

Keep the report operational. Avoid generic advice; tie every recommendation to an observed command, procedure, gap, or repeated step.
