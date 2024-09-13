from fastapi import APIRouter, HTTPException
from typing import List
from app.models.knr import KNR, KNRUpdate
from app.services.knr_service import KNRServiceSingleton
from app.utils.fail_labeler import label_knr
from app.services.predict_service import predict_pipeline
from datetime import datetime

router = APIRouter(prefix="/api/knr", tags=["KNR"])


@router.get(
    "/",
    response_model=List[KNR],
    response_description="List of all KNRs",
)
async def get_all_knr():
    knrs = KNRServiceSingleton.get_instance().get_all_knrs()
    return knrs


@router.get(
    "/{knr_id}",
    response_model=KNR,
    response_description="Get a single KNR info",
)
async def get_knr(knr_id: str):
    knr = KNRServiceSingleton.get_instance().get_knr(knr_id)
    if knr is None:
        raise HTTPException(status_code=404, detail="KNR not found")
    return knr


@router.post(
    "/",
    response_model=KNR,
    response_description="Add a new KNR to process",
)
async def add_knr(knr: KNR):
    knr_id = KNRServiceSingleton.get_instance().create_knr(knr)

    result = predict_pipeline(knr)
    knr.predicted_fail_codes = result
    knr = label_knr(knr)
    knr.timestamp = str(datetime.now())

    KNRServiceSingleton.get_instance().update_knr(knr_id, knr)

    return KNRServiceSingleton.get_instance().get_knr(knr_id)


@router.put(
    "/{knr_id}",
    response_model=KNR,
    response_description="Update a KNR",
)
async def update_knr(knr_id: str, knr: KNRUpdate):
    existing_knr = KNRServiceSingleton.get_instance().get_knr(knr_id)

    if not existing_knr:
        raise HTTPException(status_code=404, detail="KNR not found")

    KNRServiceSingleton.get_instance().update_knr(knr_id, knr)

    updated_knr = KNRServiceSingleton.get_instance().get_knr(knr_id)
    return updated_knr


@router.delete(
    "/{knr_id}",
    response_model=dict,
    response_description="Delete a KNR",
)
async def delete_knr(knr_id: str):
    if not KNRServiceSingleton.get_instance().delete_knr(knr_id):
        raise HTTPException(status_code=404, detail="KNR not found")
    return {"message": "KNR deleted successfully"}
