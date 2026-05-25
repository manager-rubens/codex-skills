# Catalogo de skills do Codex

Gerado em: 2026-05-25 (America/Sao_Paulo)

Escopo: skills criadas pelo usuario em $CODEX_HOME/skills (exclui .system e skills vindas de plugins/cache).

## Resumo

| Metrica | Total |
| --- | ---: |
| Skills pessoais catalogadas | 16 |

## Catalogo

| Skill | Arquivo | Descricao |
| --- | --- | --- |
| `career-company-jobs` | [skills/career-company-jobs/SKILL.md](../skills/career-company-jobs/SKILL.md) | Find current job openings from official company careers surfaces and build single-company or aggregated HTML job digests from primary sources. Use when Codex needs to search company careers pages or ATS boards, collect and normalize current openings, package them for a career-company-jobs or job-alerts digest, or deliver the digest through Apps Script and Gmail relay without leaving raw payload emails visible in the inbox. |
| `career-gemini-interview-prep-prompt` | [skills/career-gemini-interview-prep-prompt/SKILL.md](../skills/career-gemini-interview-prep-prompt/SKILL.md) | Create a ready-to-paste Gemini prompt that turns Gemini into a rigorous, concise, respectful interview preparation coach and evaluator. Use when the user provides a professional CV/resume, LinkedIn/profile information, job description, extra context, hiring-process stage, recruiter notes, interview format, or asks to generate a prompt for Gemini to prepare someone for a job interview, mock interview, technical interview, HR screening, hiring-manager conversation, case interview, panel interview, or final interview. |
| `career-job-fit-evaluator` | [skills/career-job-fit-evaluator/SKILL.md](../skills/career-job-fit-evaluator/SKILL.md) | Evaluate whether a job posting, recruiter message, LinkedIn role, or vacancy description is compatible with Ruben's CV, experience, target job profile, preferences, and positioning. Use when asked to assess job fit, match a role to the user's background, identify gaps, decide whether to apply, tailor a CV/profile summary, or explain how well a position aligns with the user's experience. |
| `career-pj-contract-risk-review` | [skills/career-pj-contract-risk-review/SKILL.md](../skills/career-pj-contract-risk-review/SKILL.md) | Evaluate Brazilian PJ individual service arrangements for career decisions using contract scope, role/vacancy description, company context, operating model, and contexto-pj-brasil.md or the bundled PJ Brazil reference. Use when the user asks to review a vaga PJ, proposta PJ, contrato PJ, escopo de prestacao de servicos, pejotizacao risk, questions for the company/legal team, or points to negotiate before accepting or signing a PJ engagement. |
| `career-review-company-ratings` | [skills/career-review-company-ratings/SKILL.md](../skills/career-review-company-ratings/SKILL.md) | Analyze public employee-review pages for a target company and summarize only reviews whose job titles are related or adjacent to career targets such as technology, IT, data, product management, project/program management, PMO, implementation, digital transformation, business systems, or product operations. Use when the user asks to inspect Glassdoor, Indeed, Comparably, Love Mondays-style company reviews, filter by relevant roles, compute average review scores, and synthesize pros and cons for career decision-making. |
| `career-salary-market-research` | [skills/career-salary-market-research/SKILL.md](../skills/career-salary-market-research/SKILL.md) | Research current salary ranges for a job position by company, role/title, contract type, and market using Glassdoor as the priority source and Michael Page as a secondary benchmark. Use when the user asks for salario, salary, remuneracao, compensation, media salarial, Glassdoor salary, Michael Page salary guide, or wants monthly and annual salary estimates with sources, company-name ambiguity checks, fallback to comparable companies, and a confidence level. |
| `career-tailor-cv-to-job` | [skills/career-tailor-cv-to-job/SKILL.md](../skills/career-tailor-cv-to-job/SKILL.md) | Adapt an existing editable CV/resume to a specific job description while preserving the original document formatting and generating a PDF. Use when the user sends a vacancy/job description and asks to tailor, reescrever, otimizar para ATS, adaptar CV/curriculo/resume, extrair palavras-chave da vaga, update the Objective/Objetivo section, or create a PDF named for the candidate and job title without inventing experience or changing real job history. If the only source is PDF, use this skill only to save/analyze the original and request an editable source before producing the final formatted CV. |
| `career-translate-cv-to-english` | [skills/career-translate-cv-to-english/SKILL.md](../skills/career-translate-cv-to-english/SKILL.md) | Translate an existing tailored CV/resume into natural, ATS-friendly professional English while preserving the editable document formatting and exporting an updated PDF. Use when Codex needs to convert a Portuguese CV to English for a specific job, adapt bullet phrasing to English-speaking resume expectations, avoid literal translations, keep facts unchanged, and produce an English ODT/DOCX/PDF version. |
| `codex-ops-publish-local-skills-catalog` | [skills/codex-ops-publish-local-skills-catalog/SKILL.md](../skills/codex-ops-publish-local-skills-catalog/SKILL.md) | Compare user-created local Codex skills in $CODEX_HOME/skills with the GitHub catalog repository, synchronize changed skill folders and generated catalog files, validate the result, and publish safe updates to GitHub. Use when the user asks to varrer, sincronizar, comparar, atualizar, publicar, pushar, or catalogar local skills in manager-rubens/codex-skills or another personal skills catalog repository. |
| `codex-ops-skill-usage-auditor` | [skills/codex-ops-skill-usage-auditor/SKILL.md](../skills/codex-ops-skill-usage-auditor/SKILL.md) | Audit how a Codex skill was used in a conversation or transcript, mapping invoked skills, shell/tool commands, app/browser/web calls, file edits, procedures performed, repeated steps, friction points, and concrete opportunities to improve the skill workflow. Use when the user asks to audit, review, varrer, analisar, or mapear uso de skill; list commands or procedures used by a skill; reduce repetitive work after a skill run; or turn a conversation into skill improvements. |
| `product-dev-prd-to-codex-prompt` | [skills/product-dev-prd-to-codex-prompt/SKILL.md](../skills/product-dev-prd-to-codex-prompt/SKILL.md) | Create a clear, complete initial prompt for OpenAI Codex from a Product Requirements Document (PRD). Use when the user wants to turn a PRD, product spec, feature brief, ticket, or requirements document into a Codex-ready prompt for implementation, refactoring, debugging, review, testing, or planning. The skill must require the user to provide or attach a PRD before drafting the prompt. |
| `product-prd-interviewer` | [skills/product-prd-interviewer/SKILL.md](../skills/product-prd-interviewer/SKILL.md) | Act as a senior product professional to interview the user about an app, SaaS, internal tool, platform, website, automation, or software product and turn the discovery into a professional Product Requirements Document (PRD). Use when the user asks to be interviewed about a product idea, define app objectives, create a PRD, product brief, MVP scope, requirements document, user stories, acceptance criteria, feature spec, or product handoff for development. Trigger on Portuguese or English requests such as "me entrevista para entender o app", "gera um PRD", "brief de produto", "requisitos da aplicacao", "product requirements", or "turn this idea into a PRD". |
| `product-rice-matrix` | [skills/product-rice-matrix/SKILL.md](../skills/product-rice-matrix/SKILL.md) | Create a Product Management RICE prioritization matrix for a set of previously scoped tasks. Use when the user asks to classify, rank, prioritize, score, or compare roadmap/Kanban/backlog tasks using RICE, especially when task titles, status, summaries, scope, acceptance criteria, Notion cards, issues, tickets, or PRD tasks are already available. Always base scoring on the provided task scope and evidence; do not invent missing scope. |
| `research-curadoria-eventos` | [skills/research-curadoria-eventos/SKILL.md](../skills/research-curadoria-eventos/SKILL.md) | Buscar, curar e retornar eventos atuais para uma cidade usando fontes oficiais, APIs, portais locais, Instagram/redes sociais e inteligencia de eventos, com opcao de gerar PDF bonito com imagem de fonte para cada evento. Use quando o usuario pedir eventos, agenda cultural, shows, gastronomia, eventos corporativos, eventos gratuitos, programacao de fim de semana, o que fazer, roles, destaques por data, periodo, categoria, bairro, ponto turistico ou cidade, ou quando pedir um PDF/relatorio visual da agenda. |
| `research-pessoa-due-diligence` | [skills/research-pessoa-due-diligence/SKILL.md](../skills/research-pessoa-due-diligence/SKILL.md) | Levantamento juridico, reputacional e de idoneidade documental de pessoa fisica com base em fontes publicas, oficiais ou autorizadas, reunindo documentos, links, processos, diarios oficiais, registros profissionais, sancoes, certidoes, sinais criminais publicos, informacoes militares publicas quando licitas e evidencias rastreaveis de boa ou ma conduta institucional. Use quando o usuario pedir investigacao juridica, due diligence, background check, "levantar tudo sobre uma pessoa", pesquisar processos, antecedentes, documentos, vinculos publicos, risco criminal, historico militar, certidoes, compliance, OSINT legal, reputacao, idoneidade, "indole" ou relatorio rastreavel sobre uma pessoa identificada ou parcialmente identificada. |
| `weather-next-weekend-bh-sp` | [skills/weather-next-weekend-bh-sp/SKILL.md](../skills/weather-next-weekend-bh-sp/SKILL.md) | List the weather forecast for the next weekend in Belo Horizonte, Jundiai, Guarulhos, and Sao Paulo city. Use when the user asks for "tempo", weather, forecast, chuva, temperatura, or weekend conditions for BH, Jundiai, Guarulhos, and SP together, especially for the upcoming Saturday and Sunday. |

