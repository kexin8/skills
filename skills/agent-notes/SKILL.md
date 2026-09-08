---
name: agent-notes
description: Maintain durable engineering decision records in .agents/notes during non-trivial codebase changes. Use for architecture, public API or protocol, cross-module responsibility, persistence, security, infrastructure, testing-strategy, or important workflow decisions; skip mechanical edits, ordinary bug fixes, and local refactors that introduce no durable tradeoff.
---

# Agent Notes

Preserve why a consequential engineering choice exists, what was rejected, its consequences, and how it is verified. Notes complement code and current documentation; they are not task logs, implementation plans, or summaries of every change.

## On first use in a repository

If `.agents/notes/README.md` or the root `AGENTS.md` trigger rule is missing, run:

```bash
python3 <skill-directory>/scripts/bootstrap.py <repository-root>
```

Review the generated files before continuing. The bootstrap is additive: it refuses to overwrite existing Note policy files and inserts a marked root rule only when absent. If the repository already has an Agent Notes convention, follow it instead of replacing it.

Read [references/convention.md](references/convention.md) before creating or changing a Note. It is the source of truth for classification, file format, and lifecycle transitions.

## Decide whether a Note is warranted

Create or update a Note when the work makes a durable choice involving architecture, public API or protocol, cross-module ownership, persistence, security, infrastructure, testing strategy, or an important engineering workflow.

Skip a new Note when the change is mechanical, a routine dependency refresh, a local implementation detail, an ordinary bug fix restoring already-intended behavior, or a refactor with no durable tradeoff. Update an existing implemented Note when those edits make its factual paths, symbols, defaults, or mechanisms stale.

When uncertain, use this test: would a future maintainer plausibly undo or contradict the choice because its rationale is absent from code and current docs? If not, do not create a Note.

## Work with the active decision set

Before designing or editing, search `proposed/`, `implemented/`, and `rejected/` by concepts, affected modules, APIs, and mechanisms—not only titles. Do not treat `archived/` as current authority.

- Follow an applicable active decision.
- Update factual realization in an implemented Note without rewriting its original decision.
- Create a proposed Note for a genuinely new decision.
- If the new choice reverses or replaces an old one, cross-link both Notes. Archive a fully superseded implemented Note; keep a partially superseded Note active and state the remaining scope.
- Do not silently edit a decision into its opposite.

## Keep the lifecycle synchronized

Create a proposal before or alongside implementation once the decision is concrete enough to state. Keep it focused on rationale and acceptance criteria rather than narrating work.

At task completion, reconcile the Note with what actually happened:

- Shipped: move it to `implemented/`, change the status, and rewrite proposal-era sections into present-tense decision, consequences, and verification.
- Declined: move it to `rejected/`, keep the proposal context, and put the one-line rejection reason in the status.
- Still unresolved or only partly shipped: leave it proposed and say what remains unresolved. Never mark it implemented merely because coding stopped.
- No longer useful as current guidance: move an implemented Note to `archived/`. Archived Notes are frozen; supersede them with a new active Note rather than editing them.

Do not create a centralized index. Find Notes through their lifecycle/class paths and repository search.

## Validate

After every Note creation, edit, or move, run:

```bash
python3 <skill-directory>/scripts/validate.py <repository-root>
```

Fix all reported structural and format errors. Also run the repository's normal validation. Mechanical validation cannot prove that a missing Note was warranted or that the rationale is truthful; check those points during review.
