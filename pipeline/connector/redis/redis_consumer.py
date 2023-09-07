import redis
from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface
from connector.producer import AbstractProducer
from connector.consumer import AbstractConsumer

class RedisConsumer(AbstractConsumer):
    '''Class responsible of consumning and creating kafka consumer.'''
    def __init__(self, trasformer: TransforerRunnerInterface, producer: AbstractProducer,
                  configuration: dict):
        self.redis_client = redis.Redis(host=configuration['host'], port=configuration['port'], db=0)
        self.topic = configuration['topic']
        self.transformer = trasformer
        self.producer = producer
        self.running = False

    def consume(self):
        '''Function start the consuming
            Args:
                topic: string array of the topic to consume'''
        self.running = True
        p = self.redis_client.pubsub()
        p.subscribe(self.topic)

        while self.running:
            logger.debug("process message")
            message = p.get_message()
            if message:
                results = self.transformer.run_logic(message)
                logger.debug("produce message")
                self.producer.produce(results)
                logger.debug("end message pipeline")

    def shutdown(self):
        '''Function shutdown the consumer if needed'''
        self.running = False

    def get_message_value_as_dict(self, msg):
        pass
