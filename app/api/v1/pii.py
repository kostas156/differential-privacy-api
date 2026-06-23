from fastapi import APIRouter, HTTPException
from app.models.pii_models import PIIMaskRequest, PIIMaskResponse
from app.core.pii.masker import masker

router = APIRouter(prefix="/pii", tags=["PII Masking"])


@router.post("/mask", response_model=PIIMaskResponse)
def mask_pii(request: PIIMaskRequest) -> PIIMaskResponse:
    """
    Detect and mask PII entities in unstructured text.
    Replaces names, emails, phone numbers and other PII with placeholder tokens.
    """

    try:
        result = masker.mask(
            text=request.text,
            entities=request.entities,
        )
        return PIIMaskResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))