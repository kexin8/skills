.PHONY: help new validate

help:
	@echo "make new NAME=my-skill  Create a new skill"
	@echo "make validate           Validate all skills"

new:
	@test -n "$(NAME)" || (echo "NAME is required: make new NAME=my-skill" >&2; exit 2)
	@python3 scripts/new_skill.py "$(NAME)"

validate:
	@python3 scripts/validate_skills.py

