from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required to validate recurrence rules. "
        "Install it with: pip install pyyaml"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = REPO_ROOT / "rules" / "recurrence-rules.yaml"

REQUIRED_TOP_LEVEL_FIELDS = {
    "version",
    "title",
    "description",
    "rules",
}

REQUIRED_RULE_FIELDS = {
    "id",
    "status",
    "severity",
    "source_failure",
    "recurrence_pattern",
    "recurrence_rule",
    "check",
    "targets",
    "remediation",
}

REQUIRED_CHECK_FIELDS = {
    "script",
    "enabled",
}

ALLOWED_STATUSES = {
    "active",
    "draft",
    "deprecated",
}

ALLOWED_SEVERITIES = {
    "low",
    "medium",
    "high",
    "critical",
}


def fail(message: str) -> None:
    print(f"[recurrence-rules] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_rules_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"Rules file not found: {path}")

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"Invalid YAML in {path}: {exc}")

    if not isinstance(data, dict):
        fail("Rules file must contain a top-level mapping.")

    return data


def require_fields(container: dict[str, Any], required: set[str], context: str) -> None:
    missing = sorted(required - set(container.keys()))
    if missing:
        fail(f"{context} is missing required fields: {', '.join(missing)}")


def validate_non_empty_string(value: Any, field: str, context: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{context}.{field} must be a non-empty string.")


def validate_targets(value: Any, context: str) -> None:
    if not isinstance(value, list) or not value:
        fail(f"{context}.targets must be a non-empty list.")

    for index, target in enumerate(value):
        if not isinstance(target, str) or not target.strip():
            fail(f"{context}.targets[{index}] must be a non-empty string.")


def validate_check(value: Any, context: str) -> None:
    if not isinstance(value, dict):
        fail(f"{context}.check must be a mapping.")

    require_fields(value, REQUIRED_CHECK_FIELDS, f"{context}.check")

    script = value["script"]
    enabled = value["enabled"]

    validate_non_empty_string(script, "script", f"{context}.check")

    if not isinstance(enabled, bool):
        fail(f"{context}.check.enabled must be a boolean.")

    script_path = REPO_ROOT / script
    if enabled and not script_path.exists():
        fail(f"{context}.check.script is enabled but file does not exist: {script}")


def validate_rule(rule: Any, index: int) -> str:
    context = f"rules[{index}]"

    if not isinstance(rule, dict):
        fail(f"{context} must be a mapping.")

    require_fields(rule, REQUIRED_RULE_FIELDS, context)

    rule_id = rule["id"]
    validate_non_empty_string(rule_id, "id", context)

    status = rule["status"]
    if status not in ALLOWED_STATUSES:
        fail(
            f"{context}.status must be one of: "
            f"{', '.join(sorted(ALLOWED_STATUSES))}"
        )

    severity = rule["severity"]
    if severity not in ALLOWED_SEVERITIES:
        fail(
            f"{context}.severity must be one of: "
            f"{', '.join(sorted(ALLOWED_SEVERITIES))}"
        )

    for field in (
        "source_failure",
        "recurrence_pattern",
        "recurrence_rule",
        "remediation",
    ):
        validate_non_empty_string(rule[field], field, context)

    validate_check(rule["check"], context)
    validate_targets(rule["targets"], context)

    return rule_id


def validate_rules_document(data: dict[str, Any]) -> None:
    require_fields(data, REQUIRED_TOP_LEVEL_FIELDS, "top-level document")

    validate_non_empty_string(data["version"], "version", "top-level document")
    validate_non_empty_string(data["title"], "title", "top-level document")
    validate_non_empty_string(data["description"], "description", "top-level document")

    rules = data["rules"]
    if not isinstance(rules, list) or not rules:
        fail("top-level document.rules must be a non-empty list.")

    seen_ids: set[str] = set()

    for index, rule in enumerate(rules):
        rule_id = validate_rule(rule, index)

        if rule_id in seen_ids:
            fail(f"Duplicate rule id found: {rule_id}")

        seen_ids.add(rule_id)


def main() -> None:
    data = load_rules_file(RULES_PATH)
    validate_rules_document(data)
    print(f"[recurrence-rules] OK: {RULES_PATH}")


if __name__ == "__main__":
    main()
