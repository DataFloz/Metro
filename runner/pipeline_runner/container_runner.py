import docker
from docker.errors import NotFound
from pipeline_runner.abstract_runner import AbstractRunner
from models.connector_cfg import ConnectorConfig
from models.pipline.pipeline_config import PipelineConfig


class ContainerRunner(AbstractRunner):
    def __init__(self):
        super().__init__()
        self.client = docker.from_env()


    def rollout(self, pipeline_configuration: PipelineConfig, kafka_connector: ConnectorConfig):
        # create a container with environment variables
        self.client = docker.from_env()
        envs_dict = pipeline_configuration.as_dict()
        envs_dict.update(kafka_connector.as_dict())
        self.client.images.build(path="./pipeline",
                            tag=f"{pipeline_configuration.name}:latest")

        try:
            self.client.containers.get(pipeline_configuration.name).stop()
            self.client.containers.prune()
        except NotFound:
            print("no such container")

        self.client.containers.run(image=f"{pipeline_configuration.name}:latest",
                            environment=envs_dict,
                            network='metro_devcontainer_default',
                            name=pipeline_configuration.name,
                            volumes={'./runner/cfg/': {'bind': '/mnt/configs/', 'mode': 'ro'}},
                            detach=True)
