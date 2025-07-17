import mysql.connector
from config import Config

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            database=Config.DB_NAME
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_user(self, user_id: int) -> dict:
        query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def add_user(self, user_id: int, username: str):
        query = "INSERT INTO users (user_id, username) VALUES (%s, %s)"
        self.cursor.execute(query, (user_id, username))
        self.connection.commit()

    def get_items(self) -> list:
        query = "SELECT * FROM items"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_item(self, item_id: int) -> dict:
        query = "SELECT * FROM items WHERE id = %s"
        self.cursor.execute(query, (item_id,))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