## Conteudo completo

### career-company-jobs

Origem: `$CODEX_HOME/skills/career-company-jobs/SKILL.md`

````markdown
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
````

### career-gemini-interview-prep-prompt

Origem: `$CODEX_HOME/skills/career-gemini-interview-prep-prompt/SKILL.md`

````markdown
---
name: career-gemini-interview-prep-prompt
description: Create a ready-to-paste Gemini prompt that turns Gemini into a rigorous, concise, respectful interview preparation coach and evaluator. Use when the user provides a professional CV/resume, LinkedIn/profile information, job description, extra context, hiring-process stage, recruiter notes, interview format, or asks to generate a prompt for Gemini to prepare someone for a job interview, mock interview, technical interview, HR screening, hiring-manager conversation, case interview, panel interview, or final interview.
---

# Gemini Interview Prep Prompt

## Overview

Create a complete prompt for Gemini to act as an interview preparation coach for a specific professional, vacancy, and selection-process stage. The final answer should usually be only the prompt ready to paste into Gemini, unless the user asks for explanation or variants.

## Workflow

1. Gather inputs from the user message and attached files: CV/profile, job description, company/context, process stage, interview format, language, seniority, target role, known recruiter feedback, concerns, constraints, and extra instructions.
2. If a core input is missing, make a reasonable placeholder inside the prompt instead of blocking, using bracketed fields such as `[colar CV aqui]`, `[colar descritivo da vaga aqui]`, or `[informar etapa]`.
3. Identify the interview stage and adapt emphasis:
   - HR screening: motivation, fit, communication, compensation, availability, career narrative.
   - Hiring manager: role scope, impact examples, stakeholder management, priorities, decision-making.
   - Technical interview: hard skills, tools, architecture, trade-offs, debugging, depth checks.
   - Case or assignment: structure, assumptions, clarifying questions, business reasoning, presentation.
   - Panel or final: executive presence, consistency, strategic fit, risk areas, concise storytelling.
4. Use the detailed structure in [references/gemini-prompt-template.md](references/gemini-prompt-template.md) when composing the final prompt.
5. Preserve the requested tone: preparatory, concise, direct, rigorous, respectful, and evaluative.

## Output Rules

- Return a prompt addressed to Gemini, not the interview-preparation content itself.
- Make the prompt self-contained: include or clearly reserve space for all relevant CV, vacancy, stage, and context information.
- Instruct Gemini not to flatter the candidate and not to invent facts.
- Force Gemini to evaluate evidence from the CV against the vacancy requirements.
- Ask Gemini to expose gaps, risks, weak answers, likely objections, and concrete ways to improve.
- Include mock interview behavior: ask one question at a time, wait for the candidate answer, score it, critique it, and demand a stronger version.
- Prefer Portuguese if the user writes in Portuguese, unless the interview language or user instruction suggests otherwise.

## Quality Bar

The generated Gemini prompt must make Gemini behave like a demanding interview trainer, not a generic career advisor. It should produce specific preparation around the actual role scope, likely questions, answer frameworks, evidence from the candidate's background, red flags, score rubrics, and drills for the current stage.
````

### career-job-fit-evaluator

Origem: `$CODEX_HOME/skills/career-job-fit-evaluator/SKILL.md`

````markdown
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
````

### career-pj-contract-risk-review

Origem: `$CODEX_HOME/skills/career-pj-contract-risk-review/SKILL.md`

````markdown
---
name: career-pj-contract-risk-review
description: Evaluate Brazilian PJ individual service arrangements for career decisions using contract scope, role/vacancy description, company context, operating model, and contexto-pj-brasil.md or the bundled PJ Brazil reference. Use when the user asks to review a vaga PJ, proposta PJ, contrato PJ, escopo de prestacao de servicos, pejotizacao risk, questions for the company/legal team, or points to negotiate before accepting or signing a PJ engagement.
---

# Career PJ Contract Risk Review

## Purpose

Produce a practical pre-signature review for a Brazilian individual PJ engagement. Focus on career, negotiation, and contract-risk questions, not on giving definitive legal advice.

State clearly that the output is informational and should be validated with a labor lawyer and accountant when the decision is material.

## Reference

When available, read the user's project/source file first, especially `docs/contexto-pj-brasil.md` or an attached equivalent. Otherwise read `references/pj-brasil.md`.

For current legal or jurisprudential claims, especially if the user asks for "lei atual", "STF", "risco juridico", "processo", "hoje", or a concrete decision to sign, verify the current official/legal sources before relying on them and cite the sources used.

## Inputs To Use

Use all information the user provides, including:

- Contract draft, proposal, SOW, job description, vacancy, recruiter message, or informal scope.
- Company name, business model, country/state/city, reputation, employee reviews, litigation/news history, and how it usually hires.
- Expected routine: schedule, meetings, reporting line, tools, workplace, remote/hybrid, equipment, on-call, availability, exclusivity, benefits, vacation, deliverables, and acceptance criteria.
- Payment model: monthly retainer, hourly, per project, milestones, invoice flow, tax regime, reimbursement, currency, adjustment, termination, and penalties.
- Professional context: whether the user is converting from CLT, replacing an employee, joining a team, using own CNPJ/MEI/LTDA, or serving multiple clients.

If facts are missing, continue with explicit assumptions and include an "Informacoes faltantes" section.

## Workflow

1. Summarize the arrangement in 3-6 bullets: role, company, scope, operating model, payment, and unknowns.
2. Classify risk as `baixo`, `moderado`, `alto`, or `indeterminado`, with a short reason. Avoid claiming certainty.
3. Map the facts against PJ risk dimensions:
   - autonomia versus subordinacao;
   - entrega/resultado versus jornada/disponibilidade;
   - pessoalidade and ability to use substitutes or support;
   - habitualidade and permanent team integration;
   - exclusivity, economic dependence, and ability to serve other clients;
   - benefits, company email/title/org chart, equipment, and employee-like treatment;
   - prior CLT relationship or replacement of a CLT role;
   - taxes, invoices, CNPJ activity, accountant, and fiscal regularity;
   - IP, confidentiality, LGPD, non-compete, non-solicit, liability, termination, and dispute terms.
