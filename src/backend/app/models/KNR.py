import enum
from typing import List, Optional
from pydantic import BaseModel, Field

class fails(enum.Enum):
    PORTA_DIANTEIRA_NA_PINTURA = "PORTA DIANTEIRA NA PINTURA"

class tests(enum.Enum):
    TESTE_DE_PINTURA = "Teste de pintura"

class KNR(BaseModel):
    knr: str = Field(..., description="Car KNR")

    predicted_date: str = Field(..., description="Date of the prediction in iso format")

    predicted_fail: Optional[enum.Enum] = Field(..., description="Predicted fail")
    indicated_test: Optional[enum.Enum] = Field(..., description="Indicated test")
    real_fail: Optional[enum.Enum] = Field(..., description="Real fail")

    class Config:
        schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "PORTA DIANTEIRA NA PINTURA",
                "indicated_test": "Teste de pintura",
                "real_fail": "PORTA DIANTEIRA NA PINTURA",
            }
        }


class RegisterKNR(BaseModel):
    knr: str = Field(..., description="Car KNR")

    predicted_fail: fails = Field(..., description="Predicted fail")
    indicated_test: tests = Field(..., description="Indicated test")

    class Config:
        json_schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "PORTA DIANTEIRA NA PINTURA",
                "indicated_test": "Teste de pintura",
                "real_fail": "PORTA DIANTEIRA NA PINTURA",
            }
        }


class UpdateKNR(BaseModel):
    knr: Optional[str] = Field(None, description="Car KNR")

    predicted_date: Optional[str] = Field(
        None, description="Date of the prediction in iso format"
    )

    predicted_fail: Optional[enum.Enum] = Field(None, description="Predicted fail")
    indicated_test: Optional[enum.Enum] = Field(None, description="Indicated test")
    real_fail: Optional[enum.Enum] = Field(None, description="Real fail")

    class Config:
        schema_extra = {
            "example": {
                "knr": "KNR123",
                "date": "2021-01-01T00:00:00",
                "predicted_fail": "PORTA DIANTEIRA NA PINTURA",
                "indicated_test": "Teste de pintura",
                "real_fail": "PORTA DIANTEIRA NA PINTURA",
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
                        "predicted_fail": "PORTA DIANTEIRA NA PINTURA",
                        "indicated_test": "Teste de pintura",
                        "real_fail": "PORTA DIANTEIRA NA PINTURA",
                    }
                ]
            }
        }
