from typing import List, Optional
from pydantic import BaseModel, Field


class KNR(BaseModel):
    KNR: str = Field(..., description="Car KNR")

    NAME: Optional[str] = Field(..., description="Car NAME")
    ID: Optional[int] = Field(..., description="Car ID")
    STATUS: Optional[int] = Field(..., description="Car STATUS")
    UNIT: Optional[str] = Field(..., description="Car UNIT")
    VALUE_ID: Optional[str] = Field(..., description="Car VALUE_ID")
    VALUE: Optional[str] = Field(..., description="Car VALUE")
    DATA: Optional[str] = Field(..., description="Car DATA")

    timestamp: Optional[str] = Field(
        "", description="Date of the prediction in iso format"
    )

    predicted_fail: Optional[str] = Field("", description="Predicted fail")
    predicted_fail_code: Optional[int] = Field(-1, description="Predicted fail code")
    indicated_test: Optional[str] = Field("", description="Indicated test")
    real_fail: Optional[str] = Field("", description="Real fail")
    real_fail_code: Optional[int] = Field(-1, description="Real fail code")

    class Config:
        json_schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "Assoalho Externo",
                "indicated_test": "Teste de pintura",
                "real_fail": "Assoalho Externo",
            }
        }
