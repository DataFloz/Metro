from models.pipline.input_cfg import InputConfig
from models.pipline.output_cfg import OutputConfig
from models.pipline.transformations.transformation_cfg import TransformationConfig
from models.pipline.transformations.transformation_cfg_builder import from_config_dict as convert_transformation_config

class PipelineConfig:
    '''Class represent the pipeline configuration'''
    def __init__(self, name, input: InputConfig, output: OutputConfig,
                 transformation: TransformationConfig):
        self.name = name
        self.input = input
        self.output = output
        self.transformation = transformation

    def as_dict(self):
        '''Function for convert config to dict'''
        return {
            'name': self.name,
            'input': self.input.as_dict(),
            'output': self.output.as_dict(),
            'transformation': self.transformation.as_dict()
        }

    @classmethod
    def from_config_dict(cls, pipeline_dict):
        '''Responsible to convert the pipline config
       Args:
        pipeline: dict
       Returns:
        PipelineConfig object'''
        pipeline_config = PipelineConfig(name=pipeline_dict["name"],
                        input=InputConfig(pipeline_dict["input"]["topic"]),
                        output=OutputConfig(pipeline_dict["output"]["topic"]),
                        transformation=convert_transformation_config(pipeline_dict))

        return pipeline_config
    