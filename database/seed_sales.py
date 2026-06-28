import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("database/iffco.db")
cursor = conn.cursor()

# Clear old sales
cursor.execute("DELETE FROM sales")

# Get master data
employees = [row[0] for row in cursor.execute("SELECT employee_id FROM employees WHERE role='employee'").fetchall()]
states = [row[0] for row in cursor.execute("SELECT id FROM states").fetchall()]
fertilizers = cursor.execute("SELECT id, price_per_bag FROM fertilizers").fetchall()

for _ in range(5000):

    employee = random.choice(employees)

    state = random.choice(states)

    districts = cursor.execute(
        "SELECT id FROM districts WHERE state_id=?",
        (state,)
    ).fetchall()

    district = random.choice(districts)[0]

    fertilizer = random.choice(fertilizers)

    fertilizer_id = fertilizer[0]
    price = fertilizer[1]

    quantity = random.randint(20, 400)

    total = quantity * price

    date = (
        datetime.now() -
        timedelta(days=random.randint(0, 365))
    ).strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO sales(
            employee_id,
            state_id,
            district_id,
            fertilizer_id,
            quantity,
            total_amount,
            sale_date
        )
        VALUES(?,?,?,?,?,?,?)
    """, (
        employee,
        state,
        district,
        fertilizer_id,
        quantity,
        total,
        date
    ))

conn.commit()
conn.close()

print("5000 Sales Records Inserted Successfully.")