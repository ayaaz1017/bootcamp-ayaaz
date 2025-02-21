import sqlite3

def create_table():
    """Create a fresh products table."""
    conn = sqlite3.connect("store.db")
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
    print("Database and table 'products' created.")

if __name__ == "__main__":
    create_table()
