import sqlite3

def insert_sample_data():
    """Insert sample products into the products table."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [
        ("Monitor", 199.99),
        ("Printer", 149.99)
    ])
    
    conn.commit()
    conn.close()
    print("Sample data inserted.")

if __name__ == "__main__":
    insert_sample_data()
