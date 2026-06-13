# Structural Rumination Layer

**Structural Rumination Layer** is a protocol for reducing repeated structural errors in AI-assisted specification workflows.

It does not aim to make AI perfectly error-free.

Instead, it helps AI systems and human operators verify outputs, reflect on mistakes, ruminate on repeated error patterns, convert them into recurrence-prevention rules, share those rules across multiple structural wings, and connect them to AI agent execution boundaries.

In short:

> Mistakes may occur.
> But the same structural mistake should not pass through the workflow unchanged twice.

日本語では：

> ミスは起こる。
> だが、同じ構造的過ちは二度通さない。

---

## Purpose

AI systems can generate advanced reasoning, documentation, schemas, examples, validators, and release notes.

However, in practical GitHub specification work, they may still repeat basic structural mistakes, such as:

* referencing files that do not exist,
* adding validator targets before schema/example pairs are complete,
* drifting between README, CHANGELOG, and actual repository state,
* assuming `.github/workflows` exists when it does not,
* producing polished documentation before verifying concrete file paths,
* repeating YAML / JSON / Python syntax mistakes during rapid iteration,
* recommending releases before validation evidence is complete,
* pushing repeated debugging work back onto the human operator.

This repository defines a minimal protocol for digesting those errors instead of merely correcting them once.

The goal is not binary perfection.

The goal is:

> Bias correction, recurrence reduction, cross-wing failure sharing, AI agent boundary checks, and human burden reduction through structured rumination.

---

## Core Concept

`structural-rumination-layer` is a minimal OS for treating AI development failures not as disposable logs, but as structural data that can be recorded, digested, converted into recurrence-prevention rules, shared across wings, and connected to AI agent execution boundaries.

The project evolves through these layers:

```text
v0.1 = Structural Rumination Record
       Failure becomes structured memory.

v0.2 = Executable Recurrence Rules
       Structured memory becomes executable prevention.

v0.3 = Multi-Wing Integration
       Recurrence knowledge becomes shareable across wings.

v0.4 = AI Agent Hooks
       Recurrence knowledge becomes agent-facing execution guidance.
```

In metaphorical terms:

```text
v0.1 = digestive layer
v0.2 = first immune response
v0.3 = cross-wing nervous system
v0.4 = agent-facing reflex layer
```

---

## Core Lifecycle

The core lifecycle is:

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

This turns AI-assisted work from a simple output loop into a learning workflow.

---

## 1. Forward Generation

The workflow moves from intention to output.

```text
Objective
  -> Schema
  -> Example
  -> Validator
  -> Documentation
  -> Changelog
  -> Release
```

Forward generation is useful for creating artifacts, but it can also cause AI systems to move too quickly.

Without later inspection, this can lead to polished but inconsistent output.

---

## 2. Reverse Trace Check

The workflow is then checked backward.

```text
Release
  -> Changelog
  -> Documentation
  -> Validator
  -> Example
  -> Schema
  -> Objective
```

Reverse trace checks whether the final output can be traced back to the original intention without broken links, missing files, or unsupported assumptions.

This is the “思考の巻き戻し” layer.

---

## 3. Verification

Verification checks what actually happened.

Examples:

* Did the referenced file exist?
* Did the validator pass?
* Did the example match the schema?
* Did README match the real repository structure?
* Did CHANGELOG match the actual changes?
* Did the executable recurrence checks pass?
* Did the agent hook require human review before release?

Verification is the eye of the workflow.

It sees the concrete state before interpretation begins.

---

## 4. Reflection

Reflection identifies why the error happened.

Examples:

* Was repository state assumed before checking?
* Was a validator target added too early?
* Was README updated before file paths were confirmed?
* Was a previous recurrence rule ignored?
* Was an AI agent allowed to proceed without a boundary check?
* Did the burden shift back to the human operator?

Reflection is not about apology.

It is about cause classification.

---

## 5. Rumination

Rumination converts the lesson into a recurrence-prevention rule.

Examples:

* Do not reference a path unless the file tree confirms it.
* Do not add validator targets until schema and example both exist.
* Do not propose workflow edits before confirming workflow existence.
* Do not proceed to release if README and CHANGELOG drift from actual files.
* Do not recommend a candidate tag before validation evidence is available.
* Do not allow the same structural error to recur without a new rule.

Rumination is the digestive layer of the workflow.

It turns mistakes into future guardrails.

---

## 6. Breathing Alignment

Breathing Alignment calms and rebalances the workflow before proceeding.

It asks:

* Is the output too large?
* Is uncertainty visible?
* Has human burden been reduced?
* Is the next step clear?
* Is the workflow lighter than before?
* Should an AI agent pause, warn, block, or ask for human review?

