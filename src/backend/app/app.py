from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.mongodb import MongoDB
from app.repositories.knr_repo import KNRRepository
from app.routers.knr_router import router as knr_router
from app.services.knr_service import KNRServiceSingleton

from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI", "mongodb://localhost:27017")
DATABASE_NAME = config.get("DATABASE_NAME", "cross_the_line")
KNR_COLLECTION_NAME = config.get("COLLECTION_NAME", "knrs")
MODELS_COLLECTION_NAME = config.get("MODELS_COLLECTION_NAME", "models")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    KNRServiceSingleton.initiate(KNRRepository(MongoDB(DATABASE_URI, DATABASE_NAME)))
    print("Connected to the MongoDB database!")

    yield

    app.state.db.close()
    print("Disconnected to the MongoDB database!")


app = FastAPI(lifespan=app_lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(knr_router)


@app.get("/")
async def read_root():
    return {"message": "crossing the line!"}
