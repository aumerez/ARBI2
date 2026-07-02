from fastapi import FastAPI

app = FastAPI(
    title="Arbi Backend",
    description="FastAPI backend for the Arbi Platform",
    version="0.1.0",
)


@app.get("/health")
async def health():
    return {"status": "ok"}
