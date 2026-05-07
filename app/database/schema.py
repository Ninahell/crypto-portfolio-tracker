from app.database.db import Database


def initialize_database():
    db = Database()

    db.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset TEXT NOT NULL,
            amount REAL NOT NULL,
            price REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    db.close()
