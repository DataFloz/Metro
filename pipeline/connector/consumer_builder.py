import ast
import os
from connector.consumer import AbstractConsumer
from connector.kafka.kafka_consumer import KafkaConsumer
from connector.producer import AbstractProducer
from bl.transformer_runner_interface import TransforerRunnerInterface

def build_consumer(transformer: TransforerRunnerInterface, producer: AbstractProducer) \
      -> AbstractConsumer:
    '''Function build the consumer object
        return:
            AbstractConsumer for the relant environment connector'''
    consumer_type = os.environ.get('type')
    if consumer_type == 'kafka':
        kafka_config = {
            'bootstrap.servers': os.environ.get('brokers'),
            'group.id': os.environ.get('group_id'),
            'topics': [ast.literal_eval(os.environ.get('input'))['topic']]
        }
        return KafkaConsumer(transformer, producer, kafka_config)
