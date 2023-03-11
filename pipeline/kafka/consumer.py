from confluent_kafka import Consumer, KafkaError, KafkaException

conf = {
        'bootstrap.servers': "host1:9092,host2:9092",
        'group.id': "test",
        'auto.offset.reset': 'smallest'
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