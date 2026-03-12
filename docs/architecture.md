# Architecture

## Core idea
This repository is skills-first, not playbook-first.

The primary unit is the domain pack under `skills/`.
Each pack represents a reusable Codex-native work capability:
- sales
- pm
- executive assistance
- research
- customer support

## Main layers

### 1. Skills layer
`skills/` is the core of the repository.
Each pack defines:
- a `SKILL.md`
- pack-specific templates
- pack-specific references
- pack-specific examples
- pack-specific validation scripts

### 2. Flow layer
`flows/` defines how work should move.
Flows are not top-level products here.
They are reusable process guides that support packs.

### 3. Gate layer
`gates/` defines quality checks before output is considered usable.
These gates protect sendability, signal quality, evidence quality, and handoff quality.

### 4. Artifact layer
`artifacts/` defines the shape of reusable output types.
Examples:
- ready-to-send draft
- weekly brief
- decision memo
- escalation note

### 5. Shared layer
`shared/` contains templates and references that are useful across packs.

### 6. Operations layer
`install/` and `scripts/` support practical installation, validation, and maintenance.

## Why there is no top-level playbooks directory
This repository is not organized around one linear pipeline.
It is organized around reusable domain capabilities.

A shipping-style repository naturally centers playbooks because the work follows a staged delivery path.
This repository centers packs because real-world work enters from different directions:
- a messy sales inquiry
- a PM status need
- an executive brief request
- a comparison memo
- a support escalation

## Quality target
The repository should be understandable as a system, not just as a file dump.
A reader should quickly understand:
- what the core unit is
- how packs relate to flows, gates, and artifacts
- how a real case can move across multiple packs
