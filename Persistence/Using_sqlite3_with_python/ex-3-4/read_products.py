import sqlite3

def fetch_products():
    """Fetch and print all records from the products table."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    conn.close()

    if products:
        for product in products:
            print(product)
    else:
        print("No products found.")

# Run the function
if __name__ == "__main__":
    fetch_products()
