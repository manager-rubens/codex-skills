---
name: career-translate-cv-to-english
description: Translate an existing tailored CV/resume into natural, ATS-friendly professional English while preserving the editable document formatting and exporting an updated PDF. Use when Codex needs to convert a Portuguese CV to English for a specific job, adapt bullet phrasing to English-speaking resume expectations, avoid literal translations, keep facts unchanged, and produce an English ODT/DOCX/PDF version.
---

# Translate CV To English

## Purpose

Convert an already tailored CV into professional English for the target job while preserving factual integrity, layout, section order, and export quality. The result should read like an English-language resume, not a literal translation.

## Non-Negotiable Rules

- Do not invent employers, roles, dates, metrics, tools, technologies, degrees, certifications, English fluency, or achievements.
- Preserve the original job history and seniority. Translate held titles only when the English title keeps the same meaning and level.
- Use the target vacancy to choose emphasis, vocabulary, and bullet style, but include only skills supported by the source CV.
- Do not copy content from sample English CVs supplied only as formatting references. Use them only for structure, bullet rhythm, and tone.
- Preserve the editable source formatting. Do not rewrite PDF text streams or fixed-position PDF coordinates.
- Keep language concise, concrete, and human. Avoid inflated phrases such as "visionary leader", "proven track record", "dynamic environment", or "passionate professional".
- If the English version overflows the original/reference PDF page count, shorten wording and regenerate before returning the final files.

## Default Output

- Edited source: `CV [Full Name] - [Job Title] - English.odt` or matching editable format.
- PDF: `CV [Full Name] - [Job Title] - English.pdf`.
- Optional audit file when using audited replacements.

## Workflow

1. Inspect the source CV and job description.
   - Prefer the most recent tailored editable CV for the role.
   - Dump or extract visible text before drafting replacements.
   - Identify sections, summary lines, work history, skills, education, courses, page count, and formatting constraints.
   - When the user supplies an English CV only as a format reference, inspect it for structure and style only. Do not copy its content.
   - For the recruiter-style English CV format, read `references/english-cv-format.md`.

2. Build a translation ledger.
   - Mark each target job keyword as explicit, strongly supported, weakly supported, or unsupported.
   - Translate and emphasize explicit/strongly supported items.
   - Use weak support only as broad positioning.
   - Omit unsupported terms instead of forcing them into the English CV.

3. Translate for English resume expectations.
   - Prefer action + scope + outcome when the source supports it.
   - Prefer the structure `Professional Summary`, `Core Competencies`, `Professional Experience`, `Education`, and `Certifications & Development` when the user asks for the English CV format reference.
   - Put competency groups before experience when following that reference format.
   - Keep quantified impact already present, such as lead time reduction, satisfaction improvement, ramp-up reduction, or number of leaders developed.
   - Replace literal Portuguese business phrasing with idiomatic English:
     - `PDIs` -> `individual development plans` or `development plans`.
     - `ritos Scrum e Kanban` -> `Scrum/Kanban facilitation`.
     - `métricas de fluxo` -> `flow metrics`.
     - `times técnicos/não técnicos` -> `technical and non-technical teams`.
     - `stakeholders técnicos e não técnicos` -> `technical and non-technical stakeholders`.
     - `Gestão de Pessoas` -> `People Management`.
     - `Formação Acadêmica` -> `Education`.
     - `Formação Complementar` -> `Additional Training`.
   - Keep common global tech terms in English (`lead time`, `KPIs`, `APIs`, `microservices`, `containers`, `stakeholders`).
   - Use `Bachelor's degree` only when the source supports a completed undergraduate degree.

4. Preserve document structure.
   - For ODT sources, reuse `career-tailor-cv-to-job/scripts/tailor_odt.py` if available.
   - If a user-provided ODT is explicitly a format reference, it may be used as the output template, replacing all sample content with content from the current source CV.
   - Create UTF-8 replacement JSON with exact `old`, `new`, and `expected` counts.
   - Validate replacements before applying.
   - When a visible line crosses styled spans, use `--find-visible-text-fragment` and replace smaller exact text-node segments.
   - If text-node replacements include XML-escaped characters such as `&amp;`, `&quot;`, or `&apos;`, keep replacements XML-valid.
   - Never use the same file as both source and output; write to a new file, then rename only after validation if needed.

5. Compact for layout.
   - English usually expands versus Portuguese. Draft compact bullets from the start.
   - If export adds pages, shorten summary lines, repeated verbs, course names, and long skill lists while preserving supported keywords.
   - Prefer concise lines such as `Stakeholder communication, translating business needs into technical solutions.` over literal long sentences.

6. Export and validate.
   - Export the edited source to PDF using the existing project converter when available.
   - Compare final PDF page count to the source/reference PDF.
   - Inspect the final visible text enough to verify translated sections, required facts, and no accidental Portuguese leftovers except names, institutions, or course titles that should remain.
   - Return the PDF path and editable source path only after page count and text checks pass.

## Ruben-Specific Safeguards

When working on Ruben's CV files, preserve existing AI/tool/course additions if present:

- Keep `Claude Code`, `OpenAi Codex`, and `Agent Skills` in the AI/tools line.
- Keep `Claude Code in Action - Anthropic`, `Introduction to Agent Skills - Anthropic`, `Introduction to Model Context Protocol - Anthropic`, and `Buiding with the Claude API - Anthropic`.
- Do not add a Languages section or English fluency unless the user explicitly requests it.
