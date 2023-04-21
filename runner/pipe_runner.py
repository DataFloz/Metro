import docker
from docker.errors import NotFound
from models.pipeline_config import PipelineConfig
from models.connector_cfg import ConnectorConfig

def run_pipeline(pipeline_configuration: PipelineConfig, kafka_connector: ConnectorConfig):
    client = docker.from_env()
    envs_dict = pipeline_configuration.as_dict()
    envs_dict.update(kafka_connector.as_dict())
    client.images.build(path="./pipeline",
                        tag=f"{pipeline_configuration.name}:latest")

    try:
        client.containers.get(pipeline_configuration.name).stop()
        client.containers.prune()
    except NotFound:
        print("no such container")

    client.containers.run(image=f"{pipeline_configuration.name}:latest",
                          environment=envs_dict,
                          network='metro_devcontainer_default',
                          name=pipeline_configuration.name,
                          detach=True)
