# codex-work-os

A Codex-native operating system for real work beyond coding.

This repository is designed to help Codex handle recurring cross-functional work more reliably through:

- research and comparison work
- PM summaries and status reporting
- sales reply drafting and lead triage
- executive briefing and meeting prep
- customer support summarization and escalation prep

It is **not** a generic PM toolkit.
It is **not** a prompt dump.
It is **not** a clone of another public skills repository.
Its native structure is built around:

- Codex-ready `skills/`
- shared operating rules in `AGENTS.md`
- reusable `templates/`
- supporting `references/`
- lightweight validation and install scripts
- examples and specs

---

## What this repository is for

This repository exists to make recurring work easier to repeat inside Codex in a consistent, reusable, and reviewable way.

It is for cases where you want Codex to do practical work such as:

- turning messy notes into an executive-ready brief
- turning scattered updates into a weekly PM status report
- drafting a sales reply from a Slack thread or email notes
- comparing options and turning them into a decision memo
- summarizing a support case before escalation

The goal is to support **real work outputs**, not just nice sounding AI prose.

---

## Core model

The native structure of this repository is:

- **skills** for reusable Codex behaviors
- **shared templates** for consistent output structure
- **references** for tone, safety, and prioritization guidance
- **install scripts** for moving packs into Codex-readable skill directories
- **validation scripts** for repository hygiene and structural checks
- **examples** that prove how each pack should be used
- **spec** documents that define the source-of-truth project intent

If compatibility with another format is needed later, handle it through adapters or separate exports.
The native structure should remain primary.

---

## Current pack set

The repository currently includes five pack-level skills:

1. `research-pack`
2. `pm-pack`
3. `sales-pack`
4. `exec-assist-pack`
5. `cs-pack`

Together they cover a practical loop from information intake to structured output and handoff.

---

## Why use this with Codex

The value of this project is not abstract business theory.

The value is that it helps Codex answer practical questions such as:

- What information matters most in this request?
- What format should the answer take to be immediately usable?
- What should be separated into facts, assumptions, and recommendations?
- What risks or missing inputs should remain visible?
- What next action should the user take after reading the output?
- What draft can be sent or pasted with minimal editing?

In other words, this repository is meant to help Codex do better operational work **as Codex**, not just imitate generic prompt behavior.

---

## Start here

If you are new to the repository, use this order:

1. `AGENTS.md`
2. `spec/`
3. `docs/vision.md`
4. `docs/roadmap.md`
5. `skills/`
6. `examples/`
7. `install/`

This gives you the rules, the source-of-truth intent, the staged roadmap, the reusable packs, concrete usage proofs, and installation methods.

---

## Maturity model

This repository is designed to move through these stages:

- **Phase 0: Seed** — empty structure and naming only
- **Phase 1: Foundation** — core repo structure, AGENTS, README, spec, install path
- **Phase 2: MVP** — shared templates, usable skill packs, examples, lightweight scripts
- **Phase 3: Pack Coverage** — all five packs are materially usable
- **Phase 4: Internal RC** — docs, spec, examples, validation, and install flow feel cohesive
- **Phase 5: Publication Grade** — real-world validation, stronger examples, CI, public polish

This current draft is intended to land around **Phase 4: Internal RC**.
It is significantly beyond an empty skeleton, but it is not yet a proven public release.

---

## Repository structure

```text
codex-work-os/
├─ AGENTS.md
├─ README.md
├─ DISCLAIMER.md
├─ LICENSE
├─ .github/
├─ spec/
├─ docs/
├─ skills/
├─ shared/
├─ examples/
├─ install/
└─ scripts/
```

---

## Basic usage

### Option A: personal installation

Clone this repository and install one or more packs into `~/.agents/skills`.

Example:

```bash
bash install/install-symlinks.sh research-pack pm-pack
```

Then open any working repository in Codex and ask for work naturally.

Examples:

- “Turn these notes into a weekly PM status update.”
- “Draft a polite sales reply from this Slack thread.”
- “Compare these two proposals and write a decision memo.”
- “Prepare a short executive brief for this meeting.”
- “Summarize this support case for escalation.”

### Option B: project-local installation

Copy selected packs into a project-local `.agents/skills/` directory when you want the pack set to travel with one repository.

---

## What this repository is not

This project is not intended to become:

- a general business self-help library
- a giant prompt archive
- a vague “AI productivity” repo
- a framework that ignores Codex-specific operating behavior

---

## Publisher

Published by **NicheWorks**.

Website:

- `https://nicheworks.app/`

---

## Support

If this project is useful, you can support NicheWorks here:

- Ko-fi: `https://ko-fi.com/nicheworks`
- OFUSE: `https://ofuse.me/nicheworks`

GitHub funding metadata is also included through `.github/FUNDING.yml`.

---

## Disclaimer

This repository is provided as a workflow resource.

Nothing here should be treated as a guarantee of correctness, safety, completeness, policy compliance, data accuracy, delivery quality, or business outcome.

For the full disclaimer, see:

- `DISCLAIMER.md`
