# Kafka StreamStore

A hands-on learning project demonstrating real-time event streaming with Apache Kafka. This project implements a simple order processing system with a producer that publishes orders and a consumer (tracker) that processes them.

## Tech Stack

- **Python 3.13** — Core language
- **Apache Kafka** — Event streaming platform
- **confluent-kafka** — Python client for Kafka
- **Docker** — Containerization
- **uv** — Fast Python package manager

## What is Kafka?

**Apache Kafka** is a distributed event streaming platform used for building real-time data pipelines and streaming applications. Think of it as a highly scalable message queue that can handle millions of events per second.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Producer** | Publishes messages (events) to Kafka topics |
| **Consumer** | Subscribes to topics and processes messages |
| **Topic** | A category/feed name where messages are stored |
| **Partition** | Topics are split into partitions for parallelism |
| **Offset** | A unique ID for each message within a partition |
| **Broker** | A Kafka server that stores and serves messages |
| **Consumer Group** | Multiple consumers working together to process a topic |

### How It Works

```
┌──────────┐     ┌─────────────────┐     ┌──────────┐
│ Producer │ ──▶ │  Kafka Broker   │ ──▶ │ Consumer │
│ (orders) │     │  (topic: orders)│     │ (tracker)│
└──────────┘     └─────────────────┘     └──────────┘
```

1. **Producer** sends order data to the `orders` topic
2. **Kafka Broker** stores messages durably with an offset
3. **Consumer** polls for new messages and processes them

## Project Structure

```
kafka-streamstore/
├── docker-compose.yaml   # Kafka broker (KRaft mode)
├── src/
│   ├── producer.py       # Publishes order events
│   └── tracker.py        # Consumes and processes orders
├── pyproject.toml        # Project dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (Python package manager)

### Setup

1. **Start Kafka**
   ```bash
   docker compose up -d
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the producer** (sends an order)
   ```bash
   cd src
   uv run producer.py
   ```

4. **Run the tracker** (consumes orders)
   ```bash
   cd src
   uv run tracker.py
   ```

## Key Learnings

### KRaft Mode
This project uses Kafka in **KRaft mode** (Kafka Raft), which eliminates the need for ZooKeeper. KRaft is the modern consensus protocol for Kafka metadata management.

### Delivery Guarantees
Kafka provides three delivery semantics:
- **At-most-once** — Messages may be lost but never redelivered
- **At-least-once** — Messages are never lost but may be redelivered  
- **Exactly-once** — Each message is delivered exactly once (requires transactions)

### Consumer Groups
The `group.id` in the consumer config enables:
- **Offset tracking** — Kafka remembers where each consumer left off
- **Load balancing** — Multiple consumers in a group share partitions
- **Fault tolerance** — If one consumer dies, others pick up its partitions

## Useful Kafka Commands

```bash
# List all topics
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

# Describe a topic
docker exec -it kafka kafka-topics --describe --topic orders --bootstrap-server localhost:9092

# Read all messages from beginning
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning
```

---

*Built as a learning exercise to understand event-driven architectures and real-time data streaming.*