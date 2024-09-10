from typing import Optional
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
                "KNR": "string",
                "NAME": "string",
                "ID": 0,
                "STATUS": 0,
                "UNIT": "string",
                "VALUE_ID": "string",
                "VALUE": "string",
                "DATA": "string",
                "timestamp": "string",
                "predicted_fail": "string",
                "predicted_fail_code": 0,
                "indicated_test": "string",
                "real_fail": "string",
                "real_fail_code": 0,
            }
        }

        from typing import Optional


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
                "KNR": "string",
                "NAME": "string",
                "ID": 0,
                "STATUS": 0,
                "UNIT": "string",
                "VALUE_ID": "string",
                "VALUE": "string",
                "DATA": "string",
                "timestamp": "string",
                "predicted_fail": "string",
                "predicted_fail_code": 0,
                "indicated_test": "string",
                "real_fail": "string",
                "real_fail_code": 0,
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

    predicted_fail: Optional[str] = Field(None, description="Predicted fail")
    predicted_fail_code: Optional[int] = Field(None, description="Predicted fail code")
    indicated_test: Optional[str] = Field(None, description="Indicated test")
    real_fail: Optional[str] = Field(None, description="Real fail")
    real_fail_code: Optional[int] = Field(None, description="Real fail code")

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
                "predicted_fail": "Error in X component",
                "predicted_fail_code": 42,
                "indicated_test": "Test A",
                "real_fail": "Fail in Y",
                "real_fail_code": 99,
            }
        }
