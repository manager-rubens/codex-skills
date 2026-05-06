---
name: career-salary-market-research
description: Research current salary ranges for a job position by company, role/title, contract type, and market using Glassdoor as the priority source and Michael Page as a secondary benchmark. Use when the user asks for salario, salary, remuneracao, compensation, media salarial, Glassdoor salary, Michael Page salary guide, or wants monthly and annual salary estimates with sources, company-name ambiguity checks, fallback to comparable companies, and a confidence level.
---

# Salary Market Research

## Overview

Estimate current gross salary for a specific company, role, and contract type. Prioritize Glassdoor company salary pages, use Michael Page salary guides or salary benchmark pages as secondary context, and fall back to comparable-company market averages only when the exact company/role combination is unavailable.

Use live web research for every request because salary data, source availability, and company pages change often.

## Required Inputs

Collect or infer these fields before estimating:

- `company`: target employer name.
- `role`: target job title or close title family.
- `contract_type`: CLT, PJ, full-time, contractor, temporary, internship, apprentice, etc.
- `market`: country/city/region if provided or clearly implied. If missing and the estimate would materially vary by geography, ask for location before searching.
- `currency`: default to the market currency unless the user requests another.

If the company name is ambiguous, stop and ask the user to confirm the correct company before estimating. Ambiguity includes multiple Glassdoor companies with the same or similar name, subsidiaries with separate salary pages, or a company name that maps to unrelated employers.

## Research Workflow

1. Normalize the role and contract type.
   - Keep the user title as the primary search phrase.
   - Also prepare 2 to 4 close variants such as translated titles, seniority variants, or common local equivalents.
   - Do not silently change seniority. If the title says Pleno, Senior, Lead, Director, Intern, etc., preserve that level.

2. Search Glassdoor first.
   - Look for the official Glassdoor company salary page and the specific role.
   - Prefer pages/snippets that show company, role, market, salary period, currency, and sample count.
   - If Glassdoor blocks full content but search snippets expose salary data, use the snippet only with reduced confidence and cite the search result/page URL.

3. Check company ambiguity before salary extraction.
   - If results show more than one plausible company identity, ask: "Encontrei mais de uma empresa possivel: A, B, C. Qual delas devo usar?"
   - Include location, industry, parent/subsidiary, or Glassdoor company page clue when available.
   - Continue only after confirmation.

4. Extract exact company-role salary when available.
   - Capture monthly salary, annual salary, currency, market/location, role title as displayed, contract type, base/total compensation distinction, sample count, and source URL.
   - Prefer base gross salary unless the user requests total compensation.

5. Use Michael Page as secondary benchmark.
   - Search Michael Page salary guide, salary comparison, or market reports for the same market and role family.
   - Treat Michael Page as market benchmark, not company-specific data, unless a page explicitly names the company.

6. If the exact role is missing for the company, build a comparable-market estimate.
   - First use same-company adjacent roles with the same seniority and function.
   - Then use comparable companies in the same industry, size, geography, and talent market.
   - Use at least 3 observations when feasible. If fewer than 3 are available, report low confidence.
   - Explain the comparables briefly and cite each source.

7. Normalize and calculate.
   - Convert monthly to annual using 12 months unless the market/contract clearly uses a different convention. For Brazil CLT, report monthly base and annualized 12x base; mention that 13th salary/benefits are not included unless explicitly included in the source.
   - Convert annual to monthly by dividing by 12 unless the source states another basis.
   - Keep source currency. Convert currencies only if the user requests it, and then cite an exchange-rate source.
   - Prefer median when sources provide medians. If only ranges are available, use midpoint per source and then average the midpoints.

Use `scripts/normalize_salary_estimate.py` when there are multiple salary observations and you want deterministic mean/median calculations. See `references/methodology.md` for the JSON shape and confidence rubric.

## Output Format

Return a concise report in Portuguese unless the user asks for another language:

- Empresa confirmada.
- Cargo pesquisado and contract type.
- Market/location and currency.
- Estimated monthly salary.
- Estimated annual salary.
- Confidence: High, Medium, Low, or Very low.
- Sources: bullet list with source name, URL, salary value used, and notes.
- Method note: exact Glassdoor company-role match, Glassdoor snippet, Michael Page benchmark, or comparable-company estimate.

When the estimate is not an exact company-role match, say that clearly before the numbers.

## Confidence Rubric

- High: exact Glassdoor company-role-market match, recent visible source, clear currency/period, enough sample context or corroboration.
- Medium: exact company-role source but partial visibility, limited sample context, or corroborated by Michael Page/comparables.
- Low: no exact company-role match; estimate relies on adjacent roles or 2 to 4 comparable-company observations.
- Very low: only snippets, stale pages, one comparable observation, unclear contract type, unclear market, or conflicting data.

Never fabricate salary values or hidden sample counts. If the data is unavailable, say so and provide the best available benchmark with low confidence.
