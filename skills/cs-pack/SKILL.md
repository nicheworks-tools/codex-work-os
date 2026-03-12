---
name: cs-pack
description: Use this pack for support case summaries, escalation notes, customer-safe reply drafts, and issue handoff materials built from messy tickets, threads, or support notes.
---

# CS Pack

## Purpose
Turn messy support context into concise, actionable customer support outputs.

## Use this pack when
- a support case is too long or noisy
- an escalation note is needed for engineering or management
- a safe customer-facing reply draft is needed
- support notes must be turned into a handoff artifact
- the user needs impact, reproduction clues, and next steps clarified

## Do not use this pack when
- the request is mainly a PM status brief
- the task is a research or decision memo
- the main need is a sales reply
- the request is executive meeting support
- the task is implementation rather than issue communication

## Inputs
- support thread, ticket text, or case notes
- user-facing symptoms
- current severity and impact
- reproduction clues if known
- actions already taken if known

## Required behavior
1. Summarize the problem clearly.
2. Surface impact and urgency early.
3. Preserve reproduction clues and evidence.
4. Avoid blame language and speculation.
5. End with a concrete next step or escalation direction.

## Default output order
1. Case summary
2. User impact
3. Evidence / reproduction
4. Actions already taken
5. Escalation recommendation
6. Ready-to-send escalation note or safe reply

## Quality standard
A useful CS output should help the next owner understand:
- what the issue is
- who is affected
- what evidence exists
- what has already been tried
- what should happen next

## Use with
- ../../flows/cs-escalation-flow.md
- ../../gates/sendability-gate.md
- ../../artifacts/escalation-note.md
- ./templates/ticket-summary.md
- ./templates/escalation-brief.md
- ./references/cs-response-rules.md
