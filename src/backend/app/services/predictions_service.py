from app.models.predictions import Prediction, PredictionUpdate
from app.models.knr import KNR
from app.repositories.predictions_repo import PredictionsRepository
from typing import Optional, List
from app.utils.predict import mock_prediction


# TODO: Completar predict Service
class PredictionService:
    def __init__(self, predict_repo: PredictionsRepository):
        self.predict_repo = predict_repo

    def get_all_predictions(self) -> List[Prediction]:
        return self.predict_repo.get_all_predictions()

    def get_prediction(self, knr: str) -> Optional[Prediction]:
        return self.predict_repo.get_prediction(knr)

    def predict(self, knr: KNR) -> Prediction:
        prediction = mock_prediction()
        return self.predict_repo.create_prediction(prediction)

    def update_prediction(self, knr: str, prediction: PredictionUpdate) -> bool:
        return self.predict_repo.update_prediction(knr, prediction)

    def delete_prediction(self, knr: str) -> bool:
        return self.predict_repo.delete_prediction(knr)

    def fail_codes_prediction(self) -> dict:
        return self.predict_repo.fail_codes_prediction()

    def total_fails(self) -> dict:
        return self.predict_repo.total_fails_prediction()


class PredictionsServiceSingleton:
    _instance: Optional[PredictionService] = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def initialize(cls, predict_repo: PredictionsRepository):
        if cls._instance is None:
            cls._instance = PredictionService(predict_repo)

    @classmethod
    def get_instance(cls) -> PredictionService:
        if cls._instance is None:
            raise Exception(
                "ModelServiceSingleton is not initialized. Call initialize() first."
            )

        return cls._instance
