from__future__import annotations

from io import BytesIO
from pathlib import Path
import py_compile
import sys
import tokenize


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

MALFORMED_DUNDER_TEXT_PATTERNS = (
    "__ future__",
    "__future __",
    "__ file__",
    "__file __",
)

MALFORMED_DUNDER_IDENTIFIER_NAMES = {
    "_future_",
    "_file_",
}


def fail(message: str) -> None:
    print(f"[python-syntax] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_malformed_text_patterns(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    for pattern in MALFORMED_DUNDER_TEXT_PATTERNS:
        if pattern in text:
            fail(
                f"{path}: suspicious malformed dunder-like text found: {pattern!r}. "
                "Check __future__ or __file__ spelling."
            )


def check_malformed_identifier_names(path: Path) -> None:
    source = path.read_bytes()

    try:
        tokens = tokenize.tokenize(BytesIO(source).readline)
    except tokenize.TokenError as exc:
        fail(f"{path}: tokenization failed: {exc}")

    for token in tokens:
        if token.type != tokenize.NAME:
            continue

        if token.string in MALFORMED_DUNDER_IDENTIFIER_NAMES:
            line, column = token.start
            fail(
                f"{path}:{line}:{column + 1}: suspicious malformed identifier "
                f"found: {token.string!r}. Check __future__ or __file__ spelling."
            )


def check_compile(path: Path) -> None:
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as exc:
        fail(f"{path}: Python syntax check failed:\n{exc.msg}")


def check_file(path: Path) -> None:
    check_malformed_text_patterns(path)
    check_malformed_identifier_names(path)
    check_compile(path)


def main() -> None:
    if not SCRIPTS_DIR.exists():
        print("[python-syntax] OK: no scripts directory found")
        return

    python_paths = sorted(SCRIPTS_DIR.glob("*.py"))

    for path in python_paths:
        check_file(path)

    print(f"[python-syntax] OK: checked {len(python_paths)} Python script file(s)")


if __name__ == "__main__":
    main()
