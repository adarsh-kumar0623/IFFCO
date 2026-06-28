import sqlite3

conn = sqlite3.connect("database/iffco.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

print("===== STATES =====")

for row in cursor.execute("""
SELECT id, state_name
FROM states
ORDER BY state_name
"""):
    print(dict(row))

conn.close()