# Job Board Patterns

Use this reference when the careers page delegates listings to an ATS or when the first scrape is incomplete.

## Common ATS Hosts

- Greenhouse: `boards.greenhouse.io`, `job-boards.greenhouse.io`
- Lever: `jobs.lever.co`
- Ashby: `jobs.ashbyhq.com`
- Workday: `*.myworkdayjobs.com`
- SmartRecruiters: `jobs.smartrecruiters.com`
- Recruitee: `*.recruitee.com`
- Workable: `apply.workable.com`
- BambooHR: `*.bamboohr.com/careers`
- Gupy: `*.gupy.io`
- Kenoby/Gupy legacy: `jobs.kenoby.com`
- Teamtailor: `*.teamtailor.com`
- Comeet: `www.comeet.com/jobs`

## Practical Checks

- Look for pagination controls, department filters, and location filters.
- Search the page source for `JobPosting`, `application/ld+json`, `jobs`, `openings`, `positions`, `departments`, and `requisition`.
- If a page renders empty HTML but visible jobs appear in the browser, inspect network/API calls for public JSON endpoints.
- For Workday, the visible page may require POST-backed search endpoints; browser inspection is usually more reliable than raw HTML.
- For Ashby and some Greenhouse boards, rendered content may be the authoritative surface even when initial HTML has little data.

## Exclusion Rules

Exclude pages that are clearly:

- Talent communities or spontaneous application pools.
- Closed/expired jobs.
- Recruiting agency reposts when the user asked for direct company listings.
- Duplicates of the same role and location. If duplicates differ only by tracking parameters, keep the cleanest canonical URL.
