# Skills pessoais do Codex

Gerado em 2026-05-04 (America/Sao_Paulo).

Escopo: somente skills criadas pelo usuario em `$CODEX_HOME/skills`. Foram excluidas as skills originais do Codex em `.system` e as skills vindas de plugins/cache.

## Resumo

| Metrica | Total |
| --- | ---: |
| Skills pessoais catalogadas | 7 |

## Catalogo

| Skill | Arquivo | Descricao |
| --- | --- | --- |
| `company-jobs` | [skills/company-jobs/SKILL.md](../skills/company-jobs/SKILL.md) | Find current job openings from a company's official website or careers page. Use when the user asks to read a company site, careers page, ATS board, or recruitment page and return all available vacancies, roles, jobs, positions, openings, or "vagas"; also use when the user provides only a company name and wants current hiring opportunities. |
| `curadoria-eventos` | [skills/curadoria-eventos/SKILL.md](../skills/curadoria-eventos/SKILL.md) | Buscar, curar e retornar eventos atuais para uma cidade usando fontes oficiais, APIs, portais locais, Instagram/redes sociais e inteligencia de eventos, com opcao de gerar PDF bonito com imagem de fonte para cada evento. Use quando o usuario pedir eventos, agenda cultural, shows, gastronomia, eventos corporativos, eventos gratuitos, programacao de fim de semana, o que fazer, roles, destaques por data, periodo, categoria, bairro, ponto turistico ou cidade, ou quando pedir um PDF/relatorio visual da agenda. |
| `gemini-interview-prep-prompt` | [skills/gemini-interview-prep-prompt/SKILL.md](../skills/gemini-interview-prep-prompt/SKILL.md) | Create a ready-to-paste Gemini prompt that turns Gemini into a rigorous, concise, respectful interview preparation coach and evaluator. Use when the user provides a professional CV/resume, LinkedIn/profile information, job description, extra context, hiring-process stage, recruiter notes, interview format, or asks to generate a prompt for Gemini to prepare someone for a job interview, mock interview, technical interview, HR screening, hiring-manager conversation, case interview, panel interview, or final interview. |
| `job-fit-evaluator` | [skills/job-fit-evaluator/SKILL.md](../skills/job-fit-evaluator/SKILL.md) | Evaluate whether a job posting, recruiter message, LinkedIn role, or vacancy description is compatible with Ruben's CV, experience, target job profile, preferences, and positioning. Use when asked to assess job fit, match a role to the user's background, identify gaps, decide whether to apply, tailor a CV/profile summary, or explain how well a position aligns with the user's experience. |
| `pessoa-due-diligence` | [skills/pessoa-due-diligence/SKILL.md](../skills/pessoa-due-diligence/SKILL.md) | Levantamento juridico, reputacional e de idoneidade documental de pessoa fisica com base em fontes publicas, oficiais ou autorizadas, reunindo documentos, links, processos, diarios oficiais, registros profissionais, sancoes, certidoes, sinais criminais publicos, informacoes militares publicas quando licitas e evidencias rastreaveis de boa ou ma conduta institucional. Use quando o usuario pedir investigacao juridica, due diligence, background check, "levantar tudo sobre uma pessoa", pesquisar processos, antecedentes, documentos, vinculos publicos, risco criminal, historico militar, certidoes, compliance, OSINT legal, reputacao, idoneidade, "indole" ou relatorio rastreavel sobre uma pessoa identificada ou parcialmente identificada. |
| `prd-to-codex-prompt` | [skills/prd-to-codex-prompt/SKILL.md](../skills/prd-to-codex-prompt/SKILL.md) | Create a clear, complete initial prompt for OpenAI Codex from a Product Requirements Document (PRD). Use when the user wants to turn a PRD, product spec, feature brief, ticket, or requirements document into a Codex-ready prompt for implementation, refactoring, debugging, review, testing, or planning. The skill must require the user to provide or attach a PRD before drafting the prompt. |
| `tailor-cv-to-job` | [skills/tailor-cv-to-job/SKILL.md](../skills/tailor-cv-to-job/SKILL.md) | Adapt an existing editable CV/resume to a specific job description while preserving the original document formatting and generating a PDF. Use when the user sends a vacancy/job description and asks to tailor, reescrever, otimizar para ATS, adaptar CV/curriculo/resume, extrair palavras-chave da vaga, update the Objective/Objetivo section, or create a PDF named for the candidate and job title without inventing experience or changing real job history. If the only source is PDF, use this skill only to save/analyze the original and request an editable source before producing the final formatted CV. |

## Conteudo completo

### company-jobs

Origem: `$CODEX_HOME/skills/company-jobs/SKILL.md`

````markdown
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
````

### curadoria-eventos

Origem: `$CODEX_HOME/skills/curadoria-eventos/SKILL.md`

````markdown
---
name: curadoria-eventos
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
python C:/Users/ruben/.codex/skills/curadoria-eventos/scripts/generate_event_pdf.py --input eventos.json --output agenda-eventos.pdf --title "Agenda de eventos" --subtitle "Cidade e periodo pesquisados"
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

### gemini-interview-prep-prompt

Origem: `$CODEX_HOME/skills/gemini-interview-prep-prompt/SKILL.md`

````markdown
---
name: gemini-interview-prep-prompt
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

### job-fit-evaluator

Origem: `$CODEX_HOME/skills/job-fit-evaluator/SKILL.md`

````markdown
---
name: job-fit-evaluator
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

### pessoa-due-diligence

Origem: `$CODEX_HOME/skills/pessoa-due-diligence/SKILL.md`

````markdown
---
name: pessoa-due-diligence
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

### prd-to-codex-prompt

Origem: `$CODEX_HOME/skills/prd-to-codex-prompt/SKILL.md`

````markdown
---
name: prd-to-codex-prompt
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

### tailor-cv-to-job

Origem: `$CODEX_HOME/skills/tailor-cv-to-job/SKILL.md`

````markdown
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
````

