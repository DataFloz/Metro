import json
import docker
from models.pipeline_config import PipelineConfig
from models.connector_cfg import ConnectorConfig

def run_pipeline(pipeline_configuration: PipelineConfig, kafka_connector: ConnectorConfig):
    client = docker.from_env()
    envs_dict = pipeline_configuration.__dict__.update(kafka_connector.__dict__)
    client.images.build(path="../pipeline",
                        tag=f"{pipeline_configuration.name}:latest")

    client.containers.run(image=f"{pipeline_configuration.name}:latest",
                          environment=json.dumps(envs_dict,
                                                 indent=4,
                                                 default=lambda x: x.__dict__),
                          detach=True)
