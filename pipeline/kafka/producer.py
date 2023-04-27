import json
from utils.logger import logger
from confluent_kafka import Producer
import config as cfg

class KafkaProducer():
    '''Class responsible of producing and creating kafka prooducer.'''
    def __init__(self, topic):
        conf = {
            'bootstrap.servers': cfg.kafka_config['bootstrap.servers'] 
        }

        self.producer = Producer(conf)
        self.topic = topic


    def produced_callback(self, err, msg):
        '''Callback after produce
            Args:
                err: if the produce failed
                msg: the msg that produced'''
        if err is not None:
            logger.error("Failed to deliver message: %s:%s", str(msg), str(err))
        else:
            logger.error("Message produced: %s", str(msg))

    def produce(self, values):
        '''Function produce msg
            Args:
                value: the value that will be produce'''
        if isinstance(values, list):
            for value in values:
                self.producer.produce(self.topic, key=None, value=json.dumps(value, default=str),
                                      callback=self.produced_callback)
        else:
            self.producer.produce(self.topic, key=None, value=json.dumps(values, default=str), 
                                      callback=self.produced_callback)
