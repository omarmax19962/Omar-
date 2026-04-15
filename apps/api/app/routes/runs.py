from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas.run import CreateRunRequest, CreateRunResponse, RunStatusResponse
from app.services.store import store

router = APIRouter(tags=["runs"])


@router.post("/runs", response_model=CreateRunResponse)
def create_run(payload: CreateRunRequest) -> CreateRunResponse:
    run = store.create_run(payload)
    return CreateRunResponse(runId=run.runId, status="queued")


@router.get("/runs/{run_id}", response_model=RunStatusResponse)
def get_run(run_id: str) -> RunStatusResponse:
    run = store.get_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")

    return RunStatusResponse(
        runId=run.runId,
        status=run.status,
        createdAt=run.createdAt,
        updatedAt=run.updatedAt,
        metrics=run.metrics,
    )
