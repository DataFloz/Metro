import json
import docker
from models.pipeline_config import PipelineConfig

def run_pipeline(pipeline_configuration: PipelineConfig):
    client = docker.from_env()
    client.images.build(path="../pipeline",
                        tag=f"{pipeline_configuration.name}:latest")

    client.containers.run(image=f"{pipeline_configuration.name}:latest",
                          environment=json.dumps(pipeline_configuration.__dict__,
                                                 indent=4,
                                                 default=lambda x: x.__dict__),
                          detach=True)
