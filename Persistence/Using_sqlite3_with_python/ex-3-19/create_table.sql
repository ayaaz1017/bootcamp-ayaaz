CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL CHECK(balance >= 0)
);

INSERT INTO accounts (name, balance) VALUES ('Alice', 500.00);
INSERT INTO accounts (name, balance) VALUES ('Bob', 300.00);

