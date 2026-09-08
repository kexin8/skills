# Agent Notes convention

This is a compact convention compatible with the core DeepSeek Harness Agent Notes model. Repository-specific bilingual pairs, archive manifests, and custom build tooling are intentionally excluded.

## Paths

Use:

```text
.agents/notes/<lifecycle>/<class>/yyyy-mm-dd-topic-title.md
```

The date is when the topic was first proposed and does not change during moves. Use lowercase kebab-case for the topic title.

Lifecycles:

- `proposed`: an undecided or not-fully-shipped proposal.
- `implemented`: a shipped decision kept accurate about current realization.
- `rejected`: a considered proposal that was declined and remains useful to prevent repetition.
- `archived`: frozen history that is no longer current guidance.

Classes:

- `feature`: a user- or model-facing capability.
- `bug-fix`: a non-obvious corrective decision, not an ordinary defect repair.
- `simplification`: intentional removal of behavior or surface area.
- `architecture`: structure, module boundaries, or runtime vocabulary.
- `process`: engineering tooling, policy, delivery, or workflow.
- `testing`: test infrastructure or strategy.

Choose the class representing the decision, not merely the files changed.

## Shared header

The first three lines are:

```markdown
# Agent Note: Descriptive title

Status: proposed
```

The status must match the lifecycle directory. Accepted status forms are exactly:

```text
Status: proposed
Status: implemented
Status: rejected — concise reason
```

Archived files retain `Status: implemented` because they record a decision that did ship.

## Proposed body

```markdown
## Problem

Why a durable decision is needed.

## Proposal

The proposed choice and its boundaries.

## Alternatives considered

Meaningful alternatives and why they are not preferred.

## Acceptance criteria

Observable conditions for considering the decision implemented.

## Risks

Tradeoffs, failure modes, and mitigations.
```

## Implemented body

Rewrite plans as shipped facts; do not merely change the status line.

```markdown
## Problem

Why the decision was needed.

## Decision

What is now implemented, in present tense, including important boundaries.

## Alternatives considered

Meaningful rejected alternatives and rationale.

## Consequences

Benefits, costs, constraints, and follow-on effects.

## Verification

Tests, checks, or observable evidence that pins the behavior.
```

`## Verification` is strongly expected but may be omitted only when verification is fully and concretely covered under `## Consequences`.

## Rejected body

Keep the proposal structure so readers can understand what was declined. The one-line verdict belongs in `Status: rejected — ...`. Do not add a parallel decision that was never implemented.

## Cross-links and supersession

Use relative Markdown links for related Notes. A replacing Note must identify what it supersedes and whether replacement is full or partial. A partially superseded Note stays active with its remaining authoritative scope stated clearly. A fully superseded implemented Note moves to `archived/` only after the replacement is active.

Never edit archived content. If archived history is wrong or incomplete, explain the correction in a new active Note that links back to it.
