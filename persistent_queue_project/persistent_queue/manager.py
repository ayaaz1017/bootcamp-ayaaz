import sqlite3

def list_failed_jobs():
    with sqlite3.connect("queue.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, data FROM queue WHERE status = 'failed'")
        return cursor.fetchall()

def resubmit_failed_jobs():
    with sqlite3.connect("queue.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE queue SET status = 'pending' WHERE status = 'failed'")
        conn.commit()
        print("Resubmitted failed jobs.")

if __name__ == "__main__":
    print("Failed Jobs:", list_failed_jobs())
    resubmit_failed_jobs()
