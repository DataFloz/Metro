from config import kafka_input_topic, kafka_output_topic
from kafka.consumer import KafkaConsumer
from kafka.producer import KafkaProducer
from bl.transformation_builder import build_transformation

def main():
    print("start pipeline")
    transformer = build_transformation()
    producer = KafkaProducer(kafka_output_topic)
    consumer = KafkaConsumer(transformer, producer)
    consumer.consume([kafka_input_topic])

main()
