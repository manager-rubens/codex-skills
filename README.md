# Codex Skills

Inventario organizado das skills encontradas neste ambiente local do Codex.

Generated on: 2026-05-04 (America/Sao_Paulo)

## Snapshot

| Metric | Count |
| --- | ---: |
| Discovered `SKILL.md` files | 73 |
| Available in the current Codex session | 70 |
| Present on disk only | 3 |

## Files

- `docs/skills.md`: human-readable catalog grouped by source/plugin.
- `data/skills.json`: machine-readable inventory with roots, counts, and skill metadata.
- `data/skills.csv`: spreadsheet-friendly export.
- `scripts/generate-inventory.ps1`: repeatable generator for refreshing this repo.

## Notes

- This repository lists metadata only. It intentionally does not copy full `SKILL.md` instruction bodies.
- `available_in_session` means the skill was advertised as available to Codex in the current session.
- `present_on_disk_only` means the `SKILL.md` file exists locally but was not advertised in the current session list.
