from app.models.train import Train
from app.repositories.models_repo import ModelRepository
from app.pipeline.orchestrator import Orchestrator
import json
import base64
import pandas as pd
from io import StringIO

class TrainService:
    def __init__(self, model_repo: ModelRepository):
        self.model_repo = model_repo

    def train_model(self, train: Train) -> str:
        # Decode base64 content to CSV strings
        df_resultados_content = base64.b64decode(train.df_resultados).decode('utf-8')
        df_falhas_content = base64.b64decode(train.df_falhas).decode('utf-8')

        # Convert content to DataFrames
        df_resultados = pd.read_csv(StringIO(df_resultados_content))
        df_falhas = pd.read_csv(StringIO(df_falhas_content))

        dataframes = {
        "df_resultados": df_resultados,
        "df_falhas": df_falhas,
        }

        # Load pipeline configuration
        with open("./pipeline/pipeline_classificacao.json", "r") as file:
            pipeline_config = json.load(file)

        training_steps = pipeline_config.get("training_steps", [])

        orchestrator = Orchestrator(
            pipeline_steps=training_steps,
            initial_df=dataframes,
            mongo_uri="mongodb://localhost:27017",
            db_name="cross_the_line",
        )

        orchestrator.run_dynamic_pipeline()

        # TODO 1: Store the trained model metrics in the DB and the model also. 

        # TODO 2: Return the model's metrics to make the user choose between the last model and the newest model.


        return "Training completed successfully"


class TrainServiceSingleton:
    _instance: TrainService = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def initialize(cls, model_repo: ModelRepository):
        if cls._instance is None:
            cls._instance = TrainService(model_repo)

    @classmethod
    def get_instance(cls) -> TrainService:
        if cls._instance is None:
            raise Exception(
                "ModelServiceSingleton is not initialized. Call initialize() first."
            )
        return cls._instance
