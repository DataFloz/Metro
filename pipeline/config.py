import os
import ast


kafka_config = {
    'bootstrap.servers': os.environ.get('brokers'),
    'group.id': os.environ.get('group_id'),
}

kafka_input_topic = ast.literal_eval(os.environ.get('input'))['topic']

kafka_output_topic = ast.literal_eval(os.environ.get('output'))['topic']
