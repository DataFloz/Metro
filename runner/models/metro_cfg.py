from typing import List
from models.connector.connector_cfg import ConnectorConfig
from models.connector.connector_cfg_builder import from_config_dict as pipeline_connector_convert
from models.pipline.pipeline_config import PipelineConfig
from models.infrastructure_runner.pipeline_infrastructure_runner \
    import PipelineInfrastructureRunner
from models.infrastructure_runner.pipeline_infra_runner_cfg_builder \
    import from_config_dict as pipeline_infra_convert

class MetroConfig:
    '''Class represent the metro configuration'''
    def __init__(self, name, connector: ConnectorConfig, pipelines: List[PipelineConfig],
                 pipeline_infrastructure_runner: PipelineInfrastructureRunner):
        self.name = name
        self.connector = connector
        self.pipelines = pipelines
        self.pipeline_infrastructure_runner = pipeline_infrastructure_runner

    def as_dict(self):
        '''Function for convert config to dict'''
        return {
            'name': self.name,
            'connector': self.connector.as_dict(),
            'pipelines': [pipeline.as_dict() for pipeline in  self.pipelines],
            'pipeline_infrastructure_runner': self.pipeline_infrastructure_runner.as_dict()
        }

    @classmethod
    def from_config_dict(cls, metro_dict):
        '''The function responsible to convert the metro config
           Args:
           metro dict
           Returns:
           MetroConfig object'''
        pipelines_config = \
                [PipelineConfig.from_config_dict(pipeline_dict=pipeline_yml)
                    for pipeline_yml in metro_dict['pipelines']]
        connector_config = \
                pipeline_connector_convert(connector_dict=metro_dict['connector'])
        pipeline_infrastructure_runner = \
                                    pipeline_infra_convert(metro_dict['running_infrastructure'])

        metro_config = MetroConfig(metro_dict["name"], connector_config,
                                        pipelines_config, pipeline_infrastructure_runner)

        return metro_config
