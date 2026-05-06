---
name: career-tailor-cv-to-job
description: Adapt an existing editable CV/resume to a specific job description while preserving the original document formatting and generating a PDF. Use when the user sends a vacancy/job description and asks to tailor, reescrever, otimizar para ATS, adaptar CV/curriculo/resume, extrair palavras-chave da vaga, update the Objective/Objetivo section, or create a PDF named for the candidate and job title without inventing experience or changing real job history. If the only source is PDF, use this skill only to save/analyze the original and request an editable source before producing the final formatted CV.
---

# Tailor CV To Job

## Purpose

Adapt the user's original CV to a job description with strict factual integrity, ATS-friendly language, and the same visual formatting as the source CV. The output must be an edited CV file plus a PDF named `CV [nome completo] - [cargo da vaga].pdf`.

## Non-Negotiable Rules

- Do not invent employers, projects, metrics, tools, domains, responsibilities, certifications, education, dates, or achievements.
- Do not change held job titles. Only use a close synonym/SEO variant when it preserves the same meaning and seniority.
- Do not mention the target company in the CV unless the original CV already mentions it as factual history.
- Do not add flattery, motivation, or "quero trabalhar na empresa" language.
- Preserve the original CV's formatting, layout, sections, order, typography, spacing, colors, and page structure as strictly as the editable source allows.
- Do not rewrite final CV content by editing fixed-position PDF text streams, PDF glyph codes, `TJ` arrays, or coordinates. PDF text does not reflow and can clip, overlap, lose indentation, or break ATS extraction.
- Prefer concise, human, ATS-friendly Portuguese or English matching the CV language. Avoid common AI phrasing such as "profissional apaixonado", "historico comprovado", "ambiente dinamico", "solida experiencia em impulsionar", "alavancar sinergias", or exaggerated superlatives.
- Keep the "Objetivo" section to the target job title/role only, or a very short title phrase if the original layout requires a sentence.
- If an instruction conflicts with factual accuracy or formatting preservation, factual accuracy and formatting preservation win.

## Required Inputs

Use the job description supplied by the user and the original CV file supplied or clearly present in the project. Require an editable source file (`.docx`, `.odt`, `.rtf`) to produce the final formatted CV and PDF. A PDF-only source may be saved and analyzed for text/keywords, but must not be rewritten as the final artifact when the user requires strict formatting preservation.

If only a PDF exists, stop after saving/analyzing it and ask for the editable original. Offer a separate "reconstructed layout" path only if the user explicitly accepts that it will not strictly preserve the original formatting.

For Ruben's CV work in this project, use `C:\Users\ruben\Documents\New project 3\cv-original\CV Rubens - Tech Manager.odt` as the default original CV source when no other editable CV file is explicitly supplied. Keep this file unchanged and edit only a copied output file.

Ruben's project CV base must preserve these current additions in every tailored CV unless the user explicitly asks to remove them:
- In "Habilidades e Competencias", keep `Claude Code`, `OpenAi Codex`, and `Agent Skills` in the AI/tools line.
- In "Formacao Complementar", keep `Claude Code in Action - Anthropic`, `Introduction to Agent Skills - Anthropic`, `Introduction to Model Context Protocol - Anthropic`, and `Buiding with the Claude API - Anthropic` in the same one-course-per-line style as the existing section.
- Do not reinsert `Idiomas` or `Ingles` unless the user explicitly asks.

If multiple possible CV files exist, ask the user which one is the source.

## Workflow

1. Inspect the source CV.
   - Identify language, candidate full name, sections, Objective/Objetivo, work history, education, skills, certifications, and formatting constraints.
   - Make a copy before editing. Never overwrite the original CV.
   - If the source is only PDF and no editable counterpart exists, copy it into the project, extract/analyze text if useful, then stop and request the editable source. Do not generate a final tailored PDF from fixed PDF coordinates.

2. Analyze the job description.
   - Extract target title, seniority, domain, must-have skills, nice-to-have skills, tools/technologies, responsibilities, language requirements, certifications, and recurring ATS keywords.
   - If the role clearly matches a family template in `references/templates/`, read only that JSON file before drafting replacements. Treat templates as reusable guidance, not as factual evidence.
   - Create a short internal "evidence ledger": for each high-priority keyword, mark whether it is explicitly present in the CV, strongly supported by existing experience, weakly supported, or unsupported.

3. Decide what can be changed.
   - Use explicit or strongly supported evidence freely.
   - Use weakly supported evidence only as broad positioning, not as a claimed hands-on achievement.
   - Omit unsupported keywords. Do not force every job keyword into the CV.
   - Keep original dates, employers, roles, education, and certifications unchanged unless the user explicitly supplies a correction.

4. Rewrite conservatively.
   - Update "Objetivo" to the target job title from the vacancy, without company name.
   - Reorder or tune existing skills to emphasize matching core competencies.
   - Rewrite bullets to foreground relevant responsibilities and tools already present in the CV.
   - Preserve the candidate's real seniority and scope. Do not inflate leadership, architecture, management, budget, or stakeholder ownership.
   - Prefer direct nouns and verbs used in the vacancy. Keep language natural, specific, and short.

