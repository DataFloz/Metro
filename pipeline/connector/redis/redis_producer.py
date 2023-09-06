import json
from connector.producer import AbstractProducer

class RedisProducer(AbstractProducer):
    '''Class responsible of producing and creating Redis prooducer.'''
    def __init__(self, configuration: dict):
      pass

    def produce(self, values):
        '''Function produce msg
            Args:
                value: the value that will be produce'''
        if isinstance(values, list):
            for value in values:
                pass
        else:
            pass
