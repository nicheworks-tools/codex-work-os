# Workflows

## Overview
This repository supports both single-pack and cross-pack workflows.

## Single-pack workflows

### Sales workflow
Use when the main need is inquiry triage or a reply draft.
Typical route:
- sales-pack
- sales-response-flow
- sendability-gate
- ready-to-send draft

### PM workflow
Use when the main need is a status brief, blocker map, or progress digest.
Typical route:
- pm-pack
- pm-brief-flow
- summary-quality-gate
- weekly brief

### Executive workflow
Use when the main need is a fast leader-facing brief.
Typical route:
- exec-assist-pack
- exec-brief-flow
- brief-signal-gate
- ready-to-send draft

### Research workflow
Use when the main need is a comparison or decision memo.
Typical route:
- research-pack
- research-memo-flow
- decision-memo-gate
- evidence-quality-gate
- decision memo

### CS workflow
Use when the main need is a case summary or escalation handoff.
Typical route:
- cs-pack
- cs-escalation-flow
- handoff-quality-gate
- escalation note

## Cross-pack workflows
Real work often moves across multiple packs.

Example sequence:
1. Start with messy input
2. Use research-pack to clarify options
3. Use pm-pack to turn progress and blockers into an operational brief
4. Use exec-assist-pack to prepare a leadership summary
5. Use sales-pack to draft outward-facing communication
6. Use cs-pack if a live issue requires escalation

See:
- `docs/pack-mapping.md`
- `docs/end-to-end-scenarios.md`
- `examples/end-to-end/`
