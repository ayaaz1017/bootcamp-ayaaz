import sqlite3

def insert_sample_data():
    """Insert sample products into the products table."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    products = [
        ("Laptop", 999.99),
        ("Mouse", 49.99),
        ("Keyboard", 79.99)
    ]
    
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
    conn.commit()
    conn.close()
    
    print("Sample products inserted successfully.")

# Run script
if __name__ == "__main__":
    insert_sample_data()
