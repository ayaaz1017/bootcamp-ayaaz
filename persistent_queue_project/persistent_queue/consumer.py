import time
import random
from persistent_queue.queue_sqlite import PersistentQSQLite

queue = PersistentQSQLite()

while True:
    job = queue.dequeue()
    if job:
        job_id, payload = job
        print(f"[Consumer] Processing job {job_id}...")
        time.sleep(random.randint(7, 15))  # Simulate processing time
        if random.random() > 0.2:  # 80% chance of success
            queue.mark_done(job_id)
            print(f"[Consumer] Completed job {job_id}")
        else:
            queue.mark_failed(job_id)
            print(f"[Consumer] Failed job {job_id}")
    else:
        time.sleep(3)  # No jobs, wait before checking again
