from models.input_cfg import InputConfig
from models.output_cfg import OutputConfig
from models.transformation_cfg import TransformationConfig

class PipelineConfig:
    def __init__(self, name, input: InputConfig, output: OutputConfig, transformation: TransformationConfig):
        self.name = name
        self.input = input
        self.output = output
        self.transformation = transformation

    def as_dict(self):
        return {
            'name': self.name,
            'input': self.input.__dict__,
            'output': self.output.__dict__,
            'transformation': self.transformation.__dict__
        }