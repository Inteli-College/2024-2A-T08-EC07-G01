from typing import Optional, List
from app.db.mongodb import MongoDB
from app.models.predictions import Prediction, PredictionUpdate


class PredictionsRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection = db.get_collection("predictions")

    def get_all_predictions(self) -> List[Prediction]:
        documents = self.collection.find()
        return [Prediction(**document) for document in documents]

    def create_prediction(self, prediction_info: Prediction) -> str:
        self.collection.insert_one(prediction_info.model_dump(by_alias=True))
        return prediction_info

    def get_prediction(self, knr_id: str) -> Optional[Prediction]:
        document = self.collection.find_one({"KNR": knr_id})
        return Prediction(**document) if document else None

    def update_prediction(self, knr_id: str, prediction_info: PredictionUpdate) -> bool:
        result = self.collection.update_one(
            {"KNR": knr_id},
            {"$set": prediction_info.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0

    def delete_prediction(self, knr_id: str) -> bool:
        result = self.collection.delete_one({"KNR": knr_id})
        return result.deleted_count > 0

    def fail_codes_prediction(self) -> dict:
        pipeline = [
            {"$unwind": "$predicted_fail_codes"},
            {"$group": {"_id": "$predicted_fail_codes", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
        ]
        result = self.collection.aggregate(pipeline)
        return {doc["_id"]: doc["count"] for doc in result}
