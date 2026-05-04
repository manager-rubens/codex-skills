---
name: tailor-cv-to-job
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
   - When using DOCX tools, avoid operations that flatten runs or remove style metadata. If replacing text programmatically would damage formatting, use the app-native editor or a safer manual replacement strategy.
   - Keep replacement text within the original section's layout capacity. Shorten wording before allowing text to overflow, clip, overlap, or remove indentation.
   - After editing, open or inspect the resulting document enough to verify page count, visible sections, indentation, line wrapping, and no clipped/overlapping text. If visual validation is not possible, say so and do not claim strict formatting preservation.

6. Export the PDF.
   - Use `scripts/convert_docx_to_pdf.py` when the edited source is DOCX, ODT, or RTF and LibreOffice/OpenOffice/soffice is available.
   - Name the PDF exactly `CV [nome completo] - [cargo da vaga].pdf`, with filesystem-unsafe characters removed from the title.
   - Return the path to the final PDF and the edited source file only after layout validation passes. Include a brief note of any unsupported job keywords intentionally omitted.

## Script

`scripts/convert_docx_to_pdf.py` converts DOCX/ODT/RTF to PDF using LibreOffice/OpenOffice/soffice and optionally renames the output:

```bash
python scripts/convert_docx_to_pdf.py "path/to/edited.odt" --output-dir "path/to/output" --pdf-name "CV Nome Completo - Cargo.pdf"
```

If conversion fails because LibreOffice is missing, use an available app-native export method or tell the user exactly what dependency is missing.

## Final Response

Keep the final response short. Provide:

- PDF path.
- Edited source path.
- Core competencies targeted.
- Any job keywords not used because they were unsupported by the original CV.
- If blocked by PDF-only input, say that the original PDF was saved/analyzed and ask for the editable CV source instead of returning a flawed final PDF.
