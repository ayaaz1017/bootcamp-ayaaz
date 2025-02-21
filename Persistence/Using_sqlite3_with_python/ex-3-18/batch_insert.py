import sqlite3

def batch_insert(products):
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        # Create table if not exists
        with open("create_table.sql", "r") as f:
            cursor.executescript(f.read())

        # Start transaction
        conn.execute("BEGIN TRANSACTION;")

        # Insert multiple products
        cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

        # Commit transaction
        conn.commit()
        print("Batch insert committed successfully.")

    except sqlite3.Error as e:
        conn.rollback()
        print("Batch insert failed. Rolling back...")
        print("Error:", e)

    finally:
        conn.close()

# Run function with sample data
if __name__ == "__main__":
    products = [
        ("Laptop", 999.99),
        ("Mouse", 29.99),
        ("Keyboard", 49.99),
    ]
    batch_insert(products)

