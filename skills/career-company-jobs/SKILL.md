---
name: career-company-jobs
description: Find current job openings from official company careers surfaces and build single-company or aggregated HTML job digests from primary sources. Use when Codex needs to search company careers pages or ATS boards, collect and normalize current openings, package them for a career-company-jobs or job-alerts digest, or deliver the digest through Apps Script and Gmail relay without leaving raw payload emails visible in the inbox.
---

# Company Jobs

## Overview

Find and return current vacancies from a company's official hiring surface. Prefer direct company or ATS sources over aggregators, verify information with live browsing when possible, and cite every source used.

When the requested output is a jobs digest, keep the collection, normalization, delivery, and inbox-cleanup steps in the same flow so the recipient ends up with the final formatted HTML email only.

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

   - If the page is JavaScript-heavy, protected by consent UI, or incomplete, use browser or web tools to inspect the rendered page and linked ATS endpoints.
   - Read pagination, departments, location filters, and remote or hybrid filters. Do not assume the first page is complete.

3. Normalize each role.
   - Capture title, location or remote status, department or team when available, employment type when available, and the direct application or job-detail URL.
   - Preserve exact public-facing titles.
   - Deduplicate repeated roles across pagination, alternate URLs, or ATS detail pages.
   - Exclude expired, closed, speculative, or general-application or talent-pool roles unless the user asks for them.
   - If a public detail page is incomplete or unavailable, say that explicitly in `note` or `risk` and lower confidence instead of guessing.

4. Package the result.
   - For a plain jobs answer, return a compact table in the user's language.
   - For digests, normalize each kept role into a delivery object with:
     - `title`
     - `company`
     - `location`
     - `model`
     - `source`
     - `score`
     - `decision`
     - `confidence`
     - `why`
     - `risk`
     - `url`
   - Sort valid roles by score descending.
   - Put the top roles in `jobs` and the remaining valid roles in `otherJobs`.

5. Deliver the digest when asked.
   - Use `template: "job-alerts"` for aggregated or multi-company digests.
   - Use `template: "career-company-jobs"` for single-company digests.
   - Read `references/digest-delivery.md` before sending any Apps Script or Gmail-based digest.
   - If manual HTML rendering is truly required, use `assets/job-fit-digest-template.html` as the canonical fallback layout instead of inventing a new email shape.

## CV Handoff Notes

When the user asks to use discovered vacancies to tailor Ruben's CV, hand the vacancy text to `career-tailor-cv-to-job` and preserve the current project CV base additions:

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

For email digests, keep the payload and delivery rules in `references/digest-delivery.md`.

## Source Handling

- Browse for current data; job listings change frequently.
- Cite the exact pages checked.
- If using search results to discover the careers page, still validate against the official page.
- Do not log in, bypass access controls, solve CAPTCHAs, or scrape private or internal job systems.
- Respect rate limits. Keep crawls small and targeted.

## Delivery Guardrails

- Never replace a requested formatted digest with a simplified plain-text fallback.
- Never leave relay payload JSON or temporary helper emails visible in the recipient inbox once the final digest exists.
- If the Apps Script Web App POST fails, use the Gmail relay flow from `references/digest-delivery.md`, verify the final HTML digest from `Ruben Job Fit Alerts`, and archive the relay or helper emails so only the final digest remains in inbox.
- Keep JSON and payload text in UTF-8. Do not replace accents with HTML entities in the payload.

## Script Notes

`scripts/job_scraper.py` is a best-effort helper for static HTML, JSON-LD `JobPosting`, and common ATS link patterns. Treat it as a discovery aid, not the final authority. For dynamic boards such as Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Recruitee, Workable, Gupy, and BambooHR, combine script output with direct browser inspection when needed.

Read `references/job-board-patterns.md` only when a site uses a known ATS or the first pass misses obvious listings.
