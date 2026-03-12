# AGENTS.md

## Purpose of this repository

This repository is an original **Codex work operating system** for non-dev and cross-functional workflows.

It is not:

- a generic PM toolkit
- a clone of another public skills repository
- a loose pile of prompts
- a writing-only prompt pack

Its job is to help work move more consistently from:

- rough intake
- structured synthesis
- decision support
- communication drafting
- operational handoff

The native structure of the repository is built around:

- `skills/`
- `shared/templates/`
- `shared/references/`
- `install/`
- `scripts/`
- `examples/`
- `spec/`

---

## Core rules

### 1. Work output first
Favor outputs that help a user act.

Priority goes to:

- clear summaries
- structured decision support
- practical next steps
- ready-to-send drafts
- explicit risks and gaps

Do not let the repository drift into a generic inspiration library.

### 2. Codex-native behavior
This repo should encode behavior that is useful **inside Codex**.

That means:

- reusable skill packs
- stable output ordering
- explicit “when to use / when not to use” rules
- references that reduce style drift
- scripts that encourage consistency

### 3. Facts, assumptions, recommendations
Whenever practical, keep these distinct.

A strong output should make it easy to see:

- what is known
- what is inferred
- what is recommended next

### 4. Handoff quality matters
A skill output is incomplete if the user still has to guess what to do next.

Whenever practical, include:

- next action
- remaining unknowns
- draft language or a reusable structure

### 5. Real-world sendability
For replies, briefs, and summaries, prefer outputs that can be pasted or adapted quickly.

Avoid:

- fluffy transitions
- over-hedged filler
- ornamental prose with no operational value

---

## Clean-room rules

This repository may learn from public ideas, but it must remain original in wording, structure, naming, examples, and public framing.

### Allowed

- learning from public workflow ideas
- learning from broad operational patterns
- solving similar work problems from scratch
- building equivalent capabilities in a new structure

### Not allowed

- copying README wording
- copying another repo’s section order line by line
- copying template text too closely
- copying naming in a way that makes the repo feel derivative
- reproducing another project’s public identity

When in doubt, rewrite from first principles.

---

## Structural rules

### Layer responsibilities

- `skills/`
  Codex-ready reusable pack-level behaviors

- `shared/templates/`
  Reusable output scaffolds

- `shared/references/`
  Cross-pack style, safety, and prioritization guidance

- `install/`
  Installation helpers for personal or project-local use

- `scripts/`
  Repository validation and markdown hygiene helpers

- `examples/`
  Usage proofs and sample requests

- `spec/`
  Source-of-truth intent documents

### Required separation
Do not blur these layers.

Examples:

- broad style rules belong in `shared/references/`
- Codex pack instructions belong in `skills/*/SKILL.md`
- install logic belongs in `install/`
- repository checks belong in `scripts/`

---

## Rules for skill packs

### One folder, one pack
Each folder under `skills/` should represent one reusable pack-level skill.

Good examples:

- `pm-pack`
- `research-pack`
- `sales-pack`

Bad examples:

- `misc`
- `useful-prompts`
- `general-business`

### Required file
Each pack must include:

- `SKILL.md`

It may also include:

- `templates/`
- `references/`
- `scripts/`

### Every `SKILL.md` must make these points clear

- what the pack is for
- when to use it
- when not to use it
- what inputs it expects
- what outputs it should produce
- what shared templates or references it relies on
- what mistakes to avoid

### Naming rule
Use action-capable, operational names for sections and examples.
Avoid vague branding language.

---

## Output rules

When practical, prefer this order:

1. Goal
2. Current situation
3. Key points
4. Risks or missing inputs
5. Recommended next actions
6. Ready-to-send or ready-to-use draft

Not every pack needs every section, but outputs should feel stable and reusable.

---

## Repository evolution rules

This repository should grow in a controlled way.

Expansion is allowed when it improves:

- Codex usability
- output consistency
- installation clarity
- reviewability
- real-world usefulness

Expansion should not turn the repo into:

- a generic business wiki
- a template swamp
- a compatibility-first clone
- a social-media-facing inspiration pack
