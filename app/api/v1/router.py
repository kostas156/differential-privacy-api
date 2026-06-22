from fastapi import APIRouter
from app.api.v1 import pii, dp

router = APIRouter(prefix="/v1")
router.include_router(pii.router)
router.include_router(dp.router)