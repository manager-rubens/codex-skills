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
