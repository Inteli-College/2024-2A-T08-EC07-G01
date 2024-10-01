from typing import Optional

from app.db.mongodb import MongoDB
from app.models.model import Model, ModelUpdate


class ModelRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection = db.get_collection("models")

    def get_all_models(self) -> list[Model]:
        documents = self.collection.find()
        return [Model(**document) for document in documents]

    def create_model(self, model_info: Model) -> str:
        self.collection.insert_one(model_info.model_dump(by_alias=True))
        return str(model_info.model_name)

    def get_model(self, model_name: str) -> Optional[Model]:
        document = self.collection.find_one({"model_name": model_name})
        return Model(**document) if document else None

    def update_model(self, model_name: str, model_info: ModelUpdate) -> bool:
        result = self.collection.update_one(
            {"model_name": model_name},
            {"$set": model_info.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0

    def delete_model(self, model_name: str) -> bool:
        result = self.collection.delete_one({"model_name": model_name})
        return result.deleted_count > 0

    def get_models_by_type(self, model_type: str) -> list[Model]:
        documents = self.collection.find({"type_model": model_type})
        return [Model(**document) for document in documents]

    def get_current_models(self) -> list[Model]:
        documents = self.collection.find({"using": True})
        return [Model(**document) for document in documents]
    
    def get_latest_model(self) -> Optional[Model]:
        document = self.collection.find_one(sort=[('_id', -1)])
        return Model(**document) if document else None

    def unset_all_using(self):
        self.collection.update_many({}, {'$set': {'using': False}})

    def set_model_using(self, model_name: str):
        result = self.collection.update_one({'model_name': model_name}, {'$set': {'using': True}})
        if result.matched_count == 0:
            raise ValueError(f"Model '{model_name}' not found.")
