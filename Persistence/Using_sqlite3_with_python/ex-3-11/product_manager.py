import sqlite3

class ProductManager:
    """Handles SQLite operations with transactions."""

    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Create the products table if it doesn't exist."""
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

    def add_product(self, name, price):
        """Insert a product using transactions."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            conn.commit()
            print("Product added successfully.")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Transaction failed: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Monitor", 299.99)
