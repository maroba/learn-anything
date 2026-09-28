#!/usr/bin/env python3
"""Create a new book from the templates.

Public part (text, metadata, working files) goes to books/<slug>/ in this repo.
Private part (learner profile etc.) goes to books/<slug>/ in the private repo.

Example:
    python scripts/new_book.py neugriechisch --title "Neugriechisch" \
        --topic "Neugriechisch für Anfänger" --lang de --target-lang el --archetype languages
"""

import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PRIVATE = ROOT.parent / "learn-anything-private"

ARCHETYPES = ["languages", "formal-sciences", "natural-sciences", "programming", "humanities", "practical"]

# UI strings that appear in the book skeleton, per book language. Fallback: English.
LABELS = {
    "de": {"library_label": "Bibliothek", "preface_title": "Vorwort"},
    "en": {"library_label": "Library", "preface_title": "Preface"},
    "el": {"library_label": "Βιβλιοθήκη", "preface_title": "Πρόλογος"},
    "es": {"library_label": "Biblioteca", "preface_title": "Prefacio"},
    "fr": {"library_label": "Bibliothèque", "preface_title": "Préface"},
    "it": {"library_label": "Biblioteca", "preface_title": "Prefazione"},
}


def instantiate(template: Path, target: Path, values: dict) -> None:
    """Copy a template directory, filling {{placeholders}} in text files. Symlinks are kept."""
    shutil.copytree(template, target, symlinks=True)
    for path in target.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        filled = re.sub(r"\{\{(\w+)\}\}", lambda m: str(values.get(m.group(1), m.group(0))), text)
        path.write_text(filled, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", help="short URL-safe name, e.g. neugriechisch")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--topic", required=True, help="what the book teaches, in one line")
    parser.add_argument("--lang", required=True, help="language the book is written in (BCP-47, e.g. de)")
    parser.add_argument("--target-lang", default="", help="language being learned, for language books")
    parser.add_argument("--archetype", required=True, choices=ARCHETYPES)
    parser.add_argument("--private-dir", type=Path, default=DEFAULT_PRIVATE, help="checkout of the private repo")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.slug):
        parser.error("slug must consist of lowercase letters, digits and hyphens")

    public_target = ROOT / "books" / args.slug
    private_template = args.private_dir / "templates" / "book"
    private_target = args.private_dir / "books" / args.slug

    if public_target.exists():
        parser.error(f"{public_target} already exists")
    if not private_template.is_dir():
        parser.error(f"private template not found at {private_template} (is the private repo checked out?)")
    if private_target.exists():
        parser.error(f"{private_target} already exists")

    labels = LABELS.get(args.lang, LABELS.get(args.lang[:2], LABELS["en"]))
    values = {
        "slug": args.slug,
        "title": args.title,
        "subtitle": args.subtitle,
        "topic": args.topic,
        "lang": args.lang,
        "target_lang": args.target_lang,
        "archetype": args.archetype,
        "date": datetime.date.today().isoformat(),
        **labels,
    }

    instantiate(ROOT / "templates" / "book", public_target, values)
    instantiate(private_template, private_target, values)

    print(f"Created {public_target.relative_to(ROOT)}")
    print(f"Created {private_target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
