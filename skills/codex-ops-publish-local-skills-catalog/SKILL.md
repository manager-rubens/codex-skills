---
name: codex-ops-publish-local-skills-catalog
description: Compare user-created local Codex skills in $CODEX_HOME/skills with the GitHub catalog repository, synchronize changed skill folders and generated catalog files, validate the result, and publish safe updates to GitHub. Use when the user asks to varrer, sincronizar, comparar, atualizar, publicar, pushar, or catalogar local skills in manager-rubens/codex-skills or another personal skills catalog repository.
---

# Publish Local Skills Catalog

## Overview

Synchronize personal Codex skills from the local `$CODEX_HOME/skills` tree into a GitHub catalog repository. Preserve each skill folder, regenerate catalog indexes, validate the copied skills, and publish only after the diff is understood.

This skill is for user-created skills only. Never include `.system` skills or plugin/cache skills.

## Default Repository

Use `https://github.com/manager-rubens/codex-skills.git` and branch `main` unless the user names a different catalog repository or branch.

Read `references/catalog-format.md` when the repository structure is unfamiliar, when updating the sync script, or when a diff looks inconsistent with the catalog format.

## Workflow

1. Resolve scope:
   - Confirm the target repository URL and branch.
   - Resolve the local skills root. Prefer `$CODEX_HOME/skills`; if `CODEX_HOME` is unset, use `~/.codex/skills`.
   - Exclude `.system`, plugin caches, and folders without `SKILL.md`.

2. Prepare the repository:
   - Clone the catalog if no checkout exists.
   - If a checkout exists, run `git status -sb` before modifying it.
   - Stop if the checkout has unrelated local changes.
   - Fetch and fast-forward the target branch before syncing.
   - Stop if the branch has diverged or cannot fast-forward cleanly.

3. Synchronize:
   - Run `scripts/sync_personal_skills_catalog.ps1` without `-Publish` first unless the user already explicitly approved publishing in the current request.
   - Copy the complete folder for each local personal skill into `skills/<name>/`, preserving `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/`.
   - Regenerate `README.md`, `docs/skills.md`, `data/skills.json`, and `data/skills.csv`.
   - Calculate SHA-256 from each copied `SKILL.md`.

4. Handle removals cautiously:
   - Treat skills that exist in the repository but not locally as stale remote skills.
   - Do not delete stale remote skills unless the user explicitly approves removals.
   - If removals are approved, pass `-AllowRemovals` to the script and mention the removed skill names in the summary.

5. Validate:
   - Run `quick_validate.py` for each synchronized skill unless validation is impossible.
   - Parse `data/skills.json` to confirm valid JSON.
   - Run `git diff --check`.
   - Review `git status -sb` and `git diff --stat`.

6. Publish:
   - Publish only when the user asked for publishing or approves after seeing the diff summary.
   - Stage only catalog files and `skills/`.
   - Commit with a short message such as `Update personal Codex skills catalog`.
   - Push to the configured remote branch.
   - If `gh` is unavailable, use plain `git push`; do not require a PR unless the user asks for one.

## Script

Use the bundled script for deterministic synchronization:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1
```

Common forms:

```powershell
# Prepare a local diff only
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1

# Commit and push after approval
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1 -Publish

# Allow deletion of remote skills that no longer exist locally
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1 -Publish -AllowRemovals
```

The script clones or updates the catalog checkout, copies personal skill folders, regenerates indexes, validates skills, prints the diff summary, and optionally commits and pushes.

## Output

Report:

- repository path, branch, and remote;
- local skills found;
- added, changed, unchanged, and stale remote skills;
- validation result;
- diff stat;
- commit hash and push result when published;
- any blocked step and the exact reason.

Keep the final response short when publication succeeds. If publication is blocked, give the next safe action.
