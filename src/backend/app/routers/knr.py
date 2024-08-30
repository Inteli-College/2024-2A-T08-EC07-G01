from fastapi import APIRouter, Request
from app.models.KNR import KNRCollection, KNR
from app.services.model_service import mocked_predict_pipeline 
from app.utils.fail_labeler import label_knr
from datetime import datetime

router = APIRouter(
    prefix="/api/knr",
)


@router.get(
    "/",
    response_model=KNRCollection,
    response_description="List of all knrs",
    tags=["KNR"],
)
async def get_all_knrs(request: Request):
    knrs = knrs = await request.app.state.knr_collection.find().to_list(100)
    knrs = KNRCollection(knrs=knrs)
    return knrs


@router.get(
    "/{knr}",
    response_model=KNR | dict,
    response_description="Get a single knr info",
    tags=["KNR"],
)
async def get_knr(request: Request, knr: str):
    knr = await request.app.state.knr_collection.find_one({"knr": knr})

    if knr is None:
        return {"message": "KNR not found"}

    knr = KNR(**knr)

    return knr


@router.post(
    "/",
    response_model=KNR,
    response_description="Add a new knr to process",
    tags=["KNR"],
)
async def add_knr(request: Request, knr: KNR):
    await request.app.state.knr_collection.insert_one(knr.model_dump())

    result = mocked_predict_pipeline(knr)

    knr.predicted_fail_code = result

    knr = label_knr(knr)

    knr.timestamp = str(datetime.now())

    await request.app.state.knr_collection.update_one(
        {"knr": knr.knr}, {"$set": knr.model_dump()}
    )

    return await request.app.state.knr_collection.find_one({"knr": knr.knr})


@router.put(
    "/{knr_id}",
    response_model=KNR,
    response_description="Update a knr",
    tags=["KNR"],
)
async def update_knr(request: Request, knr_id: str, knr: KNR):
    stored_knr = await request.app.state.knr_collection.find_one({"knr": knr_id})

    if stored_knr is None:
        return {"message": "KNR not found"}

    updated_data = knr.model_dump(exclude_unset=True)

    for key, value in stored_knr.items():
        if key in updated_data:
            stored_knr[key] = updated_data[key]

    stored_knr = KNR(**stored_knr)

    stored_knr = label_knr(stored_knr)

    await request.app.state.knr_collection.update_one(
        {"knr": knr_id}, {"$set": stored_knr.model_dump()}
    )

    return await request.app.state.knr_collection.find_one({"knr": knr.knr})


@router.delete(
    "/{knr}",
    response_model=dict,
    response_description="Delete a knr",
    tags=["KNR"],
)
async def delete_knr(request: Request, knr: str):
    await request.app.state.knr_collection.delete_one({"knr": knr})

    return {"message": "KNR deleted successfully"}
