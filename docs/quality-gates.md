# Quality Gates

## Purpose
Quality gates are reusable checks that improve output reliability before delivery or handoff.

## Gates in this repository

### sendability-gate
Use before finalizing any outward-facing draft.

### summary-quality-gate
Use before finalizing PM-style summaries or digests.

### decision-memo-gate
Use before finalizing recommendations or comparison memos.

### brief-signal-gate
Use before finalizing executive-facing briefs.

### handoff-quality-gate
Use before finalizing escalations or ownership handoffs.

### evidence-quality-gate
Use before finalizing evidence-heavy memos or recommendations.

## Practical use
A pack should normally be paired with at least one relevant gate.

Examples:
- sales-pack -> sendability-gate
- pm-pack -> summary-quality-gate
- exec-assist-pack -> brief-signal-gate
- research-pack -> decision-memo-gate + evidence-quality-gate
- cs-pack -> handoff-quality-gate (+ sendability-gate if customer-facing)

## Design rule
Do not add gates just to increase file count.
Each gate should protect a real failure mode in actual work.
