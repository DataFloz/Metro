import yaml
from models.pipeline_config import PipelineConfig
from models.input_cfg import InputConfig
from models.output_cfg import OutputConfig
from models.transformation_cfg import TransformationConfig
from models.connector_cfg import ConnectorConfig
from models.metro_cfg import MetroConfig

CONFIGURATION_FILE = './cfg/metro.yaml'

def read_configuration_file()->MetroConfig:
    metro_config = {}
    with open(CONFIGURATION_FILE, 'r') as stream:
        try:
            configuration_data=yaml.safe_load(stream)
            pipelines_config = \
                [convert_pipeline_dict_to_models(pipeline_yml)
                    for pipeline_yml in configuration_data['pipelines']]
            connectors_config = \
                [convert_connector_dict_to_models(connector_yml)
                    for connector_yml in configuration_data['connectors']]
          
            metro_config = MetroConfig(configuration_data["name"], connectors_config, pipelines_config)
            
        except yaml.YAMLError as e:
            print(e)

    return metro_config


def convert_pipeline_dict_to_models(pipeline):
    pipeline_config = PipelineConfig(name=pipeline["name"],
                                     input=InputConfig(pipeline["input"]["topic"]),
                                     output=OutputConfig(pipeline["output"]["topic"]),
                                     transformation=TransformationConfig(pipeline["transformation"]["container-image"]))

    return pipeline_config


def convert_connector_dict_to_models(connector):
    connector_config = ConnectorConfig(name=connector["name"],
                                     brokers=connector["brokers"],
                                     group_id=connector["group_id"])

    return connector_config
