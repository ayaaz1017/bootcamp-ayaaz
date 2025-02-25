# Persistent Queue System

## Overview
The **Persistent Queue System** is a lightweight, file-based queue implementation designed for reliable message passing between producer and consumer processes. It ensures data persistence using SQLite and follows a Supervisor-based process management approach.

## Project Structure
```
PERSISTENT_QUEUE_SYSTEM/
│── README.md        # Project documentation
│── persistent_queue/   # Your Python package
│   │── __init__.py  # Marks it as a package
│   │── queue.py     # Persistent queue implementation
│   │── producer.py  # Producer script
│   │── consumer.py  # Consumer script
│   │── ops_console.py  # Streamlit dashboard for job monitoring
│── supervisor/       # Supervisor config directory
│   │── supervisord.conf  # Configuration for managing processes
│── logs/            # Log files directory
```

## Getting Started

### Cloning the Repository
```bash
git clone https://github.com/bootcamp-ayaaz/persistent-queue.git
cd persistent-queue
```

### Running the Queue System
The queue system consists of a **producer** that adds messages to the queue and a **consumer** that processes them. Supervisor is used to manage both processes.

#### Step 1: Start Supervisor
```bash
supervisord -c supervisor/supervisord.conf
```

#### Step 2: Monitor the Processes
To check the status of the running processes:
```bash
supervisorctl -c supervisor/supervisord.conf status
```
To start/stop a process:
```bash
supervisorctl -c supervisor/supervisord.conf start producer
supervisorctl -c supervisor/supervisord.conf stop consumer
```

#### Step 3: Checking Logs
Logs are stored in the `logs/` directory:
```bash
tail -f logs/producer.out.log  # View producer logs
tail -f logs/consumer.out.log  # View consumer logs
```

## Design Decisions
### Why SQLite for Persistence?
- Ensures durability of messages even after process restarts.
- Easy to manage without requiring a separate database server.
- ACID compliance ensures message consistency.

### Why Supervisor for Process Management?
- Ensures automatic restarts if a process crashes.
- Provides a simple interface to control multiple processes.
- Logs stdout and stderr for easier debugging.

### Why a File-Based Queue Instead of Redis/Kafka?
- Simplicity: No need for external services.
- Lower system requirements.
- Suitable for lightweight applications.

## Logging & Debugging
- **Producer logs**: Track messages being added to the queue.
- **Consumer logs**: Monitor processed messages and errors.
- **Supervisor logs**: Check process health and crashes.

If processes are failing unexpectedly, check:
```bash
tail -f /tmp/supervisord.log
```

## License
This project is open-source under the MIT License.
