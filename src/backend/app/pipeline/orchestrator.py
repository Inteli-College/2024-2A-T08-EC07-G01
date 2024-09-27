import gridfs
from pymongo import MongoClient
import importlib.util
import os
import tempfile
import datetime as datetime
import json
import pandas as pd


class Orchestrator:
    def __init__(self, pipeline_steps, initial_df, mongo_uri, db_name):
        self.pipeline_steps = pipeline_steps
        self.initial_df = initial_df
        self.logs = []
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def log(self, message, error=False):
        log_type = "ERROR" if error else "INFO"
        self.logs.append(f"[{log_type}] {message}")
        if error:
            self.save_logs()

    def fetch_script_from_gridfs(self, file_path):
        try:
            # grid_out = self.fs.get(file_path)
            grid_out = open(file_path, "rb")
            script_content = grid_out.read()
            self.log(f"Script with ID {file_path} successfully fetched from GridFS.")
            return script_content
        except Exception as e:
            self.log(f"Error fetching script from GridFS: {e}", error=True)
            raise

    def load_module_from_file(self, module_name, script_content):
        # Write script content to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
        temp_file.write(script_content)
        temp_file.close()

        try:
            # Load the module from the temporary file path
            spec = importlib.util.spec_from_file_location(module_name, temp_file.name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.log(f"Module {module_name} successfully loaded from {temp_file.name}.")
            return module
        except Exception as e:
            self.log(f"Error loading module {module_name} from file: {e}", error=True)
            raise
        finally:
            # Clean up the temporary file after loading the module
            os.remove(temp_file.name)

    def execute_step(self, step_name, module, **kwargs):
        try:
            func_name = "execute"
            func = getattr(module, func_name)
            self.log(f"Executing '{step_name}'...")
            result = func(**kwargs)  # Pass any needed arguments
            self.log(f"'{step_name}' completed successfully.")
            return result
        except AttributeError as e:
            self.log(
                f"Function {func_name} not found in {module.__name__}: {e}", error=True
            )
            raise
        except Exception as e:
            self.log(f"Error during '{step_name}': {e}", error=True)
            raise

    def run_dynamic_pipeline(self):
        last_result = self.initial_df
        for step in self.pipeline_steps:
            module_name = step["name"]
            file_path = step["file_path"]  # Fetch the file path from GridFS
            kwargs = step.get("kwargs", {})

            # Fetch the script from GridFS
            script_content = self.fetch_script_from_gridfs(file_path)

            # Load the module from the script content
            module = self.load_module_from_file(module_name, script_content)

            kwargs.update({"df": last_result})

            # Execute the function from the loaded module
            last_result = self.execute_step(step["name"], module, **kwargs)

        print(f"Pipeline completed successfully. Last result: {last_result}")

    def save_logs(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"./pipeline/logs/logs_{timestamp}.txt", "a") as f:
            for log in self.logs:
                f.write(log + "\n")

        self.db.logs.insert_one({"timestamp": timestamp, "logs": self.logs})
        self.logs.clear()


if __name__ == "__main__":
    # Correctly load JSON configuration
    with open("./pipeline/pipeline_classificacao.json", "r") as file:
        pipeline_config = json.load(file)
    
    # Access the appropriate key based on your JSON structure
    # Assuming you want to access "prediction_steps" and "training_steps"
    prediction_steps = pipeline_config.get("prediction_steps", [])
    training_steps = pipeline_config.get("training_steps", [])
    
    # Combine steps if necessary, or handle them separately
    # For example, if Orchestrator expects a single list of steps:
    steps = prediction_steps + training_steps
    
    # Load the initial DataFrame
    initial_df = pd.read_csv("./pipeline/initial.csv")  # Corrected path if needed
    
    print("Pipeline steps:", steps)
    print("Initial DataFrame shape:", initial_df.shape)
    
    # Initialize and run the orchestrator
    orchestrator = Orchestrator(
        pipeline_steps=steps,
        initial_df=initial_df,
        mongo_uri="mongodb://localhost:27017",
        db_name="cross_the_line",
    )
    orchestrator.run_dynamic_pipeline()