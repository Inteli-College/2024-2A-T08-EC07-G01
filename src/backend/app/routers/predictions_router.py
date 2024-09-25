from fastapi import APIRouter, HTTPException
from typing import List
from app.models.model import Model, ModelUpdate
from app.services.models_service import ModelServiceSingleton

router = APIRouter(prefix="/api/predictions", tags=["Predictions"])

@router.get(
        "/get_predictions",
        response_description="List of all predictions",
        )
async def get_all_predictions():
    predictions = ModelServiceSingleton.get_instance().get_all_predictions()
    return predictions

@router.get(
        "/get_prediction/{knr}",
        response_description="Get information about a specific prediction",
        )
async def get_prediction(knr: str):
    prediction = ModelServiceSingleton.get_instance().get_prediction(knr)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction

@router.post(
    "/predict",
    response_description="Predict the failure codes for a given KNR",
)
async def predict_fail_codes(knr: str):
    predictions = ModelServiceSingleton.get_instance().predict_orquestrator(knr)
    return predictions