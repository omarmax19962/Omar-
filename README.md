# Mobile Flow Mapper (MVP Scaffold)

This repository contains an end-to-end scaffold for a **mobile app flow mapper**:

- **FastAPI backend** to create runs and serve flow graph/screen data.
- **Python worker** scaffold for Appium-based crawling.
- **React viewer** scaffold to visualize graph nodes and hotspot overlays.

## Project Layout

- `apps/api` — FastAPI API service
- `apps/worker` — crawler/automation worker service
- `apps/web` — React viewer UI
- `docker-compose.yml` — local Postgres + MinIO services

## Quickstart

### 1) Start infra

```bash
docker compose up -d postgres minio
```

### 2) Start API

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3) Start Worker

```bash
cd apps/worker
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m worker.main
```

### 4) Start Web Viewer

```bash
cd apps/web
npm install
npm run dev
```

### 5) Create a run

```bash
curl -X POST http://localhost:8000/runs \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "android",
    "bundleId": "com.example.app",
    "limits": {
      "maxSteps": 80,
      "maxDepth": 5,
      "maxActionsPerState": 6,
      "actionTimeoutMs": 10000,
      "revisitThreshold": 1
    }
  }'
```

## Notes

This is an MVP scaffold meant to get you to a working baseline quickly. You can extend:

- Durable queue (Redis/Celery/RQ)
- Real Appium integration in worker
- Persistent DB models/migrations
- Auth and multi-tenant support

## External Plugin Integration

This repo reserves `external/My-Plugin` for the upstream plugin source from:

- `https://github.com/omarmax19962/My-Plugin.git`

If GitHub access is available in your environment, run:

```bash
./scripts/import_my_plugin.sh
```

Or use submodules:

```bash
git submodule update --init --recursive
```
