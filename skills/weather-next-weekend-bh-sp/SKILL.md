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