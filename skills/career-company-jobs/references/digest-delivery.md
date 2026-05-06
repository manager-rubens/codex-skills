# Digest Delivery

Read this file when the user wants company-job results delivered as an HTML email digest through Google Apps Script or Gmail.

## Goal

Deliver the same final formatted HTML email the user expects from the Apps Script renderer, and leave only that final digest visible in the inbox.

## Choose the Template

- Use `template: "job-alerts"` for aggregated or multi-company digests.
- Use `template: "career-company-jobs"` for a single-company digest.

## Canonical Layout

- The canonical manual fallback layout lives in `assets/job-fit-digest-template.html`.
- Match the Apps Script section order:
  - header with `Job Fit Digest - DD/MM/YYYY`
  - headline
  - stats pills
  - `Principais sinais`
  - `Melhores matches`
  - `Outras boas opcoes`
  - `Ignorados nesta varredura`
  - final `Observacao`
- Preserve the same subject line as the intended final digest.
- Preserve the sender expectation whenever the Apps Script path is available: the final digest should come from `Ruben Job Fit Alerts`.

## Payload Contract

Build a UTF-8 JSON payload with at least:

```json
{
  "template": "job-alerts",
  "token": "<apps-script-token>",
  "to": "manager.rubens@gmail.com",
  "subject": "Vagas Empresa A e Empresa B - YYYY-MM-DD",
  "headline": "Ruben, encontrei N vagas abertas nas empresas-alvo com analise de fit.",
  "stats": {
    "emailsScanned": 0,
    "jobsExtracted": 0,
    "jobsSelected": 0
  },
  "signals": [],
  "jobs": [],
  "otherJobs": [],
  "ignored": [],
  "note": "Fontes oficiais verificadas."
}
```

For PowerShell delivery to the Web App:

```powershell
$json = $payload | ConvertTo-Json -Depth 6
$bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
Invoke-RestMethod -Uri $endpoint -Method Post -ContentType 'application/json; charset=utf-8' -Body $bytes
```

Do not replace accents with HTML entities in the JSON payload.

## Preferred Delivery Path

1. Send the payload to the Apps Script Web App.
2. Validate the JSON response.
3. If `ok=true`, stop.

## Required Fallback Path

If the Web App fails because of network error, timeout, invalid response, or `ok=false`:

1. Do not send a simplified summary email.
2. Do not leave a raw JSON payload visible in inbox as the final state.
3. Send the raw payload JSON through Gmail relay:
   - `to`: the processing mailbox
   - `subject`: `[JOB_DIGEST_PAYLOAD] <automation-id> YYYY-MM-DD`
   - `body`: the raw JSON only, with no prose before or after it
4. Check for the final rendered digest with:
   - sender `Ruben Job Fit Alerts`
   - the expected final subject
   - snippet starting with the digest header rather than JSON
5. Archive the relay payload email after the final digest appears.
6. Archive any temporary helper or manual resend used during recovery, leaving only the final formatted digest in inbox.

## Manual Recovery Only If Needed

If the Apps Script relay does not produce the final email soon enough and a human-readable email must still be sent immediately:

1. Render the message from `assets/job-fit-digest-template.html`.
2. Keep the exact section order and visual hierarchy used by the Apps Script template.
3. Once the Apps Script-rendered digest appears later, archive the manual recovery email so the inbox keeps only the canonical digest.

## Verification Checklist

Before closing the task, confirm all of the following:

- the final digest subject is correct
- the final digest is HTML, not plain text
- no raw JSON payload email remains visible in inbox
- no simplified fallback email remains visible in inbox
- top jobs and other jobs are sorted correctly
- limitations and confidence reductions are explicit when detail pages were partial

## Common Failure Pattern

The main failure to avoid is:

- Web App POST fails
- a plain-text or ad hoc HTML fallback is sent
- the raw relay payload stays in inbox
- the recipient sees duplicate or malformed messages

Always drive the task to the cleaned-up end state: one final digest in HTML, no helper messages visible.
