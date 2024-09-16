from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Model(BaseModel):
    model_name: str = Field(..., description="Name of the trained model")
    training_date: datetime = Field(..., description="Date when the model was trained")
    gridfs_path: str = Field(
        ..., description="Path in GridFS where the model is stored"
    )

    accuracy: float = Field(..., description="Accuracy of the model")
    precision: float = Field(..., description="Precision of the model")
    recall: float = Field(..., description="Recall of the model")
    f1_score: float = Field(..., description="F1 score of the model")

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "RandomForestModel_v1",
                "training_date": "2024-09-10T12:00:00",
                "gridfs_path": "/path/to/model/in/gridfs",
                "accuracy": 0.10,
                "precision": 0.20,
                "recall": 0.30,
                "f1_score": 0.40,
            }
        }


class ModelUpdate(BaseModel):
    model_name: Optional[str] = Field(None, description="Name of the trained model")
    training_date: Optional[datetime] = Field(
        None, description="Date when the model was trained"
    )
    gridfs_path: Optional[str] = Field(
        None, description="Path in GridFS where the model is stored"
    )

    accuracy: Optional[float] = Field(None, description="Accuracy of the model")
    precision: Optional[float] = Field(None, description="Precision of the model")
    recall: Optional[float] = Field(None, description="Recall of the model")
    f1_score: Optional[float] = Field(None, description="F1 score of the model")

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "RandomForestModel_v1",
                "training_date": "2024-09-10T12:00:00",
                "gridfs_path": "/path/to/model/in/gridfs",
                "accuracy": 0.10,
                "precision": 0.20,
                "recall": 0.30,
                "f1_score": 0.40,
            }
        }
