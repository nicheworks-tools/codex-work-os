# Pack Mapping

## Purpose
This document maps packs to their most natural supporting flows, gates, and artifacts.

## Mapping

### sales-pack
- Flow: `flows/sales-response-flow.md`
- Gates: `gates/sendability-gate.md`
- Artifact: `artifacts/ready-to-send-draft.md`

### pm-pack
- Flow: `flows/pm-brief-flow.md`
- Gates: `gates/summary-quality-gate.md`
- Artifact: `artifacts/weekly-brief.md`

### exec-assist-pack
- Flow: `flows/exec-brief-flow.md`
- Gates: `gates/brief-signal-gate.md`, `gates/summary-quality-gate.md`
- Artifact: `artifacts/ready-to-send-draft.md`

### research-pack
- Flow: `flows/research-memo-flow.md`
- Gates: `gates/decision-memo-gate.md`, `gates/evidence-quality-gate.md`
- Artifact: `artifacts/decision-memo.md`

### cs-pack
- Flow: `flows/cs-escalation-flow.md`
- Gates: `gates/handoff-quality-gate.md`, `gates/sendability-gate.md`
- Artifact: `artifacts/escalation-note.md`

## Rule of use
Start with the pack that matches the primary work type.
Then apply the relevant flow, gate, and artifact.
