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
            print(f"Failed to deliver message: {str(msg)}: {str(err)}")
        else:
            print(f"Message produced: {str(msg)}")

    def produce(self, value):
        '''Function produce msg
            Args:
                value: the value that will be produce'''
        self.producer.produce(self.topic, key=None, value=value, callback=self.produced_callback)
