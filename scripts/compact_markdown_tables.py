#!/usr/bin/env python3
"""Rewrite padded/aligned markdown tables in compact style.

Many editors and formatters pad table cells with spaces so the pipes line up in
the source. That makes long-form posts painful to edit: adding one word to a
cell means re-padding every other row. This script strips the padding, leaving
exactly one space on each side of every pipe and a bare `---` delimiter row --
the layout markdownlint calls the "compact" table style (MD060).

Cell text is never touched, so the rendered HTML is unchanged. Content inside
fenced or indented code blocks and YAML front matter is left alone.

Usage:
    python3 compact_markdown_tables.py PATH [PATH ...] [--check]

    PATH may be a markdown file or a directory to search recursively.

Examples:
    python3 scripts/compact_markdown_tables.py _posts/2018-06-15-demystifying-dmarc.md
    python3 scripts/compact_markdown_tables.py _posts _tabs
    python3 scripts/compact_markdown_tables.py . --check
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKDOWN_SUFFIXES = frozenset({".md", ".markdown"})
SKIP_DIRS = frozenset({"_site", "vendor", "node_modules", ".git", ".jekyll-cache"})

# A delimiter cell: dashes with optional leading/trailing alignment colons.
DELIMITER_CELL = re.compile(r"^:?-+:?$")
FENCE = re.compile(r"^\s{0,3}(```+|~~~+)")
# Split on pipes that aren't backslash-escaped.
UNESCAPED_PIPE = re.compile(r"(?<!\\)\|")


def split_row(line: str) -> list[str]:
    """Split a table row into its stripped cell values, ignoring the outer pipes."""
    cells = UNESCAPED_PIPE.split(line.strip())[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    return [cell.strip() for cell in cells]


def is_delimiter_row(cells: list[str]) -> bool:
    """Report whether `cells` is a table's delimiter row (the `| --- |` line)."""
    return bool(cells) and all(DELIMITER_CELL.match(cell) for cell in cells)


def compact_delimiter(cells: list[str]) -> list[str]:
    """Shrink delimiter cells to a bare `---`, preserving any alignment colons."""
    compacted = []
    for cell in cells:
        left = ":" if cell.startswith(":") else ""
        right = ":" if cell.endswith(":") else ""
        compacted.append(f"{left}---{right}")
    return compacted


def format_row(cells: list[str], indent: str) -> str:
    """Render cells with one space on each side of every pipe.

    An empty cell becomes `| |` -- the single space serves both of its pipes,
    which is what MD060's compact style expects.
    """
    return indent + "|" + "".join(f" {cell} |" if cell else " |" for cell in cells)


def compact_tables(text: str) -> tuple[str, int]:
    """Return `text` with every markdown table compacted, plus the table count."""
    lines = text.split("\n")
    output: list[str] = []
    index = 0
    tables = 0
    in_fence = False
    fence_marker = ""

    # Skip YAML front matter verbatim.
    if lines and lines[0].strip() == "---":
        for offset, line in enumerate(lines[1:], start=1):
            if line.strip() in {"---", "..."}:
                output.extend(lines[: offset + 1])
                index = offset + 1
                break

    while index < len(lines):
        line = lines[index]
        stripped = line.lstrip()
        fence_match = FENCE.match(line)

        if in_fence:
            in_fence = not (fence_match and fence_match.group(1).startswith(fence_marker))
        elif fence_match:
            in_fence, fence_marker = True, fence_match.group(1)

        # Four or more leading spaces is an indented code block, not a table.
        is_row = not in_fence and stripped.startswith("|") and len(line) - len(stripped) < 4
        if not is_row:
            output.append(line)
            index += 1
            continue

        start = index
        block: list[tuple[str, list[str]]] = []
        while index < len(lines):
            candidate = lines[index]
            bare = candidate.lstrip()
            if not bare.startswith("|") or len(candidate) - len(bare) >= 4:
                break
            block.append((candidate[: len(candidate) - len(bare)], split_row(candidate)))
            index += 1

        if len(block) < 2 or not is_delimiter_row(block[1][1]):
            output.extend(lines[start:index])  # Not a table; leave it as written.
            continue

        for row, (indent, cells) in enumerate(block):
            output.append(format_row(compact_delimiter(cells) if row == 1 else cells, indent))
        tables += 1

    return "\n".join(output), tables


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    """Expand the given files and directories into a sorted list of markdown files."""
    found: set[Path] = set()
    for path in paths:
        if path.is_dir():
            found.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.suffix.lower() in MARKDOWN_SUFFIXES
                and not SKIP_DIRS.intersection(candidate.parts)
            )
        else:
            found.add(path)
    return sorted(found)


def build_arg_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", type=Path, nargs="+", help="Markdown files or directories.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that need reformatting without writing; exit 1 if any do.",
    )
    return parser


def main() -> int:
    """Entry point for CLI usage."""
    args = build_arg_parser().parse_args()

    files = iter_markdown_files(args.paths)
    if not files:
        print("No markdown files found.", file=sys.stderr)
        return 1

    changed: list[Path] = []
    for path in files:
        original = path.read_text(encoding="utf-8")
        compacted, tables = compact_tables(original)
        if compacted == original:
            continue
        changed.append(path)
        if not args.check:
            path.write_text(compacted, encoding="utf-8")
        verb = "would reformat" if args.check else "reformatted"
        print(f"{verb} {path} ({tables} table{'s' if tables != 1 else ''})")

    if not changed:
        print(f"All {len(files)} file(s) already use compact tables.")
    return 1 if changed and args.check else 0


if __name__ == "__main__":
    sys.exit(main())
