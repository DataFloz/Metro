from confluent_kafka import Consumer, KafkaError, KafkaException

class kafkaConsumer:
    def __init__(self):
        conf = {
        'bootstrap.servers': "host1:9092,host2:9092",
        'group.id': "test",
        'auto.offset.reset': 'smallest'
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