This prevents reflection from becoming rigid perfectionism.

The purpose is not to punish errors.

The purpose is to restore flow.

---

## 7. Error Visibility

Errors must be visible before they can be digested.

The final check should make the following clear:

* What error occurred?
* Why did it occur?
* What burden did it create?
* What recurrence rule prevents it?
* What uncertainty remains?
* Can this recurrence pattern help another wing?
* Should this recurrence pattern become an AI agent hook?

Invisible errors cannot become reflection, rumination, recurrence prevention, cross-wing learning, or agent-facing execution guidance.

---

## Rumination Sieve

Structural errors are passed through three sieve layers.

This is the protocol version of 三度目の正直.

```text
Pass 1: Existence Check
Pass 2: Consistency Check
Pass 3: Recurrence Check
```

### Pass 1: Existence Check

Question:

> Do the referenced files and paths actually exist?

Examples:

* Does the schema exist?
* Does the example exist?
* Does the docs path exist?
* Does `.github/workflows` exist before referencing it?

### Pass 2: Consistency Check

Question:

> Do the artifacts align with each other?

Examples:

* Does README match the real file tree?
* Does CHANGELOG match actual changes?
* Does the validator reference existing schema/example pairs?
* Does the example conform to the schema?

### Pass 3: Recurrence Check

Question:

> Is this the same structural error pattern as before?

Examples:

* repeated path mismatch,
* repeated validator target mismatch,
* repeated workflow assumption,
* repeated README/file-tree drift,
* repeated human-side debugging burden,
* repeated YAML / JSON / Python syntax corruption,
* repeated release recommendation before validation evidence.

A workflow should not proceed if the same structural error pattern appears again without a new recurrence-prevention rule.

---

## v0.1 — Structural Rumination Record

v0.1 defines the first minimal structure for recording, digesting, and reducing repeated structural errors in AI-assisted specification workflows.

It introduces:

* the core rumination lifecycle,
* the Rumination Sieve,
* final error visibility checks,
* a structural rumination schema,
* a validated example,
* local example validation,
* initial GitHub Actions validation.

In short:

```text
v0.1 = record and digest failure
```

---

## v0.2 — Executable Recurrence Rules

As of v0.2, `structural-rumination-layer` extends Structural Rumination Records into executable recurrence checks.

The project no longer treats implementation failures as passive logs.

Instead, repeated failure patterns are converted into rule definitions and validation scripts that can detect similar errors before release.

In short:

```text
v0.2 = detect recurrence
```

### What v0.2 adds

* `rules/recurrence-rules.yaml`

  * Defines recurrence patterns and executable recurrence rules.
* `scripts/check_recurrence_rules.py`

  * Validates the recurrence rule registry itself.
* `scripts/check_workflow_structure.py`

  * Detects recurring GitHub Actions workflow structure problems.
* `scripts/check_yaml_lists.py`

  * Detects malformed YAML list contamination such as unquoted `*` markers.
* `scripts/check_json_schema_syntax.py`

  * Ensures JSON Schema files are parseable as strict JSON.
* `scripts/check_python_syntax.py`

  * Checks Python scripts for syntax errors and suspicious dunder corruption patterns.
* `docs/executable-recurrence-rules.md`

  * Explains how recurrence patterns become executable validation checks.

These checks are derived from actual implementation failures encountered during the development of this repository, including workflow indentation issues, Python syntax corruption, JSON escaping errors, and YAML list marker contamination.

---

## v0.3 — Multi-Wing Integration

As of v0.3, `structural-rumination-layer` extends recurrence knowledge across multiple wings.

A wing may be:

* a GitHub repository,
* an AI agent,
* a GPT configuration,
* a validator,
* a schema module,
* a documentation layer,
* a governance layer,
* another structural protocol implementation.

The goal is to allow one wing’s failure pattern to become another wing’s prevention signal.

In short:

```text
v0.3 = share recurrence knowledge across wings
```

### What v0.3 adds

* `docs/multi-wing-integration.md`

  * Explains how recurrence knowledge can move across repositories, agents, validators, and structural protocol layers.
* `schemas/multi-wing-rumination-link.schema.json`

  * Defines a schema for linking recurrence patterns and recurrence rules across multiple wings.
* `examples/multi-wing-rumination-link.example.yaml`

  * Provides a validated example of a recurrence rule being adapted from one wing to another.
* `scripts/validate_examples.py`

  * Validates the multi-wing rumination link example.

v0.3 turns local recurrence prevention into cross-wing immune memory.

