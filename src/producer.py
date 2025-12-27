"""
Kafka Producer for Order Events

This module demonstrates publishing order messages to a Kafka topic.
Orders are serialized as JSON and sent to the 'orders' topic.
"""

from confluent_kafka import Producer
import uuid
import json

# Configure the Kafka producer with broker address
producer_config = {
    "bootstrap.servers": "localhost:9092",  # Kafka broker endpoint
    "log_level": 0  # Suppress debug/warning messages (0=critical only)
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    """Callback invoked after delivery. Logs success with offset or failure with error."""
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered {msg.value().decode('utf-8')}")
        print(f"Delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


# Create an order payload with unique ID
order = {
    "order_id": str(uuid.uuid4()),
    "user": "rishi", 
    "item": "pineappple pizza", 
    "quantity": 1
}

# Serialize order to JSON and encode as UTF-8 bytes for Kafka
value = json.dumps(order).encode("utf-8")

# Produce the message to the 'orders' topic (async operation)
producer.produce(
    topic="orders",     
    value=value,         
    callback=delivery_report 
)
producer.flush()