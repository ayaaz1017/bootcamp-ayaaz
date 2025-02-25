import sqlite3
from persistent_queue.queue_interface import PersistentQueue

class PersistentQSQLite(PersistentQueue):
    """SQLite-based Persistent Queue."""

    def __init__(self, db_path="queue.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Create necessary tables in SQLite if they don’t exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS queue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    status TEXT CHECK(status IN ('pending', 'processing', 'failed', 'completed')) DEFAULT 'pending',
                    attempts INTEGER DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS bad_records (
                    id INTEGER PRIMARY KEY,
                    data TEXT NOT NULL,
                    reason TEXT
                );
            """)
            conn.commit()

    def enqueue(self, job_data: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO queue (data) VALUES (?)", (job_data,))
            conn.commit()

    def dequeue(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, data FROM queue WHERE status = 'pending' ORDER BY id LIMIT 1")
            job = cursor.fetchone()
            if job:
                cursor.execute("UPDATE queue SET status = 'processing' WHERE id = ?", (job[0],))
                conn.commit()
            return job

    def mark_complete(self, job_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE queue SET status = 'completed' WHERE id = ?", (job_id,))
            conn.commit()

    def mark_failed(self, job_id: int):
        """Mark job as failed if it exceeds 3 attempts."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT attempts, data FROM queue WHERE id = ?", (job_id,))
            job = cursor.fetchone()
            
            if job and job[0] >= 3:
                cursor.execute("INSERT INTO bad_records (id, data, reason) VALUES (?, ?, ?)", 
                               (job_id, job[1], "Too many failed attempts"))
                cursor.execute("DELETE FROM queue WHERE id = ?", (job_id,))
            else:
                cursor.execute("UPDATE queue SET attempts = attempts + 1 WHERE id = ?", (job_id,))
            conn.commit()
