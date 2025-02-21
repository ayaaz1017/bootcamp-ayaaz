import sqlite3

class ProductManager:
    """Handles SQLite operations including batch insertion."""

    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Create the products table."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def batch_insert(self, products):
        """Insert multiple products in one transaction."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
        conn.commit()
        conn.close()
        print("Batch insert completed.")

if __name__ == "__main__":
    manager = ProductManager()
    manager.batch_insert([
        ("Keyboard", 75.99),
        ("Speaker", 150.00),
        ("Webcam", 120.50)
    ])
