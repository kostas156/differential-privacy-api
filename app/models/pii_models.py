from pydantic import BaseModel, Field
from typing import List, Optional

class PIIMaskRequest(BaseModel):
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=10_000, 
        description="The unstructured text to scan for PIIs.",
        example="My name is John Doe and my email is john@example.com"
    )
    entities: Optional[List[str]] = Field(
        default=None,
        description="PII entity types to detect. If None, detects all supported types.",
        examples=[["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"]],
    )

class DetectedEntity(BaseModel):
    entity_type: str = Field(
        description="The type of PII detected, e.g. 'EMAIL_ADDRESS'."
    )
    start: int = Field(
        description="Start character index in the original text."
    )
    end: int = Field(
        description="End character index in the original text."
    )
    score: float = Field(
        description="Confidence score of the detection, between 0.0 and 1.0."
    )

class PIIMaskResponse(BaseModel):
    masked_text: str = Field(
        description="The original text with PII replaced by placeholders."
    )
    detections: List[DetectedEntity] = Field(
        description="List of all detected PII entities."
    )
    detection_count: int = Field(
        description="Total number of detected PII entities."
    )