A failure pattern discovered in one context can now become a structural warning, reference, or adapted check in another.

---

## v0.4 — AI Agent Hooks

As of v0.4, `structural-rumination-layer` connects recurrence knowledge to AI agent execution boundaries.

An AI agent should not only generate outputs.

It should also pass through structural rumination boundaries before, during, and after execution.

These boundaries are called **AI Agent Hooks**.

In short:

```text
v0.4 = hook recurrence knowledge into AI agent execution
```

### What v0.4 adds

* `docs/ai-agent-hooks.md`

  * Explains how recurrence knowledge can be connected to AI agent execution boundaries.
* `schemas/ai-agent-rumination-hook.schema.json`

  * Defines a schema for representing AI agent rumination hooks.
* `examples/ai-agent-rumination-hook.example.yaml`

  * Provides a validated example of a pre-release agent hook.
* `scripts/validate_examples.py`

  * Validates the AI agent rumination hook example.

### Hook types

v0.4 defines the following hook types:

* `pre_run`

  * Runs before an AI agent begins a task.
* `pre_write`

  * Runs before an AI agent writes or modifies files.
* `post_run`

  * Runs after an AI agent completes a task.
* `pre_release`

  * Runs before a tag, release, or candidate state.
* `failure_capture`

  * Runs when an error occurs and may trigger rumination recording.

### Hook actions

An AI Agent Hook may:

* allow execution,
* warn,
* block,
* request validation,
* create a rumination record,
* escalate to human review.

v0.4 turns recurrence knowledge into agent-facing execution guidance.

It is the first step toward structural rumination gates for AI-assisted development.

---

## Repository Structure

```text
docs/
  ai-agent-hooks.md
  executable-recurrence-rules.md
  final-error-visibility-check.md
  multi-wing-integration.md
  rumination-sieve-protocol.md

rules/
  recurrence-rules.yaml

schemas/
  ai-agent-rumination-hook.schema.json
  multi-wing-rumination-link.schema.json
  rumination-record.schema.json

examples/
  ai-agent-rumination-hook.example.yaml
  multi-wing-rumination-link.example.yaml
  rumination-record.example.yaml

scripts/
  check_json_schema_syntax.py
  check_python_syntax.py
  check_recurrence_rules.py
  check_workflow_structure.py
  check_yaml_lists.py
  validate_examples.py

.github/
  workflows/
    validate-examples.yml

README.md
CHANGELOG.md
```

---

## Key Documents

* [`docs/rumination-sieve-protocol.md`](docs/rumination-sieve-protocol.md)

  * Explains the three-pass structural rumination sieve.
* [`docs/final-error-visibility-check.md`](docs/final-error-visibility-check.md)

  * Defines the final visibility check before moving forward.
* [`docs/executable-recurrence-rules.md`](docs/executable-recurrence-rules.md)

  * Explains how recorded recurrence patterns become executable validation checks.
* [`docs/multi-wing-integration.md`](docs/multi-wing-integration.md)

  * Explains how recurrence knowledge can be shared across wings.
* [`docs/ai-agent-hooks.md`](docs/ai-agent-hooks.md)

  * Explains how recurrence knowledge can be connected to AI agent execution boundaries.

---

## Schemas

### Rumination Record

```text
schemas/rumination-record.schema.json
```

Records:

* repository scope,
* forward trace,
* reverse trace,
* verification results,
* reflection root causes,
* rumination rules,
* breathing alignment state,
* visible error summary,
* next-gate conditions.

### Multi-Wing Rumination Link

```text
schemas/multi-wing-rumination-link.schema.json
```

Records:

* source wing,
* target wing,
* link type,
* linked recurrence rule,
* adaptation status,
* validation status,
* human review boundary,
* notes.

### AI Agent Rumination Hook

```text
schemas/ai-agent-rumination-hook.schema.json
```

Records:

* hook ID,
* agent identity,
* hook type,
* execution boundary,
* linked recurrence rules,
* linked rumination records,
* linked multi-wing references,
* hook action,
* validation status,
* human review boundary,
* notes.

---

## Examples

### Rumination Record Example

```text
examples/rumination-record.example.yaml
```

Demonstrates how to record a repeated structural error pattern and convert it into a recurrence-prevention rule.

### Multi-Wing Rumination Link Example

```text
examples/multi-wing-rumination-link.example.yaml
```

Demonstrates how a recurrence rule from one wing can be referenced, adapted, or reused by another wing.

### AI Agent Rumination Hook Example

```text
examples/ai-agent-rumination-hook.example.yaml
```

Demonstrates how recurrence rules and multi-wing rumination links can be connected to an AI agent’s pre-release execution boundary.

