from confluent_kafka import Producer


conf = {'bootstrap.servers': "host1:9092,host2:9092" }

producer = Producer(conf)


def produced_callback(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def produce(topic, key, value):
    producer.produce(topic, key=key, value=value, callback=produced_callback)