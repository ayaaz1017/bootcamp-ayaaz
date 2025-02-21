import sqlite3

def update_inventory(product_id, quantity_change):
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        # Create tables if not exists
        with open("create_tables.sql", "r") as f:
            cursor.executescript(f.read())

        # Start transaction
        conn.execute("BEGIN TRANSACTION;")

        # Check current stock
        cursor.execute("SELECT stock FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if product is None or product[0] + quantity_change < 0:
            raise ValueError("Invalid stock update")

        # Update stock
        cursor.execute("UPDATE products SET stock = stock + ? WHERE product_id = ?", (quantity_change, product_id))

        # Log inventory change
        cursor.execute("INSERT INTO inventory_log (product_id, change) VALUES (?, ?)", (product_id, quantity_change))

        # Commit transaction
        conn.commit()
        print("Inventory updated successfully.")

    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print("Transaction failed. Rolling back...")
        print("Error:", e)

    finally:
        conn.close()

# Run function with sample values
if __name__ == "__main__":
    update_inventory(1, -3)

