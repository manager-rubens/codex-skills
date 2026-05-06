---
name: career-job-fit-evaluator
description: Evaluate whether a job posting, recruiter message, LinkedIn role, or vacancy description is compatible with Ruben's CV, experience, target job profile, preferences, and positioning. Use when asked to assess job fit, match a role to the user's background, identify gaps, decide whether to apply, tailor a CV/profile summary, or explain how well a position aligns with the user's experience.
---

# Job Fit Evaluator

## Overview

Assess job opportunities against the user's stored CV, target profile, and fit rubric. Produce a practical decision that explains compatibility, gaps, risks, and how to position the user's experience.

## Required References

Before evaluating a role, read:

- `references/cv.md` for the user's background, experience, skills, achievements, education, languages, and constraints.
- `references/target-profile.md` for desired roles, industries, seniority, work model, compensation, and non-negotiables.
- `references/evaluation-rubric.md` for scoring rules and output format.

If any reference still contains placeholder text, say what is missing and continue with a provisional assessment using only the available information.

## Workflow

1. Read the required references.
2. Parse the job post into:
   - role title and seniority
   - core responsibilities
   - required qualifications
   - preferred qualifications
   - technical skills, domain skills, languages, and tools
   - location, remote policy, contract type, compensation, and schedule if present
3. Compare the role against the CV and target profile.
4. Score fit using `references/evaluation-rubric.md`.
5. Return a clear recommendation:
   - `Strong fit`
   - `Possible fit`
   - `Stretch`
   - `Not recommended`
6. Ground every major conclusion in evidence from the CV, target profile, or job post. Do not invent experience.

## Evaluation Guidance

- Treat "required" criteria as more important than "preferred" criteria.
- Distinguish direct experience from adjacent or transferable experience.
- Consider seniority fit: under-leveling, right-leveling, and over-leveling.
- Do not over-trust job titles. In technology roles, titles can be disconnected from the real job; evaluate the responsibility mix, scope, stakeholders, outcomes, and operating model first.
- Flag dealbreakers from the target profile even when the experience match is strong.
- Apply conservative scoring. Do not inflate the 0-100 score to be agreeable; high scores require direct evidence and no major hard-requirement gaps.
- Treat mandatory education, credentials, licenses, and background requirements as real constraints. If the requested formation is far from technology, design, product, digital, or exact sciences, apply the rubric's stronger penalty/cap.
- Call out missing evidence separately from true skill gaps.
- Be candid but helpful: if the role is weak, explain why and suggest better role keywords or titles.
- If the user asks in Portuguese, answer in Portuguese. Otherwise, match the language of the user's request.

## Output

Use this concise structure unless the user requests another format:

```markdown
**Decision:** <Strong fit | Possible fit | Stretch | Not recommended>
**Fit Score:** <0-100>
**Confidence:** <High | Medium | Low>

**Why**
- <Evidence-based reason>
- <Evidence-based reason>

**Matched Experience**
- <Job requirement> -> <matching CV evidence>

**Gaps / Risks**
- <Gap, risk, or missing evidence>

**Score Inhibitors**
- <Main reasons the score is not higher, especially mandatory education, credentials, seniority, language, tools, or domain gaps>

**Application Strategy**
- <How to position the user's background>
- <CV/profile keywords to emphasize>

**Better-Fit Search Terms**
- <Role titles, keywords, or industries if useful>
```
