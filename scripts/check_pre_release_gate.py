from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "docs/pre-release-rumination-gate.md",
    "schemas/pre-release-rumination-gate.schema.json",
    "examples/pre-release-rumination-gate.example.yaml",
]

GATE_COMMANDS = [
    ["scripts/check_recurrence_rules.py"],
    ["scripts/check_workflow_structure.py"],
    ["scripts/check_yaml_lists.py"],
    ["scripts/check_json_schema_syntax.py"],
    ["scripts/check_python_syntax.py"],
    ["scripts/validate_examples.py"],
]


def fail(message: str) -> None:
    print(f"[pre-release-gate] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.exists():
            fail(f"Required file not found: {relative_path}")


def run_command(command: list[str]) -> None:
    script = command[0]
    script_path = REPO_ROOT / script

    if not script_path.exists():
        fail(f"Gate command script not found: {script}")

    full_command = [sys.executable, *command]
    print(f"[pre-release-gate] Running: {' '.join(full_command)}")

    result = subprocess.run(
        full_command,
        cwd=REPO_ROOT,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        fail(f"Gate command failed: {' '.join(full_command)}")


def main() -> None:
    check_required_files()

    for command in GATE_COMMANDS:
        run_command(command)

    print("[pre-release-gate] OK: pre-release rumination gate passed")


if __name__ == "__main__":
    main()
