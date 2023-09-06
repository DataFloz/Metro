from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface
from connector.producer import AbstractProducer
from connector.consumer import AbstractConsumer

class RedisConsumer(AbstractConsumer):
    '''Class responsible of consumning and creating kafka consumer.'''
    def __init__(self, trasformer: TransforerRunnerInterface, producer: AbstractProducer,
                  configuration: dict):
        pass

    def consume(self):
        '''Function start the consuming
            Args:
                topic: string array of the topic to consume'''
        pass

    def shutdown(self):
        '''Function shutdown the consumer if needed'''
        pass

    def get_message_value_as_dict(self, msg):
        pass
