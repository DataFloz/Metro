from dotenv import load_dotenv
import os

load_dotenv()

kafka_config = {
    'bootstrap.servers': os.environ.get('bosstrap.servers'),
    'group.id': os.environ.get('group.id'),
    'auto.offset.reset': os.environ.get('auto.offset.reset')
}