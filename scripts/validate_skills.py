#!/usr/bin/env python3
"""Validate structural invariants for every skill in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PLACEHOLDERS = ("TODO", "YOUR_SKILL", "example-skill")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter"]

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, ["SKILL.md frontmatter is not closed with ---"]

    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            # Nested values belong to supported optional frontmatter fields.
            continue
        if ":" not in line:
            errors.append(f"unsupported top-level frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    return fields, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"

    if len(name) >= 64 or not NAME_PATTERN.fullmatch(name):
        errors.append("directory name must use lowercase letters, digits, and single hyphens")
    if not skill_file.is_file():
        return errors + ["missing SKILL.md"]

    fields, frontmatter_errors = parse_frontmatter(skill_file)
    errors.extend(frontmatter_errors)
    if fields.get("name") != name:
        errors.append(f"frontmatter name must equal directory name {name!r}")
    if not fields.get("description"):
        errors.append("frontmatter description is required")

    for path in skill_dir.rglob("*"):
        if path.is_file():
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            found = [marker for marker in PLACEHOLDERS if marker in content]
            if found:
                errors.append(f"{path.relative_to(skill_dir)} contains placeholder: {', '.join(found)}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.is_file():
        content = openai_yaml.read_text(encoding="utf-8")
        if "default_prompt:" in content and f"${name}" not in content:
            errors.append(f"agents/openai.yaml default_prompt must mention ${name}")

    return errors


def main() -> int:
    skill_dirs = sorted(
        path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    failures = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"FAIL {skill_dir.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {skill_dir.relative_to(ROOT)}")

    if failures:
        print(f"\n{failures} skill(s) failed validation", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
