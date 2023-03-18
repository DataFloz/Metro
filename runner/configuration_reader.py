import yaml
from models.pipeline_config import PipelineConfig
from models.input_cfg import InputConfig
from models.output_cfg import OutputConfig
from models.transformation_cfg import TransformationConfig

CONFIGURATION_FILE = './cfg/metro.yaml'

def read_configuration_file()->list[PipelineConfig]:
    pipelines_config = []
    with open(CONFIGURATION_FILE, 'r') as stream:
        try:
            configuration_data=yaml.safe_load(stream)
            pipelines_config = \
                [convert_pipeline_dict_to_models(pipeline_yml) 
                    for pipeline_yml in configuration_data['pipelines']]
        except yaml.YAMLError as e:
            print(e)

    return pipelines_config


def convert_pipeline_dict_to_models(pipeline):
    pipeline_config = PipelineConfig(name=pipeline["name"],
                                     input=InputConfig(pipeline["input"]["topic"]),
                                     output=OutputConfig(pipeline["output"]["topic"]),
                                     transformation=TransformationConfig(pipeline["transformation"]["container-image"]))

    return pipeline_config    
