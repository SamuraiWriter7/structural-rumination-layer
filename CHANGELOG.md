# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple principle:

> Mistakes may occur.
> But the same structural mistake should not pass through the workflow unchanged twice.

---

## v0.1.0-candidate

### Added

* Initial definition of **Structural Rumination Layer**.
* Added the core lifecycle:

```text
Forward Generation
→ Reverse Trace Check
→ Verification
→ Reflection
→ Rumination
→ Breathing Alignment
→ Error Visibility
→ Next-Gate Registration
```

* Added **Rumination Sieve** model:

```text
Pass 1: Existence Check
Pass 2: Consistency Check
Pass 3: Recurrence Check
```

* Added documentation for staged error digestion:

  * `docs/rumination-sieve-protocol.md`
  * `docs/final-error-visibility-check.md`

* Added the first schema/example pair:

  * `schemas/rumination-record.schema.json`
  * `examples/rumination-record.example.yaml`

* Added local validation script:

  * `scripts/validate_examples.py`

---

### Added

* Added GitHub Actions validation workflow:

  * `.github/workflows/validate-examples.yml`

* The workflow validates the confirmed v0.1 schema/example pair by running:

```bash
python scripts/validate_examples.py
```

* CI validation has passed for the initial v0.1 structure.

---

### Rumination Notes

The first CI validation cycle surfaced and digested several structural errors:

* GitHub Actions YAML indentation error around `steps:`.
* `setup-python` cache configuration used without `requirements.txt` or `pyproject.toml`.
* Python double-underscore names were corrupted during code transfer.
* JSON Schema regex backslashes were not escaped correctly.
* YAML example lists used Markdown-style `*` bullets instead of YAML `-` list markers.

These errors were converted into recurrence-prevention rules.

The v0.1 workflow now confirms:

* schema/example validation can run locally,
* the same validation can run in GitHub Actions,
* the repository can use its own rumination protocol to identify and reduce repeated structural errors.

---

### Updated Design Notes

This candidate now includes a minimal CI validation loop.

The workflow remains intentionally narrow:

* one confirmed schema,
* one confirmed example,
* one local validation script,
* one GitHub Actions validation workflow.

The purpose is not broad automation.

The purpose is to ensure that the first rumination loop is executable and stable before expanding the repository.


### Design Notes

This version intentionally keeps the scope small.

It does not attempt to make AI-assisted workflows perfectly error-free.

Instead, it focuses on:

* making errors visible,
* identifying repeated structural patterns,
* converting mistakes into recurrence-prevention rules,
* reducing human-side rework,
* preventing workflow drift before release.

---

### Intentionally Deferred

The following features are intentionally not included in this candidate version:

* GitHub Actions workflow,
* multiple schema support,
* automated release generation,
* README badges,
* external package publishing.

These are deferred to avoid adding structure faster than it can be verified.

---

### Core Rule

> Do not proceed if the same structural error pattern appears again without a new recurrence-prevention rule.

In Japanese:

> 同じ構造的過ちが再発した場合、反芻と再発防止ルールなしに次へ進まない。

---

### Status

This is the first candidate release of Structural Rumination Layer.

The purpose of this version is to establish the minimum digestive structure for AI-assisted GitHub specification work before expanding the repository.

## [0.2.0-candidate] - 2026-06-14

### Added

- Added `rules/recurrence-rules.yaml` as the initial executable recurrence rule registry.
- Added `scripts/check_recurrence_rules.py` to validate the recurrence rule registry.
- Added `scripts/check_workflow_structure.py` to detect recurring GitHub Actions workflow structure issues.
- Added `scripts/check_yaml_lists.py` to detect malformed YAML list marker contamination.
- Added `scripts/check_json_schema_syntax.py` to ensure JSON Schema files are parseable as strict JSON.
- Added `scripts/check_python_syntax.py` to detect Python syntax errors and suspicious dunder corruption patterns.
- Introduced the v0.2 theme: **Executable Recurrence Rules**.

### Changed

- Extended the project from passive Structural Rumination Records toward executable recurrence checks.
- Reframed recorded implementation failures as reusable recurrence prevention rules.
- Updated the validation flow to include executable recurrence rule checks.

### Validated

- Confirmed that GitHub Actions passes with the v0.2 executable recurrence checks enabled.
- Confirmed that previously observed error patterns have been converted into structural recurrence checks.
