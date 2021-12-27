from confluent_kafka import Consumer
from confluent_kafka.avro import AvroConsumer


avroconf = {'bootstrap.servers': "localhost:9092",
        'schema.registry.url': "http://localhost:8081",
        'group.id': "foo",
        'auto.offset.reset': 'earliest'}

conf = {'bootstrap.servers': "localhost:9092", 
        'group.id': "foo",
        'auto.offset.reset': 'earliest'}

#consumer = Consumer(conf)
consumer = AvroConsumer(avroconf)

running = True

def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Successfully poll a record from "
                  f"Kafka topic: {msg.topic()}, partition: {msg.partition()}, offset: {msg.offset()}\n"
                  f"message key: {msg.key()} || message value: {msg.value()}")
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

basic_consume_loop(consumer, ["atm_transactions"])

def shutdown():
    running = False