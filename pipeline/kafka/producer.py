from confluent_kafka import Producer
import config as cfg

class KafkaProducer():
    def __init__(self, topic):
        conf = {
            'bootstrap.servers': cfg.kafka_config['bootstrap.servers'] 
        }

        self.producer = Producer(conf)
        self.topic = topic


    def produced_callback(self, err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    def produce(self, value):
        self.producer.produce(self.topic, key=None, value=value, callback=self.produced_callback)