---

## Validation

Install dependencies:

```bash
pip install jsonschema pyyaml
```

Run the full local validation suite:

```bash
python scripts/check_recurrence_rules.py
python scripts/check_workflow_structure.py
python scripts/check_yaml_lists.py
python scripts/check_json_schema_syntax.py
python scripts/check_python_syntax.py
python scripts/validate_examples.py
```

Expected result:

```text
All checks pass.
```

These checks validate:

* the recurrence rule registry,
* GitHub Actions workflow structure,
* YAML list marker hygiene,
* JSON Schema syntax,
* Python syntax and suspicious dunder corruption patterns,
* schema/example consistency,
* multi-wing rumination link examples,
* AI agent rumination hook examples.

---

## Continuous Validation

This repository includes a minimal GitHub Actions workflow for validating confirmed schema/example pairs and recurrence checks.

Workflow:

```text
.github/workflows/validate-examples.yml
```

The workflow runs on:

* push to `main`,
* pull requests targeting `main`,
* manual dispatch.

The workflow intentionally remains small.

It does not attempt to automate release generation, package publishing, broad multi-repository execution, or live AI agent orchestration yet.

Its purpose is narrower:

> Keep the rumination loop executable, visible, stable, and agent-aware.

---

## CI Status

The validation workflow has passed after resolving and digesting the first set of structural rumination errors.

The first-generation errors digested during this process included:

* GitHub Actions `steps:` indentation drift,
* `setup-python` cache assumptions without dependency files,
* Python double-underscore name corruption during code transfer,
* JSON Schema regex escape errors,
* YAML list syntax corruption caused by Markdown-style `*` bullets.

These were not treated as isolated fixes.

They were treated as first-generation rumination records and converted into recurrence-prevention rules.

In short:

> The repository has already begun using its own protocol to digest its own structural errors.

---

## Design Philosophy

This repository rejects binary perfectionism.

It does not say:

> AI must never make mistakes.

Instead, it says:

> Mistakes may occur.
> Repeated structural mistakes must be digested.
> Recurrence rules must become executable.
> Useful failure knowledge should be shareable across wings.
> AI agents should pass through structural rumination boundaries.
> The workflow must become lighter after each cycle.

The goal is not zero error.

The goal is reduced recurrence, reduced human burden, better structural digestion, and safer agent-assisted execution.

---

## Relationship to AI-Assisted GitHub Specification Work

This protocol is intended for workflows involving:

* JSON Schema design,
* YAML examples,
* local validators,
* README updates,
* CHANGELOG updates,
* release notes,
* repository structure validation,
* AI-assisted documentation,
* recurring error pattern management,
* multi-agent or multi-repository specification work,
* AI agent pre-run, pre-write, post-run, pre-release, and failure-capture boundaries.

It is especially useful when AI systems repeatedly produce plausible but structurally inconsistent outputs.

---

## Minimal Scope

This repository intentionally grows in small verified steps.

Current scope:

```text
v0.1 = Structural Rumination Record
v0.2 = Executable Recurrence Rules
v0.3 = Multi-Wing Integration
v0.4 = AI Agent Hooks
```

Not included yet:

* automated release generation,
* external package publishing,
* full multi-repository orchestration,
* live AI agent runtime integration,
* automatic rule propagation across repositories,
* autonomous blocking of external agent actions.

These are deferred to avoid adding structure faster than it can be verified.

---

## Version Position

```text
v0.1 = Structural Rumination Record
       Failure is recorded and digested.

v0.2 = Executable Recurrence Rules
       Failure is converted into executable recurrence checks.

v0.3 = Multi-Wing Integration
       Failure knowledge is linked across structural wings.

v0.4 = AI Agent Hooks
       Recurrence knowledge is connected to AI agent execution boundaries.
```

---

## Status

Current version:

```text
v0.4.0-candidate
```

This version introduces the first validated structure for connecting recurrence knowledge to AI agent execution boundaries.

---

## Summary

Structural Rumination Layer exists to give AI-assisted work a digestive system, an immune response, a cross-wing nervous system, and the beginning of an agent-facing reflex layer.

It helps transform:

```text
Output
  -> Error
  -> Correction
  -> Repeated Error
```

into:

```text
Output
  -> Error Visibility
  -> Reflection
  -> Rumination
  -> Recurrence Prevention
  -> Cross-Wing Learning
  -> Agent Boundary Check
  -> Lighter Workflow
```

In one sentence:

> Verify with the eyes, reflect with the mind, ruminate with the stomach, circulate through the wings, hook into the agent boundary, and align the breath before moving forward.


