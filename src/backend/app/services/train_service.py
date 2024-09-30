import json
import os
import pandas as pd
from app.models.model import Model
from app.repositories.models_repo import ModelRepository
from app.pipeline.orchestrator import Orchestrator
import datetime

class TrainService:
    def __init__(self, model_repo: ModelRepository):
        self.model_repo = model_repo

    def train_model(self, df_resultados: pd.DataFrame, df_falhas: pd.DataFrame) -> dict:
        # Load pipeline configuration
        pipeline_file_path = os.path.join(os.getcwd(), 'app', 'pipeline', 'pipeline_principal.json')
        print("Absolute Path to JSON file:", pipeline_file_path)

        with open(pipeline_file_path, "r") as file:
            pipeline_config = json.load(file)

        steps = pipeline_config.get("prediction_steps", []) + pipeline_config.get("training_steps", [])

        # Initialize dataframes for the pipeline
        dataframes = {
            "df_resultados": df_resultados,
            "df_falhas": df_falhas,
        }

        # Create an orchestrator to run the pipeline
        orchestrator = Orchestrator(
            pipeline_steps=steps,
            dataframes=dataframes,
            mongo_uri="mongodb://db:27017",
            db_name="cross_the_line",
        )

        # Run the pipeline and get the model metadata
        model_metadata = orchestrator.run_dynamic_pipeline()

        # Debug print to verify model metadata
        print(f"[DEBUG] Orchestrator returned model metadata: {model_metadata}")

        # Create a new Model object to store in the database
        new_model = Model(
            model_name=model_metadata.get("model_name"),
            type_model=model_metadata.get("type_model"),
            gridfs_path="path/to/model/in/gridfs",  # Replace with actual GridFS path
            recipe_path="path/to/recipe/in/gridfs",  # Replace with actual GridFS path
            accuracy=model_metadata["metrics"].get("accuracy", 0.0),
            precision=model_metadata["metrics"].get("precision", 0.0),  # Calculate or provide this value
            recall=model_metadata["metrics"].get("recall", 0.0),
            f1_score=model_metadata["metrics"].get("f1", 0.0),
            last_used=None,  # You can set this to `datetime.datetime.utcnow()` if needed
            using=False  # Adjust based on your logic
        )

        # Save the model in the repository
        try:
            self.model_repo.create_model(new_model)
            print(f"[INFO] Model '{new_model.model_name}' saved to repository.")
        except Exception as e:
            raise RuntimeError(f"Failed to save model: {str(e)}")

        return model_metadata

    def retrain_model(self, df_resultados: pd.DataFrame, df_falhas: pd.DataFrame) -> dict:
        # Load pipeline configuration
        pipeline_file_path = os.path.join(os.getcwd(), 'app', 'pipeline', 'pipeline_principal.json')
        print("Absolute Path to JSON file:", pipeline_file_path)

        with open(pipeline_file_path, "r") as file:
            pipeline_config = json.load(file)

        steps = pipeline_config.get("prediction_steps", []) + pipeline_config.get("training_steps", [])

        # Initialize dataframes for the pipeline
        dataframes = {
            "df_resultados": df_resultados,
            "df_falhas": df_falhas,
        }

        # Create an orchestrator to run the pipeline
        orchestrator = Orchestrator(
            pipeline_steps=steps,
            dataframes=dataframes,
            mongo_uri="mongodb://db:27017",
            db_name="cross_the_line",
        )

        # Run the pipeline and get the new model metadata
        new_model_metadata = orchestrator.run_dynamic_pipeline()

        # Create a new Model object to store in the database
        new_model = Model(
            model_name=new_model_metadata.get("model_name"),
            type_model=new_model_metadata.get("type_model"),
            gridfs_path="path/to/model/in/gridfs",  # Replace with actual GridFS path
            recipe_path="path/to/recipe/in/gridfs",  # Replace with actual GridFS path
            accuracy=new_model_metadata["metrics"].get("accuracy", 0.0),
            precision=new_model_metadata["metrics"].get("precision", 0.0),
            recall=new_model_metadata["metrics"].get("recall", 0.0),
            f1_score=new_model_metadata["metrics"].get("f1_score", 0.0),
            last_used=None,
            using=False,
            created_at=datetime.datetime.utcnow()
        )

        # Save the new model in the repository
        try:
            self.model_repo.create_model(new_model)
            print(f"[INFO] New model '{new_model.model_name}' saved to repository.")
        except Exception as e:
            raise RuntimeError(f"Failed to save new model: {str(e)}")

        # Get the last model from the repository
        last_model = self.model_repo.get_latest_model()

        # Exclude the newly saved model from comparison if necessary
        if last_model and last_model.model_name != new_model.model_name:
            # Compare the new model's metrics with the last model's metrics
            comparison = self.compare_models(new_model_metadata, last_model)
        else:
            # No previous model, so new model is the first model
            comparison = {
                "message": "No previous model to compare with.",
                "new_model_metrics": new_model_metadata["metrics"]
            }

        # Return the comparison result
        return comparison

    def compare_models(self, new_model_metadata, last_model) -> dict:
        new_metrics = new_model_metadata["metrics"]
        last_metrics = {
            "accuracy": last_model.accuracy,
            "precision": last_model.precision,
            "recall": last_model.recall,
            "f1_score": last_model.f1_score
        }

        differences = {}
        for metric in new_metrics:
            new_value = new_metrics[metric]
            last_value = last_metrics.get(metric, 0.0)
            differences[metric] = new_value - last_value

        comparison = {
            "new_model_metrics": new_metrics,
            "last_model_metrics": last_metrics,
            "differences": differences
        }

        return comparison

    def select_model(self, model_name: str):
        # Set 'using' to False for all models
        self.model_repo.unset_all_using()
        # Set 'using' to True for the selected model
        self.model_repo.set_model_using(model_name)
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
