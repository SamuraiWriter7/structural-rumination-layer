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
