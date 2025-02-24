import uuid
import time
from persistent_queue.queue_sqlite import PersistentQSQLite

queue = PersistentQSQLite()

while True:
    job_id = str(uuid.uuid4())
    queue.enqueue(job_id, f"Data for {job_id}")
    print(f"[Producer] Submitted job {job_id}")
    time.sleep(5)
