import ast
import os
from connector.kafka.kafka_producer import KafkaProducer
from connector.redis.redis_producer import RedisProducer
from connector.producer import AbstractProducer

def build_producer() -> AbstractProducer:
    '''Function build the producer object
        return:
            AbstractProducer for the relant environment connector'''

    producer_type = os.environ.get('type')
    if producer_type == 'kafka':
        kafka_config = {
            'bootstrap.servers': os.environ.get('brokers'),
            'topic': ast.literal_eval(os.environ.get('output'))['topic']
        }
        return KafkaProducer(kafka_config)
    elif producer_type == 'redis':
        redis_config = {
            'host': os.environ.get('host'),
            'port': os.environ.get('port'),
            'topic': ast.literal_eval(os.environ.get('output'))['topic']
        }
        return RedisProducer(redis_config)