import gridfs
from pymongo import MongoClient
import importlib.util
import sys
import os
import tempfile
import datetime as datetime

class Orquestrator:
    def __init__(self, pipeline_config, mongo_uri, db_name):
        self.pipeline_config = pipeline_config
        self.logs = []
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def log(self, message, error=False):
        log_type = "ERROR" if error else "INFO"
        self.logs.append(f"[{log_type}] {message}")
        if error:
            self.save_logs()

    def fetch_script_from_gridfs(self, file_id):
        try:
            grid_out = self.fs.get(file_id)
            script_content = grid_out.read()
            self.log(f"Script with ID {file_id} successfully fetched from GridFS.")
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

    def execute_step(self, step_name, module, func_name, **kwargs):
        try:
            func = getattr(module, func_name)
            self.log(f"Executing {step_name}...")
            result = func(**kwargs)  # Pass any needed arguments
            self.log(f"{step_name} completed successfully.")
            return result
        except AttributeError as e:
            self.log(f"Function {func_name} not found in {module.__name__}: {e}", error=True)
            raise
        except Exception as e:
            self.log(f"Error during {step_name}: {e}", error=True)
            raise

    def run_dynamic_pipeline(self):
        for step in self.pipeline_config:
            module_name = step["module_name"]
            file_id = step["file_id"]  # Fetch the file ID from GridFS
            func_name = step["function"]
            kwargs = step.get("kwargs", {})

            # Fetch the script from GridFS
            script_content = self.fetch_script_from_gridfs(file_id)

            # Load the module from the script content
            module = self.load_module_from_file(module_name, script_content)

            # Execute the function from the loaded module
            self.execute_step(step["name"], module, func_name, **kwargs)

    def save_logs(self):
        timestamp = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
        with open(f"logs_{timestamp}.txt", "a") as f:
            for log in self.logs:
                f.write(log + "\n")
        self.logs.clear()

# Example pipeline configuration
pipeline_config = [
    {"name": "Extracting Data", "module_name": "extract_module", "file_id": "some_gridfs_id_1", "function": "extract_data"},
    {"name": "Transforming Data", "module_name": "transform_module", "file_id": "some_gridfs_id_2", "function": "transform_data"},
    {"name": "Loading Data", "module_name": "load_module", "file_id": "some_gridfs_id_3", "function": "load_data", "kwargs": {"param1": "value"}}
]

# Create orchestrator with MongoDB connection and run the pipeline
orchestrator = Orquestrator(pipeline_config, mongo_uri="mongodb://localhost:27017", db_name="your_database")
orchestrator.run_dynamic_pipeline()
