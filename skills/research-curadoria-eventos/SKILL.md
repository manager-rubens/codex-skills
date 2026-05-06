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
