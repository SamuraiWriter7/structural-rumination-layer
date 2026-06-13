from __future__ import annotations

from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = REPO_ROOT / "examples"

ASTERISK_LIST_PATTERN = re.compile(r"^\s*\*\s+")


def fail(message: str) -> None:
    print(f"[yaml-lists] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_file(path: Path) -> None:
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if ASTERISK_LIST_PATTERN.match(line):
            fail(
                f"{path}:{line_number}: found '*' used as a YAML list marker. "
                "Use '-' for YAML lists, or quote '*' when it is literal data."
            )


def main() -> None:
    if not EXAMPLES_DIR.exists():
        print("[yaml-lists] OK: no examples directory found")
        return

    yaml_paths = sorted(
        list(EXAMPLES_DIR.glob("*.yaml")) + list(EXAMPLES_DIR.glob("*.yml"))
    )

    for path in yaml_paths:
        check_file(path)

    print(f"[yaml-lists] OK: checked {len(yaml_paths)} YAML example file(s)")


if __name__ == "__main__":
    main()
