# Final Error Visibility Check

The **Final Error Visibility Check** is the closing step of the Structural Rumination Layer.

Its purpose is not only to determine whether the output is correct.

Its purpose is to make errors, uncertainties, recurrence risks, and human-side burdens visible before the workflow proceeds.

In short:

> Invisible errors cannot be digested.
> Visible errors can become reflection, rumination, and recurrence prevention.

日本語では：

> 見えないミスは消化されない。
> 見える化されたミスだけが、反省・反芻・再発防止に回せる。

---

## Purpose

AI-assisted specification work often produces polished output before all structural errors are visible.

This can create hidden drift between:

* actual repository state,
* README,
* CHANGELOG,
* schemas,
* examples,
* validators,
* release notes,
* human expectations.

The Final Error Visibility Check prevents the workflow from closing while unresolved errors remain hidden.

It is the final breathing alignment before the next step.

---

## Core Principle

> A workflow should not be considered complete until its visible errors, remaining uncertainties, and recurrence risks have been surfaced.

This does not mean every mistake must be eliminated.

It means every known structural risk should be made visible enough to be digested or explicitly carried forward.

---

## What Must Be Made Visible

The final check should surface five things:

```text id="ksr7yy"
1. What happened?
2. Where did it happen?
3. Why did it happen?
4. What burden did it create?
5. What prevents recurrence?
```

These five questions turn an error from a vague failure into a reusable learning unit.

---

## 1. What Happened?

Describe the observable error or uncertainty.

Examples:

```text id="6z7v4p"
A referenced file did not exist.
A schema/example pair was incomplete.
A validator target pointed to the wrong path.
README described files that were not yet created.
CHANGELOG included changes that were not implemented.
A workflow was assumed before `.github/workflows` existed.
```

This stage should be factual.

Avoid vague statements such as:

```text id="oohj9a"
Something may be wrong.
```

Prefer concrete statements such as:

```text id="vnikdx"
README references `docs/example.md`, but that file has not been confirmed.
```

---

## 2. Where Did It Happen?

Identify the affected artifact or workflow stage.

Examples:

```text id="7uvoym"
schemas/
examples/
scripts/validate_examples.py
README.md
CHANGELOG.md
docs/
release notes
tagging process
```

The goal is to locate the error precisely enough that it can be checked again later.

---

## 3. Why Did It Happen?

Identify the likely structural cause.

Examples:

```text id="i03oox"
Repository state was assumed before verification.
Forward generation moved faster than reverse trace checking.
A validator target was added before schema/example pairing was complete.
Documentation was updated before file existence was confirmed.
A previous error pattern was not checked before proceeding.
The AI output shifted verification burden back to the human operator.
```

This stage is reflection.

The goal is not blame.

The goal is cause classification.

---

## 4. What Burden Did It Create?

Record the human-side burden created by the error.

Examples:

```text id="xrt9zi"
manual debugging
repeated command execution
extra file-tree checking
additional copy-paste corrections
delayed release preparation
increased cognitive fatigue
loss of workflow momentum
```

Human burden must be visible because AI errors often appear small in output but large in operational cost.

A path mismatch may be one line of text for the AI.

For the human operator, it may create several rounds of checking, correction, and re-validation.

---

## 5. What Prevents Recurrence?

Convert the visible error into a recurrence-prevention rule.

Examples:

```text id="jy606p"
Do not reference a file path unless the file tree confirms it.
Do not add validator targets until schema and example both exist.
Do not update README before confirming repository structure.
Do not prepare release notes before CHANGELOG reflects actual changes.
Do not propose GitHub Actions changes before confirming `.github/workflows`.
Do not proceed if the same structural error appears without a new rule.
```

This is where visibility becomes rumination.

An error is not fully digested until it changes a future gate.

---

## Final Visibility Template

Use the following template before closing a workflow step:

