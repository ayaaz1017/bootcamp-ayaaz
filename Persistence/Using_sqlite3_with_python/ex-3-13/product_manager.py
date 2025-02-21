import sqlite3

class ProductManager:
    """Handles SQLite operations including aggregation queries."""

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

    def add_product(self, name, price):
        """Insert a product."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()

    def calculate_total_value(self):
        """Calculate the total value of all products."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(price) FROM products")
        total = cursor.fetchone()[0]
        conn.close()

        print(f"Total value of all products: {total:.2f}")

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Laptop", 1200.00)
    manager.add_product("Mouse", 50.00)
    manager.calculate_total_value()
