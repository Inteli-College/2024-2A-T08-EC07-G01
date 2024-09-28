from fastapi import APIRouter, HTTPException
import base64
from typing import List
from app.models.train import Train
from app.services.train_service import TrainServiceSingleton

router = APIRouter(prefix="/api/train", tags=["Training"])

@router.post(
    "/",
    response_description="Train a model",
)
async def train_model(train: Train):
    TrainServiceSingleton.get_instance().train_model(train)
    
    return {"message": "Model trained successfully"}