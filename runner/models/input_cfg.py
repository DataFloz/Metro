class InputConfig:
    def __init__(self, topic):
        self.topic = topic

    def as_dict(self):
        return self.__dict__
