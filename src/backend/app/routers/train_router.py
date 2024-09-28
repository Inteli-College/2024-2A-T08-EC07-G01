from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from app.services.train_service import TrainServiceSingleton

router = APIRouter(prefix="/api/train", tags=["Training"])

@router.post(
    "/",
    response_description="Train a model",
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
