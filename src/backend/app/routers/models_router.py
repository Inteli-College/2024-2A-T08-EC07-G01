from fastapi import APIRouter, HTTPException
from typing import List
from app.models.model import Model, ModelUpdate
from app.services.models_service import ModelServiceSingleton

router = APIRouter(prefix="/api/models", tags=["Models"])


@router.get(
    "/",
    response_model=List[Model],
    response_description="List of all trained models",
)
async def get_all_models():
    models = ModelServiceSingleton.get_instance().get_all_models()
    return models


@router.get(
    "/{model_name}",
    response_model=Model,
    response_description="Get information about a specific model",
)
async def get_model(model_name: str):
    model = ModelServiceSingleton.get_instance().get_model(model_name)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model


@router.post(
    "/",
    response_model=Model,
    response_description="Add a new model to the database",
)
async def add_model(model: Model):
    model_name = ModelServiceSingleton.get_instance().create_model(model)

    return ModelServiceSingleton.get_instance().get_model(model_name)


@router.put(
    "/{model_name}",
    response_model=Model,
    response_description="Update a model's information",
)
async def update_model(model_name: str, model: ModelUpdate):
    existing_model = ModelServiceSingleton.get_instance().get_model(model_name)
    if not existing_model:
        raise HTTPException(status_code=404, detail="Model not found")

    ModelServiceSingleton.get_instance().update_model(model_name, model)

    updated_model = ModelServiceSingleton.get_instance().get_model(model_name)
    return updated_model


@router.delete(
    "/{model_name}",
    response_model=dict,
    response_description="Delete a model",
)
async def delete_model(model_name: str):
    if not ModelServiceSingleton.get_instance().delete_model(model_name):
        raise HTTPException(status_code=404, detail="Model not found")
    return {"message": "Model deleted successfully"}

# Roteadores referentes ao orquestrador

@router.post(
    "/predict",
    response_description="Predict the failure codes for a given KNR",
)
async def predict_fail_codes(knr: str):
    predictions = ModelServiceSingleton.get_instance().predict_orquestrator(knr)
    return predictions