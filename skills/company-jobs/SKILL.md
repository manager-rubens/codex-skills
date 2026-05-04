---
name: company-jobs
description: Find current job openings from a company's official website or careers page. Use when the user asks to read a company site, careers page, ATS board, or recruitment page and return all available vacancies, roles, jobs, positions, openings, or "vagas"; also use when the user provides only a company name and wants current hiring opportunities.
---

# Company Jobs

## Overview

Find and return current vacancies from a company's official hiring surface. Prefer direct company or ATS sources over aggregators, verify information with live browsing when possible, and cite every source used.

## Workflow

1. Identify the official careers source.
   - If the user provides a careers URL, start there.
   - If the user provides only a company name, search the web for the official careers page, jobs page, or linked ATS board.
   - Prefer official company domains and first-party linked ATS providers over LinkedIn, Indeed, Glassdoor, or scraped mirrors.

2. Collect openings.
   - Run `scripts/job_scraper.py` against the careers URL for a first pass:

```bash
python <skill-dir>/scripts/job_scraper.py "https://example.com/careers" --max-pages 40 --output markdown
```

   - If the page is JavaScript-heavy, protected by consent UI, or incomplete, use browser/web tools to inspect the rendered page and linked ATS endpoints.
   - Read pagination, departments, location filters, and remote/hybrid filters. Do not assume the first page is complete.

3. Normalize each role.
   - Capture title, location or remote status, department/team when available, employment type when available, and the direct application/job-detail URL.
   - Preserve exact public-facing titles.
   - Exclude expired, closed, speculative, or "general application/talent pool" roles unless the user asks for them.

4. Return the result in the user's language.
   - Include the company/source name and access date.
   - If roles were found, provide a compact table.
   - If none were found, say which official pages were checked and whether the company has no listed vacancies or the site could not be read fully.

## CV Handoff Notes

When the user asks to use discovered vacancies to tailor Ruben's CV, hand the vacancy text to `tailor-cv-to-job` and preserve the current project CV base additions:

- Keep `Claude Code`, `OpenAi Codex`, and `Agent Skills` in "Habilidades e Competencias".
- Keep `Claude Code in Action - Anthropic`, `Introduction to Agent Skills - Anthropic`, `Introduction to Model Context Protocol - Anthropic`, and `Buiding with the Claude API - Anthropic` in "Formacao Complementar", using the same one-course-per-line style as the existing section.
- Do not reinsert `Idiomas` or `Ingles` unless the user explicitly asks.

## Output Format

Use this shape unless the user requests another format:

```markdown
Encontrei N vagas abertas em <empresa> em <data>.

| Vaga | Local | Area | Link |
| --- | --- | --- | --- |
| <title> | <location> | <department> | <url> |

Fontes: <career page>, <ATS page if separate>
Observacoes: <pagination/rendering limitations, if any>
```

## Source Handling

- Browse for current data; job listings change frequently.
- Cite the exact pages checked.
- If using search results to discover the careers page, still validate against the official page.
- Do not log in, bypass access controls, solve CAPTCHAs, or scrape private/internal job systems.
- Respect rate limits. Keep crawls small and targeted.

## Script Notes

`scripts/job_scraper.py` is a best-effort helper for static HTML, JSON-LD `JobPosting`, and common ATS link patterns. Treat it as a discovery aid, not the final authority. For dynamic boards such as Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Recruitee, Workable, Gupy, and BambooHR, combine script output with direct browser inspection when needed.

Read `references/job-board-patterns.md` only when a site uses a known ATS or the first pass misses obvious listings.
