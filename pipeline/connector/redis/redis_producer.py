import json
import redis
from connector.producer import AbstractProducer

class RedisProducer(AbstractProducer):
    '''Class responsible of producing and creating Redis prooducer.'''
    def __init__(self, configuration: dict):
        self.redis_client = redis.Redis(host=configuration['host'], port=configuration['port'], db=0)
        self.topic = configuration['topic']

    def produce(self, values):
        '''Function produce msg
            Args:
                value: the value that will be produce'''
        if isinstance(values, list):
            for value in values:
                self.redis_client.publish(self.topic, value)
        else:
            self.redis_client.publish(self.topic, values)
