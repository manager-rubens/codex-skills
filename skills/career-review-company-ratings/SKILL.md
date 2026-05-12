---
name: career-review-company-ratings
description: Analyze public employee-review pages for a target company and summarize only reviews whose job titles are related or adjacent to career targets such as technology, IT, data, product management, project/program management, PMO, implementation, digital transformation, business systems, or product operations. Use when the user asks to inspect Glassdoor, Indeed, Comparably, Love Mondays-style company reviews, filter by relevant roles, compute average review scores, and synthesize pros and cons for career decision-making.
---

# Career Review Company Ratings

## Overview

Analyze company-review sites from a career lens: gather public review data, keep only roles relevant to the user's target domains, compute the average rating for the filtered sample, and summarize recurring positive and negative themes.

## Workflow

1. Open the user-provided company review URL first.
2. Browse/search the web because review counts, ratings, and recent reviews change frequently.
3. Prefer primary review pages from the named platform. Use search snippets only as supplements when the platform exposes public snippets that the opened page hides or paginates.
4. Record source date context: current date, platform, company name, overall rating, total review count, recommendation percentage, and category ratings when visible.
5. Extract public review records with these fields when available:
   - `rating`
   - `date`
   - `title`
   - `job_title`
   - `employment_status`
   - `location`
   - `pros`
   - `cons`
   - `source_url`
6. Filter review records by role relevance.
7. Compute the arithmetic mean of the numeric ratings in the filtered set.
8. Summarize themes from the filtered set, not from all company reviews, unless explicitly labeled as overall-company context.
9. Cite the exact pages used.

## Role Filtering

Default inclusion targets:

- Technology and IT: `TI`, `tecnologia`, `technology`, `IT`, `sistemas`, `systems`, `software`, `developer`, `desenvolvedor`, `engenharia de software`, `infraestrutura`, `security`, `cyber`, `cloud`, `support`, `suporte`, `data`, `dados`, `analytics`, `BI`, `business intelligence`.
- Product: `produto`, `product`, `product manager`, `product owner`, `PO`, `PM`, `product designer`, `UX`, `service design`, `product ops`.
- Projects and delivery: `projeto`, `projetos`, `project`, `program`, `portfolio`, `PMO`, `scrum`, `agile`, `delivery`, `implantacao`, `implementacao`, `implementation`, `transformacao digital`.
- Adjacent business/technology roles: `business analyst`, `analista de negocios`, `processos`, `automacao`, `digital`, `sistemas de negocio`, `engenharia` only when the title or review content implies implementation, systems, product, data, transformation, or project work.

Default exclusions:

- Generic titles with no domain signal, such as only `Analista`, `Especialista`, `Analista Senior`, `Coordenador`, or `Gerente`.
- Operational, maintenance, toll, cashier, administrative, HR, legal, finance, sales, hospital, atendimento, arrecadacao, and apprentice roles unless the user explicitly asks to include them.
- Vague confidential/anonymous titles unless the review text clearly signals target-domain work.

If a role is ambiguous, either exclude it or include it in a separate "possivelmente relacionado" group. Do not blend ambiguous roles into the main average unless explaining the assumption.

## Glassdoor Notes

Glassdoor frequently limits public access, changes pagination, and exposes different snippets through search indexing versus direct page opens. Do not imply a complete scrape when only public snippets are available.

When access is limited:

- Say the analysis is based on publicly accessible reviews/snippets.
- Distinguish direct page data from search-index snippets.
- Avoid scraping behind login walls or bypassing platform controls.
- Use the platform's visible aggregate numbers for company context, but compute the filtered-role average only from review records whose rating and role are visible.

## Calculations

For the filtered sample:

```text
average = sum(visible numeric ratings for included role reviews) / count(included role reviews)
```

Report:

- filtered review count
- included roles
- average rating rounded to one decimal
- optional alternate average excluding "adjacent" roles
- notes on excluded ambiguous roles

## Output Format

Respond in the user's language. Keep the answer concise but decision-useful.

Use this structure unless the user requested another format:

1. Short scope note with date and access limitations.
2. Company-level context from the review platform.
3. Table of included filtered reviews.
4. Average rating for the filtered set.
5. Positive themes.
6. Negative themes.
7. Missing/limited data, especially if no product or project-management-specific reviews were visible.
8. Source links.

Do not quote long review text. Paraphrase themes and use very short excerpts only when necessary.

## Quality Checks

Before finalizing:

- Verify every included row has a role that matches the filter or is clearly marked adjacent.
- Ensure the average uses only included rows, not overall-company rating.
- Check that pros/cons summaries are not borrowed from excluded roles.
- Cite sources used.
- State uncertainty clearly when platform access or snippets limit coverage.
