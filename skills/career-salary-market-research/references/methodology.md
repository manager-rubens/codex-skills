# Salary Research Methodology

## Source Priority

Use sources in this order:

1. Glassdoor exact company, role, market, and salary period.
2. Glassdoor exact company and close role variant with same seniority/function.
3. Michael Page salary guide or salary benchmark for the same market and role family.
4. Comparable companies from the same industry, geography, size, and talent market.
5. Search snippets from Glassdoor only when full pages are blocked. Mark these as partial visibility.

Avoid salary aggregator pages unless Glassdoor and Michael Page do not provide enough signal. If used, label them as fallback.

## Comparable Company Rules

Choose comparables using the strongest available overlap:

- Same industry or product market.
- Same geography or hiring market.
- Similar company size, maturity, and compensation tier.
- Similar role scope, seniority, and contract type.

Do not mix internships, junior, mid-level, senior, lead, manager, and director roles unless no better data exists. If mixed, lower confidence and explain the adjustment.

## Normalization Rules

- Store each observation in the original currency and period.
- Convert monthly to annual using `monthly * 12`.
- Convert annual to monthly using `annual / 12`.
- For Brazil CLT, report 12x base salary by default. Mention that 13th salary, vacation bonus, bonus, equity, and benefits are excluded unless the source includes them.
- For PJ/contractor, treat values as gross invoice/base pay and do not compare directly with CLT total cost unless the user asks for a conversion.
- For ranges, use the midpoint for the point estimate and keep the original range in source notes.

## Confidence Scoring

Start from the strongest evidence and adjust down for missing details:

- `high`: exact company-role-market match, visible salary value, clear period/currency, and corroboration or sample context.
- `medium`: exact company-role match with partial visibility or missing sample context; or close role with strong corroboration.
- `low`: comparable-company estimate with 2 to 4 usable observations or unclear contract type.
- `very_low`: one usable observation, snippets only, stale/unclear pages, conflicting data, or no market/location.

## Script Input Shape

Use `scripts/normalize_salary_estimate.py` with a JSON array:

```json
[
  {
    "source": "Glassdoor",
    "company": "ExampleCo",
    "role": "Software Engineer",
    "contract_type": "CLT",
    "currency": "BRL",
    "period": "monthly",
    "value": 12000,
    "url": "https://www.glassdoor.com/...",
    "visibility": "full",
    "match_quality": "exact"
  },
  {
    "source": "Michael Page",
    "company": "Market benchmark",
    "role": "Software Engineer",
    "contract_type": "CLT",
    "currency": "BRL",
    "period": "annual",
    "range_min": 132000,
    "range_max": 180000,
    "url": "https://www.michaelpage.com/...",
    "visibility": "full",
    "match_quality": "benchmark"
  }
]
```

Supported `period` values: `monthly`, `annual`.

Supported `match_quality` values: `exact`, `close_role`, `benchmark`, `comparable`, `snippet`.
