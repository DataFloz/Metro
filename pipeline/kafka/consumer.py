from confluent_kafka import Consumer, KafkaError, KafkaException
import config as cfg

class kafkaConsumer:
    def __init__(self):
        
        conf = {
            'bootstrap.servers': cfg.kafka_config['bootstrap.servers'],
            'group.id': cfg.kafka_config['group.id'],
            'auto.offset.reset': cfg.kafka_config['auto.offset.reset']
        }       


        self.consumer = Consumer(conf)


    def consume(self, topics):
        self.running = True
        try:
            self.consumer.subscribe(topics)

            while self.running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        # Will remove later
                        print('%% %s [%d] reached end at offset %d\n' %
                                        (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    # msg_process(msg)
                    print("some msg pocess")
        finally:
            self.consumer.close()

    def shutdown(self):
        self.running = False
