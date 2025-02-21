import sqlite3

def transfer_funds(sender_id, receiver_id, amount):
    try:
        conn = sqlite3.connect("banking.db")
        cursor = conn.cursor()

        # Create table if not exists
        with open("create_table.sql", "r") as f:
            cursor.executescript(f.read())

        # Start transaction
        conn.execute("BEGIN TRANSACTION;")

        # Check sender balance
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (sender_id,))
        sender_balance = cursor.fetchone()

        if sender_balance is None or sender_balance[0] < amount:
            raise ValueError("Insufficient funds or account does not exist")

        # Deduct from sender
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, sender_id))

        # Add to receiver
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, receiver_id))

        # Commit transaction
        conn.commit()
        print("Transaction successful: Transferred", amount)

    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print("Transaction failed. Rolling back...")
        print("Error:", e)

    finally:
        conn.close()

# Run function with sample values
if __name__ == "__main__":
    transfer_funds(1, 2, 200)

