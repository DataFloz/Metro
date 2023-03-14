from kafka.consumer import kafkaConsumer
from kafka.producer import KafkaProducer
from bl.transformer_runner import Transformer

def main():
    print("start pipeline")
    transformer = Transformer()
    producer = KafkaProducer("test_result_topic")
    consumer = kafkaConsumer(transformer, producer)
    consumer.consume("test_input_topic")

main()