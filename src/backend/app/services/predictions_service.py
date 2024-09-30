from app.models.predictions import Prediction, PredictionUpdate
from app.models.knr import KNR
from app.models.predictions import Prediction
from app.repositories.predictions_repo import PredictionsRepository
from typing import Optional, List
from app.pipeline.orchestrator import Orchestrator
import pandas as pd
import os
import json


# TODO: Completar predict Service
class PredictionService:
    def __init__(self, predict_repo: PredictionsRepository):
        self.predict_repo = predict_repo

    def get_all_predictions(self) -> List[Prediction]:
        return self.predict_repo.get_all_predictions()

    def get_prediction(self, knr: str) -> Optional[Prediction]:
        return self.predict_repo.get_prediction(knr)

    def predict(self, knr: KNR) -> Prediction:
        df_input = pd.DataFrame([knr.dict()])

        pipeline_file_path = os.path.join(os.getcwd(), 'app', 'pipeline', 'pipeline_principal.json')
        with open(pipeline_file_path, "r") as file:
            pipeline_config = json.load(file)

        steps = pipeline_config.get("predict_steps", [])

        dataframes = {
        "df_input": df_input
        }

        orchestrator = Orchestrator(
            pipeline_steps=steps,
            dataframes=dataframes,
            mongo_uri="mongodb://db:27017",
            db_name="cross_the_line"
        )

        # Run the prediction pipeline
        orchestrator.run_dynamic_pipeline()

        # Get the prediction result
        prediction = orchestrator.dataframes.get("prediction_result")

        response = Prediction(
        KNR= knr.KNR,
        predicted_fail_codes = [prediction],
        real_fail_codes = [-1], 
        indicated_tests = [""]  
        )
        # Return the prediction
        return response

    def update_prediction(self, knr: str, prediction: PredictionUpdate) -> bool:
        return self.predict_repo.update_prediction(knr, prediction)

    def delete_prediction(self, knr: str) -> bool:
        return self.predict_repo.delete_prediction(knr)

    def fail_codes_prediction(self) -> dict:
        return self.predict_repo.fail_codes_prediction()


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
