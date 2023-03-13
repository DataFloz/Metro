from confluent_kafka import Consumer, KafkaError, KafkaException
from dotenv import load_dotenv
import os

load_dotenv()


conf = {
        'bootstrap.servers': os.environ.get('bootstrap.servers'),
        'group.id': os.environ.get('group.id'),
        'auto.offset.reset': os.environ.get('auto.offset.reset')
    }

consumer = Consumer(conf)


running = True

def consume(topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
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
        # Close down consumer to commit final offsets.
        consumer.close()

def shutdown():
    running = False