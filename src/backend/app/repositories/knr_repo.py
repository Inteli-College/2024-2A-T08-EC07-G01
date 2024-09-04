from typing import Optional
from bson import ObjectId

from app.db.mongodb import MongoDB
from app.models.knr import KNR


class KNRRepository:
    def __init__(self, db: MongoDB):
        self.collection = db.get_collection("knrs")

    def get_all_knrs(self) -> list[KNR]:
        documents = self.collection.find()
        return [KNR(**document) for document in documents]

    def create_knr(self, knr: KNR):
        result = self.collection.insert_one(knr.model_dump(by_alias=True))
        return str(result.inserted_id)

    def get_knr(self, knr_id: str) -> Optional[KNR]:
        document = self.collection.find_one({"_id": ObjectId(knr_id)})
        return KNR(**document) if document else None

    def update_knr(self, knr_id: str, knr: KNR) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(knr_id)},
            {"$set": knr.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0

    def delete_knr(self, knr_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(knr_id)})
        return result.deleted_count > 0
