from datetime import datetime
from app.models.predictions import Prediction, PredictionUpdate
from app.models.knr import KNR
from app.repositories.predictions_repo import PredictionsRepository
from app.repositories.knr_repo import KNRRepository
from typing import Optional, List
from app.utils.predict import mock_prediction
from collections import Counter


# TODO: Completar predict Service
class PredictionService:
    def __init__(self, predict_repo: PredictionsRepository, knr_repo: KNRRepository):
        self.predict_repo = predict_repo
        self.knr_repo = knr_repo

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

    def get_fail_code_count_by_month(self, year, fail_code: int):
        predicted_fail_code_count = {}
        real_fail_code_count = {}

        for month in range(1, 13):
            knr_list = self.knr_repo.get_knr_by_month(month, year)

            predictions = self.predict_repo.get_predictions_by_knrs(knr_list, fail_code)

            predicted_count = 0
            real_count = 0

            for prediction in predictions:
                predicted_count += prediction["predicted"].count(fail_code)
                real_count += prediction["real"].count(fail_code)

            month_name = datetime(year, month, 1).strftime("%B").lower()
            predicted_fail_code_count[month_name] = predicted_count
            real_fail_code_count[month_name] = real_count

        return {
            "predicted_fail_code_count": predicted_fail_code_count,
            "real_fail_code_count": real_fail_code_count,
        }


class PredictionsServiceSingleton:
    _instance: Optional[PredictionService] = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def initialize(cls, predict_repo: PredictionsRepository, knr_repo: KNRRepository):
        if cls._instance is None:
            cls._instance = PredictionService(predict_repo, knr_repo)

    @classmethod
    def get_instance(cls) -> PredictionService:
        if cls._instance is None:
            raise Exception(
                "ModelServiceSingleton is not initialized. Call initialize() first."
            )

        return cls._instance
