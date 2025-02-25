from persistent_queue.queue_sqlite import PersistentQSQLite

queue = PersistentQSQLite()

# Simulating job production
for i in range(5):
    queue.enqueue(f"Job {i+1}")
    print(f"Produced Job {i+1}")
