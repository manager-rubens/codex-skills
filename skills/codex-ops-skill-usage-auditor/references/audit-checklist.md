# Audit Checklist

Use this checklist when the user asks for a thorough audit or when the conversation is long.

## Evidence

- What target skill was used?
- What user goal was the skill trying to satisfy?
- Which parts of the conversation are visible?
- Are terminal output, tool calls, files, generated artifacts, or automation memory available?
- Which conclusions are observed versus inferred?

## Command And Tool Inventory

For each relevant command or tool call, capture:

- Name: shell command, MCP/app tool, browser action, web call, file edit, automation update, or subagent action.
- Purpose: why it was used.
- Inputs: important arguments, URLs, files, prompts, or filters.
- Output: result, failure, artifact, or decision enabled.
- Repeatability: one-off, repeated in this run, or likely repeated across future runs.
- Candidate resource: `SKILL.md`, `references/`, `scripts/`, `assets/`, automation, or no change.

## Procedure Extraction

Look for:

- Setup steps and prerequisite checks.
- Source discovery and source validation.
- Data extraction, normalization, ranking, or filtering.
- Human approval points.
- File generation or editing.
- Validation and cleanup.
- Final reporting.

Separate the stable procedure from task-specific details.

## Repetition Signals

Flag any of these:

- Same command pattern run multiple times with changed parameters.
- Repeated source probing or pagination.
- Manual extraction from HTML, JSON, PDFs, logs, or screenshots.
- Repeated report structure recreated from scratch.
- Repeated validation logic.
- Repeated approvals caused by predictable filesystem, network, or automation needs.
- The agent reread stable instructions because they were not in a skill reference.

## Improvement Types

- Trigger improvement: description misses common user phrasing or language.
- Workflow improvement: step order, branching, or stop conditions are unclear.
- Criteria improvement: filtering, scoring, or validation rules are implicit.
- Script improvement: deterministic repeated command sequence should become a script.
- Reference improvement: stable but detailed knowledge should move out of `SKILL.md`.
- Asset improvement: repeated output template or boilerplate should become an asset.
- Validation improvement: add a concrete check before finalizing.
- Automation improvement: recurring work should be scheduled or monitored.

## Prioritization

Score each candidate qualitatively:

- Impact: high, medium, or low.
- Effort: small, medium, or large.
- Risk: low, medium, or high.
- First patch: yes or no.

Prefer high-impact, small-effort, low-risk improvements first.
