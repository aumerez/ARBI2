# Arbi Backend

FastAPI backend for the Arbi Platform.

## Run

```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000
```

Then check health:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```
