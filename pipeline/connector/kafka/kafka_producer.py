import json
from confluent_kafka import Producer
from connector.producer import AbstractProducer
import config as cfg

class KafkaProducer(AbstractProducer):
    '''Class responsible of producing and creating kafka prooducer.'''
    def __init__(self, configuration: dict):
        conf = {
            'bootstrap.servers': cfg.kafka_config['bootstrap.servers'] 
        }

        self.producer = Producer(conf)
        self.topic = configuration['topic']

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
