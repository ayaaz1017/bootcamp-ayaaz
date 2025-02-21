# generate_sql.py
with open("insert_data.sql", "w") as f:
    f.write("BEGIN TRANSACTION;\n")
    for i in range(1, 501):
        f.write(f"INSERT INTO COMPANIES VALUES ('Company_{i}', {i});\n")
    f.write("COMMIT;\n")
