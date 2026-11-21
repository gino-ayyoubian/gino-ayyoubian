#!/usr/bin/env python3
"""Check that Markdown links to repository-local paths resolve."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]*)\)")
INLINE_CODE = re.compile(r"`[^`]*`")


def markdown_lines(path: Path):
    in_fence = False
    fence_marker = ""
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            continue
        if not in_fence:
            yield number, INLINE_CODE.sub("", line)


def check_links(root: Path) -> list[str]:
    errors = []
    for markdown in sorted(root.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        for line_number, line in markdown_lines(markdown):
            for match in LINK.finditer(line):
                tokens = match.group(1).strip().split(maxsplit=1)
                target = tokens[0].strip("<>") if tokens else ""
                if not target or target == "#":
                    errors.append(f"{markdown.relative_to(root)}:{line_number}: empty link target")
                    continue

                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue

                resolved = (markdown.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(root) or not resolved.exists():
                    errors.append(
                        f"{markdown.relative_to(root)}:{line_number}: "
                        f"unresolved local link {target!r}"
                    )
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_links(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("All repository-local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
