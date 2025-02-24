import sqlite3
import time

class PersistentQSQLite:
    def __init__(self, db_file="queue.db"):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    job_id TEXT PRIMARY KEY,
                    payload TEXT NOT NULL,
                    status TEXT CHECK(status IN ('pending', 'processing', 'done', 'failed', 'unprocessable')) DEFAULT 'pending',
                    last_updated REAL DEFAULT (strftime('%s', 'now')),
                    retry_count INTEGER DEFAULT 0
                )
            """)

    def enqueue(self, job_id, payload):
        with self.conn:
            self.conn.execute("INSERT INTO jobs (job_id, payload) VALUES (?, ?)", (job_id, payload))

    def dequeue(self, timeout=60):
        """Fetches a pending job or retries stuck jobs."""
        with self.conn:
            job = self.conn.execute("""
                SELECT job_id, payload FROM jobs 
                WHERE status='pending' OR (status='processing' AND (strftime('%s', 'now') - last_updated) > ?)
                ORDER BY last_updated ASC
                LIMIT 1
            """, (timeout,)).fetchone()
            
            if job:
                self.conn.execute("UPDATE jobs SET status='processing', last_updated=strftime('%s', 'now') WHERE job_id=?", (job[0],))
                return job
        return None

    def mark_done(self, job_id):
        with self.conn:
            self.conn.execute("UPDATE jobs SET status='done' WHERE job_id=?", (job_id,))

    def mark_failed(self, job_id):
        with self.conn:
            job = self.conn.execute("SELECT retry_count FROM jobs WHERE job_id=?", (job_id,)).fetchone()
            if job and job[0] >= 3:
                self.conn.execute("UPDATE jobs SET status='unprocessable' WHERE job_id=?", (job_id,))
            else:
                self.conn.execute("UPDATE jobs SET status='failed', retry_count=retry_count+1 WHERE job_id=?", (job_id,))
