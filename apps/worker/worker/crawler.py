from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CrawlConfig:
    max_steps: int = 80
    max_depth: int = 5
    max_actions_per_state: int = 6


class Crawler:
    """Placeholder crawler service.

    Replace methods with real Appium session + BFS traversal.
    """

    def __init__(self, config: CrawlConfig | None = None) -> None:
        self.config = config or CrawlConfig()

    def run_once(self) -> dict[str, int]:
        # Placeholder metrics to validate plumbing.
        return {"nodes": 1, "edges": 1, "steps": 1}
