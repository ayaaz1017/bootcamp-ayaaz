import sqlite3

class ProductManager:
    """Handles SQLite operations with data validation."""

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
                price REAL NOT NULL CHECK(price > 0)
            )
        """)
        conn.commit()
        conn.close()

    def add_product(self, name, price):
        """Insert a product with validation."""
        if not isinstance(name, str) or not name.strip():
            print("Invalid product name!")
            return

        if not isinstance(price, (int, float)) or price <= 0:
            print("Invalid price! It must be a positive number.")
            return

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()
        print("Product added successfully.")

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("", 199.99)  # Invalid name
    manager.add_product("Tablet", -50)  # Invalid price
    manager.add_product("Tablet", 499.99)  # Valid entry
