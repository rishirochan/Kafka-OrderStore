from confluent_kafka import Consumer
import json

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
    "log_level": 0  # Suppress debug/warning messages
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])

try:
    print("Taking Consumer Orders")
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue
        order = json.loads(msg.value().decode('utf-8'))
        print(f"Order processed: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\nStopping Tracker")
finally:
    consumer.close()
