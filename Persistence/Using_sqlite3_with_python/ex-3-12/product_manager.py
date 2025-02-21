import sqlite3

class ProductManager:
    """Handles SQLite operations including join queries."""

    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self):
        """Create products and categories tables."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        """)

        conn.commit()
        conn.close()

    def add_category(self, name):
        """Insert a category."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    def add_product(self, name, price, category_id):
        """Insert a product linked to a category."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", (name, price, category_id))
        conn.commit()
        conn.close()

    def fetch_products_with_categories(self):
        """Fetch products along with their category names."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT products.id, products.name, products.price, categories.name 
            FROM products 
            JOIN categories ON products.category_id = categories.id
        """)
        results = cursor.fetchall()
        conn.close()

        for row in results:
            print(row)

if __name__ == "__main__":
    manager = ProductManager()
    manager.add_category("Electronics")
    manager.add_product("Smartphone", 999.99, 1)
    manager.fetch_products_with_categories()
