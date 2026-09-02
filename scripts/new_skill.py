#!/usr/bin/env python3
"""Create the minimal scaffold for a personal skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT = Path(__file__).resolve().parents[1]


def title_from_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: new_skill.py <skill-name>", file=sys.stderr)
        return 2

    name = sys.argv[1]
    if len(name) >= 64 or not NAME_PATTERN.fullmatch(name):
        print(
            "skill name must be under 64 characters and contain only "
            "lowercase letters, digits, and single hyphens",
            file=sys.stderr,
        )
        return 2

    skill_dir = ROOT / "skills" / name
    if skill_dir.exists():
        print(f"skill already exists: {skill_dir}", file=sys.stderr)
        return 1

    agents_dir = skill_dir / "agents"
    agents_dir.mkdir(parents=True)
    display_name = title_from_name(name)

    (skill_dir / "SKILL.md").write_text(
        f'''---
name: {name}
description: TODO: Describe what this skill does and when it should be used.
---

# {display_name}

TODO: Add only the workflow, constraints, and routing information needed to perform this skill reliably.
''',
        encoding="utf-8",
    )
    (agents_dir / "openai.yaml").write_text(
        f'''interface:
  display_name: "{display_name}"
  short_description: "TODO: Add a concise UI description"
  default_prompt: "Use ${name} to TODO: describe a representative request."
''',
        encoding="utf-8",
    )

    print(f"created {skill_dir}")
    print("replace every TODO, remove unused files, then run: make validate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

