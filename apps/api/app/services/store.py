from __future__ import annotations

from collections.abc import Iterator
from datetime import timezone, datetime
from uuid import uuid4

from app.schemas.run import CreateRunRequest, RunRecord


class InMemoryStore:
    def __init__(self) -> None:
        self.runs: dict[str, RunRecord] = {}

    def create_run(self, payload: CreateRunRequest) -> RunRecord:
        run_id = f"run_{uuid4().hex[:8]}"
        now = datetime.now(tz=timezone.utc)
        record = RunRecord(
            runId=run_id,
            status="queued",
            createdAt=now,
            updatedAt=now,
            platform=payload.platform,
            bundleId=payload.bundleId,
            limits=payload.limits,
            metrics={"nodes": 0, "edges": 0},
        )
        self.runs[run_id] = record
        return record

    def get_run(self, run_id: str) -> RunRecord | None:
        return self.runs.get(run_id)

    def all_runs(self) -> Iterator[RunRecord]:
        return iter(self.runs.values())


store = InMemoryStore()
