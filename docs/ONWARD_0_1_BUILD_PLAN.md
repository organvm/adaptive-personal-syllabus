# Onward 0.1 Build Plan

## Purpose

This document converts the Adaptive Personal Syllabus concept into the next executable build layer: a local-first personalized learning runtime that uses the existing CLI, learner profile, corpus ingestion, ledger, and plan generation machinery as the base system.

## Current Repo Reality

The repository already contains a functioning Python package and CLI entry surface. The project scripts expose `syllabus`, `aps`, and `aps-data-export`. The existing CLI already includes command groups for profile initialization, corpus ingestion, ledger verification, plan generation, chamber hook execution, and documentation audits.

Therefore, milestone 0.1 should not recreate the project. It should add the missing learner-facing runtime loop.

## Product Thesis

Adaptive Personal Syllabus transforms any learning source into a personalized initiation path by binding source material to a learner model, current skill state, active projects, preferred vocabulary, and concrete build outputs.

The first user is the builder. The system should teach the builder how to build the system.

## Milestone 0.1 Goal

Create a minimal local runtime that can:

1. Load a learner profile.
2. Load or reference one learning source.
3. Generate one personalized lesson stub.
4. Bind that lesson to one concrete repo task.
5. Render the result in the CLI.
6. Record the event in the ledger.

## Initial Source

`AI Engineering from Scratch` should be treated as the first external curriculum source. It is not the whole educational stack, but it is an appropriate first corpus for AI engineering, transformers, agents, RAG, and implementation-from-first-principles work.

## First Personalized Learning Target

The first adapted path should teach the builder:

- how to operate the existing CLI;
- how to understand the current repo architecture;
- how to build a terminal interface layer;
- how to add AI-assisted lesson personalization;
- how to convert generic learning material into project-bound tasks.

## 0.1 Runtime Loop

```text
profile.json
  -> source descriptor
  -> personalization context
  -> lesson stub
  -> repo task
  -> CLI rendering
  -> ledger event
```

## Proposed New Command

```bash
aps lesson next \
  --profile ~/.adaptive-syllabus/profile.json \
  --source data/sources/ai_engineering_from_scratch.yaml \
  --format md
```

## Proposed Output Shape

```markdown
# Personalized Lesson: AI Engineering Runtime Primer

## Why This Matters To Your Project

You are learning this because the adaptive syllabus engine must turn generic source material into user-specific lessons and repo tasks.

## Source Concept

AI engineering from first principles.

## Personalized Translation

Instead of studying AI abstractly, use each concept to build the system that will personalize future concepts.

## Repo Task

Create the first lesson schema and renderer.

## Evidence To Save

- generated lesson markdown
- completed task note
- ledger event
```

## Files To Add Next

```text
src/adaptive_personal_syllabus/lesson_runtime.py
src/adaptive_personal_syllabus/lesson_schema.py
data/sources/ai_engineering_from_scratch.yaml
tests/test_lesson_runtime.py
```

## CLI Integration Point

The new `lesson` command group should be added to:

```text
src/adaptive_personal_syllabus/core.py
```

Suggested structure:

```python
@cli.group()
def lesson() -> None:
    """Personalized lesson runtime commands."""

@lesson.command("next")
def lesson_next(...) -> None:
    """Generate the next personalized lesson stub."""
```

## Minimal Schema

```yaml
schema_version: "0.1"
source:
  id: ai_engineering_from_scratch
  title: AI Engineering from Scratch
  type: external_curriculum
learner_binding:
  goal: build_adaptive_personal_syllabus
  current_project: adaptive-personal-syllabus
  preferred_output: repo_task
lesson:
  title: AI Engineering Runtime Primer
  source_concept: first_principles_ai_engineering
  personalized_translation: >
    Use the curriculum as a scaffold for building the personalization engine itself.
  repo_task: create lesson runtime schema and renderer
  evidence:
    - generated lesson markdown
    - passing test
    - ledger event
```

## Definition of Done

Milestone 0.1 is complete when this command works locally:

```bash
aps lesson next --profile ~/.adaptive-syllabus/profile.json --format md
```

and returns a personalized lesson that includes:

- source concept;
- why it matters to the learner;
- project-specific translation;
- next repo task;
- evidence to save.

## Non-Goals For 0.1

Do not build full RAG yet.
Do not build a full TUI yet.
Do not build a web app yet.
Do not integrate multiple LLM providers yet.
Do not personalize entire books yet.

The first milestone should prove the loop, not maximize features.

## Next Milestone

Milestone 0.2 should add a TUI wrapper around the same lesson runtime.

The TUI should not create a separate product path. It should expose the existing CLI/runtime primitives through a navigable interface.
