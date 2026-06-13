from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Install it with: pip install pyyaml"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"


def fail(message: str) -> None:
    print(f"[workflow-structure] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"Invalid YAML in {path}: {exc}")

    if not isinstance(data, dict):
        fail(f"{path} must contain a top-level mapping.")

    return data


def validate_steps(path: Path, job_name: str, job: Any) -> None:
    if not isinstance(job, dict):
        fail(f"{path}: job '{job_name}' must be a mapping.")

    if "steps" not in job:
        return

    steps = job["steps"]

    if not isinstance(steps, list):
        fail(f"{path}: job '{job_name}' has steps, but steps is not a list.")

    for index, step in enumerate(steps):
        if not isinstance(step, dict):
            fail(f"{path}: job '{job_name}' step {index} must be a mapping.")


def validate_setup_python_cache(path: Path, job_name: str, job: dict[str, Any]) -> None:
    steps = job.get("steps", [])

    if not isinstance(steps, list):
        return

    for index, step in enumerate(steps):
        if not isinstance(step, dict):
            continue

        uses = step.get("uses", "")
        if not isinstance(uses, str):
            continue

        if "actions/setup-python" not in uses:
            continue

        with_config = step.get("with", {})
        if not isinstance(with_config, dict):
            continue

        cache = with_config.get("cache")
        cache_dependency_path = with_config.get("cache-dependency-path")

        if cache and cache_dependency_path:
            dependency_path = REPO_ROOT / str(cache_dependency_path)

            if not dependency_path.exists():
                fail(
                    f"{path}: job '{job_name}' step {index} uses setup-python "
                    f"cache-dependency-path, but file does not exist: "
                    f"{cache_dependency_path}"
                )


def validate_workflow(path: Path) -> None:
    data = load_yaml(path)

    jobs = data.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        fail(f"{path}: workflow must contain non-empty jobs mapping.")

    for job_name, job in jobs.items():
        validate_steps(path, str(job_name), job)

        if isinstance(job, dict):
            validate_setup_python_cache(path, str(job_name), job)


def main() -> None:
    if not WORKFLOW_DIR.exists():
        print("[workflow-structure] OK: no workflow directory found")
        return

    workflow_paths = sorted(
        list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml"))
    )

    if not workflow_paths:
        print("[workflow-structure] OK: no workflow files found")
        return

    for path in workflow_paths:
        validate_workflow(path)

    print(f"[workflow-structure] OK: checked {len(workflow_paths)} workflow file(s)")


if __name__ == "__main__":
    main()
