from __future__ import annotations

from fastapi import FastAPI

from app.routes.graph import router as graph_router
from app.routes.runs import router as runs_router

app = FastAPI(title="Mobile Flow Mapper API", version="0.1.0")
app.include_router(runs_router)
app.include_router(graph_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
