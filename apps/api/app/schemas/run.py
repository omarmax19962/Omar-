from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class Limits(BaseModel):
    maxSteps: int = Field(default=80, ge=1, le=5000)
    maxDepth: int = Field(default=5, ge=1, le=100)
    maxActionsPerState: int = Field(default=6, ge=1, le=50)
    actionTimeoutMs: int = Field(default=10000, ge=1000, le=120000)
    revisitThreshold: int = Field(default=1, ge=0, le=20)


class CreateRunRequest(BaseModel):
    platform: Literal["android", "ios"]
    bundleId: str
    limits: Limits = Field(default_factory=Limits)


class CreateRunResponse(BaseModel):
    runId: str
    status: Literal["queued"]


class RunStatusResponse(BaseModel):
    runId: str
    status: Literal["queued", "running", "completed", "failed"]
    createdAt: datetime
    updatedAt: datetime
    metrics: dict[str, int]


class RunRecord(BaseModel):
    runId: str
    status: Literal["queued", "running", "completed", "failed"]
    createdAt: datetime
    updatedAt: datetime
    platform: str
    bundleId: str
    limits: Limits
    metrics: dict[str, int]


def now_utc() -> datetime:
    return datetime.now(tz=timezone.utc)
