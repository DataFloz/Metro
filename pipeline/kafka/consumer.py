import config as cfg
from confluent_kafka import Consumer, KafkaError, KafkaException
from bl.transformer_runner_interface import TransforerRunnerInterface
from kafka.producer import KafkaProducer

class KafkaConsumer:
    '''Class responsible of consumning and creating kafka consumer.'''
    def __init__(self, trasformer: TransforerRunnerInterface, producer: KafkaProducer):
        print("connect to:" + cfg.kafka_config['bootstrap.servers'])
        conf = {
            'bootstrap.servers': cfg.kafka_config['bootstrap.servers'],
            'group.id': cfg.kafka_config['group.id'],
            'auto.offset.reset': 'latest'
        }

        self.consumer = Consumer(conf)
        self.transformer = trasformer
        self.producer = producer
        self.running = False

    def consume(self, topics):
        '''Function start the consuming
            Args:
                topic: string array of the topic to consume'''
        print(topics)
        self.running = True
        try:
            self.consumer.subscribe(topics)

            while self.running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        print(f"{msg.topic()} {msg.partition()} \
                              reached end at offset {msg.offset()}\n")
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    # msg_process(msg)
                    print("some msg pocess")
                    results = self.transformer.run_logic(msg)
                    print("some msg produce")
                    self.producer.produce(results)
                    print("end msg pipeline")
        finally:
            self.consumer.close()

    def shutdown(self):
        '''Function shutdown the consumer if needed'''
        self.running = False
