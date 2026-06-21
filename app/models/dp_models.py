from pydantic import BaseModel, Field
from typing import List

class DPNoiseRequest(BaseModel):
    values: List[float] = Field(
        ...,
        min_length=1,
        max_length=10_000,
        description="The numerical values to which Laplace noise will be applied.",
        examples=[[120.5, 98.3, 150.0, 87.6]],
    )
    epsilon: float = Field(
        default=1.0,
        gt=0.0,
        le=10.0,
        description="Privacy Budget. Lower = stronger privacy, more noise. Typical reange: 0.1 to 10.0.",
        examples=[0.5]
    )
    sensitivity: float = Field(
        default=1.0,
        gt=0.0,
        description="Global sensitivity: max change a single record can cause in the query result.",
        examples=[1.0]
    )

class DPNoiseResponse(BaseModel):
    noisy_values: List[float] = Field(
        description="The input values after Laplace noise has been applied."
    )
    epsilon: float = Field(
        description="The privacy budget used for this request."
    )
    sensitivity: float = Field(
        description="The sensitivity value used for this request."
    )
    scale: float = Field(
        description="The Laplace distribution scale parameter (sensitivity / epsilon)."
    )
    privacy_budget_consumed: float = Field(
        description="Equal to epsilon - confirms the budget that has been spent."
    )