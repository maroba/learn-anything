#!/usr/bin/env python3
"""Build the library site into _site/.

    python scripts/build.py                  # all published books + library page (what CI deploys)
    python scripts/build.py --book <slug>    # just one book, published or not (quick local check)
    python scripts/build.py --all            # also include unpublished books

Each book under books/<slug>/ is its own Quarto book project, rendered to books/<slug>/_book
and copied to _site/<slug>/. The library page (library/) lists the published books.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
BOOKS = ROOT / "books"
LIBRARY = ROOT / "library"

STATUS_LABELS = {
    "interview": "Interview",
    "research": "Recherche",
    "outline": "Outline",
    "sample": "Probekapitel",
    "writing": "wird geschrieben",
    "complete": "fertig",
}


def quarto(*args: str) -> None:
    subprocess.run(["quarto", *args], cwd=ROOT, check=True)


def load_books() -> list[dict]:
    books = []
    for meta_file in sorted(BOOKS.glob("*/book.yml")):
        meta = yaml.safe_load(meta_file.read_text(encoding="utf-8")) or {}
        meta["slug"] = meta_file.parent.name
        books.append(meta)
    return books


def render_book(slug: str) -> None:
    book_dir = BOOKS / slug
    quarto("render", str(book_dir.relative_to(ROOT)))
    target = SITE / slug
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(book_dir / "_book", target)


def render_library(books: list[dict]) -> None:
    items = []
    for b in books:
        details = [f"Sprache: {b.get('language', '?')}"]
        if b.get("target-language"):
            details.append(f"Zielsprache: {b['target-language']}")
        details.append(f"Status: {STATUS_LABELS.get(b.get('status'), b.get('status', '?'))}")
        items.append({
            "title": b.get("title", b["slug"]),
            "subtitle": b.get("subtitle") or "",
            "description": f"{b.get('topic', '')}  \n{' · '.join(details)}",
            "path": f"{b['slug']}/index.html",
            "categories": [b.get("archetype", "")],
        })
    (LIBRARY / "books.yml").write_text(yaml.safe_dump(items, allow_unicode=True, sort_keys=False), encoding="utf-8")

    quarto("render", str(LIBRARY.relative_to(ROOT)))
    shutil.copytree(LIBRARY / "_site", SITE, dirs_exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--book", help="render only this book (and skip the library page)")
    parser.add_argument("--all", action="store_true", help="include unpublished books")
    args = parser.parse_args()

    if args.book:
        if not (BOOKS / args.book / "book.yml").is_file():
            parser.error(f"no book '{args.book}' under books/")
        SITE.mkdir(exist_ok=True)
        render_book(args.book)
        print(f"Rendered {args.book} -> _site/{args.book}/index.html")
        return 0

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    books = [b for b in load_books() if args.all or b.get("published")]
    for b in books:
        render_book(b["slug"])
    render_library(books)
    (SITE / ".nojekyll").touch()
    print(f"Built library with {len(books)} book(s) -> _site/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
