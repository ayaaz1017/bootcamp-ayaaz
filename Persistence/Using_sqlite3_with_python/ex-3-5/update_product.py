import sqlite3

def update_product_price(product_id, new_price):
    """Update the price of a product based on its ID."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

    print(f"Updated product ID {product_id} with new price {new_price}")

if __name__ == "__main__":
    update_product_price(1, 179.99)  # Example: Update product ID 1
