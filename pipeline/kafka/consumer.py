import ast
import config as cfg
from confluent_kafka import Consumer, KafkaError, KafkaException
from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface
from kafka.producer import KafkaProducer

class KafkaConsumer:
    '''Class responsible of consumning and creating kafka consumer.'''
    def __init__(self, trasformer: TransforerRunnerInterface, producer: KafkaProducer):
        logger.info(f"connect to: {cfg.kafka_config['bootstrap.servers']}")
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
        logger.info("start consume topics: %s", topics)
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
                        logger.debug("%s %s  \
                              reached end at offset {msg.offset()}\n", msg.topic(), msg.partition())
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    # msg_process(msg)
                    logger.debug("process message")
                    message_value = self.get_message_value_as_dict(msg)
                    results = self.transformer.run_logic(message_value)
                    logger.debug("produce message")
                    self.producer.produce(results)
                    logger.debug("end message pipeline")
        finally:
            self.consumer.close()

    def shutdown(self):
        '''Function shutdown the consumer if needed'''
        self.running = False

    def get_message_value_as_dict(self, msg):
        msg_value = msg.value()
        encode_msg_value = msg_value.decode('utf-8')
        message_data = ast.literal_eval(encode_msg_value)

        return message_data