# Catalog Format

The personal skills catalog stores only user-created Codex skills from `$CODEX_HOME/skills`.

## Repository Layout

```text
README.md
docs/
  skills.md
data/
  skills.csv
  skills.json
scripts/
  generate-personal-skills.ps1
skills/
  <skill-name>/
    SKILL.md
    agents/
    references/
    scripts/
    assets/
```

Only `SKILL.md` is required for each skill. Preserve optional `agents/`, `references/`, `scripts/`, and `assets/` folders when present.

## Exclusions

Never catalog:

- `$CODEX_HOME/skills/.system`
- plugin cache skills
- folders without `SKILL.md`
- generated temporary workspaces

## Generated Files

`README.md` contains the generated date, scope, and one link per skill.

`docs/skills.md` contains:

- generated date and scope;
- total skill count;
- catalog table with skill name, file path, and frontmatter description;
- full `SKILL.md` content for each skill in a fenced `markdown` block.

`data/skills.json` contains:

- `generated_at`
- `timezone`
- `scope`
- `totals.user_created_skills`
- `skills[]` with `name`, `description`, `source_path`, `repository_path`, and `sha256`

`data/skills.csv` contains the same skill metadata in tabular form.

## Ordering

Sort skills by skill name. Use repository paths in the form `skills/<name>/SKILL.md`.

## Checksums

Calculate `sha256` from the UTF-8 text content of each copied `SKILL.md`.

## Publication Guardrails

Start from a clean checkout. Fast-forward before syncing. Do not remove repository skills unless removals are explicitly approved. Validate copied skills and generated JSON before committing.
