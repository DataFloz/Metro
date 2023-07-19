from bl.transformer_runner_interface import TransforerRunnerInterface
from connector.producer import AbstractProducer

class AbstractConsumer:
    '''Class responsible of consumning and creating kafka consumer.'''
    def __init__(self, trasformer: TransforerRunnerInterface, producer: AbstractProducer, configuration: dict):
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
        '''Function that convert raw message to dictionary for easy consume and running the logic for abstract connector
            Args:
                msg: the message recieve in the consumer '''
        pass