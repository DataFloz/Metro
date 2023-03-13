from confluent_kafka import Producer
import config as cfg


conf = {'bootstrap.servers': cfg.kafka_config['bootstrap.servers'] }

producer = Producer(conf)


def produced_callback(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def produce(topic, key, value):
    producer.produce(topic, key=key, value=value, callback=produced_callback)