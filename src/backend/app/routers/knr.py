from fastapi import APIRouter, Request
from app.models.KNR import KNR, KNRCollection, RegisterKNR

router = APIRouter(
    prefix="/api/knr",
)


@router.get(
    "/",
    response_model=KNRCollection,
    response_description="List of all models",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    tags=["KNR"],
)
async def get_all_models(request: Request):
    knrs = KNRCollection(
        knrs=await request.app.state.knr_collection.find().to_list(100)
    )
    print(knrs)
    print("00000000000000000000000")
    return knrs


@router.get(
    "/{knr}",
    response_model=KNR,
    response_description="Get a single model",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    tags=["KNR"],
)
async def get_model(request: Request, knr: str):
    knr = await request.app.state.knr_collection.find_one({"knr": knr})
    print(knr)
    return KNR(**knr)


@router.post(
    "/",
    response_model=KNRCollection,
    response_description="Add a new model",
    tags=["KNR"],
)
async def add_model(request: Request, knr: RegisterKNR):
    await request.app.state.knr_collection.insert_one(knr.model_dump())

    # retorna o model
    return KNRCollection(
        knrs=await request.app.state.knr_collection.find().to_list(100)
    )
