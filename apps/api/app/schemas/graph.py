from __future__ import annotations

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int


class GraphAction(BaseModel):
    type: str
    targetElementKey: str | None = None
    tapPoint: Point | None = None
    label: str | None = None


class GraphEdge(BaseModel):
    id: str
    from_: str
    to: str
    action: GraphAction
    outcome: str
    durationMs: int


class GraphNode(BaseModel):
    id: str
    stateHash: str
    title: str
    screenshotUrl: str
    depth: int
    isTerminal: bool


class GraphResponse(BaseModel):
    runId: str
    nodes: list[GraphNode]
    edges: list[GraphEdge]
