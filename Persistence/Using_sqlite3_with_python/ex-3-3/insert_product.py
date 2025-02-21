import sqlite3

def insert_product(name, price):
    """Insert a new product into the products table."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    
    conn.commit()
    conn.close()

    print(f"Inserted product: {name} with price {price}")

# Example Usage
if __name__ == "__main__":
    insert_product("Laptop", 799.99)
    insert_product("Mouse", 19.99)
