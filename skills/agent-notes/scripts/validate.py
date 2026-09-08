#!/usr/bin/env python3
"""Validate the portable Agent Notes tree and lifecycle-specific format."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LIFECYCLES = {"proposed", "implemented", "rejected", "archived"}
CLASSES = {"feature", "bug-fix", "simplification", "architecture", "process", "testing"}
NAME = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
REQUIRED = {
    "proposed": {"Problem", "Proposal", "Alternatives considered", "Acceptance criteria", "Risks"},
    "implemented": {"Problem", "Decision", "Alternatives considered", "Consequences"},
    "rejected": {"Problem", "Proposal", "Alternatives considered"},
}


def validate_note(path: Path, lifecycle: str) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not re.fullmatch(r"# Agent Note: \S.*", lines[0]):
        errors.append("line 1 must be '# Agent Note: <title>'")
    if len(lines) < 2 or lines[1] != "":
        errors.append("line 2 must be blank")
    status = lines[2] if len(lines) > 2 else ""
    expected = {
        "proposed": r"Status: proposed",
        "implemented": r"Status: implemented",
        "rejected": r"Status: rejected — \S.*",
        "archived": r"Status: implemented",
    }[lifecycle]
    if not re.fullmatch(expected, status):
        errors.append(f"status does not match {lifecycle}/")
    headings = {line[3:] for line in lines if line.startswith("## ")}
    if lifecycle != "archived":
        for heading in sorted(REQUIRED[lifecycle] - headings):
            errors.append(f"missing section '## {heading}'")
    if lifecycle == "implemented" and headings & {"Proposal", "Acceptance criteria", "Risks"}:
        errors.append("implemented Note retains proposal-era sections")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    args = parser.parse_args()
    root = args.repository.resolve() / ".agents" / "notes"
    if not root.is_dir():
        parser.error(f"Agent Notes directory not found: {root}")

    errors: list[str] = []
    checked = 0
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if path.name in {"README.md", "AGENTS.md", "CLAUDE.md"}:
            continue
        parts = rel.parts
        if len(parts) != 3 or parts[0] not in LIFECYCLES or parts[1] not in CLASSES:
            errors.append(f"{rel}: expected <lifecycle>/<class>/<file>.md")
            continue
        if not NAME.fullmatch(path.name):
            errors.append(f"{rel}: invalid filename")
        checked += 1
        errors.extend(f"{rel}: {message}" for message in validate_note(path, parts[0]))

    if errors:
        print("agent-notes validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"agent-notes validation passed: {checked} note(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
