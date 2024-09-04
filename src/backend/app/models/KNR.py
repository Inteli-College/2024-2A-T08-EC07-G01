from typing import List, Optional
from pydantic import BaseModel, Field


class KNR(BaseModel):
    KNR: str = Field(..., description="Car KNR")
    NAME: str = Field(..., description="Car NAME")
    ID: int = Field(..., description="Car ID")
    STATUS: int = Field(..., description="Car STATUS")
    UNIT: Optional[str] = Field(..., description="Car UNIT")
    VALUE_ID: Optional[str] = Field(..., description="Car VALUE_ID")
    VALUE: Optional[str] = Field(..., description="Car VALUE")
    DATA: str = Field(..., description="Car DATA")

    timestamp: Optional[str] = Field(
        "", description="Date of the prediction in iso format"
    )

    predicted_fail: Optional[str] = Field("", description="Predicted fail")
    predicted_fail_code: Optional[int] = Field(-1, description="Predicted fail code")
    indicated_test: Optional[str] = Field("", description="Indicated test")
    real_fail: Optional[str] = Field("", description="Real fail")
    real_fail_code: Optional[int] = Field(-1, description="Real fail code")

    class Config:
        schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "Assoalho Externo",
                "indicated_test": "Teste de pintura",
                "real_fail": "Assoalho Externo",
            }
        }


class UpdateKNR(BaseModel):
    knr: Optional[str] = Field(None, description="Car KNR")

    timestamp: Optional[str] = Field(
        None, description="Date of the prediction in iso format"
    )

    predicted_fail: Optional[int] = Field(None, description="Predicted fail")
    indicated_test: Optional[int] = Field(None, description="Indicated test")
    real_fail: Optional[int] = Field(None, description="Real fail")

    class Config:
        schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "Assoalho Externo",
                "indicated_test": "Teste de pintura",
                "real_fail": "Assoalho Externo",
            }
        }


class KNRCollection(BaseModel):
    knrs: List[KNR]

    class Config:
        schema_extra = {
            "example": {
                "knrs": [
                    {
                        "knr": "KNR123",
                        "date": "2021-01-01T00:00:00",
                        "predicted_fail": "Assoalho Externo",
                        "indicated_test": "Teste de pintura",
                        "real_fail": "Assoalho Externo",
                    }
                ]
            }
        }
