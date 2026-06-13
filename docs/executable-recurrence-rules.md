# Executable Recurrence Rules

## Overview

`Executable Recurrence Rules` is the v0.2 layer of `structural-rumination-layer`.

While v0.1 introduced the **Structural Rumination Record** as a way to record AI development failures as structured data, v0.2 extends those records into executable recurrence checks.

In other words:

```text
v0.1 = record the failure
v0.2 = detect its recurrence
```

This document explains how recurrence patterns and recurrence rules are converted into validation scripts that can detect repeated implementation failures before release.

---

## Core Idea

`structural-rumination-layer` treats AI development failures not as disposable logs, but as structural signals.

A failure is not only something to fix once.
It can also become a reusable rule for preventing similar failures in the future.

The basic transformation is:

```text
failure event
  -> rumination record
  -> recurrence pattern
  -> recurrence rule
  -> executable check
  -> pre-release gate
```

This is the core transition introduced in v0.2.

---

## From Rumination Record to Executable Rule

A Structural Rumination Record may describe:

* what failed
* where it failed
* why it failed
* how it was fixed
* what pattern may recur
* what rule should prevent recurrence

In v0.2, the `recurrence_rules` concept is externalized into a dedicated rule registry:

```text
rules/
  recurrence-rules.yaml
```

This registry defines recurring failure patterns and maps them to executable validation scripts.

Each rule includes:

* `id`
* `status`
* `severity`
* `source_failure`
* `recurrence_pattern`
* `recurrence_rule`
* `check`
* `targets`
* `remediation`

Together, these fields convert a remembered failure into a checkable prevention rule.

---

## Rule Registry

The initial rule registry is located at:

```text
rules/recurrence-rules.yaml
```

Example structure:

```yaml
rules:
  - id: "workflow-steps-indentation"
    status: "active"
    severity: "high"
    source_failure: "GitHub Actions steps indentation error"
    recurrence_pattern: >
      A workflow job contains malformed or misplaced steps definitions.
    recurrence_rule: >
      Every workflow job that defines steps must declare steps as a list
      under the job body with valid YAML indentation.
    check:
      script: "scripts/check_workflow_structure.py"
      enabled: true
    targets:
      - ".github/workflows/*.yml"
      - ".github/workflows/*.yaml"
    remediation: >
      Move steps under the correct job key and ensure each step starts
      with a properly indented list item.
```

The registry itself is validated by:

```text
scripts/check_recurrence_rules.py
```

This ensures that recurrence rules are not just informal notes, but structured and testable rule definitions.

---

## Executable Checks

v0.2 introduces the first set of executable recurrence checks.

```text
scripts/
  check_recurrence_rules.py
  check_workflow_structure.py
  check_yaml_lists.py
  check_json_schema_syntax.py
  check_python_syntax.py
```

### `check_recurrence_rules.py`

Validates the recurrence rule registry itself.

It checks that:

* the rule file exists
* required top-level fields are present
* each rule has required fields
* rule IDs are unique
* status and severity values are valid
* enabled checks point to existing scripts

This is the structural integrity check for the recurrence rule layer.

---

### `check_workflow_structure.py`

Detects recurring GitHub Actions workflow structure problems.

It checks that:

* workflow files are valid YAML
* `jobs` is present and properly structured
* each job’s `steps` field is a list
* each workflow step is a mapping
* `actions/setup-python` cache configuration points to an existing dependency file when enabled

This check was derived from actual workflow errors encountered during repository development.

---

### `check_yaml_lists.py`

Detects malformed YAML list contamination.

It checks for unquoted `*` markers used as list items inside YAML example files.

This prevents Markdown-style list markers from being accidentally introduced into YAML files, where `*` may be interpreted as an alias indicator.

Correct YAML list marker:

```yaml
items:
  - first
  - second
```

Problematic pattern:

```yaml
items:
  * first
  * second
```

---

### `check_json_schema_syntax.py`

Ensures JSON Schema files are parseable as strict JSON.

This detects issues such as:

* invalid escape sequences
* broken backslash usage
* malformed JSON syntax
* incomplete schema documents

This check must pass before deeper schema validation is meaningful.

---

### `check_python_syntax.py`

Checks Python scripts for syntax errors and suspicious dunder corruption patterns.

It validates that Python files compile successfully and detects suspicious malformed variants of identifiers such as:

```text
__future__
__file__
```

This prevents failures caused by corrupted special identifiers or malformed future imports.

---

## Validation Flow

The v0.2 validation flow can be run manually:

```bash
python scripts/check_recurrence_rules.py
python scripts/check_workflow_structure.py
python scripts/check_yaml_lists.py
python scripts/check_json_schema_syntax.py
python scripts/check_python_syntax.py
python scripts/validate_examples.py
```

Together, these checks validate both:

1. the Structural Rumination Record examples
2. the executable recurrence rule layer

---

## Why This Matters

v0.1 made failure recordable.

v0.2 makes failure partially executable.

This means the repository is no longer only a place where failures are described.
It becomes a system that can detect whether similar failures are reappearing.

The project therefore begins to move from passive reflection toward active recurrence prevention.

---

## Actual Failure Patterns Absorbed

The initial v0.2 rules are derived from real implementation failures encountered while developing this repository, including:

* GitHub Actions `steps:` indentation errors
* `actions/setup-python` cache configuration errors
* Python `__future__` / `__file__` corruption
* JSON Schema backslash escaping errors
* YAML `*` list marker contamination

These were not merely fixed and forgotten.

They were converted into recurrence patterns, recurrence rules, and executable checks.

---

## Conceptual Model

A simple way to describe the version transition is:

```text
v0.1:
  Structural Rumination Record
  Failure is recorded and digested.

v0.2:
  Executable Recurrence Rules
  Failure is converted into a detectable recurrence pattern.
```

In metaphorical terms:

```text
v0.1 = digestive layer
v0.2 = first immune response
```

The project begins to learn from its own mistakes by turning them into validation structure.

---

## Toward Pre-release Rumination Gates

The next natural step is to connect executable recurrence checks into a pre-release gate.

A future release gate may include:

```text
1. Validate rumination records
2. Validate recurrence rule registry
3. Run executable recurrence checks
4. Detect repeated failure patterns
5. Block release if structural recurrence is found
```

This would allow the repository to ask before release:

```text
Have we repeated a failure that we already recorded?
```

That question is the foundation of a structural rumination gate.

---

## Version Position

```text
v0.1 = Structural Rumination Record
v0.2 = Executable Recurrence Rules
v0.3 = Multi-Wing Integration
v0.4 = AI Agent Hooks
```

v0.2 is the bridge between memory and action.

It turns remembered implementation failures into executable recurrence prevention.
