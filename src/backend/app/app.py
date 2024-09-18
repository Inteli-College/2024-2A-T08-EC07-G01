from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.mongodb import MongoDB

from app.repositories.knr_repo import KNRRepository
from app.services.knr_service import KNRServiceSingleton
from app.routers.knr_router import router as knr_router

from app.repositories.models_repo import ModelRepository
from app.services.models_service import ModelServiceSingleton
from app.routers.models_router import router as models_router

from app.routers.healthcheck_router import router as healthcheck_router
#from pymongo import MongoClient
#from pymongo.errors import ConnectionFailure

from dotenv import dotenv_values


config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI", "mongodb://localhost:27017")
DATABASE_NAME = config.get("DATABASE_NAME", "cross_the_line")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    app.state.db = MongoDB(DATABASE_URI, DATABASE_NAME)

    KNRServiceSingleton.initialize(KNRRepository(app.state.db))
    ModelServiceSingleton.initialize(ModelRepository(app.state.db))

    print("Connected to the MongoDB database!")

    yield

    app.state.db.close()
    print("Disconnected to the MongoDB database!")


app = FastAPI(lifespan=app_lifespan)

origins = [
        "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(knr_router)
app.include_router(models_router)
app.include_router(healthcheck_router)


#mongo_url = "mongodb://localhost:27017"
#timeout_ms = 1000

@app.get("/")
async def read_root():
    return {"message": "crossing the line!"}

'''
@app.get("/healthcheck/mongodb")
async def healthcheck_mongodb():
    try:
        client = MongoClient(mongo_url, serverSelectionTimeoutMS=timeout_ms)
        client.server_info()  # Apenas verifica a conectividade
        return {"status": "MongoDB is reachable", "status_code": 200}
    except ConnectionFailure as e:
        return {"status": "MongoDB is unreachable", "status_code": 500, "error": str(e)}
'''