4. Produce the requested sections in Portuguese.
5. Prioritize questions that a real candidate/contractor can send to the company or raise in a meeting.

## Output Format

Use this structure unless the user asks otherwise:

### Resumo da situacao

Briefly describe the arrangement, risk level, and why it matters.

### Questionamentos para o juridico da empresa a prestar servico

List direct questions for the company's legal team. Prefer questions that force clarity about autonomy, absence of employment relationship, scope, evidence, and risk allocation.

### Pontos de atencao na formatacao do contrato

List clauses or drafting choices to review. Highlight risky wording and safer commercial alternatives when useful.

### Perguntas para a contratante e seu juridico

List practical business/process questions for the hiring manager, recruiter, procurement, and legal team. Include work routine, management model, tools, deliverables, payment, access, and renewal/termination.

### Observacoes adicionais

Add negotiation notes, documents to request, red flags, pricing considerations, and when to seek a lawyer/accountant.

### Informacoes faltantes

Include only when relevant. Keep it short and focused on the facts that would most change the risk analysis.

## Question Patterns

Use and adapt these question patterns.

For legal:

- Como o contrato demonstra autonomia tecnica e operacional do prestador?
- Quais praticas internas evitam controle de jornada, subordinacao direta e tratamento equivalente a empregado?
- O contrato permite atendimento a outros clientes? Se houver exclusividade, qual a justificativa, prazo e compensacao?
- Como serao documentadas entregas, aceite, mudancas de escopo e comunicacoes?
- A vaga substitui ou replica uma funcao CLT existente? Houve conversao recente de CLT para PJ?
- Qual e a posicao da empresa se houver questionamento sobre vinculo ou pejotizacao?
- Existem clausulas de nao concorrencia, nao solicitacao, confidencialidade, LGPD, propriedade intelectual, multa ou responsabilidade ilimitada? Como sao proporcionais?

For contract formatting:

- Preferir escopo, entregaveis, criterios de aceite, prazos, valores e forma de pagamento.
- Evitar linguagem de cargo, chefe, subordinacao, jornada, banco de horas, ferias autorizadas, escala, advertencia ou beneficios CLT.
- Prever nota fiscal, tributos, reajuste, reembolso, rescisao, confidencialidade, LGPD, propriedade intelectual, limitacao de responsabilidade e mecanismo de mudanca de escopo.
- Diferenciar SLA comercial de controle de horario.
- Registrar se ferramentas/equipamentos sao do prestador ou fornecidos apenas para seguranca/acesso, sem caracterizar direcao do trabalho.

For the contratante:

- Quem define prioridades e quem aprova entregas?
- Ha horario fixo, reunioes obrigatorias diarias, plantao, sobreaviso ou expectativa de resposta imediata?
- O prestador pode organizar agenda, metodo e local de trabalho?
- O prestador pode atender outros clientes?
- Como ausencias planejadas, indisponibilidade e ferias comerciais serao tratadas?
- Quais acessos, sistemas, email, titulo e apresentacao publica serao usados?
- Qual e o fluxo de NF, pagamento, aceite e contestacao de entregas?
- O valor proposto considera impostos, contador, beneficios privados, ferias, doenca, equipamentos e periodos sem demanda?

## Tone And Boundaries

- Be direct, practical, and candidate-friendly.
- Separate facts from assumptions.
- Do not tell the user a contract is "legal" or "illegal" with certainty.
- Do not draft final legal clauses as if acting as counsel unless the user asks for a draft; even then, label as a discussion draft for lawyer review.
- If the user's facts strongly resemble employment, say so plainly and recommend specialized legal review before signing.
````

### career-review-company-ratings

Origem: `$CODEX_HOME/skills/career-review-company-ratings/SKILL.md`

````markdown
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
````

### career-salary-market-research

Origem: `$CODEX_HOME/skills/career-salary-market-research/SKILL.md`

````markdown
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
````

### career-tailor-cv-to-job

Origem: `$CODEX_HOME/skills/career-tailor-cv-to-job/SKILL.md`

````markdown
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
````

### career-translate-cv-to-english

Origem: `$CODEX_HOME/skills/career-translate-cv-to-english/SKILL.md`

````markdown
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
````

### codex-ops-publish-local-skills-catalog

Origem: `$CODEX_HOME/skills/codex-ops-publish-local-skills-catalog/SKILL.md`

````markdown
---
name: codex-ops-publish-local-skills-catalog
description: Compare user-created local Codex skills in $CODEX_HOME/skills with the GitHub catalog repository, synchronize changed skill folders and generated catalog files, validate the result, and publish safe updates to GitHub. Use when the user asks to varrer, sincronizar, comparar, atualizar, publicar, pushar, or catalogar local skills in manager-rubens/codex-skills or another personal skills catalog repository.
---

# Publish Local Skills Catalog

## Overview

Synchronize personal Codex skills from the local `$CODEX_HOME/skills` tree into a GitHub catalog repository. Preserve each skill folder, regenerate catalog indexes, validate the copied skills, and publish only after the diff is understood.

This skill is for user-created skills only. Never include `.system` skills or plugin/cache skills.

## Default Repository

Use `https://github.com/manager-rubens/codex-skills.git` and branch `main` unless the user names a different catalog repository or branch.

Read `references/catalog-format.md` when the repository structure is unfamiliar, when updating the sync script, or when a diff looks inconsistent with the catalog format.

## Workflow

1. Resolve scope:
   - Confirm the target repository URL and branch.
   - Resolve the local skills root. Prefer `$CODEX_HOME/skills`; if `CODEX_HOME` is unset, use `~/.codex/skills`.
   - Exclude `.system`, plugin caches, and folders without `SKILL.md`.

2. Prepare the repository:
   - Clone the catalog if no checkout exists.
   - If a checkout exists, run `git status -sb` before modifying it.
   - Stop if the checkout has unrelated local changes.
   - Fetch and fast-forward the target branch before syncing.
   - Stop if the branch has diverged or cannot fast-forward cleanly.

3. Synchronize:
   - Run `scripts/sync_personal_skills_catalog.ps1` without `-Publish` first unless the user already explicitly approved publishing in the current request.
   - Copy the complete folder for each local personal skill into `skills/<name>/`, preserving `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/`.
   - Regenerate `README.md`, `docs/skills.md`, `data/skills.json`, and `data/skills.csv`.
   - Calculate SHA-256 from each copied `SKILL.md`.

4. Handle removals cautiously:
   - Treat skills that exist in the repository but not locally as stale remote skills.
   - Do not delete stale remote skills unless the user explicitly approves removals.
   - If removals are approved, pass `-AllowRemovals` to the script and mention the removed skill names in the summary.

5. Validate:
   - Run `quick_validate.py` for each synchronized skill unless validation is impossible.
   - Parse `data/skills.json` to confirm valid JSON.
   - Run `git diff --check`.
   - Review `git status -sb` and `git diff --stat`.

6. Publish:
   - Publish only when the user asked for publishing or approves after seeing the diff summary.
   - Stage only catalog files and `skills/`.
   - Commit with a short message such as `Update personal Codex skills catalog`.
   - Push to the configured remote branch.
   - If `gh` is unavailable, use plain `git push`; do not require a PR unless the user asks for one.

## Script

Use the bundled script for deterministic synchronization:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1
```

Common forms:

```powershell
# Prepare a local diff only
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1

# Commit and push after approval
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1 -Publish

