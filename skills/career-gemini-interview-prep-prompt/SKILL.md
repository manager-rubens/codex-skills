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
