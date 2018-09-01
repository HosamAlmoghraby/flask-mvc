import sqlite3


class User:
    def getProfile(id):
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute('SELECT * FROM users WHERE id = ?', [id])
        return db.fetchone()
