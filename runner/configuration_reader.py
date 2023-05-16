import yaml
from utils.logger import logger
from models.pipline.pipeline_config import PipelineConfig
from models.pipline.input_cfg import InputConfig
from models.pipline.output_cfg import OutputConfig
from models.pipline.transformations.transformation_cfg import TransformationConfig
from models.connector_cfg import ConnectorConfig
from models.metro_cfg import MetroConfig
from models.pipline.transformations.container_transformation_cfg import ContainerTransformationConfig
from models.pipline.transformations.http_transformation_cfg import HttpTransformationCfg
from models.pipline.transformations.sql_transformation_cfg import SQLTransformationCfg
from models.pipline.transformations.pickle_transformation_cfg import PickleTransformationCfg
from models.infrastructure_runner.pipeline_infra_runner_cfg_builder import from_config_dict as pipeline_infra_convert

CONFIGURATION_FILE = './runner/cfg/metro.yaml'

def read_configuration_file()->MetroConfig:
    '''Read Metro yml configuration file
       Returns:
        class object MetroConfig'''
    metro_config = {}
    with open(CONFIGURATION_FILE, 'r', encoding='utf-8') as stream:
        try:
            configuration_data=yaml.safe_load(stream)
            metro_config = MetroConfig.from_config_dict(configuration_data)
        except yaml.YAMLError as err:
            logger.error(err)

    return metro_config
