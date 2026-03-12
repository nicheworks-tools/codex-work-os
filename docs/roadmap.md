# Roadmap

## Purpose of this document

This roadmap describes the staged development path of the repository from zero state to publication-grade quality.

The midpoint is **MVP**.
The practical goal is to reach a level comparable to a serious internal playbook repository.

---

## Phase 0: Seed

### Goal
Create the bare directory structure and naming system.

### Main targets
- top-level folders exist
- placeholder files exist
- naming direction is fixed

### Expected result
The repository can be recognized, but not used.

---

## Phase 1: Foundation

### Goal
Establish the repo identity and Codex-native rules.

### Main targets
- write `README.md`
- write `AGENTS.md`
- write spec documents
- define pack names and structure
- add install path design
- add disclaimer and license

### Expected result
The repository has a real identity and clear direction.
It is still early, but no longer empty.

---

## Phase 2: MVP

### Goal
Make the first practical working version of the repo usable.

### Main targets
- create shared templates
- create working install scripts
- create repository validation scripts
- write usable `SKILL.md` files for all five packs
- add at least one example per pack

### Expected result
A user can install packs, understand the structure, and start using the repo with Codex.
This is the minimum viable operational loop.

---

## Phase 3: Pack Coverage

### Goal
Make each pack materially useful, not just present.

### Main targets
- strengthen pack-specific templates
- strengthen pack-specific references
- improve examples
- reduce overlap between packs
- improve usage docs

### Expected result
All five packs feel distinct and workable.
The repository is meaningfully beyond MVP.

---

## Phase 4: Internal RC

### Goal
Raise the quality to a cohesive internal-release level.

### Main targets
- tighten docs and architecture explanations
- refine install and uninstall flows
- improve repository scripts
- complete source-of-truth specs in English and Japanese
- make examples and templates feel internally consistent

### Expected result
The repository feels like a serious internal operating system, not a sketch.
It is close to public quality but still lacks real-world proof.

### This draft target
This generated draft is intended to land around **Phase 4**.

---

## Phase 5: Publication Grade

### Goal
Prepare the repository for public release.

### Main targets
- validate packs in real Codex workflows
- improve documentation based on actual use
- add CI or automated checks
- improve public-facing clarity
- refine naming after proof, not before

### Expected result
The repository is no longer just internally coherent.
It is validated, explainable, and ready for outside users.

---

## What should not happen

### Failure mode 1: generic drift
The repo becomes a vague business prompt collection.

### Failure mode 2: clone drift
The repo starts to resemble a public skill repo too closely.

### Failure mode 3: pack blur
The packs overlap so much that users cannot tell which one to install or invoke.

### Failure mode 4: template sprawl
The repo gains many files without getting more usable.

### Failure mode 5: publication before proof
The repo is polished for public release before it is validated in real work.
