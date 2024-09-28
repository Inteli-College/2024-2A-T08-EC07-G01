from app.models.train import Train
from app.repositories.models_repo import ModelRepository
from app.pipeline.orchestrator import Orchestrator
import json

class TrainService:
    def __init__(self, model_repo: ModelRepository):
        self.model_repo = model_repo

    def train_model(self, train: Train) -> str:
        # DONE: call the train function
        # TODO: Store the train data inside the database using the model_repo
        # return self.model_repo.create_model(train)

        with open("./pipeline/pipeline_classificacao.json", "r") as file:
            pipeline_config = json.load(file)

       #prediction_steps = pipeline_config.get("prediction_steps", [])
        training_steps = pipeline_config.get("training_steps", [])

        steps = training_steps

        orchestrator = Orchestrator(
        pipeline_steps=steps,
        initial_df=train.data,
        mongo_uri="mongodb://localhost:27017",
        db_name="cross_the_line",
    )
        orchestrator.run_dynamic_pipeline()

        return 1


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