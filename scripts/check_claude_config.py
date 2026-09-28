#!/usr/bin/env python3
"""Validate the front matter of all agents and skills under .claude/.

A YAML error (e.g. an unquoted colon in a description) silently disables an agent or skill,
so CI runs this check.
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    files = sorted((ROOT / ".claude" / "agents").glob("*.md")) + sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md"))
    errors = []
    for path in files:
        rel = path.relative_to(ROOT)
        parts = path.read_text(encoding="utf-8").split("---", 2)
        if len(parts) < 3 or parts[0].strip():
            errors.append(f"{rel}: missing front matter")
            continue
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError as e:
            errors.append(f"{rel}: invalid YAML: {e}")
            continue
        expected = path.stem if path.parent.name == "agents" else path.parent.name
        if meta.get("name") != expected:
            errors.append(f"{rel}: name is {meta.get('name')!r}, expected {expected!r}")
        if not meta.get("description"):
            errors.append(f"{rel}: description missing")

    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    print(f"Checked {len(files)} agent/skill files, {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
