from __future__ import annotations

from pathlib import Path
import py_compile
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

SUSPICIOUS_DUNDER_PATTERNS = (
    "__ future__",
    "__future __",
    "_future_",
    "__ file__",
    "__file __",
    "_file_",
)


def fail(message: str) -> None:
    print(f"[python-syntax] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_suspicious_dunders(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    for pattern in SUSPICIOUS_DUNDER_PATTERNS:
        if pattern in text:
            fail(
                f"{path}: suspicious dunder-like pattern found: {pattern!r}. "
                "Check __future__ or __file__ spelling."
            )


def check_compile(path: Path) -> None:
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as exc:
        fail(f"{path}: Python syntax check failed:\n{exc.msg}")


def main() -> None:
    if not SCRIPTS_DIR.exists():
        print("[python-syntax] OK: no scripts directory found")
        return

    python_paths = sorted(SCRIPTS_DIR.glob("*.py"))

    for path in python_paths:
        check_suspicious_dunders(path)
        check_compile(path)

    print(f"[python-syntax] OK: checked {len(python_paths)} Python script file(s)")


if __name__ == "__main__":
    main()
