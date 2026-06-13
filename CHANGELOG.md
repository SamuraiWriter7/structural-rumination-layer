# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple principle:

> Mistakes may occur.
> But the same structural mistake should not pass through the workflow unchanged twice.

日本語では：

> ミスは起こる。
> だが、同じ構造的過ちは二度通さない。

---

## [0.4.0-candidate] - 2026-06-14

### Added

* Added `docs/ai-agent-hooks.md`.

  * Explains how recurrence knowledge can be connected to AI agent execution boundaries.
* Added `schemas/ai-agent-rumination-hook.schema.json`.

  * Defines the structure for AI agent rumination hooks.
* Added `examples/ai-agent-rumination-hook.example.yaml`.

  * Demonstrates how recurrence rules and multi-wing rumination links can be connected to an AI agent’s pre-release execution boundary.
* Added AI Agent Hooks as the v0.4 theme.

  * `v0.1 = Structural Rumination Record`
  * `v0.2 = Executable Recurrence Rules`
  * `v0.3 = Multi-Wing Integration`
  * `v0.4 = AI Agent Hooks`

### Changed

* Extended the project from cross-wing recurrence sharing toward AI agent execution boundary guidance.
* Updated the validation flow to include the AI agent rumination hook schema/example pair.
* Updated the conceptual model from a digestive / immune / nervous system model toward an agent-facing reflex layer.
* Clarified that recurrence knowledge can influence AI agent behavior before, during, or after execution.
* Added AI agent hook types:

  * `pre_run`
  * `pre_write`
  * `post_run`
  * `pre_release`
  * `failure_capture`
* Added hook actions:

  * `allow`
  * `warn`
  * `block`
  * `request_validation`
  * `create_rumination_record`
  * `escalate_to_human`

### Validated

* Confirmed that GitHub Actions passes with the v0.4 AI Agent Hooks schema/example pair included.
* Confirmed that `examples/ai-agent-rumination-hook.example.yaml` validates against `schemas/ai-agent-rumination-hook.schema.json`.
* Confirmed that README, CHANGELOG, docs, schema, example, and validation flow are aligned for the v0.4 candidate state.

### Conceptual Notes

v0.4 introduces the first structure for connecting recurrence knowledge to AI agent execution boundaries.

An AI agent can now be represented as passing through hooks such as:

* pre-run checks,
* pre-write checks,
* post-run checks,
* pre-release checks,
* failure-capture checks.

This allows recurrence rules and rumination records to become agent-facing execution guidance.

In short:

```text
v0.1 = record failure
v0.2 = detect recurrence
v0.3 = share recurrence knowledge across wings
v0.4 = hook recurrence knowledge into AI agent execution
```

---

## [0.3.0-candidate] - 2026-06-14

### Added

* Added `docs/multi-wing-integration.md`.

  * Explains how recurrence knowledge can move across multiple wings, including repositories, AI agents, validators, schema modules, documentation layers, and governance layers.
* Added `schemas/multi-wing-rumination-link.schema.json`.

  * Defines the structure for linking recurrence patterns and recurrence rules across wings.
* Added `examples/multi-wing-rumination-link.example.yaml`.

  * Demonstrates how a recurrence rule from one wing can be adapted for another wing.
* Added Multi-Wing Integration as the v0.3 theme.

  * `v0.1 = Structural Rumination Record`
  * `v0.2 = Executable Recurrence Rules`
  * `v0.3 = Multi-Wing Integration`

### Changed

* Extended the project from local recurrence prevention toward cross-wing recurrence knowledge sharing.
* Updated the validation flow to include the multi-wing rumination link schema/example pair.
* Updated the conceptual model from a single-repository digestive/immune loop toward a distributed structural learning model.
* Clarified that a wing may be a repository, AI agent, GPT configuration, validator, schema module, documentation layer, governance layer, or other structural protocol component.

### Validated

* Confirmed that GitHub Actions passes with the v0.3 Multi-Wing Integration schema/example pair included.
* Confirmed that `examples/multi-wing-rumination-link.example.yaml` validates against `schemas/multi-wing-rumination-link.schema.json`.
* Confirmed that the repository can now represent recurrence knowledge transfer across wings.

### Conceptual Notes

v0.3 introduces the first structure for cross-wing immune memory.

A failure pattern discovered in one wing can now become:

* a pattern reference,
* a rule adaptation,
* a check reuse candidate,
* a governance signal,
* an agent hook candidate.

This allows local failure digestion to become shared recurrence-prevention knowledge.

In short:

```text
v0.1 = record failure
v0.2 = detect recurrence
v0.3 = share recurrence knowledge across wings
```

