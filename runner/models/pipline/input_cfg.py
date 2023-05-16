class InputConfig:
    '''Class represent the metro configuration'''
    def __init__(self, topic):
        self.topic = topic

    def as_dict(self):
        '''Function for convert config to dict'''
        return self.__dict__
