import sqlite3

class ProductManager:
    """Handles SQLite operations including searching for products."""

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
        """Insert a product."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()

    def search_products(self, name_fragment):
        """Search for products by name fragment."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
        results = cursor.fetchall()
        conn.close()

        if results:
            for product in results:
                print(product)
        else:
            print("No matching products found.")

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Smartphone", 899.99)
    manager.search_products("phone")  # Example search
