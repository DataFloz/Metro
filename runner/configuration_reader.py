import yaml
from models.pipeline_config import PipelineConfig
from models.input_cfg import InputConfig
from models.output_cfg import OutputConfig
from models.transformation_cfg import TransformationConfig
from models.connector_cfg import ConnectorConfig
from models.metro_cfg import MetroConfig
from models.container_transformation_cfg import ContainerTransformationConfig
from models.http_transformation_cfg import HttpTransformationCfg

CONFIGURATION_FILE = './runner/cfg/metro.yaml'

def read_configuration_file()->MetroConfig:
    metro_config = {}
    with open(CONFIGURATION_FILE, 'r', encoding='utf-8') as stream:
        try:
            configuration_data=yaml.safe_load(stream)
            pipelines_config = \
                [convert_pipeline_dict_to_models(pipeline_yml)
                    for pipeline_yml in configuration_data['pipelines']]
            connectors_config = \
                [convert_connector_dict_to_models(connector_yml)
                    for connector_yml in configuration_data['connectors']]

            metro_config = MetroConfig(configuration_data["name"], connectors_config,
                                        pipelines_config)

        except yaml.YAMLError as err:
            print(err)

    return metro_config

def convert_pipeline_transformation_dict_to_models(pipeline) -> TransformationConfig:
    transfomation_type = pipeline["transformation"]["type"]
    print(f'transformationType {transfomation_type}')
    if transfomation_type == 'http':
        transformation = HttpTransformationCfg(pipeline["transformation"]["http_url"],
                                               pipeline["transformation"]["headers"],
                                               pipeline["transformation"]["params"])
    elif transfomation_type == 'container':
        transformation = ContainerTransformationConfig(
                                            pipeline["transformation"]["container-image"])
    else:
        raise Exception(f'transformation type {transfomation_type} is not supported yet!')

    return transformation

def convert_pipeline_dict_to_models(pipeline):
    pipeline_config = PipelineConfig(name=pipeline["name"],
                        input=InputConfig(pipeline["input"]["topic"]),
                        output=OutputConfig(pipeline["output"]["topic"]),
                        transformation=convert_pipeline_transformation_dict_to_models(pipeline))

    return pipeline_config


def convert_connector_dict_to_models(connector):
    connector_config = ConnectorConfig(name=connector["name"],
                                       type=connector["type"],
                                       brokers=connector["brokers"],
                                       group_id=connector["group_id"])

    return connector_config
