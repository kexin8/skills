SKILLS_HOME ?= $(HOME)/.agents/skills

.PHONY: help new validate install install-all

help:
	@echo "make new NAME=my-skill                  Create a new skill"
	@echo "make validate                           Validate all skills"
	@echo "make install NAME=my-skill              Link one skill into $(SKILLS_HOME)"
	@echo "make install-all                        Link all skills into $(SKILLS_HOME)"
	@echo "SKILLS_HOME=/path overrides the target directory"

new:
	@test -n "$(NAME)" || (echo "NAME is required: make new NAME=my-skill" >&2; exit 2)
	@python3 scripts/new_skill.py "$(NAME)"

validate:
	@python3 scripts/validate_skills.py

install: validate
	@test -n "$(NAME)" || (echo "NAME is required: make install NAME=my-skill" >&2; exit 2)
	@test -f "skills/$(NAME)/SKILL.md" || (echo "skill not found: skills/$(NAME)" >&2; exit 2)
	@source_dir="$(CURDIR)/skills/$(NAME)"; \
	target_dir="$(SKILLS_HOME)/$(NAME)"; \
	mkdir -p "$(SKILLS_HOME)"; \
	if test -L "$$target_dir"; then \
		current_target="$$(readlink "$$target_dir")"; \
		if test "$$current_target" = "$$source_dir"; then \
			echo "already installed: $$target_dir -> $$source_dir"; \
			exit 0; \
		fi; \
		echo "refusing to replace existing symlink: $$target_dir -> $$current_target" >&2; \
		exit 1; \
	fi; \
	if test -e "$$target_dir"; then \
		echo "refusing to replace existing path: $$target_dir" >&2; \
		exit 1; \
	fi; \
	ln -s "$$source_dir" "$$target_dir"; \
	echo "installed: $$target_dir -> $$source_dir"

install-all: validate
	@set -e; \
	found=0; \
	for skill_file in skills/*/SKILL.md; do \
		test -f "$$skill_file" || continue; \
		found=1; \
		skill_name="$$(basename "$$(dirname "$$skill_file")")"; \
		$(MAKE) --no-print-directory install NAME="$$skill_name" SKILLS_HOME="$(SKILLS_HOME)"; \
	done; \
	test "$$found" -eq 1 || echo "no skills found"
