"""
Kafka Consumer (Order Tracker)

This module demonstrates consuming order messages from a Kafka topic.
It continuously polls for new orders and processes them in real-time.
"""

from confluent_kafka import Consumer
import json

# Configure the Kafka consumer with broker and consumer group settings
consumer_config = {
    "bootstrap.servers": "localhost:9092",  # Kafka broker endpoint
    "group.id": "order-tracker",  # Consumer group ID for offset tracking
    "auto.offset.reset": "earliest",  # Start from oldest message if no offset exists
    "log_level": 0  # Suppress debug/warning messages
}
consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])

try:
    print("Taking Consumer Orders")
    
    # Infinite loop to continuously poll for new messages
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue
        order = json.loads(msg.value().decode('utf-8'))

        # Process and display the order details
        print(f"Order processed: {order['quantity']} x {order['item']} from {order['user']}")
        
except KeyboardInterrupt:
    print("\nStopping Tracker")
finally:
    consumer.close()
