from models.transformation_cfg import TransformationConfig


class ContainerTransformationConfig(TransformationConfig):
    def __init__(self, container_url):
        self.container_url = container_url
        self.type = 'container'

    def as_dict(self):
        return self.__dict__
