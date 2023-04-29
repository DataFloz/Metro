from models.input_cfg import InputConfig
from models.output_cfg import OutputConfig
from models.transformations.transformation_cfg import TransformationConfig

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
