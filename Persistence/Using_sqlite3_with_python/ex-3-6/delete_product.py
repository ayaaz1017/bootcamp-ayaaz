import sqlite3

def delete_product(product_id):
    """Delete a product from the table based on its ID."""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

    print(f"Deleted product ID {product_id}")

if __name__ == "__main__":
    delete_product(2)  # Example delete
