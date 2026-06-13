from __future__ import annotations

from pathlib import Path
import json
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "schemas"


def fail(message: str) -> None:
    print(f"[json-schema-syntax] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_file(path: Path) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}:{exc.lineno}:{exc.colno}: invalid JSON: {exc.msg}")


def main() -> None:
    if not SCHEMAS_DIR.exists():
        print("[json-schema-syntax] OK: no schemas directory found")
        return

    schema_paths = sorted(SCHEMAS_DIR.glob("*.json"))

    for path in schema_paths:
        check_file(path)

    print(f"[json-schema-syntax] OK: checked {len(schema_paths)} schema file(s)")


if __name__ == "__main__":
    main()

