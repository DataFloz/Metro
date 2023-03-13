from confluent_kafka import Producer
from dotenv import load_dotenv
import os


conf = {'bootstrap.servers': os.environ.get('bosstrap.servers') }

producer = Producer(conf)


def produced_callback(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def produce(topic, key, value):
    producer.produce(topic, key=key, value=value, callback=produced_callback)