import sqlite3

# Connect to SQLite (creates store.db if it doesn't exist)
conn = sqlite3.connect("store.db")

# Close the connection
conn.close()

print("Database 'store.db' has been created successfully.")
