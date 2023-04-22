from typing import List
from models.connector_cfg import ConnectorConfig
from models.pipeline_config import PipelineConfig

class MetroConfig:
    '''Class represent the metro configuration'''
    def __init__(self, name, connectors: List[ConnectorConfig], pipelines: List[PipelineConfig]):
        self.name = name
        self.connectors = connectors
        self.pipelines = pipelines

    def as_dict(self):
        '''Function for convert config to dict'''
        return {
            'name': self.name,
            'connectors': [connector.as_dict() for connector in  self.connectors],
            'pipelines': [pipeline.as_dict() for pipeline in  self.pipelines]
        }
