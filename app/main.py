from fastapi import FastAPI
from app.config import settings

app = FastAPI(
	title = settings.app_name,
	version=settings.app_version,
	description="Privacy-first data filter: PII masking and differential privacy."
)

@app.get("/health", tags=["Health"])
def health_check():
	"""Liveness probe -used by Docker and K8s."""
	return {
		"status": "ok",
		"version": settings.app_version
	}