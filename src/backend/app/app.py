from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
import motor.motor_asyncio

from .routers import knr

config = dotenv_values(".env")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    client = motor.motor_asyncio.AsyncIOMotorClient(config["DATABASE_URI"])
    db = client.get_database("cross_the_line")
    app.state.knr_collection = db.get_collection("knr")
    print("Connected to the MongoDB database!")

    yield

    app.state.mongodb_client.close()
    print("Disconnected to the MongoDB database!")


app = FastAPI(lifespan=app_lifespan)

app.include_router(knr.router)

@app.get("/")
async def read_root():
    return {"message": "crossing the line!"}


