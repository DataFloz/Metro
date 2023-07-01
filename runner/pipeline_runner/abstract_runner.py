from models.connector.connector_cfg import ConnectorConfig
from models.pipline.pipeline_config import PipelineConfig

class AbstractRunner:
    '''Abstract class for the pipelines infrastructure runner'''
    def __init__(self):
        pass

    def rollout(self, pipeline_configuration: PipelineConfig, connector: ConnectorConfig):
        ''' Abstract function for rollout the pipelines '''
