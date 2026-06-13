#!/usr/bin/env python3
"""
Validate Structural Rumination Layer examples.

This script intentionally validates only confirmed schema/example pairs.

v0.1 principle:

* Do not validate files that do not exist.
* Do not add validator targets before schema/example pairs are complete.
* Keep validation scope small until the core structure is stable.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    {
        "name": "rumination-record",
        "schema": ROOT / "schemas" / "rumination-record.schema.json",
        "example": ROOT / "examples" / "rumination-record.example.yaml",
    }
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def format_error_path(error: Any) -> str:
    if not error.path:
        return "<root>"
    return "/".join(str(part) for part in error.path)


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"\nValidating: {name}")
    print("-" * 56)

    if not schema_path.exists():
        print(f"[BLOCKER] Missing schema file: {schema_path.relative_to(ROOT)}")
        return False

    if not example_path.exists():
        print(f"[BLOCKER] Missing example file: {example_path.relative_to(ROOT)}")
        return False

    try:
        schema = load_json(schema_path)
    except json.JSONDecodeError as error:
        print(f"[ERROR] Invalid JSON schema: {schema_path.relative_to(ROOT)}")
        print(f"  - {error}")
        return False

    try:
        example = load_yaml(example_path)
    except yaml.YAMLError as error:
        print(f"[ERROR] Invalid YAML example: {example_path.relative_to(ROOT)}")
        print(f"  - {error}")
        return False

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(validator.iter_errors(example), key=lambda item: list(item.path))

    if errors:
        print(f"[FAIL] {example_path.relative_to(ROOT)} does not conform to {schema_path.relative_to(ROOT)}")
        for error in errors:
            location = format_error_path(error)
            print(f"  - {location}: {error.message}")
        return False

    print(f"[PASS] {example_path.relative_to(ROOT)}")
    return True


def main() -> int:
    print("Structural Rumination Layer example validation")
    print("=" * 56)

    all_passed = True

    for target in TARGETS:
        passed = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_passed = all_passed and passed

    print("\nFinal Error Visibility Check")
    print("=" * 56)

    if all_passed:
        print("[PASS] All confirmed schema/example pairs validated successfully.")
        print("[INFO] Validator scope remains limited to confirmed local files.")
        return 0

    print("[FAIL] Validation failed.")
    print("[RUMINATION] Do not proceed to release or tagging until the visible errors above are resolved.")
    return 1

(
    "schemas/ai-agent-rumination-hook.schema.json",
    "examples/ai-agent-rumination-hook.example.yaml",
),

(
    "schemas/pre-release-rumination-gate.schema.json",
    "examples/pre-release-rumination-gate.example.yaml",
),

if __name__ == "__main__":
    sys.exit(main())


