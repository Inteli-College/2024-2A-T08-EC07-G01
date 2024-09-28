from pydantic import BaseModel, Field

class Train(BaseModel):
    df_resultados: str = Field(..., description="Base64 encoded Results DataFrame")
    df_falhas: str = Field(..., description="Base64 encoded Failures DataFrame")

    class Config:
        schema_extra = {
            "example": {
                "df_resultados": "<base64_string_of_df_resultados.csv>",
                "df_falhas": "<base64_string_of_df_falhas.csv>",
            }
        }
