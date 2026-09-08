#!/usr/bin/env python3
"""Add the minimal Agent Notes policy to a repository without overwriting it."""

from __future__ import annotations

import argparse
from pathlib import Path


MARKER = "<!-- agent-notes-skill -->"
ROOT_RULE = f"""{MARKER}
## Engineering decisions

For non-trivial architecture, public API or protocol, cross-module responsibility,
persistence, security, infrastructure, testing-strategy, or important workflow
changes, use the `agent-notes` skill. Inspect active `.agents/notes` before
implementation and reconcile the Note lifecycle with what ships.
"""

NOTES_POLICY = """# Agent Notes

Agent Notes are durable engineering proposals and decision records. Before a
non-trivial change, search active Notes for applicable or superseded decisions.
Keep implemented Notes factually aligned with shipped code. Files in `archived/`
are frozen history and are not current authority.

Use the `agent-notes` skill for the format, lifecycle workflow, and validation.
"""

README = """# Agent Notes

Notes live at `<lifecycle>/<class>/yyyy-mm-dd-topic-title.md`.

Lifecycles are `proposed`, `implemented`, `rejected`, and `archived`. Classes are
`feature`, `bug-fix`, `simplification`, `architecture`, `process`, and `testing`.
Use the `agent-notes` skill as the source of truth for formats and transitions.
"""


def create(path: Path, content: str) -> str:
    if path.exists():
        return f"kept existing {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"created {path}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    args = parser.parse_args()
    root = args.repository.resolve()
    if not root.is_dir():
        parser.error(f"repository is not a directory: {root}")

    notes = root / ".agents" / "notes"
    messages = [create(notes / "README.md", README), create(notes / "AGENTS.md", NOTES_POLICY)]
    agents = root / "AGENTS.md"
    if agents.exists():
        text = agents.read_text(encoding="utf-8")
        if MARKER in text:
            messages.append(f"kept existing Agent Notes rule in {agents}")
        else:
            separator = "" if not text or text.endswith("\n\n") else "\n" if text.endswith("\n") else "\n\n"
            agents.write_text(text + separator + ROOT_RULE, encoding="utf-8")
            messages.append(f"updated {agents}")
    else:
        agents.write_text("# Repository instructions\n\n" + ROOT_RULE, encoding="utf-8")
        messages.append(f"created {agents}")

    for message in messages:
        print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
