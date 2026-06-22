from fastapi import APIRouter, HTTPException
from app.models.dp_models import DPNoiseRequest, DPNoiseResponse
from app.core.privacy.laplace import add_laplace_noise

router = APIRouter(prefix="/dp", tags=["Differential Privacy"])

@router.post("/noise", response_model=DPNoiseResponse)
def add_noise(request: DPNoiseRequest) -> DPNoiseResponse:
    """
    Apply Laplace differential privacy noise to a list of numerical values.
    Prevents reverse engineering of individual records while preserving statistical utility.
    """
    try:
        result = add_laplace_noise(
            values=request.values,
            sensitivity=request.sensitivity,
            epsilon=request.epsilon,
        )
        return DPNoiseResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))