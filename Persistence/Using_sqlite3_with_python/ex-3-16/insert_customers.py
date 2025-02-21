import sqlite3

def insert_customers():
    try:
        # Connect to the database (creates customers.db if not exists)
        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()

        # Create table if it does not exist
        with open("create_table.sql", "r") as f:
            cursor.executescript(f.read())

        # Begin transaction
        conn.execute("BEGIN TRANSACTION;")

        # Insert multiple customers
        customers = [
            ("Alice Johnson", "alice@example.com"),
            ("Bob Smith", "bob@example.com"),
            ("Charlie Davis", "charlie@example.com"),
        ]

        cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers)

        # Commit the transaction
        conn.commit()
        print("Transaction committed successfully.")

    except sqlite3.Error as e:
        # Rollback if error occurs
        conn.rollback()
        print("Transaction failed. Rolling back...")
        print("Error:", e)

    finally:
        conn.close()

# Run the function
if __name__ == "__main__":
    insert_customers()