5. Preserve formatting.
   - Edit the existing document structure in place. Do not rebuild the CV from a blank template.
   - Reuse existing styles, paragraph marks, tables, headers/footers, text boxes, and section spacing.
   - For ODT sources, prefer `scripts/tailor_odt.py` for audited `content.xml` replacements instead of creating a one-off script for each vacancy.
   - Use `scripts/tailor_odt.py "<source.odt>" --dump-text` to inspect visible paragraphs before drafting replacements.
   - Store ODT replacements as UTF-8 JSON (`{"old text": "new text"}` or a list of `{"old": "...", "new": "...", "expected": 1}` objects) and require exactly one match for each replacement unless there is a clear reason to set another `expected` count.
   - Before applying replacements, run `scripts/tailor_odt.py "<source.odt>" --validate-replacements "<draft-replacements.json>"` to catch invalid JSON, duplicate/zero matches, and styled-span failures.
   - When visible replacements cross styled spans, run `scripts/tailor_odt.py "<source.odt>" --suggest-segment-replacements "<draft-replacements.json>" --suggest-output "<segmented-replacements.json>"`, inspect the generated JSON, then validate the segmented file before applying it.
   - When automatic segmentation cannot safely infer a split, run `scripts/tailor_odt.py "<source.odt>" --find-visible-text-fragment "<visible text>"` to print the actual text-node/span segments, then use smaller exact segment texts as replacement keys.
   - When a replacement crosses styled spans or ODT namespace prefixes, keep the replacement as small as possible. Do not depend on a namespace prefix such as `text:` or `ns4:` unless the script verifies the exact occurrence.
   - For Ruben's CV, pass `--ruben-required` or otherwise verify the required AI/tool/course additions before exporting the PDF.
   - When using DOCX tools, avoid operations that flatten runs or remove style metadata. If replacing text programmatically would damage formatting, use the app-native editor or a safer manual replacement strategy.
   - Keep replacement text within the original section's layout capacity. Shorten wording before allowing text to overflow, clip, overlap, or remove indentation.
   - After editing, open or inspect the resulting document enough to verify page count, visible sections, indentation, line wrapping, and no clipped/overlapping text. If visual validation is not possible, say so and do not claim strict formatting preservation.
   - After PDF export, compare the final PDF page count with the original PDF page count when a source/reference PDF exists. If the final PDF has more pages, treat it as layout overflow: shorten replacements, regenerate the editable file, re-export, and repeat validation before returning files.
   - Do not rely on Chrome/headless browser screenshots of PDF viewer pages as layout proof; they can render blank or dark viewer surfaces. Prefer PDF structure checks, source/final page-count comparison, ODT visible-text inspection, and app-native or real-renderer visual review when available.

6. Export the PDF.
   - Use `scripts/convert_docx_to_pdf.py` when the edited source is DOCX, ODT, or RTF and LibreOffice/OpenOffice/soffice is available.
   - The converter uses an isolated temporary Office profile by default. For OpenOffice it tries the UNO exporter first, then falls back to `soffice --convert-to pdf`; for LibreOffice it tries `--convert-to` first, then UNO when enabled.
   - Prefer one converter command with enough room for Windows/OpenOffice, for example `--timeout 180 --attempts 2`, instead of ad hoc `soffice` or manual UNO commands.
   - If the sandbox blocks or times out while starting OpenOffice/LibreOffice headless, rerun the same converter command with the required execution approval instead of switching to PDF stream editing.
   - Name the PDF exactly `CV [nome completo] - [cargo da vaga].pdf`, with filesystem-unsafe characters removed from the title.
   - Return the path to the final PDF and the edited source file only after layout validation passes, including the page-count check. Include a brief note of any unsupported job keywords intentionally omitted.

## Script

`scripts/tailor_odt.py` applies audited replacements to an ODT copy while preserving the original package structure and validating XML:

```bash
python scripts/tailor_odt.py "path/to/source.odt" --dump-text
python scripts/tailor_odt.py "path/to/source.odt" --validate-replacements "path/to/draft-replacements.json"
python scripts/tailor_odt.py "path/to/source.odt" --suggest-segment-replacements "path/to/draft-replacements.json" --suggest-output "path/to/segmented-replacements.json"
python scripts/tailor_odt.py "path/to/source.odt" --find-visible-text-fragment "visible text that failed to replace"
python scripts/tailor_odt.py "path/to/source.odt" --output "path/to/edited.odt" --replacements "path/to/replacements.json" --audit "path/to/audit.txt" --ruben-required
```

Use this script for Ruben's default ODT workflow before PDF export.

Role-family templates in `references/templates/` provide reusable keyword and phrasing guidance for common job families. Load the matching file only when the vacancy clearly fits:

- `agile-lead-scrum-master.json`
- `it-project-manager.json`
- `delivery-manager.json`

Never copy a template keyword into the CV unless the source CV explicitly or strongly supports it.

`scripts/convert_docx_to_pdf.py` converts DOCX/ODT/RTF to PDF using LibreOffice/OpenOffice/soffice and optionally renames the output:

```bash
python scripts/convert_docx_to_pdf.py "path/to/edited.odt" --output-dir "path/to/output" --pdf-name "CV Nome Completo - Cargo.pdf" --timeout 60
```

For Windows/OpenOffice, prefer:

```bash
python scripts/convert_docx_to_pdf.py "path/to/edited.odt" --output-dir "path/to/output" --pdf-name "CV Nome Completo - Cargo.pdf" --timeout 180 --attempts 2
```

If conversion fails because LibreOffice/OpenOffice is missing, use an available app-native export method or tell the user exactly what dependency is missing. If `--convert-to` fails silently on OpenOffice, keep the UNO fallback enabled; use `--no-uno-fallback`, `--prefer-convert-to`, or `--no-isolated-profile` only for diagnosis.

## Final Response

Keep the final response short. Provide:

- PDF path.
- Edited source path.
- Core competencies targeted.
- Any job keywords not used because they were unsupported by the original CV.
- If blocked by PDF-only input, say that the original PDF was saved/analyzed and ask for the editable CV source instead of returning a flawed final PDF.
