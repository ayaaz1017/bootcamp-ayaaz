import sqlite3

class ProductManager:
    """Handles SQLite operations with exception handling."""

    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Create the products table with exception handling."""
        try:
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
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

    def add_product(self, name, price):
        """Insert a product with exception handling."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            conn.commit()
            print("Product added successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting product: {e}")
        finally:
            conn.close()

# Run script
if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Headphones", 199.99)
