import sqlite3
import csv

class ProductManager:
    """Handles SQLite operations including exporting data to CSV."""

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

    def export_to_csv(self):
        """Export data to CSV."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")

        with open("products.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Price"])
            writer.writerows(cursor.fetchall())

        conn.close()
        print("Data exported to products.csv")

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product("Monitor", 299.99)
    manager.export_to_csv()
