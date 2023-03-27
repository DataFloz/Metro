from models.connector_cfg import ConnectorConfig
from models.pipeline_config import PipelineConfig

class MetroConfig:
    def __init__(self, name, connectors: list[ConnectorConfig], pipelines: list[PipelineConfig]):
        self.name = name
        self.connectors = connectors
        self.pipelines = pipelines

    def as_dict(self):
        return {
            'name': self.name,
            'connectors': [connector.as_dict() for connector in  self.connectors],
            'pipelines': [pipeline.as_dict() for pipeline in  self.pipelines]
        }