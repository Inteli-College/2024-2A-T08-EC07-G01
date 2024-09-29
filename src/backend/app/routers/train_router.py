from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from app.services.train_service import TrainServiceSingleton
from app.models.train import Train, ModelComparison

router = APIRouter(prefix="/api/train", tags=["Training"])

@router.post(
    "/",
    response_description="Train a model",
    response_model=Train
)
async def train_model(
    df_falhas: UploadFile = File(...),
):
    df_falhas_content = await df_falhas.read()
    df_falhas = pd.read_csv(BytesIO(df_falhas_content))
    df_resultados = pd.read_csv("/app/app/pipeline/resultados.csv")

    try:
        # Use the train service to train the model and return the model metadata
        model_metadata = TrainServiceSingleton.get_instance().train_model(df_resultados, df_falhas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model training failed: {str(e)}")

    return {"message": f"Model '{model_metadata['model_name']}' trained successfully."}

@router.post(
    "/retrain",
    response_description="Retrain the model",
    response_model=ModelComparison
)
async def retrain_model(
    df_falhas: UploadFile = File(...),
):
    df_falhas_content = await df_falhas.read()
    df_falhas = pd.read_csv(BytesIO(df_falhas_content))
    df_resultados = pd.read_csv("/app/app/pipeline/resultados.csv")

    try:
        # Use the train service to retrain the model and get the comparison
        comparison = TrainServiceSingleton.get_instance().retrain_model(df_resultados, df_falhas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model retraining failed: {str(e)}")

    return comparison

@router.post(
    "/select_model",
    response_description="Select a model to use"
)
async def select_model(
    model_name: str
):
    try:
        TrainServiceSingleton.get_instance().select_model(model_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to select model: {str(e)}")
    return {"message": f"Model '{model_name}' is now in use."}