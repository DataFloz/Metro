class ConnectorConfig:
    '''Class represent the metro configuration'''
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def as_dict(self):
        '''Function for convert config to dict'''
        return self.__dict__
