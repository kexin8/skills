---
name: ask
description: Clarify a user's request through a one-question-at-a-time dialogue before completing it. Use only when the user explicitly invokes $ask or explicitly requests a sequential question-and-answer clarification flow; do not activate for ordinary ambiguous requests.
---

# Ask

These instructions apply only after the skill has been activated by `$ask` or an explicit request for sequential clarification. Once active, clarify the request with the least burdensome sequence of questions, then complete the original task from the clarified understanding.

## Dialogue

1. Read the conversation and available context before asking anything. Do not ask for information the user has already supplied or that can be discovered safely from the current environment.
2. Identify the unresolved decision whose answer would most change the result or the next question. If none remains, skip directly to completion.
3. Ask about exactly one decision per turn and wait for the answer. A single question may include mutually exclusive answer choices; those choices are not additional questions.
4. When the realistic answers form a small, meaningful set, offer two to four mutually exclusive choices, put the recommended choice first, explain each choice's effect briefly, and allow a custom answer. Otherwise ask one short open-ended question. Do not add a partial solution or unrelated advice.
5. After each answer, reconsider what remains unknown. Let the answer determine the next question instead of following a fixed questionnaire.
6. If the user answers with “either,” “I don't know,” “you decide,” or an equivalent non-preference, treat it as delegation: select the recommended safe default, record it as an assumption, and continue. If no safe default exists, ask a narrower question that explains the consequential choice without inferring authorization.
7. Use the user's language for every question, summary, and result.

## Stop asking

Normally ask no more than five questions. After the fifth answer:

- For low-risk, reversible work, choose reasonable defaults, state them, and proceed. Prefer a draft, prototype, or otherwise easy-to-revise result when the requested scope remains broad.
- For actions involving external communication, money, credentials, permissions, legal commitments, sensitive data, safety, production systems, deletion, or another hard-to-reverse effect, do not guess a consequential value or infer authorization. Continue only with the minimum question needed to resolve that blocker.

Stop earlier when:

- the request is sufficiently clear to produce a useful result;
- the user asks to proceed, stop asking, or use best judgment; or
- the plausible answers would change only cosmetic or easily reversible details.

A question is material when plausible answers would change the goal, deliverable, architecture or approach, substantial cost or effort, audience or external recipient, permissions, or a hard-to-reverse effect. Do not invent a numeric threshold for materiality; use these outcome differences as the test.

## Complete the request

When questioning ends, briefly restate the confirmed goal, material constraints, and any assumptions. Then continue the user's original task in the same response. Do not ask for an extra confirmation unless the action itself requires authorization or the summary exposes a genuine conflict.