---

## [0.2.0-candidate] - 2026-06-14

### Added

* Added `rules/recurrence-rules.yaml` as the initial executable recurrence rule registry.
* Added `scripts/check_recurrence_rules.py` to validate the recurrence rule registry.
* Added `scripts/check_workflow_structure.py` to detect recurring GitHub Actions workflow structure issues.
* Added `scripts/check_yaml_lists.py` to detect malformed YAML list marker contamination.
* Added `scripts/check_json_schema_syntax.py` to ensure JSON Schema files are parseable as strict JSON.
* Added `scripts/check_python_syntax.py` to detect Python syntax errors and suspicious dunder corruption patterns.
* Added `docs/executable-recurrence-rules.md` to document the v0.2 rule execution model.
* Introduced the v0.2 theme: **Executable Recurrence Rules**.

### Changed

* Extended the project from passive Structural Rumination Records toward executable recurrence checks.
* Reframed recorded implementation failures as reusable recurrence prevention rules.
* Updated the validation flow to include executable recurrence rule checks.
* Clarified the transition from structural failure memory to executable recurrence detection.

### Validated

* Confirmed that GitHub Actions passes with the v0.2 executable recurrence checks enabled.
* Confirmed that the recurrence rule registry is structurally valid.
* Confirmed that previously observed error patterns have been converted into structural recurrence checks.

### Rumination Notes

The v0.2 recurrence checks were derived from actual implementation failures encountered during repository development, including:

* GitHub Actions `steps:` indentation errors,
* `actions/setup-python` cache configuration errors,
* Python `__future__` / `__file__` corruption,
* JSON Schema backslash escaping errors,
* YAML `*` list marker contamination.

These were not merely fixed and forgotten.

They were converted into recurrence patterns, recurrence rules, and executable validation scripts.

In short:

```text
v0.1 = failure becomes structured memory
v0.2 = structured memory becomes executable prevention
```

---

## [0.1.0-candidate] - 2026-06-14

### Added

* Added initial definition of **Structural Rumination Layer**.
* Added the core lifecycle:

```text
Forward Generation
  -> Reverse Trace Check
  -> Verification
  -> Reflection
  -> Rumination
  -> Breathing Alignment
  -> Error Visibility
  -> Next-Gate Registration
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
* Added GitHub Actions validation workflow:

  * `.github/workflows/validate-examples.yml`

### Changed

* Established the repository as a minimal protocol for reducing repeated structural errors in AI-assisted specification workflows.
* Defined failure not as a disposable log, but as structured data that can become recurrence-prevention knowledge.
* Clarified the role of verification, reflection, rumination, breathing alignment, and error visibility in the workflow.

### Validated

* Confirmed that the initial rumination record example validates against the rumination record schema.
* Confirmed that local validation can run through `scripts/validate_examples.py`.
* Confirmed that GitHub Actions validation passes for the initial v0.1 structure.

### Rumination Notes

The first CI validation cycle surfaced and digested several structural errors:

* GitHub Actions YAML indentation error around `steps:`.
* `setup-python` cache configuration used without `requirements.txt` or `pyproject.toml`.
* Python double-underscore names were corrupted during code transfer.
* JSON Schema regex backslashes were not escaped correctly.
* YAML example lists used Markdown-style `*` bullets instead of YAML `-` list markers.

These errors were converted into recurrence-prevention rules.

The v0.1 workflow confirmed that:

* schema/example validation can run locally,
* the same validation can run in GitHub Actions,
* the repository can use its own rumination protocol to identify and reduce repeated structural errors.

### Design Notes

This version intentionally keeps the scope small.

It does not attempt to make AI-assisted workflows perfectly error-free.

Instead, it focuses on:

* making errors visible,
* identifying repeated structural patterns,
* converting mistakes into recurrence-prevention rules,
* reducing human-side rework,
* preventing workflow drift before release.

### Intentionally Deferred

The following features are intentionally deferred beyond v0.1:

* executable recurrence rule registry,
* multiple schema support,
* cross-wing recurrence sharing,
* automated release generation,
* external package publishing,
* AI agent runtime hooks.

These are deferred to avoid adding structure faster than it can be verified.

### Core Rule

> Do not proceed if the same structural error pattern appears again without a new recurrence-prevention rule.

In Japanese:

> 同じ構造的過ちが再発した場合、反芻と再発防止ルールなしに次へ進まない。

### Status

This is the first candidate release of Structural Rumination Layer.

The purpose of this version is to establish the minimum digestive structure for AI-assisted GitHub specification work before expanding the repository.

