from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest

from app.api.v1.routes_risk import router as risk_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()
app = FastAPI(title=settings.app_name)
app.include_router(risk_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics() -> str:
    return generate_latest().decode("utf-8")
