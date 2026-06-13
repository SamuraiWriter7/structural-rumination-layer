# Rumination Sieve Protocol

The **Rumination Sieve Protocol** is a staged method for reducing repeated structural mistakes in AI-assisted specification workflows.

It does not aim for zero mistakes.

Instead, it aims to prevent the same structural mistake from recurring without digestion.

In short:

> Mistakes may occur.
> But repeated structural mistakes must be passed through verification, reflection, rumination, and breathing alignment before the workflow proceeds.

日本語では：

> ミスは起こる。
> だが、同じ構造的過ちは、検証・反省・反芻・調息を通さずに次へ進めない。

---

## Purpose

AI-assisted GitHub work often fails not because the AI cannot produce complex output, but because basic structural checks are skipped.

Common repeated mistakes include:

* referencing files that do not exist,
* updating README before confirming the actual file tree,
* adding validator targets before schema/example pairs exist,
* assuming workflows exist before checking `.github/workflows`,
* drifting between documentation, schemas, examples, validators, and release notes,
* pushing repeated verification burden back to the human operator.

The Rumination Sieve Protocol exists to turn those errors into visible, reusable recurrence-prevention rules.

---

## Core Flow

The protocol follows this flow:

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

This flow transforms AI-assisted work from a one-way output process into a digestible cycle.

---

## 1. Forward Generation

Forward Generation is the normal creation path.

```text
Objective
→ Schema
→ Example
→ Validator
→ Documentation
→ Changelog
→ Release
```

This stage asks:

```text
What are we trying to create?
What artifacts are needed?
What files must be added or updated?
What should be validated before release?
```

Forward Generation is necessary, but it can also create risk.

AI systems often move quickly from concept to polished output.
Without later inspection, that speed may hide missing files, path mismatches, and unsupported assumptions.

---

## 2. Reverse Trace Check

Reverse Trace Check rewinds the workflow from output back to intention.

```text
Release
→ Changelog
→ Documentation
→ Validator
→ Example
→ Schema
→ Objective
```

This stage asks:

```text
Does the release match the changelog?
Does the changelog match the actual repository changes?
Does README reference only real files?
Does the validator reference existing schema/example pairs?
Does the example conform to the schema?
Does the schema still express the original objective?
```

Reverse Trace Check is the protocol's “思考の巻き戻し” layer.

It checks whether the final output can be traced backward to the original intent without broken links, unsupported assumptions, or hidden drift.

---

## 3. Verification

Verification checks what actually happened.

It should be concrete, observable, and grounded in repository state.

Examples:

```text
Did the referenced file exist?
Did the directory exist?
Did the validator pass?
Did the example match the schema?
Did README match the actual file tree?
Did CHANGELOG match the actual changes?
```

Verification is not interpretation.

It is the eye of the workflow.

It sees the current state before reflection begins.

---

## 4. Reflection

Reflection asks why the error happened.

Examples:

```text
Was repository state assumed before checking?
Was a path documented before file existence was confirmed?
Was a validator target added too early?
Was a known repeated error pattern ignored?
Did the workflow move too quickly from concept to release?
Did the human operator have to absorb avoidable rework?
```

Reflection is not apology.

It is cause classification.

The goal is to identify the structural bias that allowed the error to appear.

---

## 5. Rumination

Rumination converts the reflected lesson into a recurrence-prevention rule.

Examples:

```text
Do not reference a path unless the file tree confirms it.
Do not add validator targets until schema and example both exist.
Do not update release notes before CHANGELOG is aligned.
Do not propose GitHub Actions changes before confirming `.github/workflows`.
Do not proceed if the same structural error appears without a new rule.
```

Rumination is the digestive layer of the workflow.

It turns mistakes into future guardrails.

---

## 6. Breathing Alignment

Breathing Alignment calms and rebalances the workflow before proceeding.

It asks:

```text
Is the output too large?
Is uncertainty visible?
Has human burden been reduced?
Is the next step clear?
Is the workflow lighter than before?
Are we adding structure faster than we can verify it?
```

This stage prevents the protocol from becoming rigid perfectionism.

The goal is not to punish mistakes.

The goal is to restore flow.

---

## Rumination Sieve

The protocol uses three sieve passes.

This is the practical version of **三度目の正直**.

