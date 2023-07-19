import ast
import os
from connector.kafka.kafka_producer import KafkaProducer 
from connector.producer import AbstractProducer

def build_producer() -> AbstractProducer:
    producer_type = os.environ.get('type')
    if producer_type == 'kafka':
        kafka_output_topic = ast.literal_eval(os.environ.get('output'))['topic']

        return KafkaProducer({'topic': kafka_output_topic})
    else:
        return None
