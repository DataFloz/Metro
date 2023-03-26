class TransformationConfig:
    def __init__(self, container_url):
        self.container_url = container_url

    def as_dict(self):
        return self.__dict__