```text
Pass 1: Existence Check
Pass 2: Consistency Check
Pass 3: Recurrence Check
```

Each pass has a different purpose.

The same check is not repeated three times.
Instead, each pass filters a different class of error.

---

## Pass 1: Existence Check

Question:

```text
Do the referenced files and paths actually exist?
```

Check:

* schema files,
* example files,
* documentation files,
* script files,
* workflow directories,
* paths referenced in README,
* paths referenced in CHANGELOG,
* paths referenced in validation scripts.

Example rule:

```text
Do not document or validate a file path before confirming that the file exists.
```

This pass catches phantom structure.

---

## Pass 2: Consistency Check

Question:

```text
Do the artifacts align with each other?
```

Check:

* schema/example pairing,
* validator target alignment,
* README/file-tree alignment,
* CHANGELOG/change alignment,
* release note/changelog alignment,
* version naming consistency,
* stated scope versus actual files.

Example rule:

```text
Do not proceed if README, CHANGELOG, validator, and actual files describe different repository states.
```

This pass catches structural drift.

---

## Pass 3: Recurrence Check

Question:

```text
Is this the same structural error pattern as before?
```

Check for repeated patterns:

* path mismatch,
* validator target mismatch,
* documentation drift,
* workflow assumption,
* schema/example mismatch,
* premature release tagging,
* repeated human-side debugging burden.

Example rule:

```text
If the same structural error appears again, create or update a recurrence-prevention rule before proceeding.
```

This pass catches undigested mistakes.

---

## Error Visibility

A workflow should not close while errors remain invisible.

Before proceeding, make the following visible:

```text
What error occurred?
Where did it occur?
Why did it occur?
What burden did it create?
What rule prevents recurrence?
What uncertainty remains?
```

Invisible errors cannot become reflection.

Unreflected errors cannot become rumination.

Unruminated errors become repeated burden.

---

## Next-Gate Registration

After rumination, the new rule must be registered as a next-gate condition.

A recurrence-prevention rule should answer:

```text
Before what future action should this rule be checked?
What should block progress?
What uncertainty should be surfaced to the human?
```

Example:

```text
Rule:
Do not add validator targets until schema and example both exist.

Applies before:
- updating scripts/validate_examples.py
- updating README validation instructions
- preparing release notes

Block if:
- schema path is uncertain
- example path is uncertain
- schema/example pair has not been validated
```

This converts reflection into operational memory.

---

## Release Readiness Questions

Before release or tagging, run the following questions:

```text
Can the final output be traced backward to the original objective?
Do all referenced files exist?
Do schema and example pairs align?
Does the validator reference only existing pairs?
Does README match the real repository structure?
Does CHANGELOG match the actual changes?
Is any uncertainty clearly visible?
Has the same structural error appeared again?
If yes, was a recurrence-prevention rule created?
```

If the answer is unclear, do not hide the uncertainty.

Surface it.

Then breathe.

---

## Non-Goals

This protocol is not designed to:

* guarantee zero mistakes,
* replace human judgment,
* force excessive review loops,
* create rigid perfectionism,
* block all creative exploration,
* add process for its own sake.

Its purpose is narrower:

> Reduce recurrence.
> Reduce drift.
> Reduce human burden.
> Make errors digestible.

---

## Minimal v0.1 Scope

In v0.1, this protocol is intended to support:

* local schema/example validation,
* README and CHANGELOG consistency,
* repeated error pattern visibility,
* forward/reverse trace checks,
* recurrence-prevention rule creation.

It intentionally does not require:

* GitHub Actions,
* automated release tooling,
* multiple schema families,
* package publication,
* external service integration.

Those may be added later only after the core rumination cycle is stable.

---

## Japanese Summary

```text
一巡目で存在を確かめる。
二巡目で整合を確かめる。
三巡目で再発を確かめる。

順送りで作り、
逆送りでほどき、
検証で見て、
反省で原因を分け、
反芻で次の規則に変え、
調息で流れを整える。

ミスは起こる。
だが、同じ構造的過ちは二度通さない。
```

---

## Core Principle

> A workflow is not complete until its final output can be traced backward to its original intent without unresolved structural drift.

In Japanese:

> 最終出力が、元の意図まで破綻なく巻き戻せるまで、作業は完了しない。
