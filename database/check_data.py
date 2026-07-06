import sqlite3
import os

DB_PATH = os.path.join("database", "iffco.db")

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(employees)")

for row in cursor.fetchall():
    print(row)

conn.close()