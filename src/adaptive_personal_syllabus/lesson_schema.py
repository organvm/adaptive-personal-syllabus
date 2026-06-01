"""Schema models for the personalized lesson runtime."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class LessonSource:
    """External or internal source material used to generate a lesson."""

    source_id: str
    title: str
    source_type: str = "external_curriculum"
    url: str | None = None
    concepts: list[str] = field(default_factory=list)


@dataclass
class LessonEvidence:
    """Evidence targets proving that a personalized lesson was acted on."""

    items: list[str] = field(default_factory=list)


@dataclass
class PersonalizedLesson:
    """A single project-bound lesson generated for one learner profile."""

    schema_version: str
    lesson_id: str
    title: str
    learner_name: str
    source: LessonSource
    source_concept: str
    why_this_matters: str
    personalized_translation: str
    repo_task: str
    evidence: LessonEvidence
    next_command: str | None = None
    context: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a stable JSON-serializable representation."""
        return asdict(self)
