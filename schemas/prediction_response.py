from typing import Dict
from pydantic import BaseModel, Field


class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="Predicted insurance premium category (Low, Medium, High)",
        json_schema_extra={"example": "High"}
    )
    confidence: float = Field(
        ...,
        description="Confidence score for the predicted category",
        json_schema_extra={"example": 0.84}
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all target classes",
        json_schema_extra={"example": {"Low": 0.05, "Medium": 0.11, "High": 0.84}}
    )