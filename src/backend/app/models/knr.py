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

    predicted_fails: Optional[List[str]] = Field([""], description="Predicted fail")
    predicted_fail_codes: Optional[List[int]] = Field(
        [-1], description="Predicted fail code"
    )
    indicated_test: Optional[List[str]] = Field([""], description="Indicated test")
    real_fails: Optional[List[str]] = Field([""], description="Real fail")
    real_fail_codes: Optional[List[int]] = Field([-1], description="Real fail code")

    class Config:
        json_schema_extra = {
            "example": {
                "KNR": "KNR123",
                "NAME": "Model A",
                "ID": 123,
                "STATUS": 1,
                "UNIT": "Unit123",
                "VALUE_ID": "Value001",
                "VALUE": "200",
                "DATA": "2024-01-01T12:00:00",
                "timestamp": "2024-09-10T15:30:00",
                "predicted_fails": ["fail1", "fail2"],
                "predicted_fail_code": [1, 2],
                "indicated_test": ["test1", "test2"],
                "real_fail": ["fail1", "fail2"],
                "real_fail_code": [1, 2],
            }
        }


class KNRUpdate(BaseModel):
    KNR: Optional[str] = Field(None, description="Car KNR")

    NAME: Optional[str] = Field(None, description="Car NAME")
    ID: Optional[int] = Field(None, description="Car ID")
    STATUS: Optional[int] = Field(None, description="Car STATUS")
    UNIT: Optional[str] = Field(None, description="Car UNIT")
    VALUE_ID: Optional[str] = Field(None, description="Car VALUE_ID")
    VALUE: Optional[str] = Field(None, description="Car VALUE")
    DATA: Optional[str] = Field(None, description="Car DATA")

    timestamp: Optional[str] = Field(
        None, description="Date of the prediction in iso format"
    )

    predicted_fails: Optional[List[str]] = Field("", description="Predicted fail")
    predicted_fail_codes: Optional[List[int]] = Field(
        -1, description="Predicted fail code"
    )
    indicated_tests: Optional[List[str]] = Field("", description="Indicated test")
    real_fails: Optional[List[str]] = Field("", description="Real fail")
    real_fail_codes: Optional[List[int]] = Field(-1, description="Real fail code")

    class Config:
        json_schema_extra = {"example": {"real_fail": ["fail1", "fail2"]}}
