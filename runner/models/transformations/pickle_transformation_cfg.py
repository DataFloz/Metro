from models.transformations.transformation_cfg import TransformationConfig


class PickleTransformationCfg(TransformationConfig):
    '''Inhierent from TransformationConfig: responsible for pickle transformation config'''
    def __init__(self, file_name):
        self.file_name = file_name
        self.type = 'pickle'

    def as_dict(self):
        return {
            'file_name': self.file_name,
            'type': self.type
        }