# Allow deletion of remote skills that no longer exist locally
powershell -NoProfile -ExecutionPolicy Bypass -File <skill-dir>\scripts\sync_personal_skills_catalog.ps1 -Publish -AllowRemovals
```

The script clones or updates the catalog checkout, copies personal skill folders, regenerates indexes, validates skills, prints the diff summary, and optionally commits and pushes.

## Output

Report:

- repository path, branch, and remote;
- local skills found;
- added, changed, unchanged, and stale remote skills;
- validation result;
- diff stat;
- commit hash and push result when published;
- any blocked step and the exact reason.

Keep the final response short when publication succeeds. If publication is blocked, give the next safe action.
````

### codex-ops-skill-usage-auditor

Origem: `$CODEX_HOME/skills/codex-ops-skill-usage-auditor/SKILL.md`

````markdown
---
name: codex-ops-skill-usage-auditor
description: Audit how a Codex skill was used in a conversation or transcript, mapping invoked skills, shell/tool commands, app/browser/web calls, file edits, procedures performed, repeated steps, friction points, and concrete opportunities to improve the skill workflow. Use when the user asks to audit, review, varrer, analisar, or mapear uso de skill; list commands or procedures used by a skill; reduce repetitive work after a skill run; or turn a conversation into skill improvements.
---

# Skill Usage Auditor

## Overview

Audit the visible execution trail of a skill and convert it into a practical improvement report. Focus on how the work flowed: commands, tools, decisions, repeated procedures, validation steps, and where the skill could remove future friction.

Do not claim access to private reasoning. Base the audit on visible conversation text, tool traces, terminal output, files, transcripts, or artifacts the user provides.

## Inputs

Use the current conversation when it contains enough evidence. Also accept exported transcripts, copied chat logs, terminal logs, automation memory files, skill folders, or individual `SKILL.md` files.

If evidence is incomplete, audit the visible portion and mark gaps explicitly. Ask for more material only when the missing context prevents a useful audit.

For a deeper pass or when the user asks for a checklist-style audit, load `references/audit-checklist.md`.

## Workflow

1. Define the audit scope:
   - Identify the target skill or skills.
   - Identify the user's goal for the original task.
   - Identify the available evidence: conversation, tool traces, files, logs, web pages, generated artifacts.
   - State any important gaps.

2. Build a timeline:
   - List the main phases in order.
   - Capture skills invoked, tools used, shell commands, file reads, file edits, approvals, validations, and failures.
   - Mark each item as observed, inferred, or missing when confidence matters.

3. Map commands and tool use:
   - For shell commands, record the exact command when short and relevant; otherwise summarize the command family and purpose.
   - For tool calls, record the namespace/tool name, purpose, and important parameters.
   - For app or browser work, record the target, action, and result.
   - For file edits, record the path and why it changed.

4. Extract the procedure:
   - Group timeline items into repeatable stages.
   - Identify decision points, prerequisites, fallbacks, validation checks, and manual heuristics.
   - Separate one-off context gathering from reusable workflow steps.

5. Find repetition and friction:
   - Repeated searches, reads, curl calls, parsing steps, copy-paste transformations, file templates, validation commands, approvals, or manual comparisons.
   - Places where the agent had to rediscover stable knowledge.
   - Brittle steps caused by ambiguous triggers, missing criteria, missing examples, missing scripts, or unclear output expectations.
   - Validation gaps where the result was trusted without a concrete check.

6. Propose improvements:
   - `SKILL.md` updates for clearer triggers, scope, workflow order, decision rules, and output format.
   - `references/` files for criteria, examples, schemas, source lists, or report templates that should not bloat `SKILL.md`.
   - `scripts/` for deterministic or repeatedly rewritten operations.
   - `assets/` for reusable output templates, boilerplate, or static resources.
   - `agents/openai.yaml` updates when display text, default prompt, or implicit invocation policy is stale.
   - Automation candidates when the repeated task is recurring, while leaving creation to the user unless explicitly requested.

7. Prioritize:
   - Rank improvements by impact, implementation effort, and risk.
   - Prefer small, concrete changes that remove repeated work from the next run.
   - Call out any changes that need user approval before editing a live skill.

## Output Format

Use a concise report with these sections:

- **Scope**: target skill, original task goal, evidence used, gaps.
- **Timeline**: phases with commands, tools, files, and validations.
- **Procedure Map**: reusable stages and decision points.
- **Repetition And Friction**: where time or attention was spent repeatedly.
- **Improvement Backlog**: prioritized changes with rationale and suggested skill resource type.
- **Next Patch**: the smallest high-value edit to make first, if the user wants implementation.

Keep the report operational. Avoid generic advice; tie every recommendation to an observed command, procedure, gap, or repeated step.
````

### product-dev-prd-to-codex-prompt

Origem: `$CODEX_HOME/skills/product-dev-prd-to-codex-prompt/SKILL.md`

````markdown
---
name: product-dev-prd-to-codex-prompt
description: Create a clear, complete initial prompt for OpenAI Codex from a Product Requirements Document (PRD). Use when the user wants to turn a PRD, product spec, feature brief, ticket, or requirements document into a Codex-ready prompt for implementation, refactoring, debugging, review, testing, or planning. The skill must require the user to provide or attach a PRD before drafting the prompt.
---

# PRD to Codex Prompt

## Overview

Generate an initial OpenAI Codex prompt that is understandable, complete, actionable, and faithful to the user's PRD. Do not produce the Codex prompt until a PRD has been provided in the conversation or as an attached/local file.

## Required PRD Gate

Before drafting any prompt, verify that a PRD is available.

- If no PRD is present, ask the user to paste or attach the PRD. Stop there.
- If the user gives only a vague idea, roadmap item, or one-line feature request, ask for a PRD or a PRD-like brief with goals, scope, requirements, constraints, and acceptance criteria. Stop there.
- If a PRD is attached or pasted, treat it as supplied and continue.
- If the PRD is incomplete, continue only when enough implementation direction exists. Capture missing information as questions or assumptions inside the generated prompt.

Suggested request when the PRD is missing:

```text
Para gerar um prompt inicial completo para o Codex, preciso primeiro do PRD. Cole aqui o PRD ou anexe o arquivo, incluindo objetivo, escopo, requisitos, criterios de aceite, restricoes e contexto tecnico quando houver.
```

## Workflow

1. Read the PRD fully before drafting.
2. Extract the product goal, user problem, target users, required behavior, non-goals, dependencies, constraints, edge cases, acceptance criteria, and rollout or testing expectations.
3. Infer the likely Codex task type: build, modify, debug, refactor, test, review, document, or investigate.
4. Ask at most three clarifying questions only when the PRD leaves a decision that would materially change the implementation. If the prompt can proceed with reasonable assumptions, include those assumptions in the prompt instead.
5. Generate a single initial prompt for a new Codex thread. The prompt should be self-contained and written so another Codex instance can begin useful work without rereading the full conversation.

## Prompt Quality Bar

The generated Codex prompt must:

- State the desired outcome plainly.
- Include relevant PRD context without dumping unnecessary prose.
- Separate must-haves from nice-to-haves.
- Preserve named requirements, acceptance criteria, metrics, personas, platforms, APIs, data shapes, and constraints from the PRD.
- Tell Codex what to inspect first when a repo is involved.
- Define expected deliverables, verification steps, and any files or areas that should be avoided.
- Include open questions and assumptions when the PRD is ambiguous.
- Avoid inventing requirements that are not in the PRD.
- Use the same language as the user unless they request another language.

## Output Format

When the PRD is available, respond with:

```markdown
Aqui esta um prompt inicial para usar com o Codex:

[prompt in a fenced text block]

Pontos que talvez voce queira confirmar:
- [only include if there are meaningful uncertainties]
```

Inside the fenced prompt, use this structure unless the PRD calls for a different shape:

```text
You are OpenAI Codex working in this repository.

Goal
[One concise paragraph describing the outcome.]

Context From The PRD
- [Condensed product/user/business context.]

Scope
- Must do: [...]
- Out of scope: [...]

Functional Requirements
- [...]

Non-Functional Requirements And Constraints
- [...]

Acceptance Criteria
- [...]

Implementation Guidance
- Start by inspecting [...]
- Follow existing project patterns.
- Keep changes scoped to [...]
- Do not [...]

Verification
- Run or add [...]
- Manually check [...]

Deliverables
- [...]

