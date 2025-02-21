import sqlite3

def update_orders(order_id, new_total_price, detail_id, new_quantity):
    try:
        conn = sqlite3.connect("orders.db")
        cursor = conn.cursor()

        # Create tables if not exists
        with open("create_tables.sql", "r") as f:
            cursor.executescript(f.read())

        # Start transaction
        conn.execute("BEGIN TRANSACTION;")

        # Update orders table
        cursor.execute("UPDATE orders SET total_price = ? WHERE order_id = ?", (new_total_price, order_id))

        # Update order_details table
        cursor.execute("UPDATE order_details SET quantity = ? WHERE detail_id = ?", (new_quantity, detail_id))

        # Commit transaction
        conn.commit()
        print("Transaction committed successfully.")

    except sqlite3.Error as e:
        conn.rollback()
        print("Transaction failed. Rolling back...")
        print("Error:", e)

    finally:
        conn.close()

# Run the function with sample values
if __name__ == "__main__":
    update_orders(1, 200.50, 1, 5)

