from fastapi import FastAPI

from app.api.main import api_router

app = FastAPI(
    title="EventHub API",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Простой чек для мониторинга, что контейнер жив"""
    return {"status": "ok"}
