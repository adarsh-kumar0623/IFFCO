import sqlite3
import os

DB_PATH = os.path.join("database", "iffco.db")

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ================= EMPLOYEES =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    designation TEXT,
    password TEXT,
    role TEXT NOT NULL
)
""")

# ================= STATES =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS states(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state_name TEXT UNIQUE NOT NULL
)
""")

# ================= DISTRICTS =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS districts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state_id INTEGER,
    district_name TEXT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
)
""")

# ================= FERTILIZERS =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS fertilizers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fertilizer_name TEXT UNIQUE,
    price_per_bag REAL
)
""")

# ================= SALES =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    employee_id TEXT,

    state_id INTEGER,

    district_id INTEGER,

    fertilizer_id INTEGER,

    quantity INTEGER,

    total_amount REAL,

    sale_date DATE,

    FOREIGN KEY(employee_id) REFERENCES employees(employee_id),

    FOREIGN KEY(state_id) REFERENCES states(id),

    FOREIGN KEY(district_id) REFERENCES districts(id),

    FOREIGN KEY(fertilizer_id) REFERENCES fertilizers(id)
)
""")

conn.commit()
conn.close()

print("Database Initialized Successfully.")