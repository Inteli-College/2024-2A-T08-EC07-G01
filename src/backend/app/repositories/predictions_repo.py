from typing import Optional

from app.db.mongodb import MongoDB
from app.models.predictions import Prediction, PredictionUpdate

class PredictionsRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection = db.get_collection("Predictions")

    def get_all_models(self) -> list[Prediction]:
        documents = self.collection.find()
        return [Prediction(**document) for document in documents]

    def create_model(self, prediction_info: Prediction) -> str:
        self.collection.insert_one(prediction_info.model_dump(by_alias=True))
        return str(prediction_info.KNR)

    def get_model(self, knr_id: str) -> Optional[Prediction]:
        document = self.collection.find_one({"KNR": knr_id})
        return Prediction(**document) if document else None

    def update_model(self, knr_id: str, model_info: PredictionUpdate) -> bool:
        result = self.collection.update_one(
            {"KNR": knr_id},
            {"$set": model_info.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0

    def delete_model(self, knr_id: str) -> bool:
        result = self.collection.delete_one({"KNR": knr_id})
        return result.deleted_count > 0