```yaml id="vc99pa"
final_error_visibility_check:
  status: "passed_with_warnings"

  visible_errors:
    - type: "documentation_drift"
      location: "README.md"
      description: "README references should be checked against the actual file tree before release."

  remaining_uncertainty:
    - "GitHub Actions workflow is intentionally not included in v0.1."
    - "Release tagging should occur only after local validation passes."

  human_burden:
    created:
      - "manual file-tree confirmation may still be needed before tagging"
    reduced:
      - "workflow assumptions were not added prematurely"
      - "validator scope remains limited to one confirmed schema/example pair"

  recurrence_prevention:
    rules:
      - id: "path-confirmation-before-documentation"
        rule: "Do not document file paths before confirming they exist."
      - id: "validator-after-pairing"
        rule: "Do not add validator targets until schema and example both exist."

  breathing_alignment:
    output_pressure: "medium"
    proceed: true
    reason: "Known uncertainty is visible and deferred items are explicitly scoped."
```

---

## Visibility Levels

Not every issue has the same severity.

Use simple visibility levels:

```text id="66bb9m"
Info     - visible note, no immediate risk
Warning  - should be checked before release
Error    - must be corrected before proceeding
Blocker  - workflow must stop until resolved
```

Examples:

### Info

```text id="ylddxv"
GitHub Actions are not included in v0.1 by design.
```

### Warning

```text id="rmy43e"
README file references should be checked before tagging.
```

### Error

```text id="zqtc1y"
Validator references a schema file that does not exist.
```

### Blocker

```text id="2h86k7"
The same structural error has recurred without a recurrence-prevention rule.
```

---

## Closing Questions

Before ending a work cycle, answer these questions:

```text id="extepl"
What errors were found?
What uncertainty remains?
What error pattern might recur?
What rule prevents recurrence?
Was human burden reduced?
Is anything being hidden for the sake of moving quickly?
Can the next step proceed with a calmer workflow?
```

If these questions cannot be answered, the workflow should not be treated as fully closed.

---

## Breathing Alignment

The final check should not become rigid perfectionism.

Its purpose is not to freeze the workflow.

Its purpose is to calm the workflow and prevent undigested errors from being carried forward.

Ask:

```text id="n4b1zw"
Are we over-generating?
Are we hiding uncertainty?
Are we adding structure faster than we can verify it?
Are we pushing unresolved checking back to the human?
Are we repeating the same structural mistake?
```

If the answer is yes, breathe before proceeding.

Breathing Alignment means:

```text id="3whsg3"
make uncertainty visible,
reduce output pressure,
defer non-essential structure,
register recurrence rules,
move forward only when the next step is lighter.
```

---

## When to Stop

The workflow should stop or pause when:

```text id="dlqdp5"
a referenced file path is uncertain,
a validator target points to an unconfirmed file,
README and repository state disagree,
CHANGELOG describes changes that are not implemented,
the same structural error pattern appears again,
human-side burden is increasing instead of decreasing.
```

Stopping is not failure.

Stopping is a form of structural digestion.

It prevents a small error from becoming repeated operational burden.

---

## When to Proceed

The workflow may proceed when:

```text id="e2fsrp"
known errors are visible,
remaining uncertainty is named,
schema/example pairs are confirmed,
validator scope is clear,
README and CHANGELOG match the current scope,
repeated error risks have recurrence-prevention rules,
the next step is smaller and clearer than before.
```

Proceeding should feel lighter, not heavier.

---

## Non-Goals

The Final Error Visibility Check is not designed to:

* guarantee zero errors,
* create excessive review loops,
* punish mistakes,
* replace human judgment,
* force all uncertainty to disappear,
* block creative specification work.

Its purpose is narrower:

> Make errors visible enough to be digested.

---

## Minimal v0.1 Use

For v0.1 of Structural Rumination Layer, this check should be used before:

* updating README,
* updating CHANGELOG,
* adding validator targets,
* preparing release notes,
* tagging a candidate release,
* introducing GitHub Actions,
* expanding to multiple schemas.

This is especially important before adding automation.

Automation should not be added on top of hidden structural drift.

---

## Japanese Summary

```text id="xj70oz"
最後に見る。
最後に照らす。
最後に息を整える。

何が起きたか。
どこで起きたか。
なぜ起きたか。
どんな負担を生んだか。
次にどう防ぐか。

見えないミスは消化されない。
見える化されたミスだけが、反芻され、
次の風路を整える。
```

---

## Core Rule

> Do not close the workflow while repeated structural errors remain invisible.

In Japanese:

> 同じ構造的過ちが見えないまま、作業を閉じてはならない。
