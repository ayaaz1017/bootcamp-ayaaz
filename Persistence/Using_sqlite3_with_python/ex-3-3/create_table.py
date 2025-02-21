import sqlite3

# Connect to the database
conn = sqlite3.connect("store.db")

# Read and execute the SQL script
with open("create_table.sql", "r") as f:
    conn.executescript(f.read())

# Commit changes and close connection
conn.commit()
conn.close()

print("Table 'products' has been created successfully.")
