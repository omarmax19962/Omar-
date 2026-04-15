from __future__ import annotations

import json
import time

from worker.crawler import Crawler


def main() -> None:
    crawler = Crawler()
    print("[worker] started")
    while True:
        metrics = crawler.run_once()
        print(f"[worker] heartbeat metrics={json.dumps(metrics)}")
        time.sleep(5)


if __name__ == "__main__":
    main()
