from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas.graph import GraphAction, GraphEdge, GraphNode, GraphResponse, Point
from app.services.store import store

router = APIRouter(tags=["graph"])


@router.get("/runs/{run_id}/graph", response_model=GraphResponse)
def get_graph(run_id: str) -> GraphResponse:
    run = store.get_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")

    nodes = [
        GraphNode(
            id="state_001",
            stateHash="bootstrap",
            title="Entry",
            screenshotUrl="/placeholder/state_001.png",
            depth=0,
            isTerminal=False,
        )
    ]
    edges = [
        GraphEdge(
            id="tr_001",
            from_="state_001",
            to="state_001",
            action=GraphAction(type="tap", targetElementKey="seed", tapPoint=Point(x=100, y=100), label="Seed"),
            outcome="success",
            durationMs=120,
        )
    ]
    return GraphResponse(runId=run_id, nodes=nodes, edges=edges)
