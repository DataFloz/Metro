from utils.logger import logger
from connector.consumer_builder import build_consumer
from connector.producer_builder import build_producer
from bl.transformation_builder import build_transformation

def main():
    ''' The main function is the pipeline entrypoint. '''
    logger.info("starting pipeline")
    transformer = build_transformation()
    producer = build_producer()
    consumer = build_consumer(transformer, producer)
    consumer.consume()

main()
