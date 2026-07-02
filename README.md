# Adaptive Personal Syllabus

[![CI](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus/actions/workflows/ci.yml/badge.svg)](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus/blob/main/LICENSE)
[![Organ VI](https://img.shields.io/badge/Organ-VI%20Koinonia-6366F1)](https://github.com/organvm-vi-koinonia)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus)
[![Python](https://img.shields.io/badge/lang-Python-informational)](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus)

**An AI-personalized education system that transforms generic curricula into context-aware, multi-artifact learning journeys spanning OS development, algorithms, DSLs, kernel engineering, UI/sound/video, and AR/VR -- generating eight parallel professional outputs per module through a "Wings" multi-artifact framework.**

---

## Table of Contents

1. [Educational Philosophy](#1-educational-philosophy)
2. [Curriculum Overview](#2-curriculum-overview)
3. [Technical Architecture](#3-technical-architecture)
4. [Installation and Setup](#4-installation-and-setup)
5. [Usage](#5-usage)
6. [Working Examples](#6-working-examples)
7. [Pedagogical Foundation](#7-pedagogical-foundation)
8. [Testing and Quality](#8-testing-and-quality)
9. [Cross-References](#9-cross-references)
10. [Contributing](#10-contributing)
11. [License and Author](#11-license-and-author)

---

## 1. Educational Philosophy

Most educational content is written for nobody in particular. Self-help books, online courses, and university syllabi present general principles under the assumption that the reader will perform the translation work themselves -- mapping abstract advice onto the concrete circumstances of their own life, career, and projects. The Adaptive Personal Syllabus rejects this assumption. Its central claim is that AI can close the personalization gap: every piece of educational content should be processed through personalization protocols that rewrite it for YOUR business, YOUR metrics, YOUR context, YOUR life.

Consider a canonical example. *Think and Grow Rich* contains 13 principles for wealth accumulation. For a reader who is a solo software engineer building a SaaS product, those principles mean something radically different than they do for a reader who is a visual artist pursuing grant funding. The Adaptive Personal Syllabus does not leave this translation to the reader. Instead, the system ingests the source material, cross-references it with the learner's declared goals, current skill levels, professional context, and personal metrics, and generates a rewritten version where every principle, exercise, and recommendation has been adapted to the learner's specific situation.

This philosophy extends beyond books. The entire curriculum -- spanning nine modules from foundational tooling through AR/VR neural-symbolic systems -- is designed to be personalized at the point of delivery. The system maintains a learner profile that evolves as modules are completed, ensuring that later modules build on the demonstrated competencies and identified gaps from earlier ones. The result is not a static syllabus but a living document that adapts its depth, pacing, and emphasis to the individual.

### The Wings Framework

Personalization is only half the design. The other half is the recognition that learning produces professional artifacts, not just knowledge. Every module in the Adaptive Personal Syllabus generates eight parallel outputs through the Wings framework:

| Wing | Artifact Type | Purpose |
|------|--------------|---------|
| Academic | Research paper or formal summary | Demonstrates scholarly engagement with the material |
| SOP | Standard operating procedure | Translates knowledge into repeatable institutional process |
| Business | Pitch deck or business case | Frames the module's content as commercial value proposition |
| Social | Social media post or thread | Distills insights for public-facing distribution |
| Community | Discussion prompt or forum post | Seeds collaborative engagement around the module's themes |
| Wiki | Encyclopedia-style entry | Creates reference documentation for knowledge bases |
| Web/Blog | Long-form blog post | Publishes the learning journey as narrative content |
| Grants | Grant proposal section | Positions the module's output as fundable work |

This eight-wing structure means that completing a single module on, say, kernel subsystems and observability simultaneously produces a research summary suitable for a conference submission, an SOP for the learner's engineering team, a blog post for their public portfolio, and a grant proposal section for their next funding application. The Wings framework treats education not as consumption but as production -- every hour of learning generates reusable professional capital.

---

## 2. Curriculum Overview

The curriculum is structured as nine modules plus a capstone, progressing from foundational tooling through increasingly sophisticated systems engineering. Each module builds on the previous one, and each generates a full set of Wings artifacts.

### Module Progression

| Module | Title | Focus | Key Deliverables |
|--------|-------|-------|-----------------|
| 0 | ChainBlockARK & Foundational Wings | Self-documenting ledger of prompts, commits, builds, and AI interactions | Provenance chain, initial Wings templates |
| 1 | Repo & AI Workflow Setup | Git, metadata conventions, VS Code + Copilot configuration | Configured development environment, CI/CD scaffolding |
| 2 | Algorithms & Recursive Intuition | Recursion, data structures, visual explainers | Algorithm visualizations, complexity analysis documents |
| 3 | DSL & Meta-Circular Interpreter | Lisp-style interpreter, tiny DSL for OS configuration | Working interpreter, DSL specification document |
| 4 | Bootloader & Core Kernel Loop | 16KB assembly bootloader, QEMU-tested minimal kernel | Bootable kernel image, hardware abstraction layer |
| 5 | Kernel Subsystems & Observability | Memory management, filesystem, I/O drivers, eBPF tracing | Observable kernel with tracing infrastructure |
| 6 | UI, Sound & Video Ecosystem | 2D web terminal with audio, React Native mobile demo | Multi-modal interface prototype |
| 7 | AR/VR & Neural-Symbolic Extension | AR overlay, VR scene, SMT checks, AI code generation | Spatial computing prototype, formal verification proofs |
| Capstone | Unified Microkernel + Multi-Modal Platform | Integration of all modules into a single coherent system | End-to-end platform demonstration |

### Progressive Complexity

The modules are ordered by dependency and conceptual difficulty. Modules 0-1 establish the learner's working environment and provenance infrastructure. Modules 2-3 build computational thinking skills (recursion, data structures, language design) that are prerequisites for the systems work in Modules 4-5. Modules 6-7 extend the kernel foundation into user-facing domains (interfaces, spatial computing, formal methods). The capstone integrates all prior work into a unified microkernel with multi-modal capabilities.

This progression is deliberate. A learner who completes Module 4 (bootloader and kernel) has already internalized recursive thinking (Module 2) and language design (Module 3), which means they approach kernel code not as rote implementation but as an exercise in designing layered abstractions. The curriculum teaches systems thinking through systems building.

---

## 3. Technical Architecture

### Module Structure

Each module is organized as a self-contained directory with a consistent internal layout:

```
modules/
  module-00-chainblockark/
    README.md                  # Module overview, objectives, prerequisites
    syllabus.yaml              # Machine-readable module specification
    personalization/
      profile-schema.json      # Learner profile fields relevant to this module
      adaptation-rules.py      # Context-aware rewriting logic
    wings/
      academic.md.j2           # Jinja2 template for Academic wing
      sop.md.j2                # Jinja2 template for SOP wing
      business.md.j2           # Jinja2 template for Business wing
      social.md.j2             # Jinja2 template for Social wing
      community.md.j2          # Jinja2 template for Community wing
      wiki.md.j2               # Jinja2 template for Wiki wing
      web-blog.md.j2           # Jinja2 template for Web/Blog wing
      grants.md.j2             # Jinja2 template for Grants wing
    exercises/
      ...                      # Hands-on tasks, starter code, test harnesses
    readings/
      reading-list.yaml        # Curated sources with annotations
    tie-ins/
      arts-humanities.md       # Cross-disciplinary connections
      math-sciences.md
      philosophy.md
  module-01-repo-ai-workflow/
    ...
```

### Wings Generation Pipeline

The Wings pipeline transforms raw module content into eight personalized artifacts. The process has four stages:

1. **Profile Loading** -- The learner's profile (goals, skill levels, professional context, metrics) is loaded from `~/.adaptive-syllabus/profile.yaml`. This profile is updated after each module completion based on demonstrated competencies and self-assessment.

2. **Content Ingestion** -- The module's `syllabus.yaml`, exercise results, and reading annotations are parsed into a structured content graph. External sources (books, papers, courses) referenced in the module are processed through personalization protocols.

3. **Template Rendering** -- Each wing's Jinja2 template is rendered with the combined context of the learner profile and the content graph. The adaptation rules in `adaptation-rules.py` control how generic content is rewritten for the learner's specific situation.

4. **Output Assembly** -- Rendered artifacts are written to `output/<module>/<wing>/` with metadata headers that track provenance (which sources were used, which profile fields influenced the adaptation, timestamps).

```
profile.yaml ──┐
                ├──→ [Adaptation Engine] ──→ 8 Wing Artifacts
syllabus.yaml ─┘         │
                    adaptation-rules.py
```

### Personalization Engine

The personalization engine is the core innovation. It operates on a simple principle: every statement in the source material that references a generic subject ("your business," "your team," "the reader") is rewritten to reference the learner's specific context. This is not summarization or paraphrasing -- it is contextual rewriting that preserves the source material's reasoning while grounding it in the learner's reality.

The engine uses a combination of template-based rewriting (for structural elements like exercises and checklists) and LLM-assisted rewriting (for narrative content like explanations and case studies). The learner profile provides the grounding context, and the adaptation rules define which profile fields are relevant to each content type.

---

## 4. Installation and Setup

### Prerequisites

- Python 3.11 or later
- Git 2.40+

### Quick Start

```bash
# Clone the repository
git clone https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus.git
cd adaptive-personal-syllabus

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Verify installation
syllabus version
```

---

## 5. Usage

The project exports two main CLI entrypoints: `syllabus` (with `aps` as an alias) and `aps-data-export`. All local data is stored by default in `~/.adaptive-syllabus/`.

### Key Commands

**1. Generate a Learning Path**
Generate a personalized syllabus by providing organ codes and a difficulty level:
```bash
syllabus generate --organs I,II,V --level beginner --name "Jane Doe" --format md
```
*Flags:*
- `--organs`: Comma-separated organ codes (e.g., I,II,V). Required.
- `--level`: `beginner`, `intermediate`, or `advanced`. Default is `beginner`.
- `--name`: Learner display name. Default is `Learner`.
- `--format`: Output format (`text`, `json`, `md`). Default is `text`.

**2. Learner Profile Management**
Initialize a local JSON profile for the learner. The profile is saved locally and recorded in the immutable ledger.
```bash
syllabus profile init \
  --name "Jane Doe" \
  --organs I,V \
  --level beginner \
  --goals "build recursive systems" \
  --context '{"industry":"developer tools"}' \
  --output ~/.adaptive-syllabus/profile.json
```
*Flags:*
- `--name`: Learner display name. Required.
- `--organs`: Comma-separated organ codes. Default is `I`.
- `--level`: `beginner`, `intermediate`, or `advanced`. Default is `beginner`.
- `--goals`: Comma-separated goals. Default is empty.
- `--context`: JSON object with contextual metadata. Default is `{}`.
- `--completed`: Comma-separated completed module IDs. Default is empty.
- `--output`: Path to write the profile. Default is `~/.adaptive-syllabus/profile.json`.
- `--db-path`: Path to the local database. Default is `~/.adaptive-syllabus/koinonia.db`.

**3. Corpus Ingestion & Statistics**
Ingest an arbitrary directory of documents to form a deduplicated local corpus, and view stats:
```bash
syllabus corpus ingest --root ./docs --snapshot v1-docs
syllabus corpus stats --snapshot-name v1-docs
```
*Flags for `ingest`:*
- `--root`: Root directory to ingest. Required.
- `--snapshot`: Snapshot name for this ingest run. Required.
- `--db-path`: Path to the local database.

*Flags for `stats`:*
- `--snapshot-id`: Optional snapshot id selector.
- `--snapshot-name`: Optional snapshot name selector. Default is `latest`.
- `--db-path`: Path to the local database.

**4. Syllabus Planning**
Generate a profile-aware plan using a local profile and ingested corpus evidence:
```bash
syllabus plan generate --profile ~/.adaptive-syllabus/profile.json --format md
```
*Flags:*
- `--profile`: Path to the learner profile JSON. Required.
- `--format`: Output format (`text`, `json`, `md`). Default is `text`.
- `--seed-dir`: Directory for seed data.
- `--db-path`: Path to the local database.

**5. Docs Audit & Execution Plans**
Audit all documentation files against usage suggestions/milestones, exporting a detailed report or generating an execution plan:
```bash
syllabus docs audit --root ./docs --snapshot v1 --format md --write-md audit-report.md
syllabus docs execute-milestone --root ./docs --milestone "core-api" --limit 10 --format json
```
*Flags for `audit`:*
- `--root`: Root docs directory to audit. Required.
- `--snapshot`: Snapshot name. Default is `docs-audit`.
- `--format`: Output format (`json`, `md`). Default is `json`.
- `--write-json`: Optional output path for JSON report.
- `--write-md`: Optional output path for Markdown report.
- `--db-path`: Path to the local database.

*Flags for `execute-milestone`:*
- `--root`: Root docs directory to audit. Required.
- `--snapshot`: Snapshot name. Default is `docs-audit`.
- `--milestone`: Milestone ID to execute. Defaults to report-recommended start milestone.
- `--limit`: Maximum prioritized items. Default is `20`.
- `--format`: Output format (`json`, `md`). Default is `json`.
- `--write-json`: Optional output path for JSON execution plan.
- `--write-md`: Optional output path for Markdown execution plan.
- `--db-path`: Path to the local database.

**6. Ledger Verification**
Verify the integrity of the append-only SQLite ledger:
```bash
syllabus ledger verify
```
*Flags:*
- `--db-path`: Path to the local database.

**7. Chamber Hooks**
Run registered chamber hooks (e.g., `input_ritual`):
```bash
syllabus chamber run --hook input_ritual --dry-run
```
*Flags:*
- `--hook`: Hook name to execute. Required.
- `--dry-run` / `--execute`: Whether to do a dry-run. Default is `--dry-run`.
- `--context`: JSON object context for the hook. Default is `{}`.
- `--plan-id`: Optional DB plan ID.
- `--db-path`: Path to the local database.

**8. Data Export**
Export sample learning paths to JSON (generates beginner, intermediate, and advanced examples into `data/sample-learning-paths.json`):
```bash
aps-data-export
```

**9. Version**
Check the installed version:
```bash
syllabus version
```

---

## 7. Pedagogical Foundation

### Interdisciplinary Tie-Ins

Each module includes explicit connections to arts and humanities, mathematics and sciences, and philosophy. These tie-ins are not decorative -- they are structural elements of the curriculum designed to develop the integrative thinking that distinguishes senior practitioners from specialists.

| Module | Arts & Humanities | Math/Sciences | Philosophy |
|--------|------------------|---------------|------------|
| 0 | Archival science, provenance in art authentication | Hash functions, Merkle trees | Epistemology of record-keeping |
| 1 | Typographic conventions in technical writing | Information theory (Shannon entropy) | Philosophy of tools (Heidegger's readiness-to-hand) |
| 2 | Algorithmic art (Vera Molnar, Georg Nees) | Combinatorics, graph theory | Recursion and self-reference (Hofstadter) |
| 3 | Concrete poetry, constrained writing (OuLiPo) | Lambda calculus, Church encoding | Philosophy of language (Wittgenstein) |
| 4 | Hardware aesthetics, circuit board art | Boolean algebra, finite automata | Materialism and abstraction |
| 5 | Systems art (Hans Haacke, Jack Burnham) | Queuing theory, memory hierarchy | Observation and measurement (quantum mechanics parallels) |
| 6 | Interface design history (Xerox PARC to present) | Signal processing, Fourier transforms | Phenomenology of perception (Merleau-Ponty) |
| 7 | Spatial installation art, immersive theatre | Formal logic, satisfiability | Extended mind thesis (Clark and Chalmers) |

### Core Reading List

The curriculum draws from foundational texts across computer science, systems engineering, and philosophy of computation:

- **Abelson & Sussman** -- *Structure and Interpretation of Computer Programs* (SICP). The backbone of Modules 2-3. Recursive thinking, abstraction barriers, metalinguistic abstraction.
- **Chacon & Straub** -- *Pro Git*. Module 1 reference for version control internals and workflow design.
- **Queinnec** -- *Lisp in Small Pieces*. Module 3 deep reference for interpreter and compiler construction from first principles.
- **Arpaci-Dusseau & Arpaci-Dusseau** -- *Operating Systems: Three Easy Pieces*. Modules 4-5 primary text for virtualization, concurrency, and persistence.
- **Kleppmann** -- *Designing Data-Intensive Applications*. Cross-cutting reference for distributed systems thinking, used in Modules 5 and Capstone.
- **Klein et al.** -- *seL4: Formal Verification of an OS Kernel* (SOSP 2009). Module 7 and Capstone reference for formal methods applied to kernel verification.
- **Hofstadter** -- *Godel, Escher, Bach*. Philosophical backbone for recursive intuition (Module 2) and meta-circular reasoning (Module 3).
- **Sussman & Wisdom** -- *Structure and Interpretation of Classical Mechanics*. Advanced cross-reference for Module 7's neural-symbolic extensions.

### Pedagogical Methodology

The Adaptive Personal Syllabus applies three established pedagogical principles:

1. **Constructionism** (Papert, 1991) -- Learning happens through building artifacts, not consuming content. Every module produces tangible outputs (code, documents, prototypes), and the Wings framework ensures those outputs serve professional purposes beyond the learning context.

2. **Spaced Repetition with Contextual Variation** -- Concepts introduced in early modules reappear in later modules in new contexts. Recursion (Module 2) reappears in kernel interrupt handling (Module 5) and formal verification (Module 7). Each reappearance deepens understanding by providing a new application domain.

3. **Reflective Practice** (Schon, 1983) -- The ChainBlockARK provenance chain and the Wings writing process require the learner to reflect on what they have learned and articulate it in multiple registers (academic, business, social, etc.). This multi-register articulation forces deeper processing than single-format assessment.

---

## 8. Testing and Quality

### Test Suite

```bash
# Run the full test suite
pytest tests/ -v

# Run tests for a specific module
pytest tests/test_module_00.py -v

# Run personalization engine tests
pytest tests/test_personalization/ -v

# Check code quality
ruff check src/
mypy src/ --strict
```

### Quality Gates

Each module's Wings artifacts are validated against quality criteria before being marked complete:

- **Completeness** -- All eight Wings generated with non-zero content
- **Personalization Depth** -- At least 60% of generic references replaced with learner-specific context
- **Provenance** -- All source materials cited, adaptation rules logged in metadata
- **Cross-Reference Integrity** -- Internal links between Wings and module content resolve correctly

### Continuous Integration

The CI pipeline (`.github/workflows/ci.yml`) runs on every push:

1. Lint and type-check (`ruff`, `mypy`)
2. Unit tests (`pytest`)
3. Template rendering validation (all Jinja2 templates render without errors)
4. Schema validation (`profile.yaml` and `syllabus.yaml` against JSON schemas)

---

## 9. Cross-References

### ORGAN VI Repositories

The Adaptive Personal Syllabus is part of ORGAN VI (Community), which provides infrastructure for collaborative learning and knowledge sharing:

| Repository | Description | Relationship |
|-----------|-------------|-------------|
| [salon-archive](https://github.com/organvm-vi-koinonia/salon-archive) | Archive infrastructure for intellectual salons: transcription pipeline, topic taxonomy, and session metadata | Salon discussions feed into curriculum refinement; Module exercises can be adapted for salon workshops |
| [reading-group-curriculum](https://github.com/organvm-vi-koinonia/reading-group-curriculum) | Structured reading group curricula spanning eight-organ domains: 8-12 week programs with curated reading lists | Reading lists inform module readings; reading group formats inform Community Wing templates |

### Cross-Organ Dependencies

The Adaptive Personal Syllabus draws from and contributes to multiple organs:

- **ORGAN I (Theory)** -- The recursive intuition module (Module 2) references frameworks from `recursive-engine--generative-entity`. The meta-circular interpreter module (Module 3) shares conceptual foundations with `organon-noumenon--ontogenetic-morphe`.
- **ORGAN II (Art)** -- Arts and humanities tie-ins reference generative art systems from ORGAN II. The UI/Sound/Video module (Module 6) draws on audio engineering patterns explored in ORGAN II repositories.
- **ORGAN IV (Orchestration)** -- The ChainBlockARK provenance model (Module 0) mirrors the governance and audit patterns defined in ORGAN IV's orchestration system.
- **ORGAN V (Public Process)** -- The Web/Blog Wing artifact format aligns with ORGAN V's essay publishing infrastructure, enabling direct contribution to the public process.
- **ORGAN VII (Marketing)** -- The Social Wing artifact format is designed for compatibility with ORGAN VII's POSSE distribution pipeline.

### System Context

This repository is part of an eight-organ creative-institutional system coordinating 81 repositories across 8 GitHub organizations. The system is documented at [organvm-corpvs-testamentvm](https://github.com/meta-organvm/organvm-corpvs-testamentvm) and governed by a single source of truth registry (`registry-v2.json`).

---

## 10. Contributing

Contributions are welcome, particularly in these areas:

- **New module exercises** -- Hands-on tasks that reinforce module concepts. Include starter code and test harnesses.
- **Wings template improvements** -- Better Jinja2 templates that produce more natural and useful artifacts across the eight wing types.
- **Reading list expansions** -- Additional foundational texts with annotations explaining their relevance to specific modules.
- **Interdisciplinary tie-ins** -- New connections between technical modules and arts, humanities, sciences, or philosophy.
- **Personalization rules** -- More sophisticated adaptation logic for specific professional contexts (academia, startups, enterprise, creative practice).

### Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-exercise-module-03`)
3. Write tests for new functionality
4. Ensure all quality gates pass (`pytest`, `ruff`, `mypy`)
5. Submit a pull request with a description of what the contribution adds and which module(s) it affects

Please review the community guidelines in [organvm-vi-koinonia/.github](https://github.com/organvm-vi-koinonia/.github) before contributing.

---

## 11. License and Author

**License:** MIT

**Author:** [@4444j99](https://github.com/4444J99)

**Part of the Eight-Organ System:**

| Organ | Domain | GitHub Organization |
|-------|--------|-------------------|
| I | Theory | [organvm-i-theoria](https://github.com/organvm-i-theoria) |
| II | Art | [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) |
| III | Commerce | [organvm-iii-ergon](https://github.com/organvm-iii-ergon) |
| IV | Orchestration | [organvm-iv-taxis](https://github.com/organvm-iv-taxis) |
| V | Public Process | [organvm-v-logos](https://github.com/organvm-v-logos) |
| **VI** | **Community** | **[organvm-vi-koinonia](https://github.com/organvm-vi-koinonia)** |
| VII | Marketing | [organvm-vii-kerygma](https://github.com/organvm-vii-kerygma) |
| Meta | Governance | [meta-organvm](https://github.com/meta-organvm) |

---

*Adaptive Personal Syllabus is part of ORGAN VI (Koinonia) -- the community organ of the eight-organ creative-institutional system.*

<!-- SYSTEM-NAV-START -->

---

<sub>[Portfolio](https://4444j99.github.io/portfolio/) · [System Directory](https://4444j99.github.io/portfolio/directory/) · [ORGAN VI · Koinonia](https://organvm-vi-koinonia.github.io/) · Part of the <a href="https://4444j99.github.io/portfolio/directory/">ORGANVM eight-organ system</a></sub>

<!-- SYSTEM-NAV-END -->
