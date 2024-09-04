from dotenv import dotenv_values

from app.db.mongodb import MongoDB

config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI", "mongodb://localhost:27017")
DATABASE_NAME = config.get("DATABASE_NAME", "cross_the_line")
KNR_COLLECTION_NAME = config.get("COLLECTION_NAME", "knrs")
MODELS_COLLECTION_NAME = config.get("MODELS_COLLECTION_NAME", "models")


database: MongoDB

def init_db():
    global database
    database = MongoDB(DATABASE_URI, DATABASE_NAME)
    return database
