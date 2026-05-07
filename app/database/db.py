import sqlite3


class Database:
    def __init__(self, db_name="portfolio.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
