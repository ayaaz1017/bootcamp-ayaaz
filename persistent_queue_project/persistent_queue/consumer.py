import time
import random
from persistent_queue.queue_sqlite import PersistentQSQLite

queue = PersistentQSQLite()

while True:
    job = queue.dequeue()
    
    if job:
        job_id, job_data = job
        print(f"Processing {job_data} (ID: {job_id})")

        try:
            # Simulate processing with a 20% chance of failure
            if random.random() < 0.2:
                raise Exception("Random Processing Failure")

            queue.mark_complete(job_id)
            print(f"Completed {job_data}")

        except Exception as e:
            print(f"Error processing {job_data}: {e}")
            queue.mark_failed(job_id)

    time.sleep(2)  # Simulating job processing time
