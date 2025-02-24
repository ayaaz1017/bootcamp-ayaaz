import unittest
from persistent_queue.queue_sqlite import PersistentQSQLite

class TestPersistentQSQLite(unittest.TestCase):
    def setUp(self):
        self.queue = PersistentQSQLite(":memory:")  # Use in-memory DB for testing

    def test_enqueue_dequeue(self):
        self.queue.enqueue("job1", "test payload")
        job = self.queue.dequeue()
        self.assertIsNotNone(job)
        self.assertEqual(job[0], "job1")

    def test_mark_done(self):
        self.queue.enqueue("job2", "another payload")
        self.queue.mark_done("job2")
        self.assertEqual(self.queue.conn.execute("SELECT status FROM jobs WHERE job_id='job2'").fetchone()[0], "done")

if __name__ == "__main__":
    unittest.main()
