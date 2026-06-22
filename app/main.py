from fastapi import FastAPI
from app.config import settings
from app.api.v1.router import router

app = FastAPI(
	title = settings.app_name,
	version=settings.app_version,
	description="Privacy-first data filter: PII masking and differential privacy."
)

app.include_router(router)

@app.get("/health", tags=["Health"])
def health_check():
	"""Liveness probe -used by Docker and K8s."""
	return {
		"status": "ok",
		"version": settings.app_version
	}