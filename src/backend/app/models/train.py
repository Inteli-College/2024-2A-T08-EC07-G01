from pydantic import BaseModel, Field


class Train(BaseModel):
    data: str = Field(..., description="Dataframe")

    class Config:
        json_schema_extra = {
            "example": {
                "data": "df.csv",
            }
        }