Open Questions Or Assumptions
- [...]
```

## Handling Weak PRDs

If the PRD lacks implementation detail but still defines the product outcome, generate a prompt that instructs Codex to inspect the repo and ask for clarification before making high-risk decisions. If the PRD lacks the actual product outcome, ask the user for a fuller PRD instead of generating the prompt.
````

### product-prd-interviewer

Origem: `$CODEX_HOME/skills/product-prd-interviewer/SKILL.md`

````markdown
---
name: product-prd-interviewer
description: Act as a senior product professional to interview the user about an app, SaaS, internal tool, platform, website, automation, or software product and turn the discovery into a professional Product Requirements Document (PRD). Use when the user asks to be interviewed about a product idea, define app objectives, create a PRD, product brief, MVP scope, requirements document, user stories, acceptance criteria, feature spec, or product handoff for development. Trigger on Portuguese or English requests such as "me entrevista para entender o app", "gera um PRD", "brief de produto", "requisitos da aplicacao", "product requirements", or "turn this idea into a PRD".
---

# Product PRD Interviewer

## Overview

Guide a product discovery conversation, ask focused questions like a product manager/product owner, then synthesize the answers into a polished PRD that a design, engineering, or Codex implementation team can use.

Default to the user's language. If the conversation is in Portuguese, write questions and the PRD in Portuguese unless the user asks otherwise.

## Workflow

1. Establish context and stage:
   - Identify whether the user has only an idea, a partially defined product, an existing app to improve, or a development-ready concept.
   - If the user already provided enough detail, summarize what is known and ask only the highest-value missing questions.
   - If the user gave little detail, start with product framing questions before implementation details.

2. Interview in short rounds:
   - Ask 3 to 6 questions per round.
   - Group questions by theme and number them.
   - Prefer crisp, answerable questions over broad questionnaires.
   - Ask follow-ups when answers reveal ambiguity, risk, or conflicting goals.
   - Do not ask about technical stack before the user problem, users, workflows, and success criteria are clear.

3. Synthesize before drafting:
   - After each round, keep an internal map of problem, audience, value proposition, scope, constraints, risks, and open questions.
   - When enough information exists, provide a short "what I understood" summary and list remaining assumptions.
   - Ask the user whether to continue discovery or generate the PRD when key product decisions are reasonably stable.

4. Generate the PRD:
   - Use the outline in `references/prd-outline.md`.
   - Make assumptions explicit instead of hiding gaps.
   - Separate MVP scope from future ideas.
   - Include measurable success metrics where possible.
   - Include user stories and acceptance criteria for core flows.
   - Include open questions and recommended next steps.

## Interview Priorities

Cover these areas in order, adapting to the product's maturity:

1. Product intent: problem, desired outcome, why now.
2. Target users: primary users, secondary users, buyer/admin roles, context of use.
3. Jobs and workflows: current alternatives, pain points, trigger moments, expected end-to-end flow.
4. Value and differentiation: what must feel meaningfully better than current options.
5. Scope: MVP, must-haves, nice-to-haves, explicit non-goals.
6. Business model or operating model: revenue, internal ROI, adoption path, support model.
7. Data and integrations: entities, sources, privacy, permissions, APIs, import/export.
8. Quality attributes: security, performance, accessibility, reliability, mobile/desktop needs.
9. Measurement: activation, retention, conversion, task success, operational metrics.
10. Risks and constraints: deadlines, budget, regulation, dependencies, unknowns.

Use `references/question-bank.md` when a deeper question set is needed.

## Conversation Rules

- Be consultative and practical, not academic.
- Avoid overwhelming the user with a complete questionnaire unless explicitly requested.
- If the user says "I don't know", offer 2 to 4 realistic options and explain the tradeoff briefly.
- If the user asks to generate the PRD early, proceed, but mark missing information as assumptions or open questions.
- If the product is sensitive or regulated, add extra questions about privacy, compliance, auditability, and risk.
- If the user wants to build with Codex after the PRD, add a final "Implementation Handoff" section with a scoped build prompt.

## PRD Quality Bar

The final PRD should be specific enough that a product designer or engineer can start work without re-interviewing the user on basics. It should include clear decisions, not just a transcript of answers.

Strong PRDs include:

- A concise product summary and product objective.
- User personas or roles with concrete needs.
- Prioritized requirements with acceptance criteria.
- Clear exclusions and future enhancements.
- Metrics and instrumentation ideas.
- Risks, assumptions, dependencies, and open questions.
- A pragmatic MVP release plan.
````

### product-rice-matrix

Origem: `$CODEX_HOME/skills/product-rice-matrix/SKILL.md`

````markdown
---
name: product-rice-matrix
description: Create a Product Management RICE prioritization matrix for a set of previously scoped tasks. Use when the user asks to classify, rank, prioritize, score, or compare roadmap/Kanban/backlog tasks using RICE, especially when task titles, status, summaries, scope, acceptance criteria, Notion cards, issues, tickets, or PRD tasks are already available. Always base scoring on the provided task scope and evidence; do not invent missing scope.
---

# Product RICE Matrix

## Goal

Produce a pragmatic RICE ranking from tasks whose scope has already been made available through Notion, tickets, a PRD, pasted task lists, or local documents. Treat the task scope, summary, status, acceptance criteria, and implementation notes as the evidence base.

## Workflow

1. Gather tasks from the provided source.
   - If the source is Notion, fetch the database/page schema first, then fetch each relevant card.
   - Include only tasks that are in scope for the user's request. For "a fazer", include non-final statuses such as Backlog, ToDO, In Progress, Testing, or equivalent.
   - Exclude completed/finalized tasks unless the user explicitly asks for all tasks.

2. Extract evidence per task.
   - Title.
   - Status.
   - Priority, if present.
   - Product area/phase, if present.
   - Summary/objective.
   - Scope.
   - Acceptance criteria.
   - Known blockers, validation notes, dependencies, or owner confirmations.

3. Refuse to score from title alone when scope is missing.
   - Ask for the missing task scope if most tasks have only titles.
   - If only a few tasks lack detail, score them with low confidence and mark the reason.

4. Use a clear RICE scale.
   - Reach: 1 to 5. Estimate how much of the relevant user base or workflow the task affects.
   - Impact: 0.5, 1, 1.5, 2, or 3. Estimate the magnitude of benefit or risk reduction for affected users.
   - Confidence: 50% to 100%. Reflect evidence quality, clarity of scope, and validation certainty.
   - Effort: 0.5 to 5. Estimate implementation/testing effort in relative product/engineering units.
   - Score: `(Reach * Impact * Confidence) / Effort`, where Confidence is decimal form.

5. Calibrate scoring as a PM, not as a spreadsheet clerk.
   - Security, privacy, broken core flows, release blockers, and data integrity can receive high Impact even with modest Reach.
   - Tasks already in Testing can have low Effort if the remaining work is validation/configuration.
   - Dependencies should lower Confidence or raise Effort.
   - Duplicate or overlapping tasks should be called out and optionally recommended for merge.
   - Current roadmap priority may inform scoring but must not override the RICE result by itself.

6. Present the output.
   - State the source and inclusion rule.
   - State the scoring scale.
   - Provide a sorted table with Rank, Task, Status, R, I, C, E, RICE, and PM rationale.
   - Add a concise recommended execution sequence.
   - Add notes for overlaps, dependencies, missing data, or tasks needing re-scoping.

## Scoring Heuristics

Use these defaults when exact metrics are unavailable:

- Reach 5: affects the whole product, all users, or a launch gate.
- Reach 4: affects most active users or a primary workflow.
- Reach 3: affects a meaningful subset or operational maintenance.
- Reach 2: affects a narrow workflow or future scale.
- Reach 1: affects an edge case or internal-only detail.

- Impact 3: prevents launch, protects security/privacy, fixes trust-breaking behavior, or unlocks core value.
- Impact 2: materially improves a primary workflow or removes visible user friction.
- Impact 1.5: improves usability, maintainability, or operational confidence.
- Impact 1: useful polish or moderate internal leverage.
- Impact 0.5: minor polish or speculative upside.

- Confidence 90-100%: scope and acceptance criteria are clear, evidence is current, and validation path is obvious.
- Confidence 75-85%: scope is clear but effort or user impact is partly estimated.
- Confidence 60-70%: task is understandable but dependencies or missing details matter.
- Confidence 50-55%: scope is thin; mark as "needs clarification".

- Effort 0.5-1: validation, configuration, copy, or narrow UI fix.
- Effort 1.5-2: contained implementation or multi-surface test.
- Effort 2.5-3: moderate implementation with data/assets/testing.
- Effort 4-5: broad feature, migration, multiple dependencies, or uncertain implementation.

## Output Tone

Be decisive but transparent. Make the ranking useful for sequencing work, not merely mathematically neat. Prefer short rationales tied to scope and acceptance criteria.
````

### research-curadoria-eventos

Origem: `$CODEX_HOME/skills/research-curadoria-eventos/SKILL.md`

````markdown
---
name: research-curadoria-eventos
description: Buscar, curar e retornar eventos atuais para uma cidade usando fontes oficiais, APIs, portais locais, Instagram/redes sociais e inteligencia de eventos, com opcao de gerar PDF bonito com imagem de fonte para cada evento. Use quando o usuario pedir eventos, agenda cultural, shows, gastronomia, eventos corporativos, eventos gratuitos, programacao de fim de semana, o que fazer, roles, destaques por data, periodo, categoria, bairro, ponto turistico ou cidade, ou quando pedir um PDF/relatorio visual da agenda.
---

# Curadoria de Eventos

## Objetivo

Encontrar eventos atuais para a cidade solicitada, remover duplicidades, priorizar informacoes completas e entregar uma resposta agil em JSON valido ou em PDF visual quando o usuario pedir relatorio, arquivo, PDF ou material apresentavel.

## Entradas

Extraia da mensagem do usuario:

- Cidade obrigatoria. Se nao houver cidade, peca a cidade antes de pesquisar.
- Data ou periodo, como hoje, amanha, este final de semana, semana que vem, mes especifico ou intervalo de datas. Converta expressoes relativas para datas absolutas usando a data atual da conversa.
- Categoria opcional: shows, musica, teatro, gastronomia, corporativo, infantil, esporte, gratuito, exposicoes, festivais, feiras, cursos, networking ou outra categoria indicada.
- Localizacao especifica opcional: bairro, regiao, casa de show, parque, centro cultural, arena, praia, ponto turistico ou raio aproximado.

Quando a categoria nao for especificada, montar um "Mix de Destaques" com eventos variados e relevantes.

## Fontes

Use fontes atuais e rastreaveis. Pesquise na web quando a informacao puder ter mudado ou quando precisar confirmar disponibilidade, data, preco ou link.

Priorize, nesta ordem:

1. Paginas oficiais do evento, produtor, casa de show, equipamento cultural, prefeitura ou secretaria municipal.
2. Plataformas de venda e descoberta: Ticketmaster, Sympla, Eventbrite, Uhuu.com e similares.
3. Portais e guias locais: G1, Catraca Livre, jornais locais, revistas culturais e calendarios oficiais.
4. Redes sociais publicas, incluindo uma etapa obrigatoria de Instagram com 4 perfis locais da cidade, quando a web aberta trouxer evidencias suficientes.
5. Inteligencia de eventos, como PredictHQ, quando houver acesso ou resultados publicos verificaveis.

Nao invente evento, preco, horario, endereco ou link. Quando uma fonte exigir API key ou login indisponivel, use a melhor fonte publica alternativa e reduza a confianca de itens incompletos.

## Instagram local

Inclua Instagram como uma das fontes de busca. Para cada cidade pesquisada:

1. Elencar 4 perfis publicos relevantes da cidade antes de fechar a curadoria.
2. Priorizar nesta ordem:
   - perfil oficial da prefeitura, secretaria de cultura/turismo ou fundacao cultural;
   - perfis oficiais de equipamentos culturais, teatros, centros culturais, arenas, shopping centers ou casas de show;
   - guias/portais locais de agenda, turismo, gastronomia ou entretenimento;
   - produtores, coletivos, festas, feiras, bares ou restaurantes com agenda recorrente.
3. Buscar nos perfis por posts, reels, destaques, legendas publicas e paginas indexadas que mencionem o periodo, a cidade, local, horario, preco ou link.
4. Registrar internamente os 4 perfis consultados com `perfil`, `url`, `tipo` e `evidencia_encontrada`.
5. Usar eventos encontrados no Instagram somente quando houver evidencia publica suficiente e rastreavel. Preferir link do post/perfil oficial ou link da bio quando for o unico canal de venda/informacao.
6. Cruzar eventos vindos do Instagram com outra fonte sempre que possivel. Se o Instagram for a unica fonte, marcar no resumo uma observacao curta como "divulgado pelo perfil oficial/local".

Nao use conteudo privado, nao burle login, nao dependa de stories nao acessiveis publicamente e nao invente informacoes ausentes em artes ou legendas. Se o Instagram bloquear acesso direto, pesquisar a combinacao `site:instagram.com cidade evento periodo` e usar resultados publicos indexados, ou consultar perfis alternativos locais.

## Imagens

Quando gerar PDF, cada evento deve ter uma imagem retirada da mesma fonte usada para o evento ou da fonte oficial consolidada:

- Preferir `og:image`, `twitter:image` ou imagem principal da pagina do evento.
- Se a fonte de venda nao tiver imagem acessivel, usar imagem da pagina oficial do evento, produtor, equipamento cultural ou portal local que confirmou o evento.
- Nao usar imagens genericas, bancos de imagem, IA generativa ou imagens de fontes que nao falem daquele evento.
- Registrar internamente `imagem_url`, `imagem_fonte` e `fonte_nome` para cada evento antes de gerar o PDF.
- Se nao houver imagem rastreavel para um candidato, priorizar outro evento equivalente com imagem confirmada. So manter evento sem imagem se o usuario pedir explicitamente para nao descartar eventos incompletos.

## Workflow

1. Interpretar a cidade, o periodo, a categoria e a localizacao especifica.
2. Montar consultas combinando cidade, periodo, categoria e termos como agenda, eventos, ingressos, gratuito, prefeitura, Sympla, Eventbrite, Ticketmaster, Uhuu, Uhuu.com, G1, Catraca Livre e jornal local.
3. Elencar 4 perfis de Instagram da cidade e buscar evidencias publicas de eventos neles.
4. Coletar candidatos de multiplas fontes e manter o link mais confiavel para cada evento.
5. Normalizar nomes, datas, locais, categorias e precos.
6. Remover duplicados.
7. Priorizar eventos com local, data, horario, preco e link de venda ou informacao.
8. Retornar somente eventos que ocorram dentro do periodo solicitado e na cidade/regiao pedida.
9. Se a busca trouxer poucos resultados, ampliar para fontes oficiais, portais locais e novos perfis locais antes de devolver a resposta.
10. Quando o usuario pedir PDF, coletar imagem de fonte para cada evento e gerar o arquivo com `scripts/generate_event_pdf.py`.

## Deduplicacao

Considere duplicados os eventos com alta semelhanca de nome e mesma data ou mesmo local. Ao consolidar:

- Preferir o link oficial ou de venda direta.
- Preservar o menor preco confirmado quando houver faixa de valores.
- Completar dados faltantes usando fontes secundarias confiaveis.
- Manter apenas um registro por sessao/data quando o mesmo evento aparece em varios sites.
- Para temporadas, pecas e exposicoes com varias datas, incluir a data ou faixa relevante ao pedido.

## Priorizacao

Ordene por relevancia para o pedido, considerando:

- Correspondencia com periodo, cidade, categoria e bairro/ponto turistico.
- Completude: local, horario, preco e link.
- Fonte oficial ou fonte com venda ativa.
- Popularidade, destaque editorial, lotacao esperada ou sinais de demanda.
- Diversidade de categorias quando for "Mix de Destaques".

Para eventos gratuitos, confirme se o item e realmente gratuito ou se exige inscricao/retirada de ingresso. Use `preco` como "Gratuito" ou "Gratuito, mediante inscricao" quando aplicavel.

## Saida JSON

Quando o usuario pedir somente dados, responda em tom informativo, agil e prestativo, mas a entrega final deve ser somente JSON valido, sem Markdown e sem texto antes ou depois.

Para multiplos eventos, retorne um array de objetos. Cada objeto deve ter exatamente estas chaves:

```json
{
  "evento": "",
  "data_hora": "",
  "local": "",
  "categoria": "",
  "preco": "",
  "link_venda": "",
  "resumo": ""
}
```

Regras de preenchimento:

- `evento`: nome oficial ou nome mais reconhecivel.
- `data_hora`: data e horario em formato humano claro; use datas absolutas sempre que possivel.
- `local`: nome do espaco e bairro/cidade quando disponivel.
- `categoria`: categoria principal; use "Mix de Destaques" somente quando for uma selecao sem categoria unica.
- `preco`: valor, faixa de valores, "Gratuito", "Nao informado" ou "A confirmar".
- `link_venda`: URL oficial, pagina de ingressos ou pagina informativa mais confiavel.
- `resumo`: uma frase curta com o motivo do destaque e qualquer observacao pratica relevante.

Se nenhum evento confiavel for encontrado, retorne `[]`.

## Saida PDF

Quando o usuario pedir PDF, relatorio, roteiro visual, agenda diagramada ou material bonito:

1. Curar os eventos normalmente.
2. Criar um JSON interno com os campos obrigatorios e estes campos extras por evento: `imagem_url`, `imagem_fonte`, `fonte_nome`.
3. Salvar esse JSON em um arquivo de trabalho no diretorio do projeto atual.
4. Executar:

```bash
python C:/Users/ruben/.codex/skills/research-curadoria-eventos/scripts/generate_event_pdf.py --input eventos.json --output agenda-eventos.pdf --title "Agenda de eventos" --subtitle "Cidade e periodo pesquisados"
```

5. Conferir se o PDF foi criado e se cada card tem imagem.
6. Responder ao usuario com o caminho do PDF e, se util, mencionar que as imagens foram extraidas das fontes dos eventos.

O PDF deve ter layout editorial limpo, capa curta, cards com imagem, data/hora, local, categoria, preco, resumo e link clicavel. Nao despeje o JSON inteiro na resposta final quando o pedido principal for o PDF.

Por padrao, o script falha se algum evento ficar sem imagem. Se o usuario autorizar eventos incompletos, executar novamente com `--allow-missing-images`.

Em ambiente com sandbox, a renderizacao por navegador headless pode exigir aprovacao/escalacao; se a primeira tentativa criar apenas o HTML e falhar no PDF, repetir o mesmo comando com permissao apropriada.

O script aceita JSON como array de eventos ou como objeto:

```json
{
  "titulo": "Agenda de eventos",
  "subtitulo": "Jundiai, 1 a 3 de maio de 2026",
  "eventos": []
}
```
````

### research-pessoa-due-diligence

Origem: `$CODEX_HOME/skills/research-pessoa-due-diligence/SKILL.md`

````markdown
---
name: research-pessoa-due-diligence
description: Levantamento juridico, reputacional e de idoneidade documental de pessoa fisica com base em fontes publicas, oficiais ou autorizadas, reunindo documentos, links, processos, diarios oficiais, registros profissionais, sancoes, certidoes, sinais criminais publicos, informacoes militares publicas quando licitas e evidencias rastreaveis de boa ou ma conduta institucional. Use quando o usuario pedir investigacao juridica, due diligence, background check, "levantar tudo sobre uma pessoa", pesquisar processos, antecedentes, documentos, vinculos publicos, risco criminal, historico militar, certidoes, compliance, OSINT legal, reputacao, idoneidade, "indole" ou relatorio rastreavel sobre uma pessoa identificada ou parcialmente identificada.
---

# Pessoa Due Diligence

## Overview

Conduzir due diligence de pessoa fisica sem ultrapassar limites legais, eticos ou de privacidade. Priorizar fontes oficiais, registrar evidencias, distinguir homonimos e separar fatos documentados de hipoteses.

## Guardrails

- Trabalhar apenas com dados fornecidos pelo usuario, fontes publicas, bases oficiais, publicacoes legais ou fontes para as quais o usuario declara autorizacao.
- Nao burlar login, paywall, captcha, termos de uso, sigilo processual, segredo de justica, sistemas internos, bancos vazados ou fontes obtidas de forma ilicita.
- Nao tentar descobrir ou expor CPF completo, endereco residencial, telefone pessoal, e-mail pessoal, dados de familiares, dados bancarios, prontuario medico, biometria, senhas ou dados sensiveis nao necessarios.
- Mascarar identificadores sensiveis no relatorio final, salvo se o usuario ja os forneceu e pediu uso operacional: `123.***.***-45`, `***@dominio.com`.
- Nao afirmar que a pessoa cometeu crime sem condenacao ou documento oficial. Usar linguagem como "consta processo", "ha registro publico", "nao foi localizado registro publico", "pode haver homonimia".
- Para criminal, militar, seguranca ou antecedentes, limitar-se a registros publicos oficiais, diarios oficiais, tribunais, orgaos de controle, listas oficiais e documentos fornecidos/autorizados.
- Nao "comprovar indole" como verdade psicologica ou moral. Converter pedidos sobre indole em "evidencias documentais de idoneidade/reputacao", com fontes, limites e contraditorios.
- Nao produzir score de risco pessoal, perfil psicologico, inferencia de carater, diagnostico, previsao de crime ou conclusao discriminatoria. Usar categorias documentais: `sem achado relevante nas fontes consultadas`, `achado positivo`, `achado de atencao`, `achado critico`, `inconclusivo`.
- Se a finalidade parecer assedio, vigilancia pessoal, discriminacao, exposicao publica, doxxing ou decisao ilegal sobre emprego/credito/moradia, recusar essa finalidade e oferecer uma versao de compliance/licita e minimizada.

## Intake

Quando a pessoa nao estiver identificada com seguranca, pedir os dados minimos adicionais antes de pesquisar ou antes de concluir:

- Nome completo e grafias alternativas.
- Pais/estado/cidade provaveis e periodo de interesse.
- Data de nascimento ou faixa etaria, se o usuario puder fornecer.
- CPF, RG, OAB, CRM, matricula, nome dos pais ou outro identificador, preferencialmente parcial/mascarado.
- Finalidade declarada do levantamento e base de autorizacao quando houver dados nao publicos.
- Escopo desejado: civil, criminal, trabalhista, eleitoral, militar, societario, profissional, midia, sancoes, internacional.
- Nivel de profundidade: triagem rapida, relatorio completo, certidoes oficiais, ou matriz de idoneidade.

Se houver risco alto de homonimia, continuar a pesquisa, mas marcar cada achado como `confirmado`, `provavel`, `possivel homonimo` ou `descartado`, explicando o criterio.

## Workflow

1. Definir escopo, jurisdicao, finalidade e dados identificadores.
2. Montar matriz de identidade: nomes, aliases, documentos parciais, localidades, empresas, cargos, registro profissional, servico militar conhecido, datas.
3. Pesquisar fontes oficiais primeiro. Usar buscas web somente para descobrir paginas oficiais ou noticias relevantes, sempre abrindo e verificando a fonte primaria quando possivel.
4. Registrar cada achado com URL, orgao/fonte, data de consulta, termos usados, identificadores que conectam o achado a pessoa e nivel de confianca.
5. Cobrir areas conforme o escopo: processos judiciais, diarios oficiais, certidoes/consultas publicas, registros profissionais, empresas e socios, eleitorais, sancoes/listas oficiais, criminal publico, militar publico, midia confiavel e idoneidade documental.
6. Consolidar homonimos e conflitos. Nao mesclar pessoas diferentes sem identificador forte.
7. Classificar cada evidencia como favoravel, neutra, atencao, critica ou inconclusiva, sem transformar isso em julgamento moral absoluto.
8. Produzir relatorio com sumario executivo, tabela de evidencias, lacunas, riscos, recomendacoes de proximos passos licitos e anexos/links.

## Pesquisa

Ler `references/fontes-brasil.md` quando o caso envolver Brasil ou quando precisar de um mapa de fontes por categoria. Adaptar para outros paises usando a mesma logica: fonte oficial, autoridade competente, rastreabilidade e minimizacao de dados.

Ler `references/idoneidade-fontes.md` quando o usuario pedir indole, idoneidade, reputacao, confiabilidade, "se e boa pessoa", risco de contratar, negociar, emprestar, associar-se, conviver profissionalmente, ou quando o relatorio precisar ir alem de processos judiciais.

Ler `references/modelo-relatorio.md` antes de entregar um relatorio completo ou quando o usuario pedir "documentos, links e processos".

Quando houver HTML salvo do e-SAJ, usar `scripts/esaj_extract.py` para extrair listagem, detalhes, partes e movimentacoes antes de montar a tabela. Exemplo:

```bash
python scripts/esaj_extract.py caminho/para/tjsp_*.html --json saida.json
```

### Consultas judiciais e documentos

- Buscar por nome exato, variacoes do nome, CPF parcial quando fornecido, OAB/registro profissional, empresas relacionadas e localidades.
- Separar areas: civel, criminal, trabalhista, federal, eleitoral, militar, fazenda publica, familia/sucessoes quando publico.
- Para cada processo, coletar: numero CNJ, tribunal, classe, assunto, partes publicas, movimentacoes relevantes, status, segredo/sigilo quando indicado, link oficial.
- Nao tentar acessar processo sigiloso ou documentos restritos.

### Criminal

- Priorizar tribunais, diarios oficiais, ministerio publico, policias/listas oficiais, CNJ/BNMP quando publicamente acessivel, listas de procurados oficiais, Interpol e orgaos equivalentes.
- Diferenciar inquerito, acao penal, medida cautelar, mandado, condenacao, absolvido, arquivado, prescrito e extinto.
- Nao tratar noticia, boletim nao verificado ou homonimo como antecedentes.
- Quando nao houver fonte oficial suficiente, escrever "nao foram localizados registros publicos nas fontes consultadas", nunca "nada consta" de forma absoluta.

### Idoneidade e reputacao documental

- Buscar evidencias positivas e negativas. Exemplos positivos: certidoes negativas oficiais, regularidade profissional, ausencia de sancoes em cadastros oficiais consultados, exercicio publico/profissional regular documentado, historico societario sem sancoes localizadas, decisoes favoraveis ou arquivamentos documentados.
- Exemplos de atencao: execucoes fiscais, inadimplemento judicial, processos repetidos de cobranca, citacoes por edital, sancoes administrativas, inabilitacoes, impedimentos de licitar, condenacoes, mandados, punicoes profissionais, noticias relevantes confirmadas por documentos.
- Nao concluir "boa indole" ou "ma indole"; concluir apenas "os documentos consultados sustentam/nao sustentam sinais de idoneidade ou risco em X dimensoes".
- Procurar contraditorios: status atual do processo, arquivamento, extincao, pagamento, acordo, absolvição, prescricao, baixa, recurso, reforma, homonimia.
- Separar `risco juridico`, `risco financeiro-publico`, `risco reputacional`, `risco profissional/regulatorio`, `risco criminal publico` e `lacunas`.

### Militar

- Consultar apenas informacoes publicas: Justica Militar, STM/TJM, diarios oficiais, nomeacoes, promocoes, concursos, boletins publicados, condecoracoes, processos administrativos publicos, curriculos oficiais e documentos fornecidos pelo usuario.
- Nao buscar dados internos de quartel, ficha funcional reservada, servico obrigatorio individual, movimentacoes sensiveis, lotacao atual sensivel ou dados de seguranca sem fonte publica/autorizacao.
- Quando houver possivel vinculo militar, indicar orgao, posto/cargo se publico, periodo documentado e fonte.

## Output

Entregar em portugues, salvo pedido contrario. Usar esta estrutura:

- Escopo e dados usados.
- Sumario executivo com nivel geral de confianca.
- Identidade e criterios de desambiguacao.
- Tabela de achados: categoria, fato documentado, fonte, link, data de consulta, confianca, observacoes.
- Processos e documentos localizados.
- Matriz de idoneidade documental quando pedida: dimensao, evidencias favoraveis, evidencias de atencao, lacunas, leitura cautelosa.
- Achados criminais publicos, com cautela juridica.
- Achados militares publicos, com cautela de seguranca.
- Lacunas, fontes indisponiveis e proximos passos licitos.
- Aviso: levantamento informativo, nao certidao oficial nem parecer juridico.

## Quality Bar

- Preferir resultado menor e bem comprovado a lista longa de homonimos.
- Incluir links diretos e datas de consulta.
- Sinalizar limitações: sites fora do ar, bloqueios, necessidade de certidao oficial, dados insuficientes, jurisdicoes nao pesquisadas.
- Quando usar noticias ou fontes secundarias, indicar que sao secundarias e buscar confirmacao oficial.
- Nao deixar achado negativo sem contexto processual atual quando a fonte permitir verificar movimentacoes, status, extincao, arquivamento, absolvição ou recurso.
- Fazer perguntas de follow-up quando o proximo passo depender de dado identificador, jurisdicao ou autorizacao.
````

### weather-next-weekend-bh-sp

Origem: `$CODEX_HOME/skills/weather-next-weekend-bh-sp/SKILL.md`

````markdown
---
name: weather-next-weekend-bh-sp
description: List the weather forecast for the next weekend in Belo Horizonte, Jundiai, Guarulhos, and Sao Paulo city. Use when the user asks for "tempo", weather, forecast, chuva, temperatura, or weekend conditions for BH, Jundiai, Guarulhos, and SP together, especially for the upcoming Saturday and Sunday.
---

# Weather Next Weekend BH SP

## Workflow

1. Resolve the next weekend from the current date and the user's timezone.
   - Treat "proximo final de semana" as the next Saturday and Sunday.
   - If today is Saturday or Sunday, clarify in the answer whether using the current weekend or the following weekend based on the user's wording and the current date.
   - State the exact dates used.

2. Query weather for these locations:
   - Belo Horizonte, MG, Brazil
   - Jundiai, SP, Brazil
   - Guarulhos, SP, Brazil
   - Sao Paulo, SP, Brazil

3. Prefer a weather tool or authoritative forecast source available in the environment.
   - If a built-in weather tool is available, call it once per location with the Saturday start date and 2-day duration.
   - If using web sources, browse current forecast data because weekend forecasts change often.

4. Return a concise table in Portuguese with one row per city and separate Saturday/Sunday details.
   - Include condition, min/max temperature, precipitation chance or rain summary when available, and any notable alert.
   - Mention the source or tool used and the retrieval date.
   - If forecast data is unavailable for a city, say so explicitly instead of guessing.

## Output Format

Use this structure:

```markdown
Previsao para o proximo fim de semana: <sabado data> e <domingo data>.

| Cidade | Sabado | Domingo | Observacao |
| --- | --- | --- | --- |
| Belo Horizonte | ... | ... | ... |
| Jundiai | ... | ... | ... |
| Guarulhos | ... | ... | ... |
| Sao Paulo | ... | ... | ... |

Fonte: <tool/source>, consultado em <date>.
